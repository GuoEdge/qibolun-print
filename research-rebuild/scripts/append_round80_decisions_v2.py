#!/usr/bin/env python3
import csv
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
R = ROOT / "research-rebuild/reports"
D = ROOT / "research-rebuild/data"
B = R / "live-manual-budget-batch-v2-round80-30k.csv"
F = R / "round80-fulltext.json"
T = R / "round80-decisions.tsv"
M = D / "print-topic-manual-decisions-v2.csv"


def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        return list(reader.fieldnames or []), list(reader)


_, batch = read_csv(B)
fields, manual = read_csv(M)
with T.open(encoding="utf-8-sig", newline="") as fh:
    decisions = list(csv.DictReader(fh, delimiter="\t"))
full = json.loads(F.read_text(encoding="utf-8"))
registry = {row["code"] for row in read_csv(D / "print-topic-registry-v2.csv")[1]}
ids = [row["id"] for row in batch]
assert len(batch) == len(decisions) == len(full) == 17
assert len(ids) == len(set(ids)) == 17
assert ids == [row["id"] for row in full]
assert [row["title"] for row in batch] == [row["title"] for row in full] == [row["title"] for row in decisions]
manual_by_id = {row["id"]: row for row in manual}
assert len(manual_by_id) == len(manual), "manual decision table has duplicate IDs"

out = []
updated = 0
for batch_row, decision in zip(batch, decisions):
    secondary = [value for value in decision["secondary"].split(";") if value]
    assert decision["primary"] in registry and all(value in registry for value in secondary)
    assert decision["primary"] not in secondary and len(secondary) <= 3
    assert decision["status"] in {"manual_confirmed", "manual_provisional"}
    assert decision["basis"].strip()
    if int(batch_row.get("deepseek_image_count") or 0):
        assert decision["status"] == "manual_provisional"
    row = {
        "id": batch_row["id"],
        "title": batch_row["title"],
        "primary_print_topic_code": decision["primary"],
        "secondary_print_topic_codes": ";".join(secondary),
        "classification_status": decision["status"],
        "decision_basis": decision["basis"],
        "review_note": f"Round 80 full text; body_chars={batch_row['body_char_count']}; batch={B.name}",
        "reviewer": "main-thread",
        "reviewed_at": date.today().isoformat(),
    }
    existing = manual_by_id.get(row["id"])
    if existing:
        for key in ("title", "primary_print_topic_code", "secondary_print_topic_codes", "classification_status", "decision_basis"):
            assert existing[key] == row[key], f"existing decision mismatch for {row['id']}: {key}"
        updated += 1
    else:
        out.append(row)

if out:
    with M.open("a", encoding="utf-8-sig", newline="") as fh:
        csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore").writerows(out)

print(json.dumps({
    "appended": len(out),
    "confirmed": sum(row["classification_status"] == "manual_confirmed" for row in out),
    "provisional": sum(row["classification_status"] == "manual_provisional" for row in out),
    "manual_total": len(manual) + len(out),
    "body_chars": sum(int(row["body_char_count"]) for row in batch),
    "already_present_and_matching": updated,
}, ensure_ascii=False, indent=2))
