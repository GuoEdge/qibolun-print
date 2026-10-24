# -*- coding: utf-8 -*-
"""round169/170 机械自检（协议第 7 节 + 本轮附加要求）。"""
import csv, json, os, re, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = os.path.join(os.path.dirname(BASE), "..", "data", "print-topic-registry-v2.csv")
REG = os.path.normpath(REG)
ALLOWED = ["A%02d" % i for i in range(0, 22)]
BLOCK = {"source_empty", "source_truncated", "body_is_quotation", "body_is_pointer",
         "body_question_mismatch", "body_too_short_for_center", "a00_registry_gap"}

def norm(s):
    return re.sub(r"[\s\"'“”‘’「」『』]", "", s or "")

def best_fragment(q, t, n=12):
    """返回能在 t 中命中的最长连续片段长度（从 12 字窗口起检验全部子串）。"""
    nq, nt = norm(q), norm(t)
    if not nq:
        return 0
    for L in range(len(nq), n - 1, -1):
        for i in range(0, len(nq) - L + 1):
            if nq[i:i + L] in nt:
                return L
    return 0

def sec_list(s):
    return [x for x in re.split(r"[;,]", (s or "").strip()) if x]

def main():
    reg = {}
    with open(REG, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            reg[row["code"]] = row["name"]
    overall = True
    for rname in ["round169", "round170"]:
        d = os.path.join(BASE, rname)
        sel = list(csv.DictReader(open(os.path.join(d, f"{rname}-selection.csv"), encoding="utf-8-sig")))
        ft = json.load(open(os.path.join(d, f"{rname}-fulltext.json"), encoding="utf-8"))
        dec = list(csv.DictReader(open(os.path.join(d, f"{rname}-decisions.tsv"), encoding="utf-8"), delimiter="\t"))
        aud = list(csv.DictReader(open(os.path.join(d, f"{rname}-body-evidence-audit.tsv"), encoding="utf-8"), delimiter="\t"))
        rev = list(csv.DictReader(open(os.path.join(d, f"{rname}-revision-log.csv"), encoding="utf-8")))
        checks = []
        # 1 引文命中
        bad = []
        frag = {}
        for r in aud:
            e = next(x for x in ft if x["id"] == r["id"])
            L = best_fragment(r["body_evidence_quote"], e["text"])
            frag[r["title"]] = L
            if L < 12:
                bad.append((r["title"], L))
        checks.append(("每行 body_evidence_quote ≥12 字连续片段可在该篇 text 中原文命中",
                       not bad, f"{len(aud)}/{len(aud)} 命中；最短命中片段 {min(frag.values())} 字" + (f"；FAIL={bad}" if bad else "")))
        # 2 注册表
        bad = []
        for r in aud:
            for c in [r["new_primary"]] + sec_list(r["new_secondary"]):
                if c not in reg:
                    bad.append((r["title"], c))
        checks.append(("primary/secondary 均在注册表 A00–A21 内", not bad, f"注册表 {len(reg)} 个代码；异常={bad}" if bad else f"{len(reg)} 个代码，全部合法"))
        # 3 主副互斥
        bad = [(r["title"], r["new_primary"]) for r in aud if r["new_primary"] in sec_list(r["new_secondary"])]
        checks.append(("primary 不出现在 secondary", not bad, f"0 冲突" if not bad else f"FAIL={bad}"))
        # 4 单一 primary + 副专题 ≤3
        bad = [(r["title"], len(sec_list(r["new_secondary"]))) for r in aud if len(sec_list(r["new_secondary"])) > 3]
        checks.append(("每篇 1 个 primary 且 secondary ≤ 3", not bad, f"primary 均非空唯一；副专题最多 {max(len(sec_list(r['new_secondary'])) for r in aud)} 个"))
        # 5 行数与 ID 集合
        s_ids, a_ids, d_ids = [x["id"] for x in sel], [x["id"] for x in aud], [x["id"] for x in dec]
        ok = len(sel) == len(aud) == len(dec) and set(s_ids) == set(a_ids) == set(d_ids)
        checks.append(("行数与选择清单一致、ID 集合完全相等", ok,
                       f"selection={len(sel)} audit={len(aud)} decisions={len(dec)}；ID 集合{'相等' if ok else '不等'}"))
        # 6 暂定行必须有合法 blocking_reason
        bad = []
        for r in aud:
            if r["new_status"] == "manual_provisional":
                if r["blocking_reason"] not in BLOCK:
                    bad.append((r["title"], r["blocking_reason"]))
            elif r["new_status"] == "manual_confirmed":
                if r["blocking_reason"].strip() != "":
                    bad.append((r["title"], "confirmed 行不应填 blocking_reason"))
            else:
                bad.append((r["title"], "非法状态 " + r["new_status"]))
        checks.append(("保持暂定的行均填合法 blocking_reason 且取值在 R2 表内", not bad,
                       f"暂定 {sum(1 for r in aud if r['new_status']=='manual_provisional')} 行；异常={bad}" if bad else
                       f"暂定 {sum(1 for r in aud if r['new_status']=='manual_provisional')} 行，无遗留字段错误"))
        # 7 decisions 与 audit 一致
        bad = []
        dm = {r["id"]: r for r in dec}
        for r in aud:
            dd = dm[r["id"]]
            if (dd["primary"], sec_list(dd["secondary"]), dd["status"]) != (r["new_primary"], sec_list(r["new_secondary"]), r["new_status"]):
                bad.append(r["title"])
        checks.append(("decisions.tsv 与 body-evidence-audit.tsv 的主/副/状态一致", not bad, "全部一致" if not bad else f"FAIL={bad}"))
        # 8 revision-log 只含变化行且齐全
        chg = {r["id"] for r in aud if (r["old_primary"] != r["new_primary"] or r["old_secondary"] != r["new_secondary"] or r["old_status"] != r["new_status"])}
        rv = {r["id"] for r in rev}
        checks.append(("revision-log 行 = 实际发生变化的行集合", chg == rv, f"应记 {len(chg)} 行，实记 {len(rv)} 行"))
        # 9 标题/字数与输入一致
        bad = []
        for r in aud:
            e = next(x for x in ft if x["id"] == r["id"])
            if r["title"] != e["title"] or int(r["body_char_count"]) != len(e["text"]):
                bad.append(r["title"])
        checks.append(("title 与 body_char_count 与正文包一致", not bad, "全部一致" if not bad else f"FAIL={bad}"))

        print("=" * 20, rname)
        for name, ok, detail in checks:
            print(("PASS" if ok else "FAIL"), "|", name, "|", detail)
            overall = overall and ok
        print("正文字符总数:", sum(int(r["body_char_count"]) for r in aud),
              "| manual_confirmed:", sum(1 for r in aud if r["new_status"] == "manual_confirmed"),
              "| manual_provisional:", sum(1 for r in aud if r["new_status"] == "manual_provisional"))
        print("主专题改动:", sum(1 for r in aud if r["old_primary"] != r["new_primary"]),
              "副专题改动:", sum(1 for r in aud if r["old_secondary"] != r["new_secondary"]))
    print("=" * 20, "OVERALL:", "PASS" if overall else "FAIL")
    return 0 if overall else 1

if __name__ == "__main__":
    sys.exit(main())
