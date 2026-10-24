#!/usr/bin/env python3
"""Select and download a reproducible, complete image-review batch.

The article audit is the source of ordering; the image inventory is the
authoritative node list.  Existing review TSVs and decisions are excluded so
one image node cannot be counted twice.
"""
from __future__ import annotations

import argparse
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


def read_csv(path: Path, delimiter: str = ",") -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle, delimiter=delimiter))


def write_csv(path: Path, rows: list[dict[str, str]], delimiter: str = ",") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = list(rows[0]) if rows else []
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter=delimiter)
        writer.writeheader()
        writer.writerows(rows)
    temporary.replace(path)


def integer(value: str | None) -> int:
    try:
        return int(value or 0)
    except (TypeError, ValueError):
        return 0


def source_url(value: str) -> str:
    return "https:" + value if value.startswith("//") else value


def prior_reviewed_keys() -> tuple[set[tuple[str, str]], set[str]]:
    keys: set[tuple[str, str]] = set()
    article_ids: set[str] = set()
    for path in REPORTS.glob("round*-image-review.tsv"):
        for row in read_csv(path, "\t"):
            if row.get("id") and row.get("image_index"):
                keys.add((row["id"], row["image_index"]))
                article_ids.add(row["id"])
    for path in REPORTS.glob("round*-image-decisions.tsv"):
        for row in read_csv(path, "\t"):
            if row.get("id"):
                article_ids.add(row["id"])
    return keys, article_ids


def download(row: dict[str, str], destination: Path) -> dict[str, str]:
    target = destination / Path(row["local_file"]).name
    result = dict(row, download_status="failed", download_bytes="0", content_type="", download_error="")
    for attempt in range(1, 4):
        temporary: Path | None = None
        try:
            with requests.get(
                source_url(row["src"]),
                headers={"User-Agent": "Mozilla/5.0 (compatible; qbl-image-review/1.0)", "Referer": "https://sooon.ai/"},
                timeout=45,
                stream=True,
            ) as response:
                response.raise_for_status()
                with tempfile.NamedTemporaryFile(prefix=target.name + ".", suffix=".part", dir=destination, delete=False) as handle:
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
                result.update(download_status="success", download_bytes=str(size), content_type=response.headers.get("content-type", ""))
                return result
        except Exception as exc:
            if temporary and temporary.exists():
                temporary.unlink()
            result["download_error"] = f"attempt {attempt}: {type(exc).__name__}: {exc}"
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--round", type=int, required=True)
    parser.add_argument("--article-limit", type=int, default=50)
    parser.add_argument("--image-min", type=int, default=40)
    parser.add_argument("--image-max", type=int, default=50)
    parser.add_argument("--min-text-chars", type=int, default=1)
    parser.add_argument("--max-text-chars", type=int, default=5000)
    args = parser.parse_args()

    audit = read_csv(REPORTS / "image-article-audit-v1.csv")
    inventory = read_csv(DATA / "image-inventory.csv")
    by_id: dict[str, list[dict[str, str]]] = {}
    for row in inventory:
        by_id.setdefault(row["id"], []).append(row)
    reviewed_keys, reviewed_articles = prior_reviewed_keys()

    candidates = []
    for row in sorted(audit, key=lambda x: (integer(x.get("text_chars")), integer(x.get("ordinal")))):
        article_id = row.get("id", "")
        if row.get("image_review_status") == "complete" or article_id in reviewed_articles:
            continue
        if not args.min_text_chars <= integer(row.get("text_chars")) <= args.max_text_chars:
            continue
        group = sorted(by_id.get(article_id, []), key=lambda x: integer(x.get("image_index")))
        expected = integer(row.get("image_count"))
        if not group or len(group) != expected:
            continue
        if any(item.get("status") != "unreviewed" for item in group):
            continue
        if any((item.get("id", ""), item.get("image_index", "")) in reviewed_keys for item in group):
            continue
        candidates.append((row, group))

    selected: list[tuple[dict[str, str], list[dict[str, str]]]] = []
    image_count = 0
    for article, group in candidates:
        if len(selected) >= args.article_limit:
            break
        if selected and image_count + len(group) > args.image_max:
            continue
        selected.append((article, group))
        image_count += len(group)
        if image_count >= args.image_min:
            break
    if not selected or not args.image_min <= image_count <= args.image_max:
        raise RuntimeError(f"could not form image budget: {image_count} from {len(selected)} articles")

    selection_rows: list[dict[str, str]] = []
    manifest: list[dict[str, str]] = []
    destination = ROOT / f"research-rebuild/image-review/round{args.round}"
    destination.mkdir(parents=True, exist_ok=True)
    for article, group in selected:
        selection_rows.append(dict(article, priority_reasons="image_review;fresh_complete_group;round" + str(args.round)))
        for item in group:
            relative = str(destination.relative_to(ROOT)).replace("\\", "/")
            manifest.append(dict(item, local_file=f"{relative}/{len(manifest)+1:02d}-{item['id']}-{item['image_index']}.jpg", reconciliation=f"round{args.round}_fresh_complete_group"))

    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(download, item, destination): index for index, item in enumerate(manifest)}
        for future in as_completed(futures):
            manifest[futures[future]] = future.result()

    selection_path = REPORTS / f"round{args.round}-image-selection.csv"
    manifest_path = REPORTS / f"round{args.round}-image-manifest.csv"
    write_csv(selection_path, selection_rows)
    write_csv(manifest_path, manifest)
    failed = [item for item in manifest if item.get("download_status") != "success"]
    print(json.dumps({
        "round": args.round,
        "articles": len(selected),
        "images": len(manifest),
        "downloaded_and_decode_verified": len(manifest) - len(failed),
        "failed": len(failed),
        "selection": str(selection_path),
        "manifest": str(manifest_path),
        "download_dir": str(destination),
    }, ensure_ascii=False, indent=2))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
