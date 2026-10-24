#!/usr/bin/env python3
"""Write Round120 visual-review TSV and decision report only.

This records conservative visual observations. It does not OCR, authenticate
sources, or modify the canonical image inventory/manual classification table.
"""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
MANIFEST = REPORTS / "round120-image-manifest.csv"
REVIEW = REPORTS / "round120-image-review.tsv"
DECISIONS = REPORTS / "round120-decisions.tsv"

COMMON = "图片来源、时间、人物/地点身份及外部事实未独立核验；图像不能单独证明正文之外的历史、因果或制度结论。"

DATA: dict[str, list[tuple[str, str, str]]] = {
    "96d836cb-4559-5c94-82b9-51adca67267f": [
        ("宫殿拱廊前身穿蓝黄条纹制服、戴帽并持礼仪姿态的人物。", "对应正文以制服颜色、剪裁和礼仪服饰讨论军服的身份标识与仪式功能。", "consistent"),
        ("多名身穿蓝黄红相间制服、戴金属头盔和羽饰的仪仗/骑兵队列。", "支持正文比较军服配色、头盔装饰和集体仪仗形象。", "consistent"),
        ("雨中建筑门口身穿黑色长外衣、彩色长袜和帽子的制服人物。", "对应正文讨论不同机构制服的款式、颜色和场合差异。", "limited"),
        ("骑马仪仗人物身穿黑金红礼服和羽饰头盔，背景为列队人员。", "直接对应正文关于军服等级、骑兵仪式与视觉权威的材料。", "consistent"),
        ("室内长廊中一列身穿黑金制服、红色羽饰头盔的仪仗人员。", "支持正文说明制服在队列、典礼和纪律秩序中的统一效果。", "consistent"),
        ("石质建筑门廊旁两名穿黑色礼服、红羽饰头盔的卫兵。", "对应正文比较卫兵制服的颜色、武装配件和建筑场景。", "limited"),
        ("城市街道上两名身穿黑色制服、白色帽子和肩带的警察。", "支持正文把军服、警服与现代国家机构身份标识联系起来。", "limited"),
        ("两名穿黑色制服、黑色斗篷及红色内衬的礼仪人员走在城市街道。", "对应正文关于斗篷、披肩等外覆服饰如何强化仪式性与等级感的讨论。", "consistent"),
        ("建筑门前两名相同黑色斗篷制服人员，佩戴白色肩带和帽徽。", "支持正文分析制服标准化、成对出现及公共仪式形象。", "limited"),
        ("身穿红色礼仪制服、白色长裤和黑色头盔的两名人员。", "对应正文比较鲜明配色、礼仪队列与制服可识别性。", "consistent"),
        ("身穿黑色军礼服、红色披风和金色装饰的高级仪仗人物，行走于队列中。", "直接对应正文关于高级军官礼服、披风和等级装饰的视觉材料。", "consistent"),
        ("骑黑马的军装人物，穿黑色礼服、红色羽饰头盔并持缰。", "支持正文说明骑兵服饰、武装身份和仪仗功能的结合。", "limited"),
        ("室内肖像中的年长军官，穿深色礼服、佩勋章和蓝红肩带。", "对应正文讨论勋章、肩带、佩饰与军衔等级的关系。", "consistent"),
        ("身穿深色海军式礼服、戴白帽并佩戴勋章的军官。", "支持正文比较海陆军制服的剪裁、帽饰和勋章系统。", "limited"),
        ("多名骑兵/仪仗人员穿红黑礼服、戴高帽并列队行进。", "对应正文关于队列一致性、礼仪服和传统制服延续的例证。", "consistent"),
        ("身穿深蓝军礼服、戴白帽、佩勋章和肩带的军官肖像。", "支持正文说明制服配件和勋章如何传达身份与等级。", "limited"),
        ("近景中身穿深色礼服、佩蓝色肩带和多枚勋章的高级军官。", "对应正文关于礼服细节、勋章密度和权力象征的讨论。", "consistent"),
        ("平铺展示的灰色德式军装上衣，带领章、肩绳、纽扣和腰带。", "直接对应正文比较军装剪裁、徽章、肩绳等结构性部件。", "consistent"),
        ("平铺展示的灰褐色军装上衣，红色领章和袖口装饰清晰。", "支持正文分析颜色、领章和袖口在制服识别中的作用。", "consistent"),
        ("历史制服、皮靴和帽子平铺图，帽徽/臂章含纳粹标志。", "对应正文讨论制服与政治组织、历史权力符号的联系；不据此扩展历史事实。", "limited"),
        ("户外列队的深色军装人员，制服和帽饰形成重复的纵向队列。", "支持正文关于统一制服、队列纪律和集体视觉效果的说明。", "limited"),
        ("黑白高对比的人物军装肖像，白色帽檐和领口突出。", "对应正文以照片材料比较制服轮廓、色块和人物识别效果。", "limited"),
        ("身穿深蓝制服、戴白帽并持步枪的仪仗/军警人物。", "直接对应正文把制服、武器携带和仪仗身份放在同一视觉语境中。", "consistent"),
    ],
    "fe1e993d-7c2c-5c0f-b734-2bb88c4cae89": [
        ("九宫格田地示意图，中央黄色方格标‘公田’，周围蓝色方格标‘私田’，并标注百步、百亩和一里。", "直接对应正文介绍井田制九宫格模式、私田公田比例和尺度单位。", "consistent"),
        ("红色线框绘制的九块梯形/方形田地三维或平面示意。", "支持正文讨论井田分块、方整规划及其空间模型。", "consistent"),
        ("手绘剖面示意，含不同深度百分比、作物根系和地下水位标线。", "对应正文把土地、灌溉或耕作条件纳入井田空间与农业生产讨论。", "limited"),
        ("‘金文、小篆、楷书’等不同字体中的‘束/未’字形对照图。", "支持正文从文字形体与‘井田’概念字源、字形演变展开论证。", "consistent"),
        ("古文字‘未’字及字形演变说明图，旁有农具/树木形态解释。", "对应正文讨论古文字形体、字义和农业语境的材料。", "limited"),
        ("黑白线描的袋状或容器形物件，顶部有方形孔/标记。", "与正文井田制度论证的对应关系不直接，保留为原文附图，不据此改变专题。", "inconclusive"),
        ("碗中盛有颗粒状谷物或米饭，置于布料上。", "可作为正文农业、谷物和土地生产语境的辅助图，但不能证明制度史断言。", "limited"),
        ("卫星/航拍地图中的山地梯田或沟谷，黄色箭头指向多处地块。", "对应正文把现实地形、地块形态与井田空间模型进行比较的地理材料。", "limited"),
        ("白底手绘多条红蓝曲线，表现河流、沟渠或地块边界的分支走向。", "支持正文讨论田块边界、水系和农业空间组织的抽象示意。", "limited"),
        ("城市住宅区草地与树木照片，底部有粉色箭头和图片来源水印。", "与井田制度的历史论证对应关系弱，可能仅作方格/规划类比的附图语境。", "inconclusive"),
        ("航拍河流与农田，河道在深色土地之间呈弯曲带状。", "对应正文讨论自然水系、地形与土地分配空间的比较材料。", "limited"),
        ("航拍绿色平原和弯曲河网，农田条带沿水系展开。", "支持正文对农业地理、灌溉和田块形态的空间说明。", "limited"),
        ("航拍河流穿过绿色农田和湿地，河道与地块边界交错。", "对应正文把现实农业景观与井田模型的规则分块进行对照。", "limited"),
        ("与第1图相同的九宫格‘私田/公田’示意图，中央为黄色公田；本批次中 src 与第1图重复。", "直接重复正文关于井田九宫格、面积和公私田布局的说明；作为重复源图单独记账，不视为新增独立图像证据。", "consistent"),
        ("航拍褐色地块与浅色河道交错的农业景观。", "支持正文关于地形、水系和土地制度空间假设的地理语境。", "limited"),
        ("文章正文截图，讨论20世纪80年代以来井田制否定论、学术质量与研究进展。", "直接对应正文的学术史综述段落，图像是文章自身文字材料而非外部证据。", "consistent"),
        ("文章正文截图，引用胡寄窗、赵世超、李曦等学者对井田模式与历史条件的不同看法。", "直接对应正文关于学术争论、文献证据和理论解释差异的论述。", "consistent"),
        ("文章正文截图，讨论井田是否为现实土地制度、孟子构想及战国秦汉材料。", "直接对应正文的史料批判与制度实在性辨析。", "consistent"),
        ("文章正文截图，引用袁林、史建群等学者关于‘井’字形状、授田制与井田制关系的观点。", "对应正文比较字形、文献记载和授田制度的论证链。", "consistent"),
        ("文章正文截图，讨论井田与井田制名实之辨、概念混淆和学术命题。", "直接对应正文结论部分关于概念界定与方法反思的内容。", "consistent"),
        ("文章正文截图，结论认为持续清理20世纪以来研究、吸收新材料有助于接近历史真相。", "直接对应正文结尾的研究方法与谨慎结论；截图不能替代原始文献核验。", "consistent"),
    ],
}


def read_csv(path: Path, delimiter: str = ",") -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh, delimiter=delimiter)
        return list(reader.fieldnames or []), list(reader)


def main() -> None:
    _, manifest = read_csv(MANIFEST)
    assert len(manifest) == 44, len(manifest)
    assert all(r.get("download_status") == "success" for r in manifest)
    expected = {(aid, str(i)) for aid, values in DATA.items() for i in range(1, len(values) + 1)}
    actual = {(r["id"], r["image_index"]) for r in manifest}
    assert actual == expected, (len(actual), len(expected), sorted(expected - actual))

    # Explicitly verify no selected article occurs in earlier image manifests.
    prior_ids: set[str] = set()
    for path in REPORTS.glob("round*-image-manifest*.csv"):
        if path.name == "round120-image-manifest.csv":
            continue
        _, rows = read_csv(path)
        prior_ids.update(r.get("id", "") for r in rows)
    assert not (set(DATA) & prior_ids), sorted(set(DATA) & prior_ids)

    fields = ["ordinal", "id", "title", "image_index", "local_file", "download_status", "visible_content", "relation_to_text", "changes_topic_judgment", "image_text_consistency", "limitations", "review_status", "review_date"]
    out: list[dict[str, str]] = []
    for row in manifest:
        visible, relation, consistency = DATA[row["id"]][int(row["image_index"]) - 1]
        out.append({**{k: row.get(k, "") for k in fields}, "visible_content": visible, "relation_to_text": relation, "changes_topic_judgment": "no", "image_text_consistency": consistency, "limitations": COMMON, "review_status": "reviewed", "review_date": "2026-09-24"})
    with REVIEW.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, delimiter="\t", extrasaction="ignore")
        writer.writeheader(); writer.writerows(out)

    manual_path = ROOT / "research-rebuild/data/print-topic-manual-decisions-v2.csv"
    _, manual_rows = read_csv(manual_path)
    manual = {r["id"]: r for r in manual_rows}
    decisions = []
    for aid, values in DATA.items():
        rows = [r for r in out if r["id"] == aid]
        m = manual[aid]
        visible = "；".join(dict.fromkeys(r["visible_content"] for r in rows))
        relation = "；".join(dict.fromkeys(r["relation_to_text"] for r in rows))
        decisions.append({"id": aid, "title": m["title"], "primary": m["primary_print_topic_code"], "secondary": m["secondary_print_topic_codes"], "status": m["classification_status"], "recommendation": "retain_confirmed; image review completed; no topic change", "basis": m["decision_basis"], "risk_note": f"Round120 image review {len(rows)}/{len(rows)}; changes_topic_judgment=no; visible={visible}; relation={relation}; {COMMON}"})
    decisions.sort(key=lambda r: r["id"])
    with DECISIONS.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["id", "title", "primary", "secondary", "status", "recommendation", "basis", "risk_note"], delimiter="\t")
        writer.writeheader(); writer.writerows(decisions)
    print(f"wrote {REVIEW} rows={len(out)} articles={len(DATA)}")
    print(f"wrote {DECISIONS} rows={len(decisions)} status_counts={{manual_confirmed: {sum(r['status']=='manual_confirmed' for r in decisions)}}}")


if __name__ == "__main__":
    main()
