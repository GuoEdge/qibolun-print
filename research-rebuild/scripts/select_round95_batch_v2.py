#!/usr/bin/env python3
"""Select and export a bounded, queue-ordered Round 95 batch."""
import csv
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
QUEUE = REPORTS / "live-manual-classification-queue-v2.csv"
BATCH = REPORTS / "live-manual-budget-batch-v2-round95-90k.csv"
FULLTEXT = REPORTS / "round95-fulltext.json"
CORPUS = ROOT / "sooon-q9adg-articles-v2.jsonl"
SELECTOR = ROOT / "research-rebuild/scripts/select_live_manual_batch_v2.py"

subprocess.run([
    sys.executable, str(SELECTOR), "--queue", str(QUEUE), "--out", str(BATCH),
    "--target-count", "50", "--offset", "0", "--text-budget", "90000",
], check=True)

with BATCH.open(encoding="utf-8-sig", newline="") as fh:
    batch = list(csv.DictReader(fh))
articles = {}
with CORPUS.open(encoding="utf-8") as fh:
    for line in fh:
        if line.strip():
            row = json.loads(line)
            if row.get("id"):
                articles[str(row["id"])] = row

assert batch and len(batch) <= 50
ids = [row["id"] for row in batch]
assert len(ids) == len(set(ids))
assert not any(int(row.get("deepseek_image_count") or 0) for row in batch)
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
body_chars = sum(len(row["text"]) for row in out)
assert body_chars <= 90000
FULLTEXT.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps({
    "records": len(out), "body_chars": body_chars,
    "max_body_chars": max(map(lambda row: len(row["text"]), out)),
    "first_ordinal": out[0]["source_ordinal"], "last_ordinal": out[-1]["source_ordinal"],
    "output": str(FULLTEXT),
}, ensure_ascii=False, indent=2))
