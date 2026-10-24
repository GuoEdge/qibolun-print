#!/usr/bin/env python3
"""删除重复收录的 971《混沌》（与 970《混沌文笔》为同一知乎回答的两个版本）。"""
import json, os, shutil, time

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DROP = 971
TS = time.strftime('%Y%m%d_%H%M%S')

for name in ['workbook-40b-all-catalog.jsonl', 'workbook-40b-all-catalog-v4.jsonl',
             'workbook-40b-all-catalog-v5.jsonl']:
    p = os.path.join(BASE, name)
    lines = open(p, encoding='utf-8').read().splitlines()
    keep = [l for l in lines if l.strip() and json.loads(l)['workbook_ordinal'] != DROP]
    if len(keep) == len([l for l in lines if l.strip()]):
        print(name, '未找到', DROP); continue
    shutil.copy2(p, p + '.bak_dedup_' + TS)
    open(p, 'w', encoding='utf-8').write('\n'.join(keep) + '\n')
    print(name, len(lines), '->', len(keep))

p = os.path.join(BASE, 'units', 'out', 'B39.json')
d = json.load(open(p, encoding='utf-8'))
shutil.copy2(p, p + '.bak_dedup_' + TS)
for u in d['units']:
    if DROP in u['ordinals']:
        u['ordinals'].remove(DROP)
        print('B39 单元', u['name'], '剩', len(u['ordinals']))
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
