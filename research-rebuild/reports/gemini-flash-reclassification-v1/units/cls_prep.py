import json, os, collections
B = '/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1'
U = B + '/units'
cat = [json.loads(l) for l in open(B + '/workbook-40b-all-catalog-v5.jsonl', encoding='utf-8')]
meta = collections.OrderedDict()
for r in cat:
    meta.setdefault(r['booklet_code'], (r['volume_full_title'], r['booklet_stem_title']))
codes = sorted(meta)
units, o2u = {}, {}
for c in codes:
    units[c] = json.load(open(f'{U}/out/{c}.json', encoding='utf-8'))['units']
    for x in units[c]:
        for o in x['ordinals']:
            o2u[o] = (c, x['name'])
gist = {}
for k, v in json.load(open(U + '/rest_gists_final.json', encoding='utf-8')).items():
    gist[int(k)] = v['gist']
for k, v in json.load(open(U + '/geng_labels_final.json', encoding='utf-8')).items():
    gist.setdefault(int(k), v['gist'])
# 分类体系
lines = ['# 《岐伯論》全书分类体系（55 册 / 277 单元）', '']
vol = None
for c in codes:
    vt, bt = meta[c]
    if vt != vol:
        lines += ['', f'## {vt}']; vol = vt
    n = sum(len(x['ordinals']) for x in units[c])
    lines.append(f'### {c}　{bt}（{n}篇）')
    for x in units[c]:
        lines.append(f'- {c}/{x["name"]}（{len(x["ordinals"])}）：{x["intro"]}')
open(U + '/taxonomy.md', 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
# 分块：按册顺序，每块约 110 篇，不跨册拆单元
os.makedirs(U + '/cls_in', exist_ok=True)
for f in os.listdir(U + '/cls_in'):
    os.remove(U + '/cls_in/' + f)
byo = {r['workbook_ordinal']: r for r in cat}
miss = [o for o in byo if o not in gist or o not in o2u]
chunks, cur = [], []
for c in codes:
    rows = []
    for x in units[c]:
        for o in x['ordinals']:
            r = byo[o]
            q = (r.get('question') or '').replace('\n', ' ')[:70]
            rows.append(f'{o}｜{c}/{x["name"]}｜{r["title"]}｜{q}｜{gist.get(o, "")}')
    if cur and len(cur) + len(rows) > 130:
        chunks.append(cur); cur = []
    cur += rows
chunks.append(cur)
for i, ch in enumerate(chunks, 1):
    open(f'{U}/cls_in/C{i:02d}.md', 'w', encoding='utf-8').write(
        '# 序号｜现册/现单元｜标题｜问题（截）｜全文主旨\n' + '\n'.join(ch) + '\n')
print('篇数', len(byo), '缺主旨或单元', len(miss), '块数', len(chunks), [len(c) for c in chunks])
