#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build per-topic print packages (分册) for the 4,305-article corpus.

Design
------
* One directory per print primary topic; a topic is split into volumes when its
  estimated page count exceeds ``--pages-per-volume`` (default 200 A4 pages at
  ~1,200 Chinese characters per page).
* Order inside a volume: publication date, then source ordinal (stable, no
  duplicates across volumes — every article appears exactly once).
* Each article block carries the print header (ordinal / title / date / primary
  and secondary topic / source ID and URL / official object-practice path /
  23-concept tags / evidence state), the question, the full body, and the kept
  images with their audit note.
* Markers are FLAGS, never relabelling: 【待审】【排除候选】【正文疑未完结】
  【图片缺 N 张】【空正文】【正文缺失】.

Nothing is reordered by guesswork and nothing is dropped: articles flagged as
exclusion candidates or material-insufficient still get printed, but they are
routed to the appendix volume instead of a topic volume (``--appendix`` on by
default), so a topic booklet contains only articles whose print topic is
settled.

Reads the corpus read-only; writes only under ``research-rebuild/print-<date>/``.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
from collections import defaultdict
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
R = ROOT / "research-rebuild"
CORPUS = ROOT / "sooon-q9adg-articles-v2.jsonl"
INDEX = R / "reports/print-index/print-research-index.csv"
REGISTRY = R / "data/print-topic-registry-v2.csv"
IMG_AUDIT = R / "reports/image-article-audit-v1.csv"
IMG_INV = R / "data/image-inventory.csv"
MANUAL = R / "data/print-topic-manual-decisions-v2.csv"
IMG_DIRS = [R / "image-review/round182", R / "image-review/round180"]
IMG_DIRS_ALL = [R / "image-review"]
CST = timezone(timedelta(hours=8))

EXCLUSION_CANDIDATES = {"兼得", "最大成长速度", "战马阉割", "活成这样", "各行其道", "基督教与食血"}
# 用户指令（2026-09-26）：正文为空的文章不进印装册。
# 注意：这里只影响印装包，语料与分类表中原样保留，未删除任何文章。
PRINT_EXCLUDE = {"e108515f-375c-53c9-8f6d-1ee2c16b275a",   # 最大成长速度（正文 0 字）
                 "c5354fb0-7345-5864-8522-2c0cfdad3c2e"}   # 战马阉割（正文 0 字）
SHORT_ANSWER_CHARS = 60
KEEP_DECISIONS = {
    "keep_selected_images", "keep_and_ocr", "keep_if_space_allows",
    "keep_3_architecture_omit_1_unrelated", "keep_image_1_omit_image_2",
    "optional_or_keep_selected", "omit_or_keep_as_illustration",
    "omit_or_keep_as_character_reference", "source_incomplete_review_valid_images_only",
}
DROP_DECISIONS = {"omit_images", "archive_images_only", "archive_and_investigate_mismatch"}
TERMINAL = "。！？”』）】…!?\"')】"


def load_corpus() -> dict[str, dict]:
    out = {}
    with CORPUS.open(encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                o = json.loads(line)
                out[o["id"]] = o
    return out


UNFINISHED_RE = re.compile(r"（\s*未完[，,]\s*待续\s*）|（\s*待续\s*）|\(未完[,，]?\s*待续\)")
GAP_RE = re.compile(r"截断|中断|残缺|不完整|文中断")


def body_flags(text: str, note_blob: str = "") -> list[str]:
    """Evidence-based flags only.

    The earlier tail-punctuation heuristic was dropped after review: it flagged
    178 complete articles whose bodies legitimately end with English text, a URL
    or the platform's related-reading list.  A flag now needs positive evidence:
    either the author's own 未完/待续 marker, or a truncation already recorded in
    the review notes of the decision table.
    """
    flags = []
    t = (text or "").strip()
    if not t:
        return ["空正文"]
    if UNFINISHED_RE.search(t):
        flags.append("正文标注未完待续")
    if GAP_RE.search(note_blob or ""):
        flags.append("正文缺失片段（复核已记）")
    return flags


def build_image_map() -> dict[tuple[str, int], Path]:
    """(article_id, image_index) -> first usable local jpg, preferring round180/182."""
    pat = re.compile(r"([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})-(\d+)\.jpg$")
    out: dict[tuple[str, int], Path] = {}
    for p in R.glob("image-review/**/*.jpg"):
        if p.stat().st_size < 1024:
            continue
        m = pat.search(p.name)
        if not m:
            continue
        key = (m.group(1), int(m.group(2)))
        cur = out.get(key)
        if cur is None or ("round18" in str(p) and "round18" not in str(cur)):
            out[key] = p
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=R / "print-20260926")
    ap.add_argument("--pages-per-volume", type=int, default=200)
    ap.add_argument("--chars-per-page", type=int, default=1200)
    ap.add_argument("--include-provisional", action="store_true", default=True)
    ap.add_argument("--appendix", action="store_true", default=True)
    ap.add_argument("--images", action="store_true", default=True)
    args = ap.parse_args()

    corpus = load_corpus()
    idx = list(csv.DictReader(INDEX.open(encoding="utf-8-sig")))
    reg = {r["code"]: r for r in csv.DictReader(REGISTRY.open(encoding="utf-8-sig"))}
    img_audit = {r["id"]: r for r in csv.DictReader(IMG_AUDIT.open(encoding="utf-8-sig"))}
    manual_note = {r["id"]: (r.get("review_note") or "") + " " + (r.get("decision_basis") or "")
                   for r in csv.DictReader(MANUAL.open(encoding="utf-8-sig"))}
    for rnd in (180, 182):
        p = R / f"image-review/round{rnd}/round{rnd}-image-decisions.tsv"
        if p.exists():
            for r in csv.DictReader(p.open(encoding="utf-8-sig"), delimiter="\t"):
                img_audit[r["id"]] = r
    inv = defaultdict(list)
    for r in csv.DictReader(IMG_INV.open(encoding="utf-8-sig")):
        inv[r["id"]].append(int(r["image_index"]))
    img_files = build_image_map()

    grep = re.compile(r"([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})-(\d+)\.jpg$")
    img_note = {}
    for rnd in (180, 182):
        p = R / f"image-review/round{rnd}/round{rnd}-image-review.tsv"
        if p.exists():
            for r in csv.DictReader(p.open(encoding="utf-8-sig"), delimiter="\t"):
                img_note[(r["id"], int(r["image_index"]))] = r["visual_note"]

    if args.out.exists():
        shutil.rmtree(args.out)
    args.out.mkdir(parents=True, exist_ok=True)

    groups: dict[str, list[dict]] = defaultdict(list)
    appendix: list[dict] = []
    not_printed: list[dict] = []
    for r in idx:
        aid = r["id"]
        a = corpus.get(aid, {})
        text = a.get("text") or ""
        rec = {
            "row": r, "id": aid, "text": text, "question": a.get("question") or "",
            "chars": int(r["body_char_count"] or 0),
            "topic": r["primary_print_topic"],
            "date": r["published_date"] or "", "ord": int(r["source_ordinal"] or 0),
            "flags": body_flags(text, manual_note.get(aid, "")),
        }
        if not text.strip():
            rec["flags"].append("正文缺失" if aid not in corpus else "空正文")
        if r["title"] in EXCLUSION_CANDIDATES:
            rec["flags"].append("排除候选")
        if rec["chars"] and rec["chars"] < SHORT_ANSWER_CHARS:
            rec["flags"].append("极短回答")
        if r["classification_status"] == "manual_provisional":
            rec["flags"].append("待审")
        if img_audit.get(aid, {}).get("failed_image_count", "0") not in ("", "0"):
            rec["flags"].append(f"图片缺 {img_audit[aid]['failed_image_count']} 张")
        if aid in PRINT_EXCLUDE:
            not_printed.append(rec)
            continue
        settled = (r["classification_status"] == "manual_confirmed"
                   and "排除候选" not in rec["flags"]
                   and "空正文" not in rec["flags"] and "正文缺失" not in rec["flags"])
        (groups[r["primary_print_topic"]] if settled else appendix).append(rec)

    manifest, written = [], []
    corpora_hash = hashlib.sha256(CORPUS.read_bytes()).hexdigest()
    gen = datetime.now(CST).isoformat()

    def emit(volume_recs, outdir: Path, vol_no, vol_total, code, name, desc, title_prefix):
        lines = [
            f"# {title_prefix}", "",
            f"- 专题代码：{code}　专题名称：{name}",
            f"- 专题界定：{desc or '（注册表未给出界定）'}",
            f"- 本册：第 {vol_no} / {vol_total} 册　收录 {len(volume_recs)} 篇　"
            f"正文字符 {sum(x['chars'] for x in volume_recs):,}",
            f"- 语料：`sooon-q9adg-articles-v2.jsonl`（4,305 篇）　SHA-256：`{corpora_hash}`",
            f"- 生成时间：{gen}　排序：发表日期 → 源序号（全库唯一，不重复）", "",
            "**标记约定**：`【待审】` 主题仍为暂定；`【排除候选】` 图片/正文过薄的剔除候选；",
            "`【正文标注未完待续】` 作者原文自带未完标记；`【正文缺失片段（复核已记）】` 复核记录已确认的正文缺口；",
            "`【图片缺 N 张】` 源图不可获取。标记只作提示，不改写原文、不改动分类状态。", "",
            "---", "",
        ]
        body = []
        for rec in volume_recs:
            r = rec["row"]
            head = [f"## {rec['ord']:>04d}　{r['title']}", ""]
            marks = "　".join(f"`【{f}】`" for f in rec["flags"])
            head.append(f"- 日期：{rec['date'] or '（无）'}　主专题：{rec['topic']} {name}"
                        + (f"　副专题：{r['secondary_print_topics']}" if r["secondary_print_topics"] else ""))
            head.append(f"- 源 ID：`{rec['id']}`"
                        + (f"　原文链接：{r['url']}" if r.get("url") else ""))
            if r.get("native_object_paths"):
                head.append(f"- 官方对象—实践路径：{r['native_object_paths']}")
            if r.get("concept_tags"):
                head.append(f"- 23 概念标签：{r['concept_tags']}")
            head.append(f"- 证据状态：{r['classification_status']}"
                        f"　初读：{r.get('reading_status') or '（无）'}"
                        f"　独立复核：{r.get('independent_review_status') or '（无）'}")
            if marks:
                head.append(f"- 标记：{marks}")
            head.append("")
            if rec["question"]:
                head += [f"**问**：{rec['question']}", ""]
            body += head + [rec["text"].strip() if rec["text"].strip() else "_（该篇正文为空或仅有图片，无可排印正文。）_", ""]
            if args.images and inv.get(rec["id"]):
                ia = img_audit.get(rec["id"], {})
                dec = ia.get("image_decision", "")
                kept = []
                for i in sorted(inv[rec["id"]]):
                    if dec in DROP_DECISIONS:
                        break
                    src = img_files.get((rec["id"], i))
                    if not src:
                        continue
                    destdir = outdir / "images"
                    destdir.mkdir(parents=True, exist_ok=True)
                    dest = destdir / f"{rec['ord']}-{rec['id']}-{i}.jpg"
                    if not dest.exists():
                        shutil.copy2(src, dest)
                    kept.append((i, dest.relative_to(outdir).as_posix(), img_note.get((rec["id"], i), "")))
                if kept:
                    body.append(f"<!-- 图片：{len(kept)} 张，审读结论见下 -->")
                    for i, rel, note in kept:
                        body.append(f"![图 {i}]({rel})")
                        if note:
                            body.append(f"*图 {i}（已视觉复核）：{note}*")
                    body.append("")
                else:
                    body.append("_（该篇图片经审读后决定不随册排印。）_\n")
            elif inv.get(rec["id"]):
                body.append("_（该篇含图，但图片未随册排印。）_\n")
            body.append("---\n")
        (outdir).mkdir(parents=True, exist_ok=True)
        fname = outdir / f"volume-{vol_no:02d}.md"
        fname.write_text("\n".join(lines + body), encoding="utf-8")
        manifest.append({
            "topic_code": code, "topic_name": name, "volume": vol_no, "volumes_total": vol_total,
            "articles": len(volume_recs), "body_chars": sum(x["chars"] for x in volume_recs),
            "est_pages": round(sum(x["chars"] for x in volume_recs) / args.chars_per_page),
            "file": str(fname.relative_to(ROOT)),
        })
        written.append(str(fname.relative_to(ROOT)))

    for code in sorted(groups):
        recs = sorted(groups[code], key=lambda x: (x["date"], x["ord"]))
        total_pages = sum(x["chars"] for x in recs) / args.chars_per_page
        nvol = max(1, -(-int(total_pages) // args.pages_per_volume))
        per = -(-len(recs) // nvol)
        name = reg.get(code, {}).get("name", "")
        desc = reg.get(code, {}).get("description", "")
        safe = re.sub(r"[／/]", "-", f"{code}-{name}")
        for v in range(nvol):
            chunk = recs[v * per:(v + 1) * per]
            if not chunk:
                continue
            emit(chunk, args.out / safe, v + 1, nvol, code, name, desc,
                 f"{code}　{name}　第 {v + 1} 册（共 {nvol} 册）")

    if args.appendix and appendix:
        recs = sorted(appendix, key=lambda x: (x["date"], x["ord"]))
        nvol = max(1, -(-int(sum(x["chars"] for x in recs) / args.chars_per_page) // args.pages_per_volume))
        per = -(-len(recs) // nvol)
        for v in range(nvol):
            chunk = recs[v * per:(v + 1) * per]
            if not chunk:
                continue
            emit(chunk, args.out / "99-附录-档案册", v + 1, nvol, "APPENDIX", "档案册（待审·排除候选·材料不足）",
                 "主专题经判断为待审、或属排除候选、或正文为空/缺失的文章，单独归档，不混入专题正册。",
                 f"附录　档案册　第 {v + 1} 册（共 {nvol} 册）")

    with (args.out / "PRINT-MANIFEST.csv").open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(manifest[0].keys()))
        w.writeheader(); w.writerows(manifest)

    plan = {
        "generated_at": gen, "corpus_sha256": corpora_hash,
        "chars_per_page": args.chars_per_page, "pages_per_volume": args.pages_per_volume,
        "volumes": len(manifest), "files": len(written),
        "total_articles_printed": sum(m["articles"] for m in manifest),
        "topic_volumes": [m for m in manifest if m["topic_code"] != "APPENDIX"],
        "appendix_volumes": [m for m in manifest if m["topic_code"] == "APPENDIX"],
        "appendix_articles": len(appendix),
        "excluded_from_print_by_user_request": [
            {"id": x["id"], "title": x["row"]["title"], "reason": "正文为空（0 字）",
             "corpus_retained": True} for x in not_printed],
    }
    (args.out / "PRINT-MANIFEST.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k: plan[k] for k in ("volumes", "files", "total_articles_printed", "appendix_articles")},
                     ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
