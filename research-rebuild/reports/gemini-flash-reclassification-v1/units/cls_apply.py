"""归类复核落地：按 cls_moves_final.json 改单元表、三份编目 META、input tsv。"""
import json, shutil, time, collections
from pathlib import Path
D = Path('/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1/units')
BASE = D.parent
TS = time.strftime('%Y%m%d_%H%M%S')
CATS = ['workbook-40b-all-catalog.jsonl', 'workbook-40b-all-catalog-v4.jsonl', 'workbook-40b-all-catalog-v5.jsonl']
META = ['volume_code', 'booklet_code', 'booklet_name', 'volume_prefix', 'volume_full_title',
        'booklet_stem', 'booklet_stem_title', 'full_citation']
mv = {int(k): v for k, v in json.loads((D / 'cls_moves_final.json').read_text(encoding='utf-8')).items()}

# ---------- 单元表 ----------
books = {}
for p in sorted((D / 'out').glob('B*.json')):
    books[p.stem] = json.loads(p.read_text(encoding='utf-8'))
where = {o: (c, u['name']) for c, b in books.items() for u in b['units'] for o in u['ordinals']}
assert len(where) == 4391, len(where)
touched = set()
for o, v in mv.items():
    fc, fu = v['from'].split('/'); tc, tu = v['to'].split('/')
    assert where[o] == (fc, fu), (o, where[o], v['from'])
    src = next(u for u in books[fc]['units'] if u['name'] == fu)
    dst = next(u for u in books[tc]['units'] if u['name'] == tu)
    src['ordinals'].remove(o); dst['ordinals'].append(o)
    touched |= {fc, tc}
for c in touched:
    p = D / 'out' / f'{c}.json'
    shutil.copy2(p, str(p) + '.bak_cls_' + TS)
    for u in books[c]['units']:
        u['ordinals'].sort()
        assert len(u['ordinals']) >= 3, (c, u['name'])
    p.write_text(json.dumps(books[c], ensure_ascii=False, indent=1), encoding='utf-8')
o2c = {o: c for c, b in books.items() for u in b['units'] for o in u['ordinals']}
assert len(o2c) == 4391

# ---------- 编目 ----------
for name in CATS:
    p = BASE / name
    rows = [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]
    tmpl = {}
    for r in rows:
        if r['workbook_ordinal'] not in mv:
            tmpl.setdefault(r['booklet_code'], {k: r[k] for k in META})
    shutil.copy2(p, str(p) + '.bak_cls_' + TS)
    n = 0
    for r in rows:
        c = o2c[r['workbook_ordinal']]
        if r['booklet_code'] != c:
            r.update(tmpl[c]); n += 1
    cnt = collections.Counter(r['booklet_code'] for r in rows)
    want = collections.Counter(o2c.values())
    assert cnt == want, name
    p.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows), encoding='utf-8')
    print(name, '改 META', n)

# ---------- input tsv ----------
main = [json.loads(l) for l in open(BASE / CATS[0], encoding='utf-8') if l.strip()]
clean = lambda s: (s or '').replace('\t', ' ').replace('\n', ' ').strip()
for code in sorted(touched):
    rows = sorted((r for r in main if r['booklet_code'] == code), key=lambda r: r['workbook_ordinal'])
    out = [f"# {code} {rows[0]['booklet_name']} 共{len(rows)}篇", '# ordinal\ttitle\tquestion\tpreview']
    out += [f"{r['workbook_ordinal']}\t{clean(r['title'])}\t{clean(r['question'])}\t{clean(r.get('text_preview'))[:60]}" for r in rows]
    p = D / 'input' / f'{code}.tsv'
    if p.exists(): shutil.copy2(p, str(p) + '.bak_cls_' + TS)
    p.write_text('\n'.join(out) + '\n', encoding='utf-8')
print('移动', len(mv), '涉及册', len(touched), '备份后缀 .bak_cls_' + TS)
