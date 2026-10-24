#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Select a deterministic, size-aware batch from the live manual queue.

Short, text-only articles can be reviewed in larger groups.  Long or
image-dependent articles are kept in smaller groups by the same total-text
budget, while the queue's risk priority remains the first ordering key.
"""
from __future__ import annotations

import argparse
import csv
import json
import glob
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_QUEUE = ROOT / "research-rebuild/reports/live-manual-classification-queue-v2.csv"
DEFAULT_OUT = ROOT / "research-rebuild/reports/live-manual-batch-selection-v2.csv"
DEFAULT_MANUAL = ROOT / "research-rebuild/data/print-topic-manual-decisions-v2.csv"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def integer(row: dict[str, str], key: str, default: int = 0) -> int:
    try:
        return int(row.get(key) or default)
    except (TypeError, ValueError):
        return default


def prior_decision_ids(reports: Path) -> set[str]:
    """Return IDs with a prior *confirmed* decision.

    Provisional decisions deliberately remain eligible for image, source, or
    boundary follow-up.  Excluding every historical decision would strand the
    very records that need a second pass.
    """
    seen: set[str] = set()
    for path in glob.glob(str(reports / "round*-decisions.tsv")):
        with open(path, encoding="utf-8-sig", newline="") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                if row.get("id") and row.get("status") == "manual_confirmed":
                    seen.add(row["id"])
    return seen


def review_round_ids(manual_path: Path, rounds: set[int]) -> set[str]:
    """Return IDs whose manual row records one of the requested review rounds.

    The live queue intentionally retains provisional rows for later blind or
    boundary review.  A batch selector must therefore be able to exclude a
    *recent* review without treating every provisional row as finished.
    """
    if not rounds or not manual_path.exists():
        return set()
    excluded: set[str] = set()
    with manual_path.open(encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh):
            article_id = row.get("id", "")
            reviewer = row.get("reviewer", "")
            if not article_id or not reviewer:
                continue
            tagged_rounds = {
                int(match.group(1))
                for match in re.finditer(r"(?:^|[+_\-])round(\d+)(?:$|[+_\-])", reviewer, re.I)
            }
            if tagged_rounds & rounds:
                excluded.add(article_id)
    return excluded


def parse_rounds(value: str) -> set[int]:
    """Parse a comma-separated list such as ``142,143``."""
    rounds: set[int] = set()
    for item in (value or "").split(","):
        item = item.strip()
        if not item:
            continue
        try:
            rounds.add(int(item))
        except ValueError as exc:
            raise argparse.ArgumentTypeError(
                f"invalid review round {item!r}; use comma-separated integers"
            ) from exc
    return rounds


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--queue", type=Path, default=DEFAULT_QUEUE)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--manual", type=Path, default=DEFAULT_MANUAL)
    ap.add_argument("--target-count", type=int, default=50)
    ap.add_argument("--offset", type=int, default=0)
    ap.add_argument("--short-max-chars", type=int, default=1000)
    ap.add_argument(
        "--max-chars",
        type=int,
        default=None,
        help="只选择正文不超过该长度的文章；用于短文高吞吐批次。",
    )
    ap.add_argument(
        "--min-chars",
        type=int,
        default=0,
        help="只选择正文至少达到该长度的文章；用于长文批次。",
    )
    ap.add_argument("--text-budget", type=int, default=30000)
    ap.add_argument("--allow-images", action="store_true")
    ap.add_argument(
        "--exclude-prior-decisions",
        action="store_true",
        help="排除已出现在 research-rebuild/reports/round*-decisions.tsv 的文章，避免重复复读。",
    )
    ap.add_argument(
        "--exclude-review-rounds",
        type=parse_rounds,
        default=set(),
        help="排除人工表 reviewer 中带指定轮次标签的文章，例如 142,143；不影响其他 provisional 记录。",
    )
    args = ap.parse_args()

    rows = read_csv(args.queue)
    prior_ids = prior_decision_ids(args.queue.parent) if args.exclude_prior_decisions else set()
    recent_ids = review_round_ids(args.manual, args.exclude_review_rounds)
    candidates = []
    for row in rows:
        if row.get("id") in prior_ids:
            continue
        if row.get("id") in recent_ids:
            continue
        if row.get("source_body_state") != "text_present":
            continue
        if not args.allow_images and integer(row, "deepseek_image_count") > 0:
            continue
        body_chars = integer(row, "body_char_count")
        if body_chars <= 0:
            continue
        if args.max_chars is not None and body_chars > args.max_chars:
            continue
        if body_chars < args.min_chars:
            continue
        row["_body_chars"] = str(body_chars)
        row["_source_ordinal"] = str(integer(row, "source_ordinal"))
        candidates.append(row)

    # The live queue is already risk-sorted; retain that order and use ordinal
    # only as a stable tie-breaker for independently regenerated queues.
    candidates.sort(key=lambda r: (-integer(r, "priority"), integer(r, "source_ordinal"), r.get("id", "")))
    start = max(0, args.offset)
    selected = []
    used_chars = 0
    skipped_for_budget = []
    skipped_for_budget_count = 0
    for row in candidates[start:]:
        chars = integer(row, "_body_chars")
        if selected and used_chars + chars > args.text_budget:
            # Keep scanning this same filtered/risk-sorted cohort. A long
            # article must not consume the batch's opportunity to include
            # later short articles, but its ID remains available for a later
            # long-form or single-article pass.
            skipped_for_budget_count += 1
            # Keep the console summary compact. The full queue remains the
            # reproducible source for a later batch; only a small sample is
            # useful when checking why a candidate was deferred.
            if len(skipped_for_budget) < 25:
                skipped_for_budget.append({
                    "id": row.get("id", ""),
                    "title": row.get("title", ""),
                    "body_chars": chars,
                    "reason": "would_exceed_text_budget",
                })
            continue
        selected.append(row)
        used_chars += chars
        if len(selected) >= args.target_count:
            break

    if not selected and candidates:
        selected = [candidates[start]]
        used_chars = integer(selected[0], "_body_chars")

    fields = [k for k in (selected[0].keys() if selected else rows[0].keys()) if not k.startswith("_")]
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows({k: row.get(k, "") for k in fields} for row in selected)

    summary = {
        "queue_records": len(rows),
        "eligible_records": len(candidates),
        "selected_records": len(selected),
        "offset": start,
        "target_count": args.target_count,
        "short_max_chars": args.short_max_chars,
        "min_chars": args.min_chars,
        "max_chars": args.max_chars,
        "text_budget": args.text_budget,
        "total_body_chars": used_chars,
        "skipped_for_budget_count": skipped_for_budget_count,
        "skipped_for_budget_sample": skipped_for_budget,
        "image_policy": "allow" if args.allow_images else "exclude",
        "excluded_prior_decision_ids": len(prior_ids),
        "excluded_review_rounds": sorted(args.exclude_review_rounds),
        "excluded_recent_review_ids": len(recent_ids),
        "interpretation": "选择器只决定阅读顺序和批量大小，不产生专题结论。",
        "output": str(args.out),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
