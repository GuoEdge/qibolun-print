"""
落地大卷名称升级脚本（方案一·经典稳健型）：
1. 卷名升级映射：
   - V1: prefix='本根敦倫', full='本根敦倫——血親宗族與家庭撫育', full_simp='本根敦伦——血亲宗族与家庭抚育'
   - V2: prefix='陰陽合離', full='陰陽合離——兩性親密與情義名理', full_simp='阴阳合离——两性亲密与情义名理'
   - V3: prefix='酬酢進退', full='酬酢進退——人我分寸與處世防線', full_simp='酬酢进退——人我分寸与处世防线'
   - V4: prefix='存神調息', full='存神調息——身心安頓與心性知行', full_simp='存神调息——身心安顿与心性知行'
   - V5: prefix='度勢居貨', full='度勢居貨——職場博弈與財富商道', full_simp='度势居货——职场博弈与财富商道'
   - V6: prefix='觀風察變', full='觀風察變——時代思潮與家國時局', full_simp='观风察变——时代思潮与家国时局'
   - V7: prefix='滌除玄覽', full='滌除玄覽——深層哲思與義理名相', full_simp='涤除玄览——深层哲思与义理名相'
   - V8: prefix='格物鑄器', full='格物鑄器——造物工程與歷史治亂', full_simp='格物铸器——造物工程与历史治乱'
2. 更新三份编目 JSONL 中的 volume_prefix, volume_full_title 与 full_citation
3. 更新 build_volumes_v4_v8.js 中的 VOLUME_TRAD
4. 更新 build_all_covers.js 中的卷名定义
"""
import json, shutil, time, os
from pathlib import Path

BASE = Path('/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1')
TS = time.strftime('%Y%m%d_%H%M%S')
CATS = ['workbook-40b-all-catalog.jsonl', 'workbook-40b-all-catalog-v4.jsonl', 'workbook-40b-all-catalog-v5.jsonl']

VOL_MAP = {
    'V1': {
        'prefix': '本根敦倫',
        'full_trad': '本根敦倫——血親宗族與家庭撫育',
        'full_simp': '本根敦伦——血亲宗族与家庭抚育'
    },
    'V2': {
        'prefix': '陰陽合離',
        'full_trad': '陰陽合離——兩性親密與情義名理',
        'full_simp': '阴阳合离——两性亲密与情义名理'
    },
    'V3': {
        'prefix': '酬酢進退',
        'full_trad': '酬酢進退——人我分寸與處世防線',
        'full_simp': '酬酢进退——人我分寸与处世防线'
    },
    'V4': {
        'prefix': '存神調息',
        'full_trad': '存神調息——身心安頓與心性知行',
        'full_simp': '存神调息——身心安顿与心性知行'
    },
    'V5': {
        'prefix': '度勢居貨',
        'full_trad': '度勢居貨——職場博弈與財富商道',
        'full_simp': '度势居货——职场博弈与财富商道'
    },
    'V6': {
        'prefix': '觀風察變',
        'full_trad': '觀風察變——時代思潮與家國時局',
        'full_simp': '观风察变——时代思潮与家国时局'
    },
    'V7': {
        'prefix': '滌除玄覽',
        'full_trad': '滌除玄覽——深層哲思與義理名相',
        'full_simp': '涤除玄览——深层哲思与义理名相'
    },
    'V8': {
        'prefix': '格物鑄器',
        'full_trad': '格物鑄器——造物工程與歷史治亂',
        'full_simp': '格物铸器——造物工程与历史治乱'
    }
}

# 1. 更新编目 JSONL
for name in CATS:
    p = BASE / name
    rows = [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]
    shutil.copy2(p, str(p) + '.bak_volnames_' + TS)
    for r in rows:
        v = r['volume_code']
        vm = VOL_MAP[v]
        r['volume_prefix'] = vm['prefix']
        r['volume_full_title'] = vm['full_simp']
        # full_citation: 卷前缀 · 册名
        stem_title = r.get('booklet_stem_title') or (r.get('booklet_stem', '') + '冊 ' + r.get('booklet_name', ''))
        r['full_citation'] = f"{vm['prefix']} · {stem_title}"
    p.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows), encoding='utf-8')
    print(f'{name} 更新大卷名称完成')

# 2. 更新 build_volumes_v4_v8.js 中的 VOLUME_TRAD
bv_file = BASE / 'build_volumes_v4_v8.js'
bv_text = bv_file.read_text(encoding='utf-8')
shutil.copy2(bv_file, str(bv_file) + '.bak_volnames_' + TS)

old_vt = """const VOLUME_TRAD = {
  'V3': { prefix: '酬酢防身', full: '酬酢防身——熟人世道與處世防線', dirName: '卷三', coverLabel: '【 卷  三 】' },
  'V4': { prefix: '存神調息', full: '存神調息——身心安頓與心性知行', dirName: '卷四', coverLabel: '【 卷  四 】' },
  'V5': { prefix: '度勢居貨', full: '度勢居貨——職場生態與財富經營', dirName: '卷五', coverLabel: '【 卷  五 】' },
  'V6': { prefix: '觀風察變', full: '觀風察變——時代透視與群體思潮', dirName: '卷六', coverLabel: '【 卷  六 】' },
  'V7': { prefix: '滌除玄覽', full: '滌除玄覽——深層哲思與名相辨析', dirName: '卷七', coverLabel: '【 卷  七 】' },
  'V8': { prefix: '鑑往鑄器', full: '鑑往鑄器——藝文美學與歷史治亂', dirName: '卷八', coverLabel: '【 卷  八 】' }
};"""

new_vt = """const VOLUME_TRAD = {
  'V3': { prefix: '酬酢進退', full: '酬酢進退——人我分寸與處世防線', dirName: '卷三', coverLabel: '【 卷  三 】' },
  'V4': { prefix: '存神調息', full: '存神調息——身心安頓與心性知行', dirName: '卷四', coverLabel: '【 卷  四 】' },
  'V5': { prefix: '度勢居貨', full: '度勢居貨——職場博弈與財富商道', dirName: '卷五', coverLabel: '【 卷  五 】' },
  'V6': { prefix: '觀風察變', full: '觀風察變——時代思潮與家國時局', dirName: '卷六', coverLabel: '【 卷  六 】' },
  'V7': { prefix: '滌除玄覽', full: '滌除玄覽——深層哲思與義理名相', dirName: '卷七', coverLabel: '【 卷  七 】' },
  'V8': { prefix: '格物鑄器', full: '格物鑄器——造物工程與歷史治亂', dirName: '卷八', coverLabel: '【 卷  八 】' }
};"""

assert old_vt in bv_text, "未找到 VOLUME_TRAD"
bv_file.write_text(bv_text.replace(old_vt, new_vt), encoding='utf-8')
print('build_volumes_v4_v8.js 更新 VOLUME_TRAD 完成')

# 3. 更新 build_all_covers.js
cov_file = BASE / 'build_all_covers.js'
cov_text = cov_file.read_text(encoding='utf-8')
shutil.copy2(cov_file, str(cov_file) + '.bak_volnames_' + TS)

cov_text = cov_text.replace("V3: { num: '【 卷  三 】', full: '【 卷  三 】 酬酢防身', prefix: '卷三', dir: '卷三' }",
                            "V3: { num: '【 卷  三 】', full: '【 卷  三 】 酬酢進退', prefix: '卷三', dir: '卷三' }")
cov_text = cov_text.replace("V8: { num: '【 卷  八 】', full: '【 卷  八 】 鑑往鑄器', prefix: '卷八', dir: '卷八' }",
                            "V8: { num: '【 卷  八 】', full: '【 卷  八 】 格物鑄器', prefix: '卷八', dir: '卷八' }")
cov_file.write_text(cov_text, encoding='utf-8')
print('build_all_covers.js 更新卷名完成')
