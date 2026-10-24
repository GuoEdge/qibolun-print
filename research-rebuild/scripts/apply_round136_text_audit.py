#!/usr/bin/env python3
"""Apply Round136 body-first reviews while keeping image-dependent rows provisional."""
from __future__ import annotations
import argparse, csv, json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"

def read(path: Path, delimiter: str = ","):
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh, delimiter=delimiter)
        return list(reader.fieldnames or []), list(reader)

def write(path: Path, fields, rows, delimiter: str):
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, delimiter=delimiter, extrasaction="ignore")
        writer.writeheader(); writer.writerows(rows)
    tmp.replace(path)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--dry-run", action="store_true"); args = ap.parse_args()
    _, batch = read(REPORTS / "round136-selection.csv")
    fulltext = json.loads((REPORTS / "round136-fulltext.json").read_text(encoding="utf-8"))
    _, first = read(REPORTS / "round136-firsthalf-decisions.tsv", "\t")
    _, second = read(REPORTS / "round136-secondhalf-decisions.tsv", "\t")
    decisions = first + second
    assert len(batch) == len(fulltext) == len(decisions) == 20
    ids = [r["id"] for r in batch]
    assert ids == [r["id"] for r in fulltext] == [r["id"] for r in decisions]
    assert len(set(ids)) == 20
    assert [int(r["body_char_count"]) for r in batch] == [len(r.get("text") or "") for r in fulltext]
    assert sum(len(r.get("text") or "") for r in fulltext) == 19988
    _, registry = read(DATA / "print-topic-registry-v2.csv")
    codes = {r["code"] for r in registry}
    manual_fields, manual = read(DATA / "print-topic-manual-decisions-v2.csv")
    by_id = {r["id"]: r for r in manual}
    assert len(manual) == len(by_id) == 4305
    out_decisions, audits = [], []
    for b, article, d in zip(batch, fulltext, decisions):
        current = by_id[b["id"]]
        assert current["title"] == b["title"] == d["title"] == article["title"]
        primary, secondary, status = d["new_primary"], d["new_secondary"], d["status"]
        sec = [x for x in secondary.split(";") if x]
        assert primary in codes and len(sec) <= 3 and len(sec) == len(set(sec)) and all(x in codes and x != primary for x in sec)
        assert status == "manual_provisional", f"Round136 image-gated row must remain provisional: {b['id']}"
        already = current["primary_print_topic_code"] == primary and current["secondary_print_topic_codes"] == secondary and current["classification_status"] == status
        assert current["classification_status"] == "manual_provisional" or already
        basis, risk = d["basis"], d["risk_boundary"]
        assert "\t" not in basis and "\t" not in risk
        out_decisions.append({"id": b["id"], "title": b["title"], "old_primary": current["primary_print_topic_code"], "old_secondary": current["secondary_print_topic_codes"], "new_primary": primary, "new_secondary": secondary, "status": status, "decision": "round136_body_reread", "basis": basis, "risk_boundary": risk})
        audits.append({"id": b["id"], "title": b["title"], "text_chars": b["body_char_count"], "current_primary": current["primary_print_topic_code"], "current_secondary": current["secondary_print_topic_codes"], "recommended_primary": primary, "recommended_secondary": secondary, "recommended_status": status, "decision_basis": basis, "fact_risk": risk})
        current.update({"primary_print_topic_code": primary, "secondary_print_topic_codes": secondary, "classification_status": status, "decision_basis": basis, "review_note": f"Round136 full-text reread; body_chars={b['body_char_count']}; image evidence not visually reviewed; Fact-risk boundary: {risk}", "reviewer": f"{current.get('reviewer', 'main-thread')}+round136-text-reread".strip("+"), "reviewed_at": date.today().isoformat()})
    write(REPORTS / "round136-decisions.tsv", ["id","title","old_primary","old_secondary","new_primary","new_secondary","status","decision","basis","risk_boundary"], out_decisions, "\t")
    write(REPORTS / "round136-text-audit.tsv", ["id","title","text_chars","current_primary","current_secondary","recommended_primary","recommended_secondary","recommended_status","decision_basis","fact_risk"], audits, "\t")
    if not args.dry_run: write(DATA / "print-topic-manual-decisions-v2.csv", manual_fields, manual, ",")
    print(json.dumps({"round":136,"records":20,"body_chars":19988,"confirmed":0,"provisional":20,"dry_run":args.dry_run}, ensure_ascii=False, indent=2))

if __name__ == "__main__": main()
