#!/usr/bin/env python3
"""审核所有DOCX文档，确保文章内容与所在分册一致"""

import zipfile
import re
import json
from pathlib import Path
from collections import defaultdict

BASE = Path('/storage/Users/currentUser/Documents/岐伯论')
CATALOG = BASE / 'research-rebuild/reports/gemini-flash-reclassification-v1/workbook-40b-all-catalog.jsonl'

# 加载编目数据
catalog = {}
booklet_articles = defaultdict(list)  # booklet_code -> [ordinals]

with open(CATALOG, 'r', encoding='utf-8') as f:
    for line in f:
        rec = json.loads(line)
        ordinal = rec['workbook_ordinal']
        code = rec['booklet_code']
        catalog[ordinal] = rec
        booklet_articles[code].append(ordinal)

print(f"编目总数: {len(catalog)}")
print(f"分册数: {len(booklet_articles)}")

# 扫描所有DOCX文件
docx_files = []
for vol_dir in ['卷四', '卷五', '卷六', '卷七', '卷八']:
    vol_path = BASE / vol_dir
    if vol_path.exists():
        docx_files.extend(vol_path.rglob('岐伯论·*.docx'))

print(f"\n找到 {len(docx_files)} 个DOCX文件")

# 审核每个文件
issues = []
for docx_path in sorted(docx_files):
    rel_path = docx_path.relative_to(BASE)
    
    # 从文件名提取分册信息
    # 格式: 岐伯论·卷X·Y·name·suffix.docx
    name = docx_path.stem
    parts = name.split('·')
    if len(parts) < 4:
        issues.append(f"[格式错误] {rel_path}: 文件名格式不正确")
        continue
    
    # 推断 booklet_code
    vol_name = parts[1]  # 卷四/卷五/...
    booklet_letter = parts[2]  # 甲/乙/...
    suffix = parts[-1] if len(parts) >= 5 else None  # 上册/子册/...
    
    # 从目录结构或文件名推断完整的 booklet_code
    # 例如: 卷四/甲册 -> B01, 卷五/甲册/上册 -> B20A
    # 这里需要一个映射表
    
    # 先尝试从文件路径解析
    path_str = str(rel_path)
    
    # 提取文档中的二维码 ordinal
    try:
        with zipfile.ZipFile(docx_path, 'r') as z:
            files = z.namelist()
            
            # 查找 media 目录中的二维码图片
            # 格式: word/media/qr_123.png
            qr_images = [f for f in files if 'media/qr_' in f and f.endswith('.png')]
            
            if not qr_images:
                issues.append(f"[无二维码] {rel_path}: 找不到二维码图片")
                continue
            
            # 提取所有 ordinal
            ordinals = []
            for qr_file in qr_images:
                match = re.search(r'qr_(\d+)\.png', qr_file)
                if match:
                    ordinals.append(int(match.group(1)))
            
            ordinals = sorted(set(ordinals))
            
            if not ordinals:
                issues.append(f"[提取失败] {rel_path}: 无法提取 ordinal")
                continue
            
            print(f"\n{rel_path}")
            print(f"  文章数: {len(ordinals)}")
            print(f"  Ordinal 范围: {ordinals[0]}-{ordinals[-1]}")
            
            # 检查这些文章的 booklet_code 是否一致
            article_codes = set()
            for ord_num in ordinals:
                if ord_num in catalog:
                    article_codes.add(catalog[ord_num]['booklet_code'])
            
            if len(article_codes) == 0:
                issues.append(f"[编目缺失] {rel_path}: 所有文章都不在编目中")
            elif len(article_codes) > 1:
                issues.append(f"[分册混乱] {rel_path}: 包含多个分册的文章 {sorted(article_codes)}")
                print(f"  ⚠️  分册混乱: {sorted(article_codes)}")
            else:
                expected_code = list(article_codes)[0]
                print(f"  ✓ 分册: {expected_code}")
                
                # 验证是否包含该分册的所有文章
                expected_ordinals = set(booklet_articles[expected_code])
                actual_ordinals = set(ordinals)
                
                missing = expected_ordinals - actual_ordinals
                extra = actual_ordinals - expected_ordinals
                
                if missing:
                    issues.append(f"[缺失文章] {rel_path}: 缺少 {len(missing)} 篇文章 (ordinals: {sorted(list(missing))[:5]}...)")
                    print(f"  ⚠️  缺失 {len(missing)} 篇")
                
                if extra:
                    issues.append(f"[多余文章] {rel_path}: 多出 {len(extra)} 篇文章 (ordinals: {sorted(list(extra))[:5]}...)")
                    print(f"  ⚠️  多余 {len(extra)} 篇")
    
    except Exception as e:
        issues.append(f"[读取错误] {rel_path}: {e}")

# 输出审核报告
print("\n" + "=" * 80)
print("审核报告")
print("=" * 80)

if issues:
    print(f"\n发现 {len(issues)} 个问题:\n")
    for issue in issues:
        print(issue)
else:
    print("\n✓ 所有文档内容一致，无问题")
