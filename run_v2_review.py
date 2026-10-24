#!/usr/bin/env python3
"""
Comprehensive substantive review of each article in Volume 2.
Evaluates content substance, core conflict, and theme alignment.
"""

import json

with open('v2_full_reading_corpus.json', 'r', encoding='utf-8') as f:
    corpus = json.load(f)

# Let's inspect articles booklet by booklet
b11_items = [x for x in corpus if x['booklet_code'] == 'B11']
b12_items = [x for x in corpus if x['booklet_code'] == 'B12']
b13_items = [x for x in corpus if x['booklet_code'] == 'B13']

print(f"B11 count: {len(b11_items)}")
print(f"B12 count: {len(b12_items)}")
print(f"B13 count: {len(b13_items)}")
