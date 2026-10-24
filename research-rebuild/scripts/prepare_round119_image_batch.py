#!/usr/bin/env python3
"""Prepare and download the canonical Round119 image-review batch.

Round119 is deliberately restricted to six complete, currently-unreviewed
article groups which do not occur in any previous image manifest.  This keeps
the batch close to the requested 50-image budget while avoiding re-review of
any article selected by an earlier round.  Only Round119 report files and its
download directory are written; source inventory, manual decisions, and
derived indexes remain untouched.
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

ROOT = Path(__file__).resolve().parents[2]
INVENTORY = ROOT / "research-rebuild/data/image-inventory.csv"
REPORTS = ROOT / "research-rebuild/reports"
DEFAULT_BATCH = REPORTS / "live-image-review-batch-v2-round119.csv"
DEFAULT_MANIFEST = REPORTS / "round119-image-manifest.csv"
DEFAULT_DIR = ROOT / "research-rebuild/image-review/round119"

# Six complete groups: 11 + 8 + 8 + 8 + 7 + 6 = 48 images.
SELECTED_IDS = [
    "68434efd-b4b2-5ce3-8a97-8864805ba63a",  # 轮子科技
    "6d972b31-ca74-5ed9-a989-2d0352cf6ba4",  # 日式
    "5e41ab6c-b81f-549f-b326-9e6bea9cbc4a",  # 种族矛盾
    "c6a02357-79be-54da-895e-0a7a9b76dc93",  # 基督教与食血
    "9bd10f2e-221b-5789-b44c-65732e163960",  # 丑
    "88e2e0eb-6711-5cca-b0a3-f049eb97e7c7",  # 安全的路
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    with temp.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    temp.replace(path)


def as_int(value: str | None) -> int:
    try:
        return int(value or 0)
    except (TypeError, ValueError):
        return 0


def prior_article_ids() -> set[str]:
    ids: set[str] = set()
    for path in REPORTS.glob("round*-image-manifest*.csv"):
        if path.name == "round119-image-manifest.csv":
            continue
        for row in read_csv(path):
            if row.get("id"):
                ids.add(row["id"])
    return ids


def select_groups(inventory: list[dict[str, str]]) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    prior = prior_article_ids()
    groups: dict[str, list[dict[str, str]]] = {}
    for row in inventory:
        if row.get("id") in SELECTED_IDS:
            groups.setdefault(row["id"], []).append(row)
    missing = [aid for aid in SELECTED_IDS if aid not in groups]
    if missing:
        raise RuntimeError(f"selected IDs absent from inventory: {missing}")
    overlap = sorted(set(SELECTED_IDS) & prior)
    if overlap:
        raise RuntimeError(f"selected IDs occur in prior manifests: {overlap}")
    selected_ids = [aid for aid in SELECTED_IDS if groups[aid][0].get("status") == "unreviewed"]
    if selected_ids != SELECTED_IDS:
        raise RuntimeError("all selected groups must currently be unreviewed")
    articles: list[dict[str, str]] = []
    images: list[dict[str, str]] = []
    for aid in SELECTED_IDS:
        group = sorted(groups[aid], key=lambda r: as_int(r.get("image_index")))
        indices = [as_int(r.get("image_index")) for r in group]
        if indices != list(range(1, len(group) + 1)):
            raise RuntimeError(f"non-contiguous image indices for {aid}: {indices}")
        articles.append(group[0])
        images.extend(group)
    if len(images) != 48:
        raise RuntimeError(f"Round119 budget invariant failed: {len(images)} images, expected 48")
    return articles, images


def normalise_url(src: str) -> str:
    return "https:" + src if src.startswith("//") else src


def download_one(row: dict[str, str], destination: Path, timeout: int, attempts: int) -> dict[str, str]:
    target = destination / Path(row["local_file"]).name
    result = dict(row, download_status="failed", download_bytes="0", content_type="", download_error="")
    headers = {"User-Agent": "Mozilla/5.0 (compatible; qbl-image-review/1.0)", "Referer": "https://sooon.ai/"}
    last = ""
    for attempt in range(1, attempts + 1):
        temporary: Path | None = None
        try:
            with requests.get(normalise_url(row["src"]), headers=headers, timeout=timeout, stream=True) as response:
                response.raise_for_status()
                with tempfile.NamedTemporaryFile(prefix=target.name + ".", suffix=".part", dir=destination, delete=False) as fh:
                    temporary = Path(fh.name)
                    for chunk in response.iter_content(chunk_size=131072):
                        if chunk:
                            fh.write(chunk)
                size = temporary.stat().st_size
                if size <= 0:
                    raise RuntimeError("empty response body")
                os.replace(temporary, target)
                result.update(download_status="success", download_bytes=str(size), content_type=response.headers.get("content-type", ""))
                return result
        except Exception as exc:
            last = f"attempt {attempt}: {type(exc).__name__}: {exc}"
            if temporary and temporary.exists():
                temporary.unlink()
    result["download_error"] = last
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--timeout", type=int, default=45)
    parser.add_argument("--attempts", type=int, default=3)
    parser.add_argument("--batch", type=Path, default=DEFAULT_BATCH)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--download-dir", type=Path, default=DEFAULT_DIR)
    args = parser.parse_args()

    inventory = read_csv(INVENTORY)
    articles, image_rows = select_groups(inventory)
    args.download_dir.mkdir(parents=True, exist_ok=True)
    download_dir = str(args.download_dir.relative_to(ROOT)).replace("\\", "/")
    basis = "fresh unreviewed groups; complete article groups; no overlap with any prior image manifest; 48-image budget"
    batch = [{"ordinal": a["ordinal"], "id": a["id"], "title": a["title"], "image_count": str(sum(r["id"] == a["id"] for r in image_rows)), "primary": "image_review", "status": "selected_pending_review", "selection_basis": basis, "download_dir": download_dir} for a in articles]
    write_csv(args.batch, batch, ["ordinal", "id", "title", "image_count", "primary", "status", "selection_basis", "download_dir"])

    manifest: list[dict[str, str]] = []
    for seq, row in enumerate(image_rows, 1):
        name = f"{seq:02d}-{row['id']}-{row['image_index']}.jpg"
        manifest.append({**row, "local_file": f"{download_dir}/{name}", "download_status": "pending", "download_bytes": "0", "content_type": "", "download_error": ""})
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        futures = {pool.submit(download_one, row, args.download_dir, args.timeout, args.attempts): i for i, row in enumerate(manifest)}
        for future in as_completed(futures):
            manifest[futures[future]] = future.result()
    fields = list(inventory[0].keys()) + ["local_file", "download_status", "download_bytes", "content_type", "download_error"]
    write_csv(args.manifest, manifest, fields)
    failed = [r for r in manifest if r["download_status"] != "success"]
    print(json.dumps({"articles": len(articles), "images": len(manifest), "downloaded": len(manifest) - len(failed), "failed": len(failed), "batch": str(args.batch), "manifest": str(args.manifest), "download_dir": str(args.download_dir)}, ensure_ascii=False, indent=2))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
