#!/usr/bin/env python3
"""Repair stale human-review wording left by the Round116 migration.

Only review-note prose is changed.  IDs, topics, statuses, source order and
the raw corpus remain untouched.
"""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "research-rebuild/data/print-topic-manual-decisions-v2.csv"

REPLACEMENTS = {
    "地塔": ("主体心理和地方产业例证为副轴；图片未独立复核，保留 provisional", "主体心理和地方产业例证为副轴；视觉复核完成，专题未改变"),
    "世交": ("家族与物质往来是友谊机制；原文含 3 张图片，图片尚未独立复核", "家族与物质往来是友谊机制；3 张图片已完成视觉复核，专题未改变"),
    "三碗不过岗": ("技术工程和市场为副轴；后续复核产品图片材料", "技术工程和市场为副轴；正文完整但保留 provisional，待技术产品论证与事实边界复核；无图片材料"),
}


def main() -> None:
    with PATH.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        fields = list(reader.fieldnames or [])
        rows = list(reader)
    changed = []
    for row in rows:
        title = row.get("title", "")
        if title not in REPLACEMENTS:
            continue
        old, new = REPLACEMENTS[title]
        note = row.get("review_note", "")
        if old not in note:
            raise ValueError(f"expected stale wording not found for {title!r}")
        row["review_note"] = note.replace(old, new, 1)
        changed.append(title)
    if sorted(changed) != sorted(REPLACEMENTS):
        raise ValueError(f"changed={changed!r}")
    temporary = PATH.with_suffix(PATH.suffix + ".tmp")
    with temporary.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    temporary.replace(PATH)
    print({"changed": changed})


if __name__ == "__main__":
    main()
