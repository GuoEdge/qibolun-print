"""按全文复判标签，为每类导出篇目清单（标题/问题/正文主旨/字数），供子代理排 2 册单元。"""
import json, os, glob
U = os.path.dirname(os.path.abspath(__file__))
B = os.path.dirname(U)
D = os.path.join(U, 'geng_units_in'); os.makedirs(D, exist_ok=True)
os.makedirs(os.path.join(U, 'geng_units_out'), exist_ok=True)
cat = {}
for l in open(os.path.join(B, 'workbook-40b-all-catalog.jsonl'), encoding='utf-8'):
    r = json.loads(l); cat[r['workbook_ordinal']] = r
lab = {int(k): v for k, v in json.load(open(os.path.join(U, 'geng_labels_final.json'), encoding='utf-8')).items()}
# 其他册已用单元名（新单元名不得与之重复）
used = []
for f in glob.glob(os.path.join(U, 'out', '*.json')):
    d = json.load(open(f, encoding='utf-8'))
    if not d['code'].startswith('B38'):
        used += [u['name'] for u in d['units']]
open(os.path.join(D, '_used_names.txt'), 'w', encoding='utf-8').write('\n'.join(sorted(used)) + '\n')
BOOKS = {
    'X': ('B38A', 'B38B', '心性自持與精神獨立'), 'R': ('B38C', 'B38D', '處世分寸與人我進退'),
    'Q': ('B38E', 'B38F', '情愛家室與親子人倫'), 'G': ('B38G', 'B38H', '格物致知與技藝雜學'),
    'Y': ('B38I', 'B38J', '世情人性與義理雜談'), 'S': ('B36A', 'B36B', '時局經緯與家國論衡'),
}
cl = lambda s: (s or '').replace('\t', ' ').replace('\n', ' ').strip()
for tag, (c1, c2, name) in BOOKS.items():
    ords = sorted(o for o, v in lab.items() if v['tag'] == tag)
    tot = sum(cat[o]['text_len'] or 0 for o in ords)
    with open(os.path.join(D, tag + '.tsv'), 'w', encoding='utf-8') as f:
        f.write(f'# {tag} {name}：{len(ords)} 篇，共 {tot} 字；分为 {c1}（上）与 {c2}（下）两册\n')
        f.write('# 序号\t字数\t标题\t问题\t正文主旨\n')
        for o in ords:
            f.write(f"{o}\t{cat[o]['text_len']}\t{cl(cat[o]['title'])}\t{cl(cat[o]['question'])}\t{cl(lab[o]['gist'])}\n")
    print(tag, c1, c2, name, len(ords), tot)
print('已用单元名', len(used))
