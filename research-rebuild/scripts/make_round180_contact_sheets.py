#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build one labelled-free contact sheet per article for round180.

Position order is deterministic: reading order (left→right, top→bottom) equals
ascending ``image_index``.  A position→image_index index is written next to each
sheet so the audit note can refer to positions without ambiguity.  Sheets are
built with ffmpeg because Pillow is not installed in this environment.
"""
from __future__ import annotations

import csv
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
R = ROOT / "research-rebuild"
SRC = R / "image-review/round180"
SHEETS = SRC / "contact-sheets"

COLS = {1: 1, 2: 2, 3: 2, 4: 2, 5: 3, 6: 3, 7: 3, 8: 3, 9: 3, 10: 4, 11: 4, 12: 4,
        13: 4, 14: 4, 15: 4, 16: 4, 17: 5, 18: 5, 19: 5, 20: 5, 21: 5}


def grid(n: int) -> tuple[int, int]:
    c = COLS.get(n, 5)
    rows = (n + c - 1) // c
    return c, rows


def main() -> int:
    SHEETS.mkdir(parents=True, exist_ok=True)
    log = json.loads((SRC / "round180-fetch-log.json").read_text(encoding="utf-8"))
    by_article: dict[str, list[dict]] = {}
    for e in log["entries"]:
        if e.get("result") in ("ok", "cached"):
            by_article.setdefault(e["id"], []).append(e)

    made, skipped, index = 0, 0, {}
    for aid, entries in sorted(by_article.items(), key=lambda kv: kv[1][0]["ordinal"]):
        entries.sort(key=lambda e: e["image_index"])
        kept = [(ROOT / e["path"], e) for e in entries]
        kept = [(p, e) for p, e in kept if p.exists() and p.stat().st_size > 1024]
        paths = [p for p, _ in kept]
        if not paths:
            skipped += 1
            continue
        title = entries[0]["title"]
        ordinal = entries[0]["ordinal"]
        out = SHEETS / f"{ordinal}-{aid}.jpg"
        cols, rows = grid(len(paths))
        positions = {}
        for i, (_, e) in enumerate(kept):
            positions[f"r{i // cols + 1}c{i % cols + 1}"] = e["image_index"]
        cmd = ["ffmpeg", "-y", "-loglevel", "error"]
        for p in paths:
            cmd += ["-i", str(p)]
        parts = []
        for i in range(len(paths)):
            parts.append(
                f"[{i}:v]scale=360:270:force_original_aspect_ratio=decrease,"
                f"pad=360:270:(ow-iw)/2:(oh-ih)/2:color=white,setsar=1[v{i}]"
            )
        chain = "".join(f"[v{i}]" for i in range(len(paths)))
        parts.append(f"{chain}concat=n={len(paths)}:v=1:a=0[cc]")
        parts.append(f"[cc]tile={cols}x{rows}[out]")
        cmd += ["-filter_complex", ";".join(parts), "-map", "[out]", "-frames:v", "1", str(out)]
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode != 0 or not out.exists():
            print(f"FAIL {title} {proc.stderr[:200]}")
            skipped += 1
            continue
        index[aid] = {
            "ordinal": ordinal, "title": title, "images": len(paths),
            "cols": cols, "rows": rows, "sheet": str(out.relative_to(ROOT)),
            "positions": positions,
            "image_indices": [e["image_index"] for _, e in kept],
            "failed_image_indices": [e["image_index"] for e in log["entries"]
                                     if e["id"] == aid and e.get("result") == "failed"],
        }
        made += 1
        print(f"ok   {title[:16]:<18} {len(paths)} imgs -> tile {cols}x{rows}")
    (SRC / "round180-contact-sheet-index.json").write_text(
        json.dumps(index, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps({"sheets": made, "skipped": skipped}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
