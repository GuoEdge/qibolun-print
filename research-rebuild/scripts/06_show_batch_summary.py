#!/data/service/hnp/bin/python3
# -*- coding: utf-8 -*-
"""
展示指定范围的文章摘要，供深度阅读
用法：python3 06_show_batch_summary.py <batch_file> <start> <end>
"""

import json
import sys
from pathlib import Path

def main():
    if len(sys.argv) < 4:
        print("用法：python3 06_show_batch_summary.py <batch_file> <start> <end>")
        sys.exit(1)
    
    batch_file = Path(sys.argv[1])
    start = int(sys.argv[2])
    end = int(sys.argv[3])
    
    with open(batch_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for i in range(start-1, min(end, len(lines))):
        rec = json.loads(lines[i])
        print(f"### 第{i+1}篇：{rec['full_citation']}")
        print(f"标题：{rec['title']}")
        print(f"概念：{rec['concept_hits']}")
        print(f"篇幅：{len(rec['answer'])}字")
        print(f"planLevel：{rec['planLevel']}")
        print()
        # 显示前800字
        print(rec['answer'][:800])
        if len(rec['answer']) > 800:
            print(f"\n... (后续还有{len(rec['answer'])-800}字)")
        print()
        print("---")
        print()

if __name__ == '__main__':
    main()
