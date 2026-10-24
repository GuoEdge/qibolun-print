import json

with open('v4_entries_for_audit.json') as f:
    entries = json.load(f)

# 输出每篇的 slot, 标题, 问, 以及全文的前300字
for e in entries:
    print(f"ID:{e['id']} | SLOT:{e['slot']} | TITLE:{e['title']}")
    print(f"Q:{e['question']}")
    print(f"T:{e['text'][:150].replace(chr(10), ' ')}")
    print("="*60)
