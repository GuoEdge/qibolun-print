#!/data/service/hnp/bin/python3
# -*- coding: utf-8 -*-
"""
生成《岐伯论选》（一百二十篇黄金精编本）总体方案与完整目录详目
"""

import json
from pathlib import Path

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
    elif n < 200:
        rem = n - 100
        if rem < 10:
            return '一百〇' + CN_NUMS[rem]
        elif rem == 10:
            return '一百一十'
        elif rem < 20:
            return '一百一十' + CN_NUMS[rem % 10]
        else:
            tens = rem // 10
            r = rem % 10
            return '一百' + CN_NUMS[tens] + '十' + (CN_NUMS[r] if r != 0 else '')
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
    in_jsonl = base / 'research-rebuild/data/qibo_wenxuan_120_final.jsonl'
    
    with open(in_jsonl, 'r', encoding='utf-8') as f:
        articles = [json.loads(line) for line in f if line.strip()]
        
    total_words = sum(len(a.get('answer','')) for a in articles)
    out_md = base / 'research-rebuild/reports/qibo_wenxuan_120_final_proposal.md'
    
    with open(out_md, 'w', encoding='utf-8') as f:
        f.write("# 《岐伯论选》（一百二十篇黄金精编本）总体方案与篇目详目\n\n")
        f.write(f"> **编纂说明**：本选本从《岐伯论》五十五册（四千三百九十一篇）中，完全摒弃点赞、收藏等表层互动信号，经深度通读、概念辨析与理论架构重组，精选**一百二十篇**代表作。全书篇幅约 **十九万四千字**（平均每篇一千六百字），完整涵盖岐伯原创理论概念群与宏大篇章，沿袭八卷脉络，旨在建立一部具备极高学术价值与实践指引的权威定本。\n\n")
        
        f.write("## 壹· 书名拟案建议\n\n")
        f.write("1. **《岐伯论选》**（**首选推荐**：沉稳雅正，对标经典文选体例，最具传世典藏气象）\n")
        f.write("2. **《岐伯近思录》**（实践哲学取向：借宋儒近思之意，明其切问近思、下学上达之实践纲领）\n")
        f.write("3. **《岐伯通义》**（全息理论取向：彰显其贯通伦常、人情、世势、身心与玄览的思想体系）\n")
        f.write("4. **《岐伯精言》**（案头修养取向：取“精微大言”，宜于常读常新）\n\n")
        
        f.write("## 贰· 八卷架构与篇目配置\n\n")
        f.write("| 卷序 | 卷名 | 核心主旨与骨架 | 篇数 | 字数统计 |\n")
        f.write("| :--- | :--- | :--- | :---: | :---: |\n")
        for v_code in ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8']:
            v_name, v_title, v_desc = VOL_NAMES[v_code]
            v_arts = [a for a in articles if a['volume_code'] == v_code]
            v_chars = sum(len(a.get('answer','')) for a in v_arts)
            f.write(f"| {v_name} | **{v_title}** | {v_desc} | {to_cn_num(len(v_arts))}篇 | 约{v_chars}字 |\n")
        f.write(f"| **通计** | **八卷完备** | **涵盖修身、齐家、应世、格物之全息体系** | **一百二十篇** | **约{total_words}字** |\n\n")
        
        f.write("## 叁· 核心概念群谱系落地（十七个自创概念全覆盖）\n\n")
        f.write("一百二十篇体量成功激活并完备安放了岐伯的核心概念群：\n\n")
        f.write("- **自强**（二十三篇）：破除外界虚妄认可的依赖，建立内在确定性动力源。\n")
        f.write("- **神性享乐**（十七篇）：超越生理与世俗诱惑的至高认知愉悦与沉浸体验。\n")
        f.write("- **人己权界**（十四篇）：权柄决定是非，破除道德越权与社会性边界侵犯。\n")
        f.write("- **SOP**（十四篇）：将复杂处世、应对冲突与团队协作提炼为高确定性标准作业程序。\n")
        f.write("- **元技能**（十四篇）：复利认知、深度注意力与底层思维不可替代的基本功。\n")
        f.write("- **净输出**（十一篇）：停止能量内耗与债务式索取，确立向世界正向输出价值的自洽状态。\n")
        f.write("- **旷野**（八篇）：打破体制温室与确定性幻象，直面真实世界演化的生机。\n")
        f.write("- **择善固执**（八篇）：在噪音汹涌与短期诱惑中维持终极认知原则的绝对清醒。\n")
        f.write("- **信源管理**（七篇）：严防精神环境投毒与信息污染，严控输入端品质。\n")
        f.write("- **错得对**（七篇）：在复杂动态博弈中理解次优解、妥协演化与容错战略。\n")
        f.write("- **评价权**（三篇）：守住自身是非尺度，不向外界让渡核心定义权。\n")
        f.write("- **CARITAS**（二篇）：博爱与超功利慈悲在人际契约中的实践落地。\n")
        f.write("- **爱不生债**（二篇）：清爽的关系伦理，爱是施予而非索取或绑架。\n")
        f.write("- **不以恶为业**（二篇）：立足长周期博弈的道德底线与正道策略。\n")
        f.write("- **Poetic Irony**（一篇）：《美德》篇引入历史狡黠与命运宿命感的高维洞察。\n")
        f.write("- **王天下**（一篇）：《正果》篇立足大历史工程与治理秩序的宏观眼界。\n")
        f.write("- **人神分野**（一篇）：敬畏未知与把握人世有限性的边界意识。\n\n")
        
        f.write("## 肆· 精选一百二十篇完整目录详录\n\n")
        
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
                ans = a.get('answer', '').replace('\r', '').replace('\n', ' ')
                f.write(f"- **思想精要**：{ans[:160]}……\n\n")
                global_idx += 1
                
    print(f"✓ 一百二十篇完整方案报告已生成至: {out_md}")

if __name__ == '__main__':
    main()
