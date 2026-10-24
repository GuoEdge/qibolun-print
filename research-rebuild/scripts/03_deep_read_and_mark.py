#!/data/service/hnp/bin/python3
# -*- coding: utf-8 -*-
"""
深度阅读批次文件，标记高价值篇章
输出：每篇的分析标记（引入概念、论证结构、方法论价值、理论位置）
"""

import json
import sys
from pathlib import Path

# 19个自创概念标签
CORE_CONCEPTS = [
    '人己权界', '自强', '神性享乐', '净输出', '信源管理',
    '择善固执', 'SOP', 'Poetic Irony', '旷野', '不以恶为业',
    '错得对', '元技能', '爱不生债', '评价权', 'CARITAS',
    '王天下', '内务班子', '人神分野', '成功税'
]

def analyze_article(rec):
    """
    分析单篇文章，返回标记结果
    标记维度：
    1. 是否引入/定义核心概念
    2. 论证结构完整性（有清晰命题+论证+结论）
    3. 方法论价值（可操作、可推广）
    4. 理论位置（基础命题 vs 应用延伸）
    """
    article_id = rec['id']
    title = rec['title']
    answer = rec['answer']
    keywords = rec.get('keywords', [])
    
    # 1. 检测核心概念
    concept_hits = []
    for concept in CORE_CONCEPTS:
        if concept in answer or any(kw.get('label') == concept for kw in keywords):
            concept_hits.append(concept)
    
    # 2. 论证结构评估（简单启发式：篇幅、段落结构）
    answer_len = len(answer)
    has_structure = answer_len > 800  # 至少800字才可能有完整论证
    
    # 3. 方法论价值（关键词启发式）
    method_keywords = ['怎么', '如何', '方法', '策略', '步骤', '原则', '标准', '判断', '选择']
    has_method = any(kw in answer for kw in method_keywords)
    
    # 4. 理论位置（基于planLevel和篇幅）
    plan_level = rec.get('planLevel')
    is_foundational = plan_level in [2, 3] and answer_len > 1000
    
    #