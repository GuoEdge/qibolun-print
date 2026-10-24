#!/usr/bin/env python3
"""Prepare, download, and decode-check the next bounded image-review batch."""
from __future__ import annotations

import csv
import json
import os
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import requests
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"
QUEUE = REPORTS / "live-manual-classification-queue-v2.csv"
INVENTORY = DATA / "image-inventory.csv"
SELECTION = REPORTS / "round141-image-selection.csv"
MANIFEST = REPORTS / "round141-image-manifest.csv"
DEST = ROOT / "research-rebuild/image-review/round141"

TARGET_IDS = {
    "5fcaadb8-9bba-5d43-9f03-0c374dfc9729",  # 农村的未来
    "5a0bd06a-a65b-5410-9161-e4dd82420236",  # 下三路
    "09876c2d-e45f-586f-b3db-7598cc852767",  # 大洪水
    "f62a367a-978f-5c01-8471-170daaa2eea8",  # 疗愈艺术
    "f2411d1a-c591-5573-b775-8c66bfd10783",  # 礼
}


def read(path: Path, delimiter=","):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle, delimiter=delimiter))


def write(path: Path, fields, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    temporary.replace(path)


def integer(value):
    try:
        return int(value or 0)
    except (TypeError, ValueError):
        return 0


def source_url(value):
    return "https:" + value if value.startswith("//") else value


def prior_reviewed_keys():
    reviewed_keys = set()
    reviewed_ids = set()
    for path in REPORTS.glob("round*-image-review.tsv"):
        for row in read(path, delimiter="\t"):
            if row.get("id") and row.get("image_index"):
                reviewed_keys.add((row["id"], row["image_index"]))
                reviewed_ids.add(row["id"])
    for path in REPORTS.glob("round*-image-decisions.tsv"):
        for row in read(path, delimiter="\t"):
            if row.get("id"):
                reviewed_ids.add(row["id"])
    return reviewed_keys, reviewed_ids


def download(row):
    target = DEST / Path(row["local_file"]).name
    result = dict(
        row,
        download_status="failed",
        download_bytes="0",
        content_type="",
        download_error="",
    )
    for attempt in range(1, 4):
        temporary = None
        try:
            with requests.get(
                source_url(row["src"]),
                headers={
                    "User-Agent": "Mozilla/5.0 (compatible; qbl-image-review/1.0)",
                    "Referer": "https://sooon.ai/",
                },
                timeout=45,
                stream=True,
            ) as response:
                response.raise_for_status()
                with tempfile.NamedTemporaryFile(
                    prefix=target.name + ".",
                    suffix=".part",
                    dir=DEST,
                    delete=False,
                ) as handle:
                    temporary = Path(handle.name)
                    for chunk in response.iter_content(131072):
                        if chunk:
                            handle.write(chunk)
                size = temporary.stat().st_size
                if size <= 0:
                    raise RuntimeError("empty response body")
                with Image.open(temporary) as image:
                    image.verify()
                os.replace(temporary, target)
                result.update(
                    download_status="success",
                    download_bytes=str(size),
                    content_type=response.headers.get("content-type", ""),
                )
                return result
        except Exception as exc:  # retain failure evidence in the manifest
            if temporary and temporary.exists():
                temporary.unlink()
            result["download_error"] = (
                f"attempt {attempt}: {type(exc).__name__}: {exc}"
            )
    return result


def main():
    queue = read(QUEUE)
    inventory = read(INVENTORY)
    queue_by_id = {row["id"]: row for row in queue}
    missing = TARGET_IDS - set(queue_by_id)
    if missing:
        raise RuntimeError(f"target IDs missing from queue: {sorted(missing)}")

    reviewed_keys, reviewed_ids = prior_reviewed_keys()
    by_id = {}
    for row in inventory:
        by_id.setdefault(row["id"], []).append(row)

    selection = []
    manifest = []
    for article_id in sorted(TARGET_IDS, key=lambda value: integer(queue_by_id[value].get("source_ordinal"))):
        article = queue_by_id[article_id]
        if article_id in reviewed_ids:
            raise RuntimeError(f"historically reviewed article selected: {article_id}")
        group = sorted(by_id[article_id], key=lambda row: integer(row.get("image_index")))
        expected = integer(article.get("deepseek_image_count"))
        if len(group) != expected or any(row.get("status") != "unreviewed" for row in group):
            raise RuntimeError(f"incomplete or reviewed image group {article_id}: {len(group)}/{expected}")
        if any((row["id"], row["image_index"]) in reviewed_keys for row in group):
            raise RuntimeError(f"image-key overlap with prior review: {article_id}")
        selection.append({
            "priority": article.get("priority", ""),
            "priority_reasons": "image_review;fresh_complete_group;round141",
            "source_ordinal": article.get("source_ordinal", ""),
            "id": article_id,
            "title": article.get("title", ""),
            "question": article.get("question", ""),
            "published_date": article.get("published_date", ""),
            "body_char_count": article.get("body_char_count", ""),
            "source_body_state": article.get("source_body_state", ""),
            "candidate_primary": article.get("candidate_primary", ""),
            "candidate_secondary": article.get("candidate_secondary", ""),
            "candidate_score": article.get("candidate_score", ""),
            "candidate_status": article.get("candidate_status", ""),
            "official_assignment_status": article.get("official_assignment_status", ""),
            "official_category_paths": article.get("official_category_paths", ""),
            "native_object_paths": article.get("native_object_paths", ""),
            "deepseek_available": article.get("deepseek_available", ""),
            "deepseek_reading_status": article.get("deepseek_reading_status", ""),
            "deepseek_image_count": str(expected),
            "evidence_basis": article.get("evidence_basis", ""),
            "manual_status": article.get("manual_status", ""),
        })
        for row in group:
            relative = str(DEST.relative_to(ROOT)).replace("\\", "/")
            manifest.append(dict(
                row,
                local_file=f"{relative}/{len(manifest) + 1:02d}-{row['id']}-{row['image_index']}.jpg",
                reconciliation="round141_fresh_complete_group",
            ))

    if not 40 <= len(manifest) <= 50:
        raise RuntimeError(f"image budget out of range: {len(manifest)}")
    write(SELECTION, list(selection[0]), selection)
    DEST.mkdir(parents=True, exist_ok=True)
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(download, row): index for index, row in enumerate(manifest)}
        for future in as_completed(futures):
            manifest[futures[future]] = future.result()
    fields = list(inventory[0]) + [
        "local_file", "reconciliation", "download_status", "download_bytes",
        "content_type", "download_error",
    ]
    write(MANIFEST, fields, manifest)
    failed = [row for row in manifest if row["download_status"] != "success"]
    summary = {
        "round": 141,
        "articles": len(TARGET_IDS),
        "images": len(manifest),
        "downloaded_and_decode_verified": len(manifest) - len(failed),
        "failed": len(failed),
        "selection": str(SELECTION),
        "manifest": str(MANIFEST),
        "download_dir": str(DEST),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    raise SystemExit(1 if failed else 0)


if __name__ == "__main__":
    main()
