#!/usr/bin/env python3
"""Generate deep content digests for research dashboard entries.

Reads each research entry's full content/summary and uses Claude API
to extract essential insights, key arguments, and cross-cutting themes.
Saves digests back to data.json for use in dashboard analysis.

Usage:
  python3 generate_digests.py           # Process entries without digests
  python3 generate_digests.py --force   # Regenerate all digests
  python3 generate_digests.py --limit N # Process at most N entries
"""

import json
import os
import sys
import subprocess
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_JSON = os.path.join(SCRIPT_DIR, "data.json")

# Minimum content length to justify digest generation
MIN_CONTENT_LEN = 200


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


def save_data(data):
    with open(DATA_JSON, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(data)} entries to {DATA_JSON}")


def get_text_for_digest(entry):
    """Extract the best available text from an entry."""
    content = entry.get("content", "")
    summary = entry.get("summary", "")
    title = entry.get("title", "")
    category = entry.get("category", "")
    tags = ", ".join(entry.get("tags", []))

    # Prefer content, fall back to summary
    main_text = content if len(content) > len(summary) else summary
    if len(main_text) < MIN_CONTENT_LEN:
        return None

    # Truncate very long content to stay within token limits
    if len(main_text) > 30000:
        main_text = main_text[:30000] + "\n\n[...truncated...]"

    return f"タイトル: {title}\nカテゴリ: {category}\nタグ: {tags}\n\n{main_text}"


def generate_digest(text, api_key):
    """Call Claude API to generate a deep content digest."""
    import anthropic

    client = anthropic.Anthropic(api_key=api_key)

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1500,
        messages=[
            {
                "role": "user",
                "content": f"""以下のリサーチ内容を深く読み込み、本質的なダイジェストを生成してください。

要件:
1. **核心的洞察** (1-3文): このリサーチの最も重要な発見・主張は何か
2. **構造的理解** (2-4文): どのような問題構造・因果関係・メカニズムが示されているか
3. **実践的含意** (1-2文): 実務者・意思決定者にとっての意味は何か
4. **未解決の問い** (1-2項目): このリサーチが提起する、さらに探究すべき問い
5. **関連キーワード** (3-5語): 表面的なタグではなく、内容の本質を表す概念

注意: 表面的な要約ではなく、内容の本質的な理解に基づいた分析を行ってください。

---
{text}
---

JSON形式で出力してください:
{{"core_insight": "...", "structure": "...", "implications": "...", "open_questions": ["...", "..."], "deep_keywords": ["...", "..."]}}"""
            }
        ],
    )

    # Parse JSON from response
    resp_text = response.content[0].text.strip()
    # Handle markdown code blocks
    if resp_text.startswith("```"):
        resp_text = resp_text.split("\n", 1)[1].rsplit("```", 1)[0].strip()

    try:
        return json.loads(resp_text)
    except json.JSONDecodeError:
        # Try to extract JSON from response
        import re
        match = re.search(r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}', resp_text, re.DOTALL)
        if match:
            return json.loads(match.group())
        print(f"  WARNING: Could not parse JSON from response")
        return None


def main():
    force = "--force" in sys.argv
    limit = None
    if "--limit" in sys.argv:
        idx = sys.argv.index("--limit")
        if idx + 1 < len(sys.argv):
            limit = int(sys.argv[idx + 1])

    api_key = get_api_key()
    if not api_key:
        print("ERROR: No Anthropic API key found")
        sys.exit(1)

    data = load_data()
    print(f"Loaded {len(data)} entries")

    # Find entries that need digests
    to_process = []
    for entry in data:
        text = get_text_for_digest(entry)
        if text is None:
            continue
        if not force and entry.get("digest"):
            continue
        to_process.append((entry, text))

    if limit:
        to_process = to_process[:limit]

    print(f"Entries to process: {len(to_process)}")

    if not to_process:
        print("Nothing to process")
        return

    processed = 0
    errors = 0

    for entry, text in to_process:
        title = entry.get("title", "")[:50]
        print(f"  [{processed + 1}/{len(to_process)}] {title}...")

        try:
            digest = generate_digest(text, api_key)
            if digest:
                entry["digest"] = digest
                processed += 1
            else:
                errors += 1
        except Exception as e:
            print(f"    ERROR: {e}")
            errors += 1
            time.sleep(2)  # Back off on errors
            continue

        # Rate limiting: ~50 requests/minute for Sonnet
        if processed % 10 == 0:
            time.sleep(1)

    # Save updated data
    save_data(data)

    # Regenerate data.js
    datajs_path = os.path.join(SCRIPT_DIR, "data.js")
    with open(datajs_path, "w") as f:
        f.write(f"const RESEARCH_DATA = {json.dumps(data, ensure_ascii=False)};\n")
    print(f"Written {datajs_path}")

    print(f"\nDone: {processed} digests generated, {errors} errors")


if __name__ == "__main__":
    main()
