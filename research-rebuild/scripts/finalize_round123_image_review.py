#!/usr/bin/env python3
"""Validate and synchronize Round123 image-only evidence."""
from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"
BATCH = REPORTS / "round123-image-candidates.csv"
MANIFEST = REPORTS / "round123-image-manifest.csv"
REVIEW = REPORTS / "round123-image-review.tsv"
DECISIONS = REPORTS / "round123-image-decisions.tsv"
INVENTORY = DATA / "image-inventory.csv"
MANUAL = DATA / "print-topic-manual-decisions-v2.csv"


def read_rows(path: Path, delimiter: str = ","):
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh, delimiter=delimiter)
        return list(reader.fieldnames or []), list(reader)


def atomic_write(path: Path, fields, rows, delimiter: str = ",") -> None:
    temp = path.with_suffix(path.suffix + ".tmp")
    with temp.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, delimiter=delimiter, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    temp.replace(path)


def main() -> None:
    _, batch = read_rows(BATCH)
    manifest_fields, manifest = read_rows(MANIFEST)
    review_fields, review = read_rows(REVIEW, "\t")
    inventory_fields, inventory = read_rows(INVENTORY)
    manual_fields, manual = read_rows(MANUAL)

    batch_ids = [row["id"] for row in batch]
    assert len(batch) == 12 and len(set(batch_ids)) == len(batch_ids)
    assert len(manifest) == len(review) == 41
    assert len({row["id"] for row in manual}) == len(manual) == 4305
    assert len({(row["id"], row["image_index"]) for row in manifest}) == len(manifest)
    assert len({(row["id"], row["image_index"]) for row in review}) == len(review)
    assert Counter(row["id"] for row in manifest) == Counter({row["id"]: int(row["image_count"]) for row in batch})

    manifest_by_key = {(row["id"], row["image_index"]): row for row in manifest}
    review_by_key = {(row["id"], row["image_index"]): row for row in review}
    assert manifest_by_key.keys() == review_by_key.keys()
    assert set(batch_ids) == {row["id"] for row in review}
    assert all(row["review_status"] == "reviewed" for row in review)
    assert all(row["download_status"] == "success" for row in manifest)
    assert all(row["changes_topic_judgment"] == "no" for row in review)
    assert all(row["image_text_consistency"] in {"consistent", "limited", "inconclusive"} for row in review)
    assert all(row["ocr_status"] == "not_started" for row in review)
    for row in manifest:
        local = ROOT / row["local_file"]
        assert local.is_file() and local.stat().st_size == int(row["download_bytes"]), row["local_file"]

    # Enforce the no-overlap rule against every previous image batch.
    previous_ids: set[str] = set()
    previous_keys: set[tuple[str, str, str]] = set()
    for path in REPORTS.glob("round*-image-manifest*.csv"):
        if path.resolve() == MANIFEST.resolve():
            continue
        _, prior = read_rows(path)
        for row in prior:
            if row.get("id"):
                previous_ids.add(row["id"])
                previous_keys.add((row.get("id", ""), row.get("image_index", ""), row.get("src", "")))
    assert not (set(batch_ids) & previous_ids)
    current_keys = {(row.get("id", ""), row.get("image_index", ""), row.get("src", "")) for row in manifest}
    assert not (current_keys & previous_keys)

    manual_by_id = {row["id"]: row for row in manual}
    for candidate in batch:
        current = manual_by_id[candidate["id"]]
        assert current["title"] == candidate["title"]
        assert current["classification_status"] == candidate["classification_status"]
        assert current["primary_print_topic_code"] == candidate["primary_print_topic_code"]
        assert current["classification_status"] == "manual_confirmed"

    inventory_by_key = {(row.get("id", ""), row.get("image_index", "")): row for row in inventory}
    assert len(inventory_by_key) == len(inventory), "duplicate image inventory key"
    assert manifest_by_key.keys() <= inventory_by_key.keys()
    assert all(inventory_by_key[key].get("status") == "unreviewed" for key in manifest_by_key)

    groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for candidate in batch:
        groups[candidate["id"]] = []
    for item in review:
        groups[item["id"]].append(item)

    decision_fields = [
        "id", "title", "primary_before", "secondary_before", "primary_after", "secondary_after",
        "primary_changed", "secondary_changed", "final_status", "decision", "basis", "reason",
    ]
    decisions = []
    for candidate in batch:
        current = manual_by_id[candidate["id"]]
        items = groups[candidate["id"]]
        assert len(items) == int(candidate["image_count"])
        decisions.append({
            "id": candidate["id"],
            "title": candidate["title"],
            "primary_before": current["primary_print_topic_code"],
            "secondary_before": current["secondary_print_topic_codes"],
            "primary_after": current["primary_print_topic_code"],
            "secondary_after": current["secondary_print_topic_codes"],
            "primary_changed": "no",
            "secondary_changed": "no",
            "final_status": current["classification_status"],
            "decision": "retain_existing_classification",
            "basis": "Round123 image review supports/illustrates visible context only; no topic change is justified by image evidence.",
            "reason": "Image review does not independently verify article claims, OCR, or the remaining text-based topic evidence.",
        })

    for key, item in review_by_key.items():
        inventory_row = inventory_by_key[key]
        inventory_row["status"] = "reviewed"
        inventory_row["notes"] = (
            f"{item['visible_content']}；{item['relation_to_text']}；专题改变=no；"
            f"限制：{item['limitations']}；视觉复核完成，OCR未核验。"
        )

    for row in manifest:
        item = review_by_key[(row["id"], row["image_index"])]
        row["status"] = "reviewed"
        row["notes"] = f"{item['visible_content']}；图文关系：{item['relation_to_text']}；限制：{item['limitations']}"

    marker = "Round123 visual review=reports/round123-image-review.tsv"
    for aid, items in groups.items():
        row = manual_by_id[aid]
        if marker not in row.get("review_note", ""):
            row["review_note"] = row.get("review_note", "").rstrip("; ") + (
                f"; {marker} ({len(items)}/{len(items)} images; no topic change); "
                "image limitations recorded per image; OCR and factual claims remain unverified."
            )
        if "image-review" not in row.get("reviewer", ""):
            row["reviewer"] = (row.get("reviewer", "main-thread") + "+image-review").strip("+")

    atomic_write(DECISIONS, decision_fields, decisions, "\t")
    atomic_write(INVENTORY, inventory_fields, inventory)
    atomic_write(MANIFEST, manifest_fields, manifest)
    atomic_write(MANUAL, manual_fields, manual)
    counts = Counter(row["image_text_consistency"] for row in review)
    print(json.dumps({
        "round": 123,
        "articles": len(groups),
        "images": len(review),
        "reviewed": sum(row["review_status"] == "reviewed" for row in review),
        "consistent": counts["consistent"],
        "limited": counts["limited"],
        "inconclusive": counts["inconclusive"],
        "topic_changes": sum(row["changes_topic_judgment"] == "yes" for row in review),
        "official_status_changes": 0,
        "secondary_limit": 3,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
