#!/usr/bin/env python3
"""第二轮：B06「獨立觀世」离题篇目归位到合适分册；B38K 小单元合并。备份 .bak_rebal2_*。"""
import json, shutil, time
from collections import Counter
from pathlib import Path

D = Path(__file__).parent
BASE = D.parent
TS = time.strftime('%Y%m%d_%H%M%S')
CATS = ['workbook-40b-all-catalog.jsonl', 'workbook-40b-all-catalog-v4.jsonl', 'workbook-40b-all-catalog-v5.jsonl']
META = ['volume_code', 'booklet_code', 'booklet_name', 'volume_prefix', 'volume_full_title',
        'booklet_stem', 'booklet_stem_title', 'full_citation']

MOVE = {  # ordinal -> (目标册, 目标单元)
    977: ('B40', '攻守兵略'), 3575: ('B40', '攻守兵略'), 4058: ('B40', '古代民生'),
    1157: ('B40', '王朝興替'), 3427: ('B40', '文明記憶'), 3168: ('B40', '文明記憶'), 2825: ('B40', '文明記憶'),
    2760: ('B40', '大國之道'), 3853: ('B40', '大國之道'),
    2597: ('B40', '當代戰和'), 1634: ('B40', '當代戰和'), 2485: ('B40', '當代戰和'), 3420: ('B40', '當代戰和'),
    2415: ('B39', '書畫賞析'), 1668: ('B39', '文學影視'), 3015: ('B39', '生活況味'),
    1856: ('B39', '生活況味'), 1910: ('B39', '設計營造'),
    870: ('B29', '器物工程'), 883: ('B29', '器物工程'), 2115: ('B29', '器物工程'),
    2189: ('B37', '宗教社會'), 1328: ('B25', '立場極化'), 2519: ('B28', '消費市場'),
}
RENAME = {  # (册, 旧名) -> (新名, 新导语)
    ('B06', '獨立觀世'): ('獨立思考', '收何為獨立思考、如何擺脫他人思路與自成判斷之問。'),
    ('B39', '生活況味'): ('生活況味', '收飲食、閒趣、野釣、貓趣與做事態度等日常美學之問。'),
    ('B40', '古代民生'): ('古代民生', '收古代識字、秋決、牢飯、鏢行與封號等社會運轉之問。'),
    ('B40', '文明記憶'): ('文明記憶', '收修史、上古社會、神話傳說、民族與宗教文化等文明之問。'),
}
MERGE = ('B38K', ['文史雜談', '兵器武備'], '文史兵備', '收詩人神話、寓言小說與刀弓甲炮、長城兵員等文史武備之談。')

main = [json.loads(l) for l in open(BASE / CATS[0], encoding='utf-8') if l.strip()]
tpl = {}
for code in {t for t, _ in MOVE.values()}:
    rows = [r for r in main if r['booklet_code'] == code]
    tpl[code] = dict(zip(META, Counter(tuple(r[k] for k in META) for r in rows).most_common(1)[0][0]))
for name in CATS:
    p = BASE / name
    rows = [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]
    shutil.copy2(p, str(p) + '.bak_rebal2_' + TS)
    for r in rows:
        if r['workbook_ordinal'] in MOVE:
            r.update(tpl[MOVE[r['workbook_ordinal']][0]])
    p.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows), encoding='utf-8')

U = {p.stem: json.loads(p.read_text(encoding='utf-8')) for p in (D / 'out').glob('*.json')}
touched = set(t for t, _ in MOVE.values()) | {'B06', MERGE[0]}
for code, j in U.items():
    for u in j['units']:
        u['ordinals'] = [o for o in u['ordinals'] if o not in MOVE]
for o, (code, n) in MOVE.items():
    next(u for u in U[code]['units'] if u['name'] == n)['ordinals'].append(o)
for (code, old), (new, intro) in RENAME.items():
    u = next(u for u in U[code]['units'] if u['name'] == old)
    u['name'], u['intro'] = new, intro
code, olds, new, intro = MERGE
us = U[code]['units']
i = next(k for k, u in enumerate(us) if u['name'] == olds[0])
merged = {'name': new, 'intro': intro, 'ordinals': [o for u in us if u['name'] in olds for o in u['ordinals']]}
U[code]['units'] = us[:i] + [merged] + [u for u in us[i:] if u['name'] not in olds]
for code in touched:
    for u in U[code]['units']:
        u['ordinals'].sort()
    p = D / 'out' / f'{code}.json'
    shutil.copy2(p, str(p) + '.bak_rebal2_' + TS)
    p.write_text(json.dumps(U[code], ensure_ascii=False, indent=1), encoding='utf-8')

main = [json.loads(l) for l in open(BASE / CATS[0], encoding='utf-8') if l.strip()]
clean = lambda s: (s or '').replace('\t', ' ').replace('\n', ' ').strip()
for code in sorted(touched):
    rows = sorted((r for r in main if r['booklet_code'] == code), key=lambda r: r['workbook_ordinal'])
    out = [f"# {code} {rows[0]['booklet_name']} 共{len(rows)}篇", '# ordinal\ttitle\tquestion\tpreview']
    out += [f"{r['workbook_ordinal']}\t{clean(r['title'])}\t{clean(r['question'])}\t{clean(r.get('text_preview'))[:60]}" for r in rows]
    (D / 'input' / f'{code}.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8')
print('调册', len(MOVE), '篇；改动', sorted(touched))
