#!/usr/bin/env python3
"""Strengthen safety caveats identified by the Round 99 spot-check."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DECISIONS = REPORTS / "round99-decisions.tsv"
REVISIONS = {
    "抗骚扰": "文中包含夺取刀具、以物品制造追击障碍、自制辣椒喷雾及现场对抗等具体方案，可能显著升级冲突并造成伤亡；其器具合法性、喷雾制作/使用和报警策略未经专业核验，不应照做或作为安全指南，应优先离开危险现场并联系当地紧急服务。",
    "应急储备": "文中药品拆装、净水用品、煤油/火种、自卫工具和物资储量等具体做法未按地区、灾种、消防/医疗规范核验，可能导致药物误用、火灾、储备失效或人身伤害；不要直接照单执行，应遵从当地应急管理、消防及医疗专业指引。",
}


def read(path: Path, delimiter: str):
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh, delimiter=delimiter)
        return list(reader.fieldnames or []), list(reader)


def write(path: Path, fields, rows, delimiter):
    temp = path.with_suffix(path.suffix + ".tmp")
    with temp.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, delimiter=delimiter, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    temp.replace(path)


df, decisions = read(DECISIONS, "\t")
by_title = {row["title"]: row for row in decisions}
for title, risk in REVISIONS.items():
    row = by_title[title]
    row["risk_note"] = risk
write(DECISIONS, df, decisions, "\t")
print(f"Updated safety notes for {len(REVISIONS)} Round 99 articles.")
