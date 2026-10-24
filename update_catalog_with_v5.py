#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""将v5新增7篇文章追加到catalog"""
import json
from pathlib import Path

ROOT = Path("/storage/Users/currentUser/Documents/岐伯论")
CATALOG_V4 = ROOT / "research-rebuild/reports/gemini-flash-reclassification-v1/workbook-40b-all-catalog-v4.jsonl"
V5_ASSIGNMENT = ROOT / "v5_increment_final_assignment.json"
V5_ARTICLES = ROOT / "sooon-q9adg-articles-v5.jsonl"
OUTPUT_V5 = ROOT / "research-rebuild/reports/gemini-flash-reclassification-v1/workbook-40b-all-catalog-v5.jsonl"
BACKUP = ROOT / "research-rebuild/reports/gemini-flash-reclassification-v1/workbook-40b-all-catalog-v4.jsonl.backup-20261010"

METADATA_TEMPLATE = {
    "B04": {
        "volume_code": "V1",
        "booklet_name": "亲子沟通与青春叛逆",
        "volume_prefix": "本根敦倫",
        "volume_full_title": "本根敦倫——血亲宗族与家庭抚育",
        "booklet_stem": "丁",
        "booklet_stem_title": "丁冊 亲子沟通与青春叛逆",
        "full_citation": "本根敦倫 · 丁冊 亲子沟通与青春叛逆"
    },
    "B20A": {
        "volume_code": "V5",
        "booklet_name": "职场汇报与权责留痕·上册",
        "volume_prefix": "度势居货",
        "volume_full_title": "度势居货——职场生态与财富经营",
        "booklet_stem": "甲·上",
        "booklet_stem_title": "甲冊 职场汇报与权责留痕·上册",
        "full_citation": "度势居货 · 甲冊 职场汇报与权责留痕·上册"
    },
    "B24": {
        "volume_code": "V6",
        "booklet_name": "青年心境与躺平反思",
        "volume_prefix": "观风察变",
        "volume_full_title": "观风察变——时代透视与群体思潮",
        "booklet_stem": "乙",
        "booklet_stem_title": "乙冊 青年心境与躺平反思",
        "full_citation": "观风察变 · 乙冊 青年心境与躺平反思"
    },
    "B28": {
        "volume_code": "V6",
        "booklet_name": "消费主义与生活观念",
        "volume_prefix": "观风察变",
        "volume_full_title": "观风察变——时代透视与群体思潮",
        "booklet_stem": "己",
        "booklet_stem_title": "己冊 消费主义与生活观念",
        "full_citation": "观风察变 · 己冊 消费主义与生活观念"
    },
    "B30": {
        "volume_code": "V6",
        "booklet_name": "文明演进与社会秩序",
        "volume_prefix": "观风察变",
        "volume_full_title": "观风察变——时代透视与群体思潮",
        "booklet_stem": "辛",
        "booklet_stem_title": "辛冊 文明演进与社会秩序",
        "full_citation": "观风察变 · 辛冊 文明演进与社会秩序"
    },
    "B39": {
        "volume_code": "V8",
        "booklet_name": "艺能创作与生活美学",
        "volume_prefix": "鉴往铸器",
        "volume_full_title": "鉴往铸器——艺文美学与历史治乱",
        "booklet_stem": "甲",
        "booklet_stem_title": "甲冊 艺能创作与生活美学",
        "full_citation": "鉴往铸器 · 甲冊 艺能创作与生活美学"
    },
    "B40": {
        "volume_code": "V8",
        "booklet_name": "治乱兴亡与国家工程",
        "volume_prefix": "鉴往铸器",
        "volume_full_title": "鉴往铸器——艺文美学与历史治乱",
        "booklet_stem": "乙",
        "booklet_stem_title": "乙冊 治乱兴亡与国家工程",
        "full_citation": "鉴往铸器 · 乙冊 治乱兴亡与国家工程"
    }
}

def main():
    print(f"备份 v4 catalog 到：{BACKUP.name}")
    import shutil
    shutil.copy(CATALOG_V4, BACKUP)
    
    existing_entries = []
    max_ordinal = 0
    existing_ids = set()
    
    with CATALOG_V4.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                entry = json.loads(line)
                existing_entries.append(entry)
                max_ordinal = max(max_ordinal, entry.get("workbook_ordinal", 0))
                existing_ids.add(entry.get("original_id") or entry.get("article_id"))
                
    print(f"现有 catalog-v4: {len(existing_entries)} 条记录，最大序号: {max_ordinal}")
    
    with V5_ASSIGNMENT.open("r", encoding="utf-8") as f:
        v5_assignments = json.load(f)
        
    v5_articles = {}
    with V5_ARTICLES.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                article = json.loads(line)
                v5_articles[str(article["id"])] = article
                
    new_entries = []
    next_ordinal = max_ordinal + 1
    
    for item in v5_assignments:
        article_id = item["article_id"]
        if article_id in existing_ids:
            print(f"  跳过已存在: {item['title']}")
            continue
            
        article = v5_articles[article_id]
        booklet_code = item["booklet_code"]
        meta = METADATA_TEMPLATE[booklet_code]
        
        question = article.get("question", "")
        if not question and "lexical" in article and article["lexical"]:
            try:
                lexical_data = json.loads(article["lexical"]) if isinstance(article["lexical"], str) else article["lexical"]
                root = lexical_data.get("root", {})
                children = root.get("children", [])
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
                
        text = article.get("text", "")
        text_preview = text[:200] if len(text) > 200 else text
        
        entry = {
            "workbook_ordinal": next_ordinal,
            "original_id": article_id,
            "title": article["title"],
            "published_at": article["publishedAt"],
            "question": question,
            "volume_code": meta["volume_code"],
            "booklet_code": booklet_code,
            "booklet_name": meta["booklet_name"],
            "text_len": len(text),
            "text_preview": text_preview,
            "volume_prefix": meta["volume_prefix"],
            "volume_full_title": meta["volume_full_title"],
            "booklet_stem": meta["booklet_stem"],
            "booklet_stem_title": meta["booklet_stem_title"],
            "full_citation": meta["full_citation"],
            "url": article["url"],
            "article_url": article["url"]
        }
        
        new_entries.append(entry)
        next_ordinal += 1
        print(f"  +{entry['workbook_ordinal']:4d} {entry['title']:20s} → {booklet_code} {meta['booklet_name']}")
        
    # 同时覆盖原 catalog 路径与生成 v5
    with OUTPUT_V5.open("w", encoding="utf-8") as f:
        for entry in existing_entries:
            f.write(json.dumps(entry, ensure_ascii=False, separators=(',', ':')) + "\n")
        for entry in new_entries:
            f.write(json.dumps(entry, ensure_ascii=False, separators=(',', ':')) + "\n")
            
    with CATALOG_V4.open("w", encoding="utf-8") as f:
        for entry in existing_entries:
            f.write(json.dumps(entry, ensure_ascii=False, separators=(',', ':')) + "\n")
        for entry in new_entries:
            f.write(json.dumps(entry, ensure_ascii=False, separators=(',', ':')) + "\n")

    print(f"\n✓ 新 catalog 已生成：{OUTPUT_V5.name} 与 {CATALOG_V4.name}")
    print(f"  原有: {len(existing_entries)} 条")
    print(f"  新增: {len(new_entries)} 条")
    print(f"  总计: {len(existing_entries) + len(new_entries)} 条")

if __name__ == "__main__":
    main()
