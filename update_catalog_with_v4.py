#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""将v4新增29篇文章追加到catalog"""
import json
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).parent
CATALOG = ROOT / "research-rebuild/reports/gemini-flash-reclassification-v1/workbook-40b-all-catalog.jsonl"
V4_ASSIGNMENT = ROOT / "v4_increment_final_assignment_2026-10-09.jsonl"
V4_ARTICLES = ROOT / "sooon-q9adg-articles-v4.jsonl"
OUTPUT = ROOT / "research-rebuild/reports/gemini-flash-reclassification-v1/workbook-40b-all-catalog-v4.jsonl"
BACKUP = ROOT / "research-rebuild/reports/gemini-flash-reclassification-v1/workbook-40b-all-catalog.jsonl.backup-20261009"

# 卷信息
VOLUME_INFO = {
    "V1": {"prefix": "本根敦倫", "full_title": "本根敦倫——血亲宗族与家庭抚育"},
    "V2": {"prefix": "阴阳合离", "full_title": "阴阳合离——两性亲密与婚恋博弈"},
    "V3": {"prefix": "酬酢防身", "full_title": "酬酢防身——人际交往与危机应对"},
    "V4": {"prefix": "存神调息", "full_title": "存神调息——身心安顿与心性知行"},
    "V5": {"prefix": "度势居货", "full_title": "度势居货——职场生态与财富经营"},
    "V6": {"prefix": "观风察变", "full_title": "观风察变——时代透视与群体思潮"},
    "V7": {"prefix": "涤除玄览", "full_title": "涤除玄览——深层哲思与名相辨析"},
    "V8": {"prefix": "鉴往铸器", "full_title": "鉴往铸器——艺文美学与历史治乱"}
}

# 册天干映射
BOOKLET_STEM = {
    "B01": ("甲", "甲冊 艺能创作与生活美学"),
    "B02": ("乙", "乙冊 史鉴借镜与历史解读"),
    "B03": ("甲", "甲冊 言传身教与奖惩边界"),
    "B04": ("乙", "乙冊 亲子沟通与青春叛逆"),
    "B05": ("丙", "丙冊 父母控制欲与精神解绑"),
    "B06": ("丁", "丁冊 成年子女自立与边界"),
    "B07": ("戊", "戊冊 原生家庭创伤与和解"),
    "B08": ("己", "己冊 病老照护与养老反哺"),
    "B09": ("庚", "庚冊 兄弟姐妹与族亲疏近"),
    "B10": ("癸", "癸冊 临终关怀与白事奠仪"),
    "B11": ("甲", "甲冊 恋爱选择与求偶焦虑"),
    "B12": ("乙", "乙冊 婚姻存续与夫妻日常"),
    "B13": ("丙", "丙冊 婚姻危机与修复离异"),
    "B14": ("丁", "丁冊 出轨背叛与信任重建"),
    "B15": ("甲", "甲冊 社交距离与孤立自处"),
    "B16": ("乙", "乙冊 友谊维系与利益权衡"),
    "B17": ("甲", "甲冊 情志平复与容貌自和"),
    "B18": ("乙", "乙冊 作息节律与病理常识"),
    "B19": ("丙", "丙冊 知行精进与克服拖延"),
    "B20A": ("甲", "甲冊 职场汇报与权责留痕"),
    "B20B": ("乙", "乙冊 职场竞争与人际政治"),
    "B21": ("丙", "丙冊 求职择业与生涯规划"),
    "B22": ("丁", "丁冊 商业竞争与资产投资"),
    "B23": ("甲", "甲冊 公共热点与事件剖析"),
    "B24": ("乙", "乙冊 青年心境与躺平反思"),
    "B25": ("丙", "丙冊 农民工群体与阶层流动"),
    "B26": ("丁", "丁冊 性别议题与两性舆论"),
    "B27": ("戊", "戊冊 教育体制与社会流动"),
    "B28": ("己", "己冊 消费主义与生活观念"),
    "B29": ("庚", "庚冊 现代科技与工具反思"),
    "B30": ("辛", "辛冊 文明演进与社会秩序"),
    "B31": ("壬", "壬冊 传统文化与宗教信仰"),
    "B32": ("甲", "甲冊 名相辨析与语言牢笼"),
    "B33": ("乙", "乙冊 逻辑推理与思辨方法"),
    "B34": ("丙", "丙冊 认识局限与心智模型"),
    "B35": ("丁", "丁冊 伦理困境与价值选择"),
    "B36": ("戊", "戊冊 人生意义与生存哲学"),
    "B37": ("己", "己冊 历史规律与未来预判"),
    "B38": ("庚", "庚冊 AI交互与提问技巧"),
    "B39": ("辛", "辛冊 知乎社区与内容生态")
}

def main():
    # 备份原catalog
    print(f"备份原catalog到：{BACKUP.name}")
    import shutil
    shutil.copy(CATALOG, BACKUP)
    
    # 加载现有catalog
    existing_entries = []
    max_ordinal = 0
    existing_ids = set()
    
    with CATALOG.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                entry = json.loads(line)
                existing_entries.append(entry)
                max_ordinal = max(max_ordinal, entry["workbook_ordinal"])
                existing_ids.add(entry["original_id"])
    
    print(f"现有catalog: {len(existing_entries)}条记录，最大序号: {max_ordinal}")
    
    # 加载v4分配信息
    v4_assignments = {}
    with V4_ASSIGNMENT.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                item = json.loads(line)
                v4_assignments[item["article_id"]] = item
    
    # 加载v4文章全文
    v4_articles = {}
    with V4_ARTICLES.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                article = json.loads(line)
                v4_articles[article["id"]] = article
    
    # 生成新条目
    new_entries = []
    next_ordinal = max_ordinal + 1
    
    for article_id, assignment in v4_assignments.items():
        if article_id in existing_ids:
            print(f"  跳过已存在: {assignment['title']}")
            continue
        
        article = v4_articles[article_id]
        booklet_code = assignment["booklet_code"]
        volume_code = assignment["volume_code"]
        
        # 获取question字段（如果有）
        question = ""
        if "lexical" in article and article["lexical"]:
            try:
                lexical_data = json.loads(article["lexical"])
                root = lexical_data.get("root", {})
                children = root.get("children", [])
                
                # 查找第一个quote块
                for child in children:
                    if child.get("type") == "quote":
                        quote_children = child.get("children", [])
                        quote_text = []
                        for qc in quote_children:
                            if qc.get("type") == "text":
                                quote_text.append(qc.get("text", ""))
                            elif qc.get("type") == "paragraph":
                                para_children = qc.get("children", [])
                                for pc in para_children:
                                    if pc.get("type") in ["text", "p-text"]:
                                        quote_text.append(pc.get("text", ""))
                        question = "".join(quote_text).strip()
                        break
            except:
                pass
        
        # 构建catalog条目
        text = article.get("text", "")
        text_preview = text[:200] if len(text) > 200 else text
        
        volume_info = VOLUME_INFO[volume_code]
        booklet_stem, booklet_stem_title = BOOKLET_STEM[booklet_code]
        
        entry = {
            "workbook_ordinal": next_ordinal,
            "original_id": article_id,
            "title": article["title"],
            "published_at": article["publishedAt"],
            "question": question,
            "volume_code": volume_code,
            "booklet_code": booklet_code,
            "booklet_name": assignment["booklet_name"],
            "text_len": len(text),
            "text_preview": text_preview,
            "volume_prefix": volume_info["prefix"],
            "volume_full_title": volume_info["full_title"],
            "booklet_stem": booklet_stem,
            "booklet_stem_title": booklet_stem_title,
            "full_citation": f"{volume_info['prefix']} · {booklet_stem_title}",
            "url": article["url"],
            "article_url": article["url"]
        }
        
        new_entries.append(entry)
        next_ordinal += 1
        print(f"  +{entry['workbook_ordinal']:4d} {entry['title']:20s} → {booklet_code} {assignment['booklet_name']}")
    
    # 写入新catalog
    with OUTPUT.open("w", encoding="utf-8") as f:
        # 写入原有条目
        for entry in existing_entries:
            f.write(json.dumps(entry, ensure_ascii=False, separators=(',', ':')) + "\n")
        # 写入新条目
        for entry in new_entries:
            f.write(json.dumps(entry, ensure_ascii=False, separators=(',', ':')) + "\n")
    
    print(f"\n✓ 新catalog已生成：{OUTPUT.name}")
    print(f"  原有: {len(existing_entries)}条")
    print(f"  新增: {len(new_entries)}条")
    print(f"  总计: {len(existing_entries) + len(new_entries)}条")
    
    # 统计新增文章的册分布
    from collections import Counter
    booklet_counter = Counter(e["booklet_code"] for e in new_entries)
    print(f"\n新增文章册分布:")
    for booklet in sorted(booklet_counter.keys()):
        entry = next(e for e in new_entries if e["booklet_code"] == booklet)
        print(f"  {booklet} {entry['booklet_name']}: {booklet_counter[booklet]}篇")

if __name__ == "__main__":
    main()
