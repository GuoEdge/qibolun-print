#!/usr/bin/env python3
"""
逐篇全量通读审阅卷五全部 569 篇文章
判断维度：
1. 宏观主题：是否属于卷五【度势居货 —— 职场生态与财富经营】？
   - 包含：职场上下级/同事关系、权力责任、办公室生存、体制内官场生存、商业创业做生意、投资理财资产配置、商业竞争策略等。
   - 偏离大卷判定：若内容实质为家庭抚育（V1）、婚恋情感（V2）、熟人人际防身礼数（V3）、身心调养与个人心性（V4）、社会群体时代观察（V6）、纯形而上哲学名相（V7）、文艺审美技术工程（V8）。
2. 分册微观定位：
   - B20（甲册 上/中/下）：职场汇报与权责留痕（侧重职场企业生态、上下级相处、沟通汇报、背锅防坑、权责边界、团队管理）
   - B21（乙册）：体制生存与职业自保（侧重机关、事业单位、公务员、国企等体制内生存、政治站位与人事自保、编制考核）
   - B22（丙册）：商业竞争与资产投资（侧重创业经商、商业竞争、商业模式、资产配置、买房房产、股票投资理财、财富逻辑）
"""

import json

with open('/storage/Users/currentUser/Documents/岐伯论/v5_entries_for_reading.json', 'r', encoding='utf-8') as f:
    entries = json.load(f)

# 输出全部569篇的标题、原问、正文前250字至综合阅读文件
with open('/storage/Users/currentUser/Documents/岐伯论/v5_all_reading_corpus.txt', 'w', encoding='utf-8') as f:
    for i, e in enumerate(entries):
        f.write(f"[{i+1}] ORD:{e['ordinal']} SLOT:{e['slot']} TITLE:《{e['title']}》\n")
        f.write(f"Q: {e['question'].strip()}\n")
        f.write(f"T: {e['text'][:350].strip().replace(chr(10), ' ')}\n")
        f.write("-" * 80 + "\n")

print(f"Generated v5_all_reading_corpus.txt with {len(entries)} entries.")
