#!/usr/bin/env python3
"""
卷七主题契合度全量人工审查
完整阅读每一篇文章，深度理解后判断主题契合度
不使用关键词匹配，纯人工判断
"""

import json
from pathlib import Path
from collections import defaultdict

BASE = Path('/storage/Users/currentUser/Documents/岐伯论')
CATALOG = BASE / 'research-rebuild/reports/gemini-flash-reclassification-v1/workbook-40b-all-catalog.jsonl'
CLEAN_DATA = BASE / 'research-rebuild/reports/gemini-flash-reclassification-v1/all-articles-merged-v4-clean.jsonl'

V7_THEMES = {
    'B31': {
        'name': '甲册·存在本質與生命意義',
        'theme': '存在本質與生命意義',
        'description': '探讨生命的意义、存在的本质、人生的价值与目的、终极关怀、死亡、虚无等哲学命题'
    },
    'B32': {
        'name': '乙册·名相辨析與語言牢籠',
        'theme': '名相辨析與語言牢籠',
        'description': '辨析概念、澄清定义、破除语言框架与思维陷阱、揭示词语背后的认知误区与标签化思维'
    },
    'B33': {
        'name': '丙册·善惡分野與倫理底線',
        'theme': '善惡分野與倫理底線',
        'description': '探讨善恶标准、道德底线、伦理原则、是非判断、价值观、良知与操守'
    },
    'B34': {
        'name': '丁册·認識局限與心智模型',
        'theme': '認識局限與心智模型',
        'description': '揭示认知盲区、思维局限、心智模式、视角偏差、信息盲区、知识边界'
    },
    'B35': {
        'name': '戊册·命途因果與得失隨緣',
        'theme': '命途因果與得失隨緣',
        'description': '探讨命运、因果关系、得失心态、随遇而安、接受现实、放下执念'
    },
    'B36': {
        'name': '己册·人性幽微與雙重人格',
        'theme': '人性幽微與雙重人格',
        'description': '揭示人性深层、阴暗面、双重标准、虚伪、表里不一、自欺、深层动机'
    },
    'B37': {
        'name': '庚册·神聖敬畏與信仰維度',
        'theme': '神聖敬畏與信仰維度',
        'description': '探讨信仰、宗教、神圣感、敬畏之心、超越性、灵性体验、终极关怀的宗教维度'
    },
    'B38': {
        'name': '辛册·自處之道與精神獨立',
        'theme': '自處之道與精神獨立',
        'description': '探讨独处之道、自我认知、精神独立、内在自足、心理边界、个体自主性'
    }
}

# 加载数据
print("加载语料数据...")
articles_by_id = {}
with open(CLEAN_DATA, 'r', encoding='utf-8') as f:
    for line in f:
        if not line.strip():
            continue
        data = json.loads(line)
        articles_by_id[data['id']] = data

print("加载编目数据...")
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

print("\n" + "=" * 120)
print("卷七全量深度审查 - 完整阅读每篇文章")
print("=" * 120)
print()

# 逐册审查
for code in ['B31', 'B32', 'B33', 'B34', 'B35', 'B36', 'B37', 'B38']:
    theme_info = V7_THEMES[code]
    articles = booklets[code]
    
    print(f"\n{'=' * 120}")
    print(f"{code} {theme_info['name']}")
    print(f"主题: {theme_info['theme']}")
    print(f"主题描述: {theme_info['description']}")
    print(f"文章总数: {len(articles)}篇")
    print('=' * 120)
    
    for i, rec in enumerate(articles, 1):
        original_id = rec['original_id']
        article_data = articles_by_id.get(original_id)
        if not article_data:
            continue
        
        title = rec['title']
        ordinal = rec['workbook_ordinal']
        question = article_data.get('question', '')
        answer = article_data.get('answer', '')
        text = answer if answer else article_data.get('text', '')
        
        print(f"\n【{i}/{len(articles)}】序号#{ordinal} 《{title}》")
        if question:
            print(f"提问: {question}")
        print(f"\n完整内容:")
        print(text)
        print(f"\n{'─' * 120}")
        
        # 每10篇暂停，等待判断
        if i % 10 == 0:
            print(f"\n[已审查{i}篇，继续...]")
