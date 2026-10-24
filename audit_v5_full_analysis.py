#!/usr/bin/env python3
"""
逐篇深入阅读卷五 569 篇文章，进行实质性主题契合度审查
卷五定义：度势居货 —— 职场生态与财富经营
B20（甲册）：职场汇报与权责留痕（上下级相处、沟通汇报、权责划分、办公室政治与生存、工作推进与协同）
B21（乙册）：体制生存与职业自保（体制内/机关事业单位/国企生存逻辑、升迁规律、避险防坑、规矩潜规则）
B22（丙册）：商业竞争与资产投资（创业经商、市场竞争、资产配置、买房理财、行业演变、商业逻辑）
"""

import json

with open('/storage/Users/currentUser/Documents/岐伯论/v5_entries_for_reading.json', 'r', encoding='utf-8') as f:
    entries = json.load(f)

print(f"Total entries to read: {len(entries)}")

# 打印各册文章列表概况
for slot in ['B21', 'B22', 'B20A', 'B20B', 'B20C']:
    sub = [e for e in entries if e['slot'] == slot]
    print(f"Slot {slot}: {len(sub)} articles")
