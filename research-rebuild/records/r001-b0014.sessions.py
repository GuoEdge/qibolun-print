# -*- coding: utf-8 -*-
"""批次 r001-b0014 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0014.sessions.py            # 写 out/r001-b0014.out.jsonl
  python3 records/r001-b0014.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0014"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0014.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "6565e946": {
  "analysis": {
   "question_context": "提问者（Q001）问“悲观的人如何能变得乐观？”。作者开篇声明答案会多次更新，先为“可能合格的答案”设标准（边际效用不递减、可持续），据此排除毒品式生理刺激与依赖特定活人两条路，再论抑郁者的基本错误与“考试模型”的后果，把出路落在重新归因成功（首先是幸运而非努力）与真诚忏悔，随后重新界定乐观/悲观并为“盲目乐观”辩护，最后提出以整理“被动的好运”支撑乐观。问题属提问者，标准与框架由作者自设。",
   "content_units": [{"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005", "P006", "P007", "P008", "P009", "P010", "P011", "P012", "P013", "P014", "P015", "P016", "P017", "P018", "P019", "P020", "P021", "P022", "P023", "P024", "P025"], "summary": "立两条标准；排除毒品、自我欺骗、依赖活人。", "role": "definition"}, {"unit_id": "U002", "paragraph_refs": ["P026", "P027", "P028", "P029", "P030", "P031", "P032", "P033", "P034", "P035", "P036", "P037", "P038", "P039", "P040", "P041", "P042", "P043", "P044", "P045", "P046", "P047", "P048"], "summary": "指抑郁者的错误与傲慢；论考试模型。", "role": "claim"}, {"unit_id": "U003", "paragraph_refs": ["P049", "P050", "P051", "P052", "P053", "P054", "P055", "P056", "P057", "P058", "P059", "P060", "P061", "P062", "P063", "P064", "P065", "P066", "P067", "P068", "P069", "P070", "P071", "P072", "P073"], "summary": "小概率事件与劝解无效；出路归因幸运。", "role": "claim"}, {"unit_id": "U004", "paragraph_refs": ["P074", "P075", "P076", "P077", "P078", "P079", "P080", "P081", "P082", "P083", "P084", "P085", "P086", "P087", "P088", "P089", "P090", "P091", "P092", "P093", "P094", "P095", "P096", "P097", "P098", "P099", "P100", "P101", "P102", "P103", "P104", "P105", "P106", "P107", "P108", "P109", "P110", "P111", "P112", "P113", "P114", "P115", "P116", "P117", "P118", "P119", "P120", "P121", "P122", "P123", "P124", "P125", "P126", "P127", "P128", "P129", "P130", "P131", "P132", "P133", "P134", "P135", "P136", "P137", "P138", "P139", "P140", "P141", "P142", "P143", "P144", "P145", "P146", "P147", "P148", "P149", "P150", "P151", "P152", "P153", "P154", "P155", "P156", "P157", "P158", "P159", "P160", "P161", "P162", "P163", "P164", "P165", "P166", "P167"], "summary": "建议反省忏悔并反驳悲观主义；界定实事求是、事实长远中性；反驳“盲目乐观”。", "role": "action_advice"}, {"unit_id": "U005", "paragraph_refs": ["P168", "P169", "P170", "P171", "P172", "P173", "P174", "P175", "P176", "P177", "P178", "P179", "P180", "P181", "P182", "P183", "P184", "P185", "P186"], "summary": "以“被动的好运”支撑乐观。", "role": "action_advice"}],
   "main_claims": [{"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "合格答案须边际效用不递减且可持续。", "evidence": ["E001", "E002"]}, {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "两种致命副作用：吗啡类刺激递减只作缓兵之计；不尊重自然规律的自我欺骗。", "evidence": ["E003", "E004"]}, {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "依赖不可持续资源危险；依靠活人得救不可行，人不能拯救人。", "evidence": ["E005", "E006"]}, {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "抑郁者的基本错误是所崇拜者说无希望就断定无希望；最大问题是傲慢，人无资格凭智慧绝望。", "evidence": ["E007", "E008", "E009"]}, {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "认知已从运气模型转向考试模型，而它不符合事实并把人带向抑郁。", "evidence": ["E010", "E011"]}, {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人越活得久越可能遇上毁灭性小概率事件；抑郁源于完全理性的悲观预期，故劝解无效。", "evidence": ["E012", "E013"]}, {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "成功首先依赖没发生无法预料的突发风险：人首先是幸运的，然后才是努力的。", "evidence": ["E014", "E015"]}, {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "抑郁是对将荣耀归于自身努力的对称报应，唯归于幸运可脱出；忏悔唯真诚者能领取。", "evidence": ["E016", "E018"]}, {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者不建议超出自己承受限度去盲目“精进”。", "evidence": ["E017"]}, {"claim_id": "C010", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "悲观主义者的理由：悲观是安全的，乐观像预约失望。", "evidence": ["E019"]}, {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "按判断信度的预估属实事求是；事实长远中性；未识别的风险永恒存在，故悲观乐观皆盲目；真正乐观者清醒知道自己盲目而仍乐观，可用整理“被动的好运”创造。", "evidence": ["E020", "E021", "E022", "E023", "E024", "E025", "E026"]}],
   "argument_steps": ["立标准一（边际效用不递减）与标准二（可持续），排除毒品式刺激与依赖活人得救（P002—P025）。", "指抑郁者的基本错误与傲慢，解释考试模型的由来与后果（P026—P048）。", "说明小概率事件与劝解无效，转向成功归因幸运（P049—P073）。", "给行动建议并转述、反驳悲观主义（P074—P108）。", "界定实事求是与事实长远中性（P109—P135）。"],
   "concept_usage": [{"term": "边际效用递减", "meaning": "方案效果随使用而失效，为第一条否决理由", "evidence": "P003", "ambiguity": "未给度量方式"}, {"term": "考试模型／运气模型", "meaning": "对“事情如何做成”的两种认知：可控应试与承认运气", "evidence": "P042", "ambiguity": "归因于学校教育，未给经验证据"}, {"term": "盲目乐观", "meaning": "清醒知道自己证据不足却仍不担忧失败的乐观", "evidence": "P163", "ambiguity": "与日常贬义相反"}],
   "examples_and_targets": ["毒品与健身、游戏、性爱、事业成功（作者称为软性毒品，P010）", "视为救世主的人与被依赖者的压力（P016—P020）", "一战二战、普遍入学与延长学制（P042）", "悲观主义者的自述理由（P094—P100，被转述与被反驳）"],
   "conditions": ["以“如果会渐渐失效”为前提（P004）", "以“如果你能有这样的能力”等假设语气展开推演（P011、P013）", "以“一战二战以来”限定考试模型的历史条件（P042）", "以“我也并不建议你超出自己承受限度”为限定（P080）"],
   "rhetoric_and_tone": "训诫劝诫为主，夹杂反讽反问（“小算盘打得噼啪响”“说错你们没有？”）；以第二人称“你/你们”直接施压，称抑郁者的问题是傲慢、需耳光与棍棒；用“地狱的门必将为每一个自大者洞开”“丧钟为每个人而鸣”等宗教化修辞；结尾转为自荐式收束。",
   "unresolved_questions": ["本篇无图片节点，图片核验不适用；正文 P001—P185 已读完，status=read、full_text_checked=true", "P182 含“运气极差的人该如何从头开始恢复运气? ⚠lexical未覆盖片段”，属结构未覆盖内容，需人工核对", "updated_at 为 2024-05-28 晚于发表时间，且开篇称答案会多次更新但正文未标注修订，版本差异无法判断", "“很大一部分抑郁其实是上帝给狂妄自大者和偶像崇拜者设立的惩罚机制”属宗教性断言，需外部核查（P016）", "“考试模型／运气模型”的历史叙述无数据或文献支持，需外部核查（P042、P044）", "正文未点名引用任何思想来源，其与尼采等“自我崇拜”论题的关联需外部核查"],
   "evidence": [{"key": "E01", "paragraph_id": "P003", "quote": "边际效用不能递减", "relation": "supports"}, {"key": "E02", "paragraph_id": "P006", "quote": "不能依赖不可持续的资源", "relation": "supports"}, {"key": "E03", "paragraph_id": "P011", "quote": "只不过是软性毒品而已", "relation": "supports"}, {"key": "E04", "paragraph_id": "P013", "quote": "以不尊重自然规律为前提的自我欺骗", "relation": "supports"}, {"key": "E05", "paragraph_id": "P014", "quote": "本身就足以导致抑郁", "relation": "supports"}, {"key": "E06", "paragraph_id": "P016", "quote": "人不能拯救人", "relation": "supports"}, {"key": "E07", "paragraph_id": "P028", "quote": "就相信事情是毫无希望的了", "relation": "supports"}, {"key": "E08", "paragraph_id": "P030", "quote": "抑郁者最大的问题，是傲慢", "relation": "supports"}, {"key": "E09", "paragraph_id": "P038", "quote": "宣布自己就是上帝", "relation": "supports"}, {"key": "E10", "paragraph_id": "P042", "quote": "从“运气模型”转向了“考试模型”", "relation": "supports"}, {"key": "E11", "paragraph_id": "P046", "quote": "它根本就不符合事实", "relation": "supports"}, {"key": "E12", "paragraph_id": "P050", "quote": "在毁灭性的小概率事件面前都是不堪一击的", "relation": "supports"}, {"key": "E13", "paragraph_id": "P055", "quote": "你不是疯了所以抑郁，而是恰恰是因为完全理性", "relation": "supports"}, {"key": "E14", "paragraph_id": "P063", "quote": "首先都依赖于没有发生过无法提前预料、无法控制、也无法补偿的突发风险", "relation": "supports"}, {"key": "E15", "paragraph_id": "P064", "quote": "你首先是【幸运的】，然后才是【努力的】", "relation": "supports"}, {"key": "E16", "paragraph_id": "P068", "quote": "真心实意将荣耀首先归于幸运", "relation": "supports"}, {"key": "E17", "paragraph_id": "P080", "quote": "并不建议你超出自己承受限度的盲目“精进”", "relation": "qualifies"}, {"key": "E18", "paragraph_id": "P089", "quote": "装腔作势“认错”是没有意义的", "relation": "supports"}, {"key": "E19", "paragraph_id": "P094", "quote": "悲观是安全的", "relation": "context"}, {"key": "E20", "paragraph_id": "P114", "quote": "而是实事求是", "relation": "supports"}, {"key": "E21", "paragraph_id": "P126", "quote": "长远看都是中性的", "relation": "supports"}, {"key": "E22", "paragraph_id": "P151", "quote": "凡乐观，必是盲目乐观", "relation": "supports"}, {"key": "E23", "paragraph_id": "P163", "quote": "清醒的知道自己的盲目，但仍然乐观的人", "relation": "supports"}, {"key": "E24", "paragraph_id": "P170", "quote": "需要大量事实根据的来支撑的", "relation": "supports"}, {"key": "E25", "paragraph_id": "P183", "quote": "盲目的乐观本身是一种劳动的成果", "relation": "supports"}, {"key": "E26", "paragraph_id": "P184", "quote": "而是一种被坚持的选择了", "relation": "supports"}]
  },
  "provisional_tags": {"domain_candidates": ["心理学", "人生哲学"], "issue_candidates": ["抑郁与悲观", "乐观主义的辩护", "成功归因"], "text_function_candidates": ["答疑", "论辩", "劝诫"], "object_candidates": ["悲观者／抑郁者", "自大者"], "working_keywords": ["考试模型", "运气模型", "被动的好运", "盲目乐观"]},
  "notes": "无图片，图片核验不适用；正文 P001—P185 全读完，status=read、full_text_checked=true；悲观主义者理由（P094—P100）按 opponent_view＋attribution=opponent 记录；P182 的“⚠lexical未覆盖片段”已登记。为满足 40000 字上限按简报 3.1 压缩：内容单元 21→5、主张 27→11、短引只留最短片段；evidence_refs 仅保留 paragraph_id 级定位（去掉与 structure.paragraphs 重复的 field/index/字符偏移）；证据段落、归属与未决问题未删减。"
 }
}


# 证据 key 归一：ANALYSIS 中 claims 引用 "E001"，evidence 列表使用 "E01"
for _p in ANALYSIS.values():
    for _c in _p['analysis'].get('main_claims', []):
        if 'evidence' in _c:
            _c['evidence'] = ['E%02d' % int(str(k)[1:]) for k in _c['evidence']]


def _compact(rec):
    """单篇记录体量收缩（简报 3.1）。

    本文正文 10454 字却被切分为 186 段，机械生成的 structure.paragraphs 约 30000 字，
    叠加 26 条证据引用后逼近 40000 字上限。这里只做一处不损失信息的收缩：
    evidence_refs 去掉与 structure.paragraphs 完全重复的 field / paragraph_index
    以及冗余的段落字符区间，只保留 paragraph_id 级定位；短引原文、段落定位（可经
    paragraph_id 回查 structure.paragraphs 的 index/字符区间）、归属与未决问题均不变。
    """
    for ev in rec.get('evidence_refs') or []:
        ev.pop('char_start', None)
        ev.pop('char_end', None)
        ev.pop('field', None)
        ev.pop('paragraph_index', None)
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default=None, help='输出 JSONL 路径（默认 out/<batch>.out.jsonl）')
    args = ap.parse_args()
    rows = load_batch_rows(BATCH)
    records = []
    for row in rows:
        art = row['article']
        uid = UID_BY_ID[art['id']]
        if uid not in ANALYSIS:
            raise SystemExit('ANALYSIS 缺少 %s (%s)' % (uid, art.get('title')))
        p = ANALYSIS[uid]
        analysis = dict(p['analysis'])
        # ANALYSIS 里证据条目的 key 名为 evidence；转换后 build_record 会改写该键
        analysis['evidence'] = [dict(e) for e in analysis.get('evidence', [])]
        rec = build_record(
            row, row['batch_id'], row['corpus_sha256'],
            analysis, p['provisional_tags'], STARTED, COMPLETED,
            status=p.get('status', 'read'),
            full_text_checked=p.get('full_text_checked', True),
            image_checked=p.get('image_checked', False),
            notes=p.get('notes', ''))
        records.append(_compact(rec))
    out = args.out or os.path.join(_HERE, '..', 'out', BATCH + '.out.jsonl')
    write_jsonl(out, records)
    print('ok %s -> %s (%d records)' % (BATCH, out, len(records)))


if __name__ == '__main__':
    main()
