#!/usr/bin/env python3
"""Extract ordered article bodies for a selected manual-review round."""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CORPUS = ROOT / "sooon-q9adg-articles-v2.jsonl"
REPORTS = ROOT / "research-rebuild/reports"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--round", type=int, required=True)
    parser.add_argument("--selection", type=Path)
    args = parser.parse_args()
    selection = args.selection or REPORTS / f"round{args.round}-selection.csv"
    batch = read_csv(selection)

    corpus: dict[str, dict] = {}
    with CORPUS.open(encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                row = json.loads(line)
                corpus[str(row["id"])] = row

    out: list[dict[str, object]] = []
    for row in batch:
        article = corpus.get(row["id"])
        if article is None:
            raise KeyError(f"article missing from corpus: {row['id']}")
        text = str(article.get("text") or "")
        expected = int(row.get("body_char_count") or 0)
        if len(text) != expected:
            raise ValueError(f"body length mismatch for {row['id']}: {len(text)} != {expected}")
        out.append({
            "source_ordinal": int(row.get("source_ordinal") or 0),
            "id": row["id"],
            "title": row["title"],
            "question": row.get("question", ""),
            "body_char_count": expected,
            "text": text,
        })

    target = REPORTS / f"round{args.round}-fulltext.json"
    target.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({
        "round": args.round,
        "records": len(out),
        "body_chars": sum(len(str(row["text"])) for row in out),
        "output": str(target),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
