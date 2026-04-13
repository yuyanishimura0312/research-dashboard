#!/bin/bash
# save-report.sh -- ホワイトペーパー形式レポートをダッシュボードに保存するスクリプト
# 使い方:
#   ./save-report.sh --title "タイトル" --content-file report.md [--subtitle "サブタイトル"] \
#     [--category "カテゴリ"] [--tags "tag1,tag2"] [--status "draft|published"]
#
# レポート本文はMarkdownで記述。特殊記法:
#   :::pullquote ... :::     → 強調フレーズ
#   :::keyconcept[名前] ... ::: → キーコンセプトボックス

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
DATA_JSON="$SCRIPT_DIR/reports.json"
DATA_JS="$SCRIPT_DIR/reports.js"

# Initialize reports.json if missing
if [ ! -f "$DATA_JSON" ]; then
  echo "[]" > "$DATA_JSON"
fi

# Parse arguments
TITLE=""
SUBTITLE=""
CATEGORY=""
TAGS=""
STATUS="draft"
CONTENT=""
CONTENT_FILE=""

while [[ $# -gt 0 ]]; do
  case $1 in
    --title)        TITLE="$2";        shift 2 ;;
    --subtitle)     SUBTITLE="$2";     shift 2 ;;
    --category)     CATEGORY="$2";     shift 2 ;;
    --tags)         TAGS="$2";         shift 2 ;;
    --status)       STATUS="$2";       shift 2 ;;
    --content)      CONTENT="$2";      shift 2 ;;
    --content-file) CONTENT_FILE="$2"; shift 2 ;;
    *) echo "Unknown option: $1"; exit 1 ;;
  esac
done

if [ -z "$TITLE" ]; then
  echo "Error: --title is required"
  exit 1
fi

# If --content-file is given, read content from that file
if [ -n "$CONTENT_FILE" ] && [ -f "$CONTENT_FILE" ]; then
  CONTENT="$(cat "$CONTENT_FILE")"
fi

# Export for Python
export DATA_JSON DATA_JS TITLE SUBTITLE CATEGORY TAGS STATUS CONTENT

# Use Python3 to safely manipulate JSON
python3 << 'PYEOF'
import json, os, time, random, string
from datetime import datetime, timezone

data_json = os.environ.get("DATA_JSON", "reports.json")
data_js = os.environ.get("DATA_JS", "reports.js")
title = os.environ.get("TITLE", "")
subtitle = os.environ.get("SUBTITLE", "")
category = os.environ.get("CATEGORY", "")
tags_raw = os.environ.get("TAGS", "")
status = os.environ.get("STATUS", "draft")
content = os.environ.get("CONTENT", "")

# Load existing data
try:
    with open(data_json, "r", encoding="utf-8") as f:
        data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    data = []

# Generate ID
entry_id = "rpt_" + hex(int(time.time()))[2:] + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))

# Parse tags
tags = [t.strip() for t in tags_raw.split(",") if t.strip()] if tags_raw else []

now = datetime.now(timezone.utc).isoformat()

entry = {
    "id": entry_id,
    "title": title,
    "subtitle": subtitle,
    "category": category,
    "tags": tags,
    "status": status,
    "content": content,
    "createdAt": now,
    "updatedAt": now,
}

data.append(entry)

# Save reports.json
with open(data_json, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Regenerate reports.js
with open(data_js, "w", encoding="utf-8") as f:
    f.write("// Auto-generated from reports.json -- do not edit by hand\n")
    f.write("window.REPORTS_DATA = ")
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write(";\n")

print(f"Saved report: {title} (id: {entry_id})")
PYEOF
