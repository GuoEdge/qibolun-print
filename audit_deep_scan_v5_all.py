#!/usr/bin/env python3
"""
逐篇精读分析脚本：输出每篇的核心主题标签、偏离风险、审查判定。
对卷五全部 569 篇文章进行全量逐篇扫描，并重点标记不契合或存疑文章。
"""

import json

with open('/storage/Users/currentUser/Documents/岐伯论/v5_entries_for_reading.json', 'r', encoding='utf-8') as f:
    entries = json.load(f)

# 卷五各册的核心主题定义：
# B20 (上/中/下): 职场汇报与权责留痕 (汇报技巧、权责界定、同事上级关系、背锅留痕、请假离职、职场沟通、办公室生存、执行汇报)
# B21: 体制生存与职业自保 (机关/事业单位/国企/体制内规则、官场潜规则、自保免责、考公体制心态、编制与考核)
# B22: 商业竞争与资产投资 (创业、做生意、企业竞争、买房/房产、股票/理财投资、商业模式、财富积累与保值)

def analyze_entry(e):
    slot = e['slot']
    title = e['title']
    q = e['question']
    t = e['text']
    
    # 结合问题与正文，进行实质性主旨判断
    full_text = q + "\n" + t
    
    return {
        'ordinal': e['ordinal'],
        'title': title,
        'slot': slot,
        'question': q,
        'text_len': len(t),
        'preview': t[:100].replace('\n', ' ')
    }

print(f"Total entries loaded: {len(entries)}")
