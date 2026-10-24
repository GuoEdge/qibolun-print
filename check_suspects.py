#!/usr/bin/env python3
"""
Inspect all 179 articles in Volume 2.
Read the full text of suspicious articles and summarize their core essence.
"""

import json

with open('v2_full_reading_corpus.json', 'r', encoding='utf-8') as f:
    corpus = json.load(f)

print(f"Total articles: {len(corpus)}")

# Let's inspect articles by booklet and print detailed information
def examine_article(art):
    t = art['title']
    bc = art['booklet_code']
    bn = art['booklet_name']
    q = art['question']
    txt = art['text']
    length = len(txt)
    return {
        'title': t,
        'bc': bc,
        'bn': bn,
        'question': q,
        'text_len': length,
        'preview': txt[:300].replace('\n', ' ')
    }

# Let's write a script to check suspicious articles' full text
suspect_titles = [
    '勉强', '进化心理学', '歧视的自由', '射鸟', '不可论断人', 'ToTheEnd',
    '早恋1', '绝对安全', '三鞠躬', '公开换安全',
    '车道问题', '雷峰夕照', '幼稚女生', '富贵囚人',
    '无罪可言', '尘心说', 'The Game of Mole', '情绪失控的孩子', '不屈节',
    '天河', '别互补', '性', '新手村之王', '经纪人', '大前门'
]

for item in corpus:
    if item['title'] in suspect_titles:
        print(f"\n==========================================")
        print(f"【{item['booklet_code']}】《{item['title']}》 (长度: {len(item['text'])}字)")
        print(f"提问: {item['question']}")
        print(f"--- 正文开头 ---")
        print(item['text'][:600])
        print(f"--- 正文结尾 ---")
        print(item['text'][-400:] if len(item['text']) > 400 else "")
