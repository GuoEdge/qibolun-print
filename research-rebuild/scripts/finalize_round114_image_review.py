#!/usr/bin/env python3
"""Apply the verified Round114 image-review state to derived review records.

The source corpus is intentionally untouched.  This narrow migration updates
only the batch-level evidence and manual A-topic decisions after the separate
per-image review TSV has been completed and validated.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
DATA = ROOT / "research-rebuild/data"
IDS = {
    "44f8c341-fd3e-56d1-a321-7aa65d97043d": 1,
    "61a65182-b3de-5c28-bb29-5ddcb2acd079": 13,
    "bd497e81-413b-5e4c-b1df-001d0efbd369": 1,
}
APPROVED = {"61a65182-b3de-5c28-bb29-5ddcb2acd079"}


def read_csv(path: Path, delimiter: str = ",") -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh, delimiter=delimiter)
        return list(reader.fieldnames or []), list(reader)


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]], delimiter: str = ",") -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, delimiter=delimiter, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    temporary.replace(path)


def validate_image_review() -> None:
    _, manifest = read_csv(REPORTS / "round114-image-manifest.csv")
    _, review = read_csv(REPORTS / "round114-image-review.tsv", "\t")
    _, inventory = read_csv(DATA / "image-inventory.csv")
    expected = {(aid, str(index)) for aid, count in IDS.items() for index in range(1, count + 1)}
    manifest_keys = {(row["id"], row["image_index"]) for row in manifest if row["id"] in IDS}
    review_keys = {(row["id"], row["image_index"]) for row in review if row["id"] in IDS}
    inventory_keys = {(row["id"], row["image_index"]) for row in inventory if row["id"] in IDS}
    assert manifest_keys == review_keys == inventory_keys == expected
    assert len(review) == len(expected)
    assert all(row["download_status"] == "success" and row["review_status"] == "reviewed" for row in review)
    assert all(row["changes_topic_judgment"] == "no" and row["image_text_consistency"] == "consistent" for row in review)
    assert all(row["status"] == "reviewed" for row in manifest if row["id"] in IDS)
    assert all(row["status"] == "reviewed" for row in inventory if row["id"] in IDS)


def update_decisions() -> None:
    path = REPORTS / "round114-decisions.tsv"
    fields, rows = read_csv(path, "\t")
    assert {row["id"] for row in rows} == set(IDS)
    limitations = {
        "44f8c341-fd3e-56d1-a321-7aa65d97043d": "图片支持影视字幕与讽刺语境，但来源、OCR和心理/社会因果判断未核验。",
        "61a65182-b3de-5c28-bb29-5ddcb2acd079": "图片支持器物与编钟/禁的可见语境，但不能单独证明失蜡法、焊接、年代、铭文或礼制史判断。",
        "bd497e81-413b-5e4c-b1df-001d0efbd369": "图片支持聚变与星际推进书页语境，但来源、公式及热力学、推进、生态和安全判断未核验。",
    }
    for row in rows:
        row["status"] = "manual_confirmed" if row["id"] in APPROVED else "manual_provisional"
        row["risk_note"] = row["risk_note"].replace("1张图片未审读且OCR未开始。", limitations[row["id"]])
        row["risk_note"] = row["risk_note"].replace("13张图片均未审读且OCR未开始。", limitations[row["id"]])
    write_csv(path, fields, rows, "\t")


def update_manual() -> None:
    path = DATA / "print-topic-manual-decisions-v2.csv"
    fields, rows = read_csv(path)
    seen = set()
    limitations = {
        "44f8c341-fd3e-56d1-a321-7aa65d97043d": "1/1张图片已视觉复核，图文一致且未改变专题；来源和OCR未核验。",
        "61a65182-b3de-5c28-bb29-5ddcb2acd079": "13/13张图片已视觉复核，图文一致且未改变专题；图片不能单独证明工艺、年代、铭文或礼制史判断，OCR未核验。",
        "bd497e81-413b-5e4c-b1df-001d0efbd369": "1/1张图片已视觉复核，图文一致且未改变专题；来源和OCR未核验，技术与生态安全判断仍待外部核查。",
    }
    for row in rows:
        aid = row.get("id", "")
        if aid not in IDS:
            continue
        seen.add(aid)
        assert row["classification_status"] in {"manual_provisional", "manual_confirmed"}
        # Image review removes the image gate, but it does not resolve a
        # formal-vs-blind primary-topic disagreement. Only 文物 has matching
        # formal and blind primary codes in Round114.
        row["classification_status"] = "manual_confirmed" if aid in APPROVED else "manual_provisional"
        row["review_note"] = (
            f"Round 114 full text; body_chars={ {'44f8c341-fd3e-56d1-a321-7aa65d97043d':2160,'61a65182-b3de-5c28-bb29-5ddcb2acd079':6314,'bd497e81-413b-5e4c-b1df-001d0efbd369':8966}[aid] }; "
            "batch=live-manual-budget-batch-v2-round114-90k.csv; independent full-text reads in two non-overlapping halves; "
            "risk notes separated from topic status; image review=reports/round114-image-review.tsv; "
            f"{limitations[aid]} "
            f"formal/blind primary reconciliation={'agreed' if aid in APPROVED else 'pending; blind primary differs'}; "
            f"factual-risk note retained: { {'44f8c341-fd3e-56d1-a321-7aa65d97043d':'关于讽刺、幽默、欺凌、家暴风险及宣传传统的心理与社会因果判断未作实证核验。','61a65182-b3de-5c28-bb29-5ddcb2acd079':'青铜器铸造路径、焊接痕迹、工艺难度、文字训诂和礼制史解释均未由文物或历史资料核验。','bd497e81-413b-5e4c-b1df-001d0efbd369':'热力学、全球温度与生态连锁、聚变工程、星际推进及国际安全判断均未外部核验。'}[aid] }"
        )
        row["reviewer"] = "main-thread+independent-review+image-review"
    assert seen == set(IDS)
    write_csv(path, fields, rows)


def update_fulltext_export() -> None:
    path = REPORTS / "round114-fulltext.json"
    rows = json.loads(path.read_text(encoding="utf-8"))
    assert {row.get("id") for row in rows} == set(IDS)
    for row in rows:
        row["image_checked"] = True
        row["evidence_note"] = (
            "正文已导出；图片已完成逐张视觉复核并与正文语境对照；图像不改变专题判断。"
            "图片仅支持可见对象/语境，不替代OCR或外部事实核验。"
        )
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def main() -> None:
    validate_image_review()
    update_decisions()
    update_manual()
    update_fulltext_export()
    print(json.dumps({"round": 114, "records": 3, "images": sum(IDS.values()), "status": "applied"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
