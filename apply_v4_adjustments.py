import json
import shutil
from pathlib import Path
from datetime import datetime

BASE = Path('/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1')
CAT_FILE = BASE / 'workbook-40b-all-catalog-v4.jsonl'
MAIN_CAT = BASE / 'workbook-40b-all-catalog.jsonl'

# 1. 备份原编目文件
ts = datetime.now().strftime('%Y%m%d_%H%M%S')
bak_file = BASE / f"workbook-40b-all-catalog-v4.jsonl.bak_v4adjust_{ts}"
shutil.copyfile(CAT_FILE, bak_file)
print(f"Backed up {CAT_FILE} to {bak_file}")

if MAIN_CAT.exists():
    bak_main = BASE / f"workbook-40b-all-catalog.jsonl.bak_v4adjust_{ts}"
    shutil.copyfile(MAIN_CAT, bak_main)
    print(f"Backed up {MAIN_CAT} to {bak_main}")

# 2. 定义标准的分册元数据字典
META_MAP = {
    ('V1', 'B01'): {
        'volume_code': 'V1', 'booklet_code': 'B01', 'booklet_name': '幼儿启蒙与性情习惯',
        'volume_prefix': '本根敦倫', 'volume_full_title': '本根敦倫——血亲宗族与家庭抚育',
        'booklet_stem': '甲', 'booklet_stem_title': '甲冊 幼儿启蒙与性情习惯',
        'full_citation': '本根敦倫 · 甲冊 幼儿启蒙与性情习惯'
    },
    ('V1', 'B03'): {
        'volume_code': 'V1', 'booklet_code': 'B03', 'booklet_name': '言传身教与奖惩边界',
        'volume_prefix': '本根敦倫', 'volume_full_title': '本根敦倫——血亲宗族与家庭抚育',
        'booklet_stem': '丙', 'booklet_stem_title': '丙冊 言传身教与奖惩边界',
        'full_citation': '本根敦倫 · 丙冊 言传身教与奖惩边界'
    },
    ('V1', 'B04'): {
        'volume_code': 'V1', 'booklet_code': 'B04', 'booklet_name': '亲子沟通与青春叛逆',
        'volume_prefix': '本根敦倫', 'volume_full_title': '本根敦倫——血亲宗族与家庭抚育',
        'booklet_stem': '丁', 'booklet_stem_title': '丁冊 亲子沟通与青春叛逆',
        'full_citation': '本根敦倫 · 丁冊 亲子沟通与青春叛逆'
    },
    ('V1', 'B06'): {
        'volume_code': 'V1', 'booklet_code': 'B06', 'booklet_name': '成年子女自立与边界',
        'volume_prefix': '本根敦倫', 'volume_full_title': '本根敦倫——血亲宗族与家庭抚育',
        'booklet_stem': '己', 'booklet_stem_title': '己冊 成年子女自立与边界',
        'full_citation': '本根敦倫 · 己冊 成年子女自立与边界'
    },
    ('V2', 'B11'): {
        'volume_code': 'V2', 'booklet_code': 'B11', 'booklet_name': '择偶标准与两性吸引',
        'volume_prefix': '阴阳合离', 'volume_full_title': '阴阳合离——两性亲密与婚恋博弈',
        'booklet_stem': '甲', 'booklet_stem_title': '甲冊 择偶标准与两性吸引',
        'full_citation': '阴阳合离 · 甲冊 择偶标准与两性吸引'
    },
    ('V2', 'B12'): {
        'volume_code': 'V2', 'booklet_code': 'B12', 'booklet_name': '婚姻存续与夫妻日常',
        'volume_prefix': '阴阳合离', 'volume_full_title': '阴阳合离——两性亲密与婚恋博弈',
        'booklet_stem': '乙', 'booklet_stem_title': '乙冊 婚姻存续与夫妻日常',
        'full_citation': '阴阳合离 · 乙冊 婚姻存续与夫妻日常'
    },
    ('V3', 'B15'): {
        'volume_code': 'V3', 'booklet_code': 'B15', 'booklet_name': '社交距离与孤立自处',
        'volume_prefix': '人间世相', 'volume_full_title': '人间世相——社交往来与人情权义',
        'booklet_stem': '乙', 'booklet_stem_title': '乙冊 社交距离与孤立自处',
        'full_citation': '人间世相 · 乙冊 社交距离与孤立自处'
    },
    ('V4', 'B17'): {
        'volume_code': 'V4', 'booklet_code': 'B17', 'booklet_name': '情志平复与容貌自和',
        'volume_prefix': '存神调息', 'volume_full_title': '存神调息——身心安顿与心性知行',
        'booklet_stem': '甲', 'booklet_stem_title': '甲冊 情志平复与容貌自和',
        'full_citation': '存神调息 · 甲冊 情志平复与容貌自和'
    },
    ('V4', 'B18'): {
        'volume_code': 'V4', 'booklet_code': 'B18', 'booklet_name': '作息节律与病理常识',
        'volume_prefix': '存神调息', 'volume_full_title': '存神调息——身心安顿与心性知行',
        'booklet_stem': '乙', 'booklet_stem_title': '乙冊 作息节律与病理常识',
        'full_citation': '存神调息 · 乙冊 作息节律与病理常识'
    },
    ('V4', 'B19'): {
        'volume_code': 'V4', 'booklet_code': 'B19', 'booklet_name': '知行精进与克服拖延',
        'volume_prefix': '存神调息', 'volume_full_title': '存神调息——身心安顿与心性知行',
        'booklet_stem': '丙', 'booklet_stem_title': '丙冊 知行精进与克服拖延',
        'full_citation': '存神调息 · 丙冊 知行精进与克服拖延'
    },
    ('V5', 'B20A'): {
        'volume_code': 'V5', 'booklet_code': 'B20A', 'booklet_name': '职场汇报与权责留痕·上册',
        'volume_prefix': '度势居货', 'volume_full_title': '度势居货——职场生态与财富经营',
        'booklet_stem': '甲·上', 'booklet_stem_title': '甲冊 职场汇报与权责留痕·上册',
        'full_citation': '度势居货 · 甲冊 职场汇报与权责留痕·上册'
    },
    ('V5', 'B21'): {
        'volume_code': 'V5', 'booklet_code': 'B21', 'booklet_name': '体制生存与职业自保',
        'volume_prefix': '度势居货', 'volume_full_title': '度势居货——职场生态与财富经营',
        'booklet_stem': '乙', 'booklet_stem_title': '乙冊 体制生存与职业自保',
        'full_citation': '度势居货 · 乙冊 体制生存与职业自保'
    },
    ('V5', 'B22'): {
        'volume_code': 'V5', 'booklet_code': 'B22', 'booklet_name': '商业竞争与资产投资',
        'volume_prefix': '度势居货', 'volume_full_title': '度势居货——职场生态与财富经营',
        'booklet_stem': '丙', 'booklet_stem_title': '丙冊 商业竞争与资产投资',
        'full_citation': '度势居货 · 丙冊 商业竞争与资产投资'
    },
    ('V6', 'B23'): {
        'volume_code': 'V6', 'booklet_code': 'B23', 'booklet_name': '公共热点与事件剖析',
        'volume_prefix': '观风察变', 'volume_full_title': '观风察变——时代透视与群体思潮',
        'booklet_stem': '甲', 'booklet_stem_title': '甲冊 公共热点与事件剖析',
        'full_citation': '观风察变 · 甲冊 公共热点与事件剖析'
    },
    ('V6', 'B26'): {
        'volume_code': 'V6', 'booklet_code': 'B26', 'booklet_name': '性别议题与两性舆论',
        'volume_prefix': '观风察变', 'volume_full_title': '观风察变——时代透视与群体思潮',
        'booklet_stem': '丁', 'booklet_stem_title': '丁冊 性别议题与两性舆论',
        'full_citation': '观风察变 · 丁冊 性别议题与两性舆论'
    },
    ('V6', 'B27'): {
        'volume_code': 'V6', 'booklet_code': 'B27', 'booklet_name': '教育体制与社会流动',
        'volume_prefix': '观风察变', 'volume_full_title': '观风察变——时代透视与群体思潮',
        'booklet_stem': '戊', 'booklet_stem_title': '戊冊 教育体制与社会流动',
        'full_citation': '观风察变 · 戊冊 教育体制与社会流动'
    },
    ('V6', 'B30'): {
        'volume_code': 'V6', 'booklet_code': 'B30', 'booklet_name': '文明演进与社会秩序',
        'volume_prefix': '观风察变', 'volume_full_title': '观风察变——时代透视与群体思潮',
        'booklet_stem': '辛', 'booklet_stem_title': '辛冊 文明演进与社会秩序',
        'full_citation': '观风察变 · 辛冊 文明演进与社会秩序'
    },
    ('V7', 'B31A'): {
        'volume_code': 'V7', 'booklet_code': 'B31A', 'booklet_name': '存在本质与生命意义·上册',
        'volume_prefix': '涤除玄览', 'volume_full_title': '涤除玄览——深层哲思与名相辨析',
        'booklet_stem': '甲·上', 'booklet_stem_title': '甲冊 存在本质与生命意义·上册',
        'full_citation': '涤除玄览 · 甲冊 存在本质与生命意义·上册'
    },
    ('V7', 'B33'): {
        'volume_code': 'V7', 'booklet_code': 'B33', 'booklet_name': '善恶分野与伦理底线',
        'volume_prefix': '涤除玄览', 'volume_full_title': '涤除玄览——深层哲思与名相辨析',
        'booklet_stem': '丙', 'booklet_stem_title': '丙冊 善恶分野与伦理底线',
        'full_citation': '涤除玄览 · 丙冊 善恶分野与伦理底线'
    },
    ('V7', 'B34'): {
        'volume_code': 'V7', 'booklet_code': 'B34', 'booklet_name': '认识局限与心智模型',
        'volume_prefix': '涤除玄览', 'volume_full_title': '涤除玄览——深层哲思与名相辨析',
        'booklet_stem': '丁', 'booklet_stem_title': '丁冊 认识局限与心智模型',
        'full_citation': '涤除玄览 · 丁冊 认识局限与心智模型'
    },
    ('V7', 'B37'): {
        'volume_code': 'V7', 'booklet_code': 'B37', 'booklet_name': '神圣敬畏与信仰维度',
        'volume_prefix': '涤除玄览', 'volume_full_title': '涤除玄览——深层哲思与名相辨析',
        'booklet_stem': '庚', 'booklet_stem_title': '庚冊 神圣敬畏与信仰维度',
        'full_citation': '涤除玄览 · 庚冊 神圣敬畏与信仰维度'
    },
    ('V7', 'B38A'): {
        'volume_code': 'V7', 'booklet_code': 'B38A', 'booklet_name': '自處之道與精神獨立·子册',
        'volume_prefix': '涤除玄览', 'volume_full_title': '涤除玄览——深层哲思与名相辨析',
        'booklet_stem': '辛·子', 'booklet_stem_title': '辛冊 自處之道與精神獨立·子册',
        'full_citation': '涤除玄览 · 辛冊 自處之道與精神獨立·子册'
    },
    ('V8', 'B39'): {
        'volume_code': 'V8', 'booklet_code': 'B39', 'booklet_name': '艺能创作与生活美学',
        'volume_prefix': '鉴往铸器', 'volume_full_title': '鉴往铸器——艺文美学与历史治乱',
        'booklet_stem': '甲', 'booklet_stem_title': '甲冊 艺能创作与生活美学',
        'full_citation': '鉴往铸器 · 甲冊 艺能创作与生活美学'
    },
    ('V8', 'B40'): {
        'volume_code': 'V8', 'booklet_code': 'B40', 'booklet_name': '治乱兴亡与国家工程',
        'volume_prefix': '鉴往铸器', 'volume_full_title': '鉴往铸器——艺文美学与历史治乱',
        'booklet_stem': '乙', 'booklet_stem_title': '乙冊 治乱兴亡与国家工程',
        'full_citation': '鉴往铸器 · 乙冊 治乱兴亡与国家工程'
    }
}

REASSIGNMENTS = {
    # --- B18 调整 (12篇) ---
    '聪明的笨功夫': ('V4', 'B19'), # 留在V4，移至B19
    '内向缺陷':     ('V4', 'B17'), # 留在V4，移至B17
    '不如意金箍棒': ('V5', 'B21'),
    '地球梦':       ('V6', 'B23'),
    '片刻欢愉':     ('V2', 'B11'),
    '父母尊严':     ('V1', 'B04'),
    '大碗肉糜':     ('V7', 'B33'),
    '母乳喂养':     ('V2', 'B12'),
    '从小功利':     ('V5', 'B22'),
    '热烈和长久':   ('V2', 'B11'),
    '拿身体换':     ('V6', 'B26'),
    '野外迷失':     ('V8', 'B39'),

    # --- B19 调整 (18篇) ---
    '一蟹不如一蟹': ('V1', 'B06'),
    '四六分':       ('V5', 'B20A'),
    '投鞭断流':     ('V5', 'B20A'),
    '出门右转':     ('V2', 'B11'),
    '屋乌':         ('V2', 'B12'),
    '婚姻与稳定':   ('V6', 'B26'),
    '傲慢的两个来源':('V6', 'B30'),
    '远方的神坛':   ('V7', 'B38A'),
    '犯罪告解':     ('V7', 'B37'),
    '病得不轻':     ('V6', 'B23'),
    '优势在我':     ('V6', 'B23'),
    '生而贫穷':     ('V7', 'B31A'),
    '小县城的未来': ('V6', 'B27'),
    '持重':         ('V8', 'B40'),
    '摆脱贫穷':     ('V5', 'B22'),
    '信力':         ('V7', 'B34'),
    '永生酷刑':     ('V7', 'B31A'),
    '小而大':       ('V8', 'B39'),

    # --- B17 调整 (4篇) ---
    '有恋无爱':     ('V2', 'B11'),
    '不吭声':       ('V1', 'B04'),
    '小可靠':       ('V1', 'B03'),
    '冷且处理':     ('V3', 'B15'),
}

def update_file(path):
    print(f"\nProcessing {path} ...")
    lines = []
    updated_count = 0
    b38a_fixed_count = 0

    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.strip(): continue
            item = json.loads(line)
            title = item.get('title')
            
            # 1. 检查是否在显式重分配清单中
            if title in REASSIGNMENTS:
                vol, bcode = REASSIGNMENTS[title]
                meta = META_MAP[(vol, bcode)]
                item.update(meta)
                updated_count += 1
            # 2. 如果是 V4 中残留的 B38A（但其实属于知行精进且不在重分配清单中）
            elif item.get('volume_code') == 'V4' and item.get('booklet_code') == 'B38A':
                meta = META_MAP[('V4', 'B19')]
                item.update(meta)
                b38a_fixed_count += 1
            
            lines.append(json.dumps(item, ensure_ascii=False))

    with open(path, 'w', encoding='utf-8') as f:
        for l in lines:
            f.write(l + '\n')
            
    print(f"Updated {path}: {updated_count} reassignments, {b38a_fixed_count} B38A->B19 standardizations.")

update_file(CAT_FILE)
if MAIN_CAT.exists():
    update_file(MAIN_CAT)

print("\nAll catalog files successfully updated!")
