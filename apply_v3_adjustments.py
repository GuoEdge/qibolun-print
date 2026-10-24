# -*- coding: utf-8 -*-
"""
执行卷三 37 篇文章的精准调整归位
"""
import json
import os

catalog_path = 'research-rebuild/reports/gemini-flash-reclassification-v1/workbook-40b-all-catalog-v4.jsonl'

# 1. 加载并构建分册元数据映射
booklet_meta = {}
with open(catalog_path, 'r', encoding='utf-8') as f:
    for line in f:
        if not line.strip(): continue
        item = json.loads(line)
        bc = item.get('booklet_code')
        vc = item.get('volume_code')
        key = f'{vc}-{bc}'
        if key not in booklet_meta:
            booklet_meta[key] = {
                'volume_code': vc,
                'volume_prefix': item.get('volume_prefix'),
                'volume_full_title': item.get('volume_full_title'),
                'booklet_code': bc,
                'booklet_name': item.get('booklet_name'),
                'booklet_stem': item.get('booklet_stem'),
                'booklet_stem_title': item.get('booklet_stem_title'),
                'full_citation': item.get('full_citation')
            }

# 2. 定义 37 篇调整文章的目标映射 (以 title 或 original_id 为准)
# 格式: title -> (target_vol, target_booklet)
migration_map = {
    # --- 甲册 B14 (9篇) ---
    '一只小桃子': ('V1', 'B01'),      # 幼儿启蒙与性情习惯
    '欠债还钱': ('V5', 'B22'),        # 商业竞争与资产投资
    '盗火线': ('V5', 'B20A'),         # 职场汇报与权责留痕·上册
    '无私怨': ('V6', 'B23'),          # 公共热点与事件剖析
    '来不来': ('V5', 'B21'),          # 体制生存与职业自保
    '富贵险': ('V5', 'B22'),          # 商业竞争与资产投资
    '世界的二象性': ('V5', 'B20A'),   # 职场汇报与权责留痕·上册
    '作为主人的价值': ('V5', 'B20A'), # 职场汇报与权责留痕·上册
    '戒色': ('V4', 'B17'),            # 情志平复与容貌自和

    # --- 乙册 B15 (2篇) ---
    '三自由': ('V1', 'B03'),          # 言传身教与奖惩边界
    '自爱': ('V4', 'B17'),            # 情志平复与容貌自和

    # --- 丙册 B16 (26篇) ---
    '宁不畏死2': ('V6', 'B23'),       # 公共热点与事件剖析
    '2 Shots': ('V1', 'B03'),         # 言传身教与奖惩边界
    '深沉': ('V7', 'B34'),            # 认识局限与心智模型
    '哥利亚说': ('V3', 'B14'),        # 人情往来与礼数分寸 (卷内微调)
    '钢的兔': ('V6', 'B23'),          # 公共热点与事件剖析
    'zw器神教': ('V2', 'B11'),        # 择偶标准与两性吸引
    '向后看': ('V1', 'B05'),          # 父母控制欲与精神解绑
    '现实问题': ('V7', 'B32'),        # 名相辨析与语言牢笼
    '愚蠢之为物也': ('V7', 'B34'),    # 认识局限与心智模型
    '镇妖塔': ('V8', 'B40'),          # 治乱兴亡与国家工程
    '上流社会': ('V6', 'B27'),        # 教育体制与社会流动
    '你来我来': ('V8', 'B39'),        # 艺能创作与生活美学
    '本分': ('V5', 'B22'),            # 商业竞争与资产投资
    '家祭无忘告乃翁': ('V1', 'B10'),  # 临终关怀与白事奠仪
    '快改慢': ('V6', 'B23'),          # 公共热点与事件剖析
    '上下不合': ('V5', 'B20A'),       # 职场汇报与权责留痕·上册
    '骗子标准': ('V7', 'B34'),        # 认识局限与心智模型
    '天地无用': ('V6', 'B23'),        # 公共热点与事件剖析
    '政治的科学': ('V7', 'B32'),      # 名相辨析与语言牢笼
    '可信标准': ('V7', 'B34'),        # 认识局限与心智模型
    '爱的痛苦': ('V2', 'B11'),        # 择偶标准与两性吸引
    '提升格局': ('V7', 'B34'),        # 认识局限与心智模型
    '我是对的': ('V7', 'B32'),        # 名相辨析与语言牢笼
    '傲慢': ('V7', 'B34'),            # 认识局限与心智模型
    '死亡': ('V7', 'B31A'),           # 存在本质与生命意义·上册
    'Black Wallstreet': ('V8', 'B40'),# 治乱兴亡与国家工程
    '公开换安全': ('V2', 'B11'),      # 择偶标准与两性吸引
}

# 3. 执行更新
updated_count = 0
catalog_items = []

with open(catalog_path, 'r', encoding='utf-8') as f:
    for line in f:
        if not line.strip(): continue
        item = json.loads(line)
        t = item.get('title')
        vc = item.get('volume_code')
        
        # 确保只有卷三中的这些文章被调整
        if vc == 'V3' and t in migration_map:
            target_vc, target_bc = migration_map[t]
            meta_key = f'{target_vc}-{target_bc}'
            if meta_key not in booklet_meta:
                raise ValueError(f'未找到元数据: {meta_key}')
            
            meta = booklet_meta[meta_key]
            # 更新字段
            item['volume_code'] = meta['volume_code']
            item['volume_prefix'] = meta['volume_prefix']
            item['volume_full_title'] = meta['volume_full_title']
            item['booklet_code'] = meta['booklet_code']
            item['booklet_name'] = meta['booklet_name']
            item['booklet_stem'] = meta['booklet_stem']
            item['booklet_stem_title'] = meta['booklet_stem_title']
            item['full_citation'] = meta['full_citation']
            
            updated_count += 1
            print(f'已调整: 《{t}》 -> {meta["volume_code"]} ({meta["booklet_code"]} {meta["booklet_name"]})')
        
        catalog_items.append(item)

print(f'\n调整完成! 共更新 {updated_count} 篇文章。')

# 4. 写回总表
with open(catalog_path, 'w', encoding='utf-8') as f:
    for item in catalog_items:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')

print(f'已成功保存更新到 {catalog_path}')
