"""
全书结构升级方案详细测算脚本
基于“因题立骨、借象明理”原则：
1. 分析当前八卷的篇数、册数分布
2. 测算庚册（B38）各分册向对应卷回填后的物理容量影响：
   - B38F (82篇) 回填 V1（本根敦伦·亲子）
   - B38E (89篇) 回填 V2（阴阳合离·婚恋）
   - B38C/D (264篇) 回填 V3（酬酢防身·处世）
   - B38G/H (235篇) 回填 V8（鉴往铸器·格物技艺）
   - 留卷七：B38A/B/I/J 与原 B31-B37，专注于纯粹哲思、心性、名理、正义与信仰
3. 输出各卷升级前后的篇数、分册规划与页数/厚度预估
"""
import json, os, glob, collections

U = '/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1/units'
man = json.load(open(os.path.join(U, '..', 'spine_manifest.json'), encoding='utf-8'))
dom = {int(k): v for k, v in json.load(open(os.path.join(U, 'dom_final.json'), encoding='utf-8')).items()}

# 当前各册篇数与页数
arts_curr = {e['code']: e['arts'] for e in man}
pages_curr = {e['code']: e['pages'] for e in man}

print("=== 当前各卷基线状态 ===")
vol_codes = collections.defaultdict(list)
for e in man:
    code = e['code']
    if code.startswith('B0') or code.startswith('B02'): v = 'V1'
    elif code in ('B11', 'B12', 'B13'): v = 'V2'
    elif code in ('B14', 'B15', 'B16'): v = 'V3'
    elif code in ('B17A', 'B17B', 'B18'): v = 'V4'
    elif code.startswith('B20') or code.startswith('B22'): v = 'V5'
    elif code.startswith('B2') or code.startswith('B30') or code.startswith('B36'): v = 'V6'
    elif code.startswith('B31') or code.startswith('B32') or code in ('B33','B34','B35','B37') or code.startswith('B38'): v = 'V7'
    elif code in ('B39', 'B40'): v = 'V8'
    else: v = 'OTHER'
    vol_codes[v].append(code)

for v in sorted(vol_codes):
    codes = vol_codes[v]
    tot_a = sum(arts_curr[c] for c in codes)
    tot_p = sum(pages_curr[c] for c in codes)
    print(f"{v}: {len(codes):2d}册 | {tot_a:4d}篇 | {tot_p:5d}P (平均每册 {tot_p//len(codes):3d}P)")

print("\n=== 回填方案测算 ===")
# V1: 原602篇(10册) + B38F(82篇,1册) = 684篇(11册)
# V2: 原214篇(3册) + B38E(89篇,1册) = 303篇(4册)
# V3: 原123篇(3册) + B38C/D(264篇,2册) = 387篇(5册)
# V4: 原242篇(3册) = 242篇(3册) (身心知行)
# V5: 原537篇(5册) = 537篇(5册) (职场商业)
# V6: 原723篇(11册) = 723篇(11册) (思潮时政)
# V7: 原1850篇(18册) - 回填(670篇,6册) = 1180篇(12册)
# V8: 原100篇(2册) + B38G/H(235篇,2册) = 335篇(4册)
# 全书总册数: 11 + 4 + 5 + 3 + 5 + 11 + 12 + 4 = 55 册！完美守恒！

proposal = [
    ('V1', '本根敦倫——血親宗族與家庭撫育', 10, 11, 602, 684, '吸纳 B38F 为卷尾【庭訓教化篇】(增1册)'),
    ('V2', '陰陽合離——兩性親密與婚戀博弈', 3, 4, 214, 303, '吸纳 B38E 为卷尾【情愛名理篇】(增1册)'),
    ('V3', '酬酢防身——熟人世道與處世防線', 3, 5, 123, 387, '吸纳 B38C/D 为【人我進退篇·上/下】(增2册)'),
    ('V4', '存神調息——身心安頓與心性知行', 3, 3, 242, 242, '维持现有3册，内部理顺情绪、作息与练功'),
    ('V5', '度勢居貨——職場生態與財富經營', 5, 5, 537, 537, '维持现有5册，厘清求职汇报、组织政治与投资'),
    ('V6', '觀風察變——時代透視與群體思潮', 11, 11, 723, 723, '维持现有11册(含壬册时局2册)，收敛思潮热点'),
    ('V7', '滌除玄覽——深層哲思與名相辨析', 18, 12, 1850, 1180, '剥离实务，聚焦B31-B35,B37及B38子丑申酉(减6册)'),
    ('V8', '鑑往鑄器——藝文美學與歷史治亂', 2, 4, 100, 335, '吸纳 B38G/H 格物技艺杂学(增2册)，丰满历史器物')
]

print(f"{'卷号':<4} {'卷名':<20} {'原册':<4} {'新册':<4} {'原篇':<5} {'新篇':<5} {'改造要点'}")
for v, name, oc, nc, oa, na, note in proposal:
    print(f"{v:<4} {name:<20} {oc:2d}册  {nc:2d}册  {oa:4d}篇 {na:4d}篇  {note}")

print("\n全书总册数：原 55 册 -> 新 55 册（总册数完全一致，无需打破大书箱印装规划！）")
