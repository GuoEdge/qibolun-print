#!/usr/bin/env python3
"""素问增量一键流程。

  1) python3 sooon_update.py fetch
     抓取新文 → 生成待复核表 units/pending-<时间>.json（每篇需填 booklet 与 unit）
  2) 人工复核/填写 pending 文件中每篇的 "booklet"（如 B25）与 "unit"（该册已有单元名）
  3) python3 sooon_update.py apply units/pending-<时间>.json
     合并语料 → 追加三份编目 → 写入单元表 → 输出受影响分册清单
  4) python3 /storage/Users/currentUser/Documents/岐伯论/rebuild_all_docx.py <分册...>
     然后 python3 sooon_update.py covers 更新书脊与外包封
"""
import json, shutil, subprocess, sys, time, glob
from collections import Counter
from pathlib import Path

ROOT = Path("/storage/Users/currentUser/Documents/岐伯论")
BASE = ROOT / "research-rebuild/reports/gemini-flash-reclassification-v1"
PY = "/data/service/hnp/bin/python3"
FETCH = ROOT / "research/scripts/fetch_sooon_increment.py"
INC_DIR = ROOT / "research/online-increment"
BUILD_CORPUS = BASE / "sooon-q9adg-articles-v4.jsonl"   # all-articles-merged-v3.jsonl 的链接目标
CATS = [BASE / f for f in ("workbook-40b-all-catalog.jsonl", "workbook-40b-all-catalog-v4.jsonl", "workbook-40b-all-catalog-v5.jsonl")]
UNITS = BASE / "units/out"
META_KEYS = ("volume_code", "booklet_name", "volume_prefix", "volume_full_title",
             "booklet_stem", "booklet_stem_title", "full_citation")
# 拆分子册在编目里各有独立 booklet_code，B02 例外（构建时按单元三分）
TS = time.strftime("%Y%m%d_%H%M%S")


def jl(p):
    return [json.loads(l) for l in Path(p).open(encoding="utf-8") if l.strip()]


def fetch():
    subprocess.run([PY, str(FETCH), "all"], check=True, cwd=str(FETCH.parent))
    inc = max(glob.glob(str(INC_DIR / "sooon-increment-2*.jsonl")), key=lambda p: Path(p).stat().st_mtime)
    known = {r["original_id"] for r in jl(CATS[0])}
    new = [r for r in jl(inc) if r["id"] not in known and (r.get("text") or "").strip()]
    if not new:
        print("没有新文章。"); return
    pending = {"increment": inc, "articles": [
        {"id": r["id"], "title": r["title"], "question": r.get("question") or "",
         "preview": (r.get("text") or "")[:200], "booklet": "", "unit": ""} for r in new]}
    out = BASE / f"units/pending-{TS}.json"
    out.write_text(json.dumps(pending, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"新文 {len(new)} 篇，待复核表：{out}")
    print("可选单元：每册单元名见 units/out/<册>.json")


def apply(pending_path):
    pend = json.loads(Path(pending_path).read_text(encoding="utf-8"))
    arts = pend["articles"]
    recs = jl(CATS[0])
    known = {r["original_id"] for r in recs}
    errs = []
    for a in arts:
        u = UNITS / f"{a['booklet']}.json"
        if not a["booklet"] or not u.exists():
            errs.append(f"{a['title']}: booklet 未填或不存在"); continue
        names = [x["name"] for x in json.loads(u.read_text(encoding="utf-8"))["units"]]
        if a["unit"] not in names:
            errs.append(f"{a['title']}: unit 须为 {names} 之一")
        if a["id"] in known:
            errs.append(f"{a['title']}: 已在编目中")
    if errs:
        print("\n".join(errs)); sys.exit(1)

    inc = {r["id"]: r for r in jl(pend["increment"])}
    # 语料
    corpus = {str(r["id"]): r for r in jl(BUILD_CORPUS)}
    for a in arts:
        corpus[a["id"]] = inc[a["id"]]
    shutil.copy2(BUILD_CORPUS, f"{BUILD_CORPUS}.bak_{TS}")
    with BUILD_CORPUS.open("w", encoding="utf-8") as f:
        for it in sorted(corpus.values(), key=lambda x: x["publishedAt"], reverse=True):
            f.write(json.dumps(it, ensure_ascii=False, separators=(",", ":")) + "\n")
    # 编目
    ordn = max(r["workbook_ordinal"] for r in recs) + 1
    new = []
    for a in sorted(arts, key=lambda a: inc[a["id"]]["publishedAt"]):
        src = inc[a["id"]]
        tmpl = Counter(tuple(r[k] for k in META_KEYS) for r in recs if r["booklet_code"] == a["booklet"]).most_common(1)[0][0]
        rec = {"workbook_ordinal": ordn, "original_id": a["id"], "title": src["title"],
               "published_at": src["publishedAt"], "question": src.get("question") or "",
               "booklet_code": a["booklet"], "text_len": len(src.get("text") or ""),
               "text_preview": (src.get("text") or "")[:150], "url": src["url"], "article_url": src["url"]}
        rec.update(dict(zip(META_KEYS, tmpl)))
        new.append(rec); a["ordinal"] = ordn; ordn += 1
    for p in CATS:
        shutil.copy2(p, f"{p}.bak_{TS}")
        with p.open("w", encoding="utf-8") as f:
            for r in recs + new:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
    # 单元表
    for a in arts:
        u = UNITS / f"{a['booklet']}.json"
        j = json.loads(u.read_text(encoding="utf-8"))
        for x in j["units"]:
            if x["name"] == a["unit"]:
                x["ordinals"] = sorted(x["ordinals"] + [a["ordinal"]])
        u.write_text(json.dumps(j, ensure_ascii=False, indent=1), encoding="utf-8")
    affected = sorted({a["booklet"] for a in arts})
    # B02 构建键为 B02A/B/C
    keys = [k for b in affected for k in (["B02A", "B02B", "B02C"] if b == "B02" else [b])]
    print(f"已追加 {len(new)} 篇（序号 {new[0]['workbook_ordinal']}–{new[-1]['workbook_ordinal']}），编目共 {len(recs) + len(new)} 篇")
    print("重建命令：", PY, ROOT / "rebuild_all_docx.py", " ".join(keys))


def covers():
    subprocess.run([PY, str(BASE / "update_spine_manifest.py")], check=True)
    subprocess.run(["node", str(BASE / "build_all_covers.js")], check=True, cwd=str(BASE))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "fetch": fetch()
    elif cmd == "apply" and len(sys.argv) > 2: apply(sys.argv[2])
    elif cmd == "covers": covers()
    else: print(__doc__)
