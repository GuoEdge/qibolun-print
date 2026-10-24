#!/usr/bin/env python3
"""Create contact sheets only from the manifest-backed, verified image files."""
from __future__ import annotations

import argparse
import csv
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--round", type=int, required=True)
    args = parser.parse_args()
    manifest_path = REPORTS / f"round{args.round}-image-manifest.csv"
    rows = list(csv.DictReader(manifest_path.open(encoding="utf-8-sig", newline="")))
    files = []
    for row in rows:
        if row.get("download_status") != "success":
            continue
        path = ROOT / row["local_file"]
        try:
            with Image.open(path) as image:
                image.verify()
            files.append(path)
        except Exception as exc:
            print(f"skip invalid image {path}: {exc}")

    source = ROOT / f"research-rebuild/image-review/round{args.round}"
    thumb_w, thumb_h, label_h, columns, per_sheet = 420, 300, 42, 3, 9
    for sheet_number in range((len(files) + per_sheet - 1) // per_sheet):
        part = files[sheet_number * per_sheet:(sheet_number + 1) * per_sheet]
        rows_count = (len(part) + columns - 1) // columns
        sheet = Image.new("RGB", (columns * thumb_w, rows_count * (thumb_h + label_h)), "white")
        draw = ImageDraw.Draw(sheet)
        for index, path in enumerate(part):
            with Image.open(path) as image:
                image = image.convert("RGB")
                image.thumbnail((thumb_w - 12, thumb_h - 12))
                x = (index % columns) * thumb_w + (thumb_w - image.width) // 2
                y = (index // columns) * (thumb_h + label_h) + (thumb_h - image.height) // 2
                sheet.paste(image, (x, y))
            draw.text(
                ((index % columns) * thumb_w + 4,
                 (index // columns) * (thumb_h + label_h) + thumb_h + 4),
                path.name[:58],
                fill="black",
            )
        output = source / f"contact-sheet-{sheet_number + 1}.jpg"
        sheet.save(output, quality=92)
        print(output)


if __name__ == "__main__":
    main()
