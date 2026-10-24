#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract read-only evidence packets for the 2026-09-26 rebuild continuation.

The script never writes to the corpus or to any existing research index.  It
joins, for a supplied list of article IDs:

  * the raw v2 corpus record (question / body text / timestamps, read-only),
  * the current manual decision row (primary, secondary, status, notes),
  * the formal index row (official object-practice paths, DeepSeek evidence,
    concept tags, image counts).

Output is a JSON list plus a compact console summary so a later reviewer can
reproduce exactly which body text was in front of the decision.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CORPUS = ROOT / "sooon-q9adg-articles-v2.jsonl"
MANUAL = ROOT / "research-rebuild/data/print-topic-manual-decisions-v2.csv"
FORMAL = ROOT / "research-rebuild/reports/article-classification-v2.csv"
REGISTRY = ROOT / "research-rebuild/data/print-topic-registry-v2.csv"

INDEX_FIELDS = [
    "source_ordinal",
    "title",
    "published_date",
    "body_char_count",
    "source_body_state",
    "primary_print_topic",
    "secondary_print_topics",
    "classification_status",
    "theme_primary",
    "concept_primary",
    "concept_tags",
    "official_assignment_status",
    "official_category_count",
    "official_category_paths",
    "native_object_paths",
    "native_practice_paths",
    "official_root_names",
    "official_match_methods",
    "deepseek_available",
    "deepseek_reading_status",
    "deepseek_full_text_checked",
    "deepseek_main_claim_count",
    "deepseek_unresolved_question_count",
    "deepseek_image_count",
    "deepseek_image_checked",
    "independent_review_status",
    "reading_status",
    "evidence_basis",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def load_corpus(ids: set[str]) -> dict[str, dict]:
    wanted = set(ids)
    out: dict[str, dict] = {}
    with CORPUS.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            record = json.loads(line)
            if record.get("id") in wanted:
                out[record["id"]] = record
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ids", type=Path, required=True,
                    help="CSV containing an 'id' column (extra columns ignored).")
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--min-chars", type=int, default=0)
    ap.add_argument("--max-chars", type=int, default=None)
    args = ap.parse_args()

    id_rows = read_csv(args.ids)
    ordered_ids = [r["id"] for r in id_rows if r.get("id")]
    manual = {r["id"]: r for r in read_csv(MANUAL)}
    formal = {r["id"]: r for r in read_csv(FORMAL)}
    corpus = load_corpus(set(ordered_ids))

    packets = []
    missing = []
    for article_id in ordered_ids:
        record = corpus.get(article_id)
        if record is None:
            missing.append(article_id)
            continue
        text = record.get("text") or ""
        chars = len(text)
        if chars < args.min_chars:
            continue
        if args.max_chars is not None and chars > args.max_chars:
            continue
        man = manual.get(article_id, {})
        idx = formal.get(article_id, {})
        packet = {
            "source_ordinal": idx.get("source_ordinal", ""),
            "id": article_id,
            "title": record.get("title", ""),
            "question": record.get("question", "") or "",
            "published_at": record.get("publishedAt"),
            "url": record.get("url", ""),
            "body_char_count": chars,
            "text": text,
            "brief": record.get("brief") or "",
            "manual_status": man.get("classification_status", ""),
            "manual_primary": man.get("primary_print_topic_code", ""),
            "manual_secondary": man.get("secondary_print_topic_codes", ""),
            "manual_decision_basis": man.get("decision_basis", ""),
            "manual_review_note": man.get("review_note", ""),
            "manual_reviewer": man.get("reviewer", ""),
            "manual_reviewed_at": man.get("reviewed_at", ""),
            "index": {k: idx.get(k, "") for k in INDEX_FIELDS},
        }
        packets.append(packet)

    packets.sort(key=lambda p: (p["body_char_count"], str(p["source_ordinal"])))
    if args.limit:
        packets = packets[: args.limit]

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", encoding="utf-8") as fh:
        json.dump(packets, fh, ensure_ascii=False, indent=1)

    summary = {
        "requested_ids": len(ordered_ids),
        "packets": len(packets),
        "missing_from_corpus": missing,
        "total_body_chars": sum(p["body_char_count"] for p in packets),
        "min_body_chars": min((p["body_char_count"] for p in packets), default=0),
        "max_body_chars": max((p["body_char_count"] for p in packets), default=0),
        "output": str(args.out),
        "corpus_read_only": True,
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
