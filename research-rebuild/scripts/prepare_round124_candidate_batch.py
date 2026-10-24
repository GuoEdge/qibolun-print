#!/usr/bin/env python3
"""Prepare a short, text-only Round 124 candidate batch.

This is a reading packet only. It deliberately excludes article IDs that
already occur in any prior round decision file and never writes the formal
manual classification table.
"""
from __future__ import annotations

import csv
import glob
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "research-rebuild/reports"
QUEUE = REPORTS / "live-manual-classification-queue-v2.csv"
CORPUS = ROOT / "sooon-q9adg-articles-v2.jsonl"
BATCH = REPORTS / "round124-candidate-batch.csv"
FULLTEXT = REPORTS / "round124-fulltext.json"
OVERVIEW = REPORTS / "round124-candidate-overview.tsv"

# These notes are deliberately about evidence and classification risk, not
# final topic decisions. They are based on reading the selected正文.
RISK_NOTES = {
    "c0a13aa7-6476-5774-b661-e424f933d513": "正文仅4字且语义不完整；爱意表达与自责/幽默均可能，不能据标题定码",
    "1015117d-47f5-5e6d-8648-373790bd96b6": "仅成语式回答；坚持、择善与价值判断边界不足",
    "9b6db870-bac2-5741-b015-bd793dcd6dbe": "仅一句格言；怜悯与不羡慕的关系未展开，A00/A01边界不稳",
    "e8873042-d451-5335-87d7-638f1926a64a": "一句隐喻未定义刻奇；文化批评与审美/凝视主题可能混合",
    "709c7581-b9fb-5c40-9d0d-bf5f0b3ec31b": "两句价值断言；亲密关系能力与一般人生价值需区分",
    "4c8d70b4-e511-559a-abad-85a90006ee86": "政治定义极短；规范博弈与治理实践两轴均有，A10/A03需边界判断",
    "34c70769-57cc-52fb-b839-f99b12466071": "死亡箴言；宗教化拉丁语与死亡意识并存，A19/A11需区分",
    "212c4ae7-d09b-5c10-8fbb-c65d879c824a": "仅评价批评风格；原媒体事件未复核，批评/公共舆论边界不明",
    "964d3312-f52b-5cdf-a3cb-ee6085fb0dd0": "涉及基督教与同性恋罪论；规范性宗教判断和性取向议题敏感，事实未核验",
    "571762ad-24ca-5894-844b-462266f99d17": "定义式回答；‘废话’的行为影响标准未举例，A00可能过宽",
    "bad58134-0613-5973-843b-2bc93ebb9733": "死亡临终安慰语；带有来世想象，A19与家庭照护/情感支持需区分",
    "5316551a-199f-5363-8436-1c4d4a72bbc2": "未回答神话谱系而转为药物隐喻；宗教/神话与社会批评可能错位",
    "6ee1126a-85a9-5e39-890a-e06aa07ef24a": "仅一句主义定义；政治意识形态冲突与抽象论辩均可能",
    "57146303-1714-5d24-b18f-8643040174f8": "对儿童死亡教育以反问和玩笑作答；死亡/育儿与宗教想象需谨慎区分",
    "41824a1a-d9da-5134-a987-9f10639e2425": "同情资格与义务的规范断言；宗教黑色幽默不是外部伦理结论",
    "f1d9f87b-25e5-578e-9e66-cd400174e568": "死亡、唯物主义与希望并置；信仰/价值主张未展开",
    "8d2768d7-8132-585a-afcf-e00fd2effcc1": "针对网络解读的抽象评价；极端化与忠诚/背叛关系需避免替事件补事实",
    "68081827-4bf0-52db-83ab-f406ca3555b7": "AirTag隐私价值判断；技术功能和安全事实未说明，A13/A14/A10边界待审",
    "41c47afa-ca71-5905-924e-bc87c5a24f35": "仅列耆那教和santhara入口；宗教信息极不完整，不能外推事实",
    "c7951d41-c774-5708-b9b4-7a7b8242e2ae": "涉及处女情结与强奸类比；性别/性伦理敏感，需按正文主旨而非触发词归类",
    "2eca1ab5-e5fd-5ec9-a5e9-61e9e7375dc0": "以自嘲反答信任强者问题；交友关系与自我评价并置",
    "1f2225d3-9bd8-56e6-9c4a-7403ec00b281": "只写理性导致不被信任；心理解释短，理性/亲密关系边界待审",
    "48274dc5-4a4a-5096-8ddc-5e7a6dc7736d": "把艺术生偏见解释为报复；社会偏见因果断言未核验",
    "e0005624-e252-5158-8832-ba36497b20d8": "无神论与临终状态并置；涉及宗教信念及医学/临终事实但未提供证据",
    "9e331c63-31ac-5328-aa0c-524de39aef37": "将天赋定义为持续寻找坚持理由；励志/能力概念混合",
    "913f1fd9-3d73-546a-b924-70174ef27403": "婚姻正常性问题只作规范批判；未回答年龄或关系事实",
    "e6eaee74-6ff9-54b1-98ad-732cd571ee0f": "恋爱关系中的永远承诺与沟通；亲密关系主轴清楚但有反讽",
    "cf744236-ae73-5eb0-92f5-30c22ef8dd19": "作家层级以问题/答案区分；文学评价主轴与抽象认识论重叠",
    "3aeb41af-85cc-5da7-ac22-72aacbd4774f": "以刑罚隐喻回应法律问题；不是法律案例，避免当作法律事实",
    "c4effbba-4dba-537e-8bdb-e889fc6baf00": "以风的隐喻回应幸福；资产收入等题干事实未核验",
    "1f6d2379-e6ed-5e52-a24d-1bbb60aa586b": "遗嘱建议涉及老年死亡焦虑与法律程序；公证建议未核验",
    "4d34493f-ab2b-5279-89e4-630e0b103f1c": "高等生命与食物链的反讽；科幻/生命等级价值判断混合",
    "ed26c0bb-1fd9-51f3-80c5-fd5da75f39e7": "法庭行为建议具有法律场景；涉及法官和司法事实但仅为经验式劝诫",
    "e8f95c53-65c1-513e-aa90-141e0712e2c8": "数据保存问题转为经典文本传播；技术保存方案未回答",
    "29c27b45-31d3-5ee7-ae33-f46a3176d48b": "用飙车类比失恋；亲密关系主轴明显，建议不扩展为医疗/安全事实",
    "610f5c80-e08e-5b69-b9f7-2beb6563e578": "以四种善果定义正确道路；宗教伦理与公共善/医疗表述并置",
    "3f55c59c-c54c-5eee-837e-4efe0d7ca381": "双向奔赴的关系隐喻；未涉及具体关系事实",
    "669447b3-e2fc-5430-a9d0-6603ac02bf98": "声称只讲事实却给赞美例句；沟通/真诚与评价标准边界待审",
    "85aecfc3-f160-531a-8404-42441717edd4": "建议追打破坏者并录像；含报复和财产破坏风险，不能按艺术概念单独归类",
    "ea8344f2-05e3-5c4c-9f53-9531cfc1eec1": "语言词义分析简短；‘其实’的否定功能为语用判断，缺少语料",
    "c760d4b4-4c9e-5766-8050-11dcfae50b93": "未经允许帮助被称为自私；边界、恩惠与关系伦理均可能",
    "1109bcf8-390f-54ef-9191-6ec7f40f5c1d": "以偶然因素解释嫉妒/崇拜；心理机制是推断而非研究证据",
    "32f16077-799b-59cf-b3b1-63274a2819a0": "将悲观称作毒瘾并归因信仰；心理健康类比和价值判断未核验",
    "f04084e1-6bfb-5012-a1a1-d6b4112e3245": "日本法规、垃圾桶和爆炸事件均为事实性断言；需外部核验，A08/A10待审",
    "026dafd1-371b-551e-936c-51fc9e27c377": "骨灰制盲道的想象；死亡、残障与公益意象并置，实施可行性未讨论",
    "0eb2277c-4215-5ce8-a192-3328befecdcb": "强烈自我中心的生命信念；鼓励不要放弃但没有危机评估或事实依据",
    "548f6103-2d0d-5817-84eb-8da07cd01253": "以盲人比喻回应讽刺；涉及残障刻板印象与善意边界",
    "30c953b6-0a40-50ac-820d-9c7fe5ade0da": "按需分配与生育约束为政策/经济断言；明确非主张但事实仍未核验",
    "c8a3029e-592c-5d61-b3aa-31b07904c393": "科幻作品考据式批评；材料和物理推断不是现实武器事实",
    "8561dd6b-4c1d-57e7-82b6-b1321f7d23c6": "把知识兴趣解释为精神肌肉和强奸适应性；性别概括与强烈措辞敏感",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def prior_ids() -> set[str]:
    ids: set[str] = set()
    for path in glob.glob(str(REPORTS / "round*-decisions.tsv")):
        with open(path, encoding="utf-8-sig", newline="") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                if row.get("id"):
                    ids.add(row["id"])
    return ids


def main() -> int:
    queue = read_csv(QUEUE)
    seen = prior_ids()
    candidates = [
        row for row in queue
        if row["id"] not in seen
        and int(row.get("deepseek_image_count") or 0) == 0
        and int(row.get("body_char_count") or 0) > 0
    ]
    candidates.sort(key=lambda row: (int(row["body_char_count"]), int(row["source_ordinal"])))
    batch = candidates[:50]
    if len(batch) != 50:
        raise RuntimeError(f"expected 50 candidates, got {len(batch)}")
    missing_notes = [row["id"] for row in batch if row["id"] not in RISK_NOTES]
    if missing_notes:
        raise RuntimeError(f"missing risk notes for {missing_notes}")

    articles: dict[str, dict] = {}
    with CORPUS.open(encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                article = json.loads(line)
                if article.get("id") in {row["id"] for row in batch}:
                    articles[str(article["id"])] = article

    fulltext = []
    for row in batch:
        article = articles[row["id"]]
        text = article.get("text") or ""
        if len(text) != int(row["body_char_count"]):
            raise AssertionError((row["id"], len(text), row["body_char_count"]))
        fulltext.append({
            "source_ordinal": int(row["source_ordinal"]),
            "id": row["id"],
            "title": article.get("title", ""),
            "question": article.get("question", ""),
            "text": text,
        })

    with BATCH.open("w", encoding="utf-8", newline="") as fh:
        fields = [
            "source_ordinal", "id", "title", "question", "body_char_count",
            "priority", "priority_reasons", "candidate_primary", "candidate_secondary",
            "candidate_score", "candidate_status", "official_assignment_status",
            "official_category_paths", "native_object_paths", "deepseek_image_count",
            "manual_status",
        ]
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for row in batch:
            writer.writerow({field: row.get(field, "") for field in fields})

    FULLTEXT.write_text(json.dumps(fulltext, ensure_ascii=False, indent=2), encoding="utf-8")
    with OVERVIEW.open("w", encoding="utf-8", newline="") as fh:
        fields = [
            "source_ordinal", "id", "title", "body_char_count", "machine_primary",
            "machine_secondary", "candidate_score", "priority", "priority_reasons",
            "image_count", "risk_points",
        ]
        writer = csv.DictWriter(fh, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        for row in batch:
            writer.writerow({
                "source_ordinal": row["source_ordinal"],
                "id": row["id"],
                "title": row["title"],
                "body_char_count": row["body_char_count"],
                "machine_primary": row["candidate_primary"],
                "machine_secondary": row["candidate_secondary"],
                "candidate_score": row["candidate_score"],
                "priority": row["priority"],
                "priority_reasons": row["priority_reasons"],
                "image_count": row["deepseek_image_count"],
                "risk_points": RISK_NOTES[row["id"]],
            })

    print(json.dumps({
        "round": 124,
        "records": len(batch),
        "body_chars": sum(len(row["text"]) for row in fulltext),
        "max_body_chars": max(len(row["text"]) for row in fulltext),
        "excluded_prior_round_ids": len(seen),
        "remaining_novel_no_image_candidates": len(candidates) - len(batch),
        "batch": str(BATCH),
        "fulltext": str(FULLTEXT),
        "overview": str(OVERVIEW),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
