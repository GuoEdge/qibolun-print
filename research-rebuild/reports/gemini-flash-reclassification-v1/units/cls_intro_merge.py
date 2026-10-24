import json, os, sys, shutil, time
U = '/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1/units'
APPLY = '--apply' in sys.argv
SIMP = set('这个们说时为会学国对发经过还现进动种关问题间实点么当从让业长书电话单开门见无产与后应亲爱处识区')
tg = set(json.load(open(U + '/cls_intro_targets.json', encoding='utf-8')))
new = {}
for f in sorted(os.listdir(U + '/cls_intro_out')):
    new.update(json.load(open(f'{U}/cls_intro_out/{f}', encoding='utf-8'))['intros'])
errs = []
if set(new) != tg: errs.append(f'键不符 缺{tg-set(new)} 多{set(new)-tg}')
diff, by = [], {}
for k, v in new.items():
    t = v['intro'].strip()
    if not (36 <= len(t) <= 72): errs.append(f'{k} 长度{len(t)}')
    if '收' in t or '本單元' in t: errs.append(f'{k} 禁字')
    if not t.endswith('。'): errs.append(f'{k} 结尾')
    s = ''.join(c for c in t if c in SIMP)
    if s: errs.append(f'{k} 疑简体 {s}')
    by.setdefault(k.split('/')[0], {})[k.split('/')[1]] = t
stamp = time.strftime('%Y%m%d_%H%M%S')
for c, m in by.items():
    p = f'{U}/out/{c}.json'; b = json.load(open(p, encoding='utf-8')); n = 0
    for x in b['units']:
        if x['name'] in m and m[x['name']] != x['intro']:
            diff.append((f'{c}/{x["name"]}', x['intro'], m[x['name']])); x['intro'] = m[x['name']]; n += 1
    if APPLY and n:
        shutil.copy(p, p + '.bak_clsintro_' + stamp)
        json.dump(b, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('错误', len(errs)); [print(' ', e) for e in errs]
print('改写', len(diff))
json.dump(diff, open(U + '/cls_intro_diff.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
