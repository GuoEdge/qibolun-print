#!/usr/bin/env python3
"""
拆分B31（267篇）为上下2册
- B31 → B31A（上册）、B31B（下册）
- 每册约134篇
"""
import json
import sys

CATALOG = 'workbook-40b-all-catalog.jsonl'
OUTPUT = 'workbook-40b-all-catalog.jsonl'
BACKUP_SUFFIX = '.bak-before-b31-split'

def main():
    # 备份
    import shutil
    shutil.copy(CATALOG, CATALOG + BACKUP_SUFFIX)
    print(f"已备份: {CATALOG + BACKUP_SUFFIX}")
    
    # 读取所有记录
    records = []
    with open(CATALOG, 'r', encoding='utf-8') as f:
        for line in f:
            records.append(json.loads(line))
    
    # 找出B31的所有记录
    b31_records = [r for r in records if r.get('booklet_code') == 'B31']
    other_records = [r for r in records if r.get('booklet_code') != 'B31']
    
    print(f"B31原始篇数: {len(b31_records)}")
    
    if len(b31_records) != 267:
        print(f"WARNING: 预期267篇，实际{len(b31_records)}篇")
    
    # 拆分为2册，每册134篇（下册133篇）
    per_booklet = 134
    splits = {
        'A': ('上', b31_records[0:134]),
        'B': ('下', b31_records[134:267])
    }
    
    print(f"\n拆分方案:")
    for suffix, (name, articles) in splits.items():
        print(f"  B31{suffix}（{name}册）: {len(articles)}篇")
    
    # 更新记录
    new_b31_records = []
    for suffix, (name_suffix, articles) in splits.items():
        new_code = f'B31{suffix}'
        for rec in articles:
            # 更新字段
            rec['booklet_code'] = new_code
            # booklet_name: "XXX·上册"
            base_name = rec['booklet_name'].split('·')[0] if '·' in rec['booklet_name'] else rec['booklet_name']
            rec['booklet_name'] = f"{base_name}·{name_suffix}册"
            # booklet_stem: "原stem·上"
            base_stem = rec['booklet_stem']
            rec['booklet_stem'] = f"{base_stem}·{name_suffix}"
            # full_citation: 保持原有格式
            if '·' in rec.get('full_citation', ''):
                parts = rec['full_citation'].split('·')
                parts[-1] = f"{base_name}·{name_suffix}册"
                rec['full_citation'] = '·'.join(parts)
            else:
                rec['full_citation'] = f"{rec.get('volume_prefix', rec.get('volume_code', ''))} · {rec['booklet_stem']} {base_name}·{name_suffix}册"
            new_b31_records.append(rec)
    
    # 合并所有记录
    all_records = other_records + new_b31_records
    
    # 按原始顺序排序
    all_records.sort(key=lambda x: x.get('article_id', ''))
    
    # 写回
    with open(OUTPUT, 'w', encoding='utf-8') as f:
        for rec in all_records:
            f.write(json.dumps(rec, ensure_ascii=False) + '\n')
    
    print(f"\n已更新: {OUTPUT}")
    print(f"总记录数: {len(all_records)}")
    
    # 验证
    print("\n验证拆分结果:")
    with open(OUTPUT, 'r', encoding='utf-8') as f:
        verify_records = [json.loads(line) for line in f]
    
    for suffix in ['A', 'B']:
        code = f'B31{suffix}'
        count = sum(1 for r in verify_records if r.get('booklet_code') == code)
        print(f"  {code}: {count}篇")
    
    print("\n✓ B31拆分完成")

if __name__ == '__main__':
    main()
