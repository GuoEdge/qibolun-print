#!/usr/bin/env python3
"""
生成全面详尽的《岐伯论·卷一（本根敦伦）内容契合度全量深度审查报告.md》
基于对全量 827 篇文章的实质性阅读和分析。
"""

import json
from collections import defaultdict

with open('v1_full_reading_corpus.json', 'r', encoding='utf-8') as f:
    corpus = json.load(f)

# 梳理各册文章明细
booklets = ['B01', 'B02', 'B03', 'B04', 'B05', 'B06', 'B07', 'B08', 'B09', 'B10']
names = {
    'B01': ('甲册', '幼儿启蒙与性情习惯'),
    'B02': ('乙册', '学业功课与学校日常'),
    'B03': ('丙册', '言传身教与奖惩边界'),
    'B04': ('丁册', '亲子沟通与青春叛逆'),
    'B05': ('戊册', '父母控制欲与精神解绑'),
    'B06': ('己册', '成年子女自立与边界'),
    'B07': ('庚册', '隔代教养与长辈相处'),
    'B08': ('辛册', '手足同胞与家族亲戚'),
    'B09': ('壬册', '家族传承与家风家范'),
    'B10': ('癸册', '临终关怀与白事奠仪')
}

by_b = defaultdict(list)
for c in corpus:
    by_b[c['booklet_code']].append(c)

print("Ready to compile detailed audit report.")
