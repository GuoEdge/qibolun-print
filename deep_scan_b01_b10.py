#!/usr/bin/env python3
import json

with open('v1_full_reading_corpus.json', 'r', encoding='utf-8') as f:
    corpus = json.load(f)

by_booklet = {}
for item in corpus:
    by_booklet.setdefault(item['booklet_code'], []).append(item)

# 打印各册所有文章的 title, id, question[:60], text[:120]
# 重点审读：
# 1. B01 全部 52 篇
# 2. B05 全部 15 篇
# 3. B07 全部 12 篇
# 4. B10 全部 27 篇
# 5. B08 全部 60 篇
# 6. B09 全部 49 篇
# 7. B04 全部 79 篇
# 8. B03 全部 98 篇
# 9. B06 全部 136 篇
# 10. B02 全部 299 篇

with open('all_v1_articles_detailed.txt', 'w', encoding='utf-8') as out:
    for bc in ['B01', 'B05', 'B07', 'B10', 'B08', 'B09', 'B04', 'B03', 'B06', 'B02']:
        items = by_booklet.get(bc, [])
        out.write(f"\n==================== {bc} ({items[0]['booklet_name'] if items else ''}) 共 {len(items)} 篇 ====================\n")
        for idx, art in enumerate(items, 1):
            q = art['question'].replace('\n', ' ')
            txt = art['text'].replace('\n', ' ')
            out.write(f"[{idx:3d}] 【{art['title']}】 (ID: {art['id'][:8]})\n")
            out.write(f"     原问: {q[:120]}\n")
            out.write(f"     正文: {txt[:200]}\n")

print("Generated all_v1_articles_detailed.txt")
