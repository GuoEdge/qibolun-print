#!/usr/bin/env python3
"""从已生成的书芯 DOCX 实测物理页数，刷新 spine_manifest.json（篇数/正文叶/物理页/脊宽）与测算表。
每一页都是一张顶层整页表格，故按节统计顶层 <w:tbl> 数即为页数。"""
import json, re, zipfile, glob
from pathlib import Path

BASE = Path(__file__).parent
ROOT = Path("/storage/Users/currentUser/Documents/岐伯论")
MAN = BASE / "spine_manifest.json"
PAPERS = {"70g纯质纸": 0.095, "80g道林纸": 0.088, "80g轻型纸": 0.130}


def count_pages(docx):
    xml = zipfile.ZipFile(docx).read("word/document.xml").decode("utf-8")
    body = xml[xml.index("<w:body>") + 8:]
    depth, sec_tables, per_sec, arts = 0, 0, [], 0
    for m in re.finditer(r"<w:tbl>|</w:tbl>|<w:sectPr[ >]", body):
        t = m.group(0)
        if t == "<w:tbl>":
            if depth == 0: sec_tables += 1
            depth += 1
        elif t == "</w:tbl>":
            depth -= 1
        else:
            # sectPr 只出现在段落 pPr 或 body 末尾，均不在表格内
            per_sec.append(sec_tables); sec_tables = 0
    return per_sec  # [前置页, 正文叶, 封底页]


def spine(pages, t):
    return round(pages / 2 * t + 0.5, 1)


def main():
    man = json.loads(MAN.read_text(encoding="utf-8"))
    cat = [json.loads(l) for l in (BASE / "workbook-40b-all-catalog.jsonl").open(encoding="utf-8") if l.strip()]
    rows = []
    for it in man:
        bm = Path(it["dir"]) / "build-manifest.json"
        docx = json.loads(bm.read_text(encoding="utf-8")).get("docx") if bm.exists() else None
        if not docx or not Path(docx).exists():
            cands = [p for p in glob.glob(it["dir"] + "/岐伯论·*.docx") if "外包封" not in p]
            docx = max(cands, key=lambda p: Path(p).stat().st_mtime)   # 目录有旧名残留时取最新构建
        secs = count_pages(docx)
        assert len(secs) == 3, (it["code"], secs)
        it["leaves"], it["pages"] = secs[1], sum(secs)
        it["spine_mm"] = spine(it["pages"], PAPERS["70g纯质纸"])
        rows.append(it)
    # 篇数：B02A/B/C 取各自 pagination 报告中的篇数，其余直接计编目
    for it in rows:
        rep = glob.glob(it["dir"] + f"/_pagination-report-{it['code']}.json")
        it["arts"] = len({x["篇"] for x in json.load(open(rep[0], encoding="utf-8"))}) if rep else it["arts"]
    MAN.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")

    tot_a = sum(r["arts"] for r in rows); tot_l = sum(r["leaves"] for r in rows); tot_p = sum(r["pages"] for r in rows)
    md = ["# 《岐伯论》55 册物理印装书脊厚度测算表", "",
          f"全书 {len(cat)} 篇（册内合计 {tot_a}），正文 {tot_l:,} 叶（含单元扉叶），物理 {tot_p:,} P。",
          "脊宽 = 物理页数 ÷ 2 × 单张厚度 + 0.5 mm（胶装/锁线余量）。物理页数由书芯 DOCX 实测。", "",
          "| # | 分册 | 篇数 | 正文叶 | 物理页 | " + " | ".join(f"{k}脊宽(mm)" for k in PAPERS) + " |",
          "|---|---|---|---|---|" + "---|" * len(PAPERS)]
    for r in rows:
        md.append(f"| {r['idx']} | {r['desc']} | {r['arts']} | {r['leaves']} | {r['pages']} | " +
                  " | ".join(str(spine(r["pages"], t)) for t in PAPERS.values()) + " |")
    (ROOT / "55册物理印装书脊厚度测算表.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    thin = min(rows, key=lambda r: r["pages"]); thick = max(rows, key=lambda r: r["pages"])
    print(f"已刷新 {len(rows)} 册：{tot_a} 篇 / {tot_l} 叶 / {tot_p} P；最薄 {thin['code']} {thin['pages']}P {thin['spine_mm']}mm，最厚 {thick['code']} {thick['pages']}P {thick['spine_mm']}mm")


if __name__ == "__main__":
    main()
