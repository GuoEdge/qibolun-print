#!/usr/bin/env python3
"""
生成卷一全量调整映射表
包括：
1. 206 篇跨卷错置文章移出到 V2~V8 契合分册
2. 69 篇卷内分册错置文章在 B01~B10 之间精准归位
"""

import json
from pathlib import Path

with open('v1_full_reading_corpus.json', 'r', encoding='utf-8') as f:
    corpus = json.load(f)

# 建立文章 ID 索引与标题索引
corpus_map = {c['id']: c for c in corpus}
title_map = {c['title']: c for c in corpus}

print(f"Total articles in corpus: {len(corpus)}")
