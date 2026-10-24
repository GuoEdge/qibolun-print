#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Round180 image tail: fetch the source images for the 46 pending image articles.

Reads the article/ID list from the handoff snapshot, resolves each ``src`` in
``data/image-inventory.csv`` to an https URL, and downloads it into
``research-rebuild/image-review/round180/``.  Nothing is overwritten that
already exists; a failure is recorded in ``round180-fetch-log.json`` and NEVER
substituted with a neighbouring image.

Network scope: only the per-image asset URLs already recorded in the local
inventory.  This is not a site crawl and touches no authenticated endpoint, so
no Cookie / CSRF / session value is read, written or logged.
"""
from __future__ import annotations

import csv
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
R = ROOT / "research-rebuild"
SNAPSHOT = R / "reports/handoff-20260926/confirmed-with-image-work-snapshot.csv"
INVENTORY = R / "data/image-inventory.csv"
OUTDIR = R / "image-review/round180"


def main() -> int:
    tail = list(csv.DictReader(SNAPSHOT.open(encoding="utf-8-sig")))
    inv: dict[str, list[dict]] = {}
    for row in csv.DictReader(INVENTORY.open(encoding="utf-8-sig")):
        inv.setdefault(row["id"], []).append(row)

    OUTDIR.mkdir(parents=True, exist_ok=True)
    log = []
    ok = skip = fail = 0
    for art in tail:
        aid = art["id"]
        rows = sorted(inv.get(aid, []), key=lambda r: int(r["image_index"]))
        already = int(art["reviewed_image_count"] or 0)
        for row in rows:
            idx = int(row["image_index"])
            # The 5G record already has 15 visually reviewed images; the six
            # failures are retried here, the rest are kept as they are.
            if already and idx <= already:
                continue
            src = row["src"]
            url = src if src.startswith("http") else "https:" + src
            dest = OUTDIR / f"{art['ordinal']}-{aid}-{idx}.jpg"
            entry = {"ordinal": art["ordinal"], "id": aid, "title": art["title"],
                     "image_index": idx, "url": url, "path": str(dest.relative_to(ROOT))}
            if dest.exists() and dest.stat().st_size > 1024:
                entry["result"] = "cached"
                skip += 1
                log.append(entry)
                continue
            proc = subprocess.run(
                ["curl", "-sS", "-L", "--max-time", "45", "-o", str(dest), "-w", "%{http_code}", url],
                capture_output=True, text=True,
            )
            code = (proc.stdout or "").strip()
            size = dest.stat().st_size if dest.exists() else 0
            good = code == "200" and size > 1024
            if not good and dest.exists():
                dest.unlink()
            entry["http_status"] = code
            entry["bytes"] = size
            entry["result"] = "ok" if good else "failed"
            if good:
                ok += 1
            else:
                fail += 1
                entry["stderr"] = (proc.stderr or "").strip()[:300]
            log.append(entry)
            print(f"[{entry['result']:>6}] {art['title'][:14]:<16} img{idx} {code} {size}B", flush=True)

    (OUTDIR / "round180-fetch-log.json").write_text(
        json.dumps({"downloaded": ok, "cached": skip, "failed": fail,
                    "articles": len(tail), "entries": log}, ensure_ascii=False, indent=1),
        encoding="utf-8")
    print(json.dumps({"downloaded": ok, "cached": skip, "failed": fail}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
