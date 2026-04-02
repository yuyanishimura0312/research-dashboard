#!/bin/bash
# Update research dashboard digests, embeddings, and AI analysis
# Run periodically to keep content analysis fresh
# Usage: ./update-digests.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

echo "$(date): Starting digest update..."

# Generate digests for new entries (only entries without digest)
python3 generate_digests.py 2>&1

# Regenerate embeddings
python3 generate_embeddings.py 2>&1

# Generate AI analysis (weekly: only on Mondays, or if analysis.json is missing)
ANALYSIS_JSON="$SCRIPT_DIR/analysis.json"
if [ ! -f "$ANALYSIS_JSON" ] || [ "$(date +%u)" = "1" ]; then
    echo "$(date): Generating AI analysis..."
    python3 generate_analysis.py 2>&1
fi

# Check if data changed
if git diff --quiet data.json data.js embeddings.js analysis.json analysis.js 2>/dev/null; then
    echo "$(date): No changes to push"
    exit 0
fi

# Commit and push
git add data.json data.js embeddings.js analysis.json analysis.js
git commit -m "chore: auto-update digests, embeddings, and AI analysis

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>"
git push

echo "$(date): Update complete and pushed"
