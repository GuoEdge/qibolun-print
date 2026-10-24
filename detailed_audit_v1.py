#!/usr/bin/env python3
import json

with open('v1_full_reading_corpus.json', 'r', encoding='utf-8') as f:
    corpus = json.load(f)

# 让我们按分册对每一篇进行审读与标记：
# 记录错位/偏离清单：(id, title, current_bc, question, text, status, target, reason)
discrepancies = []
booklet_stats = {}

for c in corpus:
    bc = c['booklet_code']
    if bc not in booklet_stats:
        booklet_stats[bc] = {'total': 0, 'fits': 0, 'internal_shift': 0, 'misplaced_out': 0}
    booklet_stats[bc]['total'] += 1

print("Booklets present:", booklet_stats)
