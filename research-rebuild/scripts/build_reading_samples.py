#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build real-article reading-edition samples and no-page index skeletons."""
from __future__ import annotations

import csv
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
R = ROOT / "research-rebuild"
CORPUS = ROOT / "sooon-q9adg-articles-v2.jsonl"
INDEX = R / "reports/print-index/print-research-index.csv"
IMAGE_AUDIT = R / "reports/image-article-audit-v1.csv"
IMAGE_INV = R / "data/image-inventory.csv"
OUT = R / "print-design-20260927/reading-samples-real"
PRINT_PACKAGE = R / "print-20260926-rebuilt-v2"

SAMPLE_TITLES = [
    "自知其美",
    "多余的问题",
    "5G",
    "MMA",
    "各行其道",
]


def load_jsonl(path: Path) -> dict[str, dict]:
    data = {}
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                row = json.loads(line)
                data[row["id"]] = row
    return data


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def shorten_paths(value: str) -> str:
    return value.replace(";", "；") if value else "（无）"


def build_images() -> dict[str, list[int]]:
    out: dict[str, list[int]] = defaultdict(list)
    for row in load_rows(IMAGE_INV):
        try:
            out[row["id"]].append(int(row["image_index"]))
        except (KeyError, ValueError):
            continue
    # The audit inventory is authoritative for articles whose inventory rows are
    # incomplete but whose copied print-package images are available.
    for path in R.glob("print-20260926-rebuilt-v2/**/images/*.jpg"):
        m = re.search(r"-(?P<id>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})-(?P<idx>\\d+)\\.jpg$", path.name)
        if m:
            out[m.group("id")].append(int(m.group("idx")))
    for key in out:
        out[key] = sorted(set(out[key]))
    return out


def image_path(row: dict[str, str], index: int) -> str | None:
    code = row["primary_print_topic"]
    name = row["primary_print_topic_name"]
    safe = re.sub(r"[／/]", "-", f"{code}-{name}")
    candidate = PRINT_PACKAGE / safe / "images" / f"{int(row['source_ordinal'])}-{row['id']}-{index}.jpg"
    return str(candidate) if candidate.exists() else None


def article_block(row: dict[str, str], article: dict, image_indices: list[int]) -> list[str]:
    title = row["title"]
    body = (article.get("text") or "").strip()
    lines = [f"## {int(row['source_ordinal']):04d}　{title}", "", row.get("published_date") or "（日期未知）", "", "### 提问", "", article.get("question") or "（原始提问缺失）", "", "### 正文", "", body or "_（正文为空或仅由图片承载。）_", ""]
    if image_indices:
        lines += ["### 图片", "", f"本篇共有 {len(image_indices)} 张图片。正式排版时按原文顺序放置，并根据图片版面保留批注空间。", ""]
        for i in image_indices:
            path = image_path(row, i)
            if path:
                rel = path.replace(str(ROOT) + "/", "")
                lines += [f"![图 {i}]({rel})", f"图 {i}　已审图片，正式版按版心宽度排印。", ""]
            else:
                lines += [f"图 {i}　（图片文件未在当前印刷包中找到）", ""]
    lines += ["### 研究信息", "", f"原文链接：见本册来源索引，源序号 {row['source_ordinal']}", f"主专题：{row['primary_print_topic']} {row['primary_print_topic_name']}"]
    if row.get("secondary_print_topic_names"):
        lines.append(f"副专题：{row['secondary_print_topic_names'].replace(';', '；')}")
    if row.get("native_object_paths"):
        lines.append(f"官方路径：{shorten_paths(row['native_object_paths'])}")
    if row.get("concept_tags"):
        lines.append(f"概念：{row['concept_tags'].replace(';', '；')}")
    flags = []
    if row.get("classification_status") == "manual_provisional":
        flags.append("待审")
    if row.get("reading_status") in {"needs_reread", "missing_first_pass"}:
        flags.append(row["reading_status"])
    if row.get("source_body_state") != "text_present":
        flags.append(row.get("source_body_state") or "正文状态异常")
    if flags:
        lines.append("状态：" + "；".join(flags))
    lines += ["", "> 研究笔记", ">", "> ________________________________________________________________", ">", "> ________________________________________________________________", ">", "> ________________________________________________________________", "", "---", ""]
    return lines


def build_index(rows: list[dict[str, str]]) -> list[str]:
    by_topic: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_topic[row["primary_print_topic"]].append(row)
    lines = ["# 岐伯论阅读正文版目录与索引骨架", "", "本文件为无页码索引骨架。最终页码须在 PDF/DOCX 分页完成后回填。", "", "## 全书目录", ""]
    for code in sorted(by_topic):
        group = sorted(by_topic[code], key=lambda r: (r.get("published_date", ""), int(r["source_ordinal"])))
        dates = [r.get("published_date", "") for r in group if r.get("published_date")]
        lines.append(f"- {code} {group[0]['primary_print_topic_name']}：{len(group)} 篇；日期范围 {dates[0] if dates else '无'} 至 {dates[-1] if dates else '无'}")
    lines += ["", "## 源序号索引", "", "源序号｜标题｜日期｜主专题｜册号｜页码", ""]
    for row in sorted(rows, key=lambda r: int(r["source_ordinal"])):
        lines.append(f"{int(row['source_ordinal']):04d}｜{row['title']}｜{row.get('published_date','')}｜{row['primary_print_topic']} {row['primary_print_topic_name']}｜待排版｜待回填")
    lines += ["", "## 标题索引", "", "标题｜源序号｜日期｜主专题｜册号｜页码", ""]
    for row in sorted(rows, key=lambda r: (r["title"], int(r["source_ordinal"]))):
        lines.append(f"{row['title']}｜{int(row['source_ordinal']):04d}｜{row.get('published_date','')}｜{row['primary_print_topic']}｜待排版｜待回填")
    return lines


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    corpus = load_jsonl(CORPUS)
    rows = load_rows(INDEX)
    images = build_images()
    selected = [r for r in rows if r["title"] in SAMPLE_TITLES]
    selected.sort(key=lambda r: SAMPLE_TITLES.index(r["title"]))
    lines = ["# 岐伯论阅读正文版真实样章", "", "样章来自当前 v2 语料与最新印刷索引，用于确认阅读结构、篇末研究信息和批注空间。", ""]
    for row in selected:
        lines.extend(article_block(row, corpus[row["id"]], images.get(row["id"], [])))
    (OUT / "READING-SAMPLES-REAL.md").write_text("\n".join(lines), encoding="utf-8")
    (OUT / "INDEX-SKELETON.md").write_text("\n".join(build_index(rows)), encoding="utf-8")
    manifest = {
        "sample_titles": [r["title"] for r in selected],
        "sample_ordinals": [int(r["source_ordinal"]) for r in selected],
        "source_corpus": str(CORPUS.relative_to(ROOT)),
        "source_index": str(INDEX.relative_to(ROOT)),
        "note": "图片样章保留图片数量和版面提示；正式阅读版生成时嵌入已审图片文件。",
    }
    (OUT / "SAMPLE-MANIFEST.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
