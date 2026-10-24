import json
from pathlib import Path

with open('v4_entries_for_audit.json') as f:
    entries = json.load(f)

# 将 entries 按 slot 分组
by_slot = {'B17': [], 'B18': [], 'B19': []}
for e in entries:
    by_slot[e['slot']].append(e)

print(f"B17: {len(by_slot['B17'])}篇")
print(f"B18: {len(by_slot['B18'])}篇")
print(f"B19: {len(by_slot['B19'])}篇")
