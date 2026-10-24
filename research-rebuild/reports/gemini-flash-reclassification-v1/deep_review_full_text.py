#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
深度通读检查工具 - 完整阅读每篇文章全文进行判断
"""

import json
import sys
from typing import Dict, List

def load_data():
    """加载所有数据"""
    with open('workbook-40b-all-catalog.jsonl', 'r', encoding='utf-8') as f:
        catalog = [json.loads(line) for line in f]
    
    with open('merged-classification.jsonl', 'r', encoding='utf-8') as f:
        classification = {json.loads(line)['id']: json.loads(line) for line in f}
    
    with open('all-articles-merged-v3-clean.jsonl', 'r', encoding='utf-8') as f:
        articles = {json.loads(line)['id']: json.loads(line) for line in f}
    
    return catalog, classification, articles

def review_booklet_interactive(booklet_code: str, booklet_name: str, expected_topic: str, 
                               catalog: List, classification: Dict, articles: Dict):
    """交互式深度通读单个分册"""
    
    items = [x for x in catalog if x['booklet_code'] == booklet_code]
    
    print("\n" + "=" * 80)
    print(f"【{booklet_code} - {booklet_name}】")
    print(f"预期主题: {expected_topic} | 总篇数: {len(items)}")
    print("=" * 80)
    
    misplaced = []  # 确认错放的文章
    questionable = []  # 存疑的文章
    correct = []  # 正确放置的文章
    
    for i, item in enumerate(items, 1):
        article_id = item['original_id']
        title = item['title']
        question = item.get('question', '')
        
        # 获取分类和全文
        cls = classification.get(article_id, {})
        topic_code = cls.get('primary_topic_code', 'UNKNOWN')
        topic_name = cls.get('primary_topic_name', '')
        
        art = articles.get(article_id, )
        answer = art.get('answer', '')
        narrative = art.get('narrative', '')
        
        # 显示文章供人工审阅
        print(f"\n{'─'*80}")
        print(f"[{i}/{len(items)}] {title}")
        print(f"分类: [{topic_code}] {topic_name} | 预期: {expected_topic}")
        print(f"{'─'*80}")
        print(f"\n【问题】{question}\n")
        
        if narrative:
            print(f"【提问者叙述】（{len(narrative)}字）\n{narrative}\n")
        
        print(f"【岐伯回答】（{len(answer)}字）\n{answer}\n")
        
        # 如果主题代码匹配预期，记录为正确
        if topic_code == expected_topic:
            correct.append({
                'id': article_id,
                'title': title,
                'topic_code': topic_code
            })
            print(f"✓ 主题代码匹配，记录为【正确放置】")
        else:
            # 需要人工判断
            print(f"\n⚠️  主题代码为 {topic_code}，与预期 {expected_topic} 不符")
            print(f"\n请判断这篇文章：")
            print("  1 - 确认错放（内容完全不符合分册主题）")
            print("  2 - 存疑（主题代码不同但场景合理）")
            print("  3 - 实际正确（虽主题代码不同但确实应该在此分册）")
            print("  s - 跳过本篇")
            print("  q - 退出检查")
            
            choice = input("\n你的判断 [1/2/3/s/q]: ").strip().lower()
            
            if choice == 'q':
                print("\n用户选择退出检查")
                break
            elif choice == 's':
                print("跳过本篇")
                continue
            elif choice == '1':
                reason = input("请简述错放原因: ").strip()
                misplaced.append({
                    'id': article_id,
                    'title': title,
                    'topic_code': topic_code,
                    'reason': reason or '内容不符合分册主题'
                })
                print("✓ 已记录为【确认错放】")
            elif choice == '2':
                reason = input("请简述存疑原因: ").strip()
                questionable.append({
                    'id': article_id,
                    'title': title,
                    'topic_code': topic_code,
                    'reason': reason or '主题代码不同但场景可能合理'
                })
                print("✓ 已记录为【存疑待定】")
            elif choice == '3':
                reason = input("请简述正确原因: ").strip()
                correct.append({
                    'id': article_id,
                    'title': title,
                    'topic_code': topic_code,
                    'reason': reason or '虽主题代码不同但应在此分册'
                })
                print("✓ 已记录为【实际正确】")
    
    # 输出统计
    print(f"\n\n{'='*80}")
    print(f"【{booklet_code}】检查完成")
    print(f"{'='*80}")
    print(f"正确放置: {len(correct)} 篇")
    print(f"确认错放: {len(misplaced)} 篇")
    print(f"存疑待定: {len(questionable)} 篇")
    print(f"{'='*80}\n")
    
    return {
        'booklet_code': booklet_code,
        'booklet_name': booklet_name,
        'total': len(items),
        'correct': correct,
        'misplaced': misplaced,
        'questionable': questionable
    }

def main():
    if len(sys.argv) < 2:
        print("用法: python3 deep_review_full_text.py <分册代码>")
        print("示例: python3 deep_review_full_text.py B01")
        sys.exit(1)
    
    booklet_code = sys.argv[1].upper()
    
    # 加载数据
    print("正在加载数据...")
    catalog, classification, articles = load_data()
    
    # 定义分册信息（简化版，仅列主要分册）
    booklets_info = {
        'B01': ('婚恋择偶之道', 'G01'),
        'B02': ('婚前情感须知', 'G01'),
        'B03': ('两性相处之道', 'G01'),
        # ... 其他分册可按需添加
    }
    
    if booklet_code not in booklets_info:
        print(f"错误: 未找到分册 {booklet_code} 的信息")
        print("请在脚本中添加该分册的定义")
        sys.exit(1)
    
    booklet_name, expected_topic = booklets_info[booklet_code]
    
    # 执行交互式深度通读
    result = review_booklet_interactive(
        booklet_code, booklet_name, expected_topic,
        catalog, classification, articles
    )
    
    # 保存结果
    output_file = f'deep_review_{booklet_code}.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print(f"\n结果已保存到: {output_file}")

if __name__ == '__main__':
    main()
