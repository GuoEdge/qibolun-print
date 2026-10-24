import csv
import glob
import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REBUILD = ROOT / "research-rebuild"
CORPUS = ROOT / "sooon-q9adg-articles-v2.jsonl"
INVENTORY = REBUILD / "data" / "image-inventory.csv"
LOW_AUDIT = REBUILD / "reports" / "image-article-content-audit-round138.tsv"
OUT = REBUILD / "reports" / "image-article-audit-v1.csv"
SUMMARY = REBUILD / "reports" / "image-article-audit-v1-summary.json"


def read_csv(path, delimiter=","):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle, delimiter=delimiter))


def contains_any(text, terms):
    return any(term in text for term in terms)


def image_recommendation(review_rows, failed_count, image_count):
    if failed_count:
        return "source_incomplete_review_valid_images_only", "源图下载/解码失败，不能据不完整图片组决定全部图片用途"
    if not review_rows:
        return "review_required", "尚未完成逐图视觉复核"
    relations = [r.get("relation_to_text", "") for r in review_rows]
    visible = [r.get("visible_content", "") for r in review_rows]
    all_text = "；".join(relations + visible)
    if contains_any(all_text, ["直接看图", "图表", "统计表", "结构示意", "视觉说明", "曲线", "地图/", "原画", "流程", "示意图"]):
        return "keep_selected_images", "图片承担正文观察、结构/图表/地图或实例展示功能"
    if contains_any(all_text, ["直接对应", "直接支持", "直接例示", "支持正文"]):
        return "optional_or_keep_selected", "图片与正文有明确对应关系，但正文通常可独立阅读"
    if contains_any(all_text, ["关系弱", "对应有限", "不能证明", "仅作", "象征性"]):
        return "omit_unless_illustration_needed", "图片主要是语境、比喻或装饰，不能替代正文证据"
    return "optional_or_keep_selected", "已复核但图片用途未达到必须保留阈值"


def main():
    articles = {}
    with CORPUS.open(encoding="utf-8") as handle:
        for line in handle:
            row = json.loads(line)
            articles[row["id"]] = row

    inventory = read_csv(INVENTORY)
    by_id = defaultdict(list)
    for row in inventory:
        by_id[row["id"]].append(row)

    # Download manifests contain the authoritative transport/decode result for
    # the active image batches; the long-lived inventory is intentionally not
    # mutated just because a batch is still under review.
    manifest_status = {}
    for path in glob.glob(str(REBUILD / "reports" / "round*-image-manifest.csv")):
        for row in read_csv(Path(path)):
            if row.get("download_status"):
                manifest_status[(row["id"], row["image_index"])] = row["download_status"]

    reviews = defaultdict(list)
    reviewed_keys = set()
    for path in glob.glob(str(REBUILD / "reports" / "round*-image-review.tsv")):
        for row in read_csv(Path(path), delimiter="\t"):
            reviews[row["id"]].append(row)
            if row.get("review_status") == "reviewed":
                reviewed_keys.add((row.get("id", ""), row.get("image_index", "")))

    manual_decisions = {}
    for path in glob.glob(str(REBUILD / "reports" / "round*-image-decisions.tsv")):
        for row in read_csv(Path(path), delimiter="\t"):
            if row.get("id"):
                manual_decisions[row["id"]] = row.get("decision", "")

    low = {row["id"]: row for row in read_csv(LOW_AUDIT, delimiter="\t")}
    output = []
    for article_id, images in sorted(by_id.items(), key=lambda item: int(item[1][0]["ordinal"])):
        article = articles[article_id]
        text_chars = len(article.get("text") or "")
        reviewed_count = sum(
            1 for row in images
            if row.get("status") == "reviewed"
            or (row.get("id", ""), row.get("image_index", "")) in reviewed_keys
        )
        failed_count = sum(
            1 for row in images
            if manifest_status.get((row["id"], row["image_index"])) == "failed"
        )
        review_rows = reviews.get(article_id, [])
        review_status = "complete" if reviewed_count == len(images) else ("partial" if reviewed_count else "pending")
        if article_id in low:
            base = low[article_id]
            article_decision = {
                "exclude_candidate": "exclude_article_candidate",
                "exclude_from_main_research": "exclude_article_candidate",
            }.get(base["article_decision"], "retain_article")
            image_decision = {
                "omit": "omit_images",
                "omit_or_archive_only": "archive_images_only",
                "archive_images_only": "archive_images_only",
                "retain_text_remove_image": "omit_images",
                "retain_text_remove_image_pending": "review_required",
                "retain_text_image_optional": "optional_or_keep_selected",
                "retain_text_image_optional_pending": "review_required",
                "retain_text_keep_images_optional": "optional_or_keep_selected",
                "retain_text_keep_selected_images": "keep_selected_images",
                "retain_image_dependent_pending": "review_required",
            }.get(base["image_decision"], base["image_decision"])
            rationale = base["evidence_and_reason"]
            confidence = "manual_low_content_audit"
        elif failed_count:
            article_decision = "retain_article_source_incomplete"
            image_decision = "source_incomplete_review_valid_images_only"
            rationale = "正文存在且不能因部分图片失效而删除文章；失效图片保留为源材料不完整，不能用邻近缩略图替代。"
            confidence = "source_incomplete"
        elif text_chars == 0:
            article_decision = "exclude_article_candidate"
            image_decision = "archive_only_pending_image_review"
            rationale = "正文为空；图片无法单独重建题目所需的论证，须列入剔除候选而非直接删除原始语料。"
            confidence = "high"
        elif review_status == "complete":
            image_decision, rationale = image_recommendation(review_rows, failed_count, len(images))
            article_decision = "retain_article"
            confidence = "reviewed_images"
        else:
            article_decision = "retain_article_pending_image_review"
            image_decision = "review_required"
            rationale = "正文长度足以独立构成研究对象，但图片尚未逐图复核；暂不删除图片或据图确认事实。"
            confidence = "pending_image_review"
        output.append({
            "ordinal": images[0]["ordinal"],
            "id": article_id,
            "title": article.get("title", ""),
            "text_chars": text_chars,
            "image_count": len(images),
            "reviewed_image_count": reviewed_count,
            "failed_image_count": failed_count,
            "image_review_status": review_status,
            "article_decision": article_decision,
            "manual_image_decision": manual_decisions.get(article_id, ""),
            "image_decision": image_decision,
            "confidence": confidence,
            "rationale": rationale,
        })

    fields = list(output[0].keys())
    with OUT.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(output)

    from collections import Counter
    summary = {
        "article_count": len(output),
        "image_count": sum(int(row["image_count"]) for row in output),
        "reviewed_image_count": sum(int(row["reviewed_image_count"]) for row in output),
        "failed_image_count": sum(int(row["failed_image_count"]) for row in output),
        "article_decision_counts": dict(Counter(row["article_decision"] for row in output)),
        "manual_image_decision_counts": dict(
            Counter(row["manual_image_decision"] for row in output if row["manual_image_decision"])
        ),
        "image_decision_counts": dict(Counter(row["image_decision"] for row in output)),
        "image_review_status_counts": dict(Counter(row["image_review_status"] for row in output)),
        "low_content_audit_source": str(LOW_AUDIT.relative_to(ROOT)),
        "raw_corpus_unchanged": True,
    }
    SUMMARY.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
