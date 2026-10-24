#!/usr/bin/env python3
import json

with open('/storage/Users/currentUser/Documents/岐伯论/v5_entries_for_reading.json', 'r', encoding='utf-8') as f:
    entries = json.load(f)

b22 = [e for e in entries if e['slot'] == 'B22']
print(f"Total B22: {len(b22)}")

# 输出每篇的标题、问、以及前120字答
with open('/storage/Users/currentUser/Documents/岐伯论/b22_reading_list.txt', 'w', encoding='utf-8') as out:
    for i, e in enumerate(b22):
        q = e['question'].replace('\n', ' ')
        t = e['text'][:120].replace('\n', ' ')
        out.write(f"[{i+1}] ID:{e['ordinal']} 《{e['title']}》\n问: {q}\n文: {t}\n\n")

print("Exported b22_reading_list.txt")
