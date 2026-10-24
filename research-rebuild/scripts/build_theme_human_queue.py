#!/usr/bin/env python3
"""Export a traceable review queue for provisional v2 theme assignments."""
from __future__ import annotations
import csv, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
V2 = ROOT / "sooon-q9adg-articles-v2.jsonl"
MAP = ROOT / "research-rebuild/reports/article-theme-map-v2.csv"
DS = ROOT / "research-rebuild/out"
OUT = ROOT / "research-rebuild/reports/theme-human-review-queue.csv"

def jsonl(path):
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            if line.strip(): yield json.loads(line)

def evidence(rec):
    a = rec.get("analysis") or {}
    p = rec.get("provisional_tags") or a.get("provisional_tags") or {}
    bits = []
    for key in ("summary", "meaning", "evidence", "question_context", "working_keywords", "domain_candidates", "issue_candidates", "unresolved_questions"):
        value = a.get(key, p.get(key, ""))
        if isinstance(value, (list, dict)): value = json.dumps(value, ensure_ascii=False)
        if value: bits.append(f"{key}: {value}")
    return " | ".join(bits)

def main():
    articles = {r["id"]: r for r in jsonl(V2)}
    ds = {}
    for path in sorted(DS.glob("*.out.jsonl")):
        for r in jsonl(path): ds[r.get("article_id")] = r
    with MAP.open(encoding="utf-8-sig", newline="") as fh: rows = list(csv.DictReader(fh))
    rows = [r for r in rows if r.get("audit_status") in {"needs_human_classification", "manual_provisional", "missing_first_pass"}]
    fields = ["id", "ordinal", "title", "question", "candidate_concepts", "primary_candidate", "top_score", "tie_count", "matched_cues", "audit_status", "deepseek_available", "first_pass_evidence", "manual_primary", "retained_concepts", "exclusion_reason", "reviewer", "review_status"]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields); writer.writeheader()
        for row in rows:
            article = articles.get(row["id"], {}); rec = ds.get(row["id"], {})
            writer.writerow({"id": row["id"], "ordinal": row["ordinal"], "title": article.get("title", row.get("title", "")), "question": article.get("question", ""), "candidate_concepts": row.get("concepts", ""), "primary_candidate": row.get("primary", ""), "top_score": row.get("top_score", ""), "tie_count": row.get("tie_count", ""), "matched_cues": row.get("matched_cues", ""), "audit_status": row.get("audit_status", ""), "deepseek_available": bool(rec), "first_pass_evidence": evidence(rec), "manual_primary": "", "retained_concepts": "", "exclusion_reason": "", "reviewer": "", "review_status": "pending"})
    print(f"wrote {len(rows)} review records to {OUT}")

if __name__ == "__main__": main()
