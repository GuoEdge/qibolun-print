#!/usr/bin/env python3
"""Record Round136 visual review without upgrading provisional classifications."""
from __future__ import annotations
import csv, json
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"

def read(path: Path, delimiter=","):
    with path.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh, delimiter=delimiter))
def write(path: Path, fields, rows, delimiter=","):
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, delimiter=delimiter, extrasaction="ignore")
        w.writeheader(); w.writerows(rows)
    tmp.replace(path)

ARTICLE = {
    "16336056-5d08-5336-a475-bd28c6049c98": ("褐底金色竖排汉文/佛经样书页，带边框与印章", "图片显示书法/古籍视觉对象，与正文的书写和文化语境相关，但具体文本、版本和作者未核验。", "limited"),
    "c8b9d495-94a6-5c22-9dd7-770512e3e82e": ("睡眠者佩戴鼻面罩，旁有呼吸机设备", "图片直接显示睡眠呼吸设备，与正文关于打鼾和呼吸机的场景相符；不能证明诊断、效果或设备型号。", "consistent"),
    "0b17f32e-e171-5888-9b3d-d5b1c7d3dca9": ("穿白大褂并挂听诊器的男性医生肖像", "图片提供医生/医疗场景的通用视觉语境，但不能确认人物身份或正文医学判断。", "limited"),
    "00720a35-c252-57cc-9fcf-5ab697528746": ("山地盘山公路航拍图", "图片显示道路与地形环境，和正文涉及驾驶/道路场景有弱关联，但不能证明科目二训练事实。", "limited"),
    "dbd7bab9-d695-5e8a-96b9-49ce7510e790": ("带有强烈肖像风格的老人面部图像", "图片提供人物肖像和社会观察语境，不能单独证明正文关于‘俗’的概念判断。", "limited"),
    "a987e3e4-b6ad-54eb-8d0f-7dc87db5091d": ("窄长手机/网页截图，含大量缩略图和文字", "图片仅能确认信息截图和界面排布；未作OCR，无法据此核实正文引用。", "inconclusive"),
    "2d127a86-0787-59e0-9ad0-36940d65f94e": ("蓝色矿物、宗教建筑、宗教/母子绘画、蓝色花卉与器物等文化图像", "图片共同呈现蓝色与宗教、艺术、器物语境，能支持正文的视觉联想，但来源、年代和具体对象未核验。", "limited"),
    "da098d20-c643-5f18-a4ae-2fd637101811": ("台湾教育字体网页截图及韩国铁路字体说明/站牌截图", "图片直接显示字体网页、字符说明和铁路标牌，与正文的字体与公共文化对象相关；网页文字未作OCR或来源核验。", "consistent"),
    "0db27234-3f9b-52e8-a594-f5e3de3e9d39": ("动物眼部特写、观测设施、驴/猫、头骨及其他自然图像", "图片提供动物视觉、面部或生态对象的视觉材料，与正文方向相关，但混合素材不能证明演化或行为因果。", "limited"),
    "5af12600-8940-5fe3-8831-96c4c4ae285d": ("手绘线条、点阵和箭头组成的流程/碰撞示意图", "图片能显示示意图结构，与正文的过程/机制解释有形式关联，但不验证模型或工程结论。", "limited"),
    "e07ef7cd-dbd2-571f-b8d0-39b3970e5f9a": ("电影场景截图，人物对话并带中文字幕", "图片支持戏剧/演员和命定主题的影视语境，但字幕未作OCR，人物、影片及物理/神学含义未核验。", "limited"),
    "b42bc4ae-a485-58f5-96b5-cb4efc1bcdef": ("经过变形或对比处理的蒙娜丽莎肖像图", "图片支持视觉变形/表情比较的艺术语境，与正文的‘不动’概念有弱关联，但不能证明审美或心理结论。", "limited"),
    "9b2b249b-2528-59da-9898-3e18a450a6d0": ("现代书法作品与竖幅手写文字图", "图片直接显示书法和手写实践，与正文的书写艺术讨论相符；作者、字帖和书法史归属未核验。", "consistent"),
    "23791905-d312-5396-81b0-0749eac16494": ("计算机生成的复杂结构模型与金属增材制造成品", "图片直接显示增材制造/复杂结构对象，与正文制造工程主题相符；工艺参数、性能和成本未核验。", "consistent"),
}

def main():
    manifest_path = REPORTS / "round136-image-manifest.csv"
    manifest = read(manifest_path)
    assert len(manifest) == 41 and all(r.get("download_status") == "success" for r in manifest)
    review = []
    today = date.today().isoformat()
    for row in manifest:
        aid = row["id"]
        visible, relation, consistency = ARTICLE[aid]
        review.append({
            "ordinal": row.get("ordinal", ""), "id": aid, "title": row["title"], "image_index": row["image_index"],
            "local_file": row["local_file"], "download_status": row["download_status"],
            "visible_content": visible, "relation_to_text": relation, "changes_topic_judgment": "no",
            "image_text_consistency": consistency,
            "limitations": "仅记录可见对象与图文关系；图片来源、时间、人物/作品身份及正文外部事实未独立核验；图片不能替代OCR、史实、医学、法律、工程或安全核验。",
            "review_status": "reviewed", "review_date": today, "ocr_status": "not_started",
        })
        row["status"] = "reviewed"
        row["notes"] = f"{visible}；图文关系：{relation}；限制：图片来源与OCR未核验。"
    write(REPORTS / "round136-image-review.tsv", list(review[0]), review, "\t")
    write(manifest_path, list(manifest[0]), manifest)

    # Close the stale 108-113/116b manifest rows that Round136 reconciled.
    reviewed_keys = {(r["id"], r["image_index"], r["src"]) for r in manifest}
    for path in REPORTS.glob("round*-image-manifest*.csv"):
        if path.name == "round136-image-manifest.csv": continue
        fields = None; rows = read(path)
        changed = False
        for row in rows:
            key = (row.get("id", ""), row.get("image_index", ""), row.get("src", ""))
            if key in reviewed_keys and row.get("status") != "reviewed":
                row["status"] = "reviewed"
                row["notes"] = "Round136 reconciliation visual review; original unreviewed manifest closed."
                changed = True
        if changed: write(path, list(rows[0]), rows)

    inventory_fields = None; inventory = read(DATA / "image-inventory.csv")
    by_key = {(r["id"], r["image_index"]): r for r in review}
    for row in inventory:
        item = by_key.get((row.get("id", ""), row.get("image_index", "")))
        if item:
            row["status"] = "reviewed"
            row["notes"] = f"{item['visible_content']}；{item['relation_to_text']}；专题改变=no；限制：{item['limitations']}；视觉复核完成，OCR未核验。"
    write(DATA / "image-inventory.csv", list(inventory[0]), inventory)

    manual_fields, manual = None, read(DATA / "print-topic-manual-decisions-v2.csv")
    ids = {r["id"] for r in manifest}
    groups = defaultdict(list)
    for r in review: groups[r["id"]].append(r)
    for row in manual:
        if row.get("id") not in ids: continue
        aid = row["id"]
        row["review_note"] = row.get("review_note", "").rstrip("; ") + f"; Round136 visual review=reports/round136-image-review.tsv ({len(groups[aid])}/{len(groups[aid])} images; no topic change); image limitations recorded; OCR and factual claims remain unverified."
        if "image-review" not in row.get("reviewer", ""): row["reviewer"] = (row.get("reviewer", "main-thread") + "+image-review").strip("+")
    write(DATA / "print-topic-manual-decisions-v2.csv", list(manual[0]), manual)

    decisions = []
    for aid, items in groups.items():
        row = next(r for r in manual if r["id"] == aid)
        decisions.append({"id": aid, "title": row["title"], "primary_before": row["primary_print_topic_code"], "secondary_before": row["secondary_print_topic_codes"], "primary_after": row["primary_print_topic_code"], "secondary_after": row["secondary_print_topic_codes"], "primary_changed": "no", "secondary_changed": "no", "final_status": row["classification_status"], "decision": "retain_body_classification_image_reviewed", "basis": "Round136 visual review records visible context only; image evidence does not independently verify claims or justify a topic change.", "reason": "The article remains provisional because source/claim or body-length boundaries remain after image review."})
    write(REPORTS / "round136-image-decisions.tsv", list(decisions[0]), decisions, "\t")
    print(json.dumps({"round":136,"articles":len(groups),"images":len(review),"reviewed":len(review),"topic_changes":0,"status_promotions":0,"consistency_counts":{k:sum(r["image_text_consistency"]==k for r in review) for k in ("consistent","limited","inconclusive")}}, ensure_ascii=False, indent=2))

if __name__ == "__main__": main()
