#!/usr/bin/env python3
"""合并v3语料库和最新增量，生成v4语料库"""
import json
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path(__file__).parent
V3_CORPUS = PROJECT_ROOT / "sooon-q9adg-articles-v3.jsonl"
INCREMENT = PROJECT_ROOT / "research/online-increment/sooon-increment-20261009-195354.jsonl"
V4_CORPUS = PROJECT_ROOT / "sooon-q9adg-articles-v4.jsonl"

def main():
    # 加载v3语料库
    corpus_by_id = {}
    v3_count = 0
    
    print(f"读取v3语料库：{V3_CORPUS}")
    with V3_CORPUS.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            item = json.loads(line)
            item_id = str(item["id"])
            corpus_by_id[item_id] = item
            v3_count += 1
    
    print(f"  已加载 {v3_count} 篇")
    
    # 合并增量
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
                # 更新已有文章（保留较新的updatedAt）
                if item["updatedAt"] > corpus_by_id[item_id]["updatedAt"]:
                    corpus_by_id[item_id] = item
                    updated_count += 1
            else:
                # 新文章
                corpus_by_id[item_id] = item
                new_count += 1
    
    print(f"  新增 {new_count} 篇，更新 {updated_count} 篇")
    
    # 按publishedAt降序排序
    sorted_items = sorted(
        corpus_by_id.values(),
        key=lambda x: x["publishedAt"],
        reverse=True
    )
    
    # 写入v4语料库
    print(f"写入v4语料库：{V4_CORPUS}")
    with V4_CORPUS.open("w", encoding="utf-8") as f:
        for item in sorted_items:
            f.write(json.dumps(item, ensure_ascii=False, separators=(',', ':')) + "\n")
    
    print(f"✓ 完成：v4语料库共 {len(sorted_items)} 篇")
    print(f"  v3: {v3_count} 篇")
    print(f"  新增: {new_count} 篇")
    print(f"  更新: {updated_count} 篇")
    print(f"  总计: {len(sorted_items)} 篇")

if __name__ == "__main__":
    main()
