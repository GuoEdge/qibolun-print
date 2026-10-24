#!/usr/bin/env python3
"""Export the selected Round 94 source articles in batch order."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
BATCH = REPORTS / "live-manual-budget-batch-v2-round94-90k.csv"
CORPUS = ROOT / "sooon-q9adg-articles-v2.jsonl"
OUT = REPORTS / "round94-fulltext.json"

with BATCH.open(encoding="utf-8-sig", newline="") as fh:
    batch = list(csv.DictReader(fh))
articles = {}
with CORPUS.open(encoding="utf-8") as fh:
    for line in fh:
        if line.strip():
            row = json.loads(line)
            if row.get("id"):
                articles[str(row["id"])] = row

assert len(batch) == 50
assert len({row["id"] for row in batch}) == len(batch)
missing = [row["id"] for row in batch if row["id"] not in articles]
assert not missing, f"batch IDs absent from corpus: {missing}"

out = []
for selected in batch:
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

assert sum(len(row["text"]) for row in out) == 85464
OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps({
    "records": len(out),
    "body_chars": sum(len(row["text"]) for row in out),
    "max_body_chars": max(len(row["text"]) for row in out),
    "output": str(OUT),
}, ensure_ascii=False, indent=2))
