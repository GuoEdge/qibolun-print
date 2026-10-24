"""主题域汇总：各域篇数、在现有各册的分布、各册主域纯度。"""
import json, os, glob, collections
U = '/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1/units'
NM = dict(A='子女教养', B='成年亲子与家族', C='婚恋两性', D='人际处世', E='身心修养', F='职场事业', G='商业财富',
          H='时局公共', I='社会思潮', J='科技格物', K='哲思义理', L='信仰宗教', M='艺文美学', N='历史兵事')
dom = {}
for f in sorted(os.listdir(U + '/dom_out')):
    for k, v in json.load(open(f'{U}/dom_out/{f}', encoding='utf-8'))['items'].items():
        dom[int(k)] = v
o2c = {}
for p in glob.glob(U + '/out/B*.json'):
    for u in json.load(open(p, encoding='utf-8'))['units']:
        for o in u['ordinals']: o2c[o] = os.path.basename(p)[:-5]
assert set(dom) == set(o2c), (len(dom), len(o2c), list(set(o2c) - set(dom))[:5])
tot = collections.Counter(v['d'] for v in dom.values())
alt = sum(1 for v in dom.values() if v.get('alt'))
print('总篇', len(dom), '带alt', alt)
by = collections.defaultdict(collections.Counter)
for o, v in dom.items(): by[v['d']][o2c[o]] += 1
for d in sorted(tot):
    print(f'{d} {NM[d]} {tot[d]}篇 分布{len(by[d])}册:', ' '.join(f'{c}:{n}' for c, n in by[d].most_common(10)))
print('\n各册主域纯度:')
bc = collections.defaultdict(collections.Counter)
for o, v in dom.items(): bc[o2c[o]][v['d']] += 1
for c in sorted(bc):
    n = sum(bc[c].values()); top = bc[c].most_common(3)
    print(f'{c} {n} 主域{top[0][0]} {top[0][1]*100//n}% |', ' '.join(f'{d}{k}' for d, k in top))
json.dump({str(k): v for k, v in sorted(dom.items())}, open(U + '/dom_final.json', 'w', encoding='utf-8'), ensure_ascii=False)
