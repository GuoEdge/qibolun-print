#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build a refreshable queue for human A-topic classification.

The formal print index is the routing source.  Confirmed manual decisions are
the exclusion set, while provisional decisions remain eligible for follow-up
image, reread, and boundary review.  Scores only prioritize reading risk;
they are not topic decisions.
"""
from __future__ import annotations

import csv
import json
from collections import Counter
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CORPUS = ROOT / "sooon-q9adg-articles-v2.jsonl"
INDEX = ROOT / "research-rebuild/reports/print-index/print-research-index.csv"
MANUAL = ROOT / "research-rebuild/data/print-topic-manual-decisions-v2.csv"
REPORTS = ROOT / "research-rebuild/reports"
OUT_CSV = REPORTS / "live-manual-classification-queue-v2.csv"
OUT_JSON = REPORTS / "live-manual-classification-queue-v2.summary.json"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def local_date(value: str) -> str:
    try:
        stamp = int(value)
        return datetime.fromtimestamp(stamp / 1000, timezone(timedelta(hours=8))).date().isoformat()
    except (TypeError, ValueError, OSError, OverflowError):
        return ""


def corpus_rows() -> dict[str, dict]:
    result: dict[str, dict] = {}
    with CORPUS.open(encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                row = json.loads(line)
                result[str(row["id"])] = row
    return result


def score(row: dict[str, str], article: dict, image_audit: dict[str, dict[str, str]]) -> tuple[int, list[str]]:
    reasons: list[str] = []
    value = 0
    body_state = row.get("source_body_state", "")
    if body_state in {"lexical_or_image_only", "source_material_incomplete"}:
        value += 120
        reasons.append("source_material_incomplete")
    if row.get("deepseek_reading_status") in {"missing", ""} or not row.get("deepseek_available") in {"True", "true", "1"}:
        value += 95
        reasons.append("missing_first_pass")
    if row.get("deepseek_reading_status") == "needs_reread":
        value += 70
        reasons.append("first_pass_needs_reread")
    # Count image work only while the merged image audit says that an article
    # is pending or partial.  The raw image count remains non-zero after a
    # complete visual audit and must not repeatedly re-queue finished groups.
    image_row = image_audit.get(row.get("id", ""), {})
    if image_row.get("image_review_status", "") in {"pending", "partial"}:
        value += 60
        reasons.append("image_review")
    if row.get("official_assignment_status") in {"unassigned", "official_unassigned"}:
        value += 35
        reasons.append("official_unassigned")
    if row.get("official_assignment_status", "").lower().find("unassigned") >= 0:
        value += 10
    if row.get("primary_topic_status") in {"candidate_tie", "conflict_or_tie"}:
        value += 30
        reasons.append("candidate_tie_or_conflict")
    try:
        if float(row.get("primary_topic_candidate_score") or 100) < 70:
            value += 25
            reasons.append("low_candidate_score")
    except ValueError:
        pass
    if row.get("updated_date", "") >= "2026-07-01" or row.get("published_date", "") >= "2026-07-01":
        value += 15
        reasons.append("recent_v2_content")
    if not (article.get("text") or "").strip():
        value += 20
        reasons.append("empty_normalized_text")
    return value, reasons


def main() -> int:
    articles = corpus_rows()
    index = read_csv(INDEX)
    # Confirmed decisions are complete for routing purposes.  Provisional
    # decisions must remain in the live queue so image, reread, and boundary
    # follow-up work can continue after the first classification pass.
    manual_rows = read_csv(MANUAL)
    manual_ids = {
        row.get("id", "")
        for row in manual_rows
        if row.get("classification_status") == "manual_confirmed"
    }
    image_audit = {
        row.get("id", ""): row
        for row in read_csv(REPORTS / "image-article-audit-v1.csv")
        if row.get("id")
    }
    rows: list[dict[str, str | int]] = []
    strata = Counter()
    for row in index:
        aid = row.get("id", "")
        if not aid or aid in manual_ids:
            continue
        article = articles.get(aid, {})
        priority, reasons = score(row, article, image_audit)
        for reason in reasons:
            strata[reason] += 1
        rows.append({
            "priority": priority,
            "priority_reasons": ";".join(reasons),
            "source_ordinal": row.get("source_ordinal", ""),
            "id": aid,
            "title": article.get("title", row.get("title", "")),
            "question": article.get("question", ""),
            "published_date": row.get("published_date") or local_date(str(article.get("publishedAt", ""))),
            "body_char_count": row.get("body_char_count", ""),
            "source_body_state": row.get("source_body_state", ""),
            "candidate_primary": row.get("primary_print_topic", ""),
            "candidate_secondary": row.get("secondary_print_topics", ""),
            "candidate_score": row.get("primary_topic_candidate_score", ""),
            "candidate_status": row.get("primary_topic_status", ""),
            "official_assignment_status": row.get("official_assignment_status", ""),
            "official_category_paths": row.get("official_category_paths", ""),
            "native_object_paths": row.get("native_object_paths", ""),
            "deepseek_available": row.get("deepseek_available", ""),
            "deepseek_reading_status": row.get("deepseek_reading_status", ""),
            "deepseek_image_count": row.get("deepseek_image_count", ""),
            "evidence_basis": row.get("evidence_basis", ""),
            "manual_status": "pending_manual_read",
        })
    rows.sort(key=lambda row: (-int(row["priority"]), int(row["source_ordinal"] or 10**9)))
    REPORTS.mkdir(parents=True, exist_ok=True)
    fields = list(rows[0]) if rows else ["id", "manual_status"]
    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    summary = {
        "generated_at": datetime.now(timezone(timedelta(hours=8))).isoformat(),
        "corpus_records": len(articles),
        "formal_index_records": len(index),
        "manual_records_excluded": len(manual_ids),
        "queue_records": len(rows),
        "priority_counts": dict(Counter(str(row["priority"]) for row in rows)),
        "reason_counts": dict(strata),
        "outputs": [str(OUT_CSV)],
        "interpretation": "队列只决定人工阅读顺序；候选主/副专题和官方路径都是待审证据，不是最终分类。",
    }
    OUT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
