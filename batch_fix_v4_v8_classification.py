#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量修正卷四至卷八错误分类
根据人工核查清单更新编目总表中的 volume_code 和 booklet_code
"""

import json
import csv
import sys
from pathlib import Path

# 修正映射表
CORRECTIONS = {
    '登堂入室': ('V5', 'B20', '职场汇报与权责留痕'),
    '虚与实': ('V5', 'B20', '职场汇报与权责留痕'),
    '真想要': ('V5', 'B20', '职场汇报与权责留痕'),
    '豪华感之和': ('V5', 'B22', '商业竞争与资产投资'),
    '胜半子': ('V6', 'B29', '现代科技与工具反思'),
    '大法庭': ('V6', 'B23', '公共热点与事件剖析'),
    '几时崩溃': ('V8', 'B40', '治乱兴亡与国家工程'),
    '以卵击石': ('V8', 'B39', '艺能创作与生活美学'),
    '照骨镜': ('V6', 'B23', '公共热点与事件剖析'),
    '什么自信': ('V6', 'B29', '现代科技与工具反思'),
    '天眼查': ('V8', 'B39', '艺能创作与生活美学'),
    '监守者难辞其咎': ('V6', 'B23', '公共热点与事件剖析'),
    '尖夵': ('V6', 'B23', '公共热点与事件剖析'),
    '私刑': ('V6', 'B23', '公共热点与事件剖析'),
    '恶来儿': ('V6', 'B23', '公共热点与事件剖析'),
    '一毛': ('V6', 'B23', '公共热点与事件剖析'),
    '逍遥': ('V5', 'B22', '商业竞争与资产投资'),
    '成功之母': ('V5', 'B20', '职场汇报与权责留痕'),
    '组织生鲜供应': ('V6', 'B23', '公共热点与事件剖析'),
    '劳资蜀道山': ('V8', 'B39', '艺能创作与生活美学'),
    '人字拖神教': ('V7', 'B31', '存在本质与生命意义'),
    '冷且处理': ('V4', 'B17', '情志平复与容貌自和'),
    '心不动': ('V4', 'B17', '情志平复与容貌自和'),
    '要有光': ('V4', 'B17', '情志平复与容貌自和'),
    '情绪大师': ('V4', 'B17', '情志平复与容貌自和'),
    '需求表达困难': ('V4', 'B17', '情志平复与容貌自和'),
    'before trial': ('V6', 'B23', '公共热点与事件剖析'),
    '打出来': ('V6', 'B23', '公共热点与事件剖析'),
    '副武器': ('V6', 'B23', '公共热点与事件剖析'),
    '叛徒的代价': ('V6', 'B23', '公共热点与事件剖析'),
    '学霸': ('V8', 'B40', '治乱兴亡与国家工程'),
    '粮食禁运': ('V6', 'B23', '公共热点与事件剖析'),
    '俄乌战争': ('V8', 'B40', '治乱兴亡与国家工程'),
    '主动的被动': ('V2', 'B11', '择偶标准与两性吸引'),
    '使用说明': ('V2', 'B12', '婚姻存续与夫妻日常'),
    '最终困难': ('V2', 'B13', '亲密背叛与离异止损'),
    '有困难就说': ('V5', 'B20', '职场汇报与权责留痕'),
    '摘星': ('V6', 'B23', '公共热点与事件剖析'),
    '失心': ('V8', 'B39', '艺能创作与生活美学'),
    '软鼓': ('V6', 'B28', '消费主义与生活观念'),
    '免责在先': ('V6', 'B23', '公共热点与事件剖析'),
    '非猎不食': ('V6', 'B23', '公共热点与事件剖析'),
    '长江天险': ('V8', 'B40', '治乱兴亡与国家工程'),
    '世界史': ('V6', 'B27', '教育体制与社会流动'),
    '弹道学': ('V6', 'B29', '现代科技与工具反思'),
    '芯片': ('V6', 'B29', '现代科技与工具反思'),
    '夺门而入': ('V8', 'B40', '治乱兴亡与国家工程'),
    '轻而圆': ('V6', 'B28', '消费主义与生活观念'),
    '长明火': ('V6', 'B29', '现代科技与工具反思'),
    '乐见其道': ('V6', 'B23', '公共热点与事件剖析'),
    '道德': ('V7', 'B33', '善恶分野与伦理底线'),
    '一亿一天': ('V5', 'B22', '商业竞争与资产投资'),
    '通胀义务': ('V5', 'B22', '商业竞争与资产投资'),
    '禽兽之败': ('V8', 'B39', '艺能创作与生活美学'),
}

# 卷名映射
VOLUME_NAMES = {
    'V1': ('本根敦倫', '血亲宗族与家庭抚育'),
    'V2': ('阴阳合离', '两性亲密与婚恋博弈'),
    'V3': ('人间世相', '社交往来与人情权义'),
    'V4': ('存神调息', '身心安顿与心性知行'),
    'V5': ('度势居货', '职场生态与财富经营'),
    'V6': ('观风察变', '时代透视与群体思潮'),
    'V7': ('涤除玄览', '深层哲思与名相辨析'),
    'V8': ('鉴往铸器', '艺文美学与历史治乱'),
}

# 册名映射（天干）
BOOKLET_STEMS = {
    'B01': '甲', 'B02': '乙', 'B03': '丙', 'B04': '丁', 'B05': '戊',
    'B06': '己', 'B07': '庚', 'B08': '辛', 'B09': '壬', 'B10': '癸',
    'B11': '甲', 'B12': '乙', 'B13': '丙', 'B14': '丁', 'B15': '戊',
    'B16': '己', 'B17': '甲', 'B18': '乙', 'B19': '丙', 'B20': '甲',
    'B21': '乙', 'B22': '丙', 'B23': '甲', 'B24': '乙', 'B25': '丙',
    'B26': '丁', 'B27': '戊', 'B28': '己', 'B29': '庚', 'B30': '辛',
    'B31': '甲', 'B32': '乙', 'B33': '丙', 'B34': '丁', 'B35': '戊',
    'B36': '己', 'B37': '庚', 'B38': '辛', 'B39': '甲', 'B40': '乙',
}


def update_catalog(input_path, output_path):
    """更新编目总表"""
    modified_count = 0
    total_count = 0
    modified_titles = []
    
    with open(input_path, 'r', encoding='utf-8') as f_in, \
         open(output_path, 'w', encoding='utf-8') as f_out:
        
        for line in f_in:
            line = line.strip()
            if not line:
                continue
            
            try:
                record = json.loads(line)
                total_count += 1
                title = record.get('title', '')
                
                # 检查是否需要修正
                if title in CORRECTIONS:
                    old_volume = record.get('volume_code', '')
                    old_booklet = record.get('booklet_code', '')
                    
                    new_volume, new_booklet, new_booklet_name = CORRECTIONS[title]
                    
                    # 更新字段
                    record['volume_code'] = new_volume
                    record['booklet_code'] = new_booklet
                    record['booklet_name'] = new_booklet_name
                    
                    # 更新联动字段
                    if new_volume in VOLUME_NAMES:
                        volume_prefix, volume_subtitle = VOLUME_NAMES[new_volume]
                        record['volume_prefix'] = volume_prefix
                        record['volume_full_title'] = f"{volume_prefix}——{volume_subtitle}"
                    
                    if new_booklet in BOOKLET_STEMS:
                        booklet_stem = BOOKLET_STEMS[new_booklet]
                        record['booklet_stem'] = booklet_stem
                        record['booklet_stem_title'] = f"{booklet_stem}冊 {new_booklet_name}"
                    
                    # 更新完整引文
                    record['full_citation'] = f"{record.get('volume_prefix', '')} · {record.get('booklet_stem', '')}冊 {new_booklet_name}"
                    
                    modified_count += 1
                    modified_titles.append(f"{title}: {old_volume}·{old_booklet} → {new_volume}·{new_booklet}")
                    print(f"✓ 修正: {title}")
                    print(f"  {old_volume}·{old_booklet} → {new_volume}·{new_booklet} {new_booklet_name}")
                
                # 写入记录
                f_out.write(json.dumps(record, ensure_ascii=False) + '\n')
                
            except json.JSONDecodeError as e:
                print(f"⚠ JSON解析错误，跳过此行: {e}", file=sys.stderr)
                continue
    
    return modified_count, total_count, modified_titles


def main():
    # 文件路径
    catalog_path = Path('/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1/workbook-40b-all-catalog.jsonl')
    backup_path = catalog_path.with_suffix('.jsonl.bak-before-v4v8-fix')
    output_path = catalog_path
    
    if not catalog_path.exists():
        print(f"❌ 编目总表不存在: {catalog_path}")
        return 1
    
    # 备份
    print(f"📦 备份原文件...")
    import shutil
    shutil.copy2(catalog_path, backup_path)
    print(f"✓ 备份完成: {backup_path}")
    
    # 执行修正
    print(f"\n🔧 开始批量修正...")
    temp_output = catalog_path.with_suffix('.jsonl.tmp')
    modified, total, titles = update_catalog(catalog_path, temp_output)
    
    # 替换原文件
    temp_output.replace(output_path)
    
    # 输出结果
    print(f"\n{'='*60}")
    print(f"✅ 批量修正完成")
    print(f"{'='*60}")
    print(f"总记录数: {total}")
    print(f"修正数量: {modified}")
    print(f"修正清单:")
    for i, title in enumerate(titles, 1):
        print(f"  {i}. {title}")
    
    print(f"\n📄 输出文件: {output_path}")
    print(f"💾 备份文件: {backup_path}")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
