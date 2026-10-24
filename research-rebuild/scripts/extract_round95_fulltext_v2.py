#!/usr/bin/env python3
"""Export and verify the bounded Round 95 full-text batch."""
import csv
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
CORPUS = ROOT / "sooon-q9adg-articles-v2.jsonl"

parser = argparse.ArgumentParser()
parser.add_argument("--round", type=int, default=95)
args = parser.parse_args()
BATCH = REPORTS / f"live-manual-budget-batch-v2-round{args.round}-90k.csv"
FULLTEXT = REPORTS / f"round{args.round}-fulltext.json"

with BATCH.open(encoding="utf-8-sig", newline="") as fh:
    batch = list(csv.DictReader(fh))
articles = {}
with CORPUS.open(encoding="utf-8") as fh:
    for line in fh:
        if line.strip():
            article = json.loads(line)
            if article.get("id"):
                articles[str(article["id"])] = article

assert 0 < len(batch) <= 50
ids = [row["id"] for row in batch]
assert len(ids) == len(set(ids))
out = []
for selected in batch:
    assert int(selected.get("deepseek_image_count") or 0) == 0
    source = articles[selected["id"]]
    assert source.get("title", "") == selected["title"]
    text = source.get("text") or ""
    assert len(text) == int(selected["body_char_count"])
    out.append({
        "source_ordinal": int(selected["source_ordinal"]),
        "id": selected["id"],
        "title": source.get("title", ""),
        "question": source.get("question", ""),
        "text": text,
    })

body_chars = sum(len(row["text"]) for row in out)
assert body_chars <= 90000
FULLTEXT.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps({
    "records": len(out),
    "body_chars": body_chars,
    "max_body_chars": max(len(row["text"]) for row in out),
    "first_ordinal": out[0]["source_ordinal"],
    "last_ordinal": out[-1]["source_ordinal"],
    "output": str(FULLTEXT),
}, ensure_ascii=False, indent=2))
