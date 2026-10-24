"""导出庚册 B38A–L 全部篇目全文，按约 45k 字切块，供逐篇通读判定。"""
import json, os
B = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(B, 'units', 'geng_full')
os.makedirs(D, exist_ok=True)
for f in os.listdir(D): os.remove(os.path.join(D, f))
corpus = {}
for l in open(os.path.join(B, 'all-articles-merged-v3.jsonl'), encoding='utf-8'):
    r = json.loads(l); corpus[r['id']] = r
rows, miss = [], []
for l in open(os.path.join(B, 'workbook-40b-all-catalog-v5.jsonl'), encoding='utf-8'):
    r = json.loads(l)
    if r['booklet_code'].startswith('B38'):
        c = corpus.get(r['original_id'])
        if not c: miss.append(r['workbook_ordinal']); continue
        rows.append((r['workbook_ordinal'], r['title'], r.get('question') or c.get('question') or '', c.get('text') or ''))
rows.sort()
chunks, cur, size = [], [], 0
for x in rows:
    cur.append(x); size += len(x[3])
    if size >= 45000: chunks.append(cur); cur, size = [], 0
if cur: chunks.append(cur)
for i, ch in enumerate(chunks, 1):
    with open(os.path.join(D, f'G{i:02d}.md'), 'w', encoding='utf-8') as f:
        for o, t, q, txt in ch:
            f.write(f'\n=== 【{o}】{t}\n問：{q}\n答：\n{txt.strip()}\n')
    print(f'G{i:02d}', len(ch), '篇', sum(len(x[3]) for x in ch), '字', ch[0][0], '-', ch[-1][0])
print('合计', len(rows), '缺正文', miss)
