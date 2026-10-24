# -*- coding: utf-8 -*-
"""批次 r001-b0186 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0186.sessions.py            # 写 out/r001-b0186.out.jsonl
  python3 records/r001-b0186.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0186"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0186.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "d74d0e64": {
  "analysis": {
   "question_context": "提问者问“如何评价乌克兰第六任总统泽连斯基？”（Q001），属提问者语境，不计入作者立场。作者不评价其履历或人品，而是按“剧本”向前推演：在俄军占战略优势、乌军成建制投降之后，泽连斯基与欧洲将面对什么；正文以“（未完，待续）”收尾，说明这是系列推演的一部分。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "总起：泽连斯基最危险的时候还没来；俄在占全部战略优势的前提下能以低成本低伤亡维持长期军事存在。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005", "P006"], "summary": "军事推演：俄军筑工事、建前线机场后以火炮和铁壳炸弹低成本消耗；乌军不动被啃、动则遭轰炸，且不必用精确制导武器。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008", "P009", "P010", "P011", "P012", "P013"], "summary": "对乌军特定番号组织“处决式战役”、备好反人类罪行证据并释放影像；随后围困喊话劝降，投降一批批加快。", "role": "other"},
    {"unit_id": "U004", "paragraph_refs": ["P014", "P015", "P016"], "summary": "成建制部队放弃抵抗后，泽连斯基与北约、美国的真正危机才开始；该剧情俄方无物理困难，俄内部不会有反战热潮。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P017", "P018", "P019", "P020", "P021", "P022"], "summary": "该节点传递三大信息：欧美保护不了附庸；欧美媒体欺骗世界、新闻道德破产；乌克兰丧失希望、北约威望与价值负面化。", "role": "conclusion"},
    {"unit_id": "U006", "paragraph_refs": ["P023", "P024", "P025", "P026", "P027", "P028"], "summary": "以深度抑郁症状和“躺平族”作类比与反问：被继续告知“还有希望”反而伤害最大，并追问是否有权放弃。", "role": "other"},
    {"unit_id": "U007", "paragraph_refs": ["P029", "P030", "P031", "P032", "P033", "P034", "P035", "P036", "P037", "P038"], "summary": "泽连斯基个人结局：英雄形象转为不管死活的老板；投降道德压力增大；CIA 可能担心他挺不住，用斩首轰炸或中毒把他变成烈士，为战后乌克兰留下俄乌血债；现在下结论还太早。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P039", "P040", "P041", "P042", "P043", "P044", "P045", "P046", "P047", "P048", "P049", "P050", "P051", "P052", "P053"], "summary": "后续剧本1：战后大量乌克兰人赴欧，数量或达一千万至两千万；欧盟无置身事外的借口，难民引发的选民对立将冲击欧洲政治生态，催生退出北约、退出欧盟的右翼主张。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P054", "P055", "P056", "P057", "P058", "P059", "P060", "P061", "P062", "P063", "P064", "P065", "P066", "P067", "P068", "P069", "P070"], "summary": "后续剧本2：北约前线驻军造成沉重财政负担，被作者称为无意义的“仇俄税”；俄可用极小动作打击东欧经济；北约亚洲方向负担更重，顶不住则亚洲影响力崩盘。", "role": "claim"},
    {"unit_id": "U010", "paragraph_refs": ["P071", "P072", "P073", "P074", "P075", "P076", "P077", "P078", "P079", "P080", "P081", "P082", "P083"], "summary": "后续剧本3：战后俄以能源、矿产、粮食为铁饭碗，保证能源高价是其核心利益；美俄与 OPEC 利益一致收割欧盟；欧盟共识决机制难以应对，可能出现脱欧公投与解体危机。", "role": "claim"},
    {"unit_id": "U011", "paragraph_refs": ["P084", "P085", "P086"], "summary": "收束：俄国处境逐步走上坡路；“甘蔗从苦吃到甜”；再次反问读者如何看待泽连斯基，标注未完待续。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "泽连斯基最危险的时候还没有到来。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "在占据全部战略优势的前提下，俄罗斯可以用很低的成本和伤亡维持在乌克兰的长期军事存在。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_qualified", "attribution": "author", "modality": "hypothetical", "statement": "俄军若站稳脚跟、构筑工事并建立前线支援机场，就能躲在工事里以长程榴弹炮和铁壳炸弹这类低成本方式让乌克兰持续流血。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "届时俄军每天的战争损耗会低得让乌克兰和欧盟绝望。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "乌军蹲守会被火炮逐步啃掉，冲击俄军坚固阵地则啃不动且在半小时内遭轰炸，而且用不上精确制导武器。", "evidence": ["E5", "E6"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "对乌军内部几个特定番号，俄罗斯大概会组织“处决式战役”。", "evidence": ["E7"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "乌军很难在围困下长期维持抵抗意志，投降会一批批出现且越来越快。", "evidence": ["E8", "E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "一旦有成建制部队放弃抵抗，泽连斯基和北约集团、美国的真正危机才开始迎面扑来。", "evidence": ["E10"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "上述剧情对俄罗斯没有物理上的实现困难，俄罗斯内部也绝不可能出现“反战热潮”。", "evidence": ["E11", "E12"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "到该节点会传递三个信息：欧美无法保护自己的附庸；欧美媒体的新闻道德完全破产；乌克兰丧失一切希望、北约威望和价值大幅负面化。", "evidence": ["E13", "E14", "E15"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正带来最大伤害的是继续被告知“还有希望”，并反问自己是否有权“放弃”“不努力了”。", "evidence": ["E16", "E17"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "questioned", "statement": "届时泽连斯基在乌克兰人民眼里是否还是“英雄”，还是那个不管死活的老板。", "evidence": ["E18"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "到那时泽连斯基真正危险的时刻才会到来：迫使他投降的道德压力越来越大，连 CIA 也会担心他挺不住。", "evidence": ["E19", "E20"]},
    {"claim_id": "C014", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "CIA 可能怕他不体面而帮他体面，通过神秘“斩首轰炸”或“二噁英中毒”把他变成烈士，以便给战后倒向俄罗斯的乌克兰留下最大的俄乌血债。", "evidence": ["E21", "E22"]},
    {"claim_id": "C015", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "作者自称此刻下结论还太早，全文的推演属剧本式预测。", "evidence": ["E23"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "战后必然有大量怕被清算的乌克兰人前往欧洲，数量可能达一千万到两千万；欧洲在道德上有完全接纳的责任，否则将失去道德优势与软实力。", "evidence": ["E24", "E25", "E26"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "难民问题造成的选民对立将把欧洲政治生态打击到天翻地覆，一定会有右翼候选人以退出北约甚至退出欧盟为口号而受追捧。", "evidence": ["E27", "E28"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "北约前线驻军的财政负担是近乎毫无意义的“仇俄税”，既不能支撑主动出击解决俄罗斯，对防御并不会发生的俄罗斯入侵也毫无意义。", "evidence": ["E29", "E30"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "俄罗斯可以用极小的动作毁灭性打击东欧国家的经济秩序，东欧将从欧洲经济增长点变成拖累欧盟的包袱。", "evidence": ["E31"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "在北约的亚洲敌人面前需要供养的国家更多，北约顶不住则亚洲影响力崩盘，因为它只养得起三个波兰。", "evidence": ["E32"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "战后俄罗斯靠能源、矿产、粮食三个铁饭碗，保证能源高价是其核心利益；美俄与 OPEC 利益一致，一起收割欧盟的“能源税”。", "evidence": ["E33", "E34"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "欧盟的共识决机制难以应对上述挑战，可能出现脱欧公决与欧盟解体危机，未来五年内或可见到。", "evidence": ["E35"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "在这整个过程中，俄罗斯的处境会一步步走上坡路。", "evidence": ["E36"]}
   ],
   "argument_steps": [
    "以“泽连斯基最危险的时候还没来”破题，把评价对象从个人挪到后续剧本（P001）。",
    "给出军事前提：俄占全部战略优势，可低成本长期驻留（P002）。",
    "推演消耗方式：工事＋前线机场＋长程火炮与铁壳炸弹，俄军日损耗极低（P003–P004）。",
    "推演乌军两难：不动被火炮啃，动则遭轰炸且不需精确制导武器（P005–P006）。",
    "引入“处决式战役”：对特定番号备好反人类罪行证据并释放影像，类比俄罗斯版“猎杀本拉登”（P007–P009）。",
    "推演投降示范效应：围困喊话、民生优待、成建制投降加快（P010–P013）。",
    "转折：真正危机不在乌军战场，而在泽连斯基、北约、美国的信誉与叙事破产（P014–P016）。",
    "列举三大外溢信息（P017–P022）。",
    "以抑郁症状和躺平族作类比，反问“放弃”的权利（P023–P028）。",
    "落到泽连斯基个人：英雄叙事崩塌→投降道德压力→CIA 可能“帮他体面”，并自注现在下结论太早（P029–P038）。",
    "延伸推演三条线：难民潮与欧洲政治生态、北约驻军财政与亚洲影响力、能源通胀与欧盟解体（P039–P083）。",
    "收束为俄国处境持续改善，并再次反问读者，标注未完待续（P084–P086）。"
   ],
   "concept_usage": [
    {"term": "剧本", "meaning": "作者对自己推演的称呼，指按既定力量对比向前外推的剧情线，自认属预测而非既成事实。", "evidence": "P039", "ambiguity": "全文以“大概”“可能”“一定”等不同强度的词推进，剧本与断言边界不清，P038 又称现在下结论太早。"},
    {"term": "处决式战役", "meaning": "对被点名的乌军番号实施歼灭并配套收集、公开反人类罪行证据的作战与宣传行动。", "evidence": "P007", "ambiguity": "未说明针对哪些番号，也未给出该说法的外部来源。"},
    {"term": "仇俄税", "meaning": "作者对北约前线驻军开支的贬称，指为应对不会发生的俄罗斯入侵而付出的、近乎无意义的财政成本。", "evidence": "P059", "ambiguity": "属作者自造评价性标签，非既有术语。"},
    {"term": "应许之地", "meaning": "指战后乌克兰人投奔的欧洲。", "evidence": "P041", "ambiguity": "带反讽色彩，作者未说明具体指哪些国家。"},
    {"term": "吃辽饷", "meaning": "借中国明代辽东军费的历史说法，指东欧国家由经济增长点变成需要欧盟供养的负担。", "evidence": "P063", "ambiguity": "历史类比未展开，作者未界定对应关系。"},
    {"term": "躺平族", "meaning": "作者借以类比不愿继续被“希望”驱使、选择放弃努力的人群，用来解释乌克兰可能出现的抵抗意志崩溃。", "evidence": "P027", "ambiguity": "从个体生活状态类比国家战争意志，跨域类比的边界未说明。"}
   ],
   "examples_and_targets": [
    "俄罗斯与俄军（作者推演的行为主体，非引用来源）",
    "乌克兰、乌军与“几个特定番号”（作者设定的被围歼对象，番号未指明）",
    "泽连斯基（本文被评价对象，作者预测其形象崩塌与人身危险）",
    "北约、欧盟、美国与 CIA（作者推演的对方阵营；CIA 部分为预测，无来源）",
    "“猎杀本拉登”（作者用作类比，指俄罗斯版处决式行动，P009）",
    "“对面战壕烤红薯……吃了饭你们再回去防守”的劝降戏码（作者预设的喊话桥段，P010）",
    "马克龙（作者点名可能面临右翼挑战的法国领导人，P052）",
    "德国梦幻般的难民安置计划（作者引作吸引移民的例子，P045）",
    "波兰士兵受命武力阻止难民（作者预测场景，P042）",
    "台湾与二十个陆海邻国（作者用于说明北约亚洲方向负担，P065）"
   ],
   "conditions": [
    "“在占据所有战略优势的前提下”，俄才能低成本长期驻留（P002）。",
    "“俄军站稳了脚跟……的话”，工事与前线机场才成立（P003）。",
    "“乌军只要敢有任何异动”才会招致轰炸（P006）。",
    "“一旦有这样的成建制部队放弃抵抗”，危机才迎面扑来（P014）。",
    "“到了这个节点”才释放三大信息（P017）。",
    "“俄罗斯要是战争结束得早”，马克龙才可能有那类危险（P052）。",
    "“可以预见未来两三年内”，难民冲击近乎无可避免（P053）。",
    "“如果顶不住”，才有北约亚洲影响力崩盘的后果（P067）。",
    "“我们可能在未来五年内”看到欧盟解体危机（P082）。",
    "全篇多处使用“大概”“可能”“一定”“必然”等不同强度的预测词，条件的成立与否作者未逐一论证。"
   ],
   "rhetoric_and_tone": "军事推演体加预言腔，第二人称“你”“你们”直接质问读者；大量未来时态的排比推进（“一批又一批”“一轮接一轮”）；用抑郁症状、躺平族、老人与壮小伙等类比；含粗口与自我审查式缩写（“狗x的xx蛋”“有你x的希望，希你nnd望”）；结尾以“（未完，待续）”标注系列未完。",
   "unresolved_questions": [
    "“对乌军内部的几个特定番号”未指明是哪些部队，无法核查。",
    "关于 CIA 可能“斩首轰炸”或“二噁英中毒”的说法是预测还是引述，正文未给出任何来源，需外部核查。",
    "难民数量“八百万”“一千万到两千万”的口径与依据未说明。",
    "P038 自称“现在下结论还太早”，与全文大量“一定”“必然”的预测并存，作者的判断强度边界不明。",
    "“北约只养得起三个波兰”中的“三个”如何得出，正文未说明。",
    "正文 P018 写作“1）”，P039 又另起“1）”，编号层级不同但未说明结构关系。",
    "本文标注“（未完，待续）”，后续内容不在本批，本文结论的完整性受限。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "泽连斯基最危险的时候还没来。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "可以以非常低的成本和伤亡维持在乌克兰的长期军事存在", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "就可以躲在坚固工事里安全而从容的用长程榴弹炮和铁壳炸弹", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "会低得令乌克兰和欧盟绝望", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "乌军蹲着不动，那就一点一点的用火炮往前啃。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "根本用不着“精确制导武器”，搞不好还都是冷战存货。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "俄罗斯大概是要组织“处决式战役”", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P011", "quote": "乌军很难在这样的围困下长期维持抵抗意志。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P013", "quote": "一批又一批的投降，越来越快的投降。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P014", "quote": "泽连斯基和北约集团、美国的真正危机才开始迎面扑来", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P016", "quote": "俄罗斯没有任何物理上的实现困难", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P016", "quote": "俄罗斯内部绝不可能出现什么“反战热潮”", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P018", "quote": "也没有办法在下定决心的强国面前保护自己的附庸", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P020", "quote": "它们的新闻道德完全破产。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P021", "quote": "北约的威望和价值大幅的负面化", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P023", "quote": "真正带来最大的伤害的，反而是继续跟我说还有xx希望", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P026", "quote": "我是不是没有权利“放弃”？我是不是没有权利“不努力了”？", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P029", "quote": "泽连斯基在乌克兰人民的眼里还是“英雄”吗？", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P031", "quote": "泽连斯基真正危险的时刻才会到来。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P032", "quote": "驱使他投降的道德压力会越来越大", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P035", "quote": "通过一次神秘的“斩首轰炸”或者“二噁英中毒”，把他变成烈士。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P036", "quote": "给彻底对北约和美国失望、不可避免大幅倒向俄罗斯的战后乌克兰留下最大的俄乌血债", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P038", "quote": "现在下结论还太早。", "relation": "qualifies"},
    {"key": "E24", "paragraph_id": "P040", "quote": "必然会有大量害怕俄罗斯清算报复的乌克兰人想要前往欧洲", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P043", "quote": "欧洲从一切意义上都有绝对的道德责任予以完全的、上不封顶的、毫不犹豫的接纳", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P046", "quote": "其数量甚至可以达到一千万到两千万", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P050", "quote": "难民问题所造成的选民对立，势必要把欧洲的政治生态打击到天翻地覆", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P051", "quote": "一定会有右翼候选人打出“退出北约”甚至“退出欧盟”的口号而受到热烈追捧", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P059", "quote": "它完全是一种近乎毫无意义的“仇俄税”", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P060", "quote": "也对防御事实上根本不会发生的“俄罗斯入侵”毫无意义", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P062", "quote": "俄罗斯可以以极小的动作，毁灭性的打击东欧国家的经济秩序", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P069", "quote": "北约只养得起三个波兰，没有名额了", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P076", "quote": "竭尽一切手段保证这些能源的高价格就是俄罗斯的核心利益了", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P078", "quote": "大家一起肆意收割欧盟的“能源税”", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P082", "quote": "我们可能在未来五年内看到欧盟解体危机", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P084", "quote": "俄罗斯的处境会一步一步的走向上坡路", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["国际军事与地缘政治", "俄乌战争推演", "欧洲政治经济", "舆论与宣传战"],
   "issue_candidates": ["泽连斯基的政治前途", "俄军消耗战与围困战术", "乌军成建制投降", "战后难民危机", "北约驻军成本", "欧洲能源与通胀", "欧盟解体风险"],
   "text_function_candidates": ["时评", "剧本式预测", "答疑", "宣传性推演"],
   "object_candidates": ["泽连斯基", "俄罗斯", "乌克兰", "北约", "欧盟", "美国", "CIA", "波兰", "马克龙", "OPEC"],
   "working_keywords": ["剧本", "处决式战役", "仇俄税", "仇俄", "铁饭碗", "能源税", "辽饷", "躺平族", "未完，待续"]
  },
  "notes": "语料字段无 provenance/superseded 版本差异。正文与 brief 前几段基本一致（brief 是正文截断）。全文含大量预测性表述（大概、可能、一定、必然），已按 predicted/qualified 保留强度，未写成已发生事实；个别脏话为作者自我审查式缩写（狗x的、nnd），照原文转录。本篇无图片节点，正文非空，status=read。"
 },
 "f7e156a2": {
  "analysis": {
   "question_context": "提问者问：在文体界制裁俄罗斯之后，乌副总理在推特呼吁封禁俄玩家游戏账号，如何评价这种做法、对俄罗斯有多大影响（Q001）。正文并未谈游戏账号或文体制裁，而是回答一个更宏观的问题：欧洲现在的仇俄言行在日后不得不向俄罗斯低头时会付出什么代价。正文与提问的具体对象之间缺少直接对应，作者也未说明为何这样作答。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004"], "summary": "总论与定义：欧洲的仇俄言行日后会变成代价昂贵的悔恨和俄罗斯安全的保障；“安全的心理屏障”是让曾辱骂你的人日后靠你的原谅活命时心生恐惧；这等于向俄罗斯送钱。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P005", "P006", "P007", "P008"], "summary": "力量与脆弱性对比：俄的自给自足、自我防卫、维持稳定与打击欧洲的能力都远胜欧洲；欧洲是需要极高安全条件才能维持脆弱经济秩序的松散群体，像听不得响动、上楼要扶扶手的老人，却在辱骂门外拿着狼牙棒的壮小伙。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P009", "P010", "P011", "P012", "P013"], "summary": "经济后果：欧洲增长停滞并进入长期倒退期；GDP 零或负增长且无法确认何时转正，结果资本跑光、失业如潮，断绝俄资源供应又推高成本与通胀。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P014", "P015", "P016", "P017"], "summary": "出路二选一：与俄和解，或彻底消灭俄罗斯这个乱源；后者被 6200 枚核弹一票否决，走前者则现在吐出来的要一勺一勺咽回去，欧洲一定后悔。", "role": "conclusion"},
    {"unit_id": "U005", "paragraph_refs": ["P018", "P019", "P020", "P021", "P022"], "summary": "俄方视角与欧洲处境：俄罗斯明白现在被骂的每句日后都是实打实的利益，今天骂多狠、日后求饶的礼物就堆多高；欧洲真正领导人清楚结果，但舆论被美国操纵绑架，只能被“民意”裹挟；辱骂对俄是利多。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P023", "P024"], "summary": "推断欧洲真正领导者的悔意：后悔没建自己的 YouTube、FB、推特，没在媒体准入上设门槛，后悔对美国设防太少。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "欧洲现在说的每句仇俄的话、做的每件排俄的事，在不得不向俄罗斯低头的时候，都会变成代价昂贵的悔恨和俄罗斯未来安全的保障。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“安全的心理屏障”就是让曾诽谤、辱骂、散播仇恨的人，在事后不得不依赖你的原谅活命时，一想起自己说过某句话就恐惧。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "这份恐惧会日夜折磨对方，直到其完全崩溃、任人宰割。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "欧洲的仇俄言行实际上是在向俄罗斯送钱。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "俄罗斯的自给自足、自我防卫、维持稳定能力，以及物理与心理打击欧洲的能力，都远远胜过欧洲。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "欧洲是需要极高安全条件才能维持其脆弱经济秩序、同时又养尊处优的松散群体。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "欧洲像一个听不得大响动、上楼要扶扶手的老人，正在辱骂一个衣衫褴褛的壮小伙；这小伙原先给老头打工，如今成了拿着狼牙棒站在门外的敌人。", "evidence": ["E7", "E8"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "欧洲的增长不但会停滞，还会进入一个相当长的倒退期。", "evidence": ["E9"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "GDP 增长为零甚至为负、且无法确认何时转正，其结果是极其严重的。", "evidence": ["E10"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "除直接服务刚性需求的行业外资本会跑光，失业如潮水涌来，断绝俄罗斯资源供应导致的成本上涨还会让通胀淹没欧洲。", "evidence": ["E11", "E12", "E13"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "欧洲只有两条路：获得与俄罗斯的和解，或彻底消灭俄罗斯这个乱源；后者已被 6200 枚核弹一票否决。", "evidence": ["E14", "E15"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "若走和解之路，现在吐出来的到时候只能一勺一勺咽回去，欧洲一定会后悔自己现在吐得太多。", "evidence": ["E16", "E17"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "俄罗斯一定明白：现在被骂的每一句，过几个月、一两年对它全是实打实的利益；今天骂多狠，到时候求饶的礼物就要堆多高。", "evidence": ["E18", "E19"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "欧洲真正的领导人一定清楚这个结果，但欧洲舆论完全被美国操纵和绑架，只能被“民意”裹挟，看着蠢人给自己挖墓穴。", "evidence": ["E20"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "现在的这些辱骂对俄罗斯是利多，而不是利空。", "evidence": ["E21"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "欧洲真正的领导者（工业集团、金融集团与背后的政策制定者）现在一定深深后悔没有建立自己的 YouTube、FB、推特，没在媒体准入上设立足够门槛。", "evidence": ["E22"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "他们一定在后悔自己对美国设防太少了。", "evidence": ["E23"]}
   ],
   "argument_steps": [
    "先给出总判断：欧洲今日的仇俄言行会成为日后的悔恨与俄罗斯的安全保障（P001）。",
    "定义“安全的心理屏障”：使对方在依赖你原谅活命时对旧言恐惧，恐惧终至崩溃（P002–P003）。",
    "把上述机制概括为一句话——这等于向俄罗斯送钱（P004）。",
    "给出力量前提：俄在自给、自卫、维稳与打击能力上远胜欧洲（P005）。",
    "给出脆弱性前提：欧洲需要极高安全条件维持脆弱经济秩序，惯于舒适生活（P006）。",
    "以“老人辱骂壮小伙”的比喻把力量对比形象化（P007–P008）。",
    "推出经济后果：停滞转长期倒退，资本外逃、失业潮、通胀（P009–P013）。",
    "排除一条出路：消灭俄罗斯被 6200 枚核弹否决；只剩和解，且代价是咽回今日之言（P014–P017）。",
    "换到俄方视角：今日之骂即日后之利，骂得越狠、求饶礼物越高（P018–P019）。",
    "解释欧洲为何仍会这么做：真正领导人清楚结果，但舆论被美国绑架（P020–P022）。",
    "收尾为对欧洲真正领导者的后悔推断：没建自己的平台、没设媒体门槛、对美国设防太少（P023–P024）。"
   ],
   "concept_usage": [
    {"term": "安全的心理屏障", "meaning": "作者自造说法，指通过让对方恐惧自己过去的言论被追究，从而在心理上确保其不敢再敌对。", "evidence": "P002", "ambiguity": "属作者定义，非既有术语；作者把它当作可主动经营的安全机制。"},
    {"term": "利多/利空", "meaning": "借用股市用语，指欧洲的辱骂对俄罗斯是净收益而非损失。", "evidence": "P022", "ambiguity": "股市术语用于国际政治，作者未界定衡量口径。"},
    {"term": "刚性需求", "meaning": "指不受经济波动影响的基本需求，其行业资本不会外逃。", "evidence": "P011", "ambiguity": "未列举具体行业。"},
    {"term": "乱源", "meaning": "作者对俄罗斯在欧洲眼中的定位描述，指被欧洲视为动荡根源。", "evidence": "P014", "ambiguity": "是作者转述欧洲视角还是自身判断，正文未明说。"}
   ],
   "examples_and_targets": [
    "乌副总理呼吁封禁俄玩家游戏账号、文体界制裁俄罗斯（提问者给出的事例，正文未提及）",
    "欧洲（作者评述对象）",
    "俄罗斯（作者判断的获益方）",
    "美国（作者指其操纵和绑架欧洲舆论，P020）",
    "YouTube、FB、推特（作者举为欧洲缺失的自有媒体平台，P023）",
    "6200 枚核弹（作者引作否决消灭俄罗斯方案的数据，来源未注明，P015）",
    "“老人辱骂壮小伙”比喻（作者的类比材料，P008）"
   ],
   "conditions": [
    "“在不得不向俄罗斯低头的时候”，欧洲的仇俄言行才会转为悔恨与俄的安全保障（P001）。",
    "“在事后不得不依赖你的原谅活命时”，恐惧机制才成立（P002）。",
    "“GDP增长一旦为零甚至为负，而且无法确认何时能转为正增长”，后果才极其严重（P010）。",
    "“要么……要么……”：作者把欧洲的选择限定为和解或消灭俄罗斯两条（P014）。",
    "“过几个月、过一两年”，辱骂才转为俄方利益（P018）。",
    "全篇以“一定”“会”为主，条件多为作者设定而非论证所得。"
   ],
   "rhetoric_and_tone": "断言式的时评语气，短句与排比推进（“越挖越深”）；用股市术语与生理化比喻（失业如潮水、通胀淹到鼻子）；用老人与壮小伙的对比作讽刺性类比；对欧洲使用“养尊处优”“蠢人”等贬抑措辞；第二人称“你”指欧洲。",
   "unresolved_questions": [
    "正文完全没有回应提问中的“封禁俄玩家游戏账号”与“对俄罗斯有多大影响”的具体问题，只谈欧洲仇俄言行的长期代价，作答与提问的对应关系不明。",
    "“6200 枚核弹”的数据来源未注明，需外部核查。",
    "“欧洲真正的领导者”“背后的政策制定者”具体指谁、是否与民选政府一致，正文未说明。",
    "“安全的心理屏障”这一自造概念没有给出可检验的判据。",
    "P020 说欧洲领导人清楚结果却无力改变，与 P023–P024 推断其“一定后悔”之间，作者未说明其推断依据。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "都会变成代价昂贵的悔恨和俄罗斯未来安全的保障", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "安全的心理屏障就是让曾经诽谤、辱骂、散播过对你的仇恨的人", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "直到ta完全崩溃，任人宰割", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "这实际上是在向俄罗斯送钱。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "俄罗斯的自给自足能力、自我防卫能力、维持稳定能力要远远的胜过欧洲", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "欧洲是一个需要极高的安全条件才能维持其脆弱的经济秩序", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "它实际上是听不得一点大响动、上楼一定要扶着扶手的老人。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "现在不但不给他打工，还成了拿着狼牙棒站在门外的敌人。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "欧洲的增长不但要陷入停滞，还要陷入一个相当长的倒退期。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P010", "quote": "而且无法确认何时能转为正增长，其结果是极其严重的", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P011", "quote": "除了那些直接服务于刚性需求的行业，别的行业资本会跑光。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P012", "quote": "失业会如潮水般涌来。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P013", "quote": "通货膨胀会淹到鼻子", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P014", "quote": "要么获得与俄罗斯的和解，要么彻底消灭俄罗斯这个乱源。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P015", "quote": "后者已经被6200枚核弹一票否决了。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P016", "quote": "现在吐出来的，到时候只能一勺一勺的咽回去", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P017", "quote": "欧洲一定会后悔自己现在吐得太多了。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P018", "quote": "你现在骂的每一句，过几个月、过一两年，对我全是实打实的利益", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P019", "quote": "今天骂多狠，到时候求饶的礼物就要堆多高。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P020", "quote": "可惜欧洲的舆论完全被美国操纵和绑架，只能眼睁睁的被“民意”裹挟", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P022", "quote": "现在的这些辱骂，对俄罗斯是利多，而不是利空。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P023", "quote": "现在一定深深的后悔自己没有建立自己的YouTube、自己的FB、自己的推特", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P024", "quote": "ta们一定在后悔自己对美国设防太少了。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["国际政治", "俄乌战争外溢效应", "欧洲经济", "舆论与媒体"],
   "issue_candidates": ["欧洲对俄制裁的长期代价", "俄欧力量对比", "欧洲经济停滞与通胀", "核威慑", "欧洲媒体主权", "美国对欧洲舆论的影响"],
   "text_function_candidates": ["时评", "答疑", "预测性论断"],
   "object_candidates": ["欧洲", "俄罗斯", "美国", "乌副总理", "YouTube", "FB", "推特"],
   "working_keywords": ["安全的心理屏障", "利多", "利空", "刚性需求", "乱源", "6200枚核弹"]
  },
  "notes": "正文与提问 Q001（封禁俄玩家游戏账号）几乎没有直接对应：全文谈欧洲仇俄言行的长期代价，未提游戏账号、文体制裁或对俄游戏业影响。已按原文如实记录，未据提问补写；此点记入 unresolved_questions。语料无 provenance/superseded 版本差异。本篇无图片节点、正文非空，status=read。"
 },
 "bcc2b54c": {
  "analysis": {
   "question_context": "提问者问“俄罗斯进军乌克兰是否合法正义”（Q001）。作者不作个人层面的正义裁决，而是先提出一套据称客观、内嵌于人类生存本能的正义法则（以旁观者视角判定“更有让步余地却不肯让步”的一方为不正义），再声明只预测历史对该战争的稳定评价最大概率，并用两个剧本推演；两个剧本都以设问结束，作者未给出明确答案。提问立场不计入作者立场。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003", "P004", "P005"], "summary": "提出法则：对无裁决人的纷争存在客观判定方法；在旁观者眼中，“让步余地更大却选择不让步而宁可纷争发生/持续/升级”的一方会被认定为不正义；预告将逐一解释细节。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P006", "P007", "P008", "P009", "P010", "P011", "P012", "P013", "P014", "P015", "P016"], "summary": "细节1：该正义观不依赖纷争的初始缘由；双方说法各自自洽、无人有资格裁断；谁先动手也不关键，非暴力迫害同样是致命暴力；溯因断正邪只是恶习，实质是判断者选用适合自身利益的衡量方法，且该选择是政治性的。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P017", "P018", "P019", "P020", "P021", "P022", "P023", "P024", "P025", "P026", "P027", "P028", "P029"], "summary": "溯因正义法的来历与缺陷：源于师长教育中的绝对尊卑，为把冲突扼杀在萌芽、降低管理成本；人人继承幼儿园老师式正义观（如“先动手的是坏孩子”）；缺陷是个体对等世界里没有幼儿园老师，用此法者只是伪装中立的斗争参与方。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P030", "P031", "P032", "P033", "P034", "P035", "P036", "P037", "P038", "P039", "P040", "P041", "P042", "P043", "P044", "P045"], "summary": "细节2：该方法只关注纷争终结；旁观者不参与瓜分桃子、只求尽快恢复安静，故采用能最快结束纷争的中立标准，兼顾保留总体力量与迫使被判非正义方放弃；桃子例子说明帮助失去代价更大的一方成本最低。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P046", "P047", "P048", "P049", "P050", "P051", "P052", "P053", "P054", "P055", "P056"], "summary": "法则的演化论根据与边界：不按此规则的群体在演化中被淘汰；“锄强扶弱”写在人类底层；但并非无条件站弱者，前提是弱者能与强者相持，否则旁观甚至帮强者击垮弱者；法则由整体生存概率最大化决定，是自然法、顺存逆亡、不接受异议。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P057", "P058", "P059", "P060", "P061", "P062", "P063", "P064", "P065", "P066", "P067", "P068", "P069", "P070", "P071", "P072", "P073"], "summary": "应用：不讨论个人好恶，而预测历史稳定评价的最大概率。剧本A（战争无限延续）与剧本B（升级到俄北核戒备）各自设问：哪一方更有让步余地而不肯让步；两次以“那会是谁？”收束，作者未点明答案；并称你我支持谁无关紧要。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P074", "P075", "P076", "P077", "P078", "P079", "P080", "P081", "P082"], "summary": "收尾与劝勉：写这些不是为讨论俄罗斯正义性这种空问题，而是让读者掌握法则以获更好生活；世界的存亡不如你重要；在无裁决人的纷争中记牢法则、忘掉“谁先动手”；运用法则者可获震慑力，不怒自威。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "判定纷争正义与否的法则不是人类发明的正义观，而是内嵌在人类生存本能里的自然准则。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "在旁观者眼中，“让步余地更大，却选择不让步而宁可纷争发生、持续或升级”的一方会被认定为不正义。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这一正义观最终不依赖纷争的初始缘由：双方攻击对方的理由往往不一致，谁也无法像上帝一样透视真相，没人能给真正有效的裁断。", "evidence": ["E3", "E4", "E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "谁先动手也不关键：先升级到动手的一方未必不正义，以非暴力形式实施的迫害同样是致命的暴力。", "evidence": ["E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "依据事情的起因判定是否正义只是人类的一种恶习，实质是判断者在各自均可自洽的对立逻辑中，选择适合自己利益的衡量方法。", "evidence": ["E7", "E8"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对法则的选择不是客观的而是政治性的：会在所有能把对方判罪的法则中选择能带来最多同盟者的那种，把“正义”当成同盟军的有效替代物。", "evidence": ["E9", "E10"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种方法的根源在于人类成长必经的师长教育，师长凭绝对尊卑不假思索地采用“从起因断正邪”，目的是把未来冲突扼杀在萌芽、降低自己的管理成本。", "evidence": ["E11", "E12", "E13"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人人都是这样长大的，于是继承了“先动手的那个是坏孩子”这类幼儿园老师的正义观；这根本无关正义，只关乎老师自己能否轻松一点。", "evidence": ["E14", "E15"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“溯因正义法”有致命缺陷：在真正的个体对等丛林世界没有幼儿园老师，失去老师的人只能徒劳论理，那只是个人表态与暴力攻防，与正义没有有效关系。", "evidence": ["E16", "E17"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "凡用这个方法的人其实只是潜伏在围观人群中的斗争参与方；没有中立立场，就谈不上正义判断。", "evidence": ["E18", "E19"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "该法则只关注纷争的终结：真正的旁观者不参与瓜分标的、对谁赢谁输漠不关心，只希望快点分完恢复安静，因此会采用能尽快结束纷争的中立标准。", "evidence": ["E20", "E21", "E22"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "旁观者考虑两个综合目的：尽可能保留总体力量；让被判定为非正义的一方尽快放弃继续纷争的企图。", "evidence": ["E23"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "双方久争不下说明势均力敌，旁观者会权衡自己干预的效率；帮助更有让步余地的一方施压，是更有效率、更快节约群体资源的策略。", "evidence": ["E24"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "桃子例子：若你失去桃子会饿死而对方只是饿一顿，旁观者帮你是终止纷争的最低成本方案；帮对方则会使群体多饿死一个成员并招致更激烈反抗。", "evidence": ["E25", "E26", "E27"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这就是人类正义观的客观法则：几百万年演化中，不按此规则行事的群体争不过按此规则的群体，会被淘汰。", "evidence": ["E28"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "“锄强扶弱”“劫富济贫”是写在人类底层的、真正最朴素的正义观。", "evidence": ["E29"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "该规则并不总是无条件驱动旁观者站在劣势者一方；前提是劣势者能与优势者形成相持，若无力相持，最低成本方案会是旁观甚至帮助强者击垮弱者“不自量力的以下犯上”。", "evidence": ["E30", "E31", "E32"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "客观的正义观由包括纷争双方和观察者的整体的生存概率最大化原则决定。", "evidence": ["E33"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这是自然法、天意，高于一切人类的个人立场和观点；它不由人的力量维护，而是自动通过自然规律强制实施，顺之者存、逆之者亡，不接受异议和反驳。", "evidence": ["E34", "E35", "E36"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者要谈的不是个人现在的好恶和主张，而是预测历史对这件事的稳定评价最大概率是什么。", "evidence": ["E37"]},
    {"claim_id": "C021", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "剧本A（战争无限延续）：乌克兰人民（恐怕也包括全世界人民）会觉得逼泽连斯基接受放弃入北约、放弃仇俄、永久中立容易，还是帮其击退俄罗斯容易？按作者的判准，更有余地让步而不肯让步、使战争延续的一方将被视为不正义，但作者只问“那会是谁”，未点明答案。", "evidence": ["E38", "E39", "E40"]},
    {"claim_id": "C022", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "剧本B（升级到俄罗斯与北约同时宣布核武器全面戒备预热）：全球旁观者彻夜难眠、集体利益极大受损时，帮俄施压迫使北约放弃东扩容易，还是帮北约强迫俄撤军接受战败容易，哪个成本更高、风险更小？作者同样以“那会是谁”收束，未点明答案。", "evidence": ["E41", "E42", "E43"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "至于你本人或我本人现在支持谁、喜欢谁，根本无关紧要，因为这是自然法的判决、历史的回答，高于一切。", "evidence": ["E44", "E45"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者声明写这些不是为讨论俄罗斯正义性这种没有营养的空问题，而是借例让读者明白法则的存在和运转逻辑，以帮助其获得更好的生活；世界的存亡皆不如“你”重要。", "evidence": ["E46", "E47"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "行动劝勉：在一切无预定裁决人的纷争中记牢该法则、忘掉“谁先动手”之类的幼儿园法则；纠缠谁先动手是心理发育不完全的表征，易招强者觊觎沦为猎物；主动运用法则者可获震慑力，不怒自威。", "evidence": ["E48", "E49", "E50", "E51"]}
   ],
   "argument_steps": [
    "以两问开场：纷争是否存在客观有效的正义判定方法，历史最终判定哪一方不正义（P001–P002）。",
    "提出法则：旁观者眼中，更有让步余地却宁可纷争发生、持续、升级的一方为不正义（P003–P004）。",
    "细节1之一：判定不依赖初始缘由，因为双方叙事不可通约、无人可作权威裁断（P006–P008）。",
    "细节1之二：谁先动手也不重要，非暴力迫害可构成致命暴力（P009）。",
    "反推溯因正义法的实质：只是选择适合自己利益的衡量方法，且该选择是政治性的（P010–P016）。",
    "追溯该方法来历：师长教育中的绝对尊卑与降低管理成本的需要（P017–P020）。",
    "指出其普遍化：人人继承幼儿园老师式正义观（P021–P024）。",
    "指出其致命缺陷：个体对等的世界里没有幼儿园老师，论理者实为斗争参与方（P025–P029）。",
    "细节2：该法则只关注纷争终结，旁观者以最快结束纷争为标准（P030–P034）。",
    "给出旁观者的两个综合目的与干预效率考量（P035–P038）。",
    "用抢桃子的例子说明最低成本方案是帮失去代价更大的一方（P039–P045）。",
    "给出演化论根据与“锄强扶弱”的底层性（P046–P047）。",
    "限定边界：须以弱者能形成相持为前提，否则旁观或帮强者（P048–P051）。",
    "把法则归结为整体生存概率最大化，并上升为自然法、顺存逆亡（P052–P056）。",
    "转向应用：不判个人好恶，只预测历史稳定评价的最大概率，设剧本A与剧本B并各自设问（P057–P070）。",
    "强调个人支持谁无关紧要，并说明写作目的是让读者掌握法则、过好生活（P071–P076）。",
    "落到劝勉与力量许诺：记牢法则、不要自误，不怒自威（P077–P082）。"
   ],
   "concept_usage": [
    {"term": "让步余地", "meaning": "指一方放弃争夺、退让以终止纷争的空间；判准的核心变量。", "evidence": "P004", "ambiguity": "未给出衡量标准；P038 写作“帮助更让步余地的一方逼迫更有让步余地的一方放弃继续争夺”，字面自相矛盾（疑为笔误），与 P040–P042 桃子例的方向不一致。"},
    {"term": "旁观者", "meaning": "不参与瓜分纷争标的、只希望纷争尽快结束、恢复安静的第三方。", "evidence": "P031", "ambiguity": "与 P028 所说“潜伏在围观人群中的斗争参与方”相对，作者未给出识别真正旁观者的方法。"},
    {"term": "溯因正义法", "meaning": "作者自造的贬称，指依据事情起因、谁先动手来判定正邪的方法。", "evidence": "P025", "ambiguity": "非既有术语，作者未说明其与常见正义理论的关系。"},
    {"term": "幼儿园老师", "meaning": "比喻拥有绝对权威、用简便规则压制冲突以省事的管理者（并延伸为“师长”“巨兽”）。", "evidence": "P023", "ambiguity": "隐喻可扩展至国家或国际组织，作者未界定边界。"},
    {"term": "巨兽", "meaning": "指拥有绝对权威、需要降低管理成本的主体。", "evidence": "P020", "ambiguity": "未明确对应现实中的哪类主体。"},
    {"term": "自然法", "meaning": "作者称由整体生存概率最大化决定、自动强制实施、高于个人立场的规律。", "evidence": "P053", "ambiguity": "作者称其“不接受异议和反驳”，属不可证伪的表述，未给检验方式。"},
    {"term": "锄强扶弱、劫富济贫", "meaning": "作者视为写在人类底层的最朴素正义观，即旁观者倾向帮助更难得让步的一方。", "evidence": "P047", "ambiguity": "与 P048–P050 的例外条件并存，作者强调其非无条件。"}
   ],
   "examples_and_targets": [
    "抢同一个桃子（作者的假想例，P031–P044，用于说明最低成本干预）",
    "挖水渠引走田水、被锄头打死（作者举例说明“谁先动手”判断无效，P009）",
    "“先动手的那个是坏孩子”“先骂人的那个是坏孩子”（作者举的幼儿园规则，P022）",
    "师长、幼儿园老师、巨兽（作者的比喻材料，P017–P024）",
    "猴群演化与群体淘汰（作者的演化论论证，无来源，P046）",
    "俄乌战争、泽连斯基、北约东扩（作者的预测应用对象，P057–P070）",
    "俄罗斯与北约同时宣布核武器全面戒备预热（剧本B的设定，P065）",
    "读者本人（第二人称劝勉对象，P072、P075）"
   ],
   "conditions": [
    "判准成立的前提是“在旁观者们的眼中”，即第三方视角（P004）。",
    "该法则只适用于无预定裁决人的纷争（P078、P079）。",
    "帮助弱者一方的前提是“劣势者能与优势者形成相持”（P049）；“如果劣势者无力形成相持”，则旁观甚至帮强者击垮弱者（P050）。",
    "剧本推演明确“排除明确的战胜/战败不谈”（P060）。",
    "P061 以插入语“（恐怕也包括全世界人民）”表达对范围的推测。",
    "全篇多处以“事实上”“必然”“根本”作断言，但应用部分以设问结束，未给出结论。"
   ],
   "rhetoric_and_tone": "训诫式教学语气，直接称呼“你们一定要记好”“看明白没有？”“所以，记住了——”；以连环设问推进（“那会是谁？”）；用日常例子（桃子、水渠）降低抽象门槛；对“溯因正义法”用贬抑语（恶习、老婴儿、幼儿园老师）；结尾由普遍法则转向个人劝勉与力量许诺（“不怒自威”）。",
   "unresolved_questions": [
    "P038 原文“帮助更让步余地的一方逼迫更有让步余地的一方放弃继续争夺”字面自相矛盾，疑为笔误或传输错误：按 P040–P042 桃子例，应指帮助“更难让步（失去代价更大）”的一方。此点直接影响对法则的理解，需回原始版本核对。",
    "剧本A、剧本B均以“那会是谁？”收束，作者未点明答案；不能替作者补出结论。",
    "提问问的是“俄罗斯进军乌克兰是否合法正义”，作者明确拒绝作个人正义裁决，只作历史评价的概率预测且未给答案，故本文未直接回答提问。",
    "演化论断言（不按该规则行事的猴群没机会演化成人类）未给出来源，属需外部核查的自然史/人类学主张。",
    "“自然法……不接受异议和反驳”属不可证伪的表述，作者未给检验方式。",
    "“让步余地”如何衡量、由谁衡量，正文未说明，而这正是判准的唯一变量。",
    "“巨兽”“那一方”等主体未落到具体实体。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P003", "quote": "而是内嵌在人类生存本能里的自然准则", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P004", "quote": "“让步余地更大，却选择不让步而宁可纷争发生/持续/升级”的一方，会被认定为不正义", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P006", "quote": "这一正义观最终不依赖纷争的初始缘由。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P007", "quote": "没人能给你们真正有效的裁断", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P008", "quote": "这是一个没有任何人有资格做权威裁断的逻辑死结", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P009", "quote": "看似先动手的是我，实际上先动手的是你。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P010", "quote": "依据一件事情到底是因为什么发生来判定到底它是否正义，只是人类的一种恶习。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P011", "quote": "选择了一种适合自己利益的衡量方法", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P014", "quote": "而是政治性的——即你会在所有能将对方判罪的法则中，选择能为你带来最多同盟者的那种", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P015", "quote": "视为“正义”的有效替代物罢了", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P018", "quote": "师长们不假思索的采用了“从起因断正邪”的方法", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P019", "quote": "ta希望将未来的可能冲突直接扼杀在萌芽状态", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P020", "quote": "于是大大的降低巨兽的管理成本", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P022", "quote": "“先动手的那个是坏孩子”，“先骂人的那个是坏孩子”", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P024", "quote": "它根本无关乎正义，只关乎幼儿园老师自己能不能轻松一点。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P025", "quote": "在真正的个体对等的丛林世界，没有幼儿园老师。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P027", "quote": "和正义根本就没有什么有效的关系", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P028", "quote": "其实只是潜伏在围观人群中的斗争参与方而已", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P029", "quote": "没有中立立场，谈何正义判断？", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P030", "quote": "这一方法只关注纷争的终结。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P033", "quote": "我们只希望你们快点分完，恢复安静。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P034", "quote": "即能尽快结束纷争的标准", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P035", "quote": "a）尽可能保留总体力量；b）能让被判定为非正义的一方尽快放弃继续纷争的企图", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P038", "quote": "是更有效率、能更快节约群体资源的策略", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P040", "quote": "你失去这个桃子会饿死，而ta失去这个桃子只是饿一顿。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P041", "quote": "那么我们帮你显然是终止纷争的最低成本的方案。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P043", "quote": "我们处理的结果是我们的种群会多饿死一个成员", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P046", "quote": "因为做不到的群体争不过按照这个规则行事的群体，会被后者淘汰", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P047", "quote": "这就是为什么“锄强扶弱”“劫富济贫”实际上是写在人类底层的、真正最朴素的正义观。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P048", "quote": "它并不总是无条件的驱动旁观者站在实力较弱、更困窘的劣势者一方", "relation": "qualifies"},
    {"key": "E31", "paragraph_id": "P049", "quote": "它有个前提，就是劣势者能与优势者形成相持。", "relation": "qualifies"},
    {"key": "E32", "paragraph_id": "P050", "quote": "就会是旁观（甚至帮助）强者击垮弱者不自量力的以下犯上", "relation": "qualifies"},
    {"key": "E33", "paragraph_id": "P052", "quote": "它事实上是由包括纷争双方和观察者的整体的生存概率最大化原则决定的", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P053", "quote": "这是自然法，是天意，它高于一切人类的个人立场和观点。", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P054", "quote": "而是自动的通过自然规律强制实施", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P055", "quote": "顺之者存，逆之者亡。", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P058", "quote": "而是在预测历史对这件事的稳定评价最大概率就是什么", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P061", "quote": "还是帮助泽连斯基击退俄罗斯容易？", "relation": "context"},
    {"key": "E39", "paragraph_id": "P063", "quote": "更有余地让步结束战争而不肯让步、使得战争延续的一方，将被视为不正义。", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P064", "quote": "那会是谁？", "relation": "context"},
    {"key": "E41", "paragraph_id": "P065", "quote": "一直升级到俄罗斯和北约同时宣布核武器全面戒备预热", "relation": "context"},
    {"key": "E42", "paragraph_id": "P066", "quote": "不知道今天躺下，明天还起不起得来", "relation": "context"},
    {"key": "E43", "paragraph_id": "P068", "quote": "哪一个成本更高？风险更小？", "relation": "context"},
    {"key": "E44", "paragraph_id": "P071", "quote": "是谁，在这两个剧本里谁在就最后被历史钉在耻辱柱上。", "relation": "context"},
    {"key": "E45", "paragraph_id": "P072", "quote": "至于你本人（或我本人）现在支持谁、喜欢谁，根本无关紧要。", "relation": "supports"},
    {"key": "E46", "paragraph_id": "P074", "quote": "而是为了借这个例子让你明白这法则的存在和运转逻辑，以帮助你获得更好的生活", "relation": "supports"},
    {"key": "E47", "paragraph_id": "P075", "quote": "世界的存亡，皆不如你重要。", "relation": "supports"},
    {"key": "E48", "paragraph_id": "P078", "quote": "忘记什么“谁先动手”之类的幼儿园法则，不要自误。", "relation": "supports"},
    {"key": "E49", "paragraph_id": "P079", "quote": "是一种心理发育不完全的表征", "relation": "supports"},
    {"key": "E50", "paragraph_id": "P081", "quote": "但会直觉到强烈的震慑，自然收起一切敌意", "relation": "supports"},
    {"key": "E51", "paragraph_id": "P082", "quote": "不怒自威。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["政治哲学", "正义理论", "演化论解释", "国际关系", "个人处世方法"],
   "issue_candidates": ["正义的判定标准", "旁观者视角", "溯因正义法批判", "弱者与强者的相持条件", "俄乌战争的正义性预测", "核升级风险"],
   "text_function_candidates": ["论说文", "定义与论证", "答疑", "训诫与劝勉", "预测"],
   "object_candidates": ["俄罗斯", "乌克兰", "泽连斯基", "北约", "旁观者", "幼儿园老师", "巨兽"],
   "working_keywords": ["让步余地", "旁观者", "溯因正义法", "从起因断正邪", "幼儿园老师", "锄强扶弱", "劫富济贫", "自然法", "顺之者存，逆之者亡", "不怒自威"]
  },
  "notes": "正文未直接回答提问“是否合法正义”，作者明确将问题转为“预测历史稳定评价的最大概率”，且两个剧本都以“那会是谁？”结束、未点明答案，已按 open_question 记录，未替作者补全结论。P038 原文“帮助更让步余地的一方逼迫更有让步余地的一方放弃继续争夺”字面自相矛盾，疑为笔误，已原样保留并记入 unresolved_questions，未改写原文。语料无 provenance/superseded 版本差异。本篇无图片节点、正文非空，status=read。"
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
