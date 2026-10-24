#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render extracted evidence packets as a readable review sheet (stdout only)."""
from __future__ import annotations
import argparse, json
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("--packets", type=Path, required=True)
ap.add_argument("--min-chars", type=int, default=0)
ap.add_argument("--max-chars", type=int, default=None)
ap.add_argument("--ids", type=Path, default=None, help="optional CSV with id column to filter/order")
ap.add_argument("--body-limit", type=int, default=0, help="truncate body text to N chars (0 = full)")
ap.add_argument("--show-brief", action="store_true")
args = ap.parse_args()

packets = json.loads(args.packets.read_text(encoding="utf-8"))
import csv
if args.ids:
    order = [r["id"] for r in csv.DictReader(args.ids.open(encoding="utf-8-sig")) if r.get("id")]
    pos = {i: n for n, i in enumerate(order)}
    packets = sorted([p for p in packets if p["id"] in pos], key=lambda p: pos[p["id"]])

for p in packets:
    c = p["body_char_count"]
    if c < args.min_chars: continue
    if args.max_chars is not None and c > args.max_chars: continue
    idx = p["index"]
    body = p["text"]
    if args.body_limit and len(body) > args.body_limit:
        body = body[: args.body_limit] + f"\n...[TRUNCATED {len(p['text'])-args.body_limit} chars]"
    print("=" * 100)
    print(f"[{p['source_ordinal']}] {p['id']}  《{p['title']}》  body={c}  {idx.get('published_date','')}")
    print(f"  question: {p['question']}")
    print(f"  MANUAL  : primary={p['manual_primary']} secondary={p['manual_secondary']} status={p['manual_status']} reviewer={p['manual_reviewer']}")
    print(f"  INDEX   : primary={idx.get('primary_print_topic')} sec={idx.get('secondary_print_topics')} theme_primary={idx.get('theme_primary')} concept_primary={idx.get('concept_primary')}")
    print(f"  OFFICIAL: status={idx.get('official_assignment_status')} n={idx.get('official_category_count')} paths={idx.get('official_category_paths')}")
    print(f"  DEEPSEEK: avail={idx.get('deepseek_available')} read={idx.get('deepseek_reading_status')} claims={idx.get('deepseek_main_claim_count')} img={idx.get('deepseek_image_count')}/{idx.get('deepseek_image_checked')}")
    print(f"  CONCEPT : {idx.get('concept_tags')}")
    print(f"  PRIOR   : {p['manual_decision_basis']}")
    print(f"  NOTE    : {p['manual_review_note'][:1200]}")
    if args.show_brief and p.get("brief"):
        print(f"  BRIEF   : {p['brief'][:600]}")
    print("-" * 100)
    print(body)
    print()
