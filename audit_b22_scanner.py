#!/usr/bin/env python3
import json

with open('/storage/Users/currentUser/Documents/岐伯论/v5_entries_for_reading.json', 'r', encoding='utf-8') as f:
    entries = json.load(f)

b22 = [e for e in entries if e['slot'] == 'B22']

print(f"=== B22 (商业竞争与资产投资) 共 {len(b22)} 篇 ===")
# 扫描每一篇的原问与正文主旨
for idx, e in enumerate(b22):
    q = e['question'].replace('\n', ' ')
    t = e['text'].replace('\n', ' ')
    print(f"[{idx+1}] ID:{e['ordinal']} 《{e['title']}》")
    print(f"    问: {q[:70]}")
    print(f"    文: {t[:100]}")
