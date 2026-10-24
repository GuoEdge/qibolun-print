import json
from pathlib import Path

with open('v4_entries_for_audit.json', 'r', encoding='utf-8') as f:
    entries = json.load(f)

print(f"Total entries: {len(entries)}")

# 打印每一篇的基本信息
for idx, e in enumerate(entries, 1):
    # 提取正文前200字
    preview = e['text'][:200].replace('\n', ' ')
    # 准备后续审查
