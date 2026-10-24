import json

with open('v4_entries_for_audit.json') as f:
    entries = json.load(f)

# 让我们系统化遍历并生成每篇的细读评估结果
# 定义判断逻辑辅助

print(f"Total entries: {len(entries)}")

# 打印所有B19中明显可疑的文章
