#!/usr/bin/env python3
"""Select and download the first unreviewed image batch for Round115.

This script only creates Round115 artifacts.  It never edits the source image
inventory or any manual-decision table.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

import requests


ROOT = Path(__file__).resolve().parents[2]
INVENTORY = ROOT / "research-rebuild/data/image-inventory.csv"
REPORTS = ROOT / "research-rebuild/reports"
DEFAULT_BATCH = REPORTS / "live-image-review-batch-v2-round115.csv"
DEFAULT_MANIFEST = REPORTS / "round115-image-manifest.csv"
DEFAULT_DIR = ROOT / "research-rebuild/image-review/round115"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def write_csv(path: Path, rows: list[dict[str, Any]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    temporary.replace(path)


def as_int(value: str | None) -> int:
    try:
        return int(value or 0)
    except (TypeError, ValueError):
        return 0


def select_articles(rows: list[dict[str, str]], article_count: int) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    if not 1 <= article_count <= 50:
        raise ValueError("article_count must be between 1 and 50")
    groups: dict[tuple[int, str], list[dict[str, str]]] = {}
    for row in rows:
        if row.get("status") != "unreviewed":
            continue
        key = (as_int(row.get("ordinal")), row.get("id", ""))
        groups.setdefault(key, []).append(row)
    ordered = sorted(groups.items(), key=lambda item: (item[0][0], item[0][1]))
    selected_groups = ordered[:article_count]
    if len(selected_groups) != article_count:
        raise ValueError(f"only {len(selected_groups)} unreviewed articles available")
    selected_rows: list[dict[str, str]] = []
    for _, group in selected_groups:
        group.sort(key=lambda row: as_int(row.get("image_index")))
        indices = [as_int(row.get("image_index")) for row in group]
        if indices != list(range(1, len(group) + 1)):
            raise ValueError(f"non-contiguous image indices for {group[0].get('id')}: {indices}")
        selected_rows.extend(group)
    return [group[0] for _, group in selected_groups], selected_rows


def normalise_url(src: str) -> str:
    return "https:" + src if src.startswith("//") else src


def download_one(row: dict[str, Any], destination: Path, timeout: int, attempts: int) -> dict[str, Any]:
    url = normalise_url(str(row["src"]))
    local_name = str(row["local_file"])
    target = destination / Path(local_name).name
    result = dict(row)
    result["download_status"] = "failed"
    result["download_bytes"] = "0"
    result["content_type"] = ""
    result["download_error"] = ""
    headers = {"User-Agent": "Mozilla/5.0 (compatible; qbl-image-review/1.0)", "Referer": "https://sooon.ai/"}
    last_error = ""
    for attempt in range(1, attempts + 1):
        temporary_name = None
        try:
            with requests.get(url, headers=headers, timeout=timeout, stream=True) as response:
                response.raise_for_status()
                content_type = response.headers.get("content-type", "")
                with tempfile.NamedTemporaryFile(prefix=target.name + ".", suffix=".part", dir=destination, delete=False) as fh:
                    temporary_name = Path(fh.name)
                    for chunk in response.iter_content(chunk_size=1024 * 128):
                        if chunk:
                            fh.write(chunk)
            size = temporary_name.stat().st_size
            if size <= 0:
                raise RuntimeError("empty response body")
            os.replace(temporary_name, target)
            result["download_status"] = "success"
            result["download_bytes"] = str(size)
            result["content_type"] = content_type
            return result
        except Exception as exc:  # retry transient network/provider errors
            last_error = f"attempt {attempt}: {type(exc).__name__}: {exc}"
            if temporary_name and temporary_name.exists():
                temporary_name.unlink()
    result["download_error"] = last_error
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--article-count", type=int, default=20)
    parser.add_argument("--batch", type=Path, default=DEFAULT_BATCH)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--download-dir", type=Path, default=DEFAULT_DIR)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--timeout", type=int, default=45)
    parser.add_argument("--attempts", type=int, default=3)
    args = parser.parse_args()

    inventory_rows = read_csv(INVENTORY)
    articles, image_rows = select_articles(inventory_rows, args.article_count)
    args.download_dir.mkdir(parents=True, exist_ok=True)

    batch_rows = []
    for article in articles:
        batch_rows.append(
            {
                "ordinal": article["ordinal"],
                "id": article["id"],
                "title": article["title"],
                "image_count": sum(1 for row in image_rows if row["id"] == article["id"]),
                "primary": "image_review",
                "status": "selected_pending_review",
                "selection_basis": "first unreviewed unique articles by ordinal",
                "download_dir": str(args.download_dir.relative_to(ROOT)).replace("\\", "/"),
            }
        )
    write_csv(
        args.batch,
        batch_rows,
        ["ordinal", "id", "title", "image_count", "primary", "status", "selection_basis", "download_dir"],
    )

    manifest_rows: list[dict[str, Any]] = []
    for sequence, row in enumerate(image_rows, start=1):
        local_name = f"{sequence:02d}-{row['id']}-{row['image_index']}.jpg"
        manifest_rows.append(
            {
                **row,
                "local_file": str((args.download_dir / local_name).relative_to(ROOT)).replace("\\", "/"),
                "download_status": "pending",
                "download_bytes": "0",
                "content_type": "",
                "download_error": "",
            }
        )

    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        futures = {
            pool.submit(download_one, row, args.download_dir, args.timeout, args.attempts): index
            for index, row in enumerate(manifest_rows)
        }
        for future in as_completed(futures):
            manifest_rows[futures[future]] = future.result()

    fields = list(inventory_rows[0].keys()) + [
        "local_file",
        "download_status",
        "download_bytes",
        "content_type",
        "download_error",
    ]
    write_csv(args.manifest, manifest_rows, fields)

    failures = [row for row in manifest_rows if row["download_status"] != "success"]
    summary = {
        "articles": len(articles),
        "images": len(manifest_rows),
        "downloaded": len(manifest_rows) - len(failures),
        "failed": len(failures),
        "failures": [{"id": row["id"], "image_index": row["image_index"], "error": row["download_error"]} for row in failures],
        "batch": str(args.batch),
        "manifest": str(args.manifest),
        "download_dir": str(args.download_dir),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
