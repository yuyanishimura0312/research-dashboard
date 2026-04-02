#!/usr/bin/env python3
"""Generate cross-cutting analysis of research dashboard entries.

Reads all research entries from data.json, groups them by structural category,
uses Claude API for per-category analysis then cross-category synthesis,
and outputs analysis.json + analysis.js for the dashboard.

Usage:
  python3 generate_analysis.py           # Full generation
  python3 generate_analysis.py --dry-run # Show stats only, no API calls
"""

import json
import os
import re
import subprocess
import sys
import time
from collections import Counter, defaultdict
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_JSON = os.path.join(SCRIPT_DIR, "data.json")
ANALYSIS_JSON = os.path.join(SCRIPT_DIR, "analysis.json")
ANALYSIS_JS = os.path.join(SCRIPT_DIR, "analysis.js")

MODEL = "claude-sonnet-4-20250514"
# Rate limiting: sleep 1s every N calls
RATE_LIMIT_INTERVAL = 5


def get_api_key():
    """Retrieve Anthropic API key from macOS Keychain."""
    try:
        result = subprocess.run(
            ["security", "find-generic-password", "-s", "ANTHROPIC_API_KEY", "-w"],
            capture_output=True, text=True, check=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return os.environ.get("ANTHROPIC_API_KEY")


def load_data():
    with open(DATA_JSON, "r") as f:
        return json.load(f)


# ---------------------------------------------------------------------------
# classify_entry — ported from app.html classifyEntry()
# ---------------------------------------------------------------------------

def classify_entry(d):
    """Classify a research entry into one of ~20 structural categories.

    Port of the JavaScript classifyEntry() function from app.html.
    Priority-ordered rules based on tags, title, and original category.
    """
    raw_tags = [t.lower() for t in (d.get("tags") or [])]
    tags = set(raw_tags)
    title = (d.get("title") or "").lower()
    cat = (d.get("category") or "").lower()
    # summary not used in current rules but kept for parity
    # summary = (d.get("summary") or "").lower()

    def has(*kws):
        return any(
            k.lower() in tags or k.lower() in title
            for k in kws
        )

    def tag_has(*kws):
        return any(k.lower() in tags for k in kws)

    # 1. esse-sense
    if has('esse-sense', 'エッセンス') and (
        has('記事', '戦略', '経営', 'EC', 'CRM') or 'ビジネス' in cat
    ):
        return 'esse-sense・事業'

    # 2. 京都大学
    if tag_has('京都大学', '京都大学beyond2050'):
        return '京都大学・連携プロジェクト'

    # 3. フォーラム・対話・イベント
    if tag_has('フォーラム', 'カンファレンス', 'イベントレポート',
               '未来カンファレンス', 'イベント', 'ヒアリング', '取材準備'):
        return 'フォーラム・対話・イベント'

    # 4. 社会的共通資本
    if has('社会的共通資本'):
        return '社会的共通資本'

    # 5. 未来洞察・シナリオ
    if has('シナリオプランニング', 'CLA', 'PESTLE', '未来洞察',
           'フォーサイト', 'SINIC', 'メタ分析', 'メタ解析'):
        return '未来洞察・シナリオ'

    # 6. 未来学・理論  (JS: cat.includes('未来学') || tagHas(...) && !cat.includes('人類学'))
    if '未来学' in cat or (tag_has('未来学', '書籍要約') and '人類学' not in cat):
        return '未来学・理論'

    # 7. 未来の人類学
    if has('未来の人類学'):
        return '未来の人類学'

    # 8. 人類学
    if cat == '人類学' or (
        tag_has('人類学', 'エスノグラフィー', 'フィールドワーク', '身体性', '神話')
        and 'テクノロジー' not in cat
    ):
        return '人類学'

    # 9. デジタルツール・プラットフォーム (three sub-rules)
    if (has('ツール', 'プラットフォーム', 'SaaS', 'membership', 'Stripe', 'ベンチマーク')
        and ('ツール' in cat or 'デジタル' in cat or 'デザイン' in cat
             or 'ベンチマーク' in cat
             or has('比較', '調査ツール', 'リサーチツール'))):
        return 'デジタルツール・プラットフォーム'
    if has('MCP', 'Claude Code', 'ナレッジグラフ', 'リサーチダッシュボード', 'データ可視化'):
        return 'デジタルツール・プラットフォーム'
    if ('ツール調査' in cat or 'デジタルツール' in cat
            or 'デザイン調査' in cat or 'ベンチマーク' in cat):
        return 'デジタルツール・プラットフォーム'

    # 10. AI・生成AI
    if tag_has('ai秘書', 'ai') and (
        has('AI秘書', 'LLM', 'Claude', 'GPT') or 'ai' in title
    ):
        if 'ai' in cat or bool(re.match(r'^ai|ai[活導秘]|生成ai', title, re.IGNORECASE)):
            return 'AI・生成AI'

    # 11. コミュニティ・NPO
    if has('NPO', 'メンバーシップ', 'コミュニティ', '会員', '市民社会', '相互扶助'):
        return 'コミュニティ・NPO'
    if 'npo' in cat or '市民' in cat:
        return 'コミュニティ・NPO'

    # 12. 経営・組織・戦略
    if ('経営' in cat or 'ビジネス' in cat or '事業戦略' in cat
            or '組織' in cat or cat == 'market-research'):
        return '経営・組織・戦略'
    if tag_has('経営', '戦略', '事業戦略', '知的資本') and 'ソーシャル' not in cat:
        return '経営・組織・戦略'

    # 13. 財団・ガバナンス
    if has('財団', 'ガバナンス') and not tag_has('京都大学'):
        return '財団・ガバナンス'

    # 14. 教育・人材育成
    if has('教育', 'カリキュラム', '大学院', 'プログラム調査'):
        return '教育・人材育成'

    # 15. 環境・サステナビリティ
    if has('環境', 'サステナビリティ', '気候変動', 'エネルギー'):
        return '環境・サステナビリティ'

    # 16. 観光・地域・ウェルビーイング
    if has('観光', '地域', 'ウェルビーイング', 'パナソニック'):
        return '観光・地域・ウェルビーイング'

    # 17. 建築・都市
    if has('建築', '都市', 'インフォーマル'):
        return '建築・都市'

    # 18. ソーシャルイノベーション
    if 'ソーシャルイノベーション' in cat or tag_has(
        'ソーシャルイノベーション', 'ソーシャルイノベーションの歴史と背景'
    ):
        return 'ソーシャルイノベーション'

    # 19. 学術研究・科学
    if '学術' in cat or tag_has('学術', '研究', '科学'):
        return '学術研究・科学'

    # 20. テクノロジー・イノベーション
    if 'テクノロジー' in cat:
        return 'テクノロジー・イノベーション'

    # Fallback
    if cat == 'リサーチ':
        return 'ソーシャルイノベーション'
    return d.get("category") or '未分類'


# ---------------------------------------------------------------------------
# Build per-category summaries
# ---------------------------------------------------------------------------

def build_category_summaries(data):
    """Group entries by structural category and build summaries for each."""
    groups = defaultdict(list)
    for entry in data:
        cat = classify_entry(entry)
        groups[cat].append(entry)

    summaries = {}
    for cat_name, entries in sorted(groups.items(), key=lambda x: -len(x[1])):
        # Date range
        dates = [e.get("createdAt", "") for e in entries if e.get("createdAt")]
        dates_sorted = sorted(dates) if dates else []
        date_range = f"{dates_sorted[0][:10]} ~ {dates_sorted[-1][:10]}" if dates_sorted else "不明"

        # Collect digest fields
        core_insights = []
        deep_keywords = set()
        open_questions = []
        for e in entries:
            dg = e.get("digest")
            if not dg:
                continue
            ci = dg.get("core_insight", "")
            if ci:
                core_insights.append(ci)
            for kw in dg.get("deep_keywords", []):
                deep_keywords.add(kw)
            for q in dg.get("open_questions", []):
                open_questions.append(q)

        # Tag frequency
        tag_counter = Counter()
        for e in entries:
            for t in e.get("tags", []):
                tag_counter[t] += 1
        top_tags = tag_counter.most_common(15)

        # Recent titles (up to 10)
        sorted_entries = sorted(entries, key=lambda e: e.get("createdAt", ""), reverse=True)
        recent_titles = [e.get("title", "") for e in sorted_entries[:10]]

        summaries[cat_name] = {
            "count": len(entries),
            "date_range": date_range,
            "core_insights": core_insights[:30],  # cap to keep prompt reasonable
            "deep_keywords": sorted(deep_keywords)[:40],
            "open_questions": open_questions[:20],
            "top_tags": top_tags,
            "recent_titles": recent_titles,
        }

    return summaries


# ---------------------------------------------------------------------------
# Phase 1: Per-category analysis via Claude API
# ---------------------------------------------------------------------------

def analyze_category(cat_name, summary, client, call_count):
    """Send a single category summary to Claude for analysis."""
    # Build a concise prompt with the category data
    prompt_parts = [
        f"## カテゴリ: {cat_name}",
        f"エントリ数: {summary['count']}",
        f"期間: {summary['date_range']}",
        "",
        "### 主要タグ (頻度順):",
        ", ".join(f"{t}({n})" for t, n in summary['top_tags']),
        "",
    ]

    if summary['core_insights']:
        prompt_parts.append("### 核心的洞察 (各エントリのdigestから):")
        for ci in summary['core_insights']:
            # Truncate very long insights
            prompt_parts.append(f"- {ci[:300]}")
        prompt_parts.append("")

    if summary['deep_keywords']:
        prompt_parts.append("### 深層キーワード:")
        prompt_parts.append(", ".join(summary['deep_keywords']))
        prompt_parts.append("")

    if summary['open_questions']:
        prompt_parts.append("### 未解決の問い:")
        for q in summary['open_questions'][:15]:
            prompt_parts.append(f"- {q[:200]}")
        prompt_parts.append("")

    prompt_parts.append("### 直近のエントリタイトル:")
    for t in summary['recent_titles']:
        prompt_parts.append(f"- {t}")

    category_data = "\n".join(prompt_parts)

    response = client.messages.create(
        model=MODEL,
        max_tokens=2000,
        messages=[{
            "role": "user",
            "content": f"""以下はリサーチダッシュボードの「{cat_name}」カテゴリのサマリーです。
このカテゴリの研究動向を分析してください。

{category_data}

JSON形式で出力してください:
{{
  "category_narrative": "このカテゴリの研究全体の特徴と動向（200-400文字）",
  "key_themes": ["テーマ1", "テーマ2", "テーマ3"],
  "maturity": "探索段階|蓄積段階|成熟段階|転換段階",
  "research_density": "高密度|中密度|低密度",
  "notable_gaps": "このカテゴリで不足している視点や調査（100-200文字）",
  "cross_category_links": ["関連しそうな他カテゴリ名1", "関連しそうな他カテゴリ名2"]
}}"""
        }],
    )

    resp_text = response.content[0].text.strip()
    # Handle markdown code blocks
    if resp_text.startswith("```"):
        resp_text = resp_text.split("\n", 1)[1].rsplit("```", 1)[0].strip()

    try:
        return json.loads(resp_text)
    except json.JSONDecodeError:
        match = re.search(r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}', resp_text, re.DOTALL)
        if match:
            return json.loads(match.group())
        print(f"  WARNING: Could not parse JSON for {cat_name}")
        return None


# ---------------------------------------------------------------------------
# Phase 2: Cross-category synthesis via Claude API
# ---------------------------------------------------------------------------

def synthesize_all(category_analyses, summaries, entry_count, client):
    """Combine all per-category analyses into a cross-cutting synthesis."""
    # Build a structured prompt from all category analyses
    parts = [
        f"リサーチダッシュボードには{entry_count}件の調査エントリがあり、"
        f"{len(category_analyses)}カテゴリに分類されています。\n",
        "以下は各カテゴリの分析結果です:\n",
    ]

    for cat_name, analysis in sorted(category_analyses.items()):
        count = summaries[cat_name]["count"]
        parts.append(f"### {cat_name} ({count}件)")
        if analysis:
            parts.append(f"概要: {analysis.get('category_narrative', 'N/A')}")
            parts.append(f"成熟度: {analysis.get('maturity', 'N/A')}")
            parts.append(f"密度: {analysis.get('research_density', 'N/A')}")
            parts.append(f"不足: {analysis.get('notable_gaps', 'N/A')}")
            themes = analysis.get('key_themes', [])
            if themes:
                parts.append(f"テーマ: {', '.join(themes)}")
            links = analysis.get('cross_category_links', [])
            if links:
                parts.append(f"関連: {', '.join(links)}")
        parts.append("")

    all_categories_text = "\n".join(parts)

    response = client.messages.create(
        model=MODEL,
        max_tokens=6000,
        messages=[{
            "role": "user",
            "content": f"""以下はリサーチダッシュボード全体の分析データです。
これらを統合して、横断的な分析と今後の調査提案を生成してください。

{all_categories_text}

以下のJSON形式で出力してください。全ての文章は日本語で、具体的かつ豊かな内容にしてください:
{{
  "context_analysis": {{
    "narrative": "リサーチ全体の知的景観を描写する文章（500-800文字）。どのような知的探究が行われ、全体としてどんな方向性があるか。",
    "research_trajectory": "時間とともにリサーチの焦点がどう変遷してきたかの分析（300-500文字）",
    "cross_cutting_themes": [
      {{"theme": "テーマ名", "description": "そのテーマの内容（100-150文字）", "entry_count": 概算数}},
      // 5-8テーマ
    ],
    "structural_insights": [
      {{"title": "洞察のタイトル", "insight": "詳細な洞察（150-250文字）"}},
      // 3-5つ
    ]
  }},
  "research_suggestions": [
    {{
      "theme": "提案するカテゴリ/テーマ名",
      "priority": "high または medium",
      "gap_level": "有望な空白地帯 | 発展的探究 | 再調査 | 蓄積あり のいずれか",
      "background": "なぜこのテーマが重要か、既存調査との関係（200-400文字の地の文）",
      "rationale": "具体的にどう調査すべきか、何が得られるか（150-300文字）",
      "key_questions": ["問い1", "問い2"],
      "connections": ["関連カテゴリ1", "関連カテゴリ2"],
      "entry_count": 既存エントリの概算数
    }},
    // 5-7件
  ],
  "key_insights": {{
    "emerging_patterns": "複数カテゴリにまたがって浮上しているパターン（200-300文字）",
    "knowledge_gaps": "全体として不足している知識領域の分析（200-300文字）",
    "convergence_points": "異なる調査領域が交差・収束するポイントの分析（200-300文字）"
  }}
}}"""
        }],
    )

    resp_text = response.content[0].text.strip()
    if resp_text.startswith("```"):
        resp_text = resp_text.split("\n", 1)[1].rsplit("```", 1)[0].strip()

    try:
        return json.loads(resp_text)
    except json.JSONDecodeError:
        # Try to find the outermost JSON object
        depth = 0
        start = resp_text.find("{")
        if start == -1:
            print("  WARNING: No JSON found in synthesis response")
            return None
        for i in range(start, len(resp_text)):
            if resp_text[i] == "{":
                depth += 1
            elif resp_text[i] == "}":
                depth -= 1
                if depth == 0:
                    try:
                        return json.loads(resp_text[start:i + 1])
                    except json.JSONDecodeError:
                        break
        print("  WARNING: Could not parse synthesis JSON")
        return None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    dry_run = "--dry-run" in sys.argv

    data = load_data()
    print(f"Loaded {len(data)} entries from {DATA_JSON}")

    # Build category summaries
    summaries = build_category_summaries(data)
    print(f"\nCategories: {len(summaries)}")
    for cat_name, s in sorted(summaries.items(), key=lambda x: -x[1]["count"]):
        digest_count = len(s["core_insights"])
        print(f"  {cat_name}: {s['count']} entries ({digest_count} with digest), {s['date_range']}")

    if dry_run:
        print(f"\n[DRY RUN] Would make ~{len(summaries) + 1} API calls")
        print(f"  Phase 1: {len(summaries)} category analyses")
        print(f"  Phase 2: 1 cross-category synthesis")
        return

    # Get API key
    api_key = get_api_key()
    if not api_key:
        print("ERROR: No Anthropic API key found")
        sys.exit(1)

    import anthropic
    client = anthropic.Anthropic(api_key=api_key)

    # Phase 1: Per-category analysis
    print(f"\n=== Phase 1: Per-category analysis ({len(summaries)} categories) ===")
    category_analyses = {}
    call_count = 0
    errors = 0

    for i, (cat_name, summary) in enumerate(
        sorted(summaries.items(), key=lambda x: -x[1]["count"])
    ):
        print(f"  [{i + 1}/{len(summaries)}] {cat_name} ({summary['count']} entries)...", end=" ", flush=True)

        try:
            result = analyze_category(cat_name, summary, client, call_count)
            if result:
                category_analyses[cat_name] = result
                print("OK")
            else:
                print("PARSE ERROR")
                errors += 1
        except Exception as e:
            print(f"ERROR: {e}")
            errors += 1
            time.sleep(3)  # back off on errors

        call_count += 1
        # Rate limiting
        if call_count % RATE_LIMIT_INTERVAL == 0:
            time.sleep(1)

    print(f"  Phase 1 complete: {len(category_analyses)} succeeded, {errors} errors")

    # Phase 2: Cross-category synthesis
    print(f"\n=== Phase 2: Cross-category synthesis ===")
    print("  Generating synthesis...", end=" ", flush=True)

    try:
        synthesis = synthesize_all(category_analyses, summaries, len(data), client)
        if synthesis:
            print("OK")
        else:
            print("PARSE ERROR")
            sys.exit(1)
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)

    # Build final output
    output = {
        "generated_at": datetime.now(tz=__import__('datetime').timezone.utc).isoformat(),
        "entry_count": len(data),
        "context_analysis": synthesis.get("context_analysis", {}),
        "research_suggestions": synthesis.get("research_suggestions", []),
        "key_insights": synthesis.get("key_insights", {}),
    }

    # Write analysis.json
    with open(ANALYSIS_JSON, "w") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    print(f"\nWritten {ANALYSIS_JSON}")

    # Write analysis.js
    with open(ANALYSIS_JS, "w") as f:
        f.write(f"window.RESEARCH_ANALYSIS = {json.dumps(output, ensure_ascii=False)};\n")
    print(f"Written {ANALYSIS_JS}")

    print(f"\nDone. {len(output['research_suggestions'])} suggestions generated.")


if __name__ == "__main__":
    main()
