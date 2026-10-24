#!/usr/bin/env python3
"""Download the approved Round122 fresh image groups."""
from __future__ import annotations

import csv, json, os, tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import requests

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
INVENTORY = ROOT / "research-rebuild/data/image-inventory.csv"
CANDIDATE = REPORTS / "round122-image-candidates.csv"
BATCH = REPORTS / "live-image-review-batch-v2-round122.csv"
MANIFEST = REPORTS / "round122-image-manifest.csv"
DEST = ROOT / "research-rebuild/image-review/round122"

def read(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as f: return list(csv.DictReader(f))
def write(path: Path, rows, fields):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore"); w.writeheader(); w.writerows(rows)
    tmp.replace(path)
def integer(v):
    try: return int(v or 0)
    except (TypeError, ValueError): return 0
def url(src): return "https:" + src if src.startswith("//") else src
def prior_keys():
    ids=set(); keys=set()
    for p in REPORTS.glob("round*-image-manifest*.csv"):
        for r in read(p):
            if r.get("id"):
                ids.add(r["id"]); keys.add((r.get("id",""),r.get("image_index",""),r.get("src","")))
    return ids, keys
def download(row, attempts=3):
    target = DEST / Path(row["local_file"]).name
    result=dict(row,download_status="failed",download_bytes="0",content_type="",download_error="")
    last=""
    for n in range(1, attempts+1):
        tmp=None
        try:
            with requests.get(url(row["src"]),headers={"User-Agent":"Mozilla/5.0 (compatible; qbl-image-review/1.0)","Referer":"https://sooon.ai/"},timeout=45,stream=True) as resp:
                resp.raise_for_status()
                with tempfile.NamedTemporaryFile(prefix=target.name+".",suffix=".part",dir=DEST,delete=False) as f:
                    tmp=Path(f.name)
                    for chunk in resp.iter_content(131072):
                        if chunk: f.write(chunk)
                size=tmp.stat().st_size
                if size<=0: raise RuntimeError("empty response body")
                os.replace(tmp,target)
                result.update(download_status="success",download_bytes=str(size),content_type=resp.headers.get("content-type","")); return result
        except Exception as exc:
            last=f"attempt {n}: {type(exc).__name__}: {exc}"
            if tmp and tmp.exists(): tmp.unlink()
    result["download_error"]=last; return result
def main():
    inv=read(INVENTORY); candidates=read(CANDIDATE); byid={}
    for r in inv: byid.setdefault(r["id"],[]).append(r)
    ids=[r["id"] for r in candidates]; prior_ids,prior=prior_keys()
    assert len(ids)==len(set(ids)) and not (set(ids)&prior_ids), sorted(set(ids)&prior_ids)
    selected=[]; images=[]
    for c in candidates:
        group=sorted(byid.get(c["id"],[]),key=lambda r:integer(r.get("image_index")))
        assert len(group)==integer(c["image_count"])
        assert group and all(r.get("status")=="unreviewed" for r in group)
        assert [integer(r.get("image_index")) for r in group]==list(range(1,len(group)+1))
        assert not any((r.get("id",""),r.get("image_index",""),r.get("src","")) in prior for r in group)
        selected.append(c); images.extend(group)
    assert 40<=len(images)<=50
    DEST.mkdir(parents=True,exist_ok=True); rel=str(DEST.relative_to(ROOT)).replace("\\","/")
    basis="approved Round122 candidate; complete fresh unreviewed groups; no article/image-key overlap with any prior manifest; dynamic 43-image budget"
    batch=[dict(c,image_count=str(len(byid[c["id"]])),primary="image_review",status="selected_pending_review",selection_basis=basis,download_dir=rel) for c in selected]
    write(BATCH,batch,["ordinal","id","title","image_count","primary","status","selection_basis","download_dir"])
    manifest=[]
    for seq,r in enumerate(images,1):
        manifest.append(dict(r,local_file=f"{rel}/{seq:02d}-{r['id']}-{r['image_index']}.jpg",download_status="pending",download_bytes="0",content_type="",download_error=""))
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures={pool.submit(download,r):i for i,r in enumerate(manifest)}
        for f in as_completed(futures): manifest[futures[f]]=f.result()
    fields=list(inv[0])+["local_file","download_status","download_bytes","content_type","download_error"]
    write(MANIFEST,manifest,fields)
    failed=[r for r in manifest if r["download_status"]!="success"]
    print(json.dumps({"round":122,"articles":len(selected),"images":len(manifest),"downloaded":len(manifest)-len(failed),"failed":len(failed),"batch":str(BATCH),"manifest":str(MANIFEST),"download_dir":str(DEST)},ensure_ascii=False,indent=2))
    raise SystemExit(1 if failed else 0)
if __name__ == "__main__": main()
