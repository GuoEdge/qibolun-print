#!/usr/bin/env python3
import json

with open('/storage/Users/currentUser/Documents/岐伯论/v5_entries_for_reading.json', 'r', encoding='utf-8') as f:
    entries = json.load(f)

# 逐篇精读分析，输出结构化的判断与详细原因
# 审查标准：
# 1. 是否属于卷五大主题（职场生态与财富经营）？
# 2. 是否属于所在具体分册（B20职场汇报与权责 / B21体制生存 / B22商业与投资）？
# 3. 若不契合，实质主题是什么？建议迁移去哪一卷哪一册？

# 详细审读每一个分册
