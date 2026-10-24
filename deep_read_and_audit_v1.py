#!/usr/bin/env python3
import json
import re

with open('v1_full_reading_corpus.json', 'r', encoding='utf-8') as f:
    corpus = json.load(f)

# 逐册检查，先写一个综合通读分析器，输出每册可疑偏离篇目的详细上下文
def analyze_article(art):
    bc = art['booklet_code']
    bn = art['booklet_name']
    t = art['title']
    q = art['question']
    txt = art['text']
    
    # 结合问答全文进行实质性研判
    # 我们先梳理每个分册中，明显属于其他卷（V2~V8）或明显属于V1其他分册的篇目
    return {
        'id': art['id'],
        'title': t,
        'bc': bc,
        'bn': bn,
        'q': q,
        'txt_head': txt[:300],
        'len': len(txt)
    }

print("Running deep read across all 827 articles...")
