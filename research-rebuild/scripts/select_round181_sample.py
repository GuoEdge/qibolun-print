#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the 2026-09-26 stratified sample of the 616 official-unmatched articles.

Frame: the 616 local v2-corpus articles whose ``native_assignment_status`` is
``native_unassigned_valid`` (they exist in the local corpus and have no edge in
the official category snapshot).  The official layer must NOT be fabricated for
them; the audit question is only whether their *local* A-topic holds up and
whether their absence from the official inventory is a mere inventory gap or a
sign of a local classification problem.

Strata (framework v2 section 6, "官方覆盖层"):
  * body-length band  (0, 1-99, 100-499, 500-1499, 1500-3999, >=4000)
  * publication year band (2017-2019, 2020-2021, 2022-2023, 2024-2026)
  * current primary print topic A00-A21
  * boundary topics forced into the sample: A00, A09, A14, A17, A19, A21

Allocation: one seed-fixed draw per non-empty (length-band x topic) cell, then
top-up draws to reach the target, and a forced draw for every boundary topic.
The seed and the full cell table are written next to the sample so the draw is
reproducible.
"""
from __future__ import annotations

import csv
import json
import random
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
R = ROOT / "research-rebuild"
OUT = R / "reports/rebuild-20260926/round181"
SEED = 20260926
TARGET = 65
BOUNDARY = ["A00", "A09", "A14", "A17", "A19", "A21"]


def length_band(n: int) -> str:
    if n == 0:
        return "L0_empty"
    if n < 100:
        return "L1_1-99"
    if n < 500:
        return "L2_100-499"
    if n < 1500:
        return "L3_500-1499"
    if n < 4000:
        return "L4_1500-3999"
    return "L5_4000+"


def year_band(date: str) -> str:
    y = int((date or "0000")[:4] or 0)
    if y <= 2019:
        return "Y1_2017-2019"
    if y <= 2021:
        return "Y2_2020-2021"
    if y <= 2023:
        return "Y3_2022-2023"
    return "Y4_2024-2026"


def main() -> int:
    rows = [r for r in csv.DictReader(
        (R / "reports/print-index/print-research-index.csv").open(encoding="utf-8-sig"))
        if r["native_assignment_status"] == "native_unassigned_valid"]
    assert len(rows) == 616, len(rows)

    for r in rows:
        n = int(r["body_char_count"] or 0)
        r["_len"] = length_band(n)
        r["_year"] = year_band(r["published_date"])
        r["_topic"] = r["primary_print_topic"]

    rng = random.Random(SEED)
    cells: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for r in rows:
        cells[(r["_len"], r["_topic"])].append(r)
    for v in cells.values():
        v.sort(key=lambda r: r["id"])

    picked: dict[str, dict] = {}

    def take(cell_key, reason):
        pool = [r for r in cells.get(cell_key, []) if r["id"] not in picked]
        if not pool:
            return None
        r = rng.choice(pool)
        r["_stratum"] = f"{cell_key[0]}|{cell_key[1]}"
        r["_draw"] = reason
        picked[r["id"]] = r
        return r

    # stage 1 — one draw from every non-empty (length x topic) cell
    for key in sorted(cells):
        take(key, "cell_seed")

    # stage 2 — forced coverage of every boundary topic
    for topic in BOUNDARY:
        if not any(r["_topic"] == topic for r in picked.values()):
            keys = sorted(k for k in cells if k[1] == topic)
            for k in keys:
                if take(k, "boundary_forced"):
                    break

    # stage 3 — top up to target, round-robin over the largest cells
    order = sorted(cells, key=lambda k: (-len(cells[k]), k))
    i = 0
    while len(picked) < TARGET and order:
        take(order[i % len(order)], "topup")
        i += 1
        if i > 5000:
            break

    sample = sorted(picked.values(), key=lambda r: (r["source_ordinal"]))
    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT / "round181-sample-frame.csv").open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["id", "title", "source_ordinal", "published_date", "body_char_count",
                    "length_band", "year_band", "primary_print_topic", "stratum", "draw"])
        for r in sample:
            w.writerow([r["id"], r["title"], r["source_ordinal"], r["published_date"],
                        r["body_char_count"], r["_len"], r["_year"], r["_topic"],
                        r["_stratum"], r["_draw"]])
    with (OUT / "round181-ids.csv").open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["id", "title"])
        for r in sample:
            w.writerow([r["id"], r["title"]])

    frame = {
        "seed": SEED, "target": TARGET, "frame_records": len(rows), "sample_records": len(sample),
        "official_layer": "native_unassigned_valid — the official layer must not be fabricated",
        "length_band_counts": dict(Counter(r["_len"] for r in rows)),
        "year_band_counts": dict(Counter(r["_year"] for r in rows)),
        "topic_counts": dict(sorted(Counter(r["_topic"] for r in rows).items())),
        "sample_topic_counts": dict(sorted(Counter(r["_topic"] for r in sample).items())),
        "sample_length_counts": dict(sorted(Counter(r["_len"] for r in sample).items())),
        "sample_year_counts": dict(sorted(Counter(r["_year"] for r in sample).items())),
        "sample_id_count": len({r["id"] for r in sample}),
        "cell_total": len(cells),
        "cells_covered": len({r["_stratum"] for r in sample}),
    }
    (OUT / "round181-sample-frame.json").write_text(
        json.dumps(frame, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(frame, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
