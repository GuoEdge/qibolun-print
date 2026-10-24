#!/usr/bin/env python3
"""Build a transparent, refreshable audit of provisional-status reasons.

Flags intentionally overlap: an article can have both pending images and a
boundary concern.  The report is triage evidence, not a new classification.
"""
from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "research-rebuild/data"
REPORTS = ROOT / "research-rebuild/reports"
MANUAL = DATA / "print-topic-manual-decisions-v2.csv"
CLASSIFICATION = REPORTS / "article-classification-v2.csv"
INVENTORY = DATA / "image-inventory.csv"
OUT_CSV = REPORTS / "provisional-reasons-audit-v2.csv"
OUT_JSON = REPORTS / "provisional-reasons-audit-v2.json"


def read(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    temp = path.with_suffix(path.suffix + ".tmp")
    with temp.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    temp.replace(path)


def main() -> None:
    manual = [r for r in read(MANUAL) if r.get("classification_status") == "manual_provisional"]
    classification = {r.get("id", ""): r for r in read(CLASSIFICATION)}
    inventory = read(INVENTORY)
    by_id: dict[str, list[dict[str, str]]] = {}
    for row in inventory:
        by_id.setdefault(row.get("id", ""), []).append(row)
    rows = []
    for article in manual:
        aid = article.get("id", "")
        images = by_id.get(aid, [])
        pending = [r for r in images if r.get("status") != "reviewed"]
        note = f"{article.get('review_note', '')} {article.get('decision_basis', '')}"
        source_flag = (
            classification.get(aid, {}).get("reading_status") == "needs_reread"
            or any(token in note for token in ("材料不足", "正文极短", "待补源", "只有视频", "不完整", "断尾", "A00"))
        )
        boundary_flag = any(token in note for token in ("边界", "盲审", "二次复核", "分歧", "待裁定", "正式/", "正式与"))
        legacy_flag = not source_flag and not boundary_flag and not pending
        rows.append({
            "id": aid,
            "title": article.get("title", ""),
            "primary": article.get("primary_print_topic_code", ""),
            "image_count": str(len(images)),
            "unreviewed_image_count": str(len(pending)),
            "image_gate_flag": "yes" if pending else "no",
            "all_images_reviewed_flag": "yes" if images and not pending else "no",
            "no_inventory_image_flag": "yes" if not images else "no",
            "source_incomplete_flag": "yes" if source_flag else "no",
            "boundary_review_flag": "yes" if boundary_flag else "no",
            "legacy_reason_flag": "yes" if legacy_flag else "no",
            "review_note": article.get("review_note", ""),
            "decision_basis": article.get("decision_basis", ""),
            "reading_status": classification.get(aid, {}).get("reading_status", ""),
        })
    fields = list(rows[0]) if rows else ["id", "title"]
    write_csv(OUT_CSV, fields, rows)
    counts = {
        "provisional_records": len(rows),
        "image_gate_records": sum(r["image_gate_flag"] == "yes" for r in rows),
        "all_images_reviewed_records": sum(r["all_images_reviewed_flag"] == "yes" for r in rows),
        "no_inventory_image_records": sum(r["no_inventory_image_flag"] == "yes" for r in rows),
        "source_incomplete_records": sum(r["source_incomplete_flag"] == "yes" for r in rows),
        "boundary_review_records": sum(r["boundary_review_flag"] == "yes" for r in rows),
        "legacy_reason_records": sum(r["legacy_reason_flag"] == "yes" for r in rows),
        "generated_at": "2026-09-24",
        "method": "flags are deliberately overlapping triage signals; no classification status is changed",
    }
    OUT_JSON.write_text(json.dumps(counts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(counts, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
