#!/usr/bin/env python3
"""把单元扉叶 + 新目录接入 build_volume_v1.js / build_volume_v2.js"""
from pathlib import Path
import shutil, time

D = Path(__file__).parent.parent
ts = time.strftime("%Y%m%d_%H%M%S")

COMMON = [
    ("const body = [], report = [], startLeaf = new Map();\nfor (const art of arts) {\n  const items = [];",
     "const body = [], report = [], startLeaf = new Map();\nlet unitLeaves = 0;\nfor (const g of groups) {\nif (g.name) { body.push(L.buildUnitPage(g, unitCount, ctx, body.length === 0)); unitLeaves++; }\nconst uctx = { ...ctx, unitName: g.name };\nfor (const art of g.arts) {\n  const items = [];"),
    ("startOfSection: body.length === 0 }, ctx);\n    if (i === 0) startLeaf.set(art.title, report.length + 1);",
     "startOfSection: body.length === 0 }, uctx);\n    if (i === 0) startLeaf.set(art.workbook_ordinal, report.length + unitLeaves + 1);"),
    ("超限: M.HEADER_PT + M.FRAME_MIN_PT > M.PAGE_CONTENT_PT });\n  });\n}\n",
     "超限: M.HEADER_PT + M.FRAME_MIN_PT > M.PAGE_CONTENT_PT });\n  });\n}\n}\nconst bodyLeaves = report.length + unitLeaves;\n"),
    ("const tocFrames = L.buildToc(arts.map(a => ({ title: a.title, startLeafLabel: chineseLeaf(startLeaf.get(a.title)) })));",
     "const tocFrames = L.buildToc(groups, a => chineseLeaf(startLeaf.get(a.workbook_ordinal)));"),
    ("const needsBackBlank = (frontPages + 1 + report.length) % 2 === 1;",
     "const needsBackBlank = (frontPages + 1 + bodyLeaves) % 2 === 1;"),
    ("'，正文 ' + report.length + ' 叶，封底补白 ' + (needsBackBlank ? 1 : 0) + '，预计物理总页 ' + (frontPages + report.length +",
     "'，单元 ' + unitCount + '，正文 ' + bodyLeaves + ' 叶（含单元扉叶 ' + unitLeaves + '），封底补白 ' + (needsBackBlank ? 1 : 0) + '，预计物理总页 ' + (frontPages + bodyLeaves +"),
]

V2_ARTS = ("return { ...c, answer: content.answer || '', narrative: content.narrative || '' }; });\n",
           "return { ...c, answer: content.answer || '', narrative: content.narrative || '' }; });\nconst groups = L.loadUnits(part.code, arts);\nconst unitCount = groups.length;\n")

# V1：B02 不再按序三等分，而是先全册分单元，再在单元边界上三分
V1_SLICE = ("if (part.code === 'B02') {\n  const n = records.length, size = Math.ceil(n / 3), index = { B02A: 0, B02B: 1, B02C: 2 }[key];\n  records = records.slice(index * size, Math.min(n, (index + 1) * size));\n}\n",
            "let groupsAll = L.loadUnits(part.code, records);\nconst unitCount = groupsAll.length;\nif (part.code === 'B02') {\n  groupsAll = L.splitGroups(groupsAll, 3, { B02A: 0, B02B: 1, B02C: 2 }[key]);\n  records = groupsAll.flatMap(g => g.arts);\n}\n")
V1_ARTS = (V2_ARTS[0],
           V2_ARTS[0] + "const artByOrd = new Map(arts.map(a => [a.workbook_ordinal, a]));\nconst groups = groupsAll.map(g => ({ ...g, arts: g.arts.map(r => artByOrd.get(r.workbook_ordinal)) }));\n")

for name, extra in (("build_volume_v1.js", [V1_SLICE, V1_ARTS]), ("build_volume_v2.js", [V2_ARTS])):
    p = D / name
    s = p.read_text(encoding="utf-8")
    shutil.copy2(p, str(p) + ".bak_units_" + ts)
    for old, new in extra + COMMON:
        assert s.count(old) == 1, (name, old[:60], s.count(old))
        s = s.replace(old, new)
    p.write_text(s, encoding="utf-8")
    print("patched", name)
