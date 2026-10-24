#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Apply the 2026-09-26 rebuild rounds to the live decision table.

Sources (all read-only here):
  * round165..round172 decision TSVs — the 92 `manual_provisional` records.
  * round181 sampling corrections  — four confirmed records whose stored
    primary topic the stratified audit found unsupported by the body.

Steps
-----
1. back up every file that is about to change, with its pre-change sha256;
2. rewrite the matching rows of `print-topic-manual-decisions-v2.csv`
   (status / primary / secondary / decision_basis / review_note / reviewer /
   reviewed_at);
3. print a before/after diff summary and the new hashes.

The corpus, the official edge tables and every earlier report are untouched.
Derived indexes are rebuilt afterwards by the project's own build scripts.
"""
from __future__ import annotations

import csv
import hashlib
import json
import shutil
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
R = ROOT / "research-rebuild"
OUT = R / "reports/rebuild-20260926"
MANUAL = R / "data/print-topic-manual-decisions-v2.csv"
BACKUP = OUT / "backup-before-apply-20260926"
TARGETS = [
    MANUAL,
    R / "reports/article-classification-v2.csv",
    R / "reports/print-index/print-research-index.csv",
    R / "reports/live-manual-classification-queue-v2.csv",
]

# round181 stratified-audit corrections: id -> (new_primary, review_note_suffix)
AUDIT_FIX = {
    "01cc5e71-1aae-5677-8463-41640aeaa77c": ("A08", "正文中心是股价与盈利脱钩、增长叙事可信度与中国资产的长期判断，无任何艺术/审美/文化生产内容；local A15 属明显误置。"),
    "a4b0e11a-9cf1-59bc-83b7-d671271eb36e": ("A09", "正文是防疫防线设计（枢纽落地检疫、行程码认证、常备防疫设施与专业应急部队），无媒体/传播/舆论内容；local A16 属明显误置。"),
    "31dcaf05-d756-5ab9-8ee7-9c6191c35104": ("A04", "正文讨论“厉害的人”为何办法多（失败未造成恐惧、避责天堂、无知作为庇护所），无性别/身体/同意内容；local A02 属明显误置。"),
    "26c7ad17-39ab-5728-afa9-a4181110a374": ("A02", "题面与正文均讨论“女性对政治兴趣低是否是生理天性”并以女皇/女帝与弱者政治学作答，无生态/动物/自然科学内容；local A18 属明显误置。"),
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def read_decisions(rounds) -> dict[str, dict]:
    out = {}
    for rnd in rounds:
        path = OUT / f"round{rnd}/round{rnd}-decisions.tsv"
        if not path.exists():
            continue
        for row in csv.DictReader(path.open(encoding="utf-8-sig"), delimiter="\t"):
            out[row["id"]] = {"round": rnd, **row}
    return out


def main() -> int:
    BACKUP.mkdir(parents=True, exist_ok=True)
    before = {}
    for p in TARGETS:
        if p.exists():
            before[str(p.relative_to(ROOT))] = sha256(p)
            shutil.copy2(p, BACKUP / p.name)
    (OUT / "apply-before-hashes.json").write_text(
        json.dumps({"files": before, "backup_dir": str(BACKUP.relative_to(ROOT))},
                   ensure_ascii=False, indent=2), encoding="utf-8")

    decisions = read_decisions([165, 166, 167, 168, 169, 170, 171, 172])
    rows = list(csv.DictReader(MANUAL.open(encoding="utf-8-sig")))
    fields = list(rows[0].keys())
    old = {r["id"]: dict(r) for r in rows}

    applied, changed_rows = 0, []
    for r in rows:
        aid = r["id"]
        new = None
        if aid in decisions:
            d = decisions[aid]
            new = {"primary_print_topic_code": d["primary"],
                   "secondary_print_topic_codes": d["secondary"],
                   "classification_status": d["status"],
                   "decision_basis": d["basis"],
                   "review_note": d["risk_note"],
                   "reviewer": f"main-thread+round{d['round']}-body-review",
                   "reviewed_at": "2026-09-26"}
        elif aid in AUDIT_FIX:
            newp, note = AUDIT_FIX[aid]
            sec = [c for c in (r["secondary_print_topic_codes"] or "").split(";") if c and c != newp]
            new = {"primary_print_topic_code": newp,
                   "secondary_print_topic_codes": ";".join(sec),
                   "classification_status": "manual_confirmed",
                   "decision_basis": note,
                   "review_note": (r["review_note"] + " " if r["review_note"] else "")
                                  + "[round181 分层抽样修正；本轮对该篇的阅读覆盖为 head1000+tail500，"
                                    "中心判断依据正文可见的连续论述与题面对象，未通读全部中段。]",
                   "reviewer": "main-thread+round181-official-unmatched-sample",
                   "reviewed_at": "2026-09-26"}
        if not new:
            continue
        delta = {k: v for k, v in new.items() if (r.get(k) or "") != (v or "")}
        if not delta:
            continue
        changed_rows.append({"id": aid, "title": r["title"],
                             "old_primary": r["primary_print_topic_code"],
                             "new_primary": new["primary_print_topic_code"],
                             "old_secondary": r["secondary_print_topic_codes"],
                             "new_secondary": new["secondary_print_topic_codes"],
                             "old_status": r["classification_status"],
                             "new_status": new["classification_status"]})
        r.update(new)
        applied += 1

    tmp = MANUAL.with_suffix(".csv.tmp")
    with tmp.open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader(); w.writerows(rows)
    tmp.replace(MANUAL)

    after_status = Counter(r["classification_status"] for r in rows)
    summary = {
        "rows": len(rows),
        "rows_updated": applied,
        "status_after": dict(after_status),
        "status_before": dict(Counter(r["classification_status"] for r in old.values())),
        "primary_changed": sum(1 for c in changed_rows if c["old_primary"] != c["new_primary"]),
        "secondary_changed": sum(1 for c in changed_rows if c["old_secondary"] != c["new_secondary"]),
        "manual_sha256_before": before.get(str(MANUAL.relative_to(ROOT))),
        "manual_sha256_after": sha256(MANUAL),
        "changed_rows": changed_rows,
    }
    (OUT / "apply-result.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k: v for k, v in summary.items() if k != "changed_rows"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
