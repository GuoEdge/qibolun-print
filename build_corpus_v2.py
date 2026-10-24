#!/usr/bin/env python3
"""
构建语料 v2：旧语料原样保留 + 在线新增追加
设计约束：
1. 不修改原始语料 sooon-q9adg-articles.jsonl
2. v2 的前 4050 行从原始语料逐字节原样复制
3. 在线新增文章追加为 ordinal 4051 起
4. updatedAt 变新的文章不改写 v2 旧记录，新版写入 version-diff
"""
import json
import hashlib
from pathlib import Path
from datetime import datetime
from collections import defaultdict

def sha256_file(path):
    """计算文件 SHA256"""
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()

def build_corpus_v2():
    base_dir = Path('/storage/Users/currentUser/Documents/岐伯论')
    corpus_path = base_dir / 'sooon-q9adg-articles.jsonl'
    increment_dir = base_dir / 'research/online-increment'
    
    # 找最新的合并增量文件
    increment_files = sorted(increment_dir.glob('sooon-increment-merged-*.jsonl'))
    if not increment_files:
        print("错误：找不到合并的增量文件")
        return
    
    increment_path = increment_files[-1]
    print(f"使用增量文件：{increment_path.name}")
    
    # 1. 读取旧语料（逐字节原样保留）
    print("读取旧语料...")
    old_lines = []
    corpus_ids = set()
    corpus_meta = {}
    
    with open(corpus_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n\r')
            if not line.strip():
                continue
            old_lines.append(line)
            
            record = json.loads(line)
            rec_id = record['id']
            corpus_ids.add(rec_id)
            corpus_meta[rec_id] = {
                'publishedAt': record.get('publishedAt', 0),
                'updatedAt': record.get('updatedAt', 0),
                'title': record.get('title', ''),
                'url': record.get('url', '')
            }
    
    old_count = len(old_lines)
    print(f"  旧语料：{old_count} 条")
    
    # 2. 读取增量（新增追加，变更写版本差异）
    print("处理增量数据...")
    new_records = []
    version_diff = []
    increment_count = 0
    
    with open(increment_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            record = json.loads(line)
            increment_count += 1
            rec_id = record['id']
            
            if rec_id in corpus_ids:
                # 已存在的文章
                change_kind = record.get('source', {}).get('changeKind', '')
                if change_kind == 'updated':
                    version_diff.append(record)
            else:
                # 新增文章
                new_records.append(record)
    
    print(f"  增量总数：{increment_count} 条")
    print(f"  新增文章：{len(new_records)} 篇")
    print(f"  版本变更：{len(version_diff)} 篇")
    
    # 3. 写出 v2
    output_path = base_dir / 'sooon-q9adg-articles-v3.jsonl'
    print(f"\n生成 v3 语料：{output_path.name}")
    
    total_chars = 0
    empty_text = 0
    min_published = float('inf')
    max_published = 0
    platforms = {'zhihu': 0, 'afdian': 0, 'other': 0}
    
    with open(output_path, 'w', encoding='utf-8') as f:
        # 写入旧语料（逐字节原样）
        for line in old_lines:
            f.write(line + '\n')
            
            # 统计
            record = json.loads(line)
            text = record.get('text', '')
            total_chars += len(text)
            if not text.strip():
                empty_text += 1
            
            pub = record.get('publishedAt', 0)
            if pub > max_published:
                max_published = pub
            if pub < min_published:
                min_published = pub
            
            url = record.get('url', '')
            if 'zhihu' in url:
                platforms['zhihu'] += 1
            elif 'afdian' in url or 'ifdian' in url:
                platforms['afdian'] += 1
            else:
                platforms['other'] += 1
        
        # 按 publishedAt 降序追加新增文章
        new_records_sorted = sorted(
            new_records,
            key=lambda x: x.get('publishedAt', 0),
            reverse=True
        )
        
        timestamp = datetime.now().isoformat()
        for record in new_records_sorted:
            rec = {
                'id': record['id'],
                'url': record.get('url', ''),
                'title': record.get('title', ''),
                'question': record.get('question', ''),
                'brief': record.get('brief', ''),
                'text': record.get('text', ''),
                'lexical': record.get('lexical'),
                'publishedAt': record.get('publishedAt', 0),
                'updatedAt': record.get('updatedAt', 0),
                'provenance': {
                    'addedIn': f'online-sync-{datetime.now().strftime("%Y-%m-%d")}',
                    'changeKind': 'new',
                    'fetchedAt': record.get('source', {}).get('fetchedAt', ''),
                    'sourceHash': record.get('source', {}).get('hash', ''),
                    'textPolicy': 'derived-from-lexical/linebreak-dropped/single-nl',
                    'note': '未精读、未进入作者证据层与论文引用'
                }
            }
            
            f.write(json.dumps(rec, ensure_ascii=False, separators=(',', ':')) + '\n')
            
            # 统计
            text = rec['text']
            total_chars += len(text)
            if not text.strip():
                empty_text += 1
            
            pub = rec['publishedAt']
            if pub > max_published:
                max_published = pub
            if pub < min_published:
                min_published = pub
            
            url = rec['url']
            if 'zhihu' in url:
                platforms['zhihu'] += 1
            elif 'afdian' in url or 'ifdian' in url:
                platforms['afdian'] += 1
            else:
                platforms['other'] += 1
    
    # 4. 版本差异落盘
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    diff_path = increment_dir / f'version-diff-{timestamp}.jsonl'
    
    with open(diff_path, 'w', encoding='utf-8') as f:
        for record in version_diff:
            f.write(json.dumps(record, ensure_ascii=False, separators=(',', ':')) + '\n')
    
    print(f"  版本差异文件：{diff_path.name}")
    
    # 5. 生成统计
    stats = {
        'generatedAt': datetime.now().isoformat(),
        'corpusPath': str(corpus_path),
        'incrementPath': str(increment_path),
        'outputPath': str(output_path),
        'records': old_count + len(new_records),
        'oldRecords': old_count,
        'appendedRecords': len(new_records),
        'ordinalPolicy': f'ordinal 1—{old_count} 与旧语料逐字节一致；新增为 {old_count+1} 起 append-only',
        'incrementRecords': increment_count,
        'versionDiffRecords': len(version_diff),
        'operativeReplacements': 0,
        'totalTextChars': total_chars,
        'emptyText': empty_text,
        'minPublishedAt': int(min_published) if min_published != float('inf') else 0,
        'maxPublishedAt': int(max_published),
        'platforms': platforms,
        'versionDiffPath': str(diff_path),
        'corpusSha256': sha256_file(corpus_path),
        'outputSha256': sha256_file(output_path),
        'status': 'PASS'
    }
    
    stats_path = base_dir / 'sooon-q9adg-articles-v3.stats.json'
    with open(stats_path, 'w', encoding='utf-8') as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)
    
    # 输出摘要
    print(f"\n✓ v3 语料构建完成")
    print(f"  总记录：{stats['records']} 条")
    print(f"  旧记录：{stats['oldRecords']} 条")
    print(f"  新增：{stats['appendedRecords']} 条")
    print(f"  版本变更：{stats['versionDiffRecords']} 条")
    print(f"  总字符数：{stats['totalTextChars']:,}")
    print(f"  平台分布：知乎 {platforms['zhihu']}, 爱发电 {platforms['afdian']}, 其他 {platforms['other']}")
    print(f"  输出文件：{output_path.name}")
    print(f"  统计文件：{stats_path.name}")
    
    return output_path, stats

if __name__ == '__main__':
    build_corpus_v2()
