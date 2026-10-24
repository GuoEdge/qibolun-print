#!/usr/bin/env python3
"""
DOCX内容完整性审核脚本
功能：检查所有DOCX文档中的文章是否与编目数据库中的booklet_code一致
"""
import json
import os
import re
import sys
from pathlib import Path
from collections import defaultdict

# 路径配置
ROOT = Path('/storage/Users/currentUser/Documents/岐伯论')
CATALOG = ROOT / 'research-rebuild/reports/gemini-flash-reclassification-v1/workbook-40b-all-catalog.jsonl'

# 卷目录映射
VOLUME_DIRS = {
    'V4': ROOT / '卷四',
    'V5': ROOT / '卷五',
    'V6': ROOT / '卷六',
    'V7': ROOT / '卷七',
    'V8': ROOT / '卷八'
}

# 分册配置（从build_volumes_v4_v8.js提取）
BOOKLET_CONFIG = {
    'B17': {'volume': 'V4', 'name': '情志平復與容貌自和'},
    'B18': {'volume': 'V4', 'name': '作息節律與病理常識'},
    'B19': {'volume': 'V4', 'name': '知行精進與克服拖延'},
    'B20A': {'volume': 'V5', 'name': '職場彙報與權責留痕', 'suffix': '上册'},
    'B20B': {'volume': 'V5', 'name': '職場彙報與權責留痕', 'suffix': '中册'},
    'B20C': {'volume': 'V5', 'name': '職場彙報與權責留痕', 'suffix': '下册'},
    'B21': {'volume': 'V5', 'name': '體制生存與職業自保'},
    'B22': {'volume': 'V5', 'name': '商業競爭與資產投資'},
    'B23': {'volume': 'V6', 'name': '公共熱點與事件剖析'},
    'B24': {'volume': 'V6', 'name': '青年心境與躺平反思'},
    'B25': {'volume': 'V6', 'name': '網絡生態與群體極化'},
    'B26': {'volume': 'V6', 'name': '性別議題與兩性輿論'},
    'B27': {'volume': 'V6', 'name': '教育體制與社會流動'},
    'B28': {'volume': 'V6', 'name': '消費主義與生活觀念'},
    'B29': {'volume': 'V6', 'name': '現代科技與工具反思'},
    'B30': {'volume': 'V6', 'name': '文明演進與社會秩序'},
    'B31A': {'volume': 'V7', 'name': '存在本質與生命意義', 'suffix': '上册'},
    'B31B': {'volume': 'V7', 'name': '存在本質與生命意義', 'suffix': '下册'},
    'B32': {'volume': 'V7', 'name': '名相辨析與語言牢籠'},
    'B33': {'volume': 'V7', 'name': '善惡分野與倫理底線'},
    'B34': {'volume': 'V7', 'name': '認識局限與心智模型'},
    'B35': {'volume': 'V7', 'name': '命途因果與得失隨緣'},
    'B36': {'volume': 'V7', 'name': '人性幽微與雙重人格'},
    'B37': {'volume': 'V7', 'name': '神聖敬畏與信仰維度'},
    'B38A': {'volume': 'V7', 'name': '自處之道與精神獨立', 'suffix': '子册'},
    'B38B': {'volume': 'V7', 'name': '自處之道與精神獨立', 'suffix': '丑册'},
    'B38C': {'volume': 'V7', 'name': '自處之道與精神獨立', 'suffix': '寅册'},
    'B38D': {'volume': 'V7', 'name': '自處之道與精神獨立', 'suffix': '卯册'},
    'B38E': {'volume': 'V7', 'name': '自處之道與精神獨立', 'suffix': '辰册'},
    'B38F': {'volume': 'V7', 'name': '自處之道與精神獨立', 'suffix': '巳册'},
    'B38G': {'volume': 'V7', 'name': '自處之道與精神獨立', 'suffix': '午册'},
    'B38H': {'volume': 'V7', 'name': '自處之道與精神獨立', 'suffix': '未册'},
    'B38I': {'volume': 'V7', 'name': '自處之道與精神獨立', 'suffix': '申册'},
    'B38J': {'volume': 'V7', 'name': '自處之道與精神獨立', 'suffix': '酉册'},
    'B38K': {'volume': 'V7', 'name': '自處之道與精神獨立', 'suffix': '戌册'},
    'B38L': {'volume': 'V7', 'name': '自處之道與精神獨立', 'suffix': '亥册'},
    'B39': {'volume': 'V8', 'name': '藝能創作與生活美學'},
    'B40': {'volume': 'V8', 'name': '治亂興亡與國家工程'}
}

def load_catalog():
    """加载编目数据库"""
    catalog = {}
    with open(CATALOG, 'r', encoding='utf-8') as f:
        for line in f:
            rec = json.loads(line)
            # 使用original_id作为key
            catalog[rec['original_id']] = rec
    print(f"✓ 已加载编目数据库：{len(catalog)} 条记录")
    return catalog

def find_all_docx_files():
    """查找所有V4-V8的DOCX文件"""
    docx_files = []
    for vol_code, vol_dir in VOLUME_DIRS.items():
        if vol_dir.exists():
            for docx in vol_dir.rglob('岐伯论·*.docx'):
                docx_files.append(docx)
    print(f"✓ 找到 {len(docx_files)} 个DOCX文件")
    return sorted(docx_files)

def extract_booklet_code_from_path(docx_path):
    """从文件路径提取分册代码"""
    # 文件名格式：岐伯论·卷X·干·主题名·册次.docx
    # 需要根据路径和文件名反推booklet_code
    
    filename = docx_path.stem
    parent_dirs = str(docx_path.parent)
    
    # 提取主题名和册次
    parts = filename.split('·')
    if len(parts) < 3:
        return None
    
    theme_name = parts[-2] if len(parts) >= 4 else parts[-1]
    suffix = parts[-1] if len(parts) >= 4 and parts[-1].endswith('册') else None
    
    # 匹配BOOKLET_CONFIG
    for code, config in BOOKLET_CONFIG.items():
        if theme_name in config['name']:
            if suffix:
                if 'suffix' in config and suffix == config['suffix']:
                    return code
            elif 'suffix' not in config:
                return code
    
    return None

def extract_article_ids_from_docx_via_qr(docx_path):
    """
    从DOCX文件中提取所有文章ID
    方法：解析document.xml中的二维码URL
    """
    import zipfile
    
    article_ids = []
    
    try:
        with zipfile.ZipFile(docx_path, 'r') as docx_zip:
            xml_content = docx_zip.read('word/document.xml').decode('utf-8')
            
            # 提取所有二维码URL：https://sooon.ai/answer/article-{id}
            qr_pattern = r'https://sooon\.ai/answer/article-([a-f0-9-]+)'
            matches = re.findall(qr_pattern, xml_content)
            article_ids = matches
            
    except Exception as e:
        print(f"  ✗ 无法解析 {docx_path.name}: {e}")
        return []
    
    return article_ids

def main():
    """主审核流程"""
    print("=" * 80)
    print("DOCX内容完整性审核")
    print("=" * 80)
    print()
    
    # 1. 加载编目数据库
    catalog = load_catalog()
    
    # 2. 查找所有DOCX文件
    docx_files = find_all_docx_files()
    
    if not docx_files:
        print("✗ 未找到任何DOCX文件")
        return 1
    
    print()
    print("=" * 80)
    print("开始逐册审核")
    print("=" * 80)
    print()
    
    # 3. 逐册审核
    total_errors = 0
    booklet_results = {}
    
    for docx_path in docx_files:
        # 提取分册代码
        booklet_code = extract_booklet_code_from_path(docx_path)
        if not booklet_code:
            print(f"⚠ 无法识别分册代码：{docx_path}")
            continue
        
        print(f"\n>>> {booklet_code}: {docx_path.name}")
        
        # 提取文章ID列表
        article_ids = extract_article_ids_from_docx_via_qr(docx_path)
        print(f"  文章数：{len(article_ids)}")
        
        if not article_ids:
            print(f"  ⚠ 未提取到任何文章ID")
            continue
        
        # 逐篇检查
        mismatches = []
        for idx, article_id in enumerate(article_ids, 1):
            if article_id not in catalog:
                mismatches.append({
                    'seq': idx,
                    'article_id': article_id,
                    'error': '编目中不存在'
                })
                continue
            
            rec = catalog[article_id]
            expected_code = rec['booklet_code']
            
            if expected_code != booklet_code:
                mismatches.append({
                    'seq': idx,
                    'article_id': article_id,
                    'title': rec['title'],
                    'expected': expected_code,
                    'actual': booklet_code
                })
        
        # 输出结果
        if mismatches:
            print(f"  ✗ 发现 {len(mismatches)} 篇文章归属错误：")
            for m in mismatches:
                if 'error' in m:
                    print(f"    [{m['seq']}] {m['article_id']}: {m['error']}")
                else:
                    print(f"    [{m['seq']}] {m['title']} ({m['article_id']})")
                    print(f"         应归属：{m['expected']}，实际在：{m['actual']}")
            total_errors += len(mismatches)
            booklet_results[booklet_code] = {'errors': len(mismatches), 'details': mismatches}
        else:
            print(f"  ✓ 所有文章归属正确")
            booklet_results[booklet_code] = {'errors': 0}
    
    # 4. 总结
    print()
    print("=" * 80)
    print("审核总结")
    print("=" * 80)
    print()
    
    if total_errors == 0:
        print("✓ 所有DOCX文档内容与编目数据库完全一致")
        return 0
    else:
        print(f"✗ 共发现 {total_errors} 篇文章归属错误")
        print()
        print("错误分布：")
        for code, result in sorted(booklet_results.items()):
            if result['errors'] > 0:
                print(f"  {code}: {result['errors']} 篇")
        
        # 输出详细错误报告
        print()
        print("=" * 80)
        print("详细错误报告")
        print("=" * 80)
        print()
        for code, result in sorted(booklet_results.items()):
            if result['errors'] > 0:
                print(f"\n### {code}")
                for m in result['details']:
                    if 'error' in m:
                        print(f"  [{m['seq']}] {m['article_id']}: {m['error']}")
                    else:
                        print(f"  [{m['seq']}] {m['title']}")
                        print(f"       应归属：{m['expected']}，实际在：{m['actual']}")
        
        return 1

if __name__ == '__main__':
    sys.exit(main())
