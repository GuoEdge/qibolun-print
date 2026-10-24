#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Round182: fetch + contact-sheet the last 5 articles whose images were still pending."""
from __future__ import annotations
import csv, json, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
R = ROOT / "research-rebuild"
SRC = R / "image-review/round182"; SRC.mkdir(parents=True, exist_ok=True)
IDS = ["c6afed4c-3d1b-5df4-8388-494f7d756c13", "f9d288d4-cbf7-51e0-ae6f-a7180096ce4c",
       "250b12b2-5530-527c-870c-a33dc4782e36", "c4bab8ec-36c8-546c-84b2-a9fa20cd813d",
       "c947b0a0-3a44-571d-bef7-8663f537fb19"]
inv = {}
for r in csv.DictReader((R / "data/image-inventory.csv").open(encoding="utf-8-sig")):
    inv.setdefault(r["id"], []).append(r)
COLS = {1:1,2:2,3:2,4:2,5:3,6:3,7:3,8:3,9:3,10:4,11:4,12:4,13:4,14:4}
log, index = [], {}
for aid in IDS:
    rows = sorted(inv[aid], key=lambda r: int(r["image_index"]))
    kept = []
    for row in rows:
        src = row["src"]; url = src if src.startswith("http") else "https:" + src
        dest = SRC / f"{row['ordinal']}-{aid}-{row['image_index']}.jpg"
        if not (dest.exists() and dest.stat().st_size > 1024):
            p = subprocess.run(["curl","-sS","-L","--max-time","45","-o",str(dest),"-w","%{http_code}",url],
                               capture_output=True, text=True)
            if (p.stdout or "").strip() != "200" or not dest.exists() or dest.stat().st_size <= 1024:
                if dest.exists(): dest.unlink()
                log.append({"id":aid,"title":row["title"],"image_index":int(row["image_index"]),
                            "result":"failed","http_status":(p.stdout or "").strip()})
                print(f"FAILED {row['title']} img{row['image_index']}"); continue
        log.append({"id":aid,"title":row["title"],"image_index":int(row["image_index"]),"result":"ok"})
        kept.append((dest, row))
    if not kept: continue
    cols = COLS.get(len(kept), 4); grid_rows = (len(kept)+cols-1)//cols
    out = SRC / f"{rows[0]['ordinal']}-{aid}.jpg"
    cmd = ["ffmpeg","-y","-loglevel","error"]
    for p,_ in kept: cmd += ["-i", str(p)]
    parts = [f"[{i}:v]scale=360:270:force_original_aspect_ratio=decrease,pad=360:270:(ow-iw)/2:(oh-ih)/2:color=white,setsar=1[v{i}]" for i in range(len(kept))]
    parts.append("".join(f"[v{i}]" for i in range(len(kept)))+f"concat=n={len(kept)}:v=1:a=0[cc]")
    parts.append(f"[cc]tile={cols}x{grid_rows}[out]")
    cmd += ["-filter_complex",";".join(parts),"-map","[out]","-frames:v","1",str(out)]
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0: print("SHEET FAIL", rows[0]["title"], p.stderr[:200]); continue
    index[aid] = {"ordinal":rows[0]["ordinal"],"title":rows[0]["title"],"images":len(kept),
                  "cols":cols,"rows":grid_rows,"sheet":str(out.relative_to(ROOT)),
                  "positions":{f"r{i//cols+1}c{i%cols+1}":e["image_index"] for i,(_,e) in enumerate(kept)}}
    print(f"ok {rows[0]['title'][:12]:<14} {len(kept)} imgs -> {cols}x{grid_rows}  {out.name}")
(SRC/"round182-fetch-log.json").write_text(json.dumps(log,ensure_ascii=False,indent=1),encoding="utf-8")
(SRC/"round182-contact-sheet-index.json").write_text(json.dumps(index,ensure_ascii=False,indent=1),encoding="utf-8")
print(json.dumps({"ok":sum(1 for e in log if e['result']=='ok'),"failed":sum(1 for e in log if e['result']=='failed'),"sheets":len(index)},ensure_ascii=False))
