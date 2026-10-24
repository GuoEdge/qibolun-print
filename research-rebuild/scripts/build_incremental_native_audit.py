#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit incremental corpus, first-pass gaps, and native-outline gaps.

This report is deliberately read-only with respect to the corpus and the
official category edge table.  It only emits date/overlap evidence and a
field contract for the manual review queue.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
from collections import Counter
from pathlib import Path


TZ = dt.timezone(dt.timedelta(hours=8))


def read_jsonl(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as fh:
        return [json.loads(line) for line in fh if line.strip()]


def local_date(value: object) -> str | None:
    try:
        stamp = float(value) / 1000
    except (TypeError, ValueError):
        return None
    return dt.datetime.fromtimestamp(stamp, TZ).date().isoformat()


def date_counts(rows: list[dict], key: str = "publishedAt") -> dict[str, int]:
    return dict(sorted(Counter(local_date(row.get(key)) for row in rows).items()))


def month_counts(rows: list[dict], key: str = "publishedAt") -> dict[str, int]:
    counts = Counter()
    for row in rows:
        day = local_date(row.get(key))
        if day:
            counts[day[:7]] += 1
    return dict(sorted(counts.items()))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--v2", type=Path, default=Path("sooon-q9adg-articles-v2.jsonl"))
    parser.add_argument("--old", type=Path, default=Path("sooon-q9adg-articles.jsonl"))
    parser.add_argument("--first-pass", type=Path, default=Path("research-rebuild/out"))
    parser.add_argument(
        "--candidates",
        type=Path,
        default=Path("research-rebuild/reports/native-coverage/local-unclassified-candidates.csv"),
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("research-rebuild/reports/native-coverage/incremental-date-audit.json"),
    )
    args = parser.parse_args()

    v2 = read_jsonl(args.v2)
    old = read_jsonl(args.old)
    old_ids = {row.get("id") for row in old}
    v2_by_id = {row.get("id"): row for row in v2}
    new = [row for row in v2 if row.get("id") not in old_ids]

    first_pass_ids: set[str] = set()
    for path in sorted(args.first_pass.glob("*.out.jsonl")):
        for row in read_jsonl(path):
            if row.get("article_id"):
                first_pass_ids.add(row["article_id"])
    missing = [row for row in v2 if row.get("id") not in first_pass_ids]
    missing_ids = {row.get("id") for row in missing}

    with args.candidates.open(encoding="utf-8-sig", newline="") as fh:
        candidate_rows = list(csv.DictReader(fh))
    candidate_by_id = {row["article_id"]: row for row in candidate_rows}
    candidate_ids = set(candidate_by_id)
    new_unclassified = [row for row in new if row.get("id") in candidate_ids]
    missing_unclassified = [row for row in missing if row.get("id") in candidate_ids]

    status_counts = Counter(row.get("candidate_status") for row in candidate_rows)
    new_status_counts = Counter(candidate_by_id[row["id"]]["candidate_status"] for row in new_unclassified)
    missing_status_counts = Counter(candidate_by_id[row["id"]]["candidate_status"] for row in missing_unclassified)

    result = {
        "generated_at": dt.datetime.now(TZ).isoformat(),
        "corpus": {
            "v2_records": len(v2),
            "old_records": len(old),
            "new_records": len(new),
            "new_date_counts": date_counts(new),
            "new_month_counts": month_counts(new),
        },
        "first_pass": {
            "first_pass_ids": len(first_pass_ids),
            "missing_records": len(missing),
            "missing_date_counts": date_counts(missing),
            "missing_month_counts": month_counts(missing),
            "missing_items": [
                {
                    "article_id": row.get("id"),
                    "title": row.get("title"),
                    "date_local": local_date(row.get("publishedAt")),
                    "url": row.get("url"),
                    "official_native_status": "unassigned" if row.get("id") in candidate_ids else "assigned",
                    "first_pass_status": "missing_first_pass",
                }
                for row in missing
            ],
        },
        "native_unclassified": {
            "records": len(candidate_rows),
            "status_counts": dict(sorted(status_counts.items())),
            "date_counts": date_counts([v2_by_id[article_id] for article_id in candidate_ids if article_id in v2_by_id]),
            "month_counts": month_counts([v2_by_id[article_id] for article_id in candidate_ids if article_id in v2_by_id]),
            "new_records": len(new_unclassified),
            "new_status_counts": dict(sorted(new_status_counts.items())),
            "new_date_counts": date_counts(new_unclassified),
            "new_month_counts": month_counts(new_unclassified),
            "missing_first_pass_records": len(missing_unclassified),
            "missing_first_pass_status_counts": dict(sorted(missing_status_counts.items())),
        },
        "overlap": {
            "new_and_native_unclassified": len(new_unclassified),
            "missing_first_pass_and_native_unclassified": len(missing_unclassified),
            "missing_first_pass_and_native_assigned": len(missing) - len(missing_unclassified),
        },
        "recommended_fields": [
            "corpus_boundary", "date_local", "date_stratum", "first_pass_status",
            "first_pass_batch", "official_native_status", "candidate_status",
            "candidate_paths", "evidence_source", "review_priority",
            "review_decision", "pending_reason",
        ],
        "method": "Date uses Asia/Shanghai. New means v2 ID absent from old corpus. First-pass gaps are v2 IDs absent from validated out/*.out.jsonl. Native-unclassified is the existing candidate CSV; no official edge is written.",
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "out": str(args.out),
        "v2_records": len(v2),
        "new_records": len(new),
        "first_pass_missing": len(missing),
        "native_unclassified": len(candidate_rows),
        "new_native_unclassified": len(new_unclassified),
        "missing_first_pass_native_unclassified": len(missing_unclassified),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
