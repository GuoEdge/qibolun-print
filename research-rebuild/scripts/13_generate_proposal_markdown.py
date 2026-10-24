#!/data/service/hnp/bin/python3
# -*- coding: utf-8 -*-
"""
生成《岐伯论选》（或拟定书名方案）完整呈报方案与一百篇篇目详录
"""

import json
from pathlib import Path

# 汉字数字映射（零写作〇）
CN_NUMS = ['〇', '一', '二', '三', '四', '五', '六', '七', '八', '九', '十']

def to_cn_num(n):
    if n <= 10:
        return CN_NUMS[n]
    elif n < 20:
        return '十' + (CN_NUMS[n % 10] if n % 10 != 0 else '')
    elif n < 100:
        tens = n // 10
        rem = n % 10
        return CN_NUMS[tens] + '十' + (CN_NUMS[rem] if rem != 0 else '')
    elif n == 100:
        return '一百'
    else:
        return str(n)

VOL_NAMES = {
    'V1': ('卷一', '本根敦倫', '家庭、宗族、亲子与伦常之骨架'),
    'V2': ('卷二', '陰陽合離', '两性、婚恋、契约与情爱之名理'),
    'V3': ('卷三', '酬酢進退', '人情、交游、世故与应变之界限'),
    'V4': ('卷四', '存神調息', '身心、容止、节律与情绪之安顿'),
    'V5': ('卷五', '度勢居貨', '职场、产业、权责与资财之筹谋'),
    'V6': ('卷六', '觀風察變', '世相、思潮、舆论与时代之机变'),
    'V7': ('卷七', '滌除玄覽', '认知、本体、心性与哲理之本源'),
    'V8': ('卷八', '格物鑄器', '百工、技艺、造物与器用之实相'),
}

def main():
    base = Path('/storage/Users/currentUser/Documents/岐伯论')
    in_jsonl = base / 'research-rebuild/data/qibo_wenxuan_100_final.jsonl'
    
    with open(in_jsonl, 'r', encoding='utf-8') as f:
        articles = [json.loads(line) for line in f if line.strip()]
        
    out_md = base / 'research-rebuild/reports/qibo_wenxuan_100_final_proposal.md'
    
    with open(out_md, 'w', encoding='utf-8') as f:
        f.write("# 《岐伯论选》（一百篇精编本）总体方案与篇目详目\n\n")
        f.write("> **编纂说明**：本方案从《岐伯论》五十五册（四千三百九十一篇）中，摒弃点赞、收藏等表层互动指标，完全基于文本精读、概念定义完整度、论证自洽性与思想原创性，精选一百篇代表作。全书沿袭原典八卷脉络，以「因题立骨·借象明理」为指归，旨在构筑岐伯先生最为精微、坚固的思想理论大厦。\n\n")
        
        f.write("## 壹· 书名拟案建议\n\n")
        f.write("1. **《岐伯论选》**（沉稳典雅，对标经典文选体裁，最宜传世）\n")
        f.write("2. **《岐伯近思录》**（借宋代理学之意，明其切己体察、切问近思之实践哲学）\n")
        f.write("3. **《岐伯通义》**（彰显其贯通伦常、人情、世势与心性的总括理论）\n")
        f.write("4. **《岐伯精言》**（简明提纲，适合案头常备、反复涵咏）\n\n")
        
        f.write("## 贰· 八卷架构与篇目配置\n\n")
        f.write("| 卷序 | 卷名 | 核心主旨 | 选收篇数 |\n")
        f.write("| :--- | :--- | :--- | :---: |\n")
        for v_code in ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8']:
            v_name, v_title, v_desc = VOL_NAMES[v_code]
            count = sum(1 for a in articles if a['volume_code'] == v_code)
            f.write(f"| {v_name} | **{v_title}** | {v_desc} | {to_cn_num(count)}篇 |\n")
        f.write(f"| **通计** | **八卷完备** | **涵盖修身、齐家、应世、格物之全息体系** | **一百篇** |\n\n")
        
        f.write("## 叁· 核心概念群谱系落地\n\n")
        f.write("本选本全面覆盖并锚定了岐伯独创核心概念，确保概念有提出、有论证、有推演：\n\n")
        f.write("- **自强**（二十二篇）：破除外在虚妄认可，建立内在确定性动力源。\n")
        f.write("- **神性享乐**（十五篇）：超越生理与功利刺激的至高精神愉悦。\n")
        f.write("- **人己权界**（十三篇）：界定权利、权柄与是非边界，反思越权执法与道德绑架。\n")
        f.write("- **SOP**（十二篇）：将复杂处世、汇报与协同转化为高确定性作业程序。\n")
        f.write("- **元技能**（十一篇）：底层认知、注意力管理与复利学习能力。\n")
        f.write("- **旷野**（八篇）：脱离既定考核与社会评价温室，直面真实世界考验。\n")
        f.write("- **净输出**（七篇）：摆脱内耗与债务关系，保持能量与价值的正向输出。\n")
        f.write("- **择善固执**（七篇）：在信息噪音与道德绑架中保持认知坚守。\n")
        f.write("- **信源管理**（六篇）：严控输入质量，防范虚假信息与情绪投毒。\n")
        f.write("- **错得对**（五篇）：在非黑即白的世界里理解次优解、妥协演化与容错战略。\n")
        f.write("- **评价权 / CARITAS / 不以恶为业 / 爱不生债 / 人神分野**：皆在各卷立骨篇目中充分展现。\n\n")
        
        f.write("## 肆· 精选一百篇完整目录详录\n\n")
        
        global_idx = 1
        for v_code in ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8']:
            v_name, v_title, v_desc = VOL_NAMES[v_code]
            v_articles = [a for a in articles if a['volume_code'] == v_code]
            f.write(f"### {v_name} · {v_title}（共{to_cn_num(len(v_articles))}篇）\n\n")
            f.write(f"> *{v_desc}*\n\n")
            
            for a in v_articles:
                cn_idx = to_cn_num(global_idx)
                f.write(f"#### 第{cn_idx}篇：{a['title']}\n")
                f.write(f"- **出处**：{a['full_citation']}\n")
                f.write(f"- **篇幅**：{len(a.get('answer',''))}字\n")
                concepts = a.get('concept_hits', [])
                if concepts:
                    f.write(f"- **核心概念**：{', '.join(concepts)}\n")
                f.write(f"- **思想精要**：{a['answer'][:180].replace(chr(10), ' ')}……\n\n")
                global_idx += 1
                
    print(f"✓ 方案报告已生成至: {out_md}")

if __name__ == '__main__':
    main()
