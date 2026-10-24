#!/usr/bin/env python3
"""Apply Round139 body-first decisions to the formal manual classification."""
from __future__ import annotations
import argparse, csv, json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"

def read(path: Path, delimiter: str = ","):
    with path.open(encoding="utf-8-sig", newline="") as fh:
        r = csv.DictReader(fh, delimiter=delimiter)
        return list(r.fieldnames or []), list(r)

def write(path: Path, fields, rows, delimiter: str):
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, delimiter=delimiter, extrasaction="ignore")
        w.writeheader(); w.writerows(rows)
    tmp.replace(path)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--dry-run", action="store_true"); args = ap.parse_args()
    _, batch = read(REPORTS / "round139-selection.csv")
    fulltext = json.loads((REPORTS / "round139-fulltext.json").read_text(encoding="utf-8"))
    _, first = read(REPORTS / "round139-firsthalf-decisions.tsv", "\t")
    _, second = read(REPORTS / "round139-secondhalf-decisions.tsv", "\t")
    # Early Round139 first-half export omitted the literal decision column,
    # shifting basis/risk one field left. Normalize that recoverable layout
    # error before any formal-table write.
    for d in first:
        if d.get("risk_boundary") is None and d.get("basis") is not None:
            d["risk_boundary"], d["basis"], d["decision"] = d["basis"], d["decision"], "round139_body_reread"
    decisions = first + second
    assert len(batch) == len(fulltext) == len(decisions) == 7
    ids = [r["id"].strip() for r in batch]
    assert ids == [r["id"].strip() for r in fulltext] == [r["id"].strip() for r in decisions]
    assert len(set(ids)) == 7
    assert [int(r["body_char_count"]) for r in batch] == [len(r.get("text") or "") for r in fulltext]
    _, registry = read(DATA / "print-topic-registry-v2.csv")
    codes = {r["code"] for r in registry}
    manual_fields, manual = read(DATA / "print-topic-manual-decisions-v2.csv")
    by_id = {r["id"].strip(): r for r in manual}
    assert len(manual) == len(by_id) == 4305
    out_decisions, audits = [], []
    for b, article, d in zip(batch, fulltext, decisions):
        aid = b["id"].strip(); current = by_id[aid]
        assert current["title"] == b["title"] == d["title"] == article["title"]
        primary, secondary, status = d["new_primary"].strip(), d["new_secondary"].strip(), d["status"].strip()
        sec = [x for x in secondary.split(";") if x]
        assert primary in codes and len(sec) <= 3 and len(sec) == len(set(sec)) and all(x in codes and x != primary for x in sec)
        assert status in {"manual_confirmed", "manual_provisional"}
        basis, risk = d["basis"].strip(), d["risk_boundary"].strip()
        assert "\t" not in basis and "\t" not in risk
        out_decisions.append({"id": aid, "title": b["title"], "old_primary": current["primary_print_topic_code"], "old_secondary": current["secondary_print_topic_codes"], "new_primary": primary, "new_secondary": secondary, "status": status, "decision": "round139_body_reread", "basis": basis, "risk_boundary": risk})
        audits.append({"id": aid, "title": b["title"], "text_chars": b["body_char_count"], "current_primary": current["primary_print_topic_code"], "current_secondary": current["secondary_print_topic_codes"], "recommended_primary": primary, "recommended_secondary": secondary, "recommended_status": status, "decision_basis": basis, "fact_risk": risk})
        current.update({"primary_print_topic_code": primary, "secondary_print_topic_codes": secondary, "classification_status": status, "decision_basis": basis, "review_note": f"Round139 full-text reread; body_chars={b['body_char_count']}; Fact-risk boundary: {risk}", "reviewer": f"{current.get('reviewer', 'main-thread')}+round139-text-reread".strip("+"), "reviewed_at": date.today().isoformat()})
    write(REPORTS / "round139-decisions.tsv", ["id","title","old_primary","old_secondary","new_primary","new_secondary","status","decision","basis","risk_boundary"], out_decisions, "\t")
    write(REPORTS / "round139-firsthalf-decisions.tsv", ["id","title","old_primary","old_secondary","new_primary","new_secondary","status","decision","basis","risk_boundary"], first, "\t")
    write(REPORTS / "round139-text-audit.tsv", ["id","title","text_chars","current_primary","current_secondary","recommended_primary","recommended_secondary","recommended_status","decision_basis","fact_risk"], audits, "\t")
    if not args.dry_run: write(DATA / "print-topic-manual-decisions-v2.csv", manual_fields, manual, ",")
    print(json.dumps({"round":139,"records":7,"body_chars":sum(len(r.get("text") or "") for r in fulltext),"confirmed":sum(r["status"].strip() == "manual_confirmed" for r in decisions),"provisional":sum(r["status"].strip() == "manual_provisional" for r in decisions),"dry_run":args.dry_run}, ensure_ascii=False, indent=2))

if __name__ == "__main__": main()
