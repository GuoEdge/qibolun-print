#!/usr/bin/env python3
"""
逐篇通读分析卷一全部827篇，输出结构化的判断结果并统计各册契合度。
"""

import json
from pathlib import Path

with open('v1_full_reading_corpus.json', 'r', encoding='utf-8') as f:
    corpus = json.load(f)

print(f"Total corpus: {len(corpus)}")
