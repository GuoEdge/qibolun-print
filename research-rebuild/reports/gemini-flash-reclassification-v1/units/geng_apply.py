#!/usr/bin/env python3
"""庚册乙方案落地：改三份编目、重写 B38A–J 与新建 B36A/B 单元表、归档 B38K/L、重生 input tsv、改 spine_manifest。"""
import json, shutil, time, os
from pathlib import Path

D = Path(__file__).parent
BASE = D.parent
ROOT = Path('/storage/Users/currentUser/Documents/岐伯论')
TS = time.strftime('%Y%m%d_%H%M%S')
CATS = ['workbook-40b-all-catalog.jsonl', 'workbook-40b-all-catalog-v4.jsonl', 'workbook-40b-all-catalog-v5.jsonl']
BR = {'子': 'B38A', '丑': 'B38B', '寅': 'B38C', '卯': 'B38D', '辰': 'B38E', '巳': 'B38F',
      '午': 'B38G', '未': 'B38H', '申': 'B38I', '酉': 'B38J'}
NAMES = {  # code -> (繁体题名, 简体题名, 分册后缀)
    'B38A': ('心性自持與精神獨立', '心性自持与精神独立', '子'), 'B38B': ('心性自持與精神獨立', '心性自持与精神独立', '丑'),
    'B38C': ('處世分寸與人我進退', '处世分寸与人我进退', '寅'), 'B38D': ('處世分寸與人我進退', '处世分寸与人我进退', '卯'),
    'B38E': ('情愛家室與親子人倫', '情爱家室与亲子人伦', '辰'), 'B38F': ('情愛家室與親子人倫', '情爱家室与亲子人伦', '巳'),
    'B38G': ('格物致知與技藝雜學', '格物致知与技艺杂学', '午'), 'B38H': ('格物致知與技藝雜學', '格物致知与技艺杂学', '未'),
    'B38I': ('世情人性與義理雜談', '世情人性与义理杂谈', '申'), 'B38J': ('世情人性與義理雜談', '世情人性与义理杂谈', '酉'),
    'B36A': ('時局經緯與家國論衡', '时局经纬与家国论衡', '上'), 'B36B': ('時局經緯與家國論衡', '时局经纬与家国论衡', '下'),
}

def meta(code):
    trad, simp, suf = NAMES[code]
    if code.startswith('B36'):
        return dict(volume_code='V6', booklet_code=code, booklet_name=f'{simp}·{suf}册', volume_prefix='观风察变',
                    volume_full_title='观风察变——时代透视与群体思潮', booklet_stem=f'壬·{suf}',
                    booklet_stem_title=f'壬·{suf}册 {simp}·{suf}册', full_citation=f'觀風察變 · 壬·{suf}册 {simp}·{suf}册')
    return dict(volume_code='V7', booklet_code=code, booklet_name=f'{simp}·{suf}册', volume_prefix='涤除玄览',
                volume_full_title='涤除玄览——深层哲思与名相辨析', booklet_stem=f'庚·{suf}',
                booklet_stem_title=f'庚冊 {simp}·{suf}册', full_citation=f'涤除玄览 · 庚冊 {simp}·{suf}册')

# ---------- 新单元表 ----------
NEW = {}
for f in sorted((D / 'geng_units_out').glob('*.json')):
    for b in json.loads(f.read_text(encoding='utf-8'))['books']:
        NEW[b['code']] = {'code': b['code'], 'units': [{'name': u['name'], 'intro': u['intro'], 'ordinals': sorted(u['ordinals'])} for u in b['units']]}
assert set(NEW) == set(NAMES), set(NEW) ^ set(NAMES)
o2c = {o: c for c, j in NEW.items() for u in j['units'] for o in u['ordinals']}
assert len(o2c) == 1207

# ---------- 编目 ----------
for name in CATS:
    p = BASE / name
    rows = [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]
    shutil.copy2(p, str(p) + '.bak_geng_' + TS)
    n = 0
    for r in rows:
        if r['booklet_code'].startswith('B38'):
            r.update(meta(o2c[r['workbook_ordinal']])); n += 1
    assert n == 1207, (name, n)
    p.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows), encoding='utf-8')
print('编目改写 3 份，各 1207 篇')

# ---------- 单元表 ----------
for code in ['B38' + c for c in 'ABCDEFGHIJKL']:
    p = D / 'out' / f'{code}.json'
    if p.exists(): shutil.copy2(p, str(p) + '.bak_geng_' + TS)
for code in ('B38K', 'B38L'):
    for sub in ('out', 'input'):
        ext = 'json' if sub == 'out' else 'tsv'
        p = D / sub / f'{code}.{ext}'
        if p.exists(): os.replace(p, str(p) + '.retired_geng_' + TS)
for code, j in NEW.items():
    (D / 'out' / f'{code}.json').write_text(json.dumps(j, ensure_ascii=False, indent=1), encoding='utf-8')
print('单元表写入', sorted(NEW))

# ---------- input tsv ----------
main = [json.loads(l) for l in open(BASE / CATS[0], encoding='utf-8') if l.strip()]
clean = lambda s: (s or '').replace('\t', ' ').replace('\n', ' ').strip()
for code in sorted(NEW):
    rows = sorted((r for r in main if r['booklet_code'] == code), key=lambda r: r['workbook_ordinal'])
    out = [f"# {code} {rows[0]['booklet_name']} 共{len(rows)}篇", '# ordinal\ttitle\tquestion\tpreview']
    out += [f"{r['workbook_ordinal']}\t{clean(r['title'])}\t{clean(r['question'])}\t{clean(r.get('text_preview'))[:60]}" for r in rows]
    (D / 'input' / f'{code}.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8')
print('input tsv 重生 12 册')

# ---------- spine_manifest ----------
MP = BASE / 'spine_manifest.json'
man = json.loads(MP.read_text(encoding='utf-8'))
shutil.copy2(MP, str(MP) + '.bak_geng_' + TS)
cnt = {c: sum(1 for r in main if r['booklet_code'] == c) for c in NEW}
res = []
for e in man:
    if e['code'] in ('B38K', 'B38L'): continue
    if e['code'] in NAMES and e['code'].startswith('B38'):
        trad, _, suf = NAMES[e['code']]
        e = dict(e, desc=f'卷七·庚册·{suf}·{trad}', arts=cnt[e['code']])
    res.append(e)
    if e['code'] == 'B30':
        for code in ('B36A', 'B36B'):
            trad, _, suf = NAMES[code]
            res.append(dict(idx=0, code=code, desc=f'卷六·壬册·{suf}·{trad}', arts=cnt[code], leaves=0, pages=0, spine_mm=0,
                            dir=str(ROOT / '卷六' / '壬册' / f'{suf}册')))
for i, e in enumerate(res, 1): e['idx'] = i
MP.write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding='utf-8')
print('spine_manifest', len(res), '册')

# ---------- 归档旧庚册 docx ----------
AR = ROOT / '_legacy_archive_20261016' / ('庚册旧版_' + TS)
AR.mkdir(parents=True, exist_ok=True)
moved = 0
for br in ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']:
    d = ROOT / '卷七' / '庚册' / f'{br}册'
    if not d.exists(): continue
    if br in ('戌', '亥'):
        shutil.move(str(d), str(AR / f'{br}册')); moved += 1; continue
    for f in d.glob('岐伯论·*.docx'):
        if '外包封' in f.name: continue
        shutil.move(str(f), str(AR / f.name)); moved += 1
print('归档旧庚册', moved, '项 ->', AR)
