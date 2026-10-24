#!/usr/bin/env python3
"""Apply Round130 body-first reread decisions."""
from __future__ import annotations
import argparse, csv, json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"
parser = argparse.ArgumentParser(); parser.add_argument("--dry-run", action="store_true"); args = parser.parse_args()

def read(path, delimiter=","):
    with path.open(encoding="utf-8-sig", newline="") as f:
        r = csv.DictReader(f, delimiter=delimiter); return list(r.fieldnames or []), list(r)

def write(path, fields, rows, delimiter):
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, delimiter=delimiter, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    tmp.replace(path)

def main():
    _, batch = read(REPORTS/"round130-selection.csv")
    full = json.loads((REPORTS/"round130-fulltext.json").read_text(encoding="utf-8"))
    _, first = read(REPORTS/"round130-firsthalf-decisions.tsv", "\t")
    _, second = read(REPORTS/"round130-secondhalf-decisions.tsv", "\t")
    src = first + second
    assert len(batch) == len(full) == len(src) == 27
    assert [x["id"] for x in batch] == [x["id"] for x in full] == [x["id"] for x in src]
    assert sum(len(x.get("text") or "") for x in full) == 29932
    assert len({x["id"] for x in src}) == 27
    _, registry = read(DATA/"print-topic-registry-v2.csv")
    codes = {x["code"] for x in registry}
    manual_fields, manual = read(DATA/"print-topic-manual-decisions-v2.csv")
    byid = {x["id"]: x for x in manual}; assert len(byid) == len(manual) == 4305
    decisions=[]; audits=[]; updates=[]
    overrides = {
        # Adjudicated after the strict blind sample.  The article says
        # siblings/kin, so A05 is more precise than the intimate-relationship
        # route; medical service cooperation remains A07;涉密 is primarily a
        # legal/procedural responsibility question.
        "涉密": {
            "primary": "A10", "secondary": "A07",
            "basis": "正文虽仅120字，但全部围绕涉密身份、出境审批、涉密电脑携带和安全漏洞的责任链，最后提醒慎接涉密项目；国家法律、司法与制度责任为主轴，职场组织与合作者责任为副轴。",
            "risk": "具体案件事实、法域、保密等级、刑罚和跨境法律适用均未独立核验；不构成保密、出境、刑事或合规法律意见。",
        },
    }
    # The rereaders' body-based decisions are retained; no machine candidate is promoted implicitly.
    for b, a, s in zip(batch, full, src):
        cur = byid[b["id"]]; assert cur["title"] == b["title"]
        override = overrides.get(b["title"], {})
        p = override.get("primary", s["new_primary"])
        sec = override.get("secondary", s["new_secondary"])
        status = override.get("status", s["status"])
        secs=[x for x in sec.split(";") if x]
        assert p in codes and all(x in codes and x != p for x in secs)
        assert len(secs) <= 3 and len(secs) == len(set(secs))
        assert len(a.get("text") or "") == int(b["body_char_count"])
        basis = override.get("basis", s["basis"])
        risk = override.get("risk", s["risk_boundary"])
        decisions.append({"id":b["id"],"title":b["title"],"old_primary":cur["primary_print_topic_code"],"old_secondary":cur["secondary_print_topic_codes"],"new_primary":p,"new_secondary":sec,"status":status,"decision":"adjudicated_reread","basis":basis,"risk_boundary":risk})
        audits.append({"id":b["id"],"title":b["title"],"text_chars":b["body_char_count"],"current_primary":cur["primary_print_topic_code"],"current_secondary":cur["secondary_print_topic_codes"],"recommended_primary":p,"recommended_secondary":sec,"recommended_status":status,"decision_basis":basis,"fact_risk":risk})
        desired={"primary_print_topic_code":p,"secondary_print_topic_codes":sec,"classification_status":status,"decision_basis":basis}
        if all(cur.get(k,"")==v for k,v in desired.items()): continue
        assert cur["classification_status"] == "manual_provisional"
        cur.update(desired); cur["review_note"] = f"Round130 full-text reread; body_chars={b['body_char_count']}; Fact-risk boundary: {risk}"; cur["reviewer"]=(cur.get("reviewer","main-thread")+"+round130-text-reread").strip("+"); cur["reviewed_at"]=date.today().isoformat(); updates.append(cur)
    write(REPORTS/"round130-decisions.tsv", ["id","title","old_primary","old_secondary","new_primary","new_secondary","status","decision","basis","risk_boundary"], decisions, "\t")
    write(REPORTS/"round130-text-audit.tsv", ["id","title","text_chars","current_primary","current_secondary","recommended_primary","recommended_secondary","recommended_status","decision_basis","fact_risk"], audits, "\t")
    if updates and not args.dry_run: write(DATA/"print-topic-manual-decisions-v2.csv", manual_fields, manual, ",")
    print(json.dumps({"round":130,"records":27,"body_chars":29932,"updated":len(updates),"confirmed":sum(x["status"]=="manual_confirmed" for x in decisions),"provisional":sum(x["status"]=="manual_provisional" for x in decisions),"dry_run":args.dry_run},ensure_ascii=False,indent=2))
if __name__ == "__main__": main()
