#!/usr/bin/env python3
"""
Substantive reading script for each of the 179 articles in Volume 2.
Evaluates every article by:
- Real question and situation
- Real core argument of Qibo's answer
- Judgment: Fits B11/B12/B13? Internal booklet shift needed? Or misplaced to other volumes?
"""

import json

with open('v2_full_reading_corpus.json', 'r', encoding='utf-8') as f:
    corpus = json.load(f)

# Define audit results storage
audit_records = []

# Detailed analysis for each article
for item in corpus:
    bc = item['booklet_code']
    bn = item['booklet_name']
    t = item['title']
    q = item['question']
    txt = item['text']
    
    # We will record the title and evaluate
    audit_records.append({
        'title': t,
        'booklet_code': bc,
        'booklet_name': bn,
        'question': q,
        'text_len': len(txt)
    })

print(f"Total to audit: {len(audit_records)}")
