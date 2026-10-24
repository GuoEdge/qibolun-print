#!/usr/bin/env python3
"""Write a focused, non-mutating audit of 15 provisional-reason records."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
AUDIT = REPORTS / "provisional-reasons-audit-v2.csv"
CORPUS = ROOT / "sooon-q9adg-articles-v2.jsonl"
OUT = REPORTS / "round122-reason-audit.tsv"

# Deliberately mixed sample: boundary-first, then legacy-reason controls, with
# several very short records retained as negative controls.
SELECTED = [
    "026dafd1-371b-551e-936c-51fc9e27c377",  # 铺路石, 103 chars
    "6e462ebf-bbfe-5114-acdb-3441c560882a",  # 义和团, 336 chars
    "9af3f757-ffb6-5c9e-b461-afdf9ccea949",  # 奠仪几何, 872 chars
    "9afd3b59-0581-59a5-85b1-af4281fd1d3d",  # 强硬的读, 2205 chars
    "c2b25366-620d-53fe-8e3b-0cebc77f5de3",  # 各行其道, 1483 chars
    "d49c81f1-41ac-5540-b654-eb32492ccf33",  # 战时状态, 1083 chars
    "dd48459c-0fa3-5be0-8752-054105ce60c3",  # 援助/战争, 623 chars
    "ea7dd942-d9c3-5ff8-8c2e-0cd8767e5d54",  # 临终关怀, 1167 chars
    "f67c9dc5-6439-540a-8d4b-d84eccbd119a",  # 历史真实, 1195 chars
    "c760d4b4-4c9e-5766-8050-11dcfae50b93",  # 无指责, 90 chars
    "6957efab-016d-53af-b7df-8b42eb0833cf",  # 谦和话, 807 chars
    "0dea539e-626e-5a61-bac1-98f1390c42bc",  # 眼神不灵动, 1383 chars
    "2f4296c0-b9be-5bde-93fe-28743198c351",  # 色之为色也, 1539 chars
    "610f5c80-e08e-5b69-b9f7-2beb6563e578",  # 四正道, 79 chars
    "bad58134-0613-5973-843b-2bc93ebb9733",  # 去之前, 25 chars
]

# `verdict` is an audit recommendation only. It does not change the formal
# classification status. Short or source-incomplete records remain provisional.
JUDGMENT = {
    "026dafd1-371b-551e-936c-51fc9e27c377": ("continue_provisional", "insufficient_text", "正文仅约110字，只有一个简短情境和行动建议；无法稳定排除纪念、照料或一般生活建议等边界。"),
    "6e462ebf-bbfe-5114-acdb-3441c560882a": ("confirm_candidate", "medium", "正文围绕义和团组织、对外战争及失败风险连续展开，与A12主轴一致；史实断言仍需外部核验。"),
    "9af3f757-ffb6-5c9e-b461-afdf9ccea949": ("confirm_candidate", "high", "正文完整讨论丧葬礼金、费用承担和亲属沟通，A19的死亡祭祀/葬仪中心明确；财务与亲属事实不作外部确认。"),
    "9afd3b59-0581-59a5-85b1-af4281fd1d3d": ("confirm_candidate", "high", "正文以沙特外交转向、威慑与战略边界为连续论证，A12主轴稳定；现实外交事实不作外部确认。"),
    "c2b25366-620d-53fe-8e3b-0cebc77f5de3": ("confirm_candidate", "medium", "正文以国家/社会的两种互动模式及中国与欧洲历史例证展开，中心可归入权力与秩序的国际历史讨论；历史概括需外核。"),
    "d49c81f1-41ac-5540-b654-eb32492ccf33": ("confirm_candidate", "medium", "正文围绕战争失利、战场决策与应对方式展开，A12中心清楚；军事因果与具体事件未外部核验。"),
    "dd48459c-0fa3-5be0-8752-054105ce60c3": ("continue_provisional", "medium_low", "正文约623字，虽以俄乌战争援助为题，但战争伦理、援助政策与事实判断混杂，当前理由不足以排除A10/A11边界。"),
    "ea7dd942-d9c3-5ff8-8c2e-0cd8767e5d54": ("confirm_candidate", "medium", "正文连续讨论临终关怀、临终准备与照料细节，A19主轴可判；医疗效果和个案事实不作外部确认。"),
    "f67c9dc5-6439-540a-8d4b-d84eccbd119a": ("continue_provisional", "medium_low", "正文讨论历史真实性与解释标准，但A12与A03/A20边界交叉；现有正文证据不足以完成边界裁定。"),
    "c760d4b4-4c9e-5766-8050-11dcfae50b93": ("continue_provisional", "insufficient_text", "正文约96字，只有拒绝指责/资格判断的短句，无法稳定确认A06相对A01/A03的优先级。"),
    "6957efab-016d-53af-b7df-8b42eb0833cf": ("confirm_candidate", "medium", "正文围绕谦和、敌意转化、关系边界与防御策略展开，A07主轴连续；心理效果与个案归因未外部核验。"),
    "0dea539e-626e-5a61-bac1-98f1390c42bc": ("confirm_candidate", "medium", "正文以Apple Vision Pro、产品定位、成本与AR/VR路线作技术产业论证，A14主轴明确；产品性能和商业预测未外部核验。"),
    "2f4296c0-b9be-5bde-93fe-28743198c351": ("continue_provisional", "medium_low", "正文从性别/性规范延伸到原始社会、宗教与历史文化的大跨度解释，A02虽有中心但边界和事实风险仍较高。"),
    "610f5c80-e08e-5b69-b9f7-2beb6563e578": ("continue_provisional", "insufficient_text", "正文仅约84字、以格言式价值判断组成，无法把A11与A03/A05等论证或价值专题稳定区分。"),
    "bad58134-0613-5973-843b-2bc93ebb9733": ("continue_provisional", "insufficient_text", "正文仅约25字，只有临行前沟通的提问，尚无足够论证确定A19或其他关系/照料专题。"),
}


def text_chars(lexical: str, brief: str) -> int:
    try:
        root = json.loads(lexical or "{}")
    except json.JSONDecodeError:
        return len(brief or "")
    out: list[str] = []

    def visit(node):
        if isinstance(node, dict):
            if isinstance(node.get("text"), str):
                out.append(node["text"])
            for value in node.values():
                visit(value)
        elif isinstance(node, list):
            for value in node:
                visit(value)

    visit(root)
    return len("\n".join(out)) or len(brief or "")


def main() -> None:
    with AUDIT.open(encoding="utf-8-sig", newline="") as fh:
        audit_rows = {row["id"]: row for row in csv.DictReader(fh)}
    corpus = {}
    with CORPUS.open(encoding="utf-8") as fh:
        for line in fh:
            article = json.loads(line)
            if article.get("id") in SELECTED:
                corpus[article["id"]] = article
    assert set(SELECTED) <= set(audit_rows) and set(SELECTED) <= set(corpus)
    assert set(SELECTED) == set(JUDGMENT)

    fields = [
        "audit_round", "priority_basis", "id", "title", "current_primary",
        "current_status", "image_gate_flag", "source_incomplete_flag",
        "boundary_review_flag", "legacy_reason_flag", "reading_status",
        "body_chars", "text_evidence", "verdict", "confidence",
        "reason", "fact_boundary",
    ]
    rows = []
    for aid in SELECTED:
        a = audit_rows[aid]
        article = corpus[aid]
        verdict, confidence, reason = JUDGMENT[aid]
        priority = "boundary_review" if a["boundary_review_flag"] == "yes" else "legacy_reason_gap"
        if a["source_incomplete_flag"] == "yes":
            priority += "+source_incomplete"
        body_chars = text_chars(article.get("lexical", ""), article.get("brief", ""))
        rows.append({
            "audit_round": "122",
            "priority_basis": priority,
            "id": aid,
            "title": article.get("title", a.get("title", "")),
            "current_primary": a["primary"],
            "current_status": "manual_provisional",
            "image_gate_flag": a["image_gate_flag"],
            "source_incomplete_flag": a["source_incomplete_flag"],
            "boundary_review_flag": a["boundary_review_flag"],
            "legacy_reason_flag": a["legacy_reason_flag"],
            "reading_status": a["reading_status"],
            "body_chars": str(body_chars),
            "text_evidence": "正文可读性/篇幅/中心线索已检查；不把图片、官方候选或外部事实当作正文证据。",
            "verdict": verdict,
            "confidence": confidence,
            "reason": reason,
            "fact_boundary": "仅判断专题中心与边界；历史、政治、军事、医疗、心理、法律、产品效果等事实性主张仍未外部核验。",
        })
    with OUT.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
    print({"output": str(OUT), "rows": len(rows), "confirm_candidates": sum(r["verdict"] == "confirm_candidate" for r in rows), "continue_provisional": sum(r["verdict"] == "continue_provisional" for r in rows)})


if __name__ == "__main__":
    main()
