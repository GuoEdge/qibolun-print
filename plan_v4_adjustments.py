import json

with open('v4_entries_for_audit.json') as f:
    entries = json.load(f)

# 打印所有可能需要调整的篇目当前的信息
# 包括 original_id, ordinal, title, current slot, current raw_bcode
