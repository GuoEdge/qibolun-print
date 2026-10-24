#!/usr/bin/env python3
"""
Systematic inspection of all 179 articles in Volume 2.
We will inspect titles, questions, length, and core topic for each article.
"""

import json

with open('v2_full_reading_corpus.json', 'r', encoding='utf-8') as f:
    corpus = json.load(f)

for bc in ['B11', 'B12', 'B13']:
    sub = [x for x in corpus if x['booklet_code'] == bc]
    print(f"\n=======================================================")
    print(f"       BOOKLET {bc} ({sub[0]['booklet_name']}) - {len(sub)} 篇")
    print(f"=======================================================")
    for idx, item in enumerate(sub):
        t = item['title']
        q = item['question'].strip()
        txt = item['text']
        first_200 = txt[:200].replace('\n', ' ')
        last_100 = txt[-100:].replace('\n', ' ') if len(txt) > 100 else ''
        print(f"[{bc} #{idx+1:02d}] 《{t}》 ({len(txt)}字)")
        print(f"  问: {q}")
        print(f"  前: {first_200}")
        print(f"  后: {last_100}")
        print("-" * 50)
