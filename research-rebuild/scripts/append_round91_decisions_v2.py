#!/usr/bin/env python3
"""Append reviewed Round 91 decisions and reconcile audited sports cases."""
import argparse
import csv
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"
BATCH = REPORTS / "live-manual-budget-batch-v2-round91-90k.csv"
FULLTEXT = REPORTS / "round91-fulltext.json"
DECISIONS = REPORTS / "round91-decisions.tsv"
MANUAL = DATA / "print-topic-manual-decisions-v2.csv"

parser = argparse.ArgumentParser()
parser.add_argument("--dry-run", action="store_true")
args = parser.parse_args()


def read_csv(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        return list(reader.fieldnames or []), list(reader)


_, batch = read_csv(BATCH)
with DECISIONS.open(encoding="utf-8-sig", newline="") as fh:
    decisions = list(csv.DictReader(fh, delimiter="\t"))
fulltext = json.loads(FULLTEXT.read_text(encoding="utf-8"))
fields, manual = read_csv(MANUAL)
registry_fields, registry = read_csv(DATA / "print-topic-registry-v2.csv")
codes = {row["code"] for row in registry}

assert len(batch) == len(decisions) == len(fulltext) == 48
assert [row["id"] for row in batch] == [row["id"] for row in fulltext]
assert [row["title"] for row in batch] == [row["title"] for row in decisions] == [row["title"] for row in fulltext]
assert [int(row["body_char_count"]) for row in batch] == [len(row.get("text") or "") for row in fulltext]
assert sum(int(row["body_char_count"]) for row in batch) == 89775
assert sum(int(row["body_char_count"]) for row in batch) <= 90000
assert all(int(row.get("deepseek_image_count") or 0) == 0 for row in batch)

by_id = {row["id"]: row for row in manual}
assert len(by_id) == len(manual), "duplicate ID in manual decision table"
assert by_id["52223443-33d7-5ad7-8000-2d7a71c54302"]["primary_print_topic_code"] == "A00"
assert by_id["52223443-33d7-5ad7-8000-2d7a71c54302"]["classification_status"] == "manual_provisional"
assert by_id["1a8ac9a0-031e-582d-bca0-7bded99e2260"]["primary_print_topic_code"] == "A09"
assert by_id["c996df2d-f43e-5f55-b0c9-adf98ae5eecd"]["primary_print_topic_code"] == "A15"
batch_ids = {row["id"] for row in batch}
assert not batch_ids.intersection(by_id), "Round 91 article already exists in manual decisions"
by_title = {row["title"]: row for row in fulltext}
for decision, article in zip(decisions, fulltext):
    secondary = [value for value in decision["secondary"].split(";") if value]
    assert decision["primary"] in codes and all(value in codes for value in secondary)
    assert decision["primary"] not in secondary and len(secondary) <= 3
    assert decision["status"] in {"manual_confirmed", "manual_provisional"}
    assert decision["basis"].strip()
    if decision["primary"] == "A00":
        assert decision["status"] == "manual_provisional" and "入口" in decision["basis"]

new_rows = []
for batch_row, decision in zip(batch, decisions):
    risk = decision.get("risk_note", "").strip()
    review_note = (
        f"Round 91 full text; body_chars={batch_row['body_char_count']}; "
        f"batch={BATCH.name}; independent reviews=round91 1-24 and 25-48; "
        "independent boundary/safety spot-check and focused A21 corpus review"
    )
    if risk:
        review_note += f"; claim/safety note: {risk}"
    new_rows.append({
        "id": batch_row["id"],
        "title": batch_row["title"],
        "primary_print_topic_code": decision["primary"],
        "secondary_print_topic_codes": ";".join(value for value in decision["secondary"].split(";") if value),
        "classification_status": decision["status"],
        "decision_basis": decision["basis"],
        "review_note": review_note,
        "reviewer": "main-thread",
        "reviewed_at": date.today().isoformat(),
    })

# These existing decisions were made before the new, sampled A21 boundary was
# adopted. Reassign only cases whose full article was independently checked.
corrections = {
    "52223443-33d7-5ad7-8000-2d7a71c54302": (
        "A21", "A04", "manual_confirmed",
        "全文讨论中国足球问题的深层成因，中心是群众体育生态、基层参与和赛事体系；体育教育与训练能力是实质副线。",
        "A21 boundary adopted after focused full-text review; former A00 directory-gap provisional decision resolved.",
    ),
    "1a8ac9a0-031e-582d-bca0-7bded99e2260": (
        "A21", "A09", "manual_confirmed",
        "中心是职业竞技成功的身体损伤代价；身体损伤及医疗限制构成实质副轴。",
        "A21 boundary review reassigned sports-centred article from A09; A09 retained as a supported secondary axis.",
    ),
    "c996df2d-f43e-5f55-b0c9-adf98ae5eecd": (
        "A21", "A15", "manual_confirmed",
        "中心是中国职业综合格斗赛事的前景；文化接受度及价值解释为实质副轴。",
        "A21 boundary review reassigned sports-centred article from A15; A15 retained for cultural reception.",
    ),
    "5d5b4502-5b35-5392-b79f-dd62408fb0dd": (
        "A17", "A21;A03", "manual_confirmed",
        "中心是民族自豪感尺度与对金牌的中性评价；体育规则判定和事实论证为副轴。",
        "A21 boundary audit confirmed the topic is clear; factual claims remain a separate verification risk.",
    ),
    "6dfcec2b-d201-5593-a38b-3a010adf24b3": (
        "A15", "A13;A16", "manual_confirmed",
        "以奥运会为设计、建筑、媒体技术和运动科技展示平台；工程与传播是副线。",
        "A21 boundary audit removed the weak A18 secondary; the article explicitly centres non-sport meanings.",
    ),
}

correction_count = 0
for aid, (primary, secondary, status, basis, note) in corrections.items():
    row = by_id[aid]
    assert row["primary_print_topic_code"] != primary or row["secondary_print_topic_codes"] != secondary
    row["primary_print_topic_code"] = primary
    row["secondary_print_topic_codes"] = secondary
    row["classification_status"] = status
    row["decision_basis"] = basis
    row["review_note"] += f"; {note}"
    row["reviewed_at"] = date.today().isoformat()
    correction_count += 1

# Resolve Qingbai Ti Yu separately by its verified corpus ID.
assert by_id["5d5b4502-5b35-5392-b79f-dd62408fb0dd"]["title"] == "清白体育"

if not args.dry_run:
    temporary = MANUAL.with_suffix(".csv.tmp")
    with temporary.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(manual)
        writer.writerows(new_rows)
    temporary.replace(MANUAL)

print(json.dumps({
    "round91_appended": len(new_rows),
    "round91_confirmed": sum(row["classification_status"] == "manual_confirmed" for row in new_rows),
    "round91_provisional": sum(row["classification_status"] == "manual_provisional" for row in new_rows),
    "sports_decisions_updated": correction_count,
    "manual_total_after": len(manual) + len(new_rows),
    "dry_run": args.dry_run,
}, ensure_ascii=False, indent=2))
