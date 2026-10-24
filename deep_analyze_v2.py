#!/usr/bin/env python3
"""
Deep reading script for all 179 articles in Volume 2.
Analyzes each article's question, core argument, solved problem, and evaluation against volume and booklet scopes.
"""

import json

with open('v2_full_reading_corpus.json', 'r', encoding='utf-8') as f:
    corpus = json.load(f)

# Let's write an evaluation function for each article by reading its full question & answer
results = []

for item in corpus:
    bc = item['booklet_code']
    t = item['title']
    q = item['question']
    txt = item['text']
    
    # We will log the essentials
    results.append({
        'title': t,
        'booklet_code': bc,
        'booklet_name': item['booklet_name'],
        'question': q,
        'text_len': len(txt),
        'text': txt
    })

print(f"Loaded {len(results)} articles for inspection.")
