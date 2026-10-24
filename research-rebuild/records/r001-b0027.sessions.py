# -*- coding: utf-8 -*-
"""批次 r001-b0027 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0027.sessions.py            # 写 out/r001-b0027.out.jsonl
  python3 records/r001-b0027.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0027"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0027.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "e26ded3d": {
  "analysis": {
   "question_context": "提问者问：为什么不使用光代替无线电波进行通信？（Q001）。作者先以冷知识调侃——可见光通信其实是最早的电磁波通信方式（长城烽火、军舰灯语）——随后转入严肃讨论：波长越大穿透绕射越好但有效带宽越小，通信技术趋势是频率越来越高、基站越来越近，到 5G 频段后可有效穿透的方式已到头，毫米波相对可见光只有带宽劣势；而可见光在大气层中传播非常不可靠，障碍是大气不均匀造成的折射率扭曲以及雾沙尘雨雪。作者随后自问自答，指出可见光通信并非一无是处，其真正用武之地是星际、太空站、星球殖民地与卫星之间的高带宽通信。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005"], "summary": "以冷知识调侃开篇：利用可见光的通信反而最早（长城烽火、军舰灯语），比电报电话早几百几千年，随后以 OK，不开玩笑了收住。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P006", "P007", "P008"], "summary": "原理与趋势：波长越大越能穿透绕射，故长波利于远距离；但波长越长有效带宽越小，通信趋势是基站频率升高、距离缩短，基站间靠有线光纤承载超高频率交流；到 5G 频段可有效穿透的方式已到头，毫米波对可见光只有带宽劣势（除非有对毫米波透明的超膜建筑材料）。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P009", "P010", "P011", "P012", "P013"], "summary": "可见光在大气层传播非常不可靠：问题不在光强（可用高倍大口径放大镜解决），而在大气不均匀导致折射率扭曲（马路热空气、酒精与水的明暗纹路），雾、沙尘、雨、雪亦然。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P014", "P015"], "summary": "自问自答：这是否意味着可见光通信一无是处？当然不是。", "role": "transition"},
    {"unit_id": "U005", "paragraph_refs": ["P016", "P017"], "summary": "适用场景：可见光通信（更准确说是激光通信）非常适合星际信号传输，太空站、星球殖民地与卫星间的高带宽通信是绝佳的；激光单向性使其成为该场景下的唯一选择。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在一切利用电磁波的通信方式中，利用可见光通信反而是最早的，例如长城烽火与军舰灯语，比电报电话早几百几千年。", "evidence": ["E1", "E2"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "波长越大越能穿透和绕过障碍，所以长波对远距离通信大有好处。", "evidence": ["E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "波长越长有效带宽越小；通信技术发展的趋势是基站频率越来越高、基站离接收终端越来越近，基站之间依靠复杂的有线光纤网络承载超高频率的交流。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "到 5G 频段，具有有效穿透力的通信方式就已经到头；毫米波穿透力与可见光相比差不多没有优势，因此它相对可见光的带宽劣势是绝对的——除非创造出对毫米波透明的超膜建筑材料。", "evidence": ["E5", "E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "可见光在大气层中传播非常不可靠；这不是光强不足的问题（高倍大口径放大镜可解决），而是大气不均匀造成的折射率扭曲会严重干扰信号，类似问题还有雾、沙尘、雨、雪。", "evidence": ["E7", "E8", "E9"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "上述限制并不意味着可见光通信一无是处。", "evidence": ["E10"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "可见光通信（更准确说是激光通信）非常适合星际信号传输；用于太空站、各个星球殖民地和卫星之间的高带宽通信，可见光（还包括红外、紫外激光）是绝佳的。", "evidence": ["E11"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "激光的单向性在该场景下意义重大，甚至可以说是唯一选择，因为不可能拉一根几十万甚至上百万上千万公里的光缆。", "evidence": ["E12"]}
   ],
   "argument_steps": [
    "调侃式开场（P001-P004）：以长城烽火、军舰灯语说明可见光通信反而是最早的电磁波通信。",
    "转入严肃（P005-P006）：先给出波长与穿透绕射、长波利于远距离通信的基本前提。",
    "原理权衡（P007）：波长越长带宽越小，故通信趋势是频率升高、基站靠近终端、基站间靠有线光纤。",
    "推进到毫米波（P008）：5G 之后可有效穿透的方式到头，毫米波相对可见光的带宽劣势是绝对的，并留出超膜材料的例外。",
    "转折指出障碍（P009-P013）：可见光大气传播不可靠，障碍是大气不均匀的折射率扭曲与雾沙尘雨雪，而非光强。",
    "自问自答（P014-P015）：并非一无是处。",
    "给出适用场景（P016-P017）：星际、太空站、殖民地、卫星间高带宽通信，激光单向性使其成为唯一选择。"
   ],
   "concept_usage": [
    {"term": "可见光通信", "meaning": "以可见光（作者在 P016 更准确地归为激光通信，并包含红外、紫外激光）作为信息载体的通信方式；本文一半篇幅用于说明其在大气层中的不可靠。", "evidence": "P009", "ambiguity": "作者未区分照明通信、自由空间光通信与光纤通信，P007 提到光纤中承载的常常就是可见光，与大气传播场景混用。"},
    {"term": "波长与带宽的权衡", "meaning": "波长越大穿透绕射越好但有效带宽越小，故长波宜远距离、高频宜高带宽短距离。", "evidence": "P007", "ambiguity": "作者未给出具体频段与带宽的量化关系。"},
    {"term": "超膜建筑材料", "meaning": "作者假设的、对毫米波透明的材料，若存在则上述毫米波劣势的判断另当别论。", "evidence": "P008", "ambiguity": "为假设性设想，作者未说明其可行性或研究现状。"},
    {"term": "大气不均匀", "meaning": "冷热空气造成折射率扭曲，从而严重干扰可见光信号传输；雾、沙尘、雨、雪属类似问题。", "evidence": "P013", "ambiguity": "作者以生活现象类比，未给出传输模型或衰减数据。"},
    {"term": "单向性", "meaning": "激光光束方向集中，使点对点星际通信无需铺设光缆。", "evidence": "P017", "ambiguity": "文中未讨论瞄准、捕获与跟踪难题。"}
   ],
   "examples_and_targets": [
    "长城烽火、军舰灯语（P002、P003）：作者例证，说明可见光通信最早。",
    "电报电话（P004）：比较对象。",
    "5G 频段与毫米波（P008）：作者论述对象。",
    "超膜建筑材料（P008）：作者假设的例外条件。",
    "夏天灼热马路上方的光线扭曲、纯酒精倒进纯水（P012）：作者例证与类比。",
    "雾、沙尘、雨、雪（P013）：作者列举的类似干扰。",
    "太空站、各个星球殖民地、卫星（P016）：作者指出的适用场景。",
    "几十万甚至上百万上千万公里的光缆（P017）：作者的反证材料。",
    "图片节点 IMG001（阅读包列出，未核验）。"
   ],
   "conditions": [
    "毫米波劣势判断保留例外：除非创造出对毫米波透明的超膜建筑材料，这个就另当别论（P008）。",
    "适用场景限定在太空站、星球殖民地与卫星之间的高带宽通信，而非地面通用通信（P016）。",
    "P016 以更准确的说把可见光通信收窄为激光通信，并扩展至红外、紫外激光。",
    "长波优势的表述针对远距离通信大有好处，并非绝对结论（P006）。",
    "大气不可靠的论断针对大气层内传播，未涵盖真空或光纤场景（P009）。"
   ],
   "rhetoric_and_tone": "前半为网络口语调侃（说一个冷知识、哦、OK，不开玩笑了；最早是长城烽火啊。然后是军舰的灯语啊。可要比电报电话早几百几千年哦），三个短句排比并带语气词；中段转为条理清晰的科普解说，用首先、但是、所以推进；以设问自答（那么这是否意味着可见光通信一无是处呢？当然不是）完成转折；用第二人称拉近距离（你有没有看过…如果没有，那么你可以试试）；结尾以你总不能指望拉一根…光缆作口语化反证。",
   "unresolved_questions": [
    "本篇含 1 个图片节点（IMG001），图片内容未经核验，需人工/多模态复核。",
    "P007 中这个常常就是可见光了中的这个指代略含混（指光纤中传输的光，还是指可见光频段），可能影响对上下文的理解。",
    "超膜建筑材料仅作为假设提出，本文未说明其研究现状与可行性。",
    "作者未给出可见光通信的技术方案、设备或实验数据，也未提及任何具体研究机构或产品。",
    "P012 的酒精与水实验为类比说明，未说明其与大气折射率扭曲的对应关系。",
    "5G 频段之后可有效穿透的通信方式就已经到头了这一判断的依据，本文未给出标准或引用。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "说一个冷知识——在一切利用电磁波的通信方式之中，利用可见光通信的反而是最早的哦。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "最早是长城烽火啊。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P006", "quote": "波长越大，越能穿透和绕过障碍。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P007", "quote": "但是波长越长，有效带宽也就越小。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P008", "quote": "缩短到5G的频段，其实具有有效穿透力的通信方式就已经到头了。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "（除非我们创造出某些对毫米波透明的超膜建筑材料，这个就另当别论了）", "relation": "qualifies"},
    {"key": "E7", "paragraph_id": "P009", "quote": "问题是，可见光在大气层中传播非常不可靠。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P011", "quote": "问题在于大气不是均匀的。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P013", "quote": "这个冷热空气造成的折射率扭曲会严重干扰可见光传输的信号。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P015", "quote": "当然不是。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P016", "quote": "可见光通信——更准确的说，激光通信——非常适合星际信号传输。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P017", "quote": "甚至可以说是那个场景下的唯一选择", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["通信技术", "电磁波与光学", "航天通信"],
   "issue_candidates": ["可见光通信的可行性与适用场景", "波长与穿透力/带宽的权衡", "毫米波与可见光比较", "大气传输对光通信的干扰", "星际与卫星间激光通信"],
   "text_function_candidates": ["答疑", "科普解释", "评论", "调侃式开场"],
   "object_candidates": ["可见光", "无线电波", "长城烽火", "军舰灯语", "电报电话", "5G", "毫米波", "光纤", "激光", "太空站", "卫星", "超膜建筑材料"],
   "working_keywords": ["波长", "有效带宽", "穿透力", "折射率扭曲", "单向性", "超膜建筑材料", "星际信号传输", "红外/紫外激光"]
  },
  "status": "needs_reread",
  "image_checked": False,
  "notes": "本篇含 1 个图片节点（IMG001），图片内容未经核验，需图像核验；已读部分为正文文本。P007 中这个常常就是可见光了指代略含混，已在 unresolved_questions 登记。"
 },
 "1350987a": {
  "analysis": {
   "question_context": "提问者问：一两年前大火的 3D 打印建筑现在为何没动静了？是骗局吗？（Q001）。作者没有直接判定是否为骗局，而是给出路线判断：3D 打印在建筑上的应用不应该是打印混凝土，而应该是钢丝/缆骨架纺织焊接——以多股直径三毫米左右的高强高韧钢丝为基本单位，依靠打印头的拧绞、穿插、切断、接续和点焊能力构造钢缆级的有机结构，作为后续水泥浇筑或膜结构、轻质复合材料、管线设施组装的框架基础；并判定走速凝水泥路线是方向性错误、绝对的死路一条。作者随后以图片回应不可思议、不现实、不如人手工扎笼子的说法，并称图中作品远未达到该手段的上限、甚至可能没摸到下限。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "提出替代技术路线：建筑 3D 打印应是钢丝/缆骨架纺织焊接，以约 3 毫米高强高韧钢丝为单位，用打印头实现拧绞、穿插、切断、接续与点焊，构造钢缆级有机结构作为后续浇筑与组装的框架基础。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003"], "summary": "判定速凝水泥路线是方向性错误、绝对的死路一条，并以话只说到这里收住不再展开。", "role": "conclusion"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005"], "summary": "预设他人反应（不可思议、不现实、不如人手工扎笼子），并称给你们一点基本概念（随后为图片）。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P006", "P007", "P008"], "summary": "说明图片引自 Edoardo Tresoldi 作品、来自网络搜索；称这些作品还远远没有摸到该手段的上限，甚至可能连下限都没摸到。", "role": "qualification"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "3D 打印在建筑上的应用不应该是打印混凝土，而应该是钢丝/缆骨架纺织焊接：以多股直径三毫米左右的高强高韧钢丝为基本单位，依靠打印头的拧绞、穿插、切断、接续和点焊能力，构造钢缆级的有机结构，作为后续水泥浇筑或膜结构、轻质复合材料、管线设施组装的框架基础。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "走速凝水泥路线是方向性错误，绝对的死路一条。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者以话只说到这里收束，未在本文展开速凝水泥路线为何是死路的具体论证。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "opponent_view", "attribution": "opponent", "modality": "questioned", "statement": "被作者回应并反驳的质疑：很多人觉得这不可思议、不现实、不如人手工扎笼子。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "配图所示作品还远远没有摸到上述手段所能企及的上限，甚至可能连下限都没摸到。", "evidence": ["E5", "E6"]}
   ],
   "argument_steps": [
    "提出替代路线（P001）：把建筑 3D 打印的对象从混凝土改为钢丝/钢缆骨架的纺织焊接，并给出工艺动作与用途。",
    "否定既有路线（P002）：速凝水泥路线是方向性错误、绝对的死路一条。",
    "主动留白（P003）：话只说到这里，明白人应该知道怎么做了。",
    "引出质疑（P004-P005）：很多人觉得不可思议、不现实、不如人手工扎笼子，作者称给你们一点基本概念。",
    "以图为例（P006-P008）：图片引自 Edoardo Tresoldi 作品；称这些还远未达到该手段的上限，甚至可能连下限都没摸到。"
   ],
   "concept_usage": [
    {"term": "钢丝/缆骨架纺织焊接", "meaning": "作者主张的建筑 3D 打印路线：以多股约 3 毫米高强高韧钢丝为基本单位，由打印头完成拧绞、穿插、切断、接续与点焊，形成钢缆级有机结构。", "evidence": "P001", "ambiguity": "作者未说明该结构的力学性能、工艺参数、设备形态或已有实现。"},
    {"term": "打印头", "meaning": "具备拧绞、穿插、切断、接续和点焊五种动作能力的执行部件；作者将其作为该路线的关键。", "evidence": "P001", "ambiguity": "作者未说明该打印头是否已存在或需新研发。"},
    {"term": "速凝水泥", "meaning": "作者所指的现行建筑 3D 打印路线（打印混凝土），被判为方向性错误。", "evidence": "P002", "ambiguity": "作者未给出具体被批评的对象、厂商或案例。"},
    {"term": "框架基础", "meaning": "该钢丝骨架的定位：作为后续水泥浇筑、膜结构、轻质复合材料与管线设施组装的底层结构。", "evidence": "P001", "ambiguity": "与既有钢筋混凝土施工的关系本文未展开。"}
   ],
   "examples_and_targets": [
    "混凝土打印与速凝水泥路线（P002）：被否定的对象。",
    "多股直径三毫米左右的高强高韧钢丝、钢缆级有机结构（P001）：作者主张中的材料与结构。",
    "后续水泥浇筑、膜结构、轻质复合材料、管线设施组装（P001）：作者列举的后续用途。",
    "人手工扎笼子（P004）：被转述的质疑说法（钢筋笼绑扎的类比）。",
    "Edoardo Tresoldi 作品（P006）：作者配图引用的作品与作者名。",
    "图片节点 IMG001-IMG004（阅读包列出，未核验）：P006 所称图片，其内容无法在文本中确认。"
   ],
   "conditions": [
    "钢丝直径限定为三毫米左右，属约数（P001）。",
    "该路线被限定为后续水泥浇筑、膜结构、轻质复合材料与管线设施组装的框架基础，而非最终结构本身（P001）。",
    "作者主动限定论述范围：话只说到这里，不展开理由（P003）。",
    "对作品的评价带可能这一限定：甚至可能连下限都没摸到（P008）。",
    "配图作品的来源被限定为引自 Edoardo Tresoldi 作品、图片来自网络搜索，侵删（P006）。"
   ],
   "rhetoric_and_tone": "短促、断言式，用绝对的死路一条作最强否定；以话只说到这里，明白人应该知道怎么做了制造留白与圈内人暗示；用给你们一点基本概念引入图片；以远远没有摸到上限、甚至可能连下限都没摸到作递进式贬抑与抬升该手段的潜力；整体是技术主张加图片举证，不展开论证。",
   "unresolved_questions": [
    "本篇含 4 个图片节点（IMG001-IMG004），图片内容未经核验，需人工/多模态复核。",
    "P006 引用的 Edoardo Tresoldi 作品与该钢丝骨架打印手段的关系，正文未说明；图片所示究竟是手工艺术装置还是 3D 打印成果，无法从文本确认，需外部核查。",
    "作者未说明速凝水泥路线为何是方向性错误的具体理由（P003 明说不再展开）。",
    "提问中是否为骗局的问题，正文未直接回答。",
    "该钢丝骨架纺织焊接路线的工艺可行性、设备形态、成本与已有实践，本文未提供任何信息。",
    "P004 所转述质疑的具体来源（是否评论区）本文未说明。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "3D打印在建筑上的应用不应该是打印混凝土，而应该是“钢丝/缆骨架纺织焊接”", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "走“速凝水泥”路线是方向性错误，绝对的死路一条。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "话只说到这里，明白人应该知道怎么做了。", "relation": "qualifies"},
    {"key": "E4", "paragraph_id": "P004", "quote": "很多人觉得这不可思议，“不现实”，“不如人手工扎笼子”", "relation": "contradicts"},
    {"key": "E5", "paragraph_id": "P007", "quote": "而这些还远远没有摸到上面谈论的这个手段所能企及的上限。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P008", "quote": "甚至可能连下限都没摸到。", "relation": "qualifies"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["建筑技术", "增材制造", "材料与结构工艺"],
   "issue_candidates": ["3D 打印建筑的路线选择", "速凝水泥/混凝土打印路线的批评", "钢丝骨架纺织焊接方案", "3D 打印建筑行业停滞原因"],
   "text_function_candidates": ["答疑", "技术主张", "评论", "图文举证"],
   "object_candidates": ["3D打印", "混凝土", "速凝水泥", "钢丝/钢缆", "Edoardo Tresoldi", "水泥浇筑", "膜结构", "轻质复合材料"],
   "working_keywords": ["钢丝/缆骨架纺织焊接", "打印头", "拧绞", "穿插", "点焊", "速凝水泥", "框架基础", "高强高韧钢丝"]
  },
  "status": "needs_reread",
  "image_checked": False,
  "notes": "本篇含 4 个图片节点（IMG001..IMG004），图片内容未经核验，需图像核验；图片承担了本文的主要举证功能（P005 给你们一点基本概念之后即为图片），故 status=needs_reread、image_checked=false。P006 的 Edoardo Tresoldi 作品与所论手段的关系无法从文本确认，需外部核查。"
 },
 "e7441d0a": {
  "analysis": {
   "question_context": "提问者问：感觉我们财务部总是被欺负，是不是财务部在每一家公司都是弱势部门？（Q001）。作者不讨论财务部如何自保，而是把判断反过来下：财务部门受欺负的企业是没有前途的企业。作者用私司、无司两个自造词描述这类企业，理由是它无法进行估值、发债、发行股票、股权交易、期权激励、分红、资产重组等资产交易；进而把老板对财务规范性的意识视为格局的直接表现，并给出投资判断标准（第一看财务制度与财务团队地位，用成本问题的回答识别团队）和对个人的择业建议（可以暂栖，不可托付，只能作驿站）。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "提出判断：财务部门受欺负的企业没有前途；这类企业并非公司而是私司（只有老板一个私人知道底细），甚至是无司（连老板也不知道底细）。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005", "P006"], "summary": "理由：这类企业进行资产交易极其困难，估值、发债、发行股票、股权交易、期权激励、分红、资产重组都无法进行；不能进行这些金融操作等效于未长大即被阉割，注定没有前途，如同植物不能进入食物链上层一样必然。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008", "P009"], "summary": "老板是否对财务规范性和关键性有足够意识是格局最直接的表现之一，城府沟壑只是庸俗的江湖技能不足以成事；许多企业到可上市时才发现烂账算不清，这类东西不足为训。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011"], "summary": "总体判断：中国企业管理治理水平普遍不及格，退潮时会留下大片裸泳者；而财务制度稳健周全的企业，危机都是良机，可等下降周期捡尸体称霸。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P012", "P013", "P014"], "summary": "投资方法主张：业余投资人看团队、项目、业绩很不专业，第一条要看财务制度和财务团队的地位；财务制度有逻辑缺陷或财务团队无如朕亲临的地位，别的基本不用看，只是 ppt。", "role": "action_advice"},
    {"unit_id": "U006", "paragraph_refs": ["P015", "P016", "P017", "P018"], "summary": "尽调方法：从多个财务角度询问成本问题，答不出清晰稳健逻辑即可断言其不知道自己在干什么；创始人关于成本的认识深度决定性标定投资风险；对不成熟者可投人结善缘，对财务意识分明者含金量极高、踩坑风险小。", "role": "action_advice"},
    {"unit_id": "U007", "paragraph_refs": ["P019", "P020", "P021"], "summary": "个人择业建议：这类企业因时代局限占比太大，可以呆，但此非可托付之所，只是暂时栖身；不要付出职业道德成本、不要构建难以退出的羁绊、不要构造虚幻的安全感，只能作为寻找健全企业的驿站。", "role": "action_advice"},
    {"unit_id": "U008", "paragraph_refs": ["P022"], "summary": "企管答集、社科答集、科学答集、文艺答集为平台话题/收藏夹标签混入正文（lexical 未覆盖）。", "role": "transition"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "财务部门受欺负的企业，是没有前途的企业。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这类企业并非公司而是私司（只有老板自己一个私人知道底细），甚至可能是无司（连老板自己也不知道底细，只知道银行里大概还有多少现金）。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这类企业没有前途，是因为要进行资产交易极其困难：估值、发债、发行股票、股权交易、期权激励、分红、资产重组都无法进行。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在现代商业实践中无法进行上述金融操作，可以说等效于人还没长大就已经被阉割，注定不会有前途；这就像植物不可能进入食物链上层一样必然。", "evidence": ["E4", "E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "老板是否对财务规范性和关键性有足够意识，是老板格局最直接的表现之一；所谓城府沟壑只是庸俗的江湖技能，足以存身，不足以成事。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国企业管理治理水平普遍地不及格。", "evidence": ["E7"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "等退潮的时候，海滩上会留下大片裸泳者的尸体化为他人的肥料。", "evidence": ["E8"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对财务制度稳健周全的企业，危机都是良机；静静等着下降周期到来，捡对方的尸体就可以称霸。", "evidence": ["E9"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "很多业余投资人喜欢看团队、项目、业绩，这些做法都很不专业；第一条就要看财务制度和财务团队的地位。", "evidence": ["E10", "E11"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "财务制度存在逻辑缺陷、财务团队不具备必要专业性、或者没有如朕亲临的地位，别的基本不用看，看了也没有意义，只是 ppt 而已。", "evidence": ["E12"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "多从几个不同的财务角度询问项目团队关于成本的问题，若不能给出清晰逻辑稳健的回答，基本就可以断言这些人不知道自己在干什么；仅创始人对成本概念的认识深度这一个指标，就在决定性意义上标定团队的投资风险。", "evidence": ["E13"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对财务意识不成熟的项目不是不能投，但那是在投人、是在早期结个善缘，等其挫折促使其成熟后再通过提供制度资源换取更大投资收益，这才是投资机构的着力点。", "evidence": ["E14"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "项目逻辑有效且创始人财务意识分明的项目含金量极高；财务分明则项目哪怕一般般，踩坑的风险也很小。", "evidence": ["E15", "E16"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "从个人角度这类企业可以呆（因时代局限占比太大），但此非可托付之所；不要为它付出任何职业道德上的成本、不要构建难以退出的羁绊、不要给自己构造虚幻的安全感。", "evidence": ["E17", "E18"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这类地方只能作为寻找健全企业的驿站，绝对不能作为事业终点。", "evidence": ["E19"]}
   ],
   "argument_steps": [
    "反向立论（P001-P002）：财务部门受欺负的企业没有前途，并用私司、无司界定这类企业。",
    "自问自答给出理由（P003-P004）：为什么没有前途？因为资产交易与各类金融操作都无法进行。",
    "强化推论（P005-P006）：不能进行金融操作等效于未长大即被阉割，如植物不能进入食物链上层一样必然。",
    "归因到老板（P007-P008）：财务意识是格局的直接表现，城府沟壑不足以成事；企业到上市时才发现烂账算不清。",
    "总体判断与机会（P010-P011）：中国企业管理治理水平普遍不及格，退潮后裸泳者成肥料；财务稳健者危机即良机。",
    "给出投资标准（P012-P014）：第一看财务制度与财务团队地位；否则只是 ppt。",
    "给出尽调方法（P015-P018）：以成本问答识人；不成熟者投人结善缘，成熟者含金量极高。",
    "给出择业建议（P019-P021）：可以暂栖，不可托付，不作事业终点。",
    "平台标签（P022）：答集标签混入正文。"
   ],
   "concept_usage": [
    {"term": "私司", "meaning": "作者自造词：并非公司，只有老板自己一个私人知道底细的企业。", "evidence": "P002", "ambiguity": "作者未给出与法律意义上公司的严格界限。"},
    {"term": "无司", "meaning": "作者自造词，程度更重：连老板自己也不知道底细，只知道银行里大概还有多少现金可以取出来。", "evidence": "P002", "ambiguity": "与私司的边界及判断标准本文未说明。"},
    {"term": "财务团队的地位", "meaning": "作者给出的首要投资观察指标，用如朕亲临形容其应有权柄；地位不足则其余不必看。", "evidence": "P014", "ambiguity": "如朕亲临为比喻，未给出制度化的判定方式。"},
    {"term": "投人/结善缘", "meaning": "对财务意识不成熟的团队的投资方式：投的是人，等其受挫成熟后再以制度资源换取更大收益。", "evidence": "P016", "ambiguity": "未给出筛选标准与回报机制。"},
    {"term": "驿站", "meaning": "作者对财务不受重视企业的定位：只能作为寻找健全企业的中途落脚点，不能作为事业终点。", "evidence": "P021", "ambiguity": "未说明停留时长与退出时机的判断依据。"}
   ],
   "examples_and_targets": [
    "财务部门被欺负的企业与老板（P001、P002）：论述对象。",
    "估值、发债、发行股票、股权交易、期权激励、分红、资产重组（P004）：作者列举的无法进行的金融操作。",
    "植物不可能进入食物链上层（P006）：作者类比。",
    "裤子拉链拉不上、九条尾巴随风飘荡（P008）：作者的调侃式比喻。",
    "退潮后的裸泳者、尸体化为肥料、捡对方的尸体称霸（P010、P011）：作者的比喻性预测与策略。",
    "业余投资人、ppt（P012、P014）：被批评的对象与比喻。",
    "潜在市场容量与自身经营数据、成本核算（P015）：作者对业余团队数字的对比。",
    "中国企业管理治理水平（P010）：总体断言，待外部核查。",
    "企管答集、社科答集、科学答集、文艺答集（P022）：平台答集标签混入正文。"
   ],
   "conditions": [
    "判断限定在现代商业实践的语境下（P005）。",
    "个人建议的前提是时代局限使这类企业占比太大，故可以呆（P019）。",
    "投资判断用基本就可以断言、基本不用看等限定词，非绝对（P014、P015）。",
    "投人策略以等待他必然到来的挫折为前提，属作者的预测性前提（P016）。",
    "财务分明者踩坑风险小以项目哪怕一般般为让步条件（P018）。",
    "P011 的捡尸体称霸以对方在下降周期中失败为前提。"
   ],
   "rhetoric_and_tone": "断言式短句与密集比喻：私司/无司、未长大即被阉割、植物进不了食物链上层、连裤子拉链都拉不上、九条尾巴随风飘荡、退潮后的裸泳者与尸体肥料、捡尸体称霸、如朕亲临、只是ppt、驿站；用词贬抑（烂泥扶不上墙、不足为训、庸俗的江湖技能）；自问自答推进（为什么说没有前途？）；第二人称你/你们直接对话提问者与读者；对业余投资人的批评语气尖锐。",
   "unresolved_questions": [
    "P022 的企管答集、社科答集、科学答集、文艺答集为平台话题/收藏夹标签，lexical 未覆盖，属正文与结构不一致处。",
    "中国企业管理治理水平普遍地不及格为总体断言，本文未给出数据或调查来源，需外部核查。",
    "提问者所述财务部总是被欺负的具体情形，正文未复述。",
    "作者未给出财务部门如何改变弱势地位的行动方案，提问的另一半问题未被回答。",
    "如朕亲临的地位缺少制度化描述，无法据此操作。",
    "P016 的投人结善缘策略缺少具体案例或回报测算。",
    "P008 所述企业到上市时烂账算不清的情形为概括描述，未给出具体企业或案例。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "“财务部门受欺负”的企业，是没有前途的企业。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "而是“私司”——只有老板自己一个私人知道底细的企业。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "因为它要进行资产交易极其困难。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "可以说等效于人还没长大就已经被阉割，注定不会有前途。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "这个就像植物不可能进入食物链上层一样必然。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "是老板的格局最直接的表现之一。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P010", "quote": "中国企业管理治理水平普遍地不及格。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P010", "quote": "海滩上会留下大片裸泳者的尸体化为他人的肥料。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P011", "quote": "对财务制度稳健周全的企业，危机都是良机。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P012", "quote": "实际上这些做法都是很不专业的。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P013", "quote": "第一条就要看财务制度和财务团队的地位。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P014", "quote": "别的基本不用看，看了也没有意义，只是ppt而已。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P015", "quote": "仅仅创始人对“成本”概念的认识深度这一个指标就在决定性意义上标定团队的投资风险。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P016", "quote": "不是不能投，但是那是在投人，是在早期结个善缘。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P017", "quote": "这类项目的含金量都是极高的。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P018", "quote": "财务分明，项目哪怕“一般般”，踩坑的风险也很小。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P019", "quote": "从个人角度，这样的企业能不能呆？可以，毕竟因为时代局限，它占比太大了。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P020", "quote": "此非你可托付之所，不是你的归宿所在。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P021", "quote": "这些地方只能作为寻找健全企业的驿站，绝对不能作为事业终点。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P022", "quote": "企管答集", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["企业管理与公司治理", "风险投资", "财务制度", "个人职业选择"],
   "issue_candidates": ["财务部门地位与企业前途", "财务规范与资产交易能力", "投资尽调中的财务指标", "创始人的财务意识", "职业选择与企业可托付性"],
   "text_function_candidates": ["答疑", "评论", "经验总结", "训诫劝导"],
   "object_candidates": ["财务部", "老板", "私司/无司", "投资人", "创业团队", "上市企业", "中国企业管理", "企管答集"],
   "working_keywords": ["财务制度", "财务团队地位", "如朕亲临", "私司", "无司", "资产重组", "期权激励", "尽调", "成本核算", "驿站"]
  },
  "notes": "structure.divergence=true：text 尾部 chars 1154+ 的企管答集/社科答集/科学答集/文艺答集为平台话题/收藏夹标签混入正文、lexical 未覆盖，已按正文如实读出并登记。文中中国企业管理治理水平普遍不及格属作者总体断言，需外部核查。"
 },
 "b97da81b": {
  "analysis": {
   "question_context": "提问者问：有哪些简洁的人际交往模式？（Q001）。作者开宗明义否定问题前提——世界上并不存在简洁的人际交往原则——理由是篇幅短小的格言警句都面临严重的阐释问题。作者以永远不要讨好别人为例，追问讨好如何界定（鞠躬说欢迎光临、过节送礼算不算），再逐一追问标准来源（传统、祖训、大数据、感觉、身边朋友的平均值），并用永远不要过度自信、不要随大流等其他格言揭示其中的自相矛盾。结论是：用格言敷衍对稳健可持续的决策体系的探索是非常危险的懒惰，真正面对艰难决策时格言帮不上忙，最终导致反复、一事无成与焦虑的恶性循环。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "否定问题前提：世界上并不存在简洁的人际交往原则，因为篇幅短小的格言警句都面临严重的阐释问题。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005", "P006"], "summary": "以永远不要讨好别人为例，追问讨好的界定：客户进门鞠躬说欢迎光临算不算讨好，过节大包小包带礼物算不算讨好。", "role": "example"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008", "P009", "P010", "P011"], "summary": "逐一追问标准来源：是否存在过线即算的标准；标准是传统还是祖训；是大数据的平均值（而大数据与正确的关系复杂得很，按大数据鸦片战争前会显示大清绝不会输）；是感觉（则与永远不要过度自信冲突）；是身边朋友的平均值（则与不要随大流冲突）。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P012", "P013"], "summary": "判定用一条或几条格言敷衍对稳健可持续决策体系的探索是非常危险的懒惰；格言在艰难决策前完全帮不上忙，因其逻辑体系粗劣、经不起深刻追问。", "role": "conclusion"},
    {"unit_id": "U005", "paragraph_refs": ["P014", "P015"], "summary": "推论：迫不得已的艰苦再大也人人都能扛，似乎并不见得一定必要的艰苦再小也人人都扛不住；扛不住就时时反复，反复多了自然陷入一事无成。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P016", "P017", "P018"], "summary": "描绘后果：悔恨于当初把迷茫的焦虑用虚假答案麻醉过去；最终越焦虑越无法静心思考、越无法静心思考越对任何结论焦虑不安，无限循环往复，直通地狱。", "role": "conclusion"},
    {"unit_id": "U007", "paragraph_refs": ["P019"], "summary": "训诫式收束：那时候，你记住，曾经有人警告过你的。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "世界上并不存在简洁的人际交往原则。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在表达方式上篇幅短小的格言警句，都面临着严重的阐释问题。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "以永远不要讨好别人为例：什么叫作讨好并不清楚，客户进门鞠躬说欢迎光临、过节大包小包给亲戚朋友带礼物是否算讨好都无定论。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "若认为存在过线即算讨好的标准，则标准来源（传统、祖训、大数据、感觉、身边朋友的平均值）都无法成立，并与其他格言（永远不要过度自信、不要随大流）冲突。", "evidence": ["E5", "E6", "E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "大数据其实与正确的关系复杂得很；如果按照大数据，鸦片战争之前大数据会显示大清帝国绝不可能会输。", "evidence": ["E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "试图寻找一条或者几条简单的格言警句来敷衍对稳健可持续的决策体系的探索，是一种非常危险的懒惰。", "evidence": ["E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "格言在真正面对艰难决策时完全帮不上忙，因为其背后的逻辑体系太过于粗劣，一旦面对深刻的追问就会显示出苍白无力。", "evidence": ["E10"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "迫不得已的艰苦，再大也人人都能扛；似乎并不见得一定必要的艰苦，再小也人人都扛不住。", "evidence": ["E11"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "扛不住就会时时反复，反复得多了将自然而然陷入一事无成。", "evidence": ["E12"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "到那时明知不是办法却已无法平静探讨，越焦虑越无法静心思考、越无法静心思考越对任何结论焦虑不安，无限循环往复，直通地狱。", "evidence": ["E13", "E14"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "迷茫造成的焦虑本该用作扎实、严谨、反复地追问和锤炼的动力，却被随手抓起一些虚假的答案麻醉过去了。", "evidence": ["E15"]}
   ],
   "argument_steps": [
    "否定前提（P001-P002）：不存在简洁的人际交往原则，因为短格言有严重阐释问题。",
    "举例追问（P003-P006）：以永远不要讨好别人为例，追问讨好如何界定。",
    "假设与反驳（P007-P011）：若存在标准，则来源（传统、祖训、大数据、感觉、朋友平均值）逐一被质疑，并与其他格言自相矛盾。",
    "定性（P012）：用格言敷衍决策体系的探索是非常危险的懒惰。",
    "论证其无用（P013）：逻辑体系粗劣，面对深刻追问苍白无力；而决策之难源于事关重大的命运与苦难。",
    "因果推论（P014-P015）：非必要的艰苦人人都扛不住，反复则一事无成。",
    "后果描绘（P016-P018）：悔恨、焦虑与思考能力的恶性循环，直通地狱。",
    "训诫收束（P019）：曾经有人警告过你的。"
   ],
   "concept_usage": [
    {"term": "简洁的人际交往原则", "meaning": "提问所问的、可用简短格言表达的人际交往模式；作者否定其存在。", "evidence": "P001", "ambiguity": "作者未区分原则本身的复杂度与表述的简短性，批评集中在后者。"},
    {"term": "阐释问题", "meaning": "短格言因缺乏界定而在具体情境中无法确定适用范围（如讨好）。", "evidence": "P002", "ambiguity": "作者未给出解决阐释问题的替代方案。"},
    {"term": "大数据", "meaning": "作者借以指称以统计平均值为判断依据的做法，并称其与正确的关系复杂得很。", "evidence": "P009", "ambiguity": "作者未区分统计方法与数据质量，举例为修辞性反事实。"},
    {"term": "稳健可持续的决策体系", "meaning": "作者主张应替代格言的东西，需要扎实、严谨、反复的追问和锤炼；本文未展开其内容。", "evidence": "P012", "ambiguity": "作者只给出名称与要求，未给出体系构成。"}
   ],
   "examples_and_targets": [
    "永远不要讨好别人（P003）：被剖析的格言样例。",
    "客户进门鞠躬说欢迎光临、过节大包小包带礼物（P005、P006）：作者设想的界定疑难情景。",
    "传统、祖训、大数据的平均值、你的感觉、身边朋友的平均值（P008-P011）：作者逐一质疑的标准来源。",
    "永远不要过度自信、不要随大流（P010、P011）：被用来揭示自相矛盾的格言。",
    "鸦片战争之前大数据会显示大清帝国绝不可能会输（P009）：作者的修辞性反事实例证。",
    "无限循环往复，直通地狱（P018）：作者的比喻性后果描述。"
   ],
   "conditions": [
    "批评对象限定在表达方式上篇幅短小的格言警句（P002），而非一切原则。",
    "大数据质疑以如果按照大数据为前提假设（P009）。",
    "格言无用的论断限定在真正面对艰难的决策时（P013）。",
    "艰苦承受力的判断区分迫不得已与似乎并不见得一定必要两种情形（P014）。",
    "后果推断带预测性与必然性措辞（将自然而然地陷入、无限循环往复），非实证结论。"
   ],
   "rhetoric_and_tone": "训诫与警告语气，第二人称你贯穿；连续设问反问（那么什么叫作讨好？…算不算讨好？是传统？是祖训？）；以鸦片战争与大清帝国作反事实例证；句法排比与递进（越焦虑，就越无法静心思考；越无法静心思考，就越对任何结论都感到焦虑不安）；警句收束（无限循环往复，直通地狱；那时候，你记住，曾经有人警告过你的）营造预言式警告；整体是先破后立但立得很少，主要篇幅用于拆解格言。",
   "unresolved_questions": [
    "作者只否定简洁格言，未给出正面替代方案，提问所问的人际交往模式在本文中没有正面回答。",
    "稳健可持续的决策体系具体是什么，本文未展开。",
    "P009 的鸦片战争大数据举例为修辞性反事实，其与真实统计推断方法的关系未说明。",
    "P013 提到决策背后事关重大的命运和苦难，但未给出任何具体决策案例。",
    "P016-P018 的悔恨与焦虑循环为作者的预测性描绘，未给出经验依据。",
    "作者未说明阐释问题应如何解决（是否需要长文、定义或情境判断）。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "开宗明义，世界上并不存在“简洁的人际交往原则”。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "都面临着严重的阐释问题。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "随便举个例，比如，“永远不要讨好别人”。", "relation": "context"},
    {"key": "E4", "paragraph_id": "P005", "quote": "客户进门，鞠躬说“欢迎光临”算不算“讨好”？", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P008", "quote": "那么这标准确定的原则是什么？是传统？是祖训？", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P010", "quote": "那么“永远不要过度自信”这条要怎么办？", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P011", "quote": "那“不要随大流”这条要怎么办？", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "“大数据”其实与正确的关系复杂得很。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P012", "quote": "试图寻找一条或者几条简单的格言警句来敷衍对稳健可持续的决策体系的探索，是一种非常危险的懒惰。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P013", "quote": "因为它们背后的逻辑体系太过于粗劣，一旦面对深刻的追问，就会显示出苍白无力来。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P014", "quote": "迫不得已的艰苦，再大也人人都能扛；“似乎并不见得一定必要”的艰苦，再小也人人都扛不住。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P015", "quote": "扛不住，你就会时时反复。反复得多了，你将自然而然地陷入一事无成。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P017", "quote": "越焦虑，就越无法静心思考；越无法静心思考，就越对任何结论都感到焦虑不安。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P018", "quote": "无限循环往复，直通地狱。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P016", "quote": "却被你随手抓起一些虚假的答案麻醉过去了。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["人际交往", "决策方法论", "语言与格言"],
   "issue_candidates": ["格言警句的阐释问题", "是否存在简洁的人际交往原则", "标准来源（传统/大数据/感觉）的可靠性", "决策体系与艰苦承受"],
   "text_function_candidates": ["答疑", "论辩", "训诫劝导", "反面论证"],
   "object_candidates": ["格言警句", "讨好", "大数据", "传统", "祖训", "鸦片战争", "大清帝国"],
   "working_keywords": ["简洁的人际交往原则", "阐释问题", "讨好", "过度自信", "随大流", "稳健可持续的决策体系", "迫不得已的艰苦"]
  },
  "notes": "本篇无图片、无 text/lexical divergence。作者以否定提问前提为主，未给出正面替代方案；正文对鸦片战争与大数据的举例为修辞性反事实，非事实断言。"
 },
 "8a1cc032": {
  "analysis": {
   "question_context": "提问者问：不懂装懂的摩托盲都是什么样子？（Q001）。作者并未回答该问题，而是转向劝告：在中国不要玩摩托飞车。理由不是技术问题而是路况复杂——算不到货车掉落的货与沙土车落的沙，高速过弯时一把看不出来的沙、以及在高速下错估积水对抓地力的影响都可能致命；作者自述亲眼见过死亡事故，并在末段反驳某个鼓吹大排的答案，指出除哈雷戴维森这类低转速高出力大排外，一般公路赛大排不能在中国道路上安全行驶，除非找到专业赛道。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "结论与理由概述：在中国不要玩摩托飞车；这不是简单的技术问题，而是路况复杂。", "role": "conclusion"},
    {"unit_id": "U002", "paragraph_refs": ["P003"], "summary": "具体路况风险：算不到货车掉落的货与沙土车落的沙；高速过弯时一把完全看不出来的沙能要命；高速下错估积水对抓地力的影响也致命。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P004"], "summary": "以亲眼见过死亡事故作经验证言，警告不要拿生命开玩笑。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P005"], "summary": "反驳鼓吹大排的答案：除哈雷戴维森这类低转速高出力大排外，一般公路赛大排不能在中国道路上安全行驶，除非找到专业赛道。", "role": "rebuttal"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在中国不要玩摩托飞车。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这不是个简单的技术问题，而是路况复杂。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "你算不到哪里有货车掉落的货，也算不到哪里路面有过路沙土车落的沙；高速过弯时一把完全看不出来的沙能要人的命，错估积水对抓地力的影响在高速下也是致命的。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者自述亲眼见过死亡事故，因此不要拿生命开玩笑。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "除了哈雷戴维森这种低转速高出力大排，一般的公路赛大排是不能在中国的道路上安全行驶的——除非找到专业赛道。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "opponent_view", "attribution": "opponent", "modality": "questioned", "statement": "被作者反驳的他人观点：有个答案鼓吹大排。", "evidence": ["E6"]}
   ],
   "argument_steps": [
    "直接给出劝告（P001）：在中国不要玩摩托飞车。",
    "定性理由（P002）：不是技术问题，而是路况复杂。",
    "列举路况风险（P003）：掉落货物、过路沙土、积水与抓地力，均在高速下致命。",
    "经验证言（P004）：亲眼见过死亡事故，不要拿生命开玩笑。",
    "反驳与限定（P005）：反驳鼓吹大排的答案，并给出例外（哈雷戴维森式低转速高出力大排）与条件（除非找到专业赛道）。"
   ],
   "concept_usage": [
    {"term": "路况复杂", "meaning": "作者指中国道路上存在无法预判的掉落物、沙土、积水等，使风险超出骑手技术所能控制。", "evidence": "P002", "ambiguity": "作者未给出具体路段或统计。"},
    {"term": "大排（大排量摩托）", "meaning": "作者区分两类：哈雷戴维森这类低转速高出力大排，与一般公路赛大排；后者在中国道路上不能安全行驶。", "evidence": "P005", "ambiguity": "作者未给出排量界线或其他可适用车型。"},
    {"term": "专业赛道", "meaning": "作者给出的例外场所：只有在专业赛道上，一般公路赛大排才可安全行驶。", "evidence": "P005", "ambiguity": "未说明赛道条件与中国境内可得性。"}
   ],
   "examples_and_targets": [
    "货车掉落的货、过路沙土车落的沙（P003）：作者列举的路况风险。",
    "高速过弯与一把看不出来的沙、积水与抓地力（P003）：作者的风险机制说明。",
    "亲眼见过的死亡事故（P004）：作者自述经验（细节未说明）。",
    "鼓吹大排的答案（P005）：被反驳的他人答案，未具名。",
    "哈雷戴维森（P005）：被作者举为例外的品牌。",
    "专业赛道（P005）：作者给出的限定条件。"
   ],
   "conditions": [
    "劝告的地域限定为中国（P001）。",
    "对一般公路赛大排的否定带例外：除非找到专业赛道（P005）。",
    "例外车型限定为低转速高出力大排，并以哈雷戴维森为例（P005）。",
    "风险描述限定在高速过弯、高速下等工况（P003）。",
    "提问与正文的意图不一致：所问为不懂装懂的摩托盲的样子，正文为安全劝告。"
   ],
   "rhetoric_and_tone": "极简短篇，通篇断言与劝告；第二人称你拉近距离；用算不到…也算不到…的排比强调不可预判；以亲眼见过死亡事故、不要拿生命开玩笑作沉重的经验证言；对鼓吹大排的答案作不具名批评；没有调侃，语气严肃、警示。",
   "unresolved_questions": [
    "提问所问不懂装懂的摩托盲都是什么样子，正文未正面回答，问答意图不一致。",
    "作者自述亲眼见过死亡事故的具体情形、时间与地点，本文未说明。",
    "被反驳的鼓吹大排的答案未具名，无法回查其具体主张。",
    "哈雷戴维森被作为例外举出，但其是否确实适合中国道路，本文未展开论证。",
    "作者未给出替代车型建议或安全骑行的具体条件。",
    "文中未说明这些经验适用于哪些地区或路况类型。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "在中国不要玩摩托飞车。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "这不是个简单的技术问题，而是路况复杂。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "高速过弯，一把完全看不出来的沙能要人的命。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "亲眼见过死亡事故，不要拿生命开玩笑。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "一般的公路赛大排是不能在中国的道路上安全行驶的——除非找到专业赛道。", "relation": "qualifies"},
    {"key": "E6", "paragraph_id": "P005", "quote": "有个答案鼓吹大排的", "relation": "contradicts"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["摩托车与骑行", "道路交通安全", "风险警示"],
   "issue_candidates": ["中国道路摩托骑行风险", "大排量摩托的适用性", "路况与抓地力", "摩托盲与不懂装懂"],
   "text_function_candidates": ["答疑（未按提问作答）", "劝告", "批评", "经验证言"],
   "object_candidates": ["摩托飞车", "货车", "沙土车", "积水", "哈雷戴维森", "公路赛大排", "专业赛道"],
   "working_keywords": ["路况复杂", "掉落货物", "沙土", "抓地力", "大排", "低转速高出力", "专业赛道"]
  },
  "notes": "本篇无图片、无 text/lexical divergence。提问问的是不懂装懂的摩托盲的样子，正文实际写的是在中国不要玩摩托飞车的安全劝告，问答不一致，已登记于 unresolved_questions。"
 },
 "c0ef769d": {
  "analysis": {
   "question_context": "提问者问：嫉妒的根源是什么？（Q001）。作者以成功税为核心比喻作答：嫉妒的本质是一种成功税，可以理解为上帝通过对世界的规划和对历史的掌控，对人类的群体动力学机理做的设计，含义是对成功者和幸运儿强加缴税义务，确保赐福通过中间人的转移支付惠及人类总体。作者给出两条应对办法——A）使你的成功或幸运同时成为他人的福利；B）保持低调和隐形——并展开转交对象须精心挑选（否则如大衣哥般养出贪婪者）、抗拒则诅咒自动生效、避税则放弃权柄等推论，最后从人类起源论证嫉妒是文明成立的前提，并判定嫉妒与万有引力同属自然立法。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "提出核心命题：嫉妒的本质是一种成功税；以上帝的设计为喻，说明其含义是对成功者和幸运儿强加缴税义务，使赐福通过中间人的转移支付惠及人类总体。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005", "P006"], "summary": "应对办法A：使成功或幸运同时成为他人的福利；照办则权柄随之而来、受益者会本能地帮你抵御嫉妒并助你更成功；拒办则一切辩解都不能豁免负面攻击，攻击终将压倒抵抗。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008", "P009", "P010", "P011"], "summary": "转移支付对象须精心挑选：不能给得到利益反生贪婪者（大衣哥之误）；视角转换后，健康伦理观使人获得额外得福机会、社群拥有成功者友好的土壤；抗拒者诅咒自动生效、所到之处尽是敌人。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P012", "P013", "P014", "P015"], "summary": "应对办法B：保持低调和隐形；若严格保密并同时充分承担A条的成功税，可实现合法避税，但代价是放弃本来随之而来的权柄。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P016", "P017", "P018"], "summary": "积极解读：这不是变相惩罚而是有效的规约，限定了领取赐福的规则；拒绝承担责任或窃取成功税支付给亲信者，必亲手喂大将吞吃自己的野兽。", "role": "qualification"},
    {"unit_id": "U006", "paragraph_refs": ["P019", "P020"], "summary": "从人类起源论证：早在没有文字和语言时人类已有本能的嫉妒，它是铸成人类的模子上的一块，没有它人类无法有效共享群居生活的效率优势，也不会有语言、文字与之后的道德。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P021", "P022", "P023", "P024"], "summary": "收束：赞叹该设计简洁、可靠、低成本、完全去中心且不可抵抗；指出其与万有引力这样的自然立法同级，嫉妒是自然法所确立的成功税。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "嫉妒的本质是一种成功税。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "可以理解为上帝通过对世界的规划和对历史的掌控，对人类的群体动力学机理做了嫉妒这样一个设计，其含义是对成功者和幸运儿强加一项缴税义务，确保上帝的赐福能通过中间人的转移支付惠及人类总体。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "应对嫉妒的办法只有两个：A）使你的成功或幸运同时成为他人的福利；B）保持低调和隐形。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "必须让所有知道你成功的人从你的成功中分一杯羹，使你的成功同样成为ta们的成功；照办则权柄随之而来，受益者会本能地帮你抵抗嫉妒和敌意，并有本能驱动帮你更加成功。", "evidence": ["E5", "E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "若拒绝照办，只要成功变得众所周知，无论宣传嫉妒是不对的、这是我应得的、这是受法律保护的，都不能真正豁免负面攻击，这种自然生成且近乎无成本的攻击终将从规模与效能上压倒抵抗。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "转移支付的对象要经过精心挑选，不能兑现给得到利益不但不产生感激反而产生贪婪的人，否则嫉妒会变成对方的新财源——大衣哥就是犯了这个错误。", "evidence": ["E8", "E9"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "上天赐予成功不但限定了转交的义务，还限定了转交的对象；敢于抗拒则诅咒自动生效、如同附骨之蛆无处可逃，所到之处尽是敌人。", "evidence": ["E10", "E11"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "若能严格保密、保证成功只有很小的知情范围，同时又充分承担A条的成功税，就可以实现合法避税；但这等于放弃了本来随之而来的权柄，巨大成功本可带来的更大权柄会大幅缩小。", "evidence": ["E12", "E13"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "隐匿不是变相惩罚，反而是一种有效的规约，实际限定了领取赐福的规则：想要获得并长期稳定持有任何公共权柄，就必须长期明了这责任、无条件承担它，并运用全部智慧保证承担有效。", "evidence": ["E14"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "拒绝承担责任，或擅自窃取成功税支付给道德律不认可的自己亲信、指望贿赂保平安，就一定会亲手喂大将吞吃你的野兽。", "evidence": ["E15"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "上帝借着这人人仇恨、恐惧的绿眼睛的怪兽，确保了祂赐予一切幸运儿的福祉都不能被那个转交者轻松窃取。", "evidence": ["E16"]},
    {"claim_id": "C012", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "若非如此，人类的文明早已消亡——更准确地说，社会、集体这种文明现象一开始就无法成立；早在人类还没有文字和语言的时候，就已经有本能的嫉妒了。", "evidence": ["E17"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "嫉妒是铸成人类的模子上的一块；没有它，人类无法有效在群体内共享群居生活的效率优势，也就不会有群居的人类、语言、文字以及之后的一切道德。", "evidence": ["E18"]},
    {"claim_id": "C014", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "当你能看懂这个设计，你将不得不佩服这个世界的创造者——如果祂存在的话。", "evidence": ["E19"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "该设计简洁、可靠、低成本，完全去中心、不依赖任何特定机构、不依赖任何文化背书、不依赖释法和立法机制、不需要额外征税维持，而且完全不能抵抗、不容无视。", "evidence": ["E20"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "嫉妒这种约束与万有引力这样的自然立法是同级的；嫉妒是一种自然法所确立的成功税。", "evidence": ["E21", "E22"]}
   ],
   "argument_steps": [
    "定义（P001-P002）：嫉妒的本质是成功税，以上帝设计为喻说明其转移支付功能。",
    "给出两条办法（P003-P004）：A 使成功同时成为他人福利，B 保持低调和隐形。",
    "展开A（P005-P006）：照办得权柄与受益者护卫；拒办则无成本攻击终将压倒抵抗。",
    "限定A的对象（P007-P010）：转交对象须精选，不能给贪婪者；上帝既限定义务也限定对象。",
    "抗拒的后果（P011）：诅咒自动生效，处处是敌。",
    "展开B（P012-P015）：保密加承担成功税等于合法避税，但代价是权柄缩小。",
    "再解读（P016-P018）：这是有效的规约与领取赐福的规则；窃取者必自喂野兽，上帝以此确保福祉不被转交者窃取。",
    "人类起源论证（P019-P020）：嫉妒先于文字语言，是文明成立的条件。",
    "收束（P021-P024）：赞叹设计的简洁可靠，判定嫉妒与万有引力同级、属自然法。"
   ],
   "concept_usage": [
    {"term": "成功税", "meaning": "作者对嫉妒本质的定义：成功者与幸运儿被强加的一项缴税义务，须以转移支付方式使赐福惠及人类总体。", "evidence": "P001", "ambiguity": "为比喻性概念，作者未给出可计量的税率或征收标准。"},
    {"term": "转移支付", "meaning": "把成功带来的利益分给知情者与相关者，使成功同样成为ta们的成功。", "evidence": "P002", "ambiguity": "借用财政学术语，作者未界定支付形式与对象范围。"},
    {"term": "权柄", "meaning": "作者反复使用但未定义的概念，指随成功而来、可通过承担成功税获得的支配力；隐匿会使其缩小。", "evidence": "P005", "ambiguity": "本文未给出权柄的具体内容、来源与衡量方式。"},
    {"term": "合法避税", "meaning": "作者借用的说法：严格保密使知情范围极小，同时充分承担A条义务，从而避免嫉妒的攻击。", "evidence": "P013", "ambiguity": "与实际税法无关，属比喻用法，易被误读。"},
    {"term": "绿眼睛的怪兽", "meaning": "作者借以指称人人仇恨、恐惧的嫉妒本身。", "evidence": "P018", "ambiguity": "作者未说明该说法的出处。"},
    {"term": "自然法/自然立法", "meaning": "作者把嫉妒的约束与万有引力并列，视为不依赖机构、文化、立法而自动生效的规律。", "evidence": "P023", "ambiguity": "属作者的哲学判断，本文未给出论证依据。"}
   ],
   "examples_and_targets": [
    "上帝/天意/世界的创造者（P002、P018、P021）：作者隐喻框架中的主体，并以如果祂存在的话保留不确定。",
    "大衣哥（P008）：作者举出的现实例证（未说明事件细节）。",
    "嫉妒是不对的、这是我应得的、这是受法律保护的（P006）：作者列举的抗拒者辩解话术。",
    "附骨之蛆（P011）：比喻。",
    "绿眼睛的怪兽（P018）：对嫉妒的借称。",
    "吞吃你的野兽（P017）：比喻。",
    "铸成人类的模子（P020）：比喻。",
    "万有引力（P023）：作者用作自然立法的类比对象。",
    "人类的文字、语言与道德（P019、P020）：作者文明起源论述中的对象。"
   ],
   "conditions": [
    "上帝设计说以如果祂存在的话保留不可知论限定（P021）。",
    "人类文明论证以若非如此的反事实假设为条件（P019）。",
    "合法避税以同时满足严格保密与充分承担A条义务两个条件为前提（P013）。",
    "抗拒者的处境以只要你的成功变得众所周知为条件（P006）。",
    "转交对象限定为会产生感激者，排除得到利益反生贪婪的人（P008）。",
    "健康的伦理观是什么，作者明说这是另一个问题、不在这里展开（P009）。"
   ],
   "rhetoric_and_tone": "通篇以上帝、天意、赐福、诅咒、自然法与万有引力构建隐喻体系，同时借用税收与财政术语（成功税、缴税义务、转移支付、合法避税、额外征税）；比喻密集（附骨之蛆、绿眼睛的怪兽、亲手喂大将吞吃你的野兽、铸成人类的模子）；第二人称你贯穿并与ta们并用；用反问（你有没有看到这种约束的本质属性？）收束前半；对大衣哥的点评简短而直接；整体是宗教哲学式的论说与劝导，带有赞叹造物设计的语气，并以如果祂存在的话保留不确定性。",
   "unresolved_questions": [
    "上帝/天意设计是作者的隐喻框架还是实有神格的断言，文中以如果祂存在的话留下不确定，解释时需保留该歧义。",
    "健康的伦理观是什么，作者明说不在本篇展开（P009）。",
    "权柄的具体所指、来源与衡量方式，本文未界定。",
    "合法避税为作者的比喻用法，与实际税法无关，需防止误读。",
    "大衣哥所指的具体事件与情形，本文未说明，且大衣哥为公众人物的俗称，需外部核查。",
    "上帝的道德律如何界定、由谁解释，本文未说明。",
    "P012 B）保持低调和隐形仅一句展开，与A条的详略严重不对称。",
    "作者未给出成功税在经验层面的可检验形式或案例数据。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "嫉妒的本质是一种“成功税”。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "确保上帝的赐福能通过中间人的转移支付惠及人类总体。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "A）使你的成功或幸运同时成为他人的福利。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P012", "quote": "B）保持低调和隐形。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "从而使得你的成功同样成为ta们的成功。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P005", "quote": "那么权柄也会随之而来。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P006", "quote": "都不能真正的使你豁免负面的攻击。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P007", "quote": "你依照天意进行转移支付的对象要经过精心的挑选。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P008", "quote": "大衣哥就是犯了这个错误。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "还限定了你转交的对象。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P011", "quote": "诅咒就自动生效，如同附骨之蛆，无处可逃。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P013", "quote": "那么你将可以实现“合法避税”。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P014", "quote": "这样做的人也就等于放弃了本来随之而来的权柄。", "relation": "qualifies"},
    {"key": "E14", "paragraph_id": "P016", "quote": "你就必须长期的明了这责任、无条件的承担它", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P017", "quote": "你就一定会亲手喂大将吞吃你的野兽。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P018", "quote": "上帝确保了祂赐予一切幸运儿的福祉都不能被那个转交者轻松的窃取。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P019", "quote": "早在人类还没有文字和语言的时候，人类就已经有本能的“嫉妒”了。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P020", "quote": "那是铸成“人类”的模子上的一块", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P021", "quote": "如果祂存在的话。", "relation": "qualifies"},
    {"key": "E20", "paragraph_id": "P022", "quote": "完全的去中心、不依赖任何特定机构", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P023", "quote": "它与万有引力这样的自然立法是同级的。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P024", "quote": "嫉妒是一种自然法所确立的“成功税”。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["社会心理", "伦理与道德哲学", "宗教/自然法隐喻", "财富与社会关系"],
   "issue_candidates": ["嫉妒的根源", "成功的社会成本与转移支付", "财富与权柄的责任", "低调隐形的代价", "嫉妒与文明起源"],
   "text_function_candidates": ["答疑", "论说", "劝导", "隐喻式解释"],
   "object_candidates": ["上帝", "成功者与幸运儿", "大衣哥", "绿眼睛的怪兽", "万有引力", "人类", "社群"],
   "working_keywords": ["成功税", "转移支付", "缴税义务", "合法避税", "权柄", "自然法", "附骨之蛆", "绿眼睛的怪兽", "健康的伦理观"]
  },
  "notes": "本篇无图片、无 text/lexical divergence。全文以上帝/天意/自然法为隐喻框架，末段以如果祂存在的话保留不可知论限定，记录时未将其写成作者对神格存在的断言。大衣哥例证的具体事件未在正文说明，需外部核查。"
 },
 "ff44e691": {
  "analysis": {
   "question_context": "提问者问：可以用兵器打落射来的箭吗？（Q001）。作者直接给出答案——基本上不能——理由是正向飞来的箭在眼里只是一个不断放大的点。作者以 59 磅传统弓为例估算飞行时间，算出拦腰击中只有约 0.03 秒的时间窗口，并用按键小游戏类比该难度；随后说明挥动刀剑棍棒拦腰击打箭身的难度还远高于按键，并以町井勋居合斩 BB 弹的视频为例指出侧向视角看到的是线而非点、时间窗口掌握更易，属动作精度而非反应速度问题；结论是应以盾牌格挡或闪避应对，拨打是最下策。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "给出答案——基本上不能——并说明直觉理由：正向飞来的箭在眼里基本上只是一个不断放大的点。", "role": "conclusion"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006", "P007"], "summary": "以 59 磅传统弓估算：初速约 45 米/秒，保守算飞完 45 米匀减速到 30 米/秒，飞完 50 米约 1.2 秒；末端 30 米/秒、箭长算 100cm 时拦腰击中的时间窗口为 1/30 秒即 0.03 秒；并用直径从 1 毫米加速放大到 10mm 至 10.2mm 之间按按钮的小游戏作类比。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P008", "P009", "P010", "P011"], "summary": "说明按键难度仍大大低于挥动刀剑棍棒拦腰击打箭身，但即便如此成功率也会低得难以想象；并调侃若真能高概率做到，可去餐馆门口的停数字小游戏赢免单。", "role": "qualification"},
    {"unit_id": "U004", "paragraph_refs": ["P012", "P013", "P014"], "summary": "以町井勋居合斩 BB 弹的视频为例：发射方有意朝他身侧射击，站在射击轨迹旁边看到的是线而非点，令线进入刀的轨迹平面就能保证触碰到 BB 弹；故迎头斩 BB 弹在时间窗口掌握上反而比拦腰斩箭简单，主要是动作精度而非反应速度问题。", "role": "example"},
    {"unit_id": "U005", "paragraph_refs": ["P015", "P016", "P017"], "summary": "收束：既然已经站到侧面就没有必要拨打；看到箭是一个点时应以盾牌格挡或闪避，拨打真的是最下策。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "用兵器打落射来的箭，答案是基本上不能。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "因为正向你飞来的箭，在你眼里基本上只是一个不断放大的点。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "以 59 磅传统弓估算：正常箭的初速大约 45 米/秒，考虑减速保守按飞完 45 米匀减速到 30 米/秒，则飞完 50 米大概只需要 1.2 秒。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "末端速度 30 米/秒、箭长按 100cm 计算时，要拦腰打中箭只有 1/30 秒的时间窗口，也就是 0.03 秒。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "该挑战等价于在 1.2 秒的区段内踩中一个 0.03 秒的瞬间时段（以直径放大到 10mm 至 10.2mm 之间按按钮作类比）。", "evidence": ["E5", "E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这个挑战的难度仍然大大低于挥动刀剑棍棒拦腰击打箭身——毕竟只是按一下键而已。", "evidence": ["E7"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "即便只是按键，成功率也会低得难以想象。", "evidence": ["E8"]},
    {"claim_id": "C008", "claim_type": "author_reported", "attribution": "author", "modality": "asserted", "statement": "观察町井勋用居合斩拦截 BB 弹的视频会发现，发射方是有意朝他身侧射击。", "evidence": ["E9"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "站在射击轨迹旁边看到的不是点而是一条线，令线进入刀的轨迹平面就能保证刀触碰到 BB 弹；这个功夫虽然很难，但就时间窗口的掌握而言，迎头斩 BB 弹反而比拦腰斩箭简单，仍主要是动作精度而不是反应速度的问题。", "evidence": ["E10"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "站到侧面后，追蹤移动增长的线段是大脑非常擅长的，自然胜率会大增。", "evidence": ["E11"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "既然已经站到侧面就没有必要拨打；看到箭是一个点，要么用盾牌挡，要么最好闪避，拨打真的是最下策。", "evidence": ["E12", "E13"]}
   ],
   "argument_steps": [
    "直接给答案（P001-P003）：基本上不能，因为迎头飞来的箭只是一个不断放大的点。",
    "量化估算（P004-P005）：以 59 磅传统弓的初速、减速与箭长算出飞行时间与 0.03 秒时间窗口。",
    "类比与小游戏（P006-P007）：把拦箭换算成在 1.2 秒内踩中 0.03 秒的按键挑战。",
    "让步比较（P008-P011）：按键难度远低于挥刀拦腰击打，但成功率仍低得难以想象；并以餐馆小游戏调侃。",
    "引入反例（P012-P014）：町井勋斩 BB 弹的视频中射击是侧向的，看到的是线，时间窗口掌握更易，属动作精度问题。",
    "收束建议（P015-P017）：既已站到侧面就不必拨打；应以盾牌或闪避应对，拨打是最下策。"
   ],
   "concept_usage": [
    {"term": "不断放大的点", "meaning": "迎头飞来的箭在视觉上的呈现，因缺乏横向位移信息而无法据以判断与拦截。", "evidence": "P003", "ambiguity": "作者未讨论视觉训练能否改善。"},
    {"term": "时间窗口", "meaning": "箭身通过刀刃所在位置所需的时间，作者按箭长除以末端速度估为 1/30 秒。", "evidence": "P005", "ambiguity": "作者未逐步展示计算，也未讨论刃口宽度与命中容差。"},
    {"term": "动作精度与反应速度", "meaning": "作者用于区分两类难度的概念：拦腰斩箭难在反应速度，斩 BB 弹难在动作精度。", "evidence": "P013", "ambiguity": "两个概念均未量化定义。"},
    {"term": "拨打", "meaning": "用兵器格挡、拨开箭的动作；作者判定为最下策。", "evidence": "P017", "ambiguity": "与用盾牌格挡的区别本文未展开。"}
   ],
   "examples_and_targets": [
    "59 磅传统弓、45 米/秒初速、30 米/秒末端速度、100cm 箭长（P004、P005）：作者自设的估算参数。",
    "直径从 1 毫米放大到 10mm-10.2mm 的按键小游戏（P006）：作者设计的类比。",
    "餐馆门口停数字免单的小游戏（P010、P011）：作者的调侃性类比。",
    "町井勋用居合斩拦截 BB 弹的视频（P012）：作者引用的外部材料，并指出其拍摄角度。",
    "盾牌与闪避（P016）：作者给出的替代应对方式。"
   ],
   "conditions": [
    "结论带基本上这一限定，非绝对不可能（P001、P003）。",
    "估算参数为作者自设并声明保守：保守点算、箭长度我们算长一点吧，也偷点懒，算100cm（P004、P005）。",
    "按键小游戏的类比以直径放大到 10mm 到 10.2mm 之间为条件（P006）。",
    "餐馆小游戏的说法以如果你真的能高概率的做到为前提（P010）。",
    "斩 BB 弹较易的判断限定于就时间窗口的掌握而言，并强调仍主要是动作精度问题（P013）。",
    "侧向观察的优势以站到侧面为前提，而作者随即指出站到侧面就没有拨打的必要（P014、P015）。"
   ],
   "rhetoric_and_tone": "以量化估算支撑直觉判断，并自嘲式说明估算的偷懒之处（我们算长一点吧，也偷点懒）；用小游戏类比把概率问题形象化；调侃语气（你就可以饱食终日，吃成个快乐的肥仔了）；以町井勋视频为例时先指出拍摄角度，带有揭秘与反炫技意味；收束用短句下断语（拨打真的是最下策）；通篇第二人称你。",
   "unresolved_questions": [
    "59 磅传统弓、45 米/秒、30 米/秒、100cm 箭长等参数为作者自设，正文未给出测量来源，需外部核查。",
    "0.03 秒时间窗口的推算过程未逐步列出，且 1/30 秒本身为约数。",
    "町井勋居合斩 BB 弹视频的具体出处与拍摄信息，本文未给出，需外部核查。",
    "作者未给出任何成功拨箭的实例，也未讨论兵器类型（刀、棍、盾）对成功率的影响。",
    "迎头斩 BB 弹反而比拦腰斩箭简单为作者推断，未给出实验数据。",
    "餐馆小游戏为调侃性类比，与论题无直接关系。",
    "盾牌格挡的具体条件（是否随身携带、能否及时举起）本文未讨论。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "答案是——基本上不能。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "因为正向你飞来的箭，在你眼里基本上只是一个不断放大的点。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "59磅传统弓，正常的箭的初速大约45米/秒。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "你要拦腰打中它，有1/30秒的时间窗口，也就是0.03秒。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "如果在它的直径放大到10mm到10.2mm之间的时候，你瞬间按下按钮，就算拦截成功。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "就能拦腰拨开一只箭。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "这个挑战的难度仍然大大的低于挥动刀剑棍棒拦腰击打箭身", "relation": "qualifies"},
    {"key": "E8", "paragraph_id": "P009", "quote": "你的成功率也会低得难以想象。", "relation": "qualifies"},
    {"key": "E9", "paragraph_id": "P012", "quote": "就会发现发射方是有意朝他身侧射击。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P013", "quote": "这仍然主要是一个动作精度而不是一个反应速度的问题。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P014", "quote": "这时候你会发现你的大脑对分析这种运动非常擅长。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P016", "quote": "要么就是有盾牌用盾牌挡，要么最好闪避。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P017", "quote": "拨打真的是最下策。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["冷兵器与格斗", "反应与动作精度", "物理估算"],
   "issue_candidates": ["用兵器拨打箭的可行性", "时间窗口与反应极限", "动作精度与反应速度之分", "居合斩 BB 弹视频的解读"],
   "text_function_candidates": ["答疑", "估算论证", "解释", "调侃"],
   "object_candidates": ["箭", "兵器", "59磅传统弓", "町井勋", "BB弹", "居合斩", "盾牌", "餐馆小游戏"],
   "working_keywords": ["时间窗口", "初速", "末端速度", "动作精度", "反应速度", "居合斩", "不断放大的点", "拨打"]
  },
  "notes": "本篇无图片、无 text/lexical divergence。文中弹道与时间参数均为作者自设的估算口径（作者自称保守、偷懒），非实测数据，列为待外部核查。町井勋视频为外部材料，正文未给出链接或出处。"
 },
 "aa63aa65": {
  "analysis": {
   "question_context": "提问者问：你开始用香水后明白（获得）了什么？（Q001）。作者先声明不写香水审美，转而提出：喜欢什么香水主要是一个形成自我意识的认知过程，与香水本身的味道以及客观上好不好闻没多大关系，很大程度上与所预料的、所在意的人的反应相关，并给出我适合哪种香的判断法则。后半转向香水的礼仪问题：中国与欧美公共场合的默认不同，在中国应把香味压低到正常社交距离不太容易闻到的水平；并按大空间与小空间/封闭空间/紧挨就坐分场景给出用量与施用方式建议，结论是淡雅为上、香惊四座在中国不是好做法。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"], "summary": "不谈香水审美；喜欢某种香主要是形成自我意识的认知过程，与是否真的好闻几乎无关，而与所预料、所在意的人的反应相关；并给出我适合哪种香的判断法则。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P005", "P006", "P007", "P008"], "summary": "转入香水礼仪：东亚尤其是中国需注意何时何地可用；欧美默认用香水正常甚至礼仪场合必不可少，而中国一般场合默认无香，故应把香味压低到正常社交距离不太容易闻到的水平。", "role": "action_advice"},
    {"unit_id": "U003", "paragraph_refs": ["P009", "P010", "P011"], "summary": "分场景建议：大空间或开放空间可稍强；小空间、封闭空间或被迫紧挨就坐时应提前很久施用、高度控制用量，或喷在手帕上折叠放进胸兜之类；淡雅为上，香惊四座在中国不是好做法。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者不准备写关于香水审美的东西。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "喜欢什么香水主要是一个形成自我意识的认知过程，其实与香水本身的味道没多大关系；很大程度上和你脑海中所预料的、你所在意的人的反应相关。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "我相信我会喜欢喜欢这味道的人，所以我用这香来召唤ta——这就是我适合哪种香的全部实质判断法则；和客观上好不好闻几乎没有任何关系。", "evidence": ["E3", "E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "用香水要注意尺度：在东亚，尤其是中国，什么时候、什么地方可以用香水是一个需要掌握的问题。", "evidence": ["E5"]},
    {"claim_id": "C005", "claim_type": "author_reported", "attribution": "author", "modality": "asserted", "statement": "中国不像欧美，公共场合没有被香水占领；在欧美默认人用香水是正常的，甚至是一些礼仪场合中必不可少的部分，像领带一样。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在中国人们对一般场合默认是无香的，所以想用香水最好把香味压低到正常社交距离不太容易闻到的水平。", "evidence": ["E7"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "大空间或开放空间可以稍微强一点；小空间、封闭空间或被迫紧挨就坐的空间，应提前很久施用、高度控制用量，或者喷在手帕上再折叠起来放进胸兜之类。", "evidence": ["E8"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "淡雅为上；最好是只有能与你耳鬓厮磨的人才能闻得到你确切的是什么味道，这在中国才算是稳妥的用法。", "evidence": ["E9"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "香惊四座，并不是好的做法，在中国不是。", "evidence": ["E10"]}
   ],
   "argument_steps": [
    "划定范围（P001）：不写香水审美。",
    "提出自我认知论（P002）：喜欢某种香与味道、与客观好闻程度关系不大，而与所预料、所在意的人的反应相关。",
    "给出判断法则（P003-P004）：用香是召唤喜欢这味道的人，与客观好不好闻几乎无关。",
    "转入礼仪（P005-P006）：准备说香水的礼仪问题，尤其在东亚、中国需掌握尺度。",
    "地域对比（P007-P008）：欧美默认用香正常，中国一般场合默认无香，故应压低香味到社交距离不易闻到的水平。",
    "分场景建议（P009）：大空间可稍强，小空间或紧挨就坐应提前施用、高度控制或改用帕上喷香。",
    "收束标准（P010-P011）：淡雅为上，只有耳鬓厮磨者能闻到才是稳妥用法；香惊四座在中国不可取。"
   ],
   "concept_usage": [
    {"term": "自我意识的认知过程", "meaning": "作者对用香经验的定性：选择香水是借由预想他人反应来确认自我，而非对气味的客观评价。", "evidence": "P002", "ambiguity": "作者未展开这一认知过程的具体机制。"},
    {"term": "召唤", "meaning": "作者引号内用法：用某种香吸引喜欢这味道的人。", "evidence": "P003", "ambiguity": "为隐喻性表达，非实际功能描述。"},
    {"term": "无香（默认）", "meaning": "作者对中国一般社交场合气味预期的描述，与欧美默认用香相对。", "evidence": "P008", "ambiguity": "作者未给出调查依据，属经验性判断。"},
    {"term": "淡雅为上", "meaning": "作者给出的中国场景用香总原则，并以只有能与你耳鬓厮磨的人才能闻到为尺度。", "evidence": "P010", "ambiguity": "正常社交距离与耳鬓厮磨的具体距离未量化。"},
    {"term": "香惊四座", "meaning": "作者用以指香气浓烈、惊动周围人的用法，并判定在中国不是好做法。", "evidence": "P011", "ambiguity": "为四字化概括，未给出浓度标准。"}
   ],
   "examples_and_targets": [
    "香水审美（P001）：作者明确不写的范围。",
    "我相信我会喜欢喜欢这味道的人，所以我用这香来召唤ta（P003）：作者自拟并引号标出的判断法则。",
    "中国与欧美的公共场合气味默认（P007、P008）：作者的地域对比（需外部核查）。",
    "领带（P007）：作者用以类比欧美礼仪场合中香水地位的物件。",
    "大空间、开放空间、小空间、封闭空间、被迫紧挨就坐的空间（P009）：作者分场景建议的对象。",
    "喷在手帕上再折叠起来放进胸兜（P009）：作者给出的具体做法。",
    "耳鬓厮磨（P010）：作者形容亲密距离的用语。"
   ],
   "conditions": [
    "自我认知论带很大程度上这一限定，非全称判断（P002）。",
    "与客观好不好闻的关系用几乎没有任何关系作限定（P004）。",
    "礼仪建议的地域限定为东亚，尤其是中国（P006）；欧美情形作为对比出现（P007）。",
    "用量建议按空间类型分条件给出：如果是大空间或者开放空间…如果是小空间、封闭空间或者被迫紧挨就坐的空间（P009）。",
    "稳妥用法的判据限定为中国（P010），香惊四座的否定同样限定在中国不是（P011）。"
   ],
   "rhetoric_and_tone": "开篇以否定式划定范围（不准备写那些关于香水审美的东西），随后以引号内的第一人称自拟句（我相信我会喜欢喜欢这味道的人，所以我用这香来召唤ta）替代论证；中国与欧美的对比简明扼要；建议部分用最好、应该注意、干脆等祈使与程度词；以耳鬓厮磨作亲密距离的形象表达，以香惊四座作四字反面概括；语气是经验分享与礼仪规劝，非训诫。",
   "unresolved_questions": [
    "提问所问了开始用香水后明白了什么，作者给出的是认知判断与礼仪建议，未叙述个人使用经历或具体事件。",
    "brief 字段在语料中截断于这就是，正文 P003 为完整句，已以正文为准。",
    "中国一般场合默认无香、欧美默认用香正常这两项判断的依据与出处，本文未给出，需外部核查。",
    "正常社交距离的具体尺度未量化，读者难以据此操作。",
    "除喷在手帕上折叠放进胸兜之外，作者未列举其他做法或香水类型选择。",
    "作者未说明这些礼仪建议来自个人经验、观察还是其他来源。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "不准备写那些关于香水审美的东西。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "很大程度上和你脑海中所预料的、你所在意的人的反应相关。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "这就是“我适合哪种香”的全部实质判断法则。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "和客观上“好不好闻”几乎没有任何关系。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "注意掌握好这个尺度——在东亚，尤其是中国，什么时候、什么地方你可以用香水？", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "在欧美默认人用香水是正常的", "relation": "context"},
    {"key": "E7", "paragraph_id": "P008", "quote": "所以在中国如果你想用香水，你最好把香味压低到正常社交距离不太容易闻到的水平。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P009", "quote": "如果是小空间、封闭空间或者被迫紧挨就坐的空间，那么你应该注意要提前很久施用", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P010", "quote": "淡雅为上。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P011", "quote": "香惊四座，并不是好的做法，在中国不是。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["生活方式", "社交礼仪", "嗅觉与自我认知"],
   "issue_candidates": ["香水的自我意识功能", "香水使用的场合与用量", "中国与欧美的香水礼仪差异", "淡雅为上的用香标准"],
   "text_function_candidates": ["答疑", "经验总结", "礼仪建议"],
   "object_candidates": ["香水", "中国", "东亚", "欧美", "手帕", "胸兜", "领带"],
   "working_keywords": ["自我意识", "召唤", "好不好闻", "礼仪", "社交距离", "淡雅为上", "香惊四座", "耳鬓厮磨"]
  },
  "notes": "本篇无图片、无 text/lexical divergence。brief 字段在语料中截断（止于这就是），正文 P003 完整，记录以正文为准。文中关于中国与欧美公共场合用香默认的判断为作者经验性描述，需外部核查。"
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
