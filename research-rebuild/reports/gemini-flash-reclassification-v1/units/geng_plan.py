"""庚册乙方案：按标签重组为庚册子–酉 10 本 + 卷六壬册上下，估算页数并写出 geng_plan.json。"""
import json, os, glob
B = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
U = os.path.join(B, 'units')
cat = {}
for l in open(os.path.join(B, 'workbook-40b-all-catalog-v5.jsonl'), encoding='utf-8'):
    r = json.loads(l); cat[r['workbook_ordinal']] = r
# 以现有 55 册拟合 页数 ≈ a·篇数 + b·字数 + c
man = json.load(open(os.path.join(B, 'spine_manifest.json'), encoding='utf-8'))
chars = {}
for r in cat.values(): chars[r['booklet_code']] = chars.get(r['booklet_code'], 0) + (r.get('text_len') or 0)
def bchars(code):
    return chars.get(code, 0) if code in chars else None
X, Y = [], []
for e in man:
    c = bchars(e['code'])
    if c: X.append((e['arts'], c, 1)); Y.append(e['pages'])
# 最小二乘（3 元，手写正规方程）
import itertools
M = [[sum(x[i] * x[j] for x in X) for j in range(3)] for i in range(3)]
v = [sum(x[i] * y for x, y in zip(X, Y)) for i in range(3)]
def solve(A, b):
    A = [row[:] + [bb] for row, bb in zip(A, b)]
    for i in range(3):
        p = max(range(i, 3), key=lambda k: abs(A[k][i])); A[i], A[p] = A[p], A[i]
        for k in range(3):
            if k != i:
                f = A[k][i] / A[i][i]; A[k] = [a - f * c for a, c in zip(A[k], A[i])]
    return [A[i][3] / A[i][i] for i in range(3)]
a, b, c = solve(M, v)
est = lambda arts, ch: a * arts + b * ch + c
labels = {}
for f in glob.glob(os.path.join(U, 'geng_out', '*.json')):
    for k, t in json.load(open(f, encoding='utf-8'))['labels'].items(): labels[int(k)] = t
GROUPS = [  # 标签, 新册列表 (code, stem, suffix, name, dir)
    ('X', [('B38A', '庚', '子册'), ('B38B', '庚', '丑册')], '心性自持與精神獨立'),
    ('R', [('B38C', '庚', '寅册'), ('B38D', '庚', '卯册')], '處世分寸與人我進退'),
    ('Q', [('B38E', '庚', '辰册'), ('B38F', '庚', '巳册')], '情愛家室與親子人倫'),
    ('G', [('B38G', '庚', '午册'), ('B38H', '庚', '未册')], '格物致知與技藝雜學'),
    ('Y', [('B38I', '庚', '申册'), ('B38J', '庚', '酉册')], '世情人性與義理雜談'),
    ('S', [('B36A', '壬', '上册'), ('B36B', '壬', '下册')], '時局經緯與家國論衡'),
]
plan = []
for tag, books, name in GROUPS:
    ords = sorted(o for o, t in labels.items() if t == tag)
    tot = sum(cat[o].get('text_len') or 0 for o in ords)
    # 按序号顺序切两半，使两本字数接近
    acc, cut = 0, len(ords)
    for i, o in enumerate(ords):
        acc += cat[o].get('text_len') or 0
        if acc >= tot / 2: cut = i + 1; break
    for (code, stem, suf), part in zip(books, (ords[:cut], ords[cut:])):
        ch = sum(cat[o].get('text_len') or 0 for o in part)
        p = est(len(part), ch); p = int(round(p / 2) * 2)
        plan.append(dict(code=code, volume='V6' if tag == 'S' else 'V7', stem=stem, suffix=suf, name=name,
                         tag=tag, ordinals=part, arts=len(part), chars=ch, est_pages=p,
                         est_spine=round(p / 2 * 0.095 + 0.5, 1)))
json.dump(plan, open(os.path.join(U, 'geng_plan.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'拟合: 页≈{a:.2f}·篇+{b*1000:.2f}·千字+{c:.1f}')
for e in man:
    if e['code'].startswith('B38'):
        print('  旧', e['code'], e['arts'], e['pages'], '估', int(est(e['arts'], chars[e['code']])))
for p in plan:
    vol = '卷六' if p['volume'] == 'V6' else '卷七'
    print(f"{p['code']}\t{vol}·{p['stem']}册·{p['suffix'][0]}\t{p['name']}\t{p['arts']}篇\t{p['chars']//1000}千字\t≈{p['est_pages']}P\t{p['est_spine']}mm")
print('合计', sum(p['arts'] for p in plan))
