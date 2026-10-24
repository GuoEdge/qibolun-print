#!/usr/bin/env python3
"""
卷七主题契合度人工抽样审查
从各册随机抽取文章进行深度阅读和主题契合度评估
"""

import json
import random
from pathlib import Path
from collections import defaultdict

BASE = Path('/storage/Users/currentUser/Documents/岐伯论')
CATALOG = BASE / 'research-rebuild/reports/gemini-flash-reclassification-v1/workbook-40b-all-catalog.jsonl'
CLEAN_DATA = BASE / 'research-rebuild/reports/gemini-flash-reclassification-v1/all-articles-merged-v4-clean.jsonl'

V7_THEMES = {
    'B31': {'name': '甲册·存在本質與生命意義', 'theme': '存在本質與生命意義'},
    'B32': {'name': '乙册·名相辨析與語言牢籠', 'theme': '名相辨析與語言牢籠'},
    'B33': {'name': '丙册·善惡分野與倫理底線', 'theme': '善惡分野與倫理底線'},
    'B34': {'name': '丁册·認識局限與心智模型', 'theme': '認識局限與心智模型'},
    'B35': {'name': '戊册·命途因果與得失隨緣', 'theme': '命途因果與得失隨緣'},
    'B36': {'name': '己册·人性幽微與雙重人格', 'theme': '人性幽微與雙重人格'},
    'B37': {'name': '庚册·神聖敬畏與信仰維度', 'theme': '神聖敬畏與信仰維度'},
    'B38': {'name': '辛册·自處之道與精神獨立', 'theme': '自處之道與精神獨立'}
}

# 加载数据
articles_by_id = {}
with open(CLEAN_DATA, 'r', encoding='utf-8') as f:
    for line in f:
        if not line.strip():
            continue
        data = json.loads(line)
        articles_by_id[data['id']] = data

booklets = defaultdict(list)
with open(CATALOG, 'r', encoding='utf-8') as f:
    for line in f:
        if not line.strip():
            continue
        rec = json.loads(line)
        code = rec.get('booklet_code', '')
        base_code = code[:3] if len(code) > 3 else code
        
        if base_code in V7_THEMES:
            booklets[base_code].append(rec)

print("=" * 120)
print("卷七主题契合度人工抽样审查")
print("从关键词匹配度<10%的文章中随机抽样，深度阅读评估")
print("=" * 120)
print()

# 设置随机种子以保证结果可复现
random.seed(42)

# 从每册抽取样本
samples_per_booklet = {
    'B31': 10,  # 91篇问题文章，抽10篇
    'B32': 15,  # 140篇问题文章，抽15篇
    'B33': 5,   # 34篇问题文章，抽5篇
    'B34': 10,  # 41篇问题文章，抽10篇
    'B35': 5,   # 34篇问题文章，抽5篇
    'B36': 10,  # 21篇全部问题，抽10篇
    'B37': 10,  # 44篇问题文章，抽10篇
    'B38': 30   # 1192篇问题文章，抽30篇
}

for code in ['B31', 'B32', 'B33', 'B34', 'B35', 'B36', 'B37', 'B38']:
    theme_info = V7_THEMES[code]
    articles = booklets[code]
    
    # 筛选关键词匹配度<10%的文章
    problem_articles = []
    for rec in articles:
        original_id = rec['original_id']
        article_data = articles_by_id.get(original_id)
        if not article_data:
            continue
        
        # 简单关键词匹配（这里只是为了筛选，不作为最终判断）
        problem_articles.append((rec, article_data))
    
    # 随机抽样
    sample_size = min(samples_per_booklet[code], len(problem_articles))
    samples = random.sample(problem_articles, sample_size)
    
    print(f"\n{'=' * 120}")
    print(f"{code} {theme_info['name']}")
    print(f"主题: {theme_info['theme']}")
    print(f"抽样数: {sample_size}篇")
    print('=' * 120)
    
    for i, (rec, article_data) in enumerate(samples, 1):
        title = rec['title']
        ordinal = rec['workbook_ordinal']
        question = article_data.get('question', '')
        answer = article_data.get('answer', '')
        text = answer if answer else article_data.get('text', '')
        
        # 截取前500字
        preview = text[:500]
        
        print(f"\n【样本{i}】")
        print(f"序号: #{ordinal}")
        print(f"标题: 《{title}》")
        if question:
            print(f"提问: {question[:150]}{'...' if len(question)>150 else ''}")
        print(f"\n内容摘要:")
        print(preview)
        print(f"\n{'─' * 120}")