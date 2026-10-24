#!/usr/bin/env python3
"""Download the unreviewed image groups attached to Round136 articles."""
from __future__ import annotations
import csv, json, os, tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import requests

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"
INVENTORY = DATA / "image-inventory.csv"
SELECTION = REPORTS / "round136-selection.csv"
MANIFEST = REPORTS / "round136-image-manifest.csv"
DEST = ROOT / "research-rebuild/image-review/round136"

def read(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as fh: return list(csv.DictReader(fh))
def write(path: Path, fields, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore"); w.writeheader(); w.writerows(rows)
    tmp.replace(path)
def integer(v):
    try: return int(v or 0)
    except (TypeError, ValueError): return 0
def url(src): return "https:" + src if src.startswith("//") else src
def prior_keys():
    ids, keys, rows_by_key = set(), set(), {}
    for p in REPORTS.glob("round*-image-manifest*.csv"):
        for row in read(p):
            if row.get("id"):
                key = (row.get("id", ""), row.get("image_index", ""), row.get("src", ""))
                ids.add(row["id"]); keys.add(key); rows_by_key.setdefault(key, []).append(row)
    return ids, keys, rows_by_key
def download(row):
    target = DEST / Path(row["local_file"]).name
    result = dict(row, download_status="failed", download_bytes="0", content_type="", download_error="")
    last = ""
    for attempt in range(1, 4):
        tmp = None
        try:
            with requests.get(url(row["src"]), headers={"User-Agent":"Mozilla/5.0 (compatible; qbl-image-review/1.0)", "Referer":"https://sooon.ai/"}, timeout=45, stream=True) as resp:
                resp.raise_for_status()
                with tempfile.NamedTemporaryFile(prefix=target.name + ".", suffix=".part", dir=DEST, delete=False) as fh:
                    tmp = Path(fh.name)
                    for chunk in resp.iter_content(131072):
                        if chunk: fh.write(chunk)
                size = tmp.stat().st_size
                if size <= 0: raise RuntimeError("empty response body")
                os.replace(tmp, target)
                result.update(download_status="success", download_bytes=str(size), content_type=resp.headers.get("content-type", ""))
                return result
        except Exception as exc:
            last = f"attempt {attempt}: {type(exc).__name__}: {exc}"
            if tmp and tmp.exists(): tmp.unlink()
    result["download_error"] = last
    return result

def main():
    inventory = read(INVENTORY); selection = read(SELECTION)
    selected_ids = {r["id"] for r in selection}
    by_id = {}
    for row in inventory: by_id.setdefault(row["id"], []).append(row)
    prior_ids, existing_keys, prior_rows = prior_keys()
    manifest = []
    for article in selection:
        group = [r for r in sorted(by_id.get(article["id"], []), key=lambda r: integer(r.get("image_index"))) if r.get("status") == "unreviewed"]
        if not group: continue
        for row in group:
            key = (row.get("id", ""), row.get("image_index", ""), row.get("src", ""))
            # Round108-113 contain abandoned manifests with no downloaded or
            # reviewed state. Round136 is allowed to reconcile those rows;
            # any previously reviewed key remains protected from reuse.
            if key in existing_keys:
                assert all(r.get("status") != "reviewed" for r in prior_rows[key]), key
        rel = str(DEST.relative_to(ROOT)).replace("\\", "/")
        for row in group:
            manifest.append(dict(row, local_file=f"{rel}/{len(manifest)+1:02d}-{row['id']}-{row['image_index']}.jpg", reconciliation="prior_unreviewed_manifest" if (row.get("id", ""), row.get("image_index", ""), row.get("src", "")) in existing_keys else "new_round136"))
    assert len({r["id"] for r in manifest}) <= len(selected_ids)
    DEST.mkdir(parents=True, exist_ok=True)
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(download, row): i for i, row in enumerate(manifest)}
        for future in as_completed(futures): manifest[futures[future]] = future.result()
    fields = list(inventory[0]) + ["local_file", "download_status", "download_bytes", "content_type", "download_error"]
    write(MANIFEST, fields, manifest)
    failed = [r for r in manifest if r["download_status"] != "success"]
    print(json.dumps({"round":136,"articles":len({r['id'] for r in manifest}),"images":len(manifest),"downloaded":len(manifest)-len(failed),"failed":len(failed),"manifest":str(MANIFEST),"download_dir":str(DEST)}, ensure_ascii=False, indent=2))
    raise SystemExit(1 if failed else 0)
if __name__ == "__main__": main()
