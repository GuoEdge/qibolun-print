# -*- coding: utf-8 -*-
"""批次 r001-b0420 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0420.sessions.py            # 写 out/r001-b0420.out.jsonl
  python3 records/r001-b0420.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import autofill_empty_analysis, build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0420"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0420.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "6d39db90": {
  "analysis": {
   "question_context": "提问者（Q001）以“你们有没有发现国内男女对立的趋势越来越严重？”发起一个趋势判断式追问，未给数据、对象范围或比较基准。作者（答主）不接受该前提，开篇即反问“跟谁比越来越严重”，把问题改写为历史代际比较，并以第二人称“你们/维特”直接对提问一方说话。提问者的趋势判断属提问者立场，不等于作者立场；作者实际主张方向相反。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "反问式回击：追问比较基准，并追问对方是否了解上一代两性关系的实况。", "role": "rebuttal"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005", "P006", "P007", "P008", "P009"], "summary": "以居民楼与厂区家暴、必须结婚、单身不能分房与难提干等历史境况为例，说明过去高结婚率伴随高烈度冲突，并不等于两性关系好。", "role": "example"},
    {"unit_id": "U003", "paragraph_refs": ["P010", "P011", "P012", "P013", "P014", "P015", "P016", "P017"], "summary": "现在不满表面化、易分难合，但女性对男性评价总体上升；矛盾因前置化而烈度下降。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P018", "P019", "P020", "P021", "P022", "P023", "P024"], "summary": "以“胖猫”为例：今天觉得骇人听闻，恰因此类案例已少见；老一辈的反应是“他有多脆弱”。", "role": "example"},
    {"unit_id": "U005", "paragraph_refs": ["P025", "P026", "P027", "P028", "P029", "P030", "P031", "P032", "P033"], "summary": "提出“维特”机制：少年到成年转换期的精神危机必然发作，时代议题与之联结，故被感知为“越来越糟”。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P034", "P035", "P036", "P037", "P038", "P039"], "summary": "划界：个人情绪感受不能替代社会研究，感受性证据不应直接对结论产生信度贡献。", "role": "qualification"},
    {"unit_id": "U007", "paragraph_refs": ["P040", "P041", "P042", "P043", "P044"], "summary": "明确“这不科学”，要求学严肃社会学方法、查数据、与统计巫术斗争；个人感受只能作研究动力。", "role": "action_advice"},
    {"unit_id": "U008", "paragraph_refs": ["P045", "P046", "P047", "P048", "P049", "P050", "P051", "P052", "P053", "P054", "P055", "P056", "P057"], "summary": "互联网一代的劣势：长辈被隔绝在同温层外，青年期抑郁危机在同龄同圈回音壁中同步共鸣发作。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P058", "P059", "P060", "P061", "P062", "P063", "P064", "P065", "P066", "P067", "P068", "P069", "P070", "P071", "P072", "P073", "P074", "P075"], "summary": "方法一：攫取历史知识、建立覆盖自然史与文明史的完整框架以获得“绝对刻度”，学会自己观星望风，不听惊慌的麻瓜的“顺风”意见。", "role": "action_advice"},
    {"unit_id": "U010", "paragraph_refs": ["P076", "P077", "P078", "P079", "P080", "P081"], "summary": "方法二：珍惜与自己不处于同一焦虑周期的高质量异议来源；否则被同步焦虑的风暴裹挟。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“男女对立越来越严重”的追问必须先给出比较基准（与哪一代相比）；这是历史判断，要看历史，而不是近期上网的个人感受。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "上一代、上上一代的两性关系中普遍存在直接动手的暴力，且“必须要结婚”由分房、提干等制度条件支撑，因此高结婚率、高出生率不等于两性关系好。", "evidence": ["E3", "E4", "E5"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "现在的不满都在表面上、易分难合，但女性对男性的评价总体上是上升的。", "evidence": ["E6"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正发生的是分歧越来越前置和直露，而矛盾的烈度实际上下降了。", "evidence": ["E7", "E8"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "今天的人能觉得“胖猫好惨”，前提是这类案例已少见，这恰是时代进步而不是时代倒退的结果。", "evidence": ["E9"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人在少年到成年的转换期必然发作“维特的烦恼”，并把当下时代的议题与自己的濒死焦虑联结，从而把该议题认知为“越来越糟”。", "evidence": ["E10", "E11"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "维特不能拿这个人生阶段必然的绝望发作替代社会研究；自认切身的感受性证据不应直接对结论产生信度贡献（作者声明并不否认某些时候确有真实下滑因素）。", "evidence": ["E12", "E13"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "互联网把原本可由不同年龄、圈层长辈对冲的青年期抑郁危机，变成同龄同圈回音壁中的同步共鸣发作，足以形成自认为是“社会普遍共识”的幻觉。", "evidence": ["E14", "E15"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "互联网使分散的焦虑人群聚拢互激，如同核材料超过临界浓度而瞬间一起完蛋。", "evidence": ["E16", "E17"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要竭力攫取历史知识、建立完整的历史框架，以便把自身遭遇放进文明史尺度评价趋势，并学会用客观工具纠正情绪幻觉。", "evidence": ["E18", "E19"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要珍惜高质量异议来源，尤其是不与自己处在同一焦虑周期的人；能救自己的其实只有自己。", "evidence": ["E20", "E21"]}
   ],
   "argument_steps": [
    "反问比较基准：质疑“越来越严重”是与哪一代相比，并追问对方是否知道上一代两性关系的实况（P001-P002）。",
    "举证历史境况：过去居民楼与厂区每周动手、妇联主任与工会主席疲于奔命，且制度迫使结婚（P003-P006）。",
    "指出高结婚率、高出生率不叫“两性关系好”，并说明当时人以为惨烈是常态、只能忍（P007-P009）。",
    "对照现在：易分难合但女性评价上升；分歧前置化因而烈度下降（P010-P017）。",
    "以“胖猫”说明少见才显得骇人听闻，并以两代人的思维差异佐证（P018-P024）。",
    "提出“维特”机制解释趋势错觉：人生阶段的绝望发作与时代议题联结（P025-P033）。",
    "划界：感受可作研究动力，不能作信度证据；趋势判断须靠社会研究方法与数据（P034-P044）。",
    "补充互联网同温层与回音壁放大器，以及失恋、失业、失亲、丧偶四次关口（P045-P057）。",
    "给出两条方法：历史框架与绝对刻度、观星望风；珍惜不同焦虑周期的异议来源（P058-P081）。"
   ],
   "concept_usage": [
    {"term": "维特", "meaning": "借《少年维特之烦恼》指处于少年到成年转换期、必然发作绝望的青年，全文用以称呼提问一方。", "evidence": "P026", "ambiguity": "既是文学人物又是对“你们”的代称，所指在文中滑动。"},
    {"term": "男女对立", "meaning": "两性之间的冲突状态；作者把它拆为分歧的可见度与矛盾的烈度，并主张两者走向相反。", "evidence": "P015", "ambiguity": "作者未给出该词的操作性定义或衡量口径。"},
    {"term": "趋势判断／历史判断", "meaning": "作者把趋势判断等同于历史判断，主张须看历史而非个人近期感受。", "evidence": "P014", "ambiguity": "未说明“看历史”所需的数据与方法标准。"},
    {"term": "绝对刻度", "meaning": "以整个文明史尺度作参照来评价当下走势的坐标。", "evidence": "P064", "ambiguity": "如何建立与校准未说明。"},
    {"term": "顺风", "meaning": "航海隐喻：同舱乘客（同周期焦虑者）唯一够得着的、不需费力气的方向性判断。", "evidence": "P068", "ambiguity": "隐喻对应的现实主张未逐一点明。"},
    {"term": "感受性证据", "meaning": "自认切身、逼真的个人主观感受；作者主张它不应直接贡献结论的信度。", "evidence": "P039", "ambiguity": "与“研究动力”的界线作者只作原则性区分。"}
   ],
   "examples_and_targets": [
    "“胖猫”：网络舆论事件，作者用作对照案例而非亲历证据（P018-P023）。",
    "农村妇女自杀率：作者要求对方自己去查的数据，文中未给数值或来源（P019）。",
    "摔热水瓶、摔电视机、砸缝纫机、揪头发撞墙、拿剪刀扎肚子：作者对上一代家暴的历史叙述（P003）。",
    "厂里妇联主任、工会主席：单位制下疲于奔命的调解角色（P003）。",
    "单身员工不能分房、单身汉基本不用考虑提干：作者举的制度性结婚压力（P006）。",
    "“死鬼”“短命鬼”“杀千刀的”“那个负心薄幸的”：作者举的过去对丈夫的“爱称”，用作社会现实证据（P012）。",
    "少年维特与“维特的烦恼”：文学引用兼概念化（P026）。",
    "世界大战大轰炸、上山下乡返城名额、改革开放北漂南漂：假设情境类比（P027-P029）。",
    "QQ群、微信群、豆瓣小组、知乎好友：互联网回音壁的例举（P047）。",
    "核材料临界浓度与链式反应：类比（P050-P052）。",
    "观星望风、北斗南斗、海鸥海豚、福建上岸、波利尼西亚、鲨鱼：贯穿结尾的航海类比（P066-P080）。"
   ],
   "conditions": [
    "讨论范围是提问所说的“国内”（中国大陆），作者未说明数据口径与时间窗口。",
    "作者判断烈度下降，以“矛盾的前置化”这一机制成立为前提（P017）。",
    "作者自陈不否认某些时候的维特刚好赶上真实下滑因素（P038），属让步性条件。",
    "P027-P029 为“如果这时自己在经历……那么……”的假设条件句。",
    "现在分手者“往往只是吵了几次嘴、心灰意冷就分了”，是程度限定（P010）。",
    "方法建议针对“你真要关心这个议题”的读者（P043）。",
    "互联网放大机制被限定在“这一代年轻人”与四次人生关口（P045、P053、P054）。"
   ],
   "rhetoric_and_tone": "第二人称训诫体，反问密度极高（“跟谁比越来越严重？”“何必勉强硬结一辈子？”“听明白没有？维特？”）；以“维特”“你们”称呼提问方，夹带调侃与讽刺（“麻瓜”“鲨鱼丑得要死好吗？”）；用“核材料临界”与“同舱乘客强迫性信仰顺风”两组类比贯穿后半；结构为驳前提—重构机制—给方法；语气对老一辈冷峻含同情，对互联网一代是警告；结尾“就絮叨到这里，自己想想吧”收束。",
   "unresolved_questions": [
    "“农村妇女的自杀率”被要求读者自己去查，文中未给数值或来源，待外部核查（P019）。",
    "“女性对男性的评价总体上是上升的”未给数据或调查来源（P011）。",
    "“胖猫”事件的时间、经过与所指未在文中说明（P018）。",
    "“波利尼西亚”“福建就近上岸”等航海隐喻对应的现实对象未说明（P079）。",
    "P040 在结构中标注为 heading（“这不是否决你的情感……而是因为【这不科学】”），语义上是正文断言，正文与结构标注不一致。",
    "作者身份、专业背景以及“统计巫术”的具体所指均未说明。",
    "过去家暴的普遍程度只有“几乎每一栋居民楼里、每一个星期都有人直接动手”一类叙述，无量化证据。",
    "本批阅读包显示本篇无图片节点，图片状态不适用（image_checked 保持 false）。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "跟谁比越来越严重？跟上一代人、上上一代、上上上一代……相比吧？", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P014", "quote": "历史判断要看历史，不是自己“最近三个月上网的个人感受”", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "几乎每一栋居民楼里、每一个星期都有人直接动手", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "那时候人信奉“必须要结婚”", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "单身员工不能分房，只能住单身宿舍。单身汉基本不用考虑提干", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P011", "quote": "现在是不满都在表面上，易分难合，但是事实上女性对男性的评价总体上是上升的。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P015", "quote": "而是“分歧越来越前置和直露”", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P017", "quote": "矛盾的烈度实际上下降了", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P021", "quote": "这恰恰是时代进步的结果，而不是时代倒退的结果", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P026", "quote": "必然要在“少年维特”的年纪，发作“维特的烦恼”", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P032", "quote": "你必然会将这些议题和“越来越糟”的直觉认知联系起来", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P038", "quote": "维特不能仅仅拿自己到了这个人生阶段必然的绝望发作来替代社会研究", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P039", "quote": "都不应该对你的结论直接产生信度贡献", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P048", "quote": "现在全都在彼此的包围中同步共鸣着发作", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P049", "quote": "足以形成坚固的、自认为是“社会普遍共识”的强烈幻觉", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P050", "quote": "转变成了借助互联网拥抱在一起、同时互激震荡的发作", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P051", "quote": "超过临界浓度，大家一起瞬间完蛋", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P060", "quote": "要竭尽全力地攫取历史知识", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P064", "quote": "能把你自己所遭受、观察到的东西，放进整个文明史的尺度里去评价", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P076", "quote": "能救你自己的，其实只有你自己", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P077", "quote": "你要珍惜高质量的异议来源", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["社会性别", "社会变迁与代际比较", "社会研究方法", "互联网传播与舆论"],
   "issue_candidates": ["男女对立是否加剧", "家庭暴力的历史境况", "青年期抑郁与社会认知偏差", "回音壁与同温层效应", "个人感受能否作为社会判断证据"],
   "text_function_candidates": ["答疑", "论辩", "批评", "经验总结与行动建议"],
   "object_candidates": ["中国大陆", "上一代及上上代城市居民", "互联网一代青年", "胖猫", "妇联", "工会", "QQ群", "微信群", "豆瓣", "知乎"],
   "working_keywords": ["男女对立", "维特", "感受性证据", "绝对刻度", "回音壁", "同温层", "顺风", "统计巫术", "矛盾前置化"]
  },
  "notes": "提问者的问题属提问者立场，作者通篇在反驳该趋势判断。本篇无图片节点，正文 81 段（lexical 有 85 个 paragraph 节点，空段未进正文），无正文/结构分歧（divergence=0）。P040 被结构标为 heading 而语义为正文断言，已在 unresolved_questions 登记。文中多项数据（农村妇女自杀率、女性评价上升）无来源，仅标记待外部核查，未自行判断真伪。"
 },
 "ae06d950": {
  "analysis": {
   "question_context": "",
   "content_units": [],
   "main_claims": [],
   "argument_steps": [],
   "concept_usage": [],
   "examples_and_targets": [],
   "conditions": [],
   "rhetoric_and_tone": "",
   "unresolved_questions": [],
   "evidence": []
  },
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "notes": ""
 },
 "f9f7300e": {
  "analysis": {
   "question_context": "",
   "content_units": [],
   "main_claims": [],
   "argument_steps": [],
   "concept_usage": [],
   "examples_and_targets": [],
   "conditions": [],
   "rhetoric_and_tone": "",
   "unresolved_questions": [],
   "evidence": []
  },
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "notes": ""
 },
 "40232f59": {
  "analysis": {
   "question_context": "",
   "content_units": [],
   "main_claims": [],
   "argument_steps": [],
   "concept_usage": [],
   "examples_and_targets": [],
   "conditions": [],
   "rhetoric_and_tone": "",
   "unresolved_questions": [],
   "evidence": []
  },
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "notes": ""
 }
}


autofill_empty_analysis(BATCH, SKELETON, ANALYSIS)


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
        records.append(build_record(
            row, row['batch_id'], row['corpus_sha256'],
            p['analysis'], p['provisional_tags'], STARTED, COMPLETED,
            status=p.get('status', 'read'),
            full_text_checked=p.get('full_text_checked', True),
            image_checked=p.get('image_checked', False),
            notes=p.get('notes', '')))
    out = args.out or os.path.join(_HERE, '..', 'out', BATCH + '.out.jsonl')
    write_jsonl(out, records)
    print('ok %s -> %s (%d records)' % (BATCH, out, len(records)))


if __name__ == '__main__':
    main()
