"""导出庚册/壬册以外 43 册全文（按册、按单元顺序），切成约 45k 字的块，供逐篇通读写主旨。"""
import json, os, glob
U = os.path.dirname(os.path.abspath(__file__))
B = os.path.dirname(U)
D = os.path.join(U, 'rest_full'); os.makedirs(D, exist_ok=True)
os.makedirs(os.path.join(U, 'rest_full_out'), exist_ok=True)
for f in os.listdir(D): os.remove(os.path.join(D, f))
corpus = {}
for l in open(os.path.join(B, 'all-articles-merged-v3.jsonl'), encoding='utf-8'):
    r = json.loads(l); corpus[r['id']] = r
cat = {}
for l in open(os.path.join(B, 'workbook-40b-all-catalog.jsonl'), encoding='utf-8'):
    r = json.loads(l); cat[r['workbook_ordinal']] = r
items = []  # (code, unit, ordinal, title, q, text)
for f in sorted(glob.glob(os.path.join(U, 'out', '*.json'))):
    d = json.load(open(f, encoding='utf-8'))
    if d['code'][:3] in ('B36', 'B38'): continue
    for u in d['units']:
        for o in u['ordinals']:
            c = cat[o]; t = corpus[c['original_id']]
            items.append((d['code'], u['name'], o, c['title'], c.get('question') or t.get('question') or '', (t.get('text') or '').strip()))
chunks, cur, size = [], [], 0
for x in items:
    cur.append(x); size += len(x[5])
    if size >= 45000: chunks.append(cur); cur, size = [], 0
if cur: chunks.append(cur)
for i, ch in enumerate(chunks, 1):
    with open(os.path.join(D, f'R{i:02d}.md'), 'w', encoding='utf-8') as f:
        for code, un, o, t, q, txt in ch:
            f.write(f'\n=== 【{o}】{t}　〔{code}·{un}〕\n問：{q}\n答：\n{txt}\n')
print('册', len({x[0] for x in items}), '篇', len(items), '字', sum(len(x[5]) for x in items), '块', len(chunks))
