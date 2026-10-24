#!/data/service/hnp/bin/python3
# -*- coding: utf-8 -*-
"""
提取高信号清单的完整正文（分批，避免单次过大）
用法：python3 05_extract_high_signal_content.py <start> <count>
示例：python3 05_extract_high_signal_content.py 1 100
"""

import json
import sys
from pathlib import Path
from subprocess import run

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
    if len(sys.argv) < 3:
        print("用法：python3 05_extract_high_signal_content.py <start> <count>")
        sys.exit(1)
    
    start = int(sys.argv[1])
    count = int(sys.argv[2])
    
    base = Path('/storage/Users/currentUser/Documents/岐伯论')
    high_signal_path = base / 'research-rebuild/data/high_signal_articles.jsonl'
    
    # 加载高信号清单
    print("加载高信号清单...")
    high_signal = load_jsonl(high_signal_path)
    
    # 切片
    batch = high_signal[start-1 : start-1+count]
    
    print(f"提取第{start}-{start+len(batch)-1}篇，共{len(batch)}篇\n")
    
    # 提取正文
    results = []
    for i, sig in enumerate(batch, start):
        article_id = sig['id']
        print(f"[{i}/{start+len(batch)-1}] {sig['full_citation']} ... ", end='', flush=True)
        
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
                'concept_hits': sig['concept_hits'],
                'planLevel': sig['planLevel'],
                'priority_score': sig['priority_score'],
                'answer': content.get('answer', ''),
                'narrative': content.get('narrative', ''),
            })
            print(f"✓ ({len(content.get('answer', ''))} 字)")
        else:
            print("✗ 提取失败")
    
    # 写出
    out_dir = base / 'research-rebuild/data/high_signal_content'
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f'batch_{start:04d}_{start+count-1:04d}.jsonl'
    
    with open(out_path, 'w', encoding='utf-8') as f:
        for rec in results:
            f.write(json.dumps(rec, ensure_ascii=False) + '\n')
    
    print(f"\n✓ 已写入 {out_path}")
    print(f"  成功提取：{len(results)}/{len(batch)} 篇")

if __name__ == '__main__':
    main()
