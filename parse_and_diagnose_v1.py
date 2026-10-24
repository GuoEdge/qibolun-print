#!/usr/bin/env python3
"""
逐册通读研判脚本：
对 B01、B05、B07、B10、B08、B09 进行首轮详尽实质性诊断
"""
import json

with open('v1_full_reading_corpus.json', 'r', encoding='utf-8') as f:
    corpus = json.load(f)

by_booklet = {}
for item in corpus:
    by_booklet.setdefault(item['booklet_code'], []).append(item)

# 让我们逐册审视非契合篇目
