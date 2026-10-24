#!/usr/bin/env python3
"""Download the approved Round121 candidate image groups.

The candidate CSV is the selection authority. This script writes only the
Round121 batch and manifest plus its download directory; it never edits the
source corpus, image inventory, manual decisions, or derived indexes.
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
CANDIDATE = ROOT / "research-rebuild/reports/round121-candidate-batch.csv"
REPORTS = ROOT / "research-rebuild/reports"
DEFAULT_BATCH = REPORTS / "live-image-review-batch-v2-round121.csv"
DEFAULT_MANIFEST = REPORTS / "round121-image-manifest.csv"
DEFAULT_DIR = ROOT / "research-rebuild/image-review/round121"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    with temp.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        writer.writeheader(); writer.writerows(rows)
    temp.replace(path)


def as_int(value: str | None) -> int:
    try:
        return int(value or 0)
    except (TypeError, ValueError):
        return 0


def normalise_url(src: str) -> str:
    return "https:" + src if src.startswith("//") else src


def prior_manifest_keys() -> tuple[set[str], set[tuple[str, str, str]]]:
    ids: set[str] = set(); keys: set[tuple[str, str, str]] = set()
    for path in REPORTS.glob("round*-image-manifest*.csv"):
        if path.name == "round121-image-manifest.csv":
            continue
        for row in read_csv(path):
            if row.get("id"):
                ids.add(row["id"])
                keys.add((row.get("id", ""), row.get("image_index", ""), row.get("src", "")))
    return ids, keys


def select(inventory: list[dict[str, str]], candidate: list[dict[str, str]]) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    inv_by_id: dict[str, list[dict[str, str]]] = {}
    for row in inventory:
        inv_by_id.setdefault(row["id"], []).append(row)
    ids = [r["id"] for r in candidate]
    if len(ids) != len(set(ids)):
        raise RuntimeError("candidate contains duplicate article IDs")
    prior_ids, prior_keys = prior_manifest_keys()
    if set(ids) & prior_ids:
        raise RuntimeError(f"candidate article overlap with prior manifest: {sorted(set(ids) & prior_ids)}")
    articles: list[dict[str, str]] = []; images: list[dict[str, str]] = []
    for c in candidate:
        aid = c["id"]
        group = sorted(inv_by_id.get(aid, []), key=lambda r: as_int(r.get("image_index")))
        expected_count = as_int(c.get("image_count"))
        if len(group) != expected_count:
            raise RuntimeError(f"candidate/inventory image count mismatch {aid}: {len(group)} != {expected_count}")
        if not group or not all(r.get("status") == "unreviewed" for r in group):
            raise RuntimeError(f"candidate group is not fully unreviewed: {aid}")
        indices = [as_int(r.get("image_index")) for r in group]
        if indices != list(range(1, len(group) + 1)):
            raise RuntimeError(f"non-contiguous group {aid}: {indices}")
        if any((r["id"], r["image_index"], r["src"]) in prior_keys for r in group):
            raise RuntimeError(f"candidate image-key overlap with prior manifest: {aid}")
        articles.append({**c, "image_count": str(len(group))}); images.extend(group)
    if len(images) != sum(as_int(r.get("image_count")) for r in candidate):
        raise RuntimeError("candidate image total invariant failed")
    return articles, images


def download_one(row: dict[str, str], dest: Path, timeout: int, attempts: int) -> dict[str, str]:
    target = dest / Path(row["local_file"]).name
    result = dict(row, download_status="failed", download_bytes="0", content_type="", download_error="")
    headers = {"User-Agent": "Mozilla/5.0 (compatible; qbl-image-review/1.0)", "Referer": "https://sooon.ai/"}
    last = ""
    for attempt in range(1, attempts + 1):
        temp: Path | None = None
        try:
            with requests.get(normalise_url(row["src"]), headers=headers, timeout=timeout, stream=True) as response:
                response.raise_for_status()
                with tempfile.NamedTemporaryFile(prefix=target.name + ".", suffix=".part", dir=dest, delete=False) as fh:
                    temp = Path(fh.name)
                    for chunk in response.iter_content(chunk_size=131072):
                        if chunk:
                            fh.write(chunk)
                size = temp.stat().st_size
                if size <= 0:
                    raise RuntimeError("empty response body")
                os.replace(temp, target)
                result.update(download_status="success", download_bytes=str(size), content_type=response.headers.get("content-type", ""))
                return result
        except Exception as exc:
            last = f"attempt {attempt}: {type(exc).__name__}: {exc}"
            if temp and temp.exists():
                temp.unlink()
    result["download_error"] = last
    return result


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--timeout", type=int, default=45)
    ap.add_argument("--attempts", type=int, default=3)
    ap.add_argument("--candidate", type=Path, default=CANDIDATE)
    ap.add_argument("--batch", type=Path, default=DEFAULT_BATCH)
    ap.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    ap.add_argument("--download-dir", type=Path, default=DEFAULT_DIR)
    args = ap.parse_args()
    inventory = read_csv(INVENTORY); candidate = read_csv(args.candidate)
    articles, image_rows = select(inventory, candidate)
    args.download_dir.mkdir(parents=True, exist_ok=True)
    rel_dir = str(args.download_dir.relative_to(ROOT)).replace("\\", "/")
    basis = "approved Round121 candidate; complete unreviewed groups; no article/image-key overlap with any prior manifest; dynamic 46-image budget"
    batch = [{"ordinal": a["ordinal"], "id": a["id"], "title": a["title"], "image_count": a["image_count"], "primary": "image_review", "status": "selected_pending_review", "selection_basis": basis, "download_dir": rel_dir} for a in articles]
    write_csv(args.batch, batch, ["ordinal", "id", "title", "image_count", "primary", "status", "selection_basis", "download_dir"])
    manifest: list[dict[str, str]] = []
    for seq, row in enumerate(image_rows, 1):
        name = f"{seq:02d}-{row['id']}-{row['image_index']}.jpg"
        manifest.append({**row, "local_file": f"{rel_dir}/{name}", "download_status": "pending", "download_bytes": "0", "content_type": "", "download_error": ""})
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        futures = {pool.submit(download_one, row, args.download_dir, args.timeout, args.attempts): i for i, row in enumerate(manifest)}
        for future in as_completed(futures):
            manifest[futures[future]] = future.result()
    fields = list(inventory[0].keys()) + ["local_file", "download_status", "download_bytes", "content_type", "download_error"]
    write_csv(args.manifest, manifest, fields)
    failed = [r for r in manifest if r["download_status"] != "success"]
    print(json.dumps({"round": 121, "articles": len(articles), "images": len(manifest), "downloaded": len(manifest)-len(failed), "failed": len(failed), "batch": str(args.batch), "manifest": str(args.manifest), "download_dir": str(args.download_dir)}, ensure_ascii=False, indent=2))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
