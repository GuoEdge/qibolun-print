#!/usr/bin/env python3
"""
修复catalog中丢失的URL字段
从原始数据（sooon-q9adg-articles-v2.jsonl）恢复URL映射
"""
import json
import shutil
from pathlib import Path

# 路径配置
BASE = Path('/storage/Users/currentUser/Documents/岐伯论')
SOURCE_FILE = BASE / 'sooon-q9adg-articles-v2.jsonl'
CATALOG_FILE = Path('workbook-40b-all-catalog.jsonl')
BACKUP_SUFFIX = '.bak-before-url-fix'

def load_url_mapping(source_file):
    """从原始数据加载URL映射"""
    url_map = {}
    with open(source_file, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                item = json.loads(line)
                article_id = item.get('id')
                url = item.get('url')
                if article_id and url:
                    url_map[article_id] = url
            except Exception as e:
                print(f"解析原始数据失败: {e}")
    return url_map

def fix_catalog_urls(catalog_file, url_map, backup_suffix):
    """修复catalog的URL字段"""
    # 备份原文件
    backup_file = str(catalog_file) + backup_suffix
    shutil.copy2(catalog_file, backup_file)
    print(f"✓ 已备份原文件: {backup_file}")
    
    # 统计
    total = 0
    fixed = 0
    not_found = 0
    
    # 读取并修复
    fixed_lines = []
    with open(catalog_file, 'r', encoding='utf-8') as f:
        for line in f:
            item = json.loads(line)
            total += 1
            
            original_id = item.get('original_id')
            if original_id and original_id in url_map:
                item['url'] = url_map[original_id]
                fixed += 1
            else:
                not_found += 1
            
            fixed_lines.append(json.dumps(item, ensure_ascii=False))
    
    # 写回文件
    with open(catalog_file, 'w', encoding='utf-8') as f:
        for line in fixed_lines:
            f.write(line + '\n')
    
    return total, fixed, not_found

def main():
    print("=" * 60)
    print("修复catalog URL字段")
    print("=" * 60)
    
    # 加载URL映射
    print(f"\n[1/3] 从原始数据加载URL映射...")
    url_map = load_url_mapping(SOURCE_FILE)
    print(f"✓ 加载了 {len(url_map)} 个URL映射")
    
    # 修复catalog
    print(f"\n[2/3] 修复catalog...")
    total, fixed, not_found = fix_catalog_urls(CATALOG_FILE, url_map, BACKUP_SUFFIX)
    
    # 输出报告
    print(f"\n[3/3] 修复完成")
    print("=" * 60)
    print(f"总计文章: {total}篇")
    print(f"成功修复: {fixed}篇 ({fixed/total*100:.1f}%)")
    print(f"未找到URL: {not_found}篇 ({not_found/total*100:.1f}%)")
    print("=" * 60)
    
    if not_found > 0:
        print(f"\n⚠ 警告: {not_found}篇文章的URL无法从原始数据匹配")
        print("这些文章的二维码将使用后备方案生成")

if __name__ == '__main__':
    main()
