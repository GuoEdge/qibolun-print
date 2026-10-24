"""导出庚册 B38A–L 全部篇目，供逐篇判定归属。"""
import json, os
B = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(B, 'units', 'geng_in')
os.makedirs(D, exist_ok=True)
rows = {}
for l in open(os.path.join(B, 'workbook-40b-all-catalog-v5.jsonl'), encoding='utf-8'):
    r = json.loads(l)
    if r['booklet_code'].startswith('B38'):
        rows.setdefault(r['booklet_code'], []).append(r)
for code, rs in sorted(rows.items()):
    with open(os.path.join(D, code + '.tsv'), 'w', encoding='utf-8') as f:
        for r in sorted(rs, key=lambda x: x['workbook_ordinal']):
            prev = (r.get('text_preview') or '').replace('\n', ' ').replace('\t', ' ')[:90]
            q = (r.get('question') or '').replace('\t', ' ')
            f.write(f"{r['workbook_ordinal']}\t{r['title']}\t{q}\t{prev}\n")
print({k: len(v) for k, v in rows.items()}, sum(len(v) for v in rows.values()))
