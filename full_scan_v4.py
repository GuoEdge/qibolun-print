import json

with open('v4_entries_for_audit.json') as f:
    entries = json.load(f)

# 打印所有 254 篇的 slot, title, question, 以及第一段话
for idx, e in enumerate(entries, 1):
    slot = e['slot']
    title = e['title']
    q = e['question'].replace('\n', ' ')
    t_head = e['text'][:180].replace('\n', ' ')
    print(f"[{idx}/254] {slot} | 《{title}》")
    print(f"  问: {q}")
    print(f"  文: {t_head}")
