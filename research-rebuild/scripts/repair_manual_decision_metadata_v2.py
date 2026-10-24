#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Synchronize human decision metadata with the read-only v2 corpus.

The article ID is the stable key.  This repair only refreshes the copied
title field; it does not alter any topic decision, status, basis, or note.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CORPUS = ROOT / "sooon-q9adg-articles-v2.jsonl"
MANUAL = ROOT / "research-rebuild/data/print-topic-manual-decisions-v2.csv"


def load_titles() -> dict[str, str]:
    titles: dict[str, str] = {}
    with CORPUS.open(encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                row = json.loads(line)
                if row.get("id"):
                    titles[str(row["id"])] = str(row.get("title") or "")
    return titles


def main() -> int:
    titles = load_titles()
    with MANUAL.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        rows = list(reader)
        fields = list(reader.fieldnames or [])
    changed = 0
    missing = []
    for row in rows:
        aid = row.get("id", "")
        if aid not in titles:
            missing.append(aid)
            continue
        title = titles[aid]
        if row.get("title", "") != title:
            row["title"] = title
            changed += 1
    if missing:
        raise SystemExit(f"manual IDs missing from corpus: {len(missing)}")
    with MANUAL.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    print(f"updated_titles={changed} rows={len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
