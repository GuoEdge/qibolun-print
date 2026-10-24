#!/usr/bin/env python3
"""Promote six Round118 candidates after focused full-text reread."""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "research-rebuild/data"
REPORTS = ROOT / "research-rebuild/reports"
MANUAL = DATA / "print-topic-manual-decisions-v2.csv"
DECISIONS = REPORTS / "round118-decisions.tsv"

UPDATES = {
    "陵园": ("正文完整、主副边界清楚；地图/历史事实未外核不影响专题确认", "烈士陵园作为城市纪念设施及其历史形成、规划不可动的影响是中心"),
    "高尔顿钉板": ("全文完整且A03主轴明确；图片和概率/历史普遍性仅作未核验事实风险", "正文围绕随机扰动、预测边界与不得以高明替他人决策展开，认识论论证为主轴"),
    "侵略者": ("正文完整、战争/国际秩序主轴明确；历史案例与政治断言未外核", "正文围绕越境战争、侵略者定义及战后政治承认与国际秩序展开"),
    "濯我衣者": ("正文完整、工程/空间布局主轴明确；家装图片及尺寸/型号/安全效果未外核", "正文围绕洗衣机/烘干机放置、尺寸、人体工学、施工误差与可维护性展开"),
    "掐丝镂空": ("文字足以判定；材质、重量、年代/作者/价格未外核", "正文虽短但因果链闭合，材质结构与重量事实纠偏是主轴"),
    "无威": ("正文完整且家庭/代际主轴明确；叙述事实及教育、医学、法律效果未外核", "长篇按事件时间线与后续评论讨论儿童教育、夫妻共同决策、家庭权力协商和情绪承认"),
}


def read(path: Path, delimiter: str):
    with path.open(encoding="utf-8-sig", newline="") as fh:
        r = csv.DictReader(fh, delimiter=delimiter)
        return list(r.fieldnames or []), list(r)


def write(path: Path, fields, rows, delimiter: str):
    temp = path.with_suffix(path.suffix + ".tmp")
    with temp.open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, delimiter=delimiter, extrasaction="ignore")
        w.writeheader(); w.writerows(rows)
    temp.replace(path)


def main():
    fields, rows = read(MANUAL, ",")
    changed = []
    for row in rows:
        title = row.get("title", "")
        if title not in UPDATES:
            continue
        assert row.get("classification_status") == "manual_provisional", title
        row["classification_status"] = "manual_confirmed"
        row["review_note"] = UPDATES[title][0] + "; Round118 image review completed; no topic change; image limitations recorded per image; OCR and factual claims remain unverified."
        row["reviewer"] = (row.get("reviewer", "main-thread") + "+reread").strip("+")
        row["decision_basis"] = UPDATES[title][1]
        changed.append(title)
    assert sorted(changed) == sorted(UPDATES)
    write(MANUAL, fields, rows, ",")

    fields, decisions = read(DECISIONS, "\t")
    for row in decisions:
        if row.get("title") in UPDATES:
            row["status"] = "manual_confirmed"
            row["basis"] = UPDATES[row["title"]][1]
            row["risk_note"] = row.get("risk_note", "") + "；全文复读确认正文完整、主副专题边界清楚；外部事实仍未核验。"
    assert all(row.get("status") == "manual_confirmed" for row in decisions if row.get("title") in UPDATES)
    write(DECISIONS, fields, decisions, "\t")
    print({"promoted": changed, "count": len(changed)})


if __name__ == "__main__":
    main()
