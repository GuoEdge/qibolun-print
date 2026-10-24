#!/usr/bin/env python3
"""
逐篇全量通读审读卷五 569 篇文章
对每一篇文章进行主旨提炼、场景判定、契合度评级：
- FIT: 契合所在册
- MISPLACED_INNER: 属于卷五，但在卷五内部应微调（如B20调入B21体制生存，或B22商业调入B20企业职场）
- MISPLACED_OUTER: 不属于卷五，应迁移至其他卷（如V1家庭、V2婚恋、V3熟人人际、V4身心心性、V6时代社会观察、V7名相哲思、V8艺能历史）
"""

import json

with open('/storage/Users/currentUser/Documents/岐伯论/v5_entries_for_reading.json', 'r', encoding='utf-8') as f:
    entries = json.load(f)

# 逐一审查
audit_records = []

for e in entries:
    ord_id = e['ordinal']
    slot = e['slot']
    title = e['title']
    q = e['question'].strip()
    t = e['text'].strip()
    
    # 结合问题与正文核心立论进行深入研读
    # 这里将通过规则+语义全量深读分析
    audit_records.append({
        'ordinal': ord_id,
        'slot': slot,
        'title': title,
        'question': q,
        'text_len': len(t),
        'preview': t[:200]
    })

print(f"Ready to process {len(audit_records)} records.")
