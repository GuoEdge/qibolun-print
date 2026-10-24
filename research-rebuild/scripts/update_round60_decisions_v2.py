#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Apply explicit Round 60 corrections to existing rows by exact batch ID."""
from __future__ import annotations

import csv
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"
BATCH = REPORTS / "live-manual-short-batch-v2-round60-short50.csv"
DECISIONS = REPORTS / "round60-decisions.tsv"
MANUAL = DATA / "print-topic-manual-decisions-v2.csv"


def read_csv(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        r = csv.DictReader(f)
        return list(r.fieldnames or []), list(r)


_, batch = read_csv(BATCH)
fields, rows = read_csv(MANUAL)
with DECISIONS.open(encoding="utf-8-sig", newline="") as f:
    decisions = {r["title"]: r for r in csv.DictReader(f, delimiter="\t")}
ids = {r["id"] for r in batch}
titles = {r["title"] for r in batch}
assert len(ids) == len(titles) == 50 and set(decisions) == titles
by_id = {r["id"]: r for r in rows}
assert ids <= set(by_id), "some Round 60 rows are missing from manual table"
assert len(by_id) == len(rows), "manual table contains duplicate IDs"

for item in batch:
    row = by_id[item["id"]]
    d = decisions[item["title"]]
    assert row["title"] == item["title"]
    row.update({
        "primary_print_topic_code": d["primary"],
        "secondary_print_topic_codes": d["secondary"],
        "classification_status": d["status"],
        "decision_basis": d["basis"],
        "review_note": f"Round 60 full text; {item['body_char_count']} chars including question; batch={BATCH.name}",
        "reviewer": "main-thread",
        "reviewed_at": date.today().isoformat(),
    })

with MANUAL.open("w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(rows)
print(f"updated {len(batch)} existing Round 60 decisions; manual rows unchanged: {len(rows)}")

# Produce a reproducible, compact audit note from the actual full-text batch.
notes = REPORTS / "round60-review-notes.md"
by_title = {r["title"]: r for r in batch}
with notes.open("w", encoding="utf-8", newline="") as f:
    f.write("# Round 60 Review Notes\n\n")
    f.write("50篇短文，分类依据为逐篇完整正文；字符预算以选择器记录的正文+问题长度计。主专题依正文中心，副专题仅在存在明确持续论证时保留。\n\n")
    f.write("|标题|正文+问题字数|主专题|副专题|判定依据|\n|---|---:|---|---|---|\n")
    for item in batch:
        d = decisions[item["title"]]
        f.write(f"|{item['title']}|{item['body_char_count']}|{d['primary']}|{d['secondary']}|{d['basis']}|\n")
