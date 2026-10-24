#!/usr/bin/env python3
"""
执行卷二（阴阳合离）28 篇错位文章的精确编目调整与归位
包括：
- 15 篇迁出卷二至更契合的卷册 (V1, V3, V4, V5, V6, V7, V8)
- 13 篇卷二内部册间对调归位 (B11, B12, B13)
"""

import json
import shutil
from pathlib import Path
from datetime import datetime

BASE = Path('/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1')
CAT_FILE = BASE / 'workbook-40b-all-catalog-v4.jsonl'
MAIN_CAT = BASE / 'workbook-40b-all-catalog.jsonl'

# 1. 备份原编目文件
ts = datetime.now().strftime('%Y%m%d_%H%M%S')
bak_file = BASE / f"workbook-40b-all-catalog-v4.jsonl.bak_v2adjust_{ts}"
shutil.copyfile(CAT_FILE, bak_file)
print(f"Backed up {CAT_FILE} to {bak_file}")

if MAIN_CAT.exists():
    bak_main = BASE / f"workbook-40b-all-catalog.jsonl.bak_v2adjust_{ts}"
    shutil.copyfile(MAIN_CAT, bak_main)
    print(f"Backed up {MAIN_CAT} to {bak_main}")

# 2. 标准分册元数据模板
META_MAP = {
    ('V1', 'B01'): {
        'volume_code': 'V1', 'booklet_code': 'B01', 'booklet_name': '幼儿启蒙与性情习惯',
        'volume_prefix': '本根敦倫', 'volume_full_title': '本根敦倫——血亲宗族与家庭抚育',
        'booklet_stem': '甲', 'booklet_stem_title': '甲冊 幼儿启蒙与性情习惯',
        'full_citation': '本根敦倫 · 甲冊 幼儿启蒙与性情习惯'
    },
    ('V1', 'B02'): {
        'volume_code': 'V1', 'booklet_code': 'B02', 'booklet_name': '学业功课与学校日常',
        'volume_prefix': '本根敦倫', 'volume_full_title': '本根敦倫——血亲宗族与家庭抚育',
        'booklet_stem': '乙', 'booklet_stem_title': '乙冊 学业功课与学校日常',
        'full_citation': '本根敦倫 · 乙冊 学业功课与学校日常'
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
    ('V2', 'B13'): {
        'volume_code': 'V2', 'booklet_code': 'B13', 'booklet_name': '亲密背叛与离异止损',
        'volume_prefix': '阴阳合离', 'volume_full_title': '阴阳合离——两性亲密与婚恋博弈',
        'booklet_stem': '丙', 'booklet_stem_title': '丙冊 亲密背叛与离异止损',
        'full_citation': '阴阳合离 · 丙冊 亲密背叛与离异止损'
    },
    ('V3', 'B14'): {
        'volume_code': 'V3', 'booklet_code': 'B14', 'booklet_name': '人情往来与礼数分寸',
        'volume_prefix': '酬酢防身', 'volume_full_title': '酬酢防身——熟人世道与处世防线',
        'booklet_stem': '甲', 'booklet_stem_title': '甲冊 人情往来与礼数分寸',
        'full_citation': '酬酢防身 · 甲冊 人情往来与礼数分寸'
    },
    ('V3', 'B16'): {
        'volume_code': 'V3', 'booklet_code': 'B16', 'booklet_name': '危机识人与权义守界',
        'volume_prefix': '酬酢防身', 'volume_full_title': '酬酢防身——熟人世道与处世防线',
        'booklet_stem': '丙', 'booklet_stem_title': '丙冊 危机识人与权义守界',
        'full_citation': '酬酢防身 · 丙冊 危机识人与权义守界'
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
        'booklet_stem': '甲', 'booklet_stem_title': '甲冊 职场汇报与权责留痕·上册',
        'full_citation': '度势居货 · 甲冊 职场汇报与权责留痕·上册'
    },
    ('V6', 'B23'): {
        'volume_code': 'V6', 'booklet_code': 'B23', 'booklet_name': '公共热点与事件剖析',
        'volume_prefix': '观风察变', 'volume_full_title': '观风察变——时代透视与群体思潮',
        'booklet_stem': '甲', 'booklet_stem_title': '甲冊 公共热点与事件剖析',
        'full_citation': '观风察变 · 甲冊 公共热点与事件剖析'
    },
    ('V6', 'B25'): {
        'volume_code': 'V6', 'booklet_code': 'B25', 'booklet_name': '网络生态与群体极化',
        'volume_prefix': '观风察变', 'volume_full_title': '观风察变——时代透视与群体思潮',
        'booklet_stem': '丙', 'booklet_stem_title': '丙冊 网络生态与群体极化',
        'full_citation': '观风察变 · 丙冊 网络生态与群体极化'
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
    ('V7', 'B35'): {
        'volume_code': 'V7', 'booklet_code': 'B35', 'booklet_name': '命途因果与得失随缘',
        'volume_prefix': '涤除玄览', 'volume_full_title': '涤除玄览——深层哲思与名相辨析',
        'booklet_stem': '戊', 'booklet_stem_title': '戊冊 命途因果与得失随缘',
        'full_citation': '涤除玄览 · 戊冊 命途因果与得失随缘'
    },
    ('V8', 'B40'): {
        'volume_code': 'V8', 'booklet_code': 'B40', 'booklet_name': '治乱兴亡与国家工程',
        'volume_prefix': '鉴往铸器', 'volume_full_title': '鉴往铸器——艺文美学与历史治乱',
        'booklet_stem': '乙', 'booklet_stem_title': '乙冊 治乱兴亡与国家工程',
        'full_citation': '鉴往铸器 · 乙冊 治乱兴亡与国家工程'
    }
}

# 3. 目标调整映射表 (title -> (target_vol, target_booklet))
ADJUSTMENTS = {
    # 一、迁出卷二 (15篇)
    '勉强': ('V7', 'B34'),              # 改房梁/改结构成本高，因势利导心智模型
    '早恋1': ('V1', 'B04'),             # 父母应对子女早恋，监护责任与亲子沟通
    '歧视的自由': ('V7', 'B33'),         # 平等与偏见本质，事前机会与善恶伦理
    '不可论断人': ('V7', 'B33'),         # 判断权代理与伦理关系本质
    '射鸟': ('V3', 'B16'),              # 不违法不代表免除社会制裁，危机识人与防身
    'ToTheEnd': ('V6', 'B25'),          # 网络极端对立思潮与群体极化批判
    '车道问题': ('V1', 'B02'),          # 11岁儿童教育，社会公共交往规则
    '雷峰夕照': ('V7', 'B34'),          # 水至清则无鱼，容纳隐私防非战斗减员
    '富贵囚人': ('V6', 'B23'),          # 剧组夫妻，演艺明星被异化为商业资产
    '无罪可言': ('V1', 'B03'),          # 单亲父女创伤修复，家庭责任伦理
    '经纪人': ('V5', 'B20A'),           # 艺人经纪人制度缺失与资产安全看护
    '尘心说': ('V7', 'B35'),            # 破除宿命论，命途因果与得失随缘
    'The Game of Mole': ('V4', 'B19'),  # 科学计算预警与知行精进
    '情绪失控的孩子': ('V1', 'B04'),     # 10岁男孩情绪引导与亲子心理
    '不屈节': ('V1', 'B03'),            # 17岁父母闹离婚，分担家务自立谋生孝道

    # 二、内部册间对调 (13篇)
    # 调入 B11 甲册 (8篇)
    '姬别霸王': ('V2', 'B11'),          # 恋爱期女友要求过高，吸引力与精神斗志
    '于爱无违': ('V2', 'B11'),          # 大学恋爱期开玩笑谈家务，恋爱共同体构建
    '情侣话题': ('V2', 'B11'),          # 增进感情的话题，恋爱沟通与理解训练
    '大前门': ('V2', 'B11'),            # 相亲约会男生抠门，“无能而不自知”择偶筛选
    '天河': ('V2', 'B11'),              # 恋爱起步如何提供情绪价值与建立吸引力
    '别互补': ('V2', 'B11'),            # 恋爱择偶中性格互补与自洽解耦
    '性': ('V2', 'B11'),                # 恋爱何时发生性关系，婚前责任与底线筛选
    '断续': ('V2', 'B11'),              # 男友有遗传病，婚前筛选的抉择

    # 调入 B12 乙册 (2篇)
    '余庆': ('V2', 'B12'),              # 结婚十年夫妻磨合与权责沟通
    '新手村之王': ('V2', 'B12'),        # 为何追求白头到老，婚姻长期的深层探索

    # 调入 B13 丙册 (3篇)
    '绝对安全': ('V2', 'B13'),          # 如何安全离开暴力倾向男友，危机关系统筹与止损
    '公开换安全': ('V2', 'B13'),        # 学生会职务恋爱中的风险识别与止损哲学
    'one last chance': ('V2', 'B13'),   # 婚外怀孕出轨，重大背叛与离婚谈判
}

def update_file(filepath):
    updated_items = []
    applied_count = 0
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.strip(): continue
            item = json.loads(line)
            title = item.get('title')
            if title in ADJUSTMENTS:
                target_v, target_b = ADJUSTMENTS[title]
                target_meta = META_MAP[(target_v, target_b)]
                # 更新元数据
                item['volume_code'] = target_meta['volume_code']
                item['booklet_code'] = target_meta['booklet_code']
                item['booklet_name'] = target_meta['booklet_name']
                item['volume_prefix'] = target_meta['volume_prefix']
                item['volume_full_title'] = target_meta['volume_full_title']
                item['booklet_stem'] = target_meta['booklet_stem']
                item['booklet_stem_title'] = target_meta['booklet_stem_title']
                item['full_citation'] = target_meta['full_citation']
                applied_count += 1
            updated_items.append(item)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        for it in updated_items:
            f.write(json.dumps(it, ensure_ascii=False) + '\n')
    
    print(f"Updated {filepath}: applied {applied_count}/{len(ADJUSTMENTS)} adjustments.")

update_file(CAT_FILE)
if MAIN_CAT.exists():
    update_file(MAIN_CAT)

print("All catalog files updated successfully.")
