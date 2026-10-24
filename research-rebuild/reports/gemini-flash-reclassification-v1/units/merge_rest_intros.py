import json, os, sys, shutil, time
U = '/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1/units'
IN = os.path.join(U, 'rest_intro_out')
OUT = os.path.join(U, 'out')
APPLY = '--apply' in sys.argv
SIMP = set('这个们说来时为会学国对发经过还现进动种关于问题间头样实点没记么么当从让认业气长书东华实电话单开门见无产与后应亲爱处识区战')
errs, changes, report = [], 0, {}
stamp = time.strftime('%Y%m%d_%H%M%S')
for fn in sorted(os.listdir(IN)):
    if not fn.endswith('.json'):
        continue
    d = json.load(open(os.path.join(IN, fn), encoding='utf-8'))
    code = d['code']
    p = os.path.join(OUT, code + '.json')
    u = json.load(open(p, encoding='utf-8'))
    names = [x['name'] for x in u['units']]
    intros = d['intros']
    if set(intros) != set(names):
        errs.append(f'{code}: 键不符 缺{set(names)-set(intros)} 多{set(intros)-set(names)}')
        continue
    n = 0
    for x in u['units']:
        t = intros[x['name']].strip()
        L = len(t)
        if not (36 <= L <= 72): errs.append(f'{code}/{x["name"]}: 长度{L}')
        if '收' in t or '本單元' in t: errs.append(f'{code}/{x["name"]}: 禁字')
        if not t.endswith('。'): errs.append(f'{code}/{x["name"]}: 结尾')
        s = [c for c in t if c in SIMP]
        if s: errs.append(f'{code}/{x["name"]}: 疑简体 {"".join(s)}')
        if t != x['intro']:
            n += 1
            report.setdefault(code, []).append((x['name'], x['intro'], t))
            x['intro'] = t
    changes += n
    if APPLY and n:
        shutil.copy(p, p + '.bak_restintro_' + stamp)
        json.dump(u, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('错误', len(errs)); [print(' ', e) for e in errs]
print('改写单元', changes, '涉及册', len(report))
json.dump(report, open(os.path.join(U, 'rest_intro_diff.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
