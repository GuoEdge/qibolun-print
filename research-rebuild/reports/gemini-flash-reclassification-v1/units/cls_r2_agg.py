import json, os, collections
U = '/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1/units'
r1 = {int(k): v for k, v in json.load(open(U + '/cls_moves_r1.json', encoding='utf-8')).items()}
r2 = {}
for f in sorted(os.listdir(U + '/cls_r2_out')):
    for k, v in json.load(open(f'{U}/cls_r2_out/{f}', encoding='utf-8'))['items'].items():
        r2[int(k)] = v
assert set(r2) == set(r1), (set(r1) - set(r2), set(r2) - set(r1))
final = {}
for o, v in r2.items():
    if v['verdict'] == 'move':
        to = v.get('to') or r1[o]['to']
        if to != r1[o]['from']:
            final[o] = {'from': r1[o]['from'], 'to': to, 'why': v['why']}
units = {}
for f in os.listdir(U + '/out'):
    if f.endswith('.json') and f[:-5] != 'B38K':
        for x in json.load(open(f'{U}/out/{f}', encoding='utf-8'))['units']:
            units[f[:-5] + '/' + x['name']] = len(x['ordinals'])
assert all(v['to'] in units for v in final.values())
src = collections.Counter(v['from'] for v in final.values())
dst = collections.Counter(v['to'] for v in final.values())
bs = collections.Counter(v['from'].split('/')[0] for v in final.values())
bd = collections.Counter(v['to'].split('/')[0] for v in final.values())
inner = sum(1 for v in final.values() if v['from'].split('/')[0] == v['to'].split('/')[0])
print('二轮确认移动', len(final), '/ 一轮', len(r1), '册内', inner, '跨册', len(final) - inner)
bk = collections.Counter(u.split('/')[0] for u in units)
bn = collections.Counter()
for u, n in units.items(): bn[u.split('/')[0]] += n
for c in sorted(bn):
    if bs[c] or bd[c]:
        print(f'  {c} {bn[c]}→{bn[c]-bs[c]+bd[c]}（出{bs[c]} 入{bd[c]}）单元{bk[c]}')
after = {u: n - src[u] + dst[u] for u, n in units.items()}
print('移后<3篇单元:', {u: n for u, n in after.items() if n < 3})
print('变动≥4篇单元:', {u: f'{units[u]}→{after[u]}' for u in units if src[u] + dst[u] >= 4})
json.dump({str(k): v for k, v in sorted(final.items())}, open(U + '/cls_moves_final.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
