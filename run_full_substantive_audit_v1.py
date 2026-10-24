#!/usr/bin/env python3
"""
岐伯论·卷一（本根敦伦——血亲宗族与家庭抚育）全量827篇逐篇实质性通读审查与诊断
"""

import json
import re

with open('v1_full_reading_corpus.json', 'r', encoding='utf-8') as f:
    corpus = json.load(f)

# 各册文章分类字典
by_booklet = {}
for item in corpus:
    by_booklet.setdefault(item['booklet_code'], []).append(item)

# 打印各册检查进度与细查
print("Beginning detailed review of all booklets in V1...")
