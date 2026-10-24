#!/usr/bin/env python3
"""审核所有DOCX文档，确保文章数量与编目一致"""

import zipfile
import json
from pathlib import Path
from collections import defaultdict

BASE = Path('/storage/Users/currentUser/Documents/岐伯论')
CATALOG = BASE / 'research-rebuild/reports/gemini-flash-reclassification-v1/workbook-40b-all-catalog.jsonl'

# 分册代码映射（从路径和文件名推断）
BOOKLET_MAPPING = {
    # 卷四
    ('卷四', '甲册'): 'B17',
    ('卷四', '乙册'): 'B18',
    ('卷四', '丙册'): 'B19',
    # 卷五
    ('卷五', '甲册', '上册'): 'B20A',
    ('卷五', '甲册', '中册'): 'B20B',
    ('卷五', '甲册', '下册'): 'B20C',
    ('卷五', '乙册'): 'B21',
    ('卷五', '丙册'): 'B22',
    # 卷六
    ('卷六', '甲册'): 'B23',
    ('卷六', '乙册'): 'B24',
    ('卷六', '丙册'): 'B25',
    ('卷六', '丁册'): 'B26',
    ('卷六', '戊册'): 'B27',
    ('卷六', '己册'): 'B28',
    ('卷六', '庚册'): 'B29',
    ('卷六', '辛册'): 'B30',
    # 卷七
    ('卷七', '甲册', '上册'): 'B31A',
    ('卷七', '甲册', '下册'): 'B31B',
    ('卷七', '乙册'): 'B32',
    ('卷七', '丙册'): 'B33',
    ('卷七', '丁册'): 'B34',
    ('卷七', '戊册'): 'B35',
    ('卷七', '己册'): 'B36',
    ('卷七', '庚册'): 'B37',
    ('卷七', '辛册', '子册'): 'B38A',
    ('卷七', '辛册', '丑册'): 'B38B',
    ('卷七', '辛册', '寅册'): 'B38C',
    ('卷七', '辛册', '卯册'): 'B38D',
    ('卷七', '辛册', '辰册'): 'B38E',
    ('卷七', '辛册', '巳册'): 'B38F',
    ('卷七', '辛册', '午册'): 'B38G',
    ('卷七', '辛册', '未册'): 'B38H',
    ('卷七', '辛册', '申册'): 'B38I',
    ('卷七', '辛册', '酉册'): 'B38J',
    ('卷七', '辛册', '戌册'): 'B38K',
    ('卷七', '辛册', '亥册'): 'B38L',
    # 卷八
    ('卷八', '甲册'): 'B39',
    ('卷八', '乙册'): 'B40',
}

# 加载编目数据
catalog = {}
booklet_counts = defaultdict(int)

with open(CATALOG, 'r', encoding='utf-8') as f:
    for line in f:
        if not line.strip():
            continue
        rec = json.loads(line)
        ordinal = rec['workbook_ordinal']
        code = rec['booklet_code']
        catalog[ordinal] = rec
        booklet_counts[code] += 1

print(f"编目总数: {len(catalog)}")
print(f"分册数: {len(booklet_counts)}")

# 扫描所有DOCX文件
docx_files = []
for vol_dir in ['卷一', '卷二', '卷三', '卷四', '卷五', '卷六', '卷七', '卷八']:
    vol_path = BASE / vol_dir
    if vol_path.exists():
        docx_files.extend(vol_path.rglob('岐伯论·*.docx'))

print(f"\n找到 {len(docx_files)} 个DOCX文件\n")

# 审核每个文件
issues = []
checked = 0

for docx_path in sorted(docx_files):
    rel_path = docx_path.relative_to(BASE)
    
    # 从路径推断分册代码
    parts = list(docx_path.relative_to(BASE).parts)
    
    # 提取卷、册信息
    vol_name = parts[0] if len(parts) > 0 else None
    
    # 尝试匹配映射表
    booklet_code = None
    
    # 尝试不同的路径组合
    if len(parts) >= 2:
        key2 = (parts[0], parts[1])
        if key2 in BOOKLET_MAPPING:
            booklet_code = BOOKLET_MAPPING[key2]
    
    if not booklet_code and len(parts) >= 3:
        key3 = (parts[0], parts[1], parts[2])
        if key3 in BOOKLET_MAPPING:
            booklet_code = BOOKLET_MAPPING[key3]
    
    if not booklet_code:
        # 无法识别分册，跳过
        print(f"⚠️  无法识别分册: {rel_path}")
        continue
    
    expected_count = booklet_counts.get(booklet_code, 0)
    
    # 统计DOCX中的媒体文件数量
    try:
        with zipfile.ZipFile(docx_path, 'r') as z:
            media_files = [f for f in z.namelist() if f.startswith('word/media/') and not f.endswith('/')]
            
            # docx库会将图片重命名为 .undefined 后缀
            # 所有非目录的 media 文件都算
            # media数量 = 文章数 + 1封面图
            actual_article_count = len(media_files) - 1
            
            status = "✓" if actual_article_count == expected_count else "✗"
            
            print(f"{status} {booklet_code} | 期望:{expected_count:3d} | 实际:{actual_article_count:3d} | {rel_path}")
            
            if actual_article_count != expected_count:
                diff = actual_article_count - expected_count
                issues.append({
                    'path': str(rel_path),
                    'code': booklet_code,
                    'expected': expected_count,
                    'actual': actual_article_count,
                    'diff': diff
                })
            
            checked += 1
    
    except Exception as e:
        print(f"✗ {booklet_code} | 读取错误: {e} | {rel_path}")
        issues.append({
            'path': str(rel_path),
            'code': booklet_code,
            'error': str(e)
        })

# 输出审核报告
print("\n" + "=" * 80)
print("审核报告")
print("=" * 80)

print(f"\n已审核: {checked} 个文件")

if issues:
    print(f"\n发现 {len(issues)} 个问题:\n")
    for issue in issues:
        if 'error' in issue:
            print(f"  [读取错误] {issue['code']} - {issue['path']}: {issue['error']}")
        else:
            diff_str = f"+{issue['diff']}" if issue['diff'] > 0 else str(issue['diff'])
            print(f"  [数量不匹配] {issue['code']} - {issue['path']}: 期望{issue['expected']}篇，实际{issue['actual']}篇 ({diff_str})")
else:
    print("\n✓ 所有文档内容数量一致，无问题")
