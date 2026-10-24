#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build an incremental research queue for articles absent from the old corpus.

The v2 corpus and DeepSeek first-pass output remain read-only.  This script
uses the old corpus ID set as the authoritative reuse boundary, then emits
new-content reports without replacing the existing all-corpus queue.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def read_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    with path.open(encoding="utf-8") as fh:
        for line_no, line in enumerate(fh, 1):
            if line.strip():
                row = json.loads(line)
                row["_line"] = line_no
                rows.append(row)
    return rows


def priority(rec: dict) -> tuple[int, list[str]]:
    reading = rec.get("reading") or {}
    analysis = rec.get("analysis") or {}
    structure = rec.get("structure") or {}
    reasons: list[str] = []
    score = 0
    if reading.get("status") == "needs_reread":
        score += 100
        reasons.append("needs_reread")
    if structure.get("images"):
        score += 60
        reasons.append("image_review")
    if not analysis.get("evidence_locations") and not rec.get("evidence_refs"):
        score += 25
        reasons.append("no_evidence_locations")
    if not analysis.get("main_claims"):
        score += 20
        reasons.append("no_main_claims")
    if not structure.get("full_text_checked"):
        score += 15
        reasons.append("full_text_unconfirmed")
    if len(analysis.get("unresolved_questions") or []) >= 3:
        score += 5
        reasons.append("many_open_questions")
    return score, reasons


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--old", type=Path, default=Path("sooon-q9adg-articles.jsonl"))
    ap.add_argument("--v2", type=Path, default=Path("sooon-q9adg-articles-v2.jsonl"))
    ap.add_argument("--out", type=Path, default=Path("research-rebuild/out"))
    ap.add_argument("--reports", type=Path, default=Path("research-rebuild/reports"))
    args = ap.parse_args()

    old_rows = read_jsonl(args.old)
    v2_rows = read_jsonl(args.v2)
    old_ids = {row.get("id") for row in old_rows}
    new_rows = [row for row in v2_rows if row.get("id") not in old_ids]
    new_ids = {row.get("id") for row in new_rows}

    # DeepSeek output is one JSON object per line across *.out.jsonl files.
    first_pass: dict[str, dict] = {}
    for path in sorted(args.out.glob("*.out.jsonl")):
        for row in read_jsonl(path):
            article_id = row.get("article_id")
            if article_id:
                first_pass[article_id] = {"record": row, "path": path, "line": row["_line"]}

    queue: list[dict] = []
    index_rows: list[dict] = []
    for ordinal, article in enumerate(new_rows, 1):
        article_id = article.get("id")
        hit = first_pass.get(article_id)
        rec = hit["record"] if hit else {}
        score, reasons = priority(rec) if hit else (140, ["no_first_pass_record", "full_text_unconfirmed"])
        metadata = rec.get("metadata") or {}
        structure = rec.get("structure") or {}
        reading = rec.get("reading") or {}
        analysis = rec.get("analysis") or {}
        row = {
            "increment_ordinal": ordinal,
            "source_ordinal": v2_rows.index(article) + 1,
            "id": article_id,
            "title": article.get("title") or metadata.get("title", ""),
            "published_at": article.get("publishedAt") or article.get("published_at"),
            "url": article.get("url") or metadata.get("url", ""),
            "provenance_change_kind": (article.get("provenance") or {}).get("changeKind", "new"),
            "deepseek_covered": bool(hit),
            "deepseek_status": reading.get("status"),
            "batch_id": reading.get("batch_id"),
            "full_text_checked": structure.get("full_text_checked"),
            "image_count": len(structure.get("images") or []),
            "has_main_claims": bool(analysis.get("main_claims")),
            "has_evidence": bool(analysis.get("evidence_locations") or rec.get("evidence_refs")),
            "priority": score,
            "reasons": reasons,
            "record_path": str(hit["path"].relative_to(args.out.parent)).replace("\\", "/") if hit else "",
            "record_line": hit["line"] if hit else None,
            "line": hit["line"] if hit else None,
        }
        index_rows.append(row)
        queue.append(row)

    queue.sort(key=lambda row: (-row["priority"], row["increment_ordinal"]))
    args.reports.mkdir(parents=True, exist_ok=True)
    csv_path = args.reports / "new-article-index.csv"
    fields = [key for key in index_rows[0]] if index_rows else ["id"]
    with csv_path.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for row in index_rows:
            out = dict(row)
            out["reasons"] = ";".join(row["reasons"])
            writer.writerow(out)

    queue_path = args.reports / "new-independent-review-queue.jsonl"
    with queue_path.open("w", encoding="utf-8") as fh:
        for row in queue:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")

    summary = {
        "v2_records": len(v2_rows),
        "old_records": len(old_rows),
        "new_records": len(new_rows),
        "deepseek_covered": sum(row["deepseek_covered"] for row in index_rows),
        "deepseek_missing": sum(not row["deepseek_covered"] for row in index_rows),
        "needs_reread": sum(row["deepseek_status"] == "needs_reread" for row in index_rows),
        "image_review": sum(row["image_count"] > 0 for row in index_rows),
        "full_text_checked": sum(row["full_text_checked"] is True for row in index_rows),
        "has_main_claims": sum(row["has_main_claims"] for row in index_rows),
        "has_evidence": sum(row["has_evidence"] for row in index_rows),
        "old_research_reuse": {"eligible_records": len(old_rows), "new_version_review_required": "separate audit"},
        "outputs": [str(csv_path), str(queue_path)],
        "note": "新增边界由 v2 ID 不在旧语料 ID 集合中定义；DeepSeek 结果仅作初读索引，不能直接升级为最终研究结论。",
    }
    summary_path = args.reports / "new-content-progress.json"
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
