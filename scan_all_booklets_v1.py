#!/usr/bin/env python3
import json

with open('v1_full_reading_corpus.json', 'r', encoding='utf-8') as f:
    corpus = json.load(f)

by_booklet = {}
for c in corpus:
    by_booklet.setdefault(c['booklet_code'], []).append(c)

for bc in ['B02', 'B03', 'B04', 'B06', 'B08', 'B09']:
    items = by_booklet.get(bc, [])
    print(f"==================== {bc} ({items[0]['booklet_name'] if items else ''}) Total: {len(items)} ====================")
    for i, it in enumerate(items, 1):
        q = it['question'].replace('\n', ' ')[:50]
        t = it['title']
        # 打印序号、标题、问题
        if i <= 30 or i % 10 == 0 or i > len(items) - 10:
            print(f"{i:3d}. [{t}] Q: {q}")

