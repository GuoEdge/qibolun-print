import json, os, collections
U = '/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1/units'
mv = {}
for f in sorted(os.listdir(U + '/cls_out')):
    d = json.load(open(f'{U}/cls_out/{f}', encoding='utf-8'))
    for k, v in d['items'].items():
        mv[int(k)] = v
src = collections.Counter(v['from'] for v in mv.values())
dst = collections.Counter(v['to'] for v in mv.values())
bs = collections.Counter(v['from'].split('/')[0] for v in mv.values())
bd = collections.Counter(v['to'].split('/')[0] for v in mv.values())
conf = collections.Counter(v['conf'] for v in mv.values())
print('移动总数', len(mv), dict(conf))
print('册净变化:')
for c in sorted(set(bs) | set(bd)):
    print(f'  {c} 出{bs[c]} 入{bd[c]} 净{bd[c]-bs[c]:+d}')
print('出量最大单元:', src.most_common(15))
print('入量最大单元:', dst.most_common(15))
# 单元规模风险：移后单元不足3篇
units = {}
for f in os.listdir(U + '/out'):
    if f.endswith('.json'):
        for x in json.load(open(f'{U}/out/{f}', encoding='utf-8'))['units']:
            units[f[:-5] + '/' + x['name']] = len(x['ordinals'])
low = {u: n - src[u] + dst[u] for u, n in units.items() if n - src[u] + dst[u] < 3}
print('移后不足3篇:', low)
json.dump({str(k): v for k, v in sorted(mv.items())}, open(U + '/cls_moves_r1.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
