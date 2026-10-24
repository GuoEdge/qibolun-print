#!/usr/bin/env python3
"""
执行卷五 21 篇错位文章的精确编目调整与归位
同时修正 B20 中残留的 B02 错误代码为规范代码（B20A/B20B/B20C）
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
bak_file = BASE / f"workbook-40b-all-catalog-v4.jsonl.bak_v5adjust_{ts}"
shutil.copyfile(CAT_FILE, bak_file)
print(f"Backed up to {bak_file}")

# 2. 定义标准的分册元数据模板
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
    ('V1', 'B05'): {
        'volume_code': 'V1', 'booklet_code': 'B05', 'booklet_name': '父母控制欲与精神解绑',
        'volume_prefix': '本根敦倫', 'volume_full_title': '本根敦倫——血亲宗族与家庭抚育',
        'booklet_stem': '戊', 'booklet_stem_title': '戊冊 父母控制欲与精神解绑',
        'full_citation': '本根敦倫 · 戊冊 父母控制欲与精神解绑'
    },
    ('V1', 'B06'): {
        'volume_code': 'V1', 'booklet_code': 'B06', 'booklet_name': '成年子女自立与边界',
        'volume_prefix': '本根敦倫', 'volume_full_title': '本根敦倫——血亲宗族与家庭抚育',
        'booklet_stem': '己', 'booklet_stem_title': '己冊 成年子女自立与边界',
        'full_citation': '本根敦倫 · 己冊 成年子女自立与边界'
    },
    ('V1', 'B08'): {
        'volume_code': 'V1', 'booklet_code': 'B08', 'booklet_name': '手足同胞与家族亲戚',
        'volume_prefix': '本根敦倫', 'volume_full_title': '本根敦倫——血亲宗族与家庭抚育',
        'booklet_stem': '辛', 'booklet_stem_title': '辛冊 手足同胞与家族亲戚',
        'full_citation': '本根敦倫 · 辛冊 手足同胞与家族亲戚'
    },
    ('V2', 'B12'): {
        'volume_code': 'V2', 'booklet_code': 'B12', 'booklet_name': '婚姻存续与夫妻日常',
        'volume_prefix': '阴阳合离', 'volume_full_title': '阴阳合离——两性亲密与婚恋博弈',
        'booklet_stem': '乙', 'booklet_stem_title': '乙冊 婚姻存续与夫妻日常',
        'full_citation': '阴阳合离 · 乙冊 婚姻存续与夫妻日常'
    },
    ('V3', 'B14'): {
        'volume_code': 'V3', 'booklet_code': 'B14', 'booklet_name': '人情往来与礼数分寸',
        'volume_prefix': '酬酢防身', 'volume_full_title': '酬酢防身——熟人世道与处世防线',
        'booklet_stem': '甲', 'booklet_stem_title': '甲冊 人情往来与礼数分寸',
        'full_citation': '酬酢防身 · 甲冊 人情往来与礼数分寸'
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
    ('V5', 'B20A'): {
        'volume_code': 'V5', 'booklet_code': 'B20A', 'booklet_name': '职场汇报与权责留痕·上册',
        'volume_prefix': '度势居货', 'volume_full_title': '度势居货——职场生态与财富经营',
        'booklet_stem': '甲·上', 'booklet_stem_title': '甲冊 职场汇报与权责留痕·上册',
        'full_citation': '度势居货 · 甲冊 职场汇报与权责留痕·上册'
    },
    ('V5', 'B20B'): {
        'volume_code': 'V5', 'booklet_code': 'B20B', 'booklet_name': '职场汇报与权责留痕·中册',
        'volume_prefix': '度势居货', 'volume_full_title': '度势居货——职场生态与财富经营',
        'booklet_stem': '甲·中', 'booklet_stem_title': '甲冊 职场汇报与权责留痕·中册',
        'full_citation': '度势居货 · 甲冊 职场汇报与权责留痕·中册'
    },
    ('V5', 'B20C'): {
        'volume_code': 'V5', 'booklet_code': 'B20C', 'booklet_name': '职场汇报与权责留痕·下册',
        'volume_prefix': '度势居货', 'volume_full_title': '度势居货——职场生态与财富经营',
        'booklet_stem': '甲·下', 'booklet_stem_title': '甲冊 职场汇报与权责留痕·下册',
        'full_citation': '度势居货 · 甲冊 职场汇报与权责留痕·下册'
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
    ('V6', 'B28'): {
        'volume_code': 'V6', 'booklet_code': 'B28', 'booklet_name': '消费主义与生活观念',
        'volume_prefix': '观风察变', 'volume_full_title': '观风察变——时代透视与群体思潮',
        'booklet_stem': '己', 'booklet_stem_title': '己冊 消费主义与生活观念',
        'full_citation': '观风察变 · 己冊 消费主义与生活观念'
    },
    ('V8', 'B40'): {
        'volume_code': 'V8', 'booklet_code': 'B40', 'booklet_name': '治乱兴亡与国家工程',
        'volume_prefix': '鉴往铸器', 'volume_full_title': '鉴往铸器——艺文美学与历史治乱',
        'booklet_stem': '乙', 'booklet_stem_title': '乙冊 治乱兴亡与国家工程',
        'full_citation': '鉴往铸器 · 乙冊 治乱兴亡与国家工程'
    }
}

# 3. 定义迁移目标映射 (ordinal -> (vol, booklet))
ADJUSTMENTS = {
    52:   ('V1', 'B04'), # 战龙于野 -> 亲子沟通
    83:   ('V6', 'B23'), # 少点歧视 -> 公共热点
    85:   ('V4', 'B17'), # 多余的不开心 -> 情志平复
    216:  ('V1', 'B01'), # 亲爱无比 -> 幼儿启蒙
    296:  ('V1', 'B06'), # 不站队 -> 成年子女自立与边界
    574:  ('V6', 'B28'), # 逍遥 -> 消费主义与生活观念
    595:  ('V6', 'B28'), # 细品 -> 消费主义与生活观念
    677:  ('V4', 'B18'), # 野外迷失 -> 作息节律与病理常识(应急求生)
    939:  ('V5', 'B20A'),# 沉默的巨人 -> 职场汇报与博弈留痕
    1318: ('V8', 'B40'), # 聪明正直 -> 治乱兴亡与国家工程
    1553: ('V1', 'B03'), # 维生素M -> 言传身教与奖惩边界
    1781: ('V1', 'B05'), # 不脆弱义务 -> 父母控制欲与精神解绑
    1883: ('V5', 'B22'), # 德雷克医生 -> 商业竞争与资产投资
    1936: ('V1', 'B08'), # 缺养 -> 手足同胞与家族亲戚
    1977: ('V3', 'B14'), # 你好我好 -> 人情往来与礼数分寸
    2071: ('V5', 'B22'), # 千王之王 -> 商业竞争与资产投资
    2098: ('V8', 'B40'), # 韩军文化 -> 治乱兴亡与国家工程
    2122: ('V1', 'B04'), # 还手 -> 亲子沟通与青春叛逆
    2958: ('V6', 'B23'), # 性侵危机 -> 公共热点与事件剖析
    3529: ('V1', 'B04'), # 与世界为敌 -> 亲子沟通与青春叛逆
    4272: ('V2', 'B12'), # 在一起 -> 婚姻存续与夫妻日常
}

# 4. 执行遍历并更新记录
updated_lines = []
changed_count = 0
cleaned_b02_count = 0

with open(CAT_FILE, 'r', encoding='utf-8') as f:
    for line in f:
        if not line.strip(): continue
        item = json.loads(line)
        ord_id = item.get('workbook_ordinal')
        
        # 4.1 处理 21 篇错位调整
        if ord_id in ADJUSTMENTS:
            tgt_v, tgt_b = ADJUSTMENTS[ord_id]
            meta = META_MAP[(tgt_v, tgt_b)]
            item.update(meta)
            changed_count += 1
            print(f"Adjusted [{ord_id}] 《{item['title']}》 -> {tgt_v} {tgt_b} ({item['booklet_name']})")
        
        # 4.2 清洗 B20 中残留的 B02 错误代码
        elif item.get('volume_code') == 'V5' and item.get('booklet_code') == 'B02':
            bname = item.get('booklet_name', '')
            if '上册' in bname:
                item.update(META_MAP[('V5', 'B20A')])
            elif '中册' in bname:
                item.update(META_MAP[('V5', 'B20B')])
            elif '下册' in bname:
                item.update(META_MAP[('V5', 'B20C')])
            cleaned_b02_count += 1
            print(f"Cleaned legacy B02 [{ord_id}] 《{item['title']}》 -> {item['booklet_code']}")

        # 4.3 处理单独写为 B20A 无后缀的条目统一为标准名
        elif item.get('volume_code') == 'V5' and item.get('booklet_code') == 'B20A' and '上册' not in item.get('booklet_name', ''):
            item.update(META_MAP[('V5', 'B20A')])
            print(f"Standardized B20A [{ord_id}] 《{item['title']}》")

        updated_lines.append(json.dumps(item, ensure_ascii=False) + '\n')

# 5. 写回主编目与v4编目文件
with open(CAT_FILE, 'w', encoding='utf-8') as f:
    f.writelines(updated_lines)

# 同时保持当前目录的 catalog 统一
shutil.copyfile(CAT_FILE, MAIN_CAT)

print(f"Finished. Total changed articles: {changed_count}, legacy B02 cleaned: {cleaned_b02_count}")
