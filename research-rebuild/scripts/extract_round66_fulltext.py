#!/usr/bin/env python3
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BATCH = ROOT / "research-rebuild/reports/live-manual-short-batch-v2-round66-short50.csv"
CORPUS = ROOT / "sooon-q9adg-articles-v2.jsonl"
OUT = ROOT / "research-rebuild/reports/round66-fulltext.json"


def collect(node):
    if not isinstance(node, dict):
        return ""
    if node.get("type") == "text":
        return str(node.get("text") or "")
    if node.get("type") == "linebreak":
        return "\n"
    return "".join(collect(child) for child in node.get("children") or [])


with BATCH.open(encoding="utf-8-sig", newline="") as fh:
    batch = list(csv.DictReader(fh))
ids = {row["id"] for row in batch}
found = {}
with CORPUS.open(encoding="utf-8") as fh:
    for line in fh:
        article = json.loads(line)
        aid = article.get("id")
        if aid not in ids:
            continue
        lexical = article.get("lexical")
        if isinstance(lexical, str):
            try:
                lexical = json.loads(lexical)
            except json.JSONDecodeError:
                lexical = {}
        found[aid] = {
            "id": aid,
            "title": article.get("title", ""),
            "text": article.get("text") or collect((lexical or {}).get("root") or {}),
        }

assert len(batch) == len(found) == 50, (len(batch), len(found))
out = [found[row["id"]] for row in batch]
assert len({row["id"] for row in out}) == 50
assert all(len(article["text"]) <= int(row["body_char_count"]) for article, row in zip(out, batch))
OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps({
    "count": len(out),
    "body_chars": sum(len(article["text"]) for article in out),
    "max_chars": max(len(article["text"]) for article in out),
    "min_chars": min(len(article["text"]) for article in out),
    "unique_ids": len({article["id"] for article in out}),
}, ensure_ascii=False, indent=2))
