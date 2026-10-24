import json

with open('v4_entries_for_audit.json') as f:
    entries = json.load(f)

print(f"Total entries to audit: {len(entries)}")

# 让我们输出完整的文本，按分册 B18, B19, B17 分开深入通读
