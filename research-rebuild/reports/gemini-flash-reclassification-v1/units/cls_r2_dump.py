"""第二轮：把第一轮拟移的篇目导出全文，附上原单元和目标单元的导语，分块供子代理回读复核。"""
import json, os
U = '/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1/units'
B = os.path.dirname(U)
D = U + '/cls_r2_in'; os.makedirs(D, exist_ok=True); os.makedirs(U + '/cls_r2_out', exist_ok=True)
for f in os.listdir(D): os.remove(os.path.join(D, f))
mv = {int(k): v for k, v in json.load(open(U + '/cls_moves_r1.json', encoding='utf-8')).items()}
intro = {}
for f in os.listdir(U + '/out'):
    if f.endswith('.json'):
        for x in json.load(open(f'{U}/out/{f}', encoding='utf-8'))['units']:
            intro[f[:-5] + '/' + x['name']] = x['intro']
corpus = {}
for l in open(B + '/all-articles-merged-v3.jsonl', encoding='utf-8'):
    r = json.loads(l); corpus[r['id']] = r
cat = {}
for l in open(B + '/workbook-40b-all-catalog.jsonl', encoding='utf-8'):
    r = json.loads(l); cat[r['workbook_ordinal']] = r
chunks, cur, size = [], [], 0
for o in sorted(mv):
    v = mv[o]; c = cat[o]; t = corpus[c['original_id']]
    txt = (t.get('text') or '').strip()
    q = c.get('question') or t.get('question') or ''
    s = (f'\n=== 【{o}】{c["title"]}\n'
         f'现位置：{v["from"]}——{intro[v["from"]]}\n'
         f'拟移至：{v["to"]}——{intro[v["to"]]}\n'
         f'一轮理由：{v["why"]}（{v["conf"]}）\n問：{q}\n答：\n{txt}\n')
    cur.append(s); size += len(txt)
    if size >= 40000: chunks.append(cur); cur, size = [], 0
if cur: chunks.append(cur)
for i, ch in enumerate(chunks, 1):
    open(f'{D}/M{i:02d}.md', 'w', encoding='utf-8').write(''.join(ch))
print('篇', len(mv), '块', len(chunks), [len(c) for c in chunks])
