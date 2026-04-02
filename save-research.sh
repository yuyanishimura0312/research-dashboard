#!/bin/bash
# save-research.sh -- リサーチ結果をダッシュボードに保存するスクリプト
# 使い方:
#   ./save-research.sh --title "タイトル" --summary "要約" --tags "tag1,tag2" [--category "カテゴリ"] [--source "URL"] [--status "investigating|reading|organized|done"]

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
DATA_JSON="$SCRIPT_DIR/data.json"
DATA_JS="$SCRIPT_DIR/data.js"

# Initialize data.json if missing
if [ ! -f "$DATA_JSON" ]; then
  echo "[]" > "$DATA_JSON"
fi

# Parse arguments
TITLE=""
CATEGORY=""
SOURCE=""
SUMMARY=""
TAGS=""
STATUS="investigating"
CONTENT=""
CONTENT_FILE=""

while [[ $# -gt 0 ]]; do
  case $1 in
    --title)        TITLE="$2";        shift 2 ;;
    --category)     CATEGORY="$2";     shift 2 ;;
    --source)       SOURCE="$2";       shift 2 ;;
    --summary)      SUMMARY="$2";      shift 2 ;;
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
export DATA_JSON DATA_JS TITLE CATEGORY SOURCE SUMMARY TAGS STATUS CONTENT

# Use Python3 to safely manipulate JSON (no jq dependency)
python3 << 'PYEOF'
import json, sys, os, time, random, string

data_json = os.environ.get("DATA_JSON", "data.json")
data_js = os.environ.get("DATA_JS", "data.js")
title = os.environ.get("TITLE", "")
category = os.environ.get("CATEGORY", "")
source = os.environ.get("SOURCE", "")
summary = os.environ.get("SUMMARY", "")
tags_raw = os.environ.get("TAGS", "")
status = os.environ.get("STATUS", "investigating")
content = os.environ.get("CONTENT", "")

# Load existing data
try:
    with open(data_json, "r", encoding="utf-8") as f:
        data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    data = []

# Generate ID
entry_id = hex(int(time.time()))[2:] + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))

# Parse tags
tags = [t.strip() for t in tags_raw.split(",") if t.strip()] if tags_raw else []

# Create entry
from datetime import datetime, timezone
now = datetime.now(timezone.utc).isoformat()

entry = {
    "id": entry_id,
    "title": title,
    "category": category,
    "status": status,
    "source": source,
    "summary": summary,
    "tags": tags,
    "createdAt": now,
    "updatedAt": now,
}
if content:
    entry["content"] = content

data.append(entry)

# Save data.json
with open(data_json, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Regenerate data.js
with open(data_js, "w", encoding="utf-8") as f:
    f.write("// Auto-generated from data.json -- do not edit by hand\n")
    f.write("window.RESEARCH_DATA = ")
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write(";\n")

print(f"Saved: {title} (id: {entry_id})")
PYEOF

# Regenerate embeddings if generate_embeddings.py exists
EMBED_SCRIPT="$SCRIPT_DIR/generate_embeddings.py"
if [ -f "$EMBED_SCRIPT" ]; then
  echo "Regenerating embeddings..."
  python3 "$EMBED_SCRIPT"
fi

# Generate content digest for new entry
DIGEST_SCRIPT="$SCRIPT_DIR/generate_digests.py"
if [ -f "$DIGEST_SCRIPT" ]; then
  echo "Generating content digest for new entry..."
  python3 "$DIGEST_SCRIPT" --limit 5 2>&1 || true
fi
