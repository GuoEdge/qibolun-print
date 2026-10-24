"""合并 rest_full_out 主旨，核对覆盖；为 41 个编码各出一份「单元→篇目主旨」清单，供按全文复核导语。"""
import json, os, glob, collections
U = os.path.dirname(os.path.abspath(__file__))
B = os.path.dirname(U)
G = {}
for f in sorted(glob.glob(os.path.join(U, 'rest_full_out', 'R*.json'))):
    for k, v in json.load(open(f, encoding='utf-8'))['items'].items():
        G[int(k)] = v
cat = {}
for l in open(os.path.join(B, 'workbook-40b-all-catalog.jsonl'), encoding='utf-8'):
    r = json.loads(l); cat[r['workbook_ordinal']] = r
D = os.path.join(U, 'rest_intro_in'); os.makedirs(D, exist_ok=True)
os.makedirs(os.path.join(U, 'rest_intro_out'), exist_ok=True)
need, miss, mis = 0, [], collections.defaultdict(list)
for f in sorted(glob.glob(os.path.join(U, 'out', '*.json'))):
    d = json.load(open(f, encoding='utf-8'))
    if d['code'][:3] in ('B36', 'B38'): continue
    L = [f"# {d['code']} {cat[d['units'][0]['ordinals'][0]]['booklet_name']}", '']
    for u in d['units']:
        L.append(f"## {u['name']}（{len(u['ordinals'])} 篇）")
        L.append(f"现导语：{u['intro']}")
        for o in u['ordinals']:
            need += 1
            g = G.get(o)
            if not g: miss.append(o); continue
            flag = '' if g.get('fit', 1) else f"　【离题：{g.get('note','')}】"
            if not g.get('fit', 1): mis[d['code']].append((o, u['name'], g.get('note', '')))
            L.append(f"- {o}｜{cat[o]['title']}｜{g['gist']}{flag}")
        L.append('')
    open(os.path.join(D, d['code'] + '.md'), 'w', encoding='utf-8').write('\n'.join(L))
json.dump({str(k): v for k, v in sorted(G.items())}, open(os.path.join(U, 'rest_gists_final.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print('应有', need, '已得', len(G), '缺', miss[:20])
print('离题合计', sum(len(v) for v in mis.values()))
for c, v in sorted(mis.items()): print(c, len(v), [x[0] for x in v])
