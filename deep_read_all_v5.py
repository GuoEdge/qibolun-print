#!/usr/bin/env python3
"""
全文通读分析卷五569篇文章
输出各册的逐篇内容主旨、实际讨论场景、与册主题的实质契合判断，
以及建议调整/错位文章的详细清单。
"""

import json
from collections import Counter

with open('/storage/Users/currentUser/Documents/岐伯论/v5_entries_for_reading.json', 'r', encoding='utf-8') as f:
    entries = json.load(f)

# B20 上/中/下: 职场汇报与权责留痕 (356篇)
# B21: 体制生存与职业自保 (25篇)
# B22: 商业竞争与资产投资 (188篇)

results = []

for e in entries:
    slot = e['slot']
    ord_id = e['ordinal']
    title = e['title']
    q = e['question'].strip()
    t = e['text'].strip()
    
    # 记录待分析条目
    results.append({
        'ordinal': ord_id,
        'title': title,
        'slot': slot,
        'question': q,
        'text': t,
        'len': len(t)
    })

print(f"Loaded {len(results)} articles.")

# 将B20分为3组，B21一组，B22一组，分别写入专门的审查分析文本以供审查
for target_slot in ['B21', 'B22', 'B20A', 'B20B', 'B20C']:
    sub = [r for r in results if r['slot'] == target_slot]
    with open(f'/storage/Users/currentUser/Documents/岐伯论/v5_{target_slot}_reading.txt', 'w', encoding='utf-8') as out:
        for idx, item in enumerate(sub):
            out.write(f"[{idx+1}/{len(sub)}] ID:{item['ordinal']} 《{item['title']}》\n")
            out.write(f"【原问】{item['question']}\n")
            # 写入前500字供精读
            out.write(f"【正文摘录】\n{item['text'][:500]}\n")
            out.write("="*70 + "\n\n")

print("Generated reading files for all slots.")
