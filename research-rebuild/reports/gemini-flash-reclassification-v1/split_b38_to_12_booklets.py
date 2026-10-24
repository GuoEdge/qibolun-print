#!/usr/bin/env python3
"""
B38大册拆分脚本
将B38（自處之道與精神獨立，1213篇）拆分为12个地支子册
"""
import json
import shutil
from pathlib import Path

# 配置
CATALOG_PATH = Path('/storage/Users/currentUser/Documents/岐伯论/research-rebuild/reports/gemini-flash-reclassification-v1/workbook-40b-all-catalog.jsonl')
BACKUP_SUFFIX = '.bak-before-b38-split'

# 地支映射
DIZHI_MAP = {
    'A': '子', 'B': '丑', 'C': '寅', 'D': '卯',
    'E': '辰', 'F': '巳', 'G': '午', 'H': '未',
    'I': '申', 'J': '酉', 'K': '戌', 'L': '亥'
}

def split_b38():
    """执行B38拆分"""
    
    # 1. 备份原文件
    backup_path = Path(str(CATALOG_PATH) + BACKUP_SUFFIX)
    if not backup_path.exists():
        shutil.copy2(CATALOG_PATH, backup_path)
        print(f"✓ 已备份: {backup_path.name}")
    
    # 2. 读取所有记录
    all_records = []
    b38_records = []
    
    with open(CATALOG_PATH, 'r', encoding='utf-8') as f:
        for line in f:
            obj = json.loads(line)
            if obj.get('booklet_code') == 'B38':
                b38_records.append(obj)
            else:
                all_records.append(obj)
    
    print(f"\n原B38篇数: {len(b38_records)}")
    
    # 3. 拆分为12册
    num_booklets = 12
    per_booklet = 102  # 每册102篇，最后一册91篇
    
    updated_count = 0
    for i in range(num_booklets):
        start_idx = i * per_booklet
        end_idx = min((i + 1) * per_booklet, len(b38_records))
        
        sub_code = chr(ord('A') + i)  # A, B, C...
        dizhi = DIZHI_MAP[sub_code]
        new_booklet_code = f'B38{sub_code}'
        new_booklet_name = f'自處之道與精神獨立·{dizhi}册'
        
        count = 0
        for idx in range(start_idx, end_idx):
            record = b38_records[idx]
            
            # 更新字段
            record['booklet_code'] = new_booklet_code
            record['booklet_name'] = new_booklet_name
            record['booklet_stem'] = f'辛·{dizhi}'
            record['full_citation'] = f"《岐伯論·卷七·辛·{dizhi}·{record['title']}》"
            
            all_records.append(record)
            count += 1
            updated_count += 1
        
        print(f"  {new_booklet_code} ({dizhi}册): {count}篇")
    
    # 4. 写回文件
    with open(CATALOG_PATH, 'w', encoding='utf-8') as f:
        for record in all_records:
            f.write(json.dumps(record, ensure_ascii=False) + '\n')
    
    print(f"\n✓ 拆分完成，共更新 {updated_count} 条记录")
    print(f"✓ 已写入: {CATALOG_PATH}")
    
    # 5. 验证
    verify_count = {}
    with open(CATALOG_PATH, 'r', encoding='utf-8') as f:
        for line in f:
            obj = json.loads(line)
            code = obj.get('booklet_code', '')
            if code.startswith('B38'):
                verify_count[code] = verify_count.get(code, 0) + 1
    
    print("\n验证结果:")
    for code in sorted(verify_count.keys()):
        dizhi = DIZHI_MAP.get(code[-1], code[-1])
        print(f"  {code} ({dizhi}册): {verify_count[code]}篇")

if __name__ == '__main__':
    split_b38()
