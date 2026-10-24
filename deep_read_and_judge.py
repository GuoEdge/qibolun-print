import json

with open('v4_entries_for_audit.json') as f:
    entries = json.load(f)

# 编写通读分析脚本，把每篇的题目、问题、核心逻辑和审查结论输出
# 针对每一篇，输出：
# 1. 标题与所在册 (B17/B18/B19)
# 2. 问答核心实质（全文概括）
# 3. 契合度评级：【契合】/【微偏/建议调整】/【严重错位】
# 4. 理由与建议去向

print(f"Loaded {len(entries)} entries.")
