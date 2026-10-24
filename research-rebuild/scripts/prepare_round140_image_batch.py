#!/usr/bin/env python3
"""Download a bounded Round140 image-review batch from the live selection."""
from __future__ import annotations
import csv, json, os, tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import requests
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"
SELECTION = REPORTS / "round140-image-selection.csv"
MANIFEST = REPORTS / "round140-image-manifest.csv"
DEST = ROOT / "research-rebuild/image-review/round140"

def read(path):
    with path.open(encoding="utf-8-sig", newline="") as fh: return list(csv.DictReader(fh))
def write(path, fields, rows):
    path.parent.mkdir(parents=True, exist_ok=True); tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore"); w.writeheader(); w.writerows(rows)
    tmp.replace(path)
def integer(v):
    try: return int(v or 0)
    except (TypeError, ValueError): return 0
def download(row):
    target = DEST / Path(row["local_file"]).name
    result = dict(row, download_status="failed", download_bytes="0", content_type="", download_error="")
    src = "https:" + row["src"] if row["src"].startswith("//") else row["src"]
    for attempt in range(1, 4):
        tmp = None
        try:
            with requests.get(src, headers={"User-Agent":"Mozilla/5.0 (compatible; qbl-image-review/1.0)","Referer":"https://sooon.ai/"}, timeout=45, stream=True) as resp:
                resp.raise_for_status()
                with tempfile.NamedTemporaryFile(prefix=target.name + ".", suffix=".part", dir=DEST, delete=False) as fh:
                    tmp = Path(fh.name)
                    for chunk in resp.iter_content(131072):
                        if chunk: fh.write(chunk)
                size = tmp.stat().st_size
                if size <= 0: raise RuntimeError("empty response body")
                with Image.open(tmp) as image:
                    image.verify()
                os.replace(tmp, target)
                result.update(download_status="success", download_bytes=str(size), content_type=resp.headers.get("content-type", "")); return result
        except Exception as exc:
            if tmp and tmp.exists(): tmp.unlink()
            result["download_error"] = f"attempt {attempt}: {type(exc).__name__}: {exc}"
    return result
def main():
    selection = read(SELECTION); inventory = read(DATA / "image-inventory.csv")
    selected = {r["id"] for r in selection}; by_id = {}
    for row in inventory: by_id.setdefault(row["id"], []).append(row)
    prior_reviewed = set(); reviewed_ids = set()
    for path in REPORTS.glob("round*-image-review.tsv"):
        for row in read(path):
            if row.get("id") and row.get("image_index"):
                prior_reviewed.add((row["id"], row["image_index"])); reviewed_ids.add(row["id"])
    for path in REPORTS.glob("round*-image-decisions.tsv"):
        for row in read(path):
            if row.get("id"): reviewed_ids.add(row["id"])
    manifest=[]; DEST.mkdir(parents=True, exist_ok=True)
    for article in selection:
        assert article["id"] not in reviewed_ids, f"historically reviewed article selected: {article['id']}"
        group = [r for r in sorted(by_id.get(article["id"], []), key=lambda r: integer(r.get("image_index"))) if r.get("status") == "unreviewed" and (r.get("id"), r.get("image_index")) not in prior_reviewed]
        expected = integer(article.get("deepseek_image_count"))
        assert expected > 0 and len(group) == expected, f"incomplete image group {article['id']}: {len(group)}/{expected}"
        for row in group:
            key=(row.get("id",""),row.get("image_index",""))
            rel=str(DEST.relative_to(ROOT)).replace("\\","/")
            manifest.append(dict(row, local_file=f"{rel}/{len(manifest)+1:02d}-{row['id']}-{row['image_index']}.jpg", reconciliation="round140"))
    if not manifest: raise SystemExit("no unreviewed images selected")
    assert 40 <= len(manifest) <= 50, f"image budget out of range: {len(manifest)}"
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures={pool.submit(download,row):i for i,row in enumerate(manifest)}
        for future in as_completed(futures): manifest[futures[future]]=future.result()
    fields=list(inventory[0])+["local_file","download_status","download_bytes","content_type","download_error"]
    write(MANIFEST, fields, manifest)
    failed=[r for r in manifest if r["download_status"] != "success"]
    print(json.dumps({"round":140,"articles":len({r['id'] for r in manifest}),"images":len(manifest),"downloaded":len(manifest)-len(failed),"failed":len(failed),"manifest":str(MANIFEST),"download_dir":str(DEST)},ensure_ascii=False,indent=2))
    raise SystemExit(1 if failed else 0)
if __name__ == "__main__": main()
