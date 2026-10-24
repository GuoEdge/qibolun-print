# -*- coding: utf-8 -*-
"""批次 r001-b0104 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0104.sessions.py            # 写 out/r001-b0104.out.jsonl
  python3 records/r001-b0104.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0104"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0104.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "87c24ce9": {
  "analysis": {
   "question_context":"提问者要求制作美味鸡蛋羹。作者将其当作一个可重复的工艺优化问题，围绕无气泡、平整、熟度、效率和成本设计完整 SOP，并保留后续实验记录计划。",
   "content_units":[{"unit_id":"U001","paragraph_refs":["P001","P002","P003","P004","P005","P006","P007","P008"],"summary":"先定义成品质量、可靠性、时间和成本目标，并列出气泡、对流、表面破损等难点。","role":"problem_definition"},{"unit_id":"U002","paragraph_refs":["P009","P010","P011","P012","P013","P014","P015","P016","P017","P018"],"summary":"以气泡成因、传热和冷凝水解释工艺风险，提出降低风险的原则。","role":"reason"},{"unit_id":"U003","paragraph_refs":["P019","P020","P021","P022","P023","P024","P025","P026","P027","P028","P029","P030","P031","P032","P033","P034","P035","P036","P037","P038","P039","P040","P041","P042","P043","P044","P045","P046","P047","P048","P049","P050","P051","P052","P053","P054","P055","P056","P057","P058","P059","P060","P061","P062","P063","P064","P065","P066","P067","P068","P069","P070","P071","P072","P073","P074","P075","P076","P077","P078","P079","P080","P081","P082","P083","P084","P085","P086","P087","P088","P089","P090","P091","P092","P093","P094","P095","P096","P097","P098","P099","P100","P101","P102","P103","P104","P105","P106","P107","P108","P109","P110","P111","P112","P113","P114","P115","P116","P117","P118","P119","P120","P121","P122","P123","P124","P125","P126","P127","P128","P129","P130","P131","P132","P133","P134","P135","P136","P137","P138","P139","P140","P141","P142","P143","P144","P145","P146","P147","P148","P149","P150","P151","P152","P153","P154","P155","P156","P157","P158","P159","P160","P161","P162","P163","P164","P165","P166","P167","P168","P169","P170","P171","P172","P173","P174","P175"],"summary":"按打蛋、加水调味、低气泡搅拌、预热、装盘封膜、分段熟化、出品调味和实验采样推进，强调记录参数以形成可复现基准。","role":"procedure"}],
   "main_claims":[{"claim_id":"C001","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"鸡蛋羹质量可通过控制气泡、温度梯度、冷凝水和调味冲击等工艺变量稳定提升。","evidence":["E1","E2"]},{"claim_id":"C002","claim_type":"author_explicit","attribution":"author","modality":"qualified","statement":"窄体量杯、低气泡手动搅拌、保鲜膜封口和分段加热有助于提高成品平整度与成功率。","evidence":["E3","E4"]}],
   "argument_steps":["定义目标与失败模式（P001-P008）。","解释气泡、传热与冷凝水的机制（P009-P018）。","给出工具、配料和逐步操作流程（P019-P154）。","安排不同设备和参数的采样、照片与记录，以继续寻找最佳配置（P155-P175）。"],
   "concept_usage":[{"term":"外生气泡/内生气泡","meaning":"分别指搅拌捕获空气和材料沸腾或反应产生的气体。","evidence":"P009-P013","ambiguity":"机制说明是作者的工艺解释，未给出实验验证。"},{"term":"高可靠性","meaning":"在低技巧、低成本和短时间约束下仍能稳定成功。","evidence":"P002-P008","ambiguity":"尚未提供统计成功率。"}],
   "examples_and_targets":["鸡蛋羹气泡、对流痕迹、冷凝水滴落和调料击穿表面（P009-P018）。","蒸锅与微波炉两种加热路径（P105-P145）。"],
   "conditions":["蛋液和鸡蛋保持常温（P073-P078）。","搅拌头必须深浸液面以下、避免猛烈形成涡流（P091-P100）。","加热时间需按设备和熟度反复记录校准（P125-P145）。"],
   "rhetoric_and_tone":"工程化、规范化、细节密集，兼有对成品视觉和口感的夸张描写；把烹饪写成可测量、可迭代的实验流程。",
   "unresolved_questions":["具体蛋液与水、调味比例和加热时间仍需实验数据确定。","文中关于醋、菌落、温度和食品安全的技术断言需要外部或实测核验。","正文包含图片和视频链接，图片内容尚未单独核验。"],
   "evidence":[{"key":"E1","paragraph_id":"P001","quote":"最终交付物：鸡蛋羹制作流程","relation":"supports"},{"key":"E2","paragraph_id":"P009","quote":"气泡产生共有两种原理","relation":"supports"},{"key":"E3","paragraph_id":"P094","quote":"因为整个搅拌头深陷液面下","relation":"supports"},{"key":"E4","paragraph_id":"P155","quote":"计划采用多种不同数据配置来制作成品","relation":"supports"}]
  },
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "status":"needs_reread","full_text_checked":True,"image_checked":False,"notes":"正文与流程已读；图片、视频及设备示意尚未核验，故保留 needs_reread。参数和食品安全断言待实验或外部核查。"
 },
 "41824a1a": {
  "analysis": {
   "question_context":"提问者问是否有资格同情无知而不自知的人。作者直接否定资格，同时提出同情属于义务，并以宗教化反讽收束。","content_units":[{"unit_id":"U001","paragraph_refs":["P001"],"summary":"直接回答：没有资格。","role":"answer"},{"unit_id":"U002","paragraph_refs":["P002","P003"],"summary":"把同情从个人资格改写为对他人的义务，并称其为上帝式黑色幽默。","role":"reframing"}],"main_claims":[{"claim_id":"C001","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"人没有以优越位置同情无知者的资格，但对他人仍负有同情义务。","evidence":["E1","E2"]}],"argument_steps":["先否定资格（P001）。","再提出义务和反讽解释（P002-P003）。"],"concept_usage":[{"term":"资格/义务","meaning":"资格是可据以居高临下评价他人的正当性，义务是即使没有优越性也应承担的关怀责任。","evidence":"P001-P002","ambiguity":"没有说明义务来源和边界。"}],"examples_and_targets":["无知而不自知者（P001）。"],"conditions":["回答针对一般伦理态度，而非具体事件。"],"rhetoric_and_tone":"极简、断言式、宗教隐喻与黑色幽默。","unresolved_questions":["为何同情是义务而非资格，正文未展开论证。"],"evidence":[{"key":"E1","paragraph_id":"P001","quote":"你没有资格。","relation":"supports"},{"key":"E2","paragraph_id":"P002","quote":"但你有义务。","relation":"supports"}]
  },
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "notes":"极短篇，正文已读；论证主要依靠格言式断言。"
 },
 "eab37a83": {
  "analysis": {
   "question_context":"提问者问优秀是否会带来被爱。作者先否定优秀是被爱条件，再区分被爱、被依赖和被贪图，讨论关系中的自由与控制。","content_units":[{"unit_id":"U001","paragraph_refs":["P001","P002","P003"],"summary":"优秀与否都可能被爱；作者把爱定义为独立、自由、有原则且互相尊重。","role":"definition"},{"unit_id":"U002","paragraph_refs":["P004","P005","P006","P007","P008"],"summary":"部分人害怕只有被爱而没有被需要，因此要求确认对方贪图自己的某种资源，以换取安全感和话语权。","role":"analysis"}],"main_claims":[{"claim_id":"C001","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"优秀不是获得爱的必要条件，爱本身应保持人格独立、自由和互相尊重。","evidence":["E1","E2"]},{"claim_id":"C002","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"有些人把被贪图误认为获得关系话语权和稳定性的保证。","evidence":["E3"]}],"argument_steps":["否定优秀与被爱的必然关系（P001）。","定义独立且有原则的爱（P002-P003）。","解释从被爱转向被贪的依赖心理（P004-P008）。"],"concept_usage":[{"term":"被爱/被贪","meaning":"被爱是对人格的尊重和关系承认，被贪是对方依赖或索取自己的资源。","evidence":"P003-P008","ambiguity":"作者未区分健康需要、互惠与剥削。"}],"examples_and_targets":["担心对方发现真实样子而离开的关系不安全感（P004-P006）。"],"conditions":["讨论的是亲密关系中的心理需求和控制感。"],"rhetoric_and_tone":"定义式、心理剖析式，使用反差和尖锐概念替换。","unresolved_questions":["爱、依赖、需要和贪图之间的界限未被进一步说明。"],"evidence":[{"key":"E1","paragraph_id":"P001","quote":"优不优秀都被爱。","relation":"supports"},{"key":"E2","paragraph_id":"P002","quote":"爱是人格独立的，是不卑不亢的","relation":"supports"},{"key":"E3","paragraph_id":"P006","quote":"非得确认对方有在贪图自己什么","relation":"supports"}]
  },
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "notes":"正文已读；作者使用‘被贪’作为批判性关系概念，未作系统定义。"
 },
 "56e8024c": {
  "analysis": {
   "question_context":"提问者问中美首次会谈及结果和后续关注点。作者把会谈置于中美军事信誉、地区战略和霸权信号的框架中，提出高度确定性的地缘政治解释。","content_units":[{"unit_id":"U001","paragraph_refs":["P001","P002","P003","P004","P005"],"summary":"作者认为中国已判断美国无法在周边取得军事胜利，并以不留情面的反击制造美国的两难。","role":"thesis"},{"unit_id":"U002","paragraph_refs":["P006","P007","P008","P009","P010","P011","P012"],"summary":"以大哥二哥比喻说明美国若不回应会显露软弱，若回应则可能陷入无法取胜的冲突。","role":"analogy"},{"unit_id":"U003","paragraph_refs":["P013","P014","P015","P016","P017","P018"],"summary":"作者预判美国受国内政治驱动会继续试探，而中国会更强硬地回击。","role":"prediction"}],"main_claims":[{"claim_id":"C001","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"中国正在以有意而为的强硬反击，迫使美国在显露软弱和卷入无法取胜的冲突之间选择。","evidence":["E1","E2"]},{"claim_id":"C002","claim_type":"author_explicit","attribution":"author","modality":"predicted","statement":"美国若继续试探，将进一步损耗军事不可战胜神话和美元信用。","evidence":["E3"]}],"argument_steps":["提出停止继续挖坑的总喻（P001）。","说明美国军事神话和中国反击策略（P002-P005）。","用大哥二哥关系类比信誉博弈（P006-P012）。","推演美国国内政治和未来对撞（P013-P018）。"],"concept_usage":[{"term":"美国军事上无敌的神话","meaning":"支撑美国国家信用与盟友信心的霸权不可战胜叙事。","evidence":"P002-P003","ambiguity":"没有给出可检验指标。"},{"term":"阳谋","meaning":"明知对方策略仍因自身约束不得不进入对方设置的两难。","evidence":"P014-P017","ambiguity":"属于作者的战略解释。"}],"examples_and_targets":["阿拉斯加会谈（P017）。","南海、台湾、钓鱼岛等敏感议题（P004）。"],"conditions":["分析建立在美国不会或不能在中国周边发动可胜战争的前提上。","关于未来美国行动属于作者预测。"],"rhetoric_and_tone":"战略论辩、强烈断言和大哥二哥类比，语气自信且带有预言式收束。","unresolved_questions":["会谈具体议题、事实结果和军事能力判断需要外部资料核验。","美元信用与地区撤退的因果链未展开证据。"],"evidence":[{"key":"E1","paragraph_id":"P002","quote":"美国最大的本钱就是军事上无敌的神话","relation":"supports"},{"key":"E2","paragraph_id":"P005","quote":"这并不是“情绪激愤，难以自制”，而是有意而为之","relation":"supports"},{"key":"E3","paragraph_id":"P011","quote":"美元的信用堪忧","relation":"supports"}]
  },
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "notes":"正文已读；这是强预测性的地缘政治解释，事实和预测均需外部核查。"
 },
 "9a59d12b": {
  "analysis": {
   "question_context":"提问者问黑格尔为何认为汉语不宜思辨。作者拒绝把问题归因于语言本体，改以一个语种的概念资产、定义质量和学术投入解释思辨能力。","content_units":[{"unit_id":"U001","paragraph_refs":["P001","P002","P003"],"summary":"思辨适宜性与语言本身无关，关键是语境中清晰定义且被广泛掌握的概念资产数量。","role":"thesis"},{"unit_id":"U002","paragraph_refs":["P004","P005","P006"],"summary":"只要学术界和学术传播投入足够，任何语言都可形成有利于思辨的概念工具；中国具备长期投入条件。","role":"argument"}],"main_claims":[{"claim_id":"C001","claim_type":"author_explicit","attribution":"author","modality":"asserted","statement":"语言是否适合思辨主要取决于既有概念资产的清晰度和普及度，而非语言本身。","evidence":["E1","E2"]},{"claim_id":"C002","claim_type":"author_explicit","attribution":"author","modality":"predicted","statement":"通过长期学术投资，中文不仅可以适合思辨，甚至可能在长期竞争中具备优势。","evidence":["E3"]}],"argument_steps":["否定语言本体决定论（P001）。","定义思辨资产及其效率作用（P002-P003）。","用跨语言假设和中国前景完成论证（P004-P006）。"],"concept_usage":[{"term":"思辨资产","meaning":"被清晰定义或界定、并被学界或大众掌握的常用概念集合。","evidence":"P002-P003","ambiguity":"没有给出资产数量或效率的测量标准。"}],"examples_and_targets":["斯瓦希里语、泰米尔语作为跨语言假设例子（P004）。"],"conditions":["需要国家学术界和学术报道业持续有效投资。"],"rhetoric_and_tone":"简洁的概念澄清和条件推理，结尾转为对中文长期优势的预测。","unresolved_questions":["黑格尔原话及其论证未在正文中引用，需外部核查。","中文‘优势’的具体指标未说明。"],"evidence":[{"key":"E1","paragraph_id":"P001","quote":"是否适合思辨和语言本身是没关系的","relation":"supports"},{"key":"E2","paragraph_id":"P002","quote":"既有的“思辨资产”有多少","relation":"supports"},{"key":"E3","paragraph_id":"P006","quote":"中文恐怕还有优势","relation":"supports"}]
  },
  "provisional_tags": {
   "domain_candidates": [],
   "issue_candidates": [],
   "text_function_candidates": [],
   "object_candidates": [],
   "working_keywords": []
  },
  "notes":"正文已读；本文未直接重建黑格尔原论证，只提供作者自己的反解释。"
 }
}


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
