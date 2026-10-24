#!/usr/bin/env python3
"""
合并 sooon.ai 增量 JSONL 文件
按 id 去重，保留 updatedAt 最新的记录
"""
import json
import os
import sys
from pathlib import Path
from datetime import datetime
from collections import defaultdict

def merge_increments(input_dir):
    """合并增量文件"""
    input_path = Path(input_dir)
    if not input_path.exists():
        print(f"错误：找不到目录 {input_dir}")
        sys.exit(1)
    
    # 查找所有增量文件（排除已合并的）
    increment_files = sorted([
        f for f in input_path.glob("sooon-increment-*.jsonl")
        if "merged" not in f.name
    ])
    
    if not increment_files:
        print("没有找到待合并的增量文件")
        return
    
    print(f"找到 {len(increment_files)} 个增量文件：")
    for f in increment_files:
        print(f"  - {f.name}")
    
    # 按 id 去重，保留 updatedAt 最新的
    by_id = {}
    duplicates = 0
    bad_lines = []
    input_records = 0
    
    for file_path in increment_files:
        line_num = 0
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line_num += 1
                input_records += 1
                line = line.strip()
                if not line:
                    continue
                
                try:
                    record = json.loads(line)
                    rec_id = record['id']
                    
                    if rec_id in by_id:
                        duplicates += 1
                        # 保留 updatedAt 更新的
                        if record.get('updatedAt', 0) <= by_id[rec_id].get('updatedAt', 0):
                            continue
                    
                    by_id[rec_id] = record
                    
                except json.JSONDecodeError as e:
                    bad_lines.append({
                        'file': file_path.name,
                        'line': line_num,
                        'error': str(e)
                    })
                except KeyError as e:
                    bad_lines.append({
                        'file': file_path.name,
                        'line': line_num,
                        'error': f'缺少字段: {e}'
                    })
    
    # 统计信息
    required_fields = ['id', 'url', 'title', 'question', 'brief', 'text', 'publishedAt', 'updatedAt']
    missing_fields = []
    empty_text = []
    new_articles = 0
    updated_articles = 0
    total_chars = 0
    
    for rec_id, record in by_id.items():
        # 检查必需字段
        for field in required_fields:
            if field not in record:
                missing_fields.append({'id': rec_id, 'field': field})
        
        # 检查空文本
        text = record.get('text', '')
        if not text or not text.strip():
            empty_text.append({'id': rec_id, 'title': record.get('title', '')})
        
        total_chars += len(text)
        
        # 统计新增/更新
        change_kind = record.get('source', {}).get('changeKind', '')
        if change_kind == 'new':
            new_articles += 1
        elif change_kind == 'updated':
            updated_articles += 1
    
    # 按 publishedAt 降序排序输出
    sorted_records = sorted(
        by_id.values(),
        key=lambda x: x.get('publishedAt', 0),
        reverse=True
    )
    
    # 生成输出文件
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    output_path = input_path / f"sooon-increment-merged-{timestamp}.jsonl"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        for record in sorted_records:
            f.write(json.dumps(record, ensure_ascii=False, separators=(',', ':')) + '\n')
    
    # 生成统计文件
    stats = {
        'mergedAt': datetime.now().isoformat(),
        'inputFiles': [f.name for f in increment_files],
        'inputRecords': input_records,
        'records': len(by_id),
        'duplicates': duplicates,
        'newArticles': new_articles,
        'updatedArticles': updated_articles,
        'missingFields': len(missing_fields),
        'emptyText': len(empty_text),
        'badLines': len(bad_lines),
        'totalTextChars': total_chars,
        'outputPath': str(output_path),
        'status': 'PASS' if not missing_fields and not bad_lines else 'REVIEW'
    }
    
    stats_path = input_path / f"sooon-increment-merged-{timestamp}.stats.json"
    with open(stats_path, 'w', encoding='utf-8') as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)
    
    # 输出结果
    print(f"\n合并完成：")
    print(f"  输入文件：{len(increment_files)} 个")
    print(f"  输入记录：{input_records} 条")
    print(f"  输出记录：{len(by_id)} 条")
    print(f"  去重数量：{duplicates} 条")
    print(f"  新增文章：{new_articles} 篇")
    print(f"  更新文章：{updated_articles} 篇")
    print(f"  空文本：{len(empty_text)} 篇")
    print(f"  总字符数：{total_chars:,}")
    print(f"  输出文件：{output_path.name}")
    print(f"  状态：{stats['status']}")
    
    if bad_lines:
        print(f"\n警告：发现 {len(bad_lines)} 个损坏的行")
        for item in bad_lines[:5]:
            print(f"  {item['file']}:{item['line']} - {item['error']}")
    
    return output_path, stats

if __name__ == '__main__':
    input_dir = '/storage/Users/currentUser/Documents/岐伯论/research/online-increment'
    merge_increments(input_dir)
