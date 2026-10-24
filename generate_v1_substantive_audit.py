#!/usr/bin/env python3
"""
岐伯论·卷一（本根敦伦——血亲宗族与家庭抚育）全量827篇逐篇通读分析程序
逐篇输出分析结果，生成结构化数据与审查报告。
"""
import json
import sys

with open('v1_full_reading_corpus.json', 'r', encoding='utf-8') as f:
    corpus = json.load(f)

# 按册组织
by_booklet = {}
for item in corpus:
    by_booklet.setdefault(item['booklet_code'], []).append(item)

print("Booklets summary:")
for bc, items in sorted(by_booklet.items()):
    print(f"{bc}: {len(items)} 篇")
