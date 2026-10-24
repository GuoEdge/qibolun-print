#!/usr/bin/env python3
"""Export a selected live-manual CSV to verified full-text and image manifests."""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CORPUS = ROOT / "sooon-q9adg-articles-v2.jsonl"
IMAGES = ROOT / "research-rebuild/data/image-inventory.csv"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", type=Path, required=True)
    ap.add_argument("--fulltext", type=Path, required=True)
    ap.add_argument("--images", type=Path, required=True)
    args = ap.parse_args()

    selected = read_csv(args.batch)
    if not 0 < len(selected) <= 50:
        raise SystemExit(f"batch size must be 1..50, got {len(selected)}")
    selected_ids = [row["id"] for row in selected]
    if len(selected_ids) != len(set(selected_ids)):
        raise SystemExit("duplicate IDs in selected batch")

    articles: dict[str, dict] = {}
    with CORPUS.open(encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                article = json.loads(line)
                if article.get("id"):
                    articles[str(article["id"])] = article

    out = []
    for row in selected:
        article = articles.get(row["id"])
        if article is None:
            raise SystemExit(f"missing article {row['id']}")
        text = article.get("text") or ""
        if article.get("title", "") != row.get("title", ""):
            raise SystemExit(f"title mismatch {row['id']}")
        if len(text) != int(row.get("body_char_count") or 0):
            raise SystemExit(f"body length mismatch {row['id']}")
        out.append(
            {
                "source_ordinal": int(row["source_ordinal"]),
                "id": row["id"],
                "title": article.get("title", ""),
                "question": article.get("question", ""),
                "text": text,
                "image_count": int(row.get("deepseek_image_count") or 0),
                "image_checked": False,
                "evidence_note": "正文已导出；图片尚未完成视觉审读，不能据此确认最终分类。",
            }
        )

    image_rows = [r for r in read_csv(IMAGES) if r.get("id") in set(selected_ids)]
    image_rows.sort(key=lambda r: (int(r.get("ordinal") or 0), int(r.get("image_index") or 0)))
    args.fulltext.parent.mkdir(parents=True, exist_ok=True)
    args.images.parent.mkdir(parents=True, exist_ok=True)
    args.fulltext.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    with args.images.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=read_csv(IMAGES)[0].keys())
        writer.writeheader()
        writer.writerows(image_rows)

    print(
        json.dumps(
            {
                "records": len(out),
                "body_chars": sum(len(r["text"]) for r in out),
                "image_manifest_records": len(image_rows),
                "fulltext": str(args.fulltext),
                "images": str(args.images),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
