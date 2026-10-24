"""为成员变动的单元生成导语复核底稿：现导语 + 现有全部篇目（标注新入）+ 移出篇目。"""
import json, os
U = '/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1/units'
tg = json.load(open(U + '/cls_intro_targets.json', encoding='utf-8'))
mv = json.load(open(U + '/cls_moves_final.json', encoding='utf-8'))
g = {}
for k, v in json.load(open(U + '/geng_labels_final.json', encoding='utf-8')).items(): g[k] = v['gist']
for k, v in json.load(open(U + '/rest_gists_final.json', encoding='utf-8')).items(): g[k] = v['gist']
title = {}
for l in open(U + '/../workbook-40b-all-catalog.jsonl', encoding='utf-8'):
    r = json.loads(l); title[r['workbook_ordinal']] = r['title']
D = U + '/cls_intro_in'; os.makedirs(D, exist_ok=True); os.makedirs(U + '/cls_intro_out', exist_ok=True)
for f in os.listdir(D): os.remove(os.path.join(D, f))
blocks = []
for key in tg:
    c, n = key.split('/')
    u = next(x for x in json.load(open(f'{U}/out/{c}.json', encoding='utf-8'))['units'] if x['name'] == n)
    s = [f'\n## {key}（{len(u["ordinals"])}篇）', f'现导语：{u["intro"]}']
    for o in u['ordinals']:
        tag = '【新入】' if mv.get(str(o), {}).get('to') == key else ''
        s.append(f'- {o}｜{title[o]}｜{g[str(o)]}{tag}')
    out = [o for o, v in mv.items() if v['from'] == key]
    if out:
        s.append('已移出：' + '；'.join(f'{title[int(o)]}（{g[o]}）' for o in out))
    blocks.append('\n'.join(s))
n = 8
size = -(-len(blocks) // n)
for i in range(n):
    part = blocks[i * size:(i + 1) * size]
    if part:
        open(f'{D}/I{i + 1:02d}.md', 'w', encoding='utf-8').write('# 成员变动单元导语复核底稿\n' + '\n'.join(part) + '\n')
print('单元', len(blocks), '块', len(os.listdir(D)))
