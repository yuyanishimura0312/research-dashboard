#!/bin/bash
# Update research dashboard digests and push to GitHub
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

# Check if data changed
if git diff --quiet data.json data.js embeddings.js 2>/dev/null; then
    echo "$(date): No changes to push"
    exit 0
fi

# Commit and push
git add data.json data.js embeddings.js
git commit -m "chore: auto-update content digests and embeddings

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>"
git push

echo "$(date): Digest update complete and pushed"
