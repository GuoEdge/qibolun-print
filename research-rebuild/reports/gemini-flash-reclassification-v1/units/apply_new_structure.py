"""
落地脚本：执行全书 55 册架构升级
1. 建立新的册目配置表（PARTS）：
   - B38F -> V1 壬册: 卷一·壬册·庭訓教化與親恩相報 (庭训教化与亲恩相报)
   - B38E -> V2 丁册: 卷二·丁册·情義本真與兩性名理 (情义本真与两性名理)
   - B38C -> V3 丁册: 卷三·丁册·處世分寸與人我進退·上 (处世分寸与人我进退·上册)
   - B38D -> V3 戊册: 卷三·戊册·處世分寸與人我進退·下 (处世分寸与人我进退·下册)
   - B38A -> V7 庚册·子: 卷七·庚册·子·心性自持與精神獨立
   - B38B -> V7 庚册·丑: 卷七·庚册·丑·心性自持與精神獨立
   - B38I -> V7 庚册·寅: 卷七·庚册·寅·世情人性與義理雜談
   - B38J -> V7 庚册·卯: 卷七·庚册·卯·世情人性與義理雜談
   - B38G -> V8 丙册: 卷八·丙册·格物致知與機巧萬類 (格物致知与机巧万类)
   - B38H -> V8 丁册: 卷八·丁册·治家器術與聲藝百工 (治家器术与声艺百工)
2. 更新三份编目 JSONL 中的 META 字段
3. 重建 input tsv
4. 更新 spine_manifest.json
5. 更新 build_volumes_v4_v8.js 与 rebuild_all_docx.py
"""
import json, shutil, time, os
from pathlib import Path

BASE = Path('/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1')
ROOT = Path('/storage/Users/currentUser/Documents/岐伯论')
D = BASE / 'units'
TS = time.strftime('%Y%m%d_%H%M%S')
CATS = ['workbook-40b-all-catalog.jsonl', 'workbook-40b-all-catalog-v4.jsonl', 'workbook-40b-all-catalog-v5.jsonl']

# 新元数据定义：code -> meta dict
META_DEFS = {
    'B38F': {
        'volume_code': 'V1', 'volume_prefix': '本根敦倫', 'volume_full_title': '本根敦倫——血亲宗族与家庭抚育',
        'booklet_code': 'B38F', 'booklet_name': '庭训教化与亲恩相报',
        'booklet_stem': '壬', 'booklet_stem_title': '壬冊 庭训教化与亲恩相报',
        'full_citation': '本根敦倫 · 壬冊 庭训教化与亲恩相报',
        'trad_stem': '壬', 'trad_name': '庭訓教化與親恩相報', 'suffix': '全一册',
        'dir': '卷一/壬册', 'desc': '卷一·壬册·庭訓教化與親恩相報'
    },
    'B38E': {
        'volume_code': 'V2', 'volume_prefix': '陰陽合離', 'volume_full_title': '阴阳合离——两性亲密与婚恋博弈',
        'booklet_code': 'B38E', 'booklet_name': '情义本真与两性名理',
        'booklet_stem': '丁', 'booklet_stem_title': '丁冊 情义本真与两性名理',
        'full_citation': '陰陽合離 · 丁冊 情义本真与两性名理',
        'trad_stem': '丁', 'trad_name': '情義本真與兩性名理', 'suffix': '全一册',
        'dir': '卷二/丁册', 'desc': '卷二·丁册·情義本真與兩性名理'
    },
    'B38C': {
        'volume_code': 'V3', 'volume_prefix': '酬酢防身', 'volume_full_title': '酬酢防身——熟人世道与处世防线',
        'booklet_code': 'B38C', 'booklet_name': '处世分寸与人我进退·上册',
        'booklet_stem': '丁·上', 'booklet_stem_title': '丁·上册 处世分寸与人我进退·上册',
        'full_citation': '酬酢防身 · 丁·上册 处世分寸与人我进退·上册',
        'trad_stem': '丁', 'trad_name': '處世分寸與人我進退', 'suffix': '上册',
        'dir': '卷三/丁册/上册', 'desc': '卷三·丁册·上·處世分寸與人我進退'
    },
    'B38D': {
        'volume_code': 'V3', 'volume_prefix': '酬酢防身', 'volume_full_title': '酬酢防身——熟人世道与处世防线',
        'booklet_code': 'B38D', 'booklet_name': '处世分寸与人我进退·下册',
        'booklet_stem': '丁·下', 'booklet_stem_title': '丁·下册 处世分寸与人我进退·下册',
        'full_citation': '酬酢防身 · 丁·下册 处世分寸与人我进退·下册',
        'trad_stem': '丁', 'trad_name': '處世分寸與人我進退', 'suffix': '下册',
        'dir': '卷三/丁册/下册', 'desc': '卷三·丁册·下·處世分寸與人我進退'
    },
    'B38A': {
        'volume_code': 'V7', 'volume_prefix': '滌除玄覽', 'volume_full_title': '涤除玄览——深层哲思与名相辨析',
        'booklet_code': 'B38A', 'booklet_name': '心性自持与精神独立·子册',
        'booklet_stem': '庚·子', 'booklet_stem_title': '庚冊 心性自持与精神独立·子册',
        'full_citation': '涤除玄览 · 庚冊 心性自持与精神独立·子册',
        'trad_stem': '庚', 'trad_name': '心性自持與精神獨立', 'suffix': '子册',
        'dir': '卷七/庚册/子册', 'desc': '卷七·庚册·子·心性自持與精神獨立'
    },
    'B38B': {
        'volume_code': 'V7', 'volume_prefix': '滌除玄覽', 'volume_full_title': '涤除玄览——深层哲思与名相辨析',
        'booklet_code': 'B38B', 'booklet_name': '心性自持与精神独立·丑册',
        'booklet_stem': '庚·丑', 'booklet_stem_title': '庚冊 心性自持与精神独立·丑册',
        'full_citation': '涤除玄览 · 庚冊 心性自持与精神独立·丑册',
        'trad_stem': '庚', 'trad_name': '心性自持與精神獨立', 'suffix': '丑册',
        'dir': '卷七/庚册/丑册', 'desc': '卷七·庚册·丑·心性自持與精神獨立'
    },
    'B38I': {
        'volume_code': 'V7', 'volume_prefix': '滌除玄覽', 'volume_full_title': '涤除玄览——深层哲思与名相辨析',
        'booklet_code': 'B38I', 'booklet_name': '世情人性与义理杂谈·寅册',
        'booklet_stem': '庚·寅', 'booklet_stem_title': '庚冊 世情人性与义理杂谈·寅册',
        'full_citation': '涤除玄览 · 庚冊 世情人性与义理杂谈·寅册',
        'trad_stem': '庚', 'trad_name': '世情人性與義理雜談', 'suffix': '寅册',
        'dir': '卷七/庚册/寅册', 'desc': '卷七·庚册·寅·世情人性與義理雜談'
    },
    'B38J': {
        'volume_code': 'V7', 'volume_prefix': '滌除玄覽', 'volume_full_title': '涤除玄览——深层哲思与名相辨析',
        'booklet_code': 'B38J', 'booklet_name': '世情人性与义理杂谈·卯册',
        'booklet_stem': '庚·卯', 'booklet_stem_title': '庚冊 世情人性与义理杂谈·卯册',
        'full_citation': '涤除玄览 · 庚冊 世情人性与义理杂谈·卯册',
        'trad_stem': '庚', 'trad_name': '世情人性與義理雜談', 'suffix': '卯册',
        'dir': '卷七/庚册/卯册', 'desc': '卷七·庚册·卯·世情人性與義理雜談'
    },
    'B38G': {
        'volume_code': 'V8', 'volume_prefix': '鑑往鑄器', 'volume_full_title': '鉴往铸器——艺文美学与历史治乱',
        'booklet_code': 'B38G', 'booklet_name': '格物致知与机巧万类',
        'booklet_stem': '丙', 'booklet_stem_title': '丙冊 格物致知与机巧万类',
        'full_citation': '鉴往铸器 · 丙冊 格物致知与机巧万类',
        'trad_stem': '丙', 'trad_name': '格物致知與機巧萬類', 'suffix': '全一册',
        'dir': '卷八/丙册', 'desc': '卷八·丙册·格物致知與機巧萬類'
    },
    'B38H': {
        'volume_code': 'V8', 'volume_prefix': '鑑往鑄器', 'volume_full_title': '鉴往铸器——艺文美学与历史治乱',
        'booklet_code': 'B38H', 'booklet_name': '治家器术与声艺百工',
        'booklet_stem': '丁', 'booklet_stem_title': '丁冊 治家器术与声艺百工',
        'full_citation': '鉴往铸器 · 丁冊 治家器术与声艺百工',
        'trad_stem': '丁', 'trad_name': '治家器術與聲藝百工', 'suffix': '全一册',
        'dir': '卷八/丁册', 'desc': '卷八·丁册·治家器術與聲藝百工'
    }
}

# 1. 更新编目
META_FIELDS = ['volume_code', 'booklet_code', 'booklet_name', 'volume_prefix', 'volume_full_title',
               'booklet_stem', 'booklet_stem_title', 'full_citation']
for cat_name in CATS:
    p = BASE / cat_name
    rows = [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]
    shutil.copy2(p, str(p) + '.bak_upgrade_' + TS)
    n = 0
    for r in rows:
        code = r['booklet_code']
        if code in META_DEFS:
            for k in META_FIELDS:
                r[k] = META_DEFS[code][k]
            n += 1
    p.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows), encoding='utf-8')
    print(f'{cat_name} 更新 META: {n} 条')

# 2. 更新 input tsv
main = [json.loads(l) for l in open(BASE / CATS[0], encoding='utf-8') if l.strip()]
clean = lambda s: (s or '').replace('\t', ' ').replace('\n', ' ').strip()
for code in META_DEFS:
    rows = sorted((r for r in main if r['booklet_code'] == code), key=lambda r: r['workbook_ordinal'])
    out = [f"# {code} {rows[0]['booklet_name']} 共{len(rows)}篇", '# ordinal\ttitle\tquestion\tpreview']
    out += [f"{r['workbook_ordinal']}\t{clean(r['title'])}\t{clean(r['question'])}\t{clean(r.get('text_preview'))[:60]}" for r in rows]
    tsv_p = D / 'input' / f'{code}.tsv'
    if tsv_p.exists(): shutil.copy2(tsv_p, str(tsv_p) + '.bak_upgrade_' + TS)
    tsv_p.write_text('\n'.join(out) + '\n', encoding='utf-8')
print('input tsv 更新完成')

# 3. 更新 spine_manifest.json 顺序与属性
MP = BASE / 'spine_manifest.json'
man = json.loads(MP.read_text(encoding='utf-8'))
shutil.copy2(MP, str(MP) + '.bak_upgrade_' + TS)
man_map = {e['code']: e for e in man}

# 编排新的 55 册顺序
NEW_ORDER = [
    # 卷一 (11)
    'B01', 'B02A', 'B02B', 'B02C', 'B03', 'B04', 'B05', 'B06', 'B07', 'B08', 'B38F',
    # 卷二 (4)
    'B11', 'B12', 'B13', 'B38E',
    # 卷三 (5)
    'B14', 'B15', 'B16', 'B38C', 'B38D',
    # 卷四 (3)
    'B17A', 'B17B', 'B18',
    # 卷五 (5)
    'B20A', 'B20B', 'B20C', 'B22A', 'B22B',
    # 卷六 (11)
    'B23A', 'B23B', 'B24', 'B25', 'B26', 'B27', 'B28', 'B29', 'B30', 'B36A', 'B36B',
    # 卷七 (12)
    'B31A', 'B31B', 'B32A', 'B32B', 'B33', 'B34', 'B35', 'B37', 'B38A', 'B38B', 'B38I', 'B38J',
    # 卷八 (4)
    'B38G', 'B38H', 'B39', 'B40'
]

new_man = []
for idx, code in enumerate(NEW_ORDER, 1):
    e = dict(man_map[code])
    e['idx'] = idx
    if code in META_DEFS:
        m = META_DEFS[code]
        e['desc'] = m['desc']
        e['dir'] = str(ROOT / m['dir'])
    new_man.append(e)

MP.write_text(json.dumps(new_man, ensure_ascii=False, indent=2), encoding='utf-8')
print(f'spine_manifest.json 更新完成，共 {len(new_man)} 册')
