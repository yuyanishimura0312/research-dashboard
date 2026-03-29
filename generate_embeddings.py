#!/usr/bin/env python3
"""Generate embeddings for research dashboard entries.

Uses multilingual-e5-small to create vector representations of each research entry.
Outputs embeddings.js for browser-side cosine similarity search.
"""

import json
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_JSON = os.path.join(SCRIPT_DIR, "data.json")
EMBEDDINGS_JS = os.path.join(SCRIPT_DIR, "embeddings.js")

# Model: multilingual-e5-small (384 dims, ~130MB, good Japanese support)
MODEL_NAME = "intfloat/multilingual-e5-small"


def build_document_text(entry):
    """Combine title, category, summary, and tags into a single searchable string.
    E5 models expect 'passage: ' prefix for documents."""
    parts = []
    if entry.get("title"):
        parts.append(entry["title"])
    if entry.get("category"):
        parts.append(entry["category"])
    if entry.get("summary"):
        # Truncate very long summaries to keep embedding focused
        summary = entry["summary"][:2000]
        parts.append(summary)
    if entry.get("tags"):
        parts.append(" ".join(entry["tags"]))
    return "passage: " + " ".join(parts)


def main():
    # Load research data
    if not os.path.exists(DATA_JSON):
        print("Error: data.json not found", file=sys.stderr)
        sys.exit(1)

    with open(DATA_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)

    print(f"Loaded {len(data)} entries from data.json")

    # Build documents
    ids = [entry["id"] for entry in data]
    docs = [build_document_text(entry) for entry in data]

    # Load model and encode
    from sentence_transformers import SentenceTransformer

    print(f"Loading model: {MODEL_NAME}")
    model = SentenceTransformer(MODEL_NAME)

    print("Generating embeddings...")
    embeddings = model.encode(docs, show_progress_bar=True, normalize_embeddings=True)

    # Build output: mapping from id -> embedding vector
    embeddings_map = {}
    for entry_id, vec in zip(ids, embeddings):
        # Round to 6 decimal places to reduce file size
        embeddings_map[entry_id] = [round(float(v), 6) for v in vec]

    # Write embeddings.js
    with open(EMBEDDINGS_JS, "w", encoding="utf-8") as f:
        f.write("// Auto-generated embeddings — do not edit by hand\n")
        f.write(f"// Model: {MODEL_NAME}, dims: {len(embeddings[0])}\n")
        f.write("window.RESEARCH_EMBEDDINGS = ")
        json.dump(embeddings_map, f, ensure_ascii=False)
        f.write(";\n")

    file_size_mb = os.path.getsize(EMBEDDINGS_JS) / (1024 * 1024)
    print(f"Written {EMBEDDINGS_JS} ({file_size_mb:.1f} MB, {len(embeddings_map)} entries, {len(embeddings[0])} dims)")


if __name__ == "__main__":
    main()
