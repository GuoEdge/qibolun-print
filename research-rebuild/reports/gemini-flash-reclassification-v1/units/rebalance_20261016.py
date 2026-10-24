#!/usr/bin/env python3
"""薄册扩容 + 问题字段回填 + B31A 社會時局拆分。备份后改写三份编目与单元表，并重生 input/*.tsv。"""
import json, shutil, time
from collections import Counter
from pathlib import Path

D = Path(__file__).parent
BASE = D.parent
TS = time.strftime('%Y%m%d_%H%M%S')
CATS = ['workbook-40b-all-catalog.jsonl', 'workbook-40b-all-catalog-v4.jsonl', 'workbook-40b-all-catalog-v5.jsonl']
META = ['volume_code', 'booklet_code', 'booklet_name', 'volume_prefix', 'volume_full_title',
        'booklet_stem', 'booklet_stem_title', 'full_citation']

# 调册：ordinal -> (目标册, 目标单元)
MOVE = {}
for o in [161, 166, 177, 983, 1823, 2033, 2996, 3165, 3863, 3964]:
    MOVE[o] = ('B05', '原生之困')                     # B06 原生之困整单元并入
for o in [1039, 2452, 2852, 4408, 2006, 3516]:
    MOVE[o] = ('B05', '掙脫控制')
for o in [194, 296]:
    MOVE[o] = ('B05', '情緒牽絆')
for o in [3751, 1549, 2505, 2903, 2320, 4192, 1112, 2084]:
    MOVE[o] = ('B15', '交友之道')
for o in [2523, 1570, 3128, 2316]:
    MOVE[o] = ('B15', '衝突孤立')
for o in [2230, 1690, 1198, 1105, 3901]:
    MOVE[o] = ('B15', '獨處自持')

NEW_UNITS = {'B05': [('原生之困', '收原生家庭創傷、代際重複與如何走出父母陰影的問題。')]}
INTRO = {
    ('B05', '掙脫控制'): '收父母控制欲、經濟斷供與私人邊界之爭，談如何以獨立求得尊重。',
    ('B05', '情緒牽絆'): '收承接家人負能量、被迫站隊與家庭口角，談如何不被情緒裹挾。',
    ('B15', '交友之道'): '收結交朋友、維繫友誼、社交技巧與知己難覓的問題。',
    ('B15', '衝突孤立'): '收被貶低、被試探、難融入與遭排擠孤立時的應對。',
    ('B15', '獨處自持'): '收獨處孤獨、內向社恐、合群取捨與自尊自持的問題。',
}
B05_ORDER = ['原生之困', '掙脫控制', '情緒牽絆', '放下怨恨']
# B31A 社會時局 41 篇拆出列國一組
INTL = {387, 800, 1505, 1674, 1874, 1887, 1984, 2172, 2188, 2272, 2274, 2284, 2352}

# ---------- 编目 ----------
corpus = {}
for l in open(BASE / 'all-articles-merged-v3.jsonl', encoding='utf-8'):
    d = json.loads(l); corpus[d['id']] = d
main = [json.loads(l) for l in open(BASE / CATS[0], encoding='utf-8') if l.strip()]
tpl = {}
for code in {t for t, _ in MOVE.values()}:
    rows = [r for r in main if r['booklet_code'] == code]
    key = Counter(tuple(r[k] for k in META) for r in rows).most_common(1)[0][0]
    tpl[code] = dict(zip(META, key))

qfix = 0
for name in CATS:
    p = BASE / name
    rows = [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]
    shutil.copy2(p, str(p) + '.bak_rebal_' + TS)
    for r in rows:
        cq = (corpus.get(r['original_id'], {}).get('question') or '').strip()
        if cq and (r.get('question') or '').strip() != cq:
            r['question'] = cq
            if name == CATS[0]: qfix += 1
        if r['workbook_ordinal'] in MOVE:
            r.update(tpl[MOVE[r['workbook_ordinal']][0]])
    p.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows), encoding='utf-8')
print('问题字段回填', qfix, '篇；调册', len(MOVE), '篇')

# ---------- 单元表 ----------
U = {p.stem: json.loads(p.read_text(encoding='utf-8')) for p in (D / 'out').glob('*.json')}
touched = set()
for code, j in U.items():
    for u in j['units']:
        keep = [o for o in u['ordinals'] if o not in MOVE]
        if len(keep) != len(u['ordinals']):
            u['ordinals'] = keep; touched.add(code)
    j['units'] = [u for u in j['units'] if u['ordinals']]
for code, lst in NEW_UNITS.items():
    for n, intro in lst:
        U[code]['units'].append({'name': n, 'intro': intro, 'ordinals': []})
for o, (code, n) in MOVE.items():
    u = next(u for u in U[code]['units'] if u['name'] == n)
    u['ordinals'].append(o); touched.add(code)
for (code, n), intro in INTRO.items():
    next(u for u in U[code]['units'] if u['name'] == n)['intro'] = intro
U['B05']['units'].sort(key=lambda u: B05_ORDER.index(u['name']))
# B31A
units = U['B31A']['units']
i = next(k for k, u in enumerate(units) if u['name'] == '社會時局')
soc = units[i]
assert INTL <= set(soc['ordinals'])
soc['ordinals'] = [o for o in soc['ordinals'] if o not in INTL]
soc['name'], soc['intro'] = '民生世相', '收社會事件、民生經濟、輿論風氣與家國認同之剖析。'
units.insert(i + 1, {'name': '列邦角力', 'intro': '收美國社會、大國博弈、俄烏戰事與中東時局之評析。',
                     'ordinals': sorted(INTL)})
touched.add('B31A')
for code in touched:
    for u in U[code]['units']:
        u['ordinals'].sort()
    p = D / 'out' / f'{code}.json'
    shutil.copy2(p, str(p) + '.bak_rebal_' + TS)
    p.write_text(json.dumps(U[code], ensure_ascii=False, indent=1), encoding='utf-8')
print('改动单元表:', sorted(touched))

# ---------- 重生 input tsv ----------
main = [json.loads(l) for l in open(BASE / CATS[0], encoding='utf-8') if l.strip()]
clean = lambda s: (s or '').replace('\t', ' ').replace('\n', ' ').strip()
for code in sorted({r['booklet_code'] for r in main}):
    rows = sorted((r for r in main if r['booklet_code'] == code), key=lambda r: r['workbook_ordinal'])
    out = [f"# {code} {rows[0]['booklet_name']} 共{len(rows)}篇", '# ordinal\ttitle\tquestion\tpreview']
    out += [f"{r['workbook_ordinal']}\t{clean(r['title'])}\t{clean(r['question'])}\t{clean(r.get('text_preview'))[:60]}" for r in rows]
    (D / 'input' / f'{code}.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8')
print('input tsv 已重生')
