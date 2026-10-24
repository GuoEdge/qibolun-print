# -*- coding: utf-8 -*-
"""round168 机械自检（协议第 7 节）。用法: python3 check_round168.py"""
import csv, json, re, sys
BASE = "/mnt/d/岐伯论/research-rebuild/reports/rebuild-20260926/round168"
REG  = "/mnt/d/岐伯论/research-rebuild/data/print-topic-registry-v2.csv"
ALLOWED = {"A%02d" % i for i in range(0, 22)}
BLOCK = {"source_empty","source_truncated","body_is_quotation","body_is_pointer",
         "body_question_mismatch","body_too_short_for_center","a00_registry_gap"}
def clean(s): return (s or "").replace("\u23ce", "\n")   # ⏎ 还原为换行
def norm(s):  return re.sub(r"[\s\"'\u201c\u201d\u2018\u2019\u300c\u300d\u300e\u300f]", "", s or "")
def best_fragment(q, t, n=12):
    nq, nt = norm(q), norm(t)
    if len(nq) < n: return 0
    for L in range(len(nq), n - 1, -1):
        for i in range(len(nq) - L + 1):
            if nq[i:i + L] in nt: return L
    return 0
def sec_list(s): return [x for x in re.split(r"[;,]", (s or "").strip()) if x]

reg = {r["code"] for r in csv.DictReader(open(REG, encoding="utf-8-sig"))}
sel = list(csv.DictReader(open(BASE + "/round168-selection.csv", encoding="utf-8-sig")))
ft  = json.load(open(BASE + "/round168-fulltext.json", encoding="utf-8"))
fmap = {p["id"]: p for p in ft}
dec = list(csv.DictReader(open(BASE + "/round168-decisions.tsv", encoding="utf-8"), delimiter="\t"))
aud = list(csv.DictReader(open(BASE + "/round168-body-evidence-audit.tsv", encoding="utf-8"), delimiter="\t"))
rev = list(csv.DictReader(open(BASE + "/round168-revision-log.csv", encoding="utf-8")))

checks = []
bad = []; frag = {}
for r in aud:
    L = best_fragment(clean(r["body_evidence_quote"]), fmap[r["id"]]["text"])
    frag[r["title"]] = L
    if L < 12: bad.append((r["title"], L))
whole = sum(1 for r in aud if clean(r["body_evidence_quote"]) in fmap[r["id"]]["text"])
checks.append(("body_evidence_quote ≥12 字连续片段原文命中", not bad,
  "%d/%d 命中；最短 %d 字；整串包含 %d/%d" % (len(aud)-len(bad), len(aud), min(frag.values()), whole, len(aud))
  + ("；FAIL=%s" % bad if bad else "")))
bad = [(r["title"], c) for r in aud for c in [r["new_primary"]] + sec_list(r["new_secondary"])
       if c not in ALLOWED or c not in reg]
checks.append(("primary/secondary 均在 A00–A21 内", not bad, "注册表 %d 码，全部合法" % len(reg) if not bad else "FAIL=%s" % bad))
bad = [(r["title"], r["new_primary"]) for r in aud if r["new_primary"] in sec_list(r["new_secondary"])]
checks.append(("primary 不出现在 secondary", not bad, "0 冲突" if not bad else "FAIL=%s" % bad))
bad = [r["title"] for r in aud if len(sec_list(r["new_secondary"])) > 3 or not r["new_primary"].strip()]
checks.append(("每篇 1 个 primary 且 secondary ≤ 3", not bad,
  "副专题最多 %d 个" % max(len(sec_list(r["new_secondary"])) for r in aud)))
s_ids, a_ids, d_ids = [x["id"] for x in sel], [x["id"] for x in aud], [x["id"] for x in dec]
ok = len(sel) == len(aud) == len(dec) and set(s_ids) == set(a_ids) == set(d_ids)
checks.append(("行数与选择清单一致、ID 集合相等", ok,
  "selection=%d audit=%d decisions=%d；ID 集合%s" % (len(sel), len(aud), len(dec), "相等" if ok else "不等")))
bad = []
for r in aud:
    if r["new_status"] == "manual_provisional":
        if r["blocking_reason"] not in BLOCK: bad.append((r["title"], r["blocking_reason"]))
    elif r["new_status"] == "manual_confirmed":
        if r["blocking_reason"].strip(): bad.append((r["title"], "confirmed 行 blocking_reason 非空"))
    else: bad.append((r["title"], "非法状态 " + r["new_status"]))
checks.append(("暂定行均填合法 blocking_reason", not bad,
  "暂定 %d 行，无字段错误" % sum(1 for r in aud if r["new_status"] == "manual_provisional") if not bad else "FAIL=%s" % bad))
dm = {r["id"]: r for r in dec}
bad = [r["title"] for r in aud if (dm[r["id"]]["primary"], sec_list(dm[r["id"]]["secondary"]), dm[r["id"]]["status"])
       != (r["new_primary"], sec_list(r["new_secondary"]), r["new_status"])]
checks.append(("decisions 与审计表主/副/状态一致", not bad, "全部一致" if not bad else "FAIL=%s" % bad))
chg = {r["id"] for r in aud if (r["old_primary"], r["old_secondary"], r["old_status"])
       != (r["new_primary"], r["new_secondary"], r["new_status"])}
checks.append(("revision-log 行 = 变化行集合", chg == {r["id"] for r in rev},
  "应记 %d 行，实记 %d 行" % (len(chg), len(rev))))
bad = [r["title"] for r in aud if r["title"] != fmap[r["id"]]["title"]
       or int(r["body_char_count"]) != len(fmap[r["id"]]["text"])]
checks.append(("title/body_char_count 与正文包一致", not bad, "全部一致" if not bad else "FAIL=%s" % bad))
checks.append(("reviewer/reviewed_at 统一",
  all(r["reviewer"] == "subagent+round168-body-review" and r["reviewed_at"] == "2026-09-26" for r in aud),
  "%d/%d 行" % (len(aud), len(aud))))
checks.append(("引文非疑问句", all(not clean(r["body_evidence_quote"]).strip().endswith(("\uff1f", "?")) for r in aud), "12/12"))

overall = True
for name, ok, detail in checks:
    print(("PASS" if ok else "FAIL"), "|", name, "|", detail); overall = overall and ok
print("---")
print("正文字符总数:", sum(int(r["body_char_count"]) for r in aud),
      "| manual_confirmed:", sum(1 for r in aud if r["new_status"] == "manual_confirmed"),
      "| manual_provisional:", sum(1 for r in aud if r["new_status"] == "manual_provisional"))
print("主专题改动:", sum(1 for r in aud if r["old_primary"] != r["new_primary"]),
      "| 副专题改动:", sum(1 for r in aud if r["old_secondary"] != r["new_secondary"]))
print("OVERALL:", "PASS" if overall else "FAIL")
sys.exit(0 if overall else 1)
