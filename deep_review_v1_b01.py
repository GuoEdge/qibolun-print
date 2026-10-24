#!/usr/bin/env python3
"""
深入通读 B01 (甲册·幼儿启蒙与性情习惯，共52篇)
逐篇输出标题、问题核心、正文核心逻辑、判定结果与诊断原因。
"""
import json

with open('v1_full_reading_corpus.json', 'r', encoding='utf-8') as f:
    corpus = json.load(f)

b01 = [c for c in corpus if c['booklet_code'] == 'B01']

print(f"=== B01 共 {len(b01)} 篇 ===")
for i, c in enumerate(b01, 1):
    q = c['question'].replace('\n', ' ')
    txt = c['text'].replace('\n', ' ')
    print(f"\n【{i}. {c['title']}】 (ID: {c['id'][:8]})")
    print(f"问: {q[:120]}")
    print(f"文: {txt[:200]}")

