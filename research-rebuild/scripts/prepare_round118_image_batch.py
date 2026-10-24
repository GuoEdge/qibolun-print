#!/usr/bin/env python3
"""Select/download Round118, prioritizing provisional articles as whole groups.

This script deliberately writes only the Round118 report files and image-review
directory. It never changes the inventory, manual decisions, or derived indexes.
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
MANUAL = ROOT / "research-rebuild/data/print-topic-manual-decisions-v2.csv"
REPORTS = ROOT / "research-rebuild/reports"
DEFAULT_BATCH = REPORTS / "live-image-review-batch-v2-round118.csv"
DEFAULT_MANIFEST = REPORTS / "round118-image-manifest.csv"
DEFAULT_DIR = ROOT / "research-rebuild/image-review/round118"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    tmp.replace(path)


def prior_article_ids() -> set[str]:
    ids: set[str] = set()
    for path in REPORTS.glob("round*-image-manifest*.csv"):
        if path.name == "round118-image-manifest.csv":
            continue
        for row in read_csv(path):
            if row.get("id"):
                ids.add(row["id"])
    return ids


def as_int(v: str | None) -> int:
    try:
        return int(v or 0)
    except (TypeError, ValueError):
        return 0


def download_one(row: dict[str, str], dest: Path, timeout: int, attempts: int) -> dict[str, str]:
    src = row["src"]
    url = "https:" + src if src.startswith("//") else src
    target = dest / Path(row["local_file"]).name
    out = dict(row, download_status="failed", download_bytes="0", content_type="", download_error="")
    headers = {"User-Agent": "Mozilla/5.0 (compatible; qbl-image-review/1.0)", "Referer": "https://sooon.ai/"}
    last = ""
    for attempt in range(1, attempts + 1):
        temp: Path | None = None
        try:
            with requests.get(url, headers=headers, timeout=timeout, stream=True) as response:
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
                out.update(download_status="success", download_bytes=str(size), content_type=response.headers.get("content-type", ""))
                return out
        except Exception as exc:
            last = f"attempt {attempt}: {type(exc).__name__}: {exc}"
            if temp and temp.exists():
                temp.unlink()
    out["download_error"] = last
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--timeout", type=int, default=45)
    ap.add_argument("--attempts", type=int, default=3)
    ap.add_argument("--batch", type=Path, default=DEFAULT_BATCH)
    ap.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    ap.add_argument("--download-dir", type=Path, default=DEFAULT_DIR)
    args = ap.parse_args()

    inventory = read_csv(INVENTORY)
    manual = {r["id"]: r for r in read_csv(MANUAL)}
    prior = prior_article_ids()
    groups: dict[str, list[dict[str, str]]] = {}
    for row in inventory:
        if row.get("status") != "unreviewed" or row.get("id") in prior:
            continue
        groups.setdefault(row["id"], []).append(row)
    # Round118 is intentionally the complete set of eligible provisional groups;
    # 46 source images keeps the whole-group budget close to 50.
    selected_ids = [aid for aid, rs in sorted(groups.items(), key=lambda kv: as_int(kv[1][0].get("ordinal")))
                    if manual.get(aid, {}).get("classification_status") == "manual_provisional"]
    if not selected_ids:
        raise RuntimeError("no eligible provisional groups")
    selected = []
    for aid in selected_ids:
        rs = sorted(groups[aid], key=lambda r: as_int(r.get("image_index")))
        expected = list(range(1, len(rs) + 1))
        got = [as_int(r.get("image_index")) for r in rs]
        if got != expected:
            raise RuntimeError(f"non-contiguous group {aid}: {got}")
        selected.extend(rs)
    args.download_dir.mkdir(parents=True, exist_ok=True)
    batch = []
    for aid in selected_ids:
        first = groups[aid][0]
        batch.append({"ordinal": first["ordinal"], "id": aid, "title": first["title"],
                      "image_count": str(len(groups[aid])), "primary": "image_review",
                      "status": "selected_pending_review",
                      "selection_basis": "all eligible manual_provisional groups; whole groups; no prior manifest overlap",
                      "download_dir": str(args.download_dir.relative_to(ROOT)).replace("\\", "/")})
    write_csv(args.batch, batch, ["ordinal", "id", "title", "image_count", "primary", "status", "selection_basis", "download_dir"])
    manifest = []
    for seq, row in enumerate(selected, 1):
        name = f"{seq:02d}-{row['id']}-{row['image_index']}.jpg"
        manifest.append({**row, "local_file": str((args.download_dir / name).relative_to(ROOT)).replace("\\", "/"),
                         "download_status": "pending", "download_bytes": "0", "content_type": "", "download_error": ""})
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        futures = {pool.submit(download_one, row, args.download_dir, args.timeout, args.attempts): i for i, row in enumerate(manifest)}
        for future in as_completed(futures):
            manifest[futures[future]] = future.result()
    fields = list(inventory[0].keys()) + ["local_file", "download_status", "download_bytes", "content_type", "download_error"]
    write_csv(args.manifest, manifest, fields)
    failed = [r for r in manifest if r["download_status"] != "success"]
    print(json.dumps({"articles": len(selected_ids), "images": len(manifest), "downloaded": len(manifest)-len(failed),
                      "failed": len(failed), "batch": str(args.batch), "manifest": str(args.manifest),
                      "download_dir": str(args.download_dir)}, ensure_ascii=False, indent=2))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
