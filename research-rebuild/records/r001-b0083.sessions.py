# -*- coding: utf-8 -*-
"""批次 r001-b0083 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0083.sessions.py            # 写 out/r001-b0083.out.jsonl
  python3 records/r001-b0083.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0083"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0083.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "bf4744c2": {
  "analysis": {
   "question_context": "提问者问『老公/男朋友做了哪件事，让你有「这辈子就是他了」的感觉？』，即以伴侣某件令人感动的具体事件作为托付终身的判据。作者（答主）未按此预设作答，而是反驳把『体贴入微』的暖心事当成决定婚姻关系的关键事件，主张改以对方对待他人的态度为参照。提问立场属提问者，作者未予认可。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "作者说明作答缘由：看过大量答案后，发现多数答案把一件令人感动的体贴暖心事当成决定婚姻关系的关键事件。", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005", "P006", "P007"], "summary": "作者主张：与对方预期可得的性价值、社会价值、情绪价值相比，体贴入微的成本微不足道；以传统婚姻观下女性承担的家庭义务与女方社会资源（独生女可达千万量级）作对比，推论『良好服务十八个月就可以赚一千万』，并假设公开招标则体贴程度难以想象。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P008", "P009"], "summary": "让步与限定：作者承认这些事至少证明体贴能力不差，但用来作为托付终身的依据远远不够。", "role": "qualification"},
    {"unit_id": "U004", "paragraph_refs": ["P010", "P011", "P012", "P013", "P014", "P015"], "summary": "作者主张应观察对方如何对待不理解、不认同、不友好的人，对陌生人、网络上意见不同者、辜负自己者，并以连续反问要求读者自省；认为这比对自己体贴重要得多。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P016"], "summary": "以『勿谓言之不预』作警示收束。", "role": "conclusion"},
    {"unit_id": "U006", "paragraph_refs": ["P017", "P018", "P019", "P020", "P021", "P022"], "summary": "作者界定所观察者是『可持续的善良』：仅『善良』常出于对离群的焦虑与被敌对的脆弱，会招来觊觎撕咬、靠消耗自身网络资源维持，直到维持不下去而性情转变，也可能变得成熟而可持续，故『将来尚有一变』；可持续的善涉及可做与不可做、帮谁、以何方式帮、如何帮而不使对方生贪婪心等课题。", "role": "definition"},
    {"unit_id": "U007", "paragraph_refs": ["P023", "P024"], "summary": "行动建议：不推荐早婚；若要早婚须有意识地多加修炼、加深价值观的自我拷问并着力于『可持续』；不要照抄含含糊糊且大概率数学上不可持续的传统主流观点。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "与对方预期会获得的性价值、社会价值、情绪价值相比，这些『体贴入微』的成本微不足道。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国传统婚姻观里女性几乎可视为实质的家养奴隶；现代虽有改观，但女性承担的家庭义务与女方付出的社会资源（尤其独生女）是折合总量极其巨大的财富。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "若为城市中产阶级家庭（两代人均自有住房）的独生女且有985、211本科以上学历，这笔财富规模在千万起步不稀奇。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这类体贴表现作为『托付终身』的依据远远不够。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一个人对能给自己一千万的人有多体贴，完全不该是给ta这一千万的理由。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对方如何对待不理解、不认同甚至不友好的人，远比其对待能给自己性快感、价值认同、经济分担、情感支持的人的态度更有参考意义。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者连续反问读者是否观察过对方对陌生人、网络论坛上意见不同者以及辜负自己者的态度。", "evidence": ["E7"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "仅仅是『善良』常常反映内心对离群的焦虑和对被敌对的脆弱，这种善良会招来越来越多的觊觎和撕咬，往往持续不下去。", "evidence": ["E8"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "这种仅靠消耗维持的善良并非必然终局：也有很大可能变得成熟而可持续起来，故将来尚有一变。", "evidence": ["E9", "E10"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "可持续的善是一个相当复杂的问题，涉及什么可做、什么做不了、能帮谁、以什么方式帮、如何帮了而不使对方生出贪婪心等一系列课题。", "evidence": ["E11"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不推荐早婚；如果想早婚，要有意识地多加修炼、加深价值观的自我拷问，并在『可持续』上花极大精力。", "evidence": ["E12"]},
    {"claim_id": "C012", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "不要拿着『传统主流观点』直接照抄，那些观点往往含含糊糊而且数学上大概率不可持续。", "evidence": ["E13"]}
   ],
   "argument_steps": [
    "说明语境：所读答案多把体贴暖心事当作决定婚姻关系的关键事件（P001-P002）。",
    "换算成本：以对方可得的性价值、社会价值、情绪价值为对照，指出体贴成本微不足道（P003）。",
    "举例放大：以传统婚姻观下女性的家庭义务与社会资源转移、独生女千万量级财富作论据（P004-P005）。",
    "推论：客观上『对你良好服务十八个月就可以赚一千万』；若公开招标则体贴无下限（P006-P007）。",
    "让步：承认体贴证明能力不差，但不足以作托付终身的依据（P008-P009）。",
    "转向替代判据：应看对方如何对待不能给予其利益的人（P010-P011），连问三句要求读者自省（P012-P014）。",
    "警示：『勿谓言之不预』（P016）。",
    "定义：把观察对象界定为『可持续的善良』，并说明仅『善良』的机制与两种走向（P017-P021）。",
    "列举课题：可持续的善涉及可做/不可做、帮谁、如何帮而不生贪婪心等（P022）。",
    "结论与行动建议：不推荐早婚；若早婚须自我修炼与价值观拷问，不要照抄传统主流观点（P023-P024）。"
   ],
   "concept_usage": [
    {"term": "体贴入微", "meaning": "指关系中令人感动的暖心服务行为；作者将其与对方可得的性价值、社会价值、情绪价值对照，视为低成本投入。", "evidence": "P003", "ambiguity": "作者并未全盘否定其价值（P008 承认其证明体贴能力），只是否认其作为托付终身的依据。"},
    {"term": "托付终身", "meaning": "以婚姻把终身交给对方；本文讨论其判断依据是否充分。", "evidence": "P009", "ambiguity": "无"},
    {"term": "可持续的善良", "meaning": "作者提出的判据：能长期维持而不靠消耗自身网络资源的善良；与仅『善良』相对。", "evidence": "P019", "ambiguity": "作者称其为『相当复杂的问题』（P022），未给出完整判据。"},
    {"term": "性价值、社会价值、情绪价值", "meaning": "作者用来衡量关系中对方预期所得的三类价值。", "evidence": "P003", "ambiguity": "三类价值均未逐一定义。"},
    {"term": "家养奴隶", "meaning": "作者对中国传统婚姻观下女性处境的比喻性描述。", "evidence": "P004", "ambiguity": "作者随即称『现代虽有改观』。"}
   ],
   "examples_and_targets": [
    "城市中产阶级家庭（两代人均自有住房）的独生女且有985、211本科以上学历 —— 作者的条件性例证（P005）。",
    "『千万起步』的财富规模与『对你良好服务十八个月就可以赚一千万』 —— 作者的估算与推论，未给出来源（P005、P006）。",
    "『把这张榜单贴出去，公开招标』 —— 作者的假设性类比（P007）。",
    "陌生人、网络论坛上意见不同的人、辜负自己的人 —— 作者建议的观察对象（P012-P014）。",
    "『传统主流观点』 —— 作者建议不要直接照抄的对象（P024）。"
   ],
   "conditions": [
    "若为城市中产阶级家庭（两代人均自有住房）的独生女且有985、211本科以上学历，财富规模千万起步不稀奇（P005）。",
    "『如果你把这张榜单贴出去，公开招标』为假设情形（P007）。",
    "让步条件：作者承认体贴之事至少证明了体贴能力不差（P008）。",
    "若想早婚，则须有意识地多加修炼并加深价值观的自我拷问（P023）。",
    "概率限定：传统主流观点『往往是』含含糊糊、『大概率』数学上不可持续（P024）。"
   ],
   "rhetoric_and_tone": "训诫与提醒口吻，直接以『你们』称呼读者；『不得不提醒你们一个关键的问题』引入；以重复递进强调（『远、远、远、远、远远的不够』『重要得多得多得多得多』）；设问与连续反问（『这意味着什么？』以及三句『有观察……吗？』）；末段前以『勿谓言之不预』作警示；『不客气的讲』为插入性口语。整体是反驳提问预设并给出替代判据。",
   "unresolved_questions": [
    "提问者期待的是『某件具体的事』，作者未提供自己的正面事例，只给判据，故本篇不含个人叙事。",
    "P005 的『千万起步』财富估算与 P006 的『十八个月赚一千万』推论无计算依据或来源，属作者断言，待外部核查。",
    "作者性别与身份未在正文说明；提问面向伴侣作答者，不得据此推定作者身份。",
    "『可持续的善良』的判据与失败边界，正文只列举课题，未给出可操作标准。",
    "brief 与正文前段文字一致但被截断；provenance/superseded 均为 null，无版本差异信息。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P003", "quote": "这些“体贴入微”的成本是微不足道的", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P004", "quote": "女性几乎可以视作实质的家养奴隶", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P005", "quote": "这笔财富规模在千万起步不稀奇", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P009", "quote": "这种表现拿来作为“托付终身”的依据", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P010", "quote": "完全不该是给ta这一千万的理由", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P011", "quote": "远比ta对待能给ta性快感、价值认同、经济分担、情感支持的人的态度有参考意义得多", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P012", "quote": "你们有仔细观察ta对陌生人的态度吗？", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P020", "quote": "仅仅是“善良”，常常反映的是内心对离群的焦虑和对被敌对的脆弱", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P020", "quote": "当然也有很大可能是变得成熟而可持续起来", "relation": "qualifies"},
    {"key": "E10", "paragraph_id": "P021", "quote": "也就是说将来尚有一变。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P022", "quote": "如何帮了而不使对方生出贪婪心等等一系列的课题", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P023", "quote": "因此，不推荐早婚。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P024", "quote": "那些观点往往是含含糊糊而且数学上大概率不可持续的", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["婚姻与家庭", "亲密关系", "社会伦理"],
   "issue_candidates": ["婚姻决策依据", "体贴行为的价值评估", "善良的可持续性", "早婚", "传统婚姻观下女性的家庭义务"],
   "text_function_candidates": ["答疑（反驳式作答）", "评论", "训诫/劝告"],
   "object_candidates": ["城市中产阶级独生女", "985/211学历者", "中国传统婚姻观", "知乎答题者群体（『你们』）"],
   "working_keywords": ["体贴入微", "托付终身", "可持续的善良", "性价值", "社会价值", "情绪价值", "家养奴隶", "勿谓言之不预"]
  },
  "notes": "知乎问答回答；question 属提问者，作者实际是反驳提问预设。正文 24 段，text 与 lexical 无分歧（divergence=0），无图片节点，故 image_checked=false 不影响 status=read。brief 为正文前缀的截断文本，仅作导航。"
 },
 "c0a13aa7": {
  "analysis": {
   "question_context": "提问者问『有没有可以隐晦表示我爱你的句子？』（Q001，属提问者语境）。作者（答主）全文仅以一句『这怪我。』作答，未作说明、举例或论证；该句与提问的关系只能依语境推断，正文本身未交代。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "全文只有一句『这怪我。』，作为对该提问的回答，无任何展开、解释或限定。", "role": "other"}
   ],
   "main_claims": [],
   "argument_steps": [
    "本文无论证推进：正文仅一句『这怪我。』，既无前提、理由、例证，也无结论展开（P001）。"
   ],
   "concept_usage": [
    {"term": "这怪我", "meaning": "本文唯一语句，字面意为把责任归于自己；作者未在正文说明它与『隐晦表示我爱你』的关系。", "evidence": "P001", "ambiguity": "含义与功能完全依赖提问语境，正文未交代，存在多种解释可能。"}
   ],
   "examples_and_targets": [
    "本文未给出任何例子、人物、事件、机构、历史叙述或数据（P001 仅为一句作答）。"
   ],
   "conditions": [
    "本文未说明任何条件、场景、时间、对象或限定。"
   ],
   "rhetoric_and_tone": "极简、口语化的单句作答；无称呼、无论证、无修饰，语气平淡。是否含自嘲、玩笑或含蓄表白的修辞意图，正文无可判定依据。",
   "unresolved_questions": [
    "正文仅 4 个汉字，无法确定作者是否以『这怪我。』作为『隐晦表示我爱你』的例句，抑或另有他意；不应代为补全解释。",
    "该短句与该提问的关联需人工复核；本篇无可据以建立主张的完整陈述。",
    "正文是否为完整回答无法确认：lexical 只有 1 个 paragraph 节点、无图片节点，语料层未见截断或删减痕迹，但平台侧删除或折叠无法从语料排除。",
    "brief 与正文同为一句话『这怪我。』，未提供额外语境；provenance/superseded 均为 null。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "这怪我。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["情感表达", "亲密关系"],
   "issue_candidates": ["隐晦表达爱意的句子"],
   "text_function_candidates": ["答疑（极简作答）"],
   "object_candidates": ["unknown"],
   "working_keywords": ["这怪我", "隐晦", "我爱你"]
  },
  "notes": "正文极短（4 字），无图片节点，status 依简报默认 read：已读完该篇全部正文（full_text_checked=true）。但内容近乎无正文、无可提取的明示主张，故 main_claims 留空，其解释空缺登记在 unresolved_questions。"
 },
 "0242735c": {
  "analysis": {
   "question_context": "提问者引述微信朋友圈论调『孩子，我宁愿欠你一个快乐的少年，也不愿看到你卑微的成年』并问如何看待（Q001，其中论调属提问者引述，非作者主张）。作者不讨论该交换是否值得、该不该做，而主张这本来就不该是交换关系：学习与工作本身应是人生至乐；并进一步界定『学会喜欢学习』不是给苦药加糖，而是爱上艰难之事本身，最后给出以『练功夫』（如徒手剥毛豆）养成该心态的具体指引。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005"], "summary": "作者主张要害不在交换值不值得，而在于本不该是交换关系；学习本身应是人生至乐、工作本身应是快乐源泉；用痛苦学习换逸乐人生行不通——即使熬到才高八斗，也只会找到压力巨大而迷茫的苦工，仍不愿做、仍苦闷或因不愿而无业困窘。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P006", "P007", "P008", "P009", "P010", "P011", "P012", "P013"], "summary": "作者补上另一种要害：『学会喜欢学习』不是把学习这味苦药撒上糖，不是『七点前默写完爸爸周末就带你去海洋公园』，不是多媒体化、互动化、趣味化、娱乐化；那如咖啡加奶加糖变成咖啡风味奶茶，爱喝的人爱的是奶茶而非咖啡；人真正应爱上的是艰难之事本身，爱咖啡就该爱咖啡的苦。", "role": "definition"},
    {"unit_id": "U003", "paragraph_refs": ["P014", "P015", "P016"], "summary": "以短句给出理由与气势化表述：难度不足的事不屑于做；不折磨哪有坚韧，没有坚韧幸福就全靠躲，坚韧的人靠的是对惊涛骇浪视如等闲。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P017", "P018", "P019"], "summary": "作者主张子女『学知识』只该是为了学会反复挑战智力极限的快乐，『学没学会那个知识』根本不那么重要；学习成瘾、工作成瘾则功名利禄如浮云。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P020", "P021", "P022", "P023", "P024", "P025"], "summary": "推论与预测：挑工作不再看待遇报酬而看有无挑战性；配得上你、能引起你兴趣的工作没有不赚钱的；把过程录下来流量百万、切成十二段流量1200万；因而不必怕穷、不必用不快乐的童年换快乐的成年；学明白了就什么都不怕。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P026", "P027", "P028", "P029"], "summary": "以假设处境为例：被发配养猪也会兴奋；断腿会琢磨3D打印假肢；高位截瘫会研究眼皮发摩斯电码与舌控指点杆（并声明创意禁止剽窃）；归结为『世界上哪有无趣之事，无趣的是人』。", "role": "example"},
    {"unit_id": "U007", "paragraph_refs": ["P030", "P031", "P032", "P033", "P034", "P035", "P036", "P037", "P038", "P039"], "summary": "条件与前提：问题在于怎么让子女爱上这种精神冲浪的感觉——那需要你自己是这样的人，要有超越一般价值而热爱的东西、无需物质报酬就已足堪享受的神性享乐、神乎其技的东西、呕心沥血物我两忘的爱；并希望读者遇到能引其进入该境界的人，遇到了绝不要放过。", "role": "qualification"},
    {"unit_id": "U008", "paragraph_refs": ["P040"], "summary": "以芭蕾票之贵作为该境界价值的例证。", "role": "example"},
    {"unit_id": "U009", "paragraph_refs": ["P041", "P042", "P043", "P044", "P045", "P046", "P047", "P048", "P049", "P050", "P051", "P052", "P053", "P054", "P055", "P056", "P057", "P058", "P059"], "summary": "行动指引：这种心态的养成除天意际遇外，可做的一件事是带领孩子练功夫（明确不是指练武术）；以『徒手剥毛豆可以有多快』为题，买十斤毛豆分二十堆研究，并连续追问观察与操作成本、动作数能否递减、豆子不弹出碗、不必用眼指引、不伤指甲不打泡、能否永远看到下一个可改进点。", "role": "action_advice"},
    {"unit_id": "U010", "paragraph_refs": ["P060", "P061", "P062", "P063", "P064", "P065", "P066", "P067", "P068"], "summary": "其他练习例证：让孩子跟着经历过程；学毛笔字把『永』字练到透、练到气韵流动筋骨十足，学会批判自己的成果、创意解决问题、体会问题的改善；削铅笔练到不断芯、无一刀多余；练线条圆转如意；练抓黄豆每把重量一样；练解二元一次方程目测有解无解。", "role": "action_advice"},
    {"unit_id": "U011", "paragraph_refs": ["P069", "P070", "P071", "P072", "P073", "P074"], "summary": "结论：先沉浸在功夫的世界里，有功夫自然锥置囊中、颖脱而出，然后庖丁解牛、举重若轻，直到任何事情只要动念必易成功；此『成功』指成就功夫而非取得功勋；出手成功的人无庸碌之辈；以『去剥剥毛豆看看』收束。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "该论调的要害不在于这个交换值不值得、该不该做，而在于这本来就不该是交换关系。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "学习本身就应该是人生至乐，工作本身就应该是人生的快乐源泉。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "『用痛苦的学习去换取逸乐的人生』事实上交换不了：即使熬到才高八斗，也只会找到同样压力巨大而迷茫的苦工，一样不愿做、一样苦闷或因不愿而无业困窘。", "evidence": ["E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "『学会喜欢学习』不是给学习这味苦药撒糖，不是用奖励作交换（如七点前默写完就去海洋公园），也不是多媒体化、互动化、趣味化、娱乐化的那种『学习』。", "evidence": ["E6", "E7"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "以咖啡加奶加糖为喻：那样爱喝的人爱的是奶茶而非咖啡；人真正应该爱上的恰恰是让普通人竭尽全力、痛不欲生的艰难之事本身，爱喝咖啡就该爱咖啡的苦。", "evidence": ["E8", "E9"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不折磨，哪有坚韧；没有坚韧，幸福就全靠躲；坚韧的人靠的是对惊涛骇浪视如等闲。", "evidence": ["E10"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "子女不需要学会任何知识，『学知识』只该是为了学会反复挑战智力极限的快乐，『学没学会那个知识』根本不那么重要。", "evidence": ["E11", "E12"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "学习成瘾、工作成瘾，功名利禄就于你如浮云；挑工作不再看待遇报酬，而是看它有没有挑战性。", "evidence": ["E13", "E14"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "配得上你来做、能引起你兴趣的工作没有不赚钱的；世界上最赚钱的东西就是别人连试都没勇气试的东西。", "evidence": ["E15"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "把做事过程录下来丢哪里流量都有百万，切成十二段流量就是1200万。", "evidence": ["E16"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要让子女爱上这种精神冲浪的感觉，需要你自己是这样的人——要有超越一般价值而热爱的东西，有无需物质报酬就已足堪享受的神性享乐。", "evidence": ["E17", "E18"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种心态的养成，除天意际遇之外，人可以做的一件事是带领自己的孩子练功夫（不是指练武术）。", "evidence": ["E19", "E20"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "先沉浸在功夫的世界里，有了功夫自然锥置囊中、颖脱而出，直到任何事情只要动念必易成功；此『成功』指成就功夫而非取得功勋。", "evidence": ["E21", "E22"]},
    {"claim_id": "C014", "claim_type": "quoted_or_cited", "attribution": "questioner", "modality": "asserted", "statement": "提问者引述的微信朋友圈论调主张：宁愿欠孩子一个快乐的少年，也不愿看到其卑微的成年（即把少年快乐与成年境遇视为交换）。论调原文见提问字段 Q001，不属正文段落，故本条仅以作者提及该交换的正文作语境证据。", "evidence": ["E23"]}
   ],
   "argument_steps": [
    "反驳框架：要害不在交换值不值得，而在于本不该是交换关系（P001）。",
    "正面主张：学习本身应是人生至乐、工作本身应是快乐源泉（P002-P003）。",
    "事实反驳：即使熬到才高八斗，交换也换不到逸乐人生（P004-P005）。",
    "追加要害：澄清『学会喜欢学习』不是给苦药加糖、不是奖励交换、不是娱乐化（P006-P009）。",
    "类比：咖啡加奶加糖变成奶茶，爱的是奶茶不是咖啡（P010）。",
    "定义：人应爱上艰难之事本身，爱咖啡就该爱咖啡的苦（P011-P013）。",
    "理由：不折磨哪有坚韧，没有坚韧幸福全靠躲（P014-P016）。",
    "重定目标：学知识只为学会挑战智力极限的快乐（P017-P019）。",
    "推论：成瘾者挑工作看挑战性，且不缺钱、不缺流量（P020-P022）。",
    "收束反问：不必用不快乐的童年换快乐的成年（P023-P025）。",
    "举例：养猪、断腿、高位截瘫等假设处境说明无趣的是人（P026-P029）。",
    "前提条件：要让子女如此，你自己必须是那样的人（P030-P039）。",
    "例证：芭蕾票之贵（P040）。",
    "行动指引：以练功夫（剥毛豆等）养育该心态（P041-P068）。",
    "结论：成就功夫即成功，出手成功的人无庸碌之辈，并以『去剥剥毛豆看看』号召（P069-P074）。"
   ],
   "concept_usage": [
    {"term": "交换关系", "meaning": "把学习当作换取未来逸乐的对价交易；作者否认这一框架，主张本来就不该是交换。", "evidence": "P001", "ambiguity": "作者未给出替代框架的正面定义，只说『本来就谈不上』。"},
    {"term": "功夫", "meaning": "本文指把一件事练到透、持续改进的技艺修炼（明确不是武术），如剥毛豆、写『永』字；作者视其为养成心态的可操作路径。", "evidence": "P043", "ambiguity": "作者特意声明『这不是指练武术』（P043）；与武术义的边界由作者自己划定。"},
    {"term": "神性享乐", "meaning": "无需再获得任何物质报酬就已经足堪享受的享乐。", "evidence": "P033", "ambiguity": "描述性用语，未给判据；与宗教义无关的用法未被作者说明。"},
    {"term": "精神冲浪", "meaning": "作者对爱上艰难之事时那种体验的比喻，是需要养成的『感觉』。", "evidence": "P030", "ambiguity": "比喻性表述，未界定具体所指。"},
    {"term": "学知识", "meaning": "作者把它与『反复挑战智力极限的快乐』区分开，认为后者才是目的；『学没学会那个知识』不重要。", "evidence": "P017", "ambiguity": "『你的子女不需要学会任何知识』（P017）为夸张或字面表述，正文未加限定。"},
    {"term": "成功", "meaning": "本文特指成就功夫，而非『取得功勋』。", "evidence": "P072", "ambiguity": "与日常用法不同，作者已作明确限定。"}
   ],
   "examples_and_targets": [
    "提问者引述的微信朋友圈论调「孩子，我宁愿欠你一个快乐的少年，也不愿看到你卑微的成年」—— 提问者的引述，本篇评论与反驳的对象（Q001，非正文段落）。",
    "『七点前默写完爸爸周末就带你去海洋公园』、多媒体化、互动化、趣味化、娱乐化 —— 作者否定/反驳的做法（P008-P009）。",
    "咖啡加奶加糖变成咖啡风味奶茶 —— 作者的类比（P010）。",
    "养猪、断腿（3D打印假肢）、高位截瘫（眼皮发摩斯电码、舌控指点杆、用舌头耍杂技）—— 作者的假设性例证与修辞材料，并附禁止剽窃创意的插话（P026-P028）。",
    "芭蕾票值得那么贵 —— 作者的例证（P040）。",
    "徒手剥毛豆（十斤毛豆分二十堆）—— 作者给家长与孩子的练习例证（P045-P059）。",
    "学毛笔字练『永』字、削铅笔、练线条、练抓黄豆、练解二元一次方程 —— 作者列举的练习例证（P062-P068）。",
    "拉面师傅 —— 作者用以说明境界可出自任何行当的例证（P039）。",
    "庖丁解牛 —— 作者引用的典故（P070）。"
   ],
   "conditions": [
    "『只要建立起这个心态，则交换与否已经没有意义』（P004，条件句）。",
    "让步：『即使你熬到真的才高八斗』（P005）。",
    "限定：『配得上你来做的工作，能引起你兴趣的工作』才没有不赚钱的（P021）。",
    "条件：『这种心态的养成，除了天意际遇之外』（P042，指出可控范围有限）。",
    "让步：『哪怕ta只是位拉面师傅』（P039）。",
    "适用对象为读者『你们』与『你的子女』，场景为家庭教育、学习与择业。",
    "养猪、断腿、高位截瘫等均为假设情形（P026-P028），非事实陈述。"
   ],
   "rhetoric_and_tone": "训诫兼煽动性的口语体；自称『老子』（『浪不大，老子还不爽』『老子还不屑于做』）；第二人称直呼『你们』，并连用九次『能不能……』排比追问；夸张（流量1200万、成为世界第一个用舌头耍杂技的人）；括号内调侃（『严正声明，此创意禁止剽窃，剽窃高位截瘫患者的创意你们还有人性吗？』）；插入英文短句『The bitterness is the point.』；引用典籍典故『庖丁解牛』；结尾以命令式行动号召『去剥剥毛豆看看』收束。",
   "unresolved_questions": [
    "提问引述的『微信朋友圈论调』出处与原作者未给出，本篇未核证；该论调属提问者引述，不得归给作者。",
    "P021『世界上最赚钱的东西就是别人连试都没勇气试的东西』与 P022『流量都有百万』『流量就是1200万』为无来源的数据性断言，待外部核查。",
    "『你的子女不需要学会任何知识』（P017）与『学没学会那个知识，根本不那么重要』（P018）之间是夸张还是字面主张，正文未加限定，存在解释歧义。",
    "P028 括号内『严正声明』是否为戏谑语气，正文未标记；该段整体为假设情形。",
    "若家长自身未达到作者所述的境界，除『天意际遇』外是否仍有可行路径，正文未说明。",
    "brief 为概括性导语且被截断，与正文表述不完全一致；以正文为准，provenance/superseded 均为 null。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "而在于这本来就不该是交换关系。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "学习本身就应该是人生至乐。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "工作本身就应该是人生的快乐源泉。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "本来就谈不上“用痛苦的学习去换取逸乐的人生”", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "你也只会找到一个专属于才高八斗者的同样压力巨大而迷茫不知归处的苦工", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "不要以为“学会喜欢学习”是指要把学习这味苦药想办法撒上糖", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "不是“七点前默写完爸爸周末就带你去海洋公园”", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P010", "quote": "爱喝的人爱的是奶茶，而不是咖啡。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P012", "quote": "爱喝咖啡，爱上的就该是咖啡的苦。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P016", "quote": "不折磨，哪有坚韧？没有坚韧，幸福就全靠躲。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P017", "quote": "ta们“学知识”只该是为了学会反复挑战智力极限的快乐", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P018", "quote": "“学没学会那个知识”，根本不那么重要。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P019", "quote": "学习成瘾，工作成瘾，功名利禄就于你如浮云。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P020", "quote": "而是看它“有没有挑战性”", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P021", "quote": "世界上最赚钱的东西就是别人连试都没勇气试的东西。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P022", "quote": "切成十二段，流量就是1200万。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P031", "quote": "那需要你自己是这样的人。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P032", "quote": "你要有超越一般价值而热爱的东西。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P042", "quote": "人可以做的一件事是带领自己的孩子练功夫", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P043", "quote": "这不是指练武术。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P069", "quote": "有了功夫，自然锥置囊中、颖脱而出。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P072", "quote": "而是指成就功夫", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P001", "quote": "这个交换值不值得、该不该做", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["教育", "学习心理", "人生哲学", "家庭教育"],
   "issue_candidates": ["快乐少年与卑微成年的交换论", "学习动机与兴趣", "难度与坚韧", "亲子教育方式", "专精（功夫）与成功"],
   "text_function_candidates": ["答疑（反驳式作答）", "训诫/劝勉", "经验总结", "行动指引"],
   "object_candidates": ["微信朋友圈论调（提问者引述）", "家长与子女", "才高八斗者", "拉面师傅", "高位截瘫者（假设例证）"],
   "working_keywords": ["交换关系", "人生至乐", "苦药撒糖", "咖啡与奶茶", "精神冲浪", "神性享乐", "功夫", "庖丁解牛", "剥毛豆", "The bitterness is the point."]
  },
  "notes": "正文 74 段（lexical paragraph 节点 76，含 2 个空段），text 与 lexical 无分歧（divergence=0），无图片节点，故 image_checked=false 不影响 status=read。brief 为概括性导语且被截断，仅作导航，未用于支持主张。发布日期 2020-12-11，更新时间 2025-06-19。"
 },
 "cdf1315e": {
  "analysis": {
   "question_context": "提问者以假设发问：『如果没有伦理道德，医学将会发展到什么样？』（Q001，属提问者的假设性提问，不得当作作者立场）。作者正文只有一句未完成的话『如果没有伦理道德，厂』，句子在『厂』字处中断，没有任何后续展开，无法据以重建作者对该问题的回答。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "正文仅一截断句『如果没有伦理道德，厂』，以『厂』字中断，无完整命题、无理由、无结论。", "role": "other"}
   ],
   "main_claims": [],
   "argument_steps": [
    "本文无论证推进：正文仅 10 字且在『厂』处中断，没有完整句子、理由或结论（P001）。"
   ],
   "concept_usage": [
    {"term": "伦理道德", "meaning": "仅出现在未完成句『如果没有伦理道德，厂』中；作者未在正文说明其含义或它与医学的关系。", "evidence": "P001", "ambiguity": "句子中断，概念用法无法确定。"}
   ],
   "examples_and_targets": [
    "本文未给出任何例子、人物、机构、事件、历史叙述或数据；『厂』字之后的内容缺失（P001）。"
   ],
   "conditions": [
    "本文未说明任何条件；句首『如果没有伦理道德』看似假设条件，但句子未完成，条件内容与结论均不可知（P001）。"
   ],
   "rhetoric_and_tone": "正文为一截断片段，语气与修辞无从判断；『如果没有伦理道德，厂』以逗号后的单字结束，无收束标点。",
   "unresolved_questions": [
    "正文仅 10 字且明显在『厂』字处截断（brief 亦为同一截断文本『如果没有伦理道德，厂』），疑为未完成稿或抓取/发布截断，无法据以理解作者观点。",
    "截断处缺失的内容（『厂』之后）无从获得，不得依标题或提问补写。",
    "本篇无图片节点（lexical 仅 1 个 paragraph 节点），断开处并非图文缺失所致，需人工核对平台原帖或编辑历史。",
    "因正文不完整，本篇不建立任何作者主张，也不能确定作者是否支持提问中的假设。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "如果没有伦理道德，厂", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["unknown"],
   "issue_candidates": ["unknown"],
   "text_function_candidates": ["unknown"],
   "object_candidates": ["unknown"],
   "working_keywords": ["伦理道德", "医学"]
  },
  "notes": "status=needs_reread：正文仅 10 字且在『厂』字处中断（brief 亦为同一截断文本），内容不足以建立阅读记录，需人工核对原帖或重新抓取后补读；已读部分仅为该截断片段。因正文不完整，full_text_checked=false，image_checked=false（本篇无图片节点）。提问中的『伦理道德』『医学』仅属提问者语境，未据此给文章贴领域标签。",
  "status": "needs_reread",
  "full_text_checked": False,
  "image_checked": False
 },
 "13eda242": {
  "analysis": {
   "question_context": "提问者就『泡泡玛特市值破 1000 亿』问如何看待盲盒经济、为何盲盒能疯狂吸粉年轻人（Q001，属提问者）。作者未正面分析盲盒经济的机制或吸粉原因，而以宋代赌博（赌菜、赌茶、赌果子、以赌代购）作历史类比，说明『赌如果不禁可以到什么地步』，把赌博定性为毁灭人生最快的方法，并在末句把『迷恋盲盒』判定为危险信号。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "以设问提出主题：赌如果不禁可以到什么地步？", "role": "context"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003", "P004"], "summary": "历史例证：宋朝有赌菜、赌茶、赌果子；买两斤猪肉可把铜钱放下与摊主赌一把，赌赢直接拿走猪肉，赌不赢铜钱白给；作者反问『浪漫不？』", "role": "example"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006"], "summary": "判断与警示：赌是毁灭人生最快的办法，应远离赌性太重的人；这类人给人勇气十足的浪漫感，其实只是不知死活造成的过度自信；迷恋盲盒可以算是一个危险信号。", "role": "claim"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "赌是毁灭人生最快的办法，应远离赌性太重的人。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "赌性太重的人常给人一种勇气十足的浪漫感，但其实只是不知死活造成的过度自信罢了。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "asserted", "statement": "迷恋盲盒可以算是一个危险信号。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_reported", "attribution": "author", "modality": "asserted", "statement": "宋朝的时候有所谓赌菜、赌茶、赌果子的（即以赌博方式进行日常买卖）。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者以反问『浪漫不？』评述宋代以赌代购的买卖方式，未直接给出褒贬判断。", "evidence": ["E5"]}
   ],
   "argument_steps": [
    "设问开局：赌如果不禁可以到什么地步（P001）。",
    "历史例证：宋代有赌菜、赌茶、赌果子（P002）。",
    "具体化：买猪肉时与摊主赌一把，输赢决定货物与铜钱归属（P003）。",
    "反问带出反讽观感：浪漫不？（P004）。",
    "下判断：赌是毁灭人生最快的办法，远离赌性太重的人；其浪漫感实为不知死活造成的过度自信（P005）。",
    "落到当下：迷恋盲盒可以算是一个危险信号（P006）。"
   ],
   "concept_usage": [
    {"term": "赌", "meaning": "作者把它视为可延伸进日常买卖的行为方式，并定性为毁灭人生最快的方法；由宋代赌菜赌茶赌果子到当代盲盒构成类比链。", "evidence": "P005", "ambiguity": "作者未定义赌博的边界，也未说明盲盒与赌博在机制上的相似点。"},
    {"term": "浪漫", "meaning": "本文指赌博式行为给人的『勇气十足』的外表观感（『浪漫不？』『勇气十足的浪漫感』），带反讽意味。", "evidence": "P004", "ambiguity": "与情感义不同，是否确为反讽正文未标记。"},
    {"term": "迷恋盲盒", "meaning": "作者把对盲盒的迷恋视为赌博类行为的当代形态，判为危险信号。", "evidence": "P006", "ambiguity": "未区分一般购买与『迷恋』的界线，危险的具体所指未展开。"}
   ],
   "examples_and_targets": [
    "宋代赌菜、赌茶、赌果子 —— 作者的历史例证（P002），未给出处，待外部核查。",
    "『你要买这两斤猪肉，把铜钱放下，跟摊主赌一把』的赌法 —— 作者的举例（P003）。",
    "泡泡玛特市值破 1000 亿、盲盒经济、年轻人 —— 提问者提供的背景（Q001）；作者未引用其中数据，只以『迷恋盲盒』为判断对象（P006）。",
    "『赌性太重的人』—— 作者建议远离的对象（P005）。"
   ],
   "conditions": [
    "『赌如果不禁可以到什么地步？』为设问式假设前提（P001）。",
    "历史类比限定于宋代的情形（P002）。",
    "作者对盲盒的判断限定于『迷恋盲盒』，而非一般购买行为（P006）。",
    "『可以算是一个危险信号』为留有余地的表述（P006）。"
   ],
   "rhetoric_and_tone": "以反问开篇并设置悬念；用宋代赌菜赌茶赌果子的历史画面作类比；以短问『浪漫不？』带出反讽；随后改用短句下判断，语气直接、警告性强（『远离赌性太重的人』）；对盲盒仅给一句结论，未展开论证或回应提问的解释性要求。",
   "unresolved_questions": [
    "宋代『赌菜、赌茶、赌果子』及以赌代购的史实未见出处，属作者转述，待外部核查。",
    "作者未说明盲盒与赌博在机制上的具体相似点，也未回答提问中『为何盲盒能疯狂吸粉年轻人』的解释性部分。",
    "『迷恋』与一般盲盒消费的界线未界定；『危险信号』具体指成瘾、财务风险还是其他，正文未展开。",
    "『浪漫不？』是否确为反讽，正文未标记。",
    "brief 为正文前缀的截断文本，与正文一致；provenance/superseded 均为 null，无版本差异。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P005", "quote": "赌是毁灭人生最快的办法，远离赌性太重的人。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P005", "quote": "但其实只是不知死活造成的过度自信罢了。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P006", "quote": "迷恋盲盒可以算是一个危险信号。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P002", "quote": "宋朝的时候，有所谓赌菜、赌茶、赌果子的。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "浪漫不？", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["赌博与成瘾行为", "消费文化", "经济现象评论"],
   "issue_candidates": ["盲盒经济与赌博的类比", "赌博的社会史", "成瘾性消费的风险", "泡泡玛特市值（提问背景）"],
   "text_function_candidates": ["答疑（简要评论式）", "警示/评论"],
   "object_candidates": ["宋代赌博者与摊主", "盲盒消费者", "赌性太重的人", "泡泡玛特（提问背景）"],
   "working_keywords": ["赌菜、赌茶、赌果子", "铜钱", "盲盒", "危险信号", "赌性", "浪漫"]
  },
  "notes": "知乎问答回答；question 属提问者，作者未按其解释性要求作答，而以历史类比与警示回应。正文 6 段，text 与 lexical 无分歧（divergence=0），无图片节点，故 image_checked=false 不影响 status=read。brief 为正文前缀的截断文本，仅作导航。发表 2020-12-12，更新 2021-05-16。"
 },
 "df000979": {
  "analysis": {
   "question_context": "提问者问『作为个人有没有种族歧视的自由？』（Q001，属提问者语境，非作者立场）。作者未直接回答『有没有』，而是先立两个事实（偏见无法根除；区别对待是天然的基本自由），再以『平等=一次公平的机会』澄清歧视与平等各指什么，最后给出结论：实践上当然可以歧视、没有人能有效阻止你、甚至没有人真的有权阻止你，只是不要以为没有代价，而那样的代价你付不起。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "前提一：不管自认多公平，人仍在基于某种程度的偏见决策；人类顶多压缩、克制，本质上无能为力；因此不允许、不承认偏见的生存空间办不到；以禁止任何偏见为诉求的公共政策要么公信力破产，要么自欺欺人。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005"], "summary": "前提二：人和人当然不同；原则上不可能对任何两个确切具体的人给予完全相同的待遇；按自己心意区别对待不同的人本来就是人天然的基本自由，否则连『该和谁谈恋爱』『该录用谁』都会变得无解。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007", "P008"], "summary": "转折设问：既然区别对待是天经地义的个人权利，还有什么『歧视』可言？到底歧视是什么？在区别对待是显著自由的前提下，平等又指什么？", "role": "transition"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P010", "P011", "P012", "P013"], "summary": "以 heading 句定义平等：平等的本质是一次公平的机会，即让别人真正凭自己的作为来形成与人的关系的机会；对方有所作为后据其行为决定关系是自由，但在其有所作为之前应被给予一次公平、干净的机会，这就是实践平等。", "role": "definition"},
    {"unit_id": "U005", "paragraph_refs": ["P014", "P015", "P016"], "summary": "把该原则推展到对方与他人的关系：人应自我克制，不在共立法律之外（譬如裁判文书网、性犯罪者公示制度）额外破坏 ta 与一切别人形成其他关系的公平机会；这就不但在实践平等，而且在追求和维护平等。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P017", "P018"], "summary": "界定平等不是什么：平等不是要你『无差别对待所有人』，而是不因籍贯、肤色、信仰、性别、种族甚至年龄等群体标签，在人凭作为形成自己形象之前天然地先被判断；即使形成了判断，也不要宣传、鼓动、扩散。", "role": "definition"},
    {"unit_id": "U007", "paragraph_refs": ["P019", "P020", "P021", "P022", "P023", "P024"], "summary": "现代社会推行平等理念的理由：为和平、理解和爱争取最大机会；帮助一切人不断再尝试建立新的友好关系；消除『一失足成千古恨』的根本恐惧；让人不轻易丧失对努力的信心；抑制人与人之间本已存在的猜忌和敌视。", "role": "reason"},
    {"unit_id": "U008", "paragraph_refs": ["P025", "P026", "P027", "P028", "P029", "P030"], "summary": "论证平等对群体的收益：现代竞争全维度全范围，不努力甚至背道而驰的群体不会因『善于怀疑』而长期幸存，最后的赢家一定是善于相信的那群人——这样的人没有天然敌人，别人会先尝试建立友好关系；且重视平等者会习得给人第二次机会的习惯，使有不良过去者仍可凭作为重建关系，因为因着过去断言现在就是没给现在的你公平的机会。", "role": "reason"},
    {"unit_id": "U009", "paragraph_refs": ["P031", "P032"], "summary": "设问并给出平等/反歧视艰难的两个原因：区别对待的天然权利与歧视的概念混淆让很多人误以为反歧视是假议题；人没有想清楚自己一生到底应该追求什么。", "role": "reason"},
    {"unit_id": "U010", "paragraph_refs": ["P033", "P034", "P035", "P036", "P037", "P038"], "summary": "心理机制：未想清楚前默认追求享乐最大化，因而以享乐不能最大化为恐惧；恐惧催生疯狂防御心态、对损失及其任何可能性高度过敏，甚至催化出捕风捉影的非理性防御；ta们不能忍受给人公平机会的风险（并引述其盘算：某群体以小偷多著称，给其子女公平机会岂不是敞开大门），于是选择『提前防御』。", "role": "reason"},
    {"unit_id": "U011", "paragraph_refs": ["P039", "P040", "P041", "P042", "P043", "P044"], "summary": "代价之一：提前防御从根本上阉割了成为任何意义上真正的领袖的资格；养成此习气者最好不要面对领袖职责或追求，因为于人于己都是折磨和灾难；哪怕独生皇储有顾命大臣拱卫，内心也无平安，因为任何人身上都有『值得歧视』的理由而恐惧开关关不掉，决策多为恐惧猜疑驱动。", "role": "claim"},
    {"unit_id": "U012", "paragraph_refs": ["P045", "P046", "P047", "P048"], "summary": "代价之二：提前防御不能带来真正安全，反而在战略层面削弱总体安全——战术安全来自防御，战略安全来自有选择；抛弃半个乃至大半个世界就失去选择，不得不选择的人获得更大筹码，你只能缩手缩脚、委屈求全；犹如怕被偷而住进牢房，是显然的愚蠢。", "role": "claim"},
    {"unit_id": "U013", "paragraph_refs": ["P049", "P050", "P051", "P052", "P053"], "summary": "代价之三：歧视者名声在外，所有人对接近与合作的犹豫三分；歧视是习惯、是瞎眼的传染病，会蔓延到整个交往圈；已知被歧视者是敌人，未知者亦不自安，于是『起步三分敌』；并反问读者是否担得起所有人都对你起步三分敌。", "role": "claim"},
    {"unit_id": "U014", "paragraph_refs": ["P054", "P055", "P056"], "summary": "结论：实践上当然可以歧视——没有人能有效阻止，甚至没有人真的有权阻止——只是不要以为没有代价；其实你付不起那样的代价，因为那几乎必然让你成为典型的『人下之人』、从而最容易被人歧视，而且这回真的是因为你的作为。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不管人自认多么公平，实际上仍在基于某种程度的偏见做决策；在偏见问题上人类顶多压缩、克制，本质上是无能为力的。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "强行实施以禁止任何偏见为诉求的公共政策，结果要么是公信力直接破产，要么是自欺欺人。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "原则上不可能对任何两个确切具体的人给予完全相同的待遇；按照自己的心意区别对待任何不同的人本来就是人天然的基本自由。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "平等的本质是一次公平的机会，即让别人真正凭自己的作为来形成与人的关系的机会。", "evidence": ["E4", "E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在对方有所作为之前，ta 应该被给予一次公平的、干净的机会；其有所作为之后据其行为决定关系则属自己的自由，这就是实践平等。", "evidence": ["E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人应自我克制，不在共立法律之外额外破坏对方与一切别人形成其他关系的公平机会；这就不但在实践平等，而且是在追求平等和维护平等。", "evidence": ["E7"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "平等不是要人无差别对待所有人，而是不因籍贯、肤色、信仰、性别、种族甚至年龄等群体标签，在人有机会凭作为形成自己的形象之前被天然地先判断。", "evidence": ["E8", "E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "即使形成了自己的判断，也不要去宣传、去鼓动、去扩散自己的判断。", "evidence": ["E10"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "现代社会推行平等理念，是为了给和平、理解和爱争取最大的机会，帮助一切人不断再尝试建立新的友好关系，消除『一失足成千古恨』的根本恐惧，让人不轻易丧失对努力的信心，抑制人与人之间本已存在的猜忌和敌视。", "evidence": ["E11", "E12"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "现代社会竞争是全维度、全范围的，在这方面不加努力甚至背道而驰的群体不会因『善于怀疑』而长期幸存；最后的赢家一定是善于相信的那一群人。", "evidence": ["E13"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "重视平等原则的人长期习惯成自然，会渐渐习得给人第二次机会的习惯，使有不良过去者仍可凭作为获得形成新关系的机会。", "evidence": ["E14"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "因着你的过去而断言你的现在，是没有给现在的你公平的机会。", "evidence": ["E15"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "平等/反歧视推行艰难，一方面因区别对待的天然权利与歧视的概念混淆让很多人误以为反歧视是假议题，另一方面因人没有想清楚自己一生到底应该追求什么。", "evidence": ["E16"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在没想清楚之前，人们默认追求享乐的最大化，因而以享乐的不能最大化为恐惧；这份恐惧催生疯狂的防御心态，对一切损失及其任何可能性高度过敏，并在脆弱不安的人身上催化出捕风捉影式的非理性防御心。", "evidence": ["E17"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "提前防御从根本上阉割了自己成为任何意义上的真正的领袖的资格；养成这种习气的人最好求老天保佑不要面对领袖的职责或追求，因为那于人于己都是折磨和灾难。", "evidence": ["E18"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "提前防御不能获得真正的安全，反而在战略层面削弱自己的总体安全：战术上安全来自防御，战略上安全来自有选择。", "evidence": ["E19"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "歧视是一种习惯、一种瞎眼的传染病，绝不会甘于固守固定的目标，而一定会蔓延到整个交往圈。", "evidence": ["E20"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "实践上当然可以歧视——没有人能有效阻止你，甚至没有人真的有权阻止你——只是不要以为没有代价；其实你付不起那样的代价，因为那几乎必然让你成为典型的『人下之人』、最容易被人歧视，而且这回真的是因为你的作为。", "evidence": ["E21", "E22"]},
    {"claim_id": "C019", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "作者引述的『提前防御』者盘算：某群体以小偷多著称，给其一个子女公平的机会，岂不是敞开大门给ta偷我的机会。此观点由作者转述并随后批评，不属作者主张。", "evidence": ["E23"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "作者反问：你担得起所有人都对你起步三分敌吗？", "evidence": ["E24"]}
   ],
   "argument_steps": [
    "先立事实一：偏见不可根除，人类只能压缩克制（P001-P002）。",
    "推论：以禁止任何偏见为诉求的公共政策要么公信力破产，要么自欺欺人（P003）。",
    "再立事实二：人和人不同，区别对待是天然的基本自由（P004-P005）。",
    "设问澄清：既然区别对待是权利，歧视是什么？平等指什么？（P006-P008）",
    "定义（heading）：平等的本质是一次公平的机会（P009-P013）。",
    "推展到第三人关系，并给出自我克制的行动要求（P014-P016）。",
    "反面界定：平等不是无差别对待，而是不以群体标签预先判断，且不宣传扩散判断（P017-P018）。",
    "说明现代社会推行平等的五项目的（P019-P024）。",
    "论证收益：善于相信者长期幸存，平等者习得给人第二次机会（P025-P030）。",
    "解释反歧视艰难的两个原因（P031-P032）。",
    "揭示心理机制：享乐最大化→恐惧→疯狂防御→提前防御（P033-P038）。",
    "列举代价一：丧失成为真正领袖的资格（P039-P044）。",
    "列举代价二：战略安全被削弱（P045-P048）。",
    "列举代价三：歧视蔓延、人人起步三分敌（P049-P053）。",
    "结论：实践上可以歧视，但代价你付不起，最终成为最易被歧视的『人下之人』（P054-P056）。"
   ],
   "concept_usage": [
    {"term": "偏见", "meaning": "作者认为人人都在某种程度上据以决策、无法根除而只能压缩克制的倾向。", "evidence": "P002", "ambiguity": "未界定偏见的程度与边界。"},
    {"term": "区别对待", "meaning": "按自己的心意对不同的人给予不同待遇，作者称之为人天然的基本自由。", "evidence": "P004", "ambiguity": "它与『歧视』的界线正是本文要澄清的问题（P006、P032）。"},
    {"term": "歧视", "meaning": "本文未给单句定义，而借『平等=一次公平的机会』对照界定，并把宣传、鼓动、扩散判断列为应自我克制之事。", "evidence": "P017", "ambiguity": "作者自承存在概念混淆（P032）；定义需由 P017-P018 反推。"},
    {"term": "平等", "meaning": "本文指给人一次公平的机会——让别人真正凭自己的作为形成与人的关系，不因群体标签在人有所作为之前被天然判断。", "evidence": "P009", "ambiguity": "作者明言平等不是『无差别对待所有人』（P017），与日常用法不同。"},
    {"term": "提前防御", "meaning": "作者对因恐惧风险而预先排斥他人的心态的称呼，本文重点论述其三重代价。", "evidence": "P038", "ambiguity": "无明确定义，靠 P037 的引述与 P040-P053 的代价说明。"},
    {"term": "战术/战略安全", "meaning": "作者区分：战术上安全来自防御，战略上安全来自有选择。", "evidence": "P046", "ambiguity": "未给严格定义，属作者的框架性区分。"},
    {"term": "人下之人", "meaning": "作者用语，指因歧视作为而几乎必然沦为最易被歧视的处境。", "evidence": "P055", "ambiguity": "带引号使用，未定义。"}
   ],
   "examples_and_targets": [
    "『该和谁谈恋爱』『该录用谁』『凭什么是ta而不是我？』—— 作者用来说明无差别对待不可能的例子（P005）。",
    "裁判文书网、性犯罪者公示制度 —— 作者所举制度例子（P016），用来说明『共立法律之外』的范围，句法指涉有歧义。",
    "籍贯、肤色、信仰、性别、种族甚至年龄 —— 作者列举的群体标签（P017）。",
    "『一个群体以小偷多著称……』的盘算 —— 作者引述并批评的提前防御者观点（P037）。",
    "独生皇储与顾命大臣 —— 作者的假设性例证（P042）。",
    "『你今天因为某种原因歧视黑人』—— 作者举例说明歧视会转移目标（P050）。",
    "『犹如人为了怕被偷，所以住进牢房』—— 作者的类比（P048）。",
    "种族歧视本身 —— 提问者的提问议题（Q001）；正文仅把『种族』列为群体标签之一（P017），未专门讨论种族问题。"
   ],
   "conditions": [
    "『不管你觉得自己多么公平』为让步性普遍条件（P002）。",
    "平等原则的适用时点：在 ta 有所作为之前给机会，有所作为之后据行为决定关系（P011-P012）。",
    "范围限定：『不要在共立法律之外』额外破坏公平机会（P016）。",
    "条件：只要有什么原因让 ta 们觉得此时的你可能有所不同，你便会获得重新凭作为形成新关系的机会（P029）。",
    "条件：『一个人如果养成这样提前防范的习气』（P041）。",
    "让步：『哪怕你是独生皇储，有一群顾命大臣拱卫着你』（P042）。",
    "预测限定：关于群体长期幸存的判断面向现代社会全维度、全范围的竞争（P025-P026）。"
   ],
   "rhetoric_and_tone": "论辩体，以层层设问推进（『到底歧视是什么？』『平等是指什么？』『为什么现代社会要推行平等理念？』『为什么平等/反歧视进行得如此的艰难呢？』）；用『首先』『第二』『一方面……另一方面』组织论证；把对手的内心盘算加引号复述后再反驳；使用类比（怕被偷而住进牢房）与反问（『你担得起所有人都对你起步三分敌吗？』）；以英文短句『It’s another poetic irony.』作反讽收束；P009 以 heading 形式的短句承担定义功能。",
   "unresolved_questions": [
    "P016 括号中『譬如裁判文书网、或者性犯罪者公示制度』究竟是『共立法律』的举例，还是『共立法律之外』的举例，句法上存在歧义。",
    "作者未给『歧视』独立的定义，只能由平等原则与 P018 的克制要求反推；作者自承存在概念混淆（P032）。",
    "P025-P026 关于『最后的赢家一定是善于相信的那一群人』属无来源的预测性判断，待外部核查。",
    "P037 引述的盘算是作者对『提前防御者』心理的转述与重构，非可核实的原始引语；已按 opponent_view 归属。",
    "P050 提到『歧视黑人』仅为说明歧视会蔓延的举例，正文未涉及具体国家、事件或数据。",
    "本篇正文泛论偏见、歧视与平等，未专门回答提问中的『种族歧视』，提问立场不得归给作者。",
    "brief 为正文前缀的截断文本，与正文一致；provenance/superseded 均为 null，无版本差异。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "在偏见问题上，人类顶多压缩一点、克制一点，但是本质上是无能为力的。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "结果要么是公信力直接破产，要么是自欺欺人。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "按照自己的心意区别对待任何不同的人本来就是人天然的基本自由。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P009", "quote": "平等的本质，是一次公平的机会。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P010", "quote": "一次让别人真正凭自己的作为来形成与人的关系的机会。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P012", "quote": "但在ta有所作为之前，ta应该被给予一次公平的、干净的机会。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P016", "quote": "额外破坏ta与一切别人形成其他关系的公平机会", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P017", "quote": "平等，不是要你“无差别对待所有人”", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P017", "quote": "譬如籍贯、肤色、信仰、性别、种族甚至年龄", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P018", "quote": "也不要去宣传、去鼓动、去扩散自己的判断。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P022", "quote": "为了消除人们“一失足成千古恨”的根本恐惧。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P024", "quote": "为了抑制人与人之间本来就已经存在的猜忌和敌视。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P026", "quote": "最后的赢家一定是善于相信的那一群人。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P028", "quote": "ta们会渐渐习得给人第二次机会的习惯。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P030", "quote": "是没有给现在的你公平的机会。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P032", "quote": "让很多人误以为反歧视是假议题", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P035", "quote": "这份恐惧会催生出疯狂的防御心态", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P040", "quote": "首先，这从根本上阉割了自己成为任何意义上的真正的领袖的资格。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P046", "quote": "战术上安全是来自防御，战略上安全是来自有选择。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P050", "quote": "歧视是一种习惯、一种瞎眼的传染病", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P054", "quote": "只是不要以为没有代价。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P055", "quote": "因为那几乎必然会让你成为典型的“人下之人”", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P037", "quote": "岂不是敞开了大门给ta偷我的机会吗？", "relation": "contradicts"},
    {"key": "E24", "paragraph_id": "P053", "quote": "你担得起所有人都对你起步三分敌吗？", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["社会伦理/政治哲学", "平等与反歧视", "社会心理"],
   "issue_candidates": ["个人是否有歧视的自由", "偏见能否被公共政策禁止", "区别对待与歧视的界线", "平等与公平机会", "歧视的代价与战略安全"],
   "text_function_candidates": ["答疑（论辩式作答）", "论辩", "概念澄清"],
   "object_candidates": ["读者『你』（个人）", "歧视者", "被歧视群体", "独生皇储与顾命大臣（假设例证）", "黑人（举例）"],
   "working_keywords": ["偏见", "区别对待", "歧视", "平等", "公平的机会", "群体标签", "提前防御", "起步三分敌", "人下之人", "poetic irony"]
  },
  "notes": "正文 56 段，其中 P009『平等的本质，是一次公平的机会。』被 lexical 解析为 heading 字段，其余为 body；text 与 lexical 无分歧（divergence=0），无图片节点，故 image_checked=false 不影响 status=read。brief 为正文前缀的截断文本，仅作导航。发表 2020-12-13，更新 2021-05-16。"
 },
 "fad3df78": {
  "analysis": {
   "question_context": "提问者问『安全带这么重要，为什么不设计成不系车就无法启动？』（Q001，属提问者）。作者以成本—必要性分析作答：该功能在逻辑上属核心机制、须满足高可靠性要求，成本论亿，并连带升级换代、召回、营销与立法游说成本，而市场收益不足，因此这件事『没有发生』。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "作者主张：设计『不激活安全带就不能启动』功能成本相当高——这类『不激活就完全不能运转』的机制再细小也已在逻辑上属核心机制，必受核心机制的高可靠性要求，意味着大量匪夷所思的极端测试，成本不是几百万而是论亿。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003"], "summary": "举例说明测试与设计负担：是否要测试撞击致安全带传感器受损、引发车辆突然失去动力的可能？是否要设计反欺骗机制（假插片欺骗卡扣）？", "role": "example"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005", "P006"], "summary": "成本链条：设计成本过亿则升级换代成本水涨船高、长期必有召回成本；还需营销成本（传递必要性、建立对可靠性的信仰，友商势必以『开着开着突然失去动力』打击销售）；成本很大，推动此事的必要性必须对称提高。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P007", "P008", "P009"], "summary": "市场必要性评估：该功能能否带来足够卖点提高销量、抹平研发成本并盈利；消费者难以为操作麻烦而解决问题无感的设备多付1000多块；若整车只涨200元，1亿研发要卖50万辆才打平，而2019年卡罗拉年销不到35万辆、唯一超50万辆的是大众朗逸。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P010"], "summary": "第二种必要性是政府立法强制：理想操作是研发同时游说立法，研发完成立法也完成即可获利；但一城一地的规定影响微乎其微，影响国家层面立法基本不可设想。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P011"], "summary": "结论性通则：阻力太大而动力不足，是一切事情没有发生的恒常原因，可循此路线分析『为什么没有』这类问题。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "设计『不激活安全带就不能启动』功能的成本相当高。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这类『不激活就完全不能运转』的机制再细小也已在逻辑上属于核心机制，必受核心机制所必然受到的高可靠性要求，意味着大量极端测试，成本不是几百万而是论亿。", "evidence": ["E2", "E3"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "设计成本过亿，则升级换代成本也水涨船高，随之而来长期也必有召回成本。", "evidence": ["E4"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "还必须承担营销成本：要向用户传递该设计的必要性和关键性、建立对可靠性的信仰，而友商势必会以『开着开着突然失去动力』一类话术打击销售。", "evidence": ["E5", "E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "成本很大，于是推动这件事的必要性也就必须对称地提高。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种必要性首先来自市场：要看该功能是否足以带来卖点提高销量，以至于抹平研发成本并进一步盈利。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "很难想象消费者会为一款在操作上给自己带来麻烦、而解决的问题却并不非常有感的设备付出1000多块。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_reported", "attribution": "author", "modality": "asserted", "statement": "若整车价格只上涨200元，则1亿人民币的研发成本要卖50万辆车才能打平；而2019年即使丰田卡罗拉这样的车型一年销量也不到35万辆，销售超过50万辆的唯一车型是大众朗逸。", "evidence": ["E10", "E11"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "第二种必要性是政府立法使其成为强制要求；理想操作是研发的同时游说立法，但一城一地的管理规定影响微乎其微，想要影响国家层面的立法基本不可设想。", "evidence": ["E12"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "阻力太大而动力不足，是一切事情没有发生的恒常原因；可以循这个路线去分析『为什么没有』这类问题。", "evidence": ["E13"]}
   ],
   "argument_steps": [
    "提出主张：该功能设计成本相当高（P001）。",
    "给理由：此类机制属核心机制，须满足高可靠性要求与极端测试，成本论亿（P002）。",
    "举例：撞击致传感器受损导致突然失去动力的测试、反欺骗机制与假插片（P003）。",
    "成本链条：换代成本、召回成本（P004）、营销与友商攻击（P005）。",
    "引出判据：成本越大，必要性必须对称提高（P006）。",
    "第一条必要性（市场）：卖点能否抹平研发成本并盈利（P007）。",
    "市场测算：消费者不愿为麻烦且无感的设备多付1000多块；涨价200元需卖50万辆，而现实销量远低于此（P008）。",
    "小结：弄不好得不偿失（P009）。",
    "第二条必要性（立法）：游说国家层面立法基本不可设想（P010）。",
    "通则化结论：阻力太大而动力不足，是一切事情没有发生的恒常原因（P011）。"
   ],
   "concept_usage": [
    {"term": "核心机制", "meaning": "作者指『不激活就完全不能运转』的机制，无论多细小在逻辑上都属核心机制，因而必须满足高可靠性要求。", "evidence": "P002", "ambiguity": "未给核心机制的形式定义或判定标准。"},
    {"term": "必要性（对称提高）", "meaning": "推动某项设计的理由强度；作者认为它必须与投入成本对称地提高。", "evidence": "P006", "ambiguity": "未给衡量必要性大小的标准。"},
    {"term": "成本", "meaning": "本文包括设计/测试成本、升级换代成本、召回成本与营销成本；作者以此解释该设计『为什么没有』。", "evidence": "P004", "ambiguity": "只有设计成本给出『论亿』的量级，其余成本未量化。"},
    {"term": "反欺骗机制", "meaning": "防止用户用假插片欺骗安全带卡扣的设计。", "evidence": "P003", "ambiguity": "未展开具体技术方案。"}
   ],
   "examples_and_targets": [
    "『车辆被撞击导致安全带传感器受损引发车辆突然失去动力』—— 作者设想的极端测试情形（P003）。",
    "『多少人买了假插片欺骗善良的保险带卡扣』—— 作者举的现实欺骗行为（P003），未给数据来源。",
    "友商可能说的『你不怕开着开着突然失去动力吗』—— 作者设想的竞争性攻击话术（P005）。",
    "1000多块、整车涨价200、1亿研发成本要卖50万辆 —— 作者的估算（P008）。",
    "2019年丰田卡罗拉年销量不到35万辆、大众朗逸是唯一超50万辆的车型 —— 作者转述的行业数据（P008），未给来源。",
    "一城一地的管理规定与国家层面的立法 —— 作者对立法路径的举例（P010）。"
   ],
   "conditions": [
    "条件：『如果只会导致整车价格上涨200』，则1亿研发成本要卖50万辆车才能打平（P008）。",
    "让步式限定：这类机制『再细小』也已在逻辑上属于核心机制（P002）。",
    "场景限定：立法路径中一城一地规定影响微乎其微，国家层面立法基本不可设想（P010）。",
    "不确定评估：『弄不好还得不偿失』（P009）。",
    "数据时点限定为2019年的车型销量（P008）。"
   ],
   "rhetoric_and_tone": "商业分析口吻，用假想车企的第一人称展开（『打击我的销售』『自然赚个满盆满钵』）；以设问推进（『要不要测试……？』『但这谈何容易？』）；用具体数字增强说服力（1亿、50万辆、35万辆、1000多块、200）；结尾提炼为一般性通则，语气断言、带经验总结意味。",
   "unresolved_questions": [
    "P008 的2019年车型销量数据（卡罗拉不到35万辆、朗逸唯一超50万辆）、1000多块与200元的定价假设均无来源，待外部核查。",
    "『1亿人民币的研发成本』与『论亿』为作者估算，未给出测算依据。",
    "作者以假想车企第一人称（『我的车』『我的销售』）展开分析，是否代表作者本人立场或仅为分析视角，正文未说明。",
    "提问问的是该设计『为什么没有』，作者只作成本—必要性解释，未讨论法规、技术或既有专利等其他可能原因。",
    "『核心机制』『必要性对称提高』未给判定标准。",
    "brief 为正文前缀的截断文本；provenance/superseded 均为 null。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "首先，设计“不激活安全带就不能启动”功能成本相当高。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "再细小也已经在逻辑上属于核心机制了", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P002", "quote": "这是一个巨大的成本——不是几百万，而是论亿。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "随之而来长期也必有召回成本。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "要建立对可靠性的信仰", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P005", "quote": "你不怕开着开着突然失去动力吗", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P006", "quote": "于是推动这件事的必要性也就必须对称的提高。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P007", "quote": "是否足以带来足够的卖点提高销量，以至于可以抹平这项研发成本而进一步造成盈利？", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P008", "quote": "而解决的问题却并不非常有感的设备付出1000多块", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P008", "quote": "1亿人民币的研发成本要卖50万辆车才能打平", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P008", "quote": "销售超过50万辆的唯一车型就是大众朗逸", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P010", "quote": "而想要影响国家层面的立法，基本不可设想。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P011", "quote": "阻力太大而动力不足，是一切事情没有发生的恒常原因", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["汽车工程与产品设计", "商业/成本分析", "公共政策与立法"],
   "issue_candidates": ["安全带联锁启动的可行性", "研发与合规成本", "市场卖点与定价", "立法游说难度", "产品安全设计"],
   "text_function_candidates": ["答疑（成本分析式）", "解释", "经验总结"],
   "object_candidates": ["汽车厂商/车企", "消费者", "友商", "政府立法机关", "丰田卡罗拉", "大众朗逸"],
   "working_keywords": ["安全带", "核心机制", "可靠性", "召回成本", "营销成本", "反欺骗机制", "50万辆", "立法", "阻力太大而动力不足"]
  },
  "notes": "知乎问答回答；question 属提问者，作者以成本—必要性框架解释『为什么没有』。正文 11 段，text 与 lexical 无分歧（divergence=0），无图片节点，故 image_checked=false 不影响 status=read。brief 为正文前缀的截断文本。发表 2020-12-13，更新 2021-06-03。"
 },
 "6503eda8": {
  "analysis": {
   "question_context": "提问者引述诗句『生命成可贵，爱情价更高，若为自由故，二者皆可抛』，问如何用马斯洛的需要层次理论分析（Q001，属提问者，诗句引文亦为提问者所引）。作者未按该理论逐层分析诗句，而是主张马斯洛需求层次理论只能在大数据这种层面成立、不能解释具体的人乃至单个人的全部行为，并以英雄主义行为（各种饿着肚子的宁死不屈）作反例。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "作者主张：马斯洛需求层次理论只能在大数据这种层面成立，不能用来解释具体的人，甚至也不能解释单个人的全部行为。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003"], "summary": "反例与推论：很多英雄主义的行为与该理论背道而驰，比如各种饿着肚子的宁死不屈；而这些极少的超常案例往往有着远超正常人群的影响力和历史意义。", "role": "rebuttal"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005"], "summary": "对仗式收束：只这一个，就名留青史；那千千万万，却了无痕迹。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "马斯洛需求层次理论只能在大数据这种层面成立，并不能用来解释具体的人，甚至也不能解释单个人的全部行为。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "很多英雄主义的行为都和这个理论背道而驰，比如各种饿着肚子的宁死不屈。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "往往这些极少的超常案例反而有着远超正常人群的影响力和历史意义。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只这一个，就名留青史；那千千万万，却了无痕迹。", "evidence": ["E4", "E5"]}
   ],
   "argument_steps": [
    "先限定理论适用范围：马斯洛需求层次理论只在『大数据这种层面』成立（P001）。",
    "推论：它不能解释具体的人，甚至不能解释单个人的全部行为（P001）。",
    "举反例：很多英雄主义行为与该理论背道而驰，如饿着肚子的宁死不屈（P002）。",
    "评价反例：极少的超常案例有着远超正常人群的影响力和历史意义（P003）。",
    "对仗收束：一个即名留青史，千千万万却了无痕迹（P004-P005）。"
   ],
   "concept_usage": [
    {"term": "马斯洛需求层次理论", "meaning": "本文指用于解释人的需求层级的理论；作者限定它只在『大数据这种层面』成立，不能解释个体。", "evidence": "P001", "ambiguity": "作者未说明『大数据这种层面』的具体所指与统计判据。"},
    {"term": "英雄主义的行为", "meaning": "作者以『饿着肚子的宁死不屈』为例，指与需求层次理论相悖的超常行为。", "evidence": "P002", "ambiguity": "未定义英雄主义，仅举一例。"},
    {"term": "影响力与历史意义", "meaning": "作者认为极少数的超常案例在这两方面远超正常人群，并以此对照『千千万万』的了无痕迹。", "evidence": "P003", "ambiguity": "两个概念均未给衡量标准。"}
   ],
   "examples_and_targets": [
    "提问引述的诗句『生命成可贵，爱情价更高，若为自由故，二者皆可抛』—— 提问者的引述材料（Q001），作者未逐句分析，也未给出自己对诗句的解读。",
    "马斯洛需求层次理论 —— 被作者限定适用范围的对象（P001）。",
    "『各种饿着肚子的宁死不屈』—— 作者用以反驳该理论的例证（P002），未举具体人物、事件或出处。",
    "『只这一个』『那千千万万』—— 作者的修辞性对照（P004-P005），具体所指未明确。"
   ],
   "conditions": [
    "适用边界：该理论只在『大数据这种层面』成立（P001）。",
    "概率限定：『往往』这些极少的超常案例反而有着远超正常人群的影响力和历史意义（P003）。",
    "作者未说明该理论适用对象的具体范围与例外判据。"
   ],
   "rhetoric_and_tone": "短评体，先限定理论的适用层面，再以反例驳论，语气直接断言；结尾用对仗式短句（『只这一个，就名留青史。那千千万万，却了无痕迹。』）作抒情式收束；全文未回应提问要求的『用该理论分析诗句』。",
   "unresolved_questions": [
    "作者未回答提问所要求的『用马斯洛理论分析该诗句』，也未给诗句解读，故不得据本篇推定作者对诗句的态度。",
    "『大数据这种层面』的具体含义与判据正文未说明。",
    "『各种饿着肚子的宁死不屈』未给具体人物、事件或出处，待外部核查；此处属作者例证，非可核实的事实断言。",
    "『只这一个』『那千千万万』的所指不明（指超常案例的当事人，还是指其他），存在解释歧义。",
    "brief 与正文前四段一致但被截断；provenance/superseded 均为 null，无版本差异。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "马斯洛需求层次理论只能在大数据这种层面成立", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "很多英雄主义的行为都和这个理论背道而驰", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "反而有着远超正常人群的影响力和历史意义", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "只这一个，就名留青史。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "那千千万万，却了无痕迹。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["心理学理论（需求层次）", "英雄主义/历史评价", "方法论（理论的适用范围）"],
   "issue_candidates": ["马斯洛需求层次理论的适用范围", "英雄主义行为与需求层次", "超常案例的历史意义"],
   "text_function_candidates": ["答疑（质疑式短评）", "评论", "驳论"],
   "object_candidates": ["马斯洛（理论）", "饿着肚子的宁死不屈者", "提问引述的诗句（未指名作者）"],
   "working_keywords": ["马斯洛需求层次理论", "大数据", "英雄主义", "宁死不屈", "名留青史", "了无痕迹"]
  },
  "notes": "知乎问答回答；question 属提问者，作者未按提问指定的理论框架作答，而是质疑该理论的解释力。正文 5 段，text 与 lexical 无分歧（divergence=0），无图片节点，故 image_checked=false 不影响 status=read。brief 为正文前缀的截断文本。发表 2020-12-15，更新 2021-05-16。"
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
