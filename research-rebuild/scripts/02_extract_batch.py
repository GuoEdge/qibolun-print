#!/data/service/hnp/bin/python3
# -*- coding: utf-8 -*-
"""
分批提取正文，供深度阅读
用法：python3 02_extract_batch.py <volume_code> <start_ordinal> <count>
示例：python3 02_extract_batch.py V1 1 50
"""

import json
import sys
from pathlib import Path
from subprocess import run, PIPE

def load_jsonl(path):
    records = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records

def extract_content_via_node(article_id, base_path):
    """调用extract_qibo_content.js提取正文"""
    js_path = base_path / 'research-rebuild/reports/gemini-flash-reclassification-v1/extract_qibo_content.js'
    articles_path = base_path / 'sooon-q9adg-articles-v6.jsonl'
    
    # 构造node命令：读取指定id的文章，调用resolveContent
    cmd = [
        'node', '-e',
        f"""
const {{resolveContent}} = require('{js_path}');
const fs = require('fs');
const lines = fs.readFileSync('{articles_path}', 'utf-8').split('\\n');
for (const line of lines) {{
  if (!line.trim()) continue;
  const rec = JSON.parse(line);
  if (rec.id === '{article_id}') {{
    const result = resolveContent(rec);
    console.log(JSON.stringify(result));
    process.exit(0);
  }}
}}
process.exit(1);
"""
    ]
    
    result = run(cmd, capture_output=True, text=True, cwd=base_path)
    if result.returncode != 0:
        return None
    
    return json.loads(result.stdout.strip())

def main():
    if len(sys.argv) < 4:
        print("用法：python3 02_extract_batch.py <volume_code> <start_ordinal> <count>")
        sys.exit(1)
    
    volume_code = sys.argv[1]
    start_ordinal = int(sys.argv[2])
    count = int(sys.argv[3])
    
    base = Path('/storage/Users/currentUser/Documents/岐伯论')
    signals_path = base / 'research-rebuild/data/all_articles_signals.jsonl'
    
    # 加载信号表
    signals = load_jsonl(signals_path)
    
    # 筛选指定卷+序号范围
    batch = [
        s for s in signals
        if s['volume_code'] == volume_code
        and start_ordinal <= s['workbook_ordinal'] < start_ordinal + count
    ]
    
    batch.sort(key=lambda x: x['workbook_ordinal'])
    
    print(f"提取 {volume_code} 第{start_ordinal}-{start_ordinal+count-1}篇，共{len(batch)}篇\n")
    
    # 提取正文
    results = []
    for i, sig in enumerate(batch, 1):
        article_id = sig['id']
        print(f"[{i}/{len(batch)}] {sig['full_citation']} ... ", end='', flush=True)
        
        content = extract_content_via_node(article_id, base)
        if content:
            results.append({
                'id': article_id,
                'workbook_ordinal': sig['workbook_ordinal'],
                'full_citation': sig['full_citation'],
                'title': sig['title'],
                'volume_code': sig['volume_code'],
                'booklet_name': sig['booklet_name'],
                'keywords': sig['keywords'],
                'planLevel': sig['planLevel'],
                'answer': content.get('answer', ''),
                'narrative': content.get('narrative', ''),
            })
            print(f"✓ ({len(content.get('answer', ''))} 字)")
        else:
            print("✗ 提取失败")
    
    # 写出
    out_dir = base / 'research-rebuild/data/batches'
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f'batch_{volume_code}_{start_ordinal:04d}_{start_ordinal+count-1:04d}.jsonl'
    
    with open(out_path, 'w', encoding='utf-8') as f:
        for rec in results:
            f.write(json.dumps(rec, ensure_ascii=False) + '\n')
    
    print(f"\n✓ 已写入 {out_path}")
    print(f"  成功提取：{len(results)}/{len(batch)} 篇")

if __name__ == '__main__':
    main()
