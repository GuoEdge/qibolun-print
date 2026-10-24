#!/usr/bin/env python3
"""修复B39的answer和narrative字段，从原始数据的lexical字段提取"""

import json
import sys

# 加载extract_qibo_content.js中的提取逻辑（Python实现）
def extract_from_lexical(lexical_str):
    """从lexical JSON字符串提取answer和narrative"""
    try:
        lexical = json.loads(lexical_str) if isinstance(lexical_str, str) else lexical_str
    except:
        return "", ""
    
    if not lexical or 'root' not in lexical:
        return "", ""
    
    narrative_parts = []
    answer_parts = []
    
    def extract_text_from_node(node):
        """递归提取节点中的文本"""
        texts = []
        if isinstance(node, dict):
            node_type = node.get('type', '')
            
            # 文本叶子节点
            if node_type in ['text', 'p-text']:
                texts.append(node.get('text', ''))
            
            # 递归处理子节点
            children = node.get('children', [])
            for child in children:
                texts.extend(extract_text_from_node(child))
        
        return texts
    
    def process_node(node, is_quote_context=False):
        """处理节点，区分quote和正文"""
        if not isinstance(node, dict):
            return
        
        node_type = node.get('type', '')
        
        # quote类型是提问者叙述
        if node_type == 'quote':
            texts = extract_text_from_node(node)
            if texts:
                narrative_parts.append(''.join(texts))
            # quote内部不再递归
            return
        
        # 其他类型是岐伯回答
        if node_type in ['paragraph', 'heading', 'list', 'list-item', 'link']:
            texts = extract_text_from_node(node)
            if texts:
                answer_parts.append(''.join(texts))
        
        # 递归处理子节点
        children = node.get('children', [])
        for child in children:
            process_node(child, is_quote_context)
    
    # 从root开始处理
    root = lexical.get('root', {})
    children = root.get('children', [])
    
    for child in children:
        process_node(child)
    
    narrative = '\n'.join(narrative_parts).strip()
    answer = '\n'.join(answer_parts).strip()
    
    return answer, narrative


# 主程序
def main():
    print("=" * 60)
    print("修复B39数据 - 从lexical提取answer和narrative")
    print("=" * 60)
    
    # 1. 加载原始数据
    original_path = 'sooon-q9adg-articles-v2.jsonl'
    original_data = {}
    
    print("\n加载原始数据...")
    with open(original_path, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line.strip())
            article_id = data.get('id')
            if article_id:
                original_data[article_id] = data
    
    print(f"原始数据共 {len(original_data)} 条记录")
    
    # 2. 加载catalog并定位B39
    catalog_path = 'research-rebuild/reports/gemini-flash-reclassification-v1/workbook-40b-all-catalog.jsonl'
    
    print("\n加载catalog并修复B39...")
    all_records = []
    b39_fixed = 0
    b39_failed = 0
    
    with open(catalog_path, 'r', encoding='utf-8') as f:
        for line in f:
            record = json.loads(line.strip())
            
            # 如果是B39且answer为空，尝试修复
            if record.get('booklet_code') == 'B39' and not record.get('answer'):
                orig_id = record.get('original_id')
                
                if orig_id in original_data:
                    orig = original_data[orig_id]
                    lexical = orig.get('lexical')
                    
                    if lexical:
                        answer, narrative = extract_from_lexical(lexical)
                        
                        if answer:  # 成功提取
                            record['answer'] = answer
                            record['narrative'] = narrative
                            record['text_len'] = len(answer) + len(narrative)
                            
                            # 更新text_preview
                            full_text = (narrative + '\n' + answer).strip()
                            record['text_preview'] = full_text[:200] + ('...' if len(full_text) > 200 else '')
                            
                            b39_fixed += 1
                            print(f"  ✓ 修复: {record.get('title')} (answer: {len(answer)}字, narrative: {len(narrative)}字)")
                        else:
                            b39_failed += 1
                            print(f"  ✗ 提取失败: {record.get('title')}")
                    else:
                        # 没有lexical，使用text字段作为answer
                        text = orig.get('text', '')
                        if text:
                            record['answer'] = text
                            record['narrative'] = ''
                            b39_fixed += 1
                            print(f"  ✓ 使用text字段: {record.get('title')} ({len(text)}字)")
                        else:
                            b39_failed += 1
                            print(f"  ✗ 无可用数据: {record.get('title')}")
            
            all_records.append(record)
    
    # 3. 备份并写入
    print(f"\n修复统计:")
    print(f"  成功修复: {b39_fixed} 篇")
    print(f"  修复失败: {b39_failed} 篇")
    
    if b39_fixed > 0:
        # 备份原文件
        backup_path = catalog_path + '.bak-before-b39-fix'
        import shutil
        shutil.copy2(catalog_path, backup_path)
        print(f"\n原文件已备份至: {backup_path}")
        
        # 写入修复后的数据
        with open(catalog_path, 'w', encoding='utf-8') as f:
            for record in all_records:
                f.write(json.dumps(record, ensure_ascii=False) + '\n')
        
        print(f"修复后的数据已写入: {catalog_path}")
        print("\n✅ B39数据修复完成！")
    else:
        print("\n⚠️  没有数据被修复")
    
    return 0 if b39_failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
