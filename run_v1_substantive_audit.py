#!/usr/bin/env python3
"""
深度逐篇通读 V1（卷一·本根敦伦）全部 827 篇文章。
全面评估其实质立论、问答核心以及与所在册/卷的契合度。
"""

import json
from pathlib import Path

with open('v1_full_reading_corpus.json', 'r', encoding='utf-8') as f:
    corpus = json.load(f)

# 按册聚合
by_booklet = {}
for item in corpus:
    bc = item['booklet_code']
    by_booklet.setdefault(bc, []).append(item)

print("V1 分册文章统计：")
for bc in sorted(by_booklet.keys()):
    print(f"  {bc}: {len(by_booklet[bc])} 篇")

