#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append the 2026-09-22 manual full-text review batch (round 26)."""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "research-rebuild/data/print-topic-manual-decisions-v2.csv"

SPEC = [
    ("d259c0c0-7071-5286-a949-17610195fbc1", "烂尾", "A08", "A10;A13", "manual_confirmed", "正文全文+引用法规条文；中心是建设周期、人工材料工期、融资缺口与土地处置规则，结尾置于1990—2015城镇化和高杠杆金融史。", "法规与宏观数据需独立核验。"),
    ("e811680f-3bf9-5abb-a1a3-f81d9fe6e6ff", "理解的原理", "A03", "A06;A01", "manual_confirmed", "正文全文；中心是对理解的定义、共同文本与推论检验，并承认理解无法客观认证而需承担误差责任。", "图片依赖：否。"),
    ("33d69ccd-d68b-5046-bcdb-6eaf949dfda2", "良好沟通", "A07", "A06;A03", "manual_confirmed", "问题与正文全文；中心是沟通作为持续合作机制，及格线是让对方愿意继续对话，而非一次性退款结果。", "图片依赖：否。"),
    ("5acee43d-6551-5368-a690-20067a2a73be", "两害相权", "A10", "A13;A08", "manual_confirmed", "问题与正文全文；中心是武汉弘芯/7nm项目的政策补贴、专业执行与失败责任，并比较计划竞争和自由竞争。", "项目事实与数字需独立核验。"),
    ("793fedad-0114-584c-b2cd-f0e849348f97", "军衔", "A12", "A07;A20", "manual_confirmed", "正文全文；中心是军衔作为国家化、非个人化指挥关系和组织韧性的机制，比较私兵、官军及中欧历史。", "正文含两处收藏链接，仅作延伸，不作证据。"),
    ("2133f3d8-4ccb-5c0f-9c09-1539ab21c794", "财富观", "A08", "A11;A18;A05", "manual_provisional", "正文全文；中心是财富的本质、管理权、节俭、正外部性投资与匿名慈善，并以自然法、可持续性和子女供养作规则。", "系列标注未完待续，保留截断/续篇风险。"),
    ("7cdfab67-7ce3-5c7f-b628-0f120d0cf51b", "社会化抚养", "A05", "A10;A04", "manual_confirmed", "问题与正文全文；中心是社会化抚养对家庭多样性、评价体系及政府权力边界的影响，定位为家庭失败时的补充机制。", "外链仅作延伸，不作正文证据。"),
    ("953904db-2f8f-5b98-9a8e-87b15a4675ab", "学历贬值", "A04", "A08;A14", "manual_confirmed", "问题与正文全文；中心是文凭内部价值重估、学校的集体生活与身份塑造，以及教育知识转化为实践成果的条件。", "AI与宏观判断保留复核备注。"),
    ("32899ea5-e149-5a04-aeda-2dd2cab5f8b9", "乱伦", "A10", "A05;A02", "manual_provisional", "正文全文；中心是关系规范、近亲性行为的执法资源、举证成本与公共禁忌如何改变实际自由。", "法律史与事实论断需独立核查。"),
]


def main() -> int:
    with PATH.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        rows = list(reader)
        fields = list(reader.fieldnames or [])
    by_id = {row.get("id", ""): row for row in rows}
    added = 0
    updated = 0
    for aid, title, primary, secondary, status, basis, note in SPEC:
        row = {
            "id": aid,
            "title": title,
            "primary_print_topic_code": primary,
            "secondary_print_topic_codes": secondary,
            "classification_status": status,
            "decision_basis": basis,
            "review_note": note,
            "reviewer": "main-thread",
            "reviewed_at": "2026-09-22",
        }
        if aid in by_id:
            if by_id[aid] != row:
                by_id[aid].update(row)
                updated += 1
        else:
            rows.append(row)
            by_id[aid] = row
            added += 1
    with PATH.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    print(f"added={added} updated={updated} rows={len(rows)}")


if __name__ == "__main__":
    main()
