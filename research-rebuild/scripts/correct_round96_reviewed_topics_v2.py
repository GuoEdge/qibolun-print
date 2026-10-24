#!/usr/bin/env python3
"""Apply documented independent spot-check corrections to Round 96."""
import csv
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"
DECISIONS = REPORTS / "round96-decisions.tsv"
BATCH = REPORTS / "live-manual-budget-batch-v2-round96-90k.csv"
MANUAL = DATA / "print-topic-manual-decisions-v2.csv"

REVISIONS = {
    "还手": {
        "primary": "A05", "secondary": "A10",
        "basis": "正文中心是父母与子女冲突中的自我保护及关系管理；权利、警方和专业人员介入为副轴。",
        "risk_note": "家庭暴力及人身危险需结合具体情境求助当地专业机构；不要将文中的社会代价分析理解为应忍受暴力，面临即时危险应优先脱险并求助。文中法律与安全策略不构成专业意见。",
    },
    "知识的上限": {
        "primary": "A03", "secondary": "A13;A18",
        "basis": "正文讨论知识增长、传承能力及可能的认知与文明限度，核心是知识如何发展及其约束；技术扩展和生态风险是重要论据。",
    },
    "病根": {
        "primary": "A03", "secondary": "A09;A01",
        "basis": "正文将抑郁归因解释为辨认真伪对错的方法论缺陷，核心是论证与判断方法，而非诊疗过程。",
        "risk_note": "将重度抑郁归因于方法论缺陷并建议自助，属于未经证实且可能误导的医学/心理健康主张；这种归因可能加重患者自责，不能替代专业评估、治疗或危机支持。",
    },
    "性骚扰共识": {
        "primary": "A02", "secondary": "A10;A16",
        "basis": "以性骚扰指控中的同意、交往边界及回应方式为中心，司法裁定与公众传播为副主题。",
        "risk_note": "对被指控者的策略性道歉、法律责任与“交由公众判断”的论述存在重大法律及受害者安全风险；无论事实争议先道歉及公众将倾向宽容等建议未经验证，不应作为法律或危机处理指南。",
    },
    "肉身菩萨": {
        "primary": "A11", "secondary": "A02;A20",
        "basis": "通过宗教传统与历史文化比较讨论贞操规范及女性性行为的意义，宗教论证为中心，性别身体及历史演变为副题。",
    },
    "贫民窟": {
        "primary": "A10", "secondary": "A08",
        "basis": "以产权登记、治安秩序、政府治理和贫民窟持续机制解释城市治理差异，国家法律制度为中心。",
    },
    "迹不代心": {
        "primary": "A20", "secondary": "A06;A17",
        "basis": "以日本社会规范及其历史—社会适应路径解释关系义务如何替代爱的伦理判断；亲密关系与日本社会身份为副轴。",
    },
    "密码安全": {
        "primary": "A13", "secondary": "-",
        "basis": "正文中心是个人账号密码的构造、分级与保管方法，属于技术应用与安全实践。",
    },
}


def read_table(path: Path, delimiter: str = ","):
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh, delimiter=delimiter)
        return list(reader.fieldnames or []), list(reader)


def write_table(path: Path, fields: list[str], rows: list[dict[str, str]], delimiter: str = ","):
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, delimiter=delimiter, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    temporary.replace(path)


batch_fields, batch = read_table(BATCH)
decision_fields, decisions = read_table(DECISIONS, "\t")
manual_fields, manual = read_table(MANUAL)
assert len(batch) == len(decisions) == 50
assert [row["id"] for row in batch] == [row["id"] for row in decisions]
assert len({row["id"] for row in manual}) == len(manual)
batch_by_title = {row["title"]: row for row in batch}
decision_by_title = {row["title"]: row for row in decisions}
manual_by_id = {row["id"]: row for row in manual}

for title, revision in REVISIONS.items():
    assert title in batch_by_title and title in decision_by_title
    decision = decision_by_title[title]
    master = manual_by_id[batch_by_title[title]["id"]]
    assert master["title"] == title
    for key, value in (("primary", revision["primary"]), ("secondary", revision["secondary"])):
        decision[key] = value
    decision["basis"] = revision["basis"]
    if "risk_note" in revision:
        decision["risk_note"] = revision["risk_note"]

    master["primary_print_topic_code"] = revision["primary"]
    master["secondary_print_topic_codes"] = "" if revision["secondary"] == "-" else revision["secondary"].replace(";", ";")
    master["decision_basis"] = revision["basis"]
    if "risk_note" in revision:
        risk = revision["risk_note"]
    else:
        risk = decision.get("risk_note", "").strip()
    note = (
        f"Round 96 full text; body_chars={batch_by_title[title]['body_char_count']}; "
        f"batch={BATCH.name}; independent reads=round96 first 1-25 and second 26-50; "
        "independent spot-check corrections applied; risk notes separated from topic status"
    )
    if risk:
        note += f"; claim/safety note: {risk}"
    master["review_note"] = note
    master["reviewer"] = "main-thread+independent-review"
    master["reviewed_at"] = date.today().isoformat()

write_table(DECISIONS, decision_fields, decisions, "\t")
write_table(MANUAL, manual_fields, manual)
print(f"Applied {len(REVISIONS)} independent Round 96 spot-check corrections.")
