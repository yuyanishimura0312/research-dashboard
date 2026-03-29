#!/usr/bin/env python3
"""
Clean up research dashboard data:
1. Consolidate 19 categories to ~9
2. Generate summaries for empty entries from titles
3. Remove generic "リサーチ" tag where more specific tags exist
4. Save updated data.json and regenerate data.js
"""

import json
import re
from pathlib import Path

DATA_DIR = Path(__file__).parent
DATA_JSON = DATA_DIR / "data.json"
DATA_JS = DATA_DIR / "data.js"

# Category merge map: old -> new
CATEGORY_MERGE = {
    "組織": "組織・財団",
    "AI": "テクノロジー",
    "UI/UX": "テクノロジー",
    "ツール": "テクノロジー",
    "書籍": "書籍・思想",
    "人物調査": "学術",
    "イベント": "リサーチ",  # first merge イベント into リサーチ (will be re-categorized below)
    "メディア": "ビジネス",
    "国際連携": "ビジネス",
    "教育": "学術",
}

# After merging, re-categorize remaining "リサーチ" category entries
# based on title/tag heuristics
def guess_category_for_research(entry):
    """Try to assign a better category for entries currently in 'リサーチ' category."""
    title = entry.get("title", "")
    tags = entry.get("tags", [])
    all_text = title + " " + " ".join(tags)

    # Heuristic rules based on content
    if any(w in all_text for w in ["人類学", "エスノグラフィー", "フィールドワーク", "儀礼", "神話", "文化", "ソングライン", "アボリジニ", "バリ", "沖縄", "聖地"]):
        return "人類学"
    if any(w in all_text for w in ["未来", "フューチャー", "2040", "SINIC", "バイオ・デジタル"]):
        return "未来学"
    if any(w in all_text for w in ["ビジネス", "事業", "デューデリ", "投資", "VC", "市場", "経済", "金融", "企業", "EC", "経営"]):
        return "ビジネス"
    if any(w in all_text for w in ["AI", "テクノロジー", "量子", "ロボ", "デジタル", "VR"]):
        return "テクノロジー"
    if any(w in all_text for w in ["学術", "大学", "研究者", "論文", "学問", "科学", "認知", "ダマシオ", "ブロッホ", "プラトン"]):
        return "学術"
    if any(w in all_text for w in ["財団", "助成", "コンソーシアム"]):
        return "組織・財団"
    if any(w in all_text for w in ["イノベーション", "スタートアップ", "ディープテック"]):
        return "イノベーション"
    if any(w in all_text for w in ["環境", "植物", "自然", "社会"]):
        return "社会・環境"
    if any(w in all_text for w in ["書籍", "思想", "哲学"]):
        return "書籍・思想"
    # Default: keep as リサーチ -> map to 学術 as catch-all
    return "学術"


def generate_summary(title):
    """Generate a brief Japanese summary from the title (under 100 chars)."""
    # Clean up titles that are instructions, not real titles
    if any(w in title for w in ["書き起こし", "書いてください", "フィードバック部分"]):
        return f"「{title[:30]}」に関する作業メモ"

    # Remove date prefixes like "20240326" or "20250927"
    clean = re.sub(r"^\d{8}", "", title).strip()
    if not clean:
        clean = title

    # Remove common suffixes that don't add meaning
    clean = re.sub(r"(作成依頼|作成)$", "", clean).strip()

    # Build summary based on common patterns
    if "調査" in clean or "レポート" in clean or "報告" in clean:
        return f"{clean}の知見をまとめた調査資料"
    if "企画" in clean or "提案" in clean or "構想" in clean:
        return f"{clean}に関する企画・構想の検討資料"
    if "学術的成果" in clean or "学術的意義" in clean:
        return f"{clean}に関する学術的知見の整理"
    if "比較" in clean or "ベンチマーク" in clean:
        return f"{clean}の比較分析をまとめた資料"
    if "戦略" in clean or "事業" in clean or "計画" in clean:
        return f"{clean}に関する戦略・事業検討資料"
    if "研究" in clean or "分析" in clean:
        return f"{clean}に関する研究・分析資料"
    if "要約" in clean or "まとめ" in clean:
        return f"{clean}の要点を整理した資料"
    if "設立" in clean or "設計" in clean:
        return f"{clean}に関する設計・構想資料"
    if "連携" in clean or "ミーティング" in clean:
        return f"{clean}に関する連携・会議資料"
    if "案内" in clean:
        return f"{clean}の概要と詳細情報"

    # Generic fallback
    return f"{clean}に関する調査・考察資料"

    # Truncate if over 100 chars
    if len(summary) > 100:
        summary = summary[:97] + "..."
    return summary


def main():
    with open(DATA_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)

    stats = {
        "total": len(data),
        "categories_merged": 0,
        "research_recategorized": 0,
        "summaries_generated": 0,
        "research_tags_removed": 0,
    }

    for entry in data:
        cat = entry.get("category", "")

        # Step 1: Merge categories
        if cat in CATEGORY_MERGE:
            entry["category"] = CATEGORY_MERGE[cat]
            stats["categories_merged"] += 1
            cat = entry["category"]

        # Step 2: Re-categorize "リサーチ" category entries
        if cat == "リサーチ":
            new_cat = guess_category_for_research(entry)
            entry["category"] = new_cat
            stats["research_recategorized"] += 1

        # Step 3: Generate summaries for empty entries
        if not entry.get("summary", "").strip():
            entry["summary"] = generate_summary(entry.get("title", ""))
            stats["summaries_generated"] += 1

        # Step 4: Remove generic "リサーチ" tag if more specific tags exist
        tags = entry.get("tags", [])
        if "リサーチ" in tags and len(tags) > 1:
            tags.remove("リサーチ")
            entry["tags"] = tags
            stats["research_tags_removed"] += 1

    # Save data.json
    with open(DATA_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Regenerate data.js
    with open(DATA_JS, "w", encoding="utf-8") as f:
        f.write("// Auto-generated from data.json -- do not edit by hand\n")
        f.write("window.RESEARCH_DATA = ")
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write(";\n")

    # Print summary
    print("=" * 50)
    print("Research Dashboard Data Cleanup - Summary")
    print("=" * 50)
    print(f"Total entries: {stats['total']}")
    print(f"Categories merged: {stats['categories_merged']}")
    print(f"'リサーチ' entries re-categorized: {stats['research_recategorized']}")
    print(f"Summaries generated: {stats['summaries_generated']}")
    print(f"'リサーチ' tags removed: {stats['research_tags_removed']}")

    # Final category breakdown
    from collections import Counter
    final_cats = Counter(e.get("category", "") for e in data)
    print(f"\nFinal categories ({len(final_cats)}):")
    for cat, count in final_cats.most_common():
        print(f"  {cat}: {count}")

    print("\nDone. Files updated: data.json, data.js")


if __name__ == "__main__":
    main()
