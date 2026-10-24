#!/usr/bin/env python3
"""Synchronize Round121 visual review into the image inventory and audit notes."""
from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"


def read(path: Path, delimiter: str = ","):
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh, delimiter=delimiter)
        return list(reader.fieldnames or []), list(reader)


def write(path: Path, fields, rows, delimiter: str = ","):
    temp = path.with_suffix(path.suffix + ".tmp")
    with temp.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, delimiter=delimiter, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    temp.replace(path)


def main() -> int:
    _, batch = read(REPORTS / "live-image-review-batch-v2-round121.csv")
    manifest_fields, manifest = read(REPORTS / "round121-image-manifest.csv")
    _, review = read(REPORTS / "round121-image-review.tsv", "\t")
    inventory_fields, inventory = read(DATA / "image-inventory.csv")
    _, manual = read(DATA / "print-topic-manual-decisions-v2.csv")
    ids = {row["id"] for row in batch}
    assert len(ids) == 21 and len(manifest) == len(review) == 46
    assert all(row["download_status"] == "success" for row in manifest)
    by_key = {(row["id"], row["image_index"]): row for row in review}
    assert set(by_key) == {(row["id"], row["image_index"]) for row in manifest}
    assert all(row["review_status"] == "reviewed" and row["changes_topic_judgment"] == "no" for row in review)

    for row in inventory:
        key = (row.get("id", ""), row.get("image_index", ""))
        if key not in by_key:
            continue
        reviewed = by_key[key]
        row["status"] = "reviewed"
        row["notes"] = (
            f"{reviewed['visible_content']}；{reviewed['relation_to_text']}；"
            f"专题改变={reviewed['changes_topic_judgment']}；限制：{reviewed['limitations']}；"
            "视觉复核完成，OCR未核验。"
        )
    assert sum(row.get("status") == "reviewed" for row in inventory if row.get("id") in ids) == 46
    write(DATA / "image-inventory.csv", inventory_fields, inventory)

    for row in manifest:
        reviewed = by_key[(row["id"], row["image_index"])]
        row["status"] = "reviewed"
        row["notes"] = f"{reviewed['visible_content']}；图文关系：{reviewed['relation_to_text']}；限制：{reviewed['limitations']}"
    write(REPORTS / "round121-image-manifest.csv", manifest_fields, manifest)

    groups = defaultdict(list)
    for row in review:
        groups[row["id"]].append(row)
    manual_by_id = {row["id"]: row for row in manual}
    for aid, rows in groups.items():
        row = manual_by_id[aid]
        marker = "Round121 visual review=reports/round121-image-review.tsv"
        if marker not in row.get("review_note", ""):
            row["review_note"] = row.get("review_note", "").rstrip("; ") + f"; {marker} ({len(rows)}/{len(rows)} images; no topic change); image limitations recorded per image; OCR and factual claims remain unverified."
        if "image-review" not in row.get("reviewer", ""):
            row["reviewer"] = (row.get("reviewer", "main-thread") + "+image-review").strip("+")
    write(DATA / "print-topic-manual-decisions-v2.csv", list(manual[0]) if manual else [], manual)
    print(json.dumps({"round": 121, "articles": len(groups), "images": len(review), "consistent": sum(r["image_text_consistency"] == "consistent" for r in review), "limited": sum(r["image_text_consistency"] == "limited" for r in review), "inconclusive": sum(r["image_text_consistency"] == "inconclusive" for r in review)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
