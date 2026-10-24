#!/usr/bin/env python3
"""
Examine every article in B11, B12, B13 by reading full question and answer.
Categorize each into:
- FIT_PERFECT: matches current booklet theme perfectly
- FIT_INTERNAL_MOVE: matches V2, but better in another booklet in V2 (e.g. B11 <-> B12 <-> B13)
- MISMATCH_EXTERNAL: belongs to another volume (V1, V3, V4, V5, V6, V7, V8)
"""

import json

with open('v2_full_reading_corpus.json', 'r', encoding='utf-8') as f:
    corpus = json.load(f)

# Let's write out text analysis for each booklet
with open('v2_audit_details.txt', 'w', encoding='utf-8') as out:
    for bc in ['B11', 'B12', 'B13']:
        items = [x for x in corpus if x['booklet_code'] == bc]
        out.write(f"\n{'='*70}\n")
        out.write(f"册代码: {bc} ({items[0]['booklet_name']}) - 共 {len(items)} 篇\n")
        out.write(f"{'='*70}\n")
        for idx, it in enumerate(items):
            out.write(f"\n[{bc} #{idx+1:02d}] 《{it['title']}》 ({len(it['text'])}字)\n")
            out.write(f"原问: {it['question']}\n")
            out.write(f"全文内容:\n{it['text']}\n")
            out.write(f"{'-'*70}\n")

print("Exported all full texts to v2_audit_details.txt")
