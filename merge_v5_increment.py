#!/usr/bin/env python3
"""合并v4语料库和最新7篇增量，生成v5语料库"""
import json
from pathlib import Path

PROJECT_ROOT = Path("/storage/Users/currentUser/Documents/岐伯论")
V4_CORPUS = PROJECT_ROOT / "sooon-q9adg-articles-v4.jsonl"
INCREMENT = PROJECT_ROOT / "research/online-increment/sooon-increment-20261010-202808.jsonl"
V5_CORPUS = PROJECT_ROOT / "sooon-q9adg-articles-v5.jsonl"

def main():
    corpus_by_id = {}
    v4_count = 0
    
    print(f"读取v4语料库：{V4_CORPUS}")
    with V4_CORPUS.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            item = json.loads(line)
            item_id = str(item["id"])
            corpus_by_id[item_id] = item
            v4_count += 1
            
    print(f"  已加载 {v4_count} 篇")
    
    print(f"读取增量文件：{INCREMENT}")
    new_count = 0
    updated_count = 0
    with INCREMENT.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            item = json.loads(line)
            item_id = str(item["id"])
            if item_id in corpus_by_id:
                if item["updatedAt"] > corpus_by_id[item_id]["updatedAt"]:
                    corpus_by_id[item_id] = item
                    updated_count += 1
            else:
                corpus_by_id[item_id] = item
                new_count += 1
                
    print(f"  新增 {new_count} 篇，更新 {updated_count} 篇")
    
    sorted_items = sorted(
        corpus_by_id.values(),
        key=lambda x: x["publishedAt"],
        reverse=True
    )
    
    print(f"写入v5语料库：{V5_CORPUS}")
    with V5_CORPUS.open("w", encoding="utf-8") as f:
        for item in sorted_items:
            f.write(json.dumps(item, ensure_ascii=False, separators=(',', ':')) + "\n")
            
    print(f"✓ 完成：v5语料库共 {len(sorted_items)} 篇")
    print(f"  v4: {v4_count} 篇")
    print(f"  新增: {new_count} 篇")
    print(f"  总计: {len(sorted_items)} 篇")

if __name__ == "__main__":
    main()
