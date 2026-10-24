#!/usr/bin/env python3
"""校验 units/out/{CODE}.json：每篇恰好出现一次、单元数与命名合规。用法：validate_units.py [CODE ...]"""
import json, sys, re
from pathlib import Path

D = Path(__file__).parent
codes = sys.argv[1:] or sorted(p.stem for p in (D / "input").glob("*.tsv"))
bad = 0
for code in codes:
    inp = [l.split("\t")[0] for l in (D / "input" / f"{code}.tsv").read_text(encoding="utf-8").splitlines() if l and not l.startswith("#")]
    want = set(int(x) for x in inp)
    p = D / "out" / f"{code}.json"
    if not p.exists():
        print(f"[缺失] {code}"); bad += 1; continue
    try:
        j = json.loads(p.read_text(encoding="utf-8"))
        units = j["units"]
        got = [o for u in units for o in u["ordinals"]]
        errs = []
        if j.get("code") != code: errs.append("code 不符")
        if len(got) != len(set(got)): errs.append("有重复篇")
        if set(got) != want: errs.append(f"缺 {sorted(want - set(got))[:8]} 多 {sorted(set(got) - want)[:8]}")
        n = len(want)
        lo, hi = (2, 3) if n < 30 else (3, 6) if n < 120 else (5, 12)
        if not lo <= len(units) <= hi: errs.append(f"单元数 {len(units)} 不在 {lo}-{hi}")
        names = [u["name"] for u in units]
        if len(set(names)) != len(names): errs.append("单元名重复")
        for u in units:
            if not re.fullmatch(r"[\u4e00-\u9fff]{4}", u["name"]): errs.append(f"单元名非四字：{u['name']}")
            if not (36 <= len(u.get("intro", "")) <= 72): errs.append(f"导语长度不合：{u['name']}")
            if "收" in u.get("intro", "") or "本單元" in u.get("intro", ""): errs.append(f"导语含“收/本單元”：{u['name']}")
            if len(u["ordinals"]) < 3: errs.append(f"单元过小：{u['name']}")
        if errs:
            bad += 1; print(f"[失败] {code}: " + "；".join(errs))
        else:
            print(f"[通过] {code} {n}篇 → " + " / ".join(f"{u['name']}{len(u['ordinals'])}" for u in units))
    except Exception as e:
        bad += 1; print(f"[解析错] {code}: {e}")
from collections import defaultdict
seen = defaultdict(list)
for p in sorted((D / "out").glob("*.json")):
    for u in json.loads(p.read_text(encoding="utf-8"))["units"]:
        seen[u["name"]].append(p.stem)
dup = {k: v for k, v in seen.items() if len(v) > 1}
if dup:
    bad += 1; print("[失败] 跨册单元重名：" + "；".join(f"{k}{v}" for k, v in dup.items()))
else:
    print(f"[通过] 全书 {sum(len(v) for v in seen.values())} 个单元名互不重复")
print("全部通过" if not bad else f"{bad} 项未通过")
sys.exit(bool(bad))
