# -*- coding: utf-8 -*-
"""批次 r001-b0078 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0078.sessions.py            # 写 out/r001-b0078.out.jsonl
  python3 records/r001-b0078.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0078"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0078.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "e6c5aa02": {
  "analysis": {
   "question_context": "提问者问「中国道路为什么走得对？」，该问法本身预设了中国道路走得对，属提问者立场，不自动归给作者。作者未复述该问，而以自设问句开场（中国到底在走一条什么路），把议题转译为「王天下的路」，并以第二人称直接对中国青年发话。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "自设问句并作答：中国走的是王天下的路。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P003", "P004", "P005"], "summary": "实力强大在昂撒文化中是称霸的工具，在中华文化中是称王的条件。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P006", "P007"], "summary": "结论：中国终将加冕为王，昂撒只是一时枭雄；中国方法曲折缓慢但不可压制，登顶后极难被撼动。", "role": "conclusion"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009", "P010"], "summary": "以中国雄视东亚近2000年的历史反驳昂撒三四百年威风即正确之见，并用中央大陆不必学海豹作类比。", "role": "reason"},
    {"unit_id": "U005", "paragraph_refs": ["P011"], "summary": "批评马前卒对台湾的心态是美国式、盎格鲁-撒克逊式的，其方法论实为大英帝国以实力支撑权谋的体系。", "role": "rebuttal"},
    {"unit_id": "U006", "paragraph_refs": ["P012", "P013", "P014"], "summary": "中国真正的武器不是权谋而是大义；权谋须服从大义，故有不打第一枪等基本国策；这是最大的权谋，但是阳谋。", "role": "claim"},
    {"unit_id": "U007", "paragraph_refs": ["P015", "P016", "P017"], "summary": "把委曲求全的读法判为不理解中国；真正威胁不是外部攻击而是青年对称霸的渴望，要求中国人有清醒认识。", "role": "qualification"},
    {"unit_id": "U008", "paragraph_refs": ["P018", "P019", "P020"], "summary": "为王者须承担称霸者不肯也不能承担的责任；西方人不懂天下共主；中国永远不称霸但必终为王。", "role": "claim"},
    {"unit_id": "U009", "paragraph_refs": ["P021", "P022", "P023", "P024"], "summary": "只有这样的国家操持世界权柄，全球问题才有转机、人类才可能幸存；大过滤器时间恐不足百年，中国只有不到五十年。", "role": "reason"},
    {"unit_id": "U010", "paragraph_refs": ["P025", "P026"], "summary": "达成这一点靠的不是惊人的强大，而是惊人的温柔；每个关口都要靠惊人的温柔攻克。", "role": "claim"},
    {"unit_id": "U011", "paragraph_refs": ["P027", "P028", "P029", "P030"], "summary": "最大隐患是青年一代不了解中国而接受昂撒模式的精神烙印，成为站在中国开局上的美国玩家；这也是作者批评马前卒潮流的原因。", "role": "claim"},
    {"unit_id": "U012", "paragraph_refs": ["P031", "P032", "P033", "P034"], "summary": "以连续反问质问读者：要新的中国、下一个美国还是下一个斯大林的苏联？美国幸运是否配作楷模？致胜之道是剑还是犁？", "role": "other"},
    {"unit_id": "U013", "paragraph_refs": ["P035", "P036", "P037"], "summary": "接力棒迟早交给这一代，不能作为有中国血统和国籍的美国人接棒，因为美国人注定接不住。", "role": "action_advice"},
    {"unit_id": "U014", "paragraph_refs": ["P038", "P039"], "summary": "末尾标题式反问与残句「帝国主义的定义什么？」，结构上游离于上文论证。", "role": "other"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国走的是王天下的路。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "实力强大对昂撒文化与中华文化是两个不同的筹码：前者是称霸的工具，后者是称王的条件。", "evidence": ["E2", "E3", "E4"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "中国注定在最后加冕为王，昂撒文化只是一时枭雄与历史的过客。", "evidence": ["E5"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "中国的方法曲折且慢，但无法压制；一旦登顶，除非自己抛弃正道，否则极难再被挑战动摇。", "evidence": ["E6"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "不应因昂撒文化看似威风了三四百年就以为他们才是对的。", "evidence": ["E7"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国雄视东亚天下近2000年，将一个又一个曾经的军事霸主送进了坟墓。", "evidence": ["E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "马前卒现在对台湾的心态完全是美国式、盎格鲁-撒克逊式的，其根本方法论是大英帝国以实力支撑权谋的体系。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "中国真正的武器不是权谋；权谋必须服从于大义。", "evidence": ["E10"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "所有权谋最后都是用来暴露敌人的不义、证明自己的义理，所以才有不打第一枪、不首先动用核武器、不排除一切和平统一的努力等基本国策。", "evidence": ["E11"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "上述基本国策本身就是最大的权谋，但这是阳谋，不是实力不济的委曲求全。", "evidence": ["E12"]},
    {"claim_id": "C011", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "被作者反驳的看法：中国这些基本国策是实力不济的委曲求全。作者判定持此见者根本没有理解中国是什么以及中国为什么必然胜利。", "evidence": ["E13", "E14"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "长远的将来对中国称王的前途最大的威胁，不是外部的任何攻击，而是中国年轻人里泛滥着的对称霸的渴望。", "evidence": ["E15"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "为王的人必需承受只满足于称霸的人所不肯承受也不能承受的责任。", "evidence": ["E16"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国永远不称霸，但中国必终为王。", "evidence": ["E17"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "只有这样的国家来操持世界的权柄，世界才能从昂撒人的分裂状态里解脱，全球变暖、环境污染、物种灭绝才有扭转的现实希望。", "evidence": ["E18"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "大过滤器留给人类的时间恐怕已经不超过百年；中国只有不到五十年的时间让整个人类明白这一点。", "evidence": ["E19", "E20"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "要做到这一点靠的不是惊人的强大，而是靠惊人的温柔；这条路上的每一个关口都要靠惊人的温柔去攻克。", "evidence": ["E21", "E22"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "民族最大的隐患是青年一代并不了解中国自己，却在极大程度上潜移默化接受了昂撒模式才是唯一可行模式的精神烙印。", "evidence": ["E23"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这些青年是站在中国开局上的美国玩家，满脑子巧妙的威逼利诱、恐吓欺诈，对仁义礼智信没有信念。", "evidence": ["E24", "E25"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这是最大的危机，也是作者对马前卒所代表的这种潮流加以反复强烈批评的原因。", "evidence": ["E26"]},
    {"claim_id": "C021", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者以连续反问质问读者：希望中国成为新的中国，还是只成为下一个美国，甚至只是下一个斯大林的苏联；美国一两百年的幸运是否配作绝对正确的楷模；最终致胜之道到底是剑还是犁。", "evidence": ["E27", "E28", "E29"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "这一代不能作为有中国血统和国籍的美国人来接棒，因为美国人注定接不住。", "evidence": ["E30", "E31"]}
   ],
   "argument_steps": [
    "以自设问句确定议题：中国走的是王天下的路（P001-P002）。",
    "给出前提性对比：昂撒文化中实力是称霸工具，中华文化中实力是称王条件（P003-P005）。",
    "由此推出中国终将加冕为王、昂撒只是一时枭雄（P006）。",
    "补充中国方法特性：曲折且慢但不可压制，登顶后须自身抛弃正道才可能被撼动（P007）。",
    "以中国近2000年东亚史反驳昂撒三四百年即正确之见（P008-P009）。",
    "以中央大陆不必学海豹作类比（P010）。",
    "转入具体批评对象：马前卒对台心态及其大英帝国式方法论（P011）。",
    "提出正面命题：中国的武器是大义，权谋须服从大义（P012）。",
    "举不打第一枪、不首先动用核武器等基本国策为例证（P013）。",
    "排除误读：这是阳谋而非委曲求全，持后者之见者不理解中国（P014-P015）。",
    "指出真正威胁来自内部对称霸的渴望（P016-P017）。",
    "提出为王者的责任与天下共主，并给出永不称霸但必终为王（P018-P020）。",
    "推出世界意义：只有中国操持权柄，全球问题才有转机、人类才可能幸存（P021-P022）。",
    "给出时间尺度与大过滤器（P023-P024）。",
    "给出方法：惊人的温柔（P025-P026）。",
    "指出最大隐患为青年所受昂撒模式精神烙印，并说明批评马前卒潮流之因（P027-P030）。",
    "以连续反问施压并要求读者想清楚（P031-P034）。",
    "结论：接力棒将交给这一代，美国人注定接不住（P035-P037）。"
   ],
   "concept_usage": [
    {"term": "王天下／称王", "meaning": "以从容照顾其他人利益为条件的统治正当性，与称霸相对", "evidence": "P002/P005", "ambiguity": "未给出制度性或历史性的界定，仅以筹码与责任描述"},
    {"term": "称霸", "meaning": "实力强大后不必顾及其他人的统治方式，被归于昂撒文化", "evidence": "P004", "ambiguity": "与称王的界限由作者单方划定"},
    {"term": "权谋", "meaning": "权术谋略；作者称中国真正的武器不是它，又称所有权谋最后都用于暴露敌人不义", "evidence": "P012/P013", "ambiguity": "权谋既被否定又被纳入大义之下，二者边界未说明"},
    {"term": "阳谋", "meaning": "以公开的基本国策呈现的最大权谋", "evidence": "P014", "ambiguity": "无定义，仅与委曲求全对举"},
    {"term": "大义／义理", "meaning": "与权谋相对的道义正当性", "evidence": "P012/P013", "ambiguity": "未说明由谁判定"},
    {"term": "昂撒／盎格鲁-撒克逊", "meaning": "指英美文化及其战略方法论", "evidence": "P003/P011/P028", "ambiguity": "时而指文化、时而指族群或国家，所指不固定"},
    {"term": "天下共主", "meaning": "为王者的世界性责任，作者称西方人不懂", "evidence": "P018", "ambiguity": "未说明其权力结构"},
    {"term": "惊人的温柔", "meaning": "作者给出的达成王天下的方法，与惊人的强大对举", "evidence": "P025/P026", "ambiguity": "未给出任何具体所指或操作标准"},
    {"term": "大过滤器", "meaning": "人类文明存亡的筛选机制，用于给出百年尺度", "evidence": "P023", "ambiguity": "术语来源与定义本文未说明"},
    {"term": "仁义礼智信", "meaning": "作者称青年对其毫无信念的儒家德目", "evidence": "P029", "ambiguity": "未展开各目的含义"},
    {"term": "岛国心理缺陷", "meaning": "作者对昂撒阴谋策略成因的贬称", "evidence": "P009", "ambiguity": "属修辞性判断，未给出论证"}
   ],
   "examples_and_targets": [
    "马前卒（第三方评论者）：作者的批评对象，涉其对台湾的心态与方法论（P011、P030）。",
    "昂撒文化／大英帝国：作者的反驳对象及其实力支撑权谋方法论的来源（P004、P011）。",
    "美国、苏联／斯大林：反问中列举的楷模与前车（P031、P032）。",
    "中国雄视东亚天下近2000年、将军事霸主送进坟墓：作者的历史论据（P008），属事实断言，待外部核查。",
    "不打第一枪、不首先动用核武器、不排除一切和平统一的努力：作者列举的基本国策例证（P013）。",
    "鲸鱼与海豹、中央大陆：类比修辞（P010）。",
    "秦失其鹿：末尾标题所用的历史典故（P038）。",
    "全球变暖、环境污染、物种灭绝、种族宗教冲突：作者列举的全球问题（P021）。",
    "大过滤器、百年与不到五十年：作者引用的时间尺度（P023、P024），来源未说明。"
   ],
   "conditions": [
    "中国登顶后极难被撼动以「除非自己抛弃正道」为条件（P007）。",
    "全球问题得到扭转以「只有这样的国家来操持世界的权柄」为条件（P021）。",
    "人类在此轮技术浪潮中幸存亦被绑定于中国式的领导（P022）。",
    "时间限制：大过滤器留给人类的时间恐怕已不超过百年，中国只有不到五十年（P023、P024）。",
    "对象条件：训诫主要面向中国人、中国的青年人（P017），并特指青年一代接棒者（P035）。",
    "自我限定：中国永远不称霸（P020）。"
   ],
   "rhetoric_and_tone": "激昂的训诫与劝勉语气，第二人称你们直接呼告；密集反问（P019、P031、P032、P033）与命令句（P034）；以ta代他／她／他们并大量使用【】作强调（P014、P026、P028）；比喻类比（一时枭雄、历史的过客、鲸鱼与海豹）；对马前卒及小孩子们的贬抑措辞（岛国心理缺陷、文盲一样的蠢人）；末尾以秦失其鹿的典故收束。",
   "unresolved_questions": [
    "P039残句「帝国主义的定义什么？」与P038标题「不然秦现在何以失其鹿？」结构上游离于上文，是否为未完稿或平台截断，正文未说明。",
    "「惊人的温柔」未给出具体所指或操作标准。",
    "「大过滤器」的术语来源与含义本文未说明，需外部核查。",
    "「中国雄视东亚天下近2000年」等历史断言需外部核查。",
    "马前卒的身份及其原文观点未在本文给出，作者转述是否准确无法由本文核验。",
    "提问者所说的「中国道路」与作者的「王天下的路」是否同指，正文未明确对应。",
    "P038在结构中标记为heading但内容是反问句，其结构作用不明。",
    "本篇无图片节点，图片维度的核验不适用；brief仅140字且被截断，只能作导航。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P002", "quote": "王天下的路。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P003", "quote": "实力强大对昂撒文化和中国文化是两个完全不同的筹码。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P004", "quote": "在昂撒文化里，实力强大是可以不必顾及其他人的筹码，是称霸的工具；", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P005", "quote": "在中国的文化里，实力强大是可以从容照顾其他人利益的筹码，是称王的条件。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P006", "quote": "正因为是这样，中国才注定在最后加冕为王。而昂撒文化注定只是一时枭雄，历史的过客。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P007", "quote": "中国的方法曲折而且慢，但却是无法压制的，而且一旦登顶，除非自己抛弃正道，否则极其难以再被挑战动摇。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P008", "quote": "不要因为昂撒文化看似威风了三四百年就以为他们才是对的。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "中国雄视东亚天下近2000年，将一个又一个曾经的军事霸主送进了坟墓。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P011", "quote": "马前卒现在对台湾的心态，完全是美国式的、盎格鲁-撒克逊式的。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P012", "quote": "中国真正的武器不是权谋", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P013", "quote": "所以才有不打第一枪，不首先动用核武器，不排除一切和平统一的努力", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P014", "quote": "这本身就是最大的权谋，但这是阳谋。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P014", "quote": "这【不是“实力不济的委曲求全”】。", "relation": "context"},
    {"key": "E14", "paragraph_id": "P015", "quote": "凡是在任何意义上认为是后者的人，自己根本就没有理解中国到底是什么以及中国为什么必然会胜利。", "relation": "contradicts"},
    {"key": "E15", "paragraph_id": "P016", "quote": "不是外部的任何攻击，而是中国年轻人里泛滥着的对称霸的渴望", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P018", "quote": "为王的人，必需承受只满足于称霸的人所不肯承受也不能承受的责任。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P020", "quote": "中国永远不称霸，但中国必终为王。", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P021", "quote": "只有这样的国家来操持世界的权柄，这个世界才能从昂撒人的这种机关算尽、机械阴谋、刻意谋划的分裂状态里解脱出来。", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P023", "quote": "大过滤器留给人类的时间恐怕已经不超过百年。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P024", "quote": "我们只有不到五十年的时间让整个人类明白这一点。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P025", "quote": "而要做到这一点，靠的不是惊人的强大，而是靠惊人的温柔。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P026", "quote": "这条路上的每一个关口，都要靠【惊人的温柔】去攻克", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P027", "quote": "因为我们这个民族最大的隐患，就是我们的青年一代在事实上并不了解中国自己", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P028", "quote": "ta们并没有意识到ta们只是一群站在“中国开局”上的【美国玩家】", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P029", "quote": "ta们完全没有对仁、义、礼、智、信的丝毫信念。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P030", "quote": "这是我们最大的危机，这也是为什么我对马前卒所代表的这种潮流加以反复强烈批评的原因。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P031", "quote": "你们是希望中国成为新的中国，还是只是希望中国成为下一个美国？甚至只是下一个斯大林的苏联？？", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P032", "quote": "美国这么一两百年的【幸运】，就配中国看在眼里，以为绝对正确的“楷模”吗？", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P033", "quote": "这个世界的最终致胜之道到底是什么，到底是剑还是犁？", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P036", "quote": "你们不能作为有中国血统和国籍的“美国人”来接这一棒。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P037", "quote": "因为“美国人”注定接不住。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P039", "quote": "帝国主义的定义什么？", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["国际政治与战略", "政治文化／文明比较", "历史观与文明兴衰", "时政评论"],
   "issue_candidates": ["中国道路", "称霸与称王", "中西／中美文化对比", "台湾问题", "青年国家认同", "全球治理与人类存续", "战略方法论"],
   "text_function_candidates": ["评论", "论辩与批驳", "训诫劝勉"],
   "object_candidates": ["中国", "美国", "昂撒／盎格鲁-撒克逊文化", "大英帝国", "苏联", "斯大林", "马前卒", "台湾", "东亚", "秦"],
   "working_keywords": ["王天下", "称霸", "称王", "权谋", "大义", "阳谋", "天下共主", "惊人的温柔", "大过滤器", "仁义礼智信", "委曲求全", "岛国心理缺陷", "实力支撑权谋"]
  },
  "notes": "正文与lexical结构有一处不一致：P039（帝国主义的定义什么？）是text尾部未被lexical覆盖的片段（text_tail_not_in_lexical，char_start=1823），本文按body计入并作为残句标记。brief为140字截断文本，仅作导航。本篇无图片节点，故图片核验不适用；提问与全文39段均已阅读，full_text_checked=true。"
 },
 "e9569275": {
  "analysis": {
   "question_context": "提问者引述布热津斯基关于中国是地区性国家、日本是国际性国家的判断，问如何理解该说法。提问字段中的引述属提问者，不归给作者。作者正文未点名布热津斯基，也未逐句回应其判断，而是把对象扩展为西方战略家整体并加以贬评，转而提出自己对战略评判标准的看法。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "总评：西方战略家不过如此，且称这是没救的文化基因缺陷。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003"], "summary": "理由：英美在近现代丢掉基督教的文化理想，退化成只知道吃的爬行动物；其战略愿景与思想原始得可悲可笑。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P004"], "summary": "以有了激光枪的匈奴人为喻，称其无法理解未来局势，仍在做地缘政治与离岸平衡的大梦。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P005", "P006"], "summary": "提出正面标准：统治者须以人类为基本出发点，把本国命运嵌入人类命运；动保持优势的捣乱念头者已失去坐在棋盘上的资格。", "role": "claim"},
    {"unit_id": "U005", "paragraph_refs": ["P007", "P008"], "summary": "预测未来竞争是对人类贡献能力的竞争，世界属于最能保证人类切实福祉的国家；并称人类已觉醒、不再接受旧规则。", "role": "conclusion"},
    {"unit_id": "U006", "paragraph_refs": ["P009", "P010"], "summary": "以评分标准变了还在练滑铲作结，并以詈语收束。", "role": "other"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "西方战略家也就不过如此。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "西方战略的缺陷是文化基因缺陷，没救的。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "英美在近现代丢掉了基督教的文化理想，退化成了一头只知道吃的爬行动物。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "所谓战略，其愿景和思想都原始得可悲，到了可笑的程度。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这些战略家只是一群有了激光枪的匈奴人，根本无法理解和想象未来局势的真正发展，还在发地缘政治、离岸平衡的大梦。", "evidence": ["E5", "E6"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这个时代的统治者必须以人类为考虑问题的基本出发点，只能把自己国家的命运嵌入到人类的命运中去考虑。", "evidence": ["E7", "E8"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "只要动了这里捣乱、那里使绊子来保持自己优势的念头，就已经失去了真正坐在棋盘上的资格。", "evidence": ["E9"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "未来的竞争是对人类贡献能力的竞争，世界属于最能保证人类切实福祉的国家；还抱着动手动脚龌龊念头的，前途一定直奔地狱。", "evidence": ["E10", "E11"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人类已经觉醒，不再接受这个游戏规则；人类所面对的问题也已经不再接受这种规则。", "evidence": ["E12", "E13"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "评分标准已经变了，而对方还在练滑铲（比喻仍在练已被淘汰的旧招式）。", "evidence": ["E14"]},
    {"claim_id": "C011", "claim_type": "quoted_or_cited", "attribution": "questioner", "modality": "asserted", "statement": "提问者引述布热津斯基的判断：中国并非全球性而是地区性的国家，日本并非地区性而是国际性的国家，并问如何理解。", "evidence": []},
    {"claim_id": "C012", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "被作者反驳的做法：以这里捣乱、那里使绊子来保持自己的优势，并继续按地缘政治、离岸平衡的框架谋划。", "evidence": ["E6"]}
   ],
   "argument_steps": [
    "先给出总评：西方战略家不过如此，并把它归因于没救的文化基因缺陷（P001-P002）。",
    "给出历史理由：英美丢掉基督教的文化理想而退化，故其战略愿景原始可笑（P003）。",
    "以匈奴人拿到激光枪为喻，指其无法理解未来局势，仍沉迷地缘政治与离岸平衡（P004）。",
    "提出正面标准：统治者须以人类为出发点、把本国命运嵌入人类命运（P005）。",
    "给出排斥条件：动保持优势的捣乱念头者失去坐在棋盘上的资格（P006）。",
    "预测未来竞争是贡献能力之争，世界属于最能保证人类福祉的国家（P007）。",
    "补充前提：人类已经觉醒且现实问题也不再接受旧规则（P008）。",
    "以评分标准变了还在练滑铲作结（P009），并以詈语收束（P010）。"
   ],
   "concept_usage": [
    {"term": "文化基因缺陷", "meaning": "作者用来说明西方战略能力不足的根源性缺陷，并称没救", "evidence": "P002", "ambiguity": "无定义，未说明是否可改变，也未给出判据"},
    {"term": "地缘政治、离岸平衡", "meaning": "作者称为大梦的西方战略框架", "evidence": "P004", "ambiguity": "术语未解释，仅作贬评对象"},
    {"term": "以人类为考虑问题的基本出发点", "meaning": "作者为这个时代统治者设定的行为标准", "evidence": "P005", "ambiguity": "未说明如何操作或由谁裁定"},
    {"term": "坐在棋盘上的资格", "meaning": "参与世界博弈的正当资格，以不以捣乱使绊子保持优势为条件", "evidence": "P006", "ambiguity": "资格由谁授予未说明"},
    {"term": "对人类贡献能力", "meaning": "作者设定的未来竞争内容", "evidence": "P007", "ambiguity": "贡献如何计量未说明"},
    {"term": "练滑铲", "meaning": "比喻继续操练已被淘汰的旧招式", "evidence": "P009", "ambiguity": "口语化比喻，未界定所指的具体招法"}
   ],
   "examples_and_targets": [
    "布热津斯基：只出现在提问者的引述中，正文自P001至P010均未点名，作者未逐句回应其判断。",
    "英美：作者的批评对象（P003、P004）。",
    "基督教的文化理想：作者称被英美在近现代丢掉（P003）。",
    "爬行动物、有了激光枪的匈奴人：对批评对象的贬抑性比喻（P003、P004）。",
    "地缘政治、离岸平衡：被指为过时的大梦（P004）。",
    "滑铲：比喻旧招式（P009）。",
    "傻x：末尾詈语（P010），属修辞而非主张。"
   ],
   "conditions": [
    "以「只要动了……的念头，就已经失去了……资格」的条件句给出排斥性判断（P006）。",
    "统治者必须且只能以人类为出发点，是作者给出的规范性要求（P005）。",
    "判断指向未来竞争（P007），并把人类已觉醒作为既成前提（P008）。",
    "评价对象限定为这个时代的统治者与西方战略家，未限定具体国家或时段（P005、P001）。"
   ],
   "rhetoric_and_tone": "冷嘲与极端贬抑：爬行动物、有了激光枪的匈奴人、练滑铲等比喻；格言式短句连缀；以ta们代称他／他们；末段以詈语「傻x。」收束，情绪外露而无论证。",
   "unresolved_questions": [
    "正文未点名布热津斯基，作者是否针对提问所引的具体判断作答，无法由正文确认。",
    "文化基因缺陷无定义与判据，也不清楚作者是否认为其绝对不可改变（作者称没救）。",
    "「人类已经觉醒」的主体、范围与时间未界定。",
    "地缘政治、离岸平衡等术语未解释，其指涉需外部核查。",
    "提问者所引布热津斯基原话的出处与语境未给出，需外部核查。",
    "brief 为140字截断文本（末尾为还在发地缘政治、），只能作导航，不能支持任何主张。",
    "本篇无图片节点，图片维度核验不适用。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "西方“战略家”，也就不过如此了。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "这是文化基因缺陷，没救的。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "英美在近现代丢掉了基督教的文化理想，退化成了一头只知道吃的爬行动物。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P003", "quote": "所谓的“战略”，其愿景和思想都原始得可悲，到了可笑的程度。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "这只是一群有了激光枪的匈奴人", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P004", "quote": "还在发地缘政治、离岸平衡的大梦。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P005", "quote": "这个时代的统治者必须以人类为考虑问题的基本出发点，只能把自己国家的命运嵌入到人类的命运中去考虑。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P005", "quote": "只能把自己国家的命运嵌入到人类的命运中去考虑", "relation": "qualifies"},
    {"key": "E9", "paragraph_id": "P006", "quote": "只要动了那种这里捣乱、那里使绊子来“保持自己的优势”的念头，就已经失去了真正坐在棋盘上的资格。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P007", "quote": "未来的竞争是对人类贡献能力的竞争，世界属于最能保证人类切实福祉的国家。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P007", "quote": "前途一定直奔地狱。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P008", "quote": "人类已经觉醒，ta们不再接受这个游戏规则了", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P008", "quote": "人类所面对的问题也已经不再接受这种规则。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P009", "quote": "评分标准都变了，还在练滑铲。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P010", "quote": "傻x。", "relation": "context"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["国际关系与战略", "政治文化批评", "时政评论"],
   "issue_candidates": ["西方战略家评价", "地缘政治与离岸平衡", "大国竞争的评判标准", "人类共同福祉", "国际规则变迁"],
   "text_function_candidates": ["评论", "批评与批驳", "讽刺"],
   "object_candidates": ["布热津斯基（提问者引述）", "英美", "西方战略家", "匈奴人（比喻）", "人类"],
   "working_keywords": ["战略家", "文化基因缺陷", "基督教的文化理想", "离岸平衡", "棋盘", "贡献能力", "练滑铲"]
  },
  "notes": "正文未出现布热津斯基之名，提问者的引述只在question字段，且question不在机械生成的段落结构中，故该条quoted_or_cited主张无段落级短引（见unresolved_questions）。brief为140字截断文本（末尾还在发地缘政治、），仅作导航。本篇无图片节点，图片核验不适用；全文10段与提问均已阅读。"
 },
 "e6d6bfe3": {
  "analysis": {
   "question_context": "提问者问员工辞职是否需要为现公司考虑。作者未直接给出应当与否的规范判断，而是把问题转换为：什么样的企业才配有离职员工的体贴，并以个人职业生涯的视角提出以再入职意愿鉴定好企业的标准，再用条件句说明该问题在何种企业里根本不存在。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002"], "summary": "从个人职业生涯角度提出好企业的一条鉴定标准：走了的员工不介意再回来、企业也乐于再录用，这样的企业更像职业母港。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P003"], "summary": "提出光荣退役是达成这一点的关键条件之一。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005"], "summary": "以条件句给出两种情形：无此文化传承的企业难获离职员工体贴、只能指望《劳动法》；有此传承则人人愿留后路，问题不存在。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "从个人职业生涯的角度可以说，好企业只有一条最好用的鉴定标准：走了的员工不介意再回来，而企业也乐于再录用。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "某种意义上，这样的企业并没有离去的员工，它更像是职业母港。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "光荣退役（honorable discharge）是达成母港式效果的关键条件之一。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "如果一家企业没有这种文化传承或先例，它自然很难获得离职员工的过多体贴，勉强只能指望《劳动法》那点保障。", "evidence": ["E4", "E5"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "如果企业有这种传承，又有谁不想多条后路，辞职是否为现公司考虑的问题也就根本不存在了。", "evidence": ["E6"]}
   ],
   "argument_steps": [
    "限定视角：从个人职业生涯的角度谈（P001）。",
    "给出标准：以离职员工是否愿意回来、企业是否乐于再录用鉴定好企业（P001）。",
    "以职业母港作比喻，说明这类企业没有真正离去的员工（P002）。",
    "补充条件：光荣退役是达成这一点的关键条件之一（P003）。",
    "反设第一种情形：无此文化传承的企业难获离职员工体贴，只剩《劳动法》保障（P004）。",
    "反设第二种情形：有此传承则人人愿留后路，提问者的问题不成立（P005）。"
   ],
   "concept_usage": [
    {"term": "好企业", "meaning": "以离职员工是否愿意回来、企业是否乐于再录用为最好用的鉴定标准", "evidence": "P001", "ambiguity": "作者自称这是最好用的一条标准，是否排除其他标准未说明"},
    {"term": "职业母港", "meaning": "比喻企业像母港，员工离开但不算离去", "evidence": "P002", "ambiguity": "航海比喻，未给出可操作判据"},
    {"term": "光荣退役（honorable discharge）", "meaning": "被作者称为达成母港效果的关键条件之一的离职方式", "evidence": "P003", "ambiguity": "本文未定义其具体内容，英文术语来源需外部核查"},
    {"term": "文化传承（或先例）", "meaning": "企业是否已有光荣退役的先例与传统", "evidence": "P004", "ambiguity": "先例与新制度的界限未说明"},
    {"term": "《劳动法》", "meaning": "被援引为无此文化传承时离职员工的最低保障来源", "evidence": "P004", "ambiguity": "未指明具体条款或保障内容"}
   ],
   "examples_and_targets": [
    "《劳动法》：作者援引的法律，作为无文化传承时员工可指望的最低保障（P004）。",
    "honorable discharge：引用的英文军事术语，用作企业离职文化的类比（P003）。",
    "母港：航海比喻，用于描述企业与离职员工的关系（P002）。"
   ],
   "conditions": [
    "结论限定于从个人职业生涯的角度（P001）。",
    "标准被表述为最好用的一条，未称为唯一正确的标准（P001）。",
    "条件句一：如果企业没有这种文化传承或先例，就很难获得离职员工的过多体贴（P004）。",
    "条件句二：如果企业有，则多条后路人人想要，问题不存在（P005）。",
    "光荣退役只是关键条件之一，作者未称其为充分条件（P003）。"
   ],
   "rhetoric_and_tone": "温和的职场建议口吻，以条件句代替直接回答；用母港与光荣退役两个比喻承载判断；以反问「又有谁不想多条后路呢？」推进结论；用引号标示好企业与离去等关键词。",
   "unresolved_questions": [
    "提问者问员工辞职是否需要为现公司考虑，作者未直接给出应当与否的判断，只给出企业侧的条件，规范性结论需读者自推。",
    "光荣退役的具体含义与操作方式本文未说明，honorable discharge 的军事来源需外部核查。",
    "好企业只有一条最好用的鉴定标准是否排除其他标准，未说明。",
    "《劳动法》所提供保障的具体内容未说明，需外部核查。",
    "brief 为140字截断文本（末尾为如果一家），只能作导航，不能支持任何主张。",
    "本篇无图片节点，图片维度核验不适用。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "“好企业”只有一条最好用的鉴定标准——走了的员工不介意再回来，而企业也乐于再录用。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "它更像是“职业母港”。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "而“光荣退役”（honorable discharge）是达成这一点的关键条件之一。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "如果一家企业并没有这种文化传承（或先例），那么它自然很难获得离职员工的过多体贴", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "勉强能指望《劳动法》那点保障罢了。", "relation": "qualifies"},
    {"key": "E6", "paragraph_id": "P005", "quote": "如果它有，又有谁不想多条后路呢？这个问题也就根本不存在了。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["职场与职业发展", "组织文化与管理", "劳动法与社会保障"],
   "issue_candidates": ["离职与再入职", "企业文化传承", "员工与雇主关系", "职业母港"],
   "text_function_candidates": ["答疑", "经验总结", "建议"],
   "object_candidates": ["企业", "离职员工", "《劳动法》"],
   "working_keywords": ["好企业", "职业母港", "光荣退役", "honorable discharge", "文化传承", "先例", "多条后路"]
  },
  "notes": "本篇无图片节点，图片核验不适用；全文5段与提问均已阅读，author_bytes 约 4KB。brief 为140字截断文本，仅作导航。honorable discharge 一语仅出现在正文括号内，作者未展开其含义。"
 },
 "dd6ddd34": {
  "analysis": {
   "question_context": "提问者问在大学四年里想好好学习哲学需要做些什么。作者先否定书目推荐的必要，把问题转为「该以什么心态接触哲学」，主张需要的是「涉猎哲学」而非「学哲学」的心态，随后论证年轻人不可能真正掌握哲学，并大段回应评论区中以「民哲」等标签否定其观点的所谓科班生。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "书目不必反复推荐，真正要准备的是涉猎哲学而非学哲学的心态。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006", "P007", "P008"], "summary": "两种心态的差别与后果，并以牛吃草、反刍消化为喻。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P009", "P010", "P011"], "summary": "中国人学哲学最大的害处：对经典与主流的下意识崇拜，政治正确内化到元问题层面。", "role": "claim"},
    {"unit_id": "U004", "paragraph_refs": ["P012", "P013", "P014", "P015"], "summary": "作者声明不批评这种偏狭的对错，称其为历史命运；无人能例外，西方学界亦五十步笑一百步。", "role": "qualification"},
    {"unit_id": "U005", "paragraph_refs": ["P016", "P017", "P018", "P019"], "summary": "个人只掌握极窄摘要即应届博士的真实水平；学派问题使元命题不被讨论，流派之多超出人生容量。", "role": "reason"},
    {"unit_id": "U006", "paragraph_refs": ["P020", "P021", "P022", "P023", "P024", "P025", "P026"], "summary": "以新生小鸡认母鸡为真理之母作喻，用时间与信息量的算术限制论证年轻人不可能真懂。", "role": "reason"},
    {"unit_id": "U007", "paragraph_refs": ["P027", "P028", "P029", "P030", "P031"], "summary": "哲学不是年轻人能宣称掌握的学问；自以为懂了就是在没入门处安营扎寨。", "role": "claim"},
    {"unit_id": "U008", "paragraph_refs": ["P032", "P033", "P034", "P035", "P036", "P037", "P038", "P039"], "summary": "以死亡、贫穷、绝望等切身经验质问凭阅读断言对错者；声明未用个人经验或学术资格压人。", "role": "rebuttal"},
    {"unit_id": "U009", "paragraph_refs": ["P040", "P041", "P042", "P043", "P044", "P045", "P046", "P047", "P048", "P049", "P050", "P051"], "summary": "解释少年成名、足不出户的哲学家之谜：握笔者只是代言人，译解者是听者而非邮差。", "role": "rebuttal"},
    {"unit_id": "U010", "paragraph_refs": ["P052", "P053", "P054", "P055", "P056", "P057", "P058"], "summary": "不推荐大学生业余学哲学；专业书籍只讲哲学史与研究工具，哲学本质是思想的艺术。", "role": "claim"},
    {"unit_id": "U011", "paragraph_refs": ["P059", "P060", "P061", "P062"], "summary": "哲学的标准不在对不对而在够不够美；人类只有对美的直觉。", "role": "claim"},
    {"unit_id": "U012", "paragraph_refs": ["P063", "P064", "P065", "P066", "P067", "P068", "P069"], "summary": "只练技巧者画出的是行货不是艺术；哲学家须是久历人世者，靠人海沉浮形成的审美直觉。", "role": "claim"},
    {"unit_id": "U013", "paragraph_refs": ["P070", "P071", "P072"], "summary": "建议先学当马克吐温、先学自然科学与手艺、先去人海沉浮，再谈哲学。", "role": "action_advice"},
    {"unit_id": "U014", "paragraph_refs": ["P073", "P074", "P075", "P076", "P077", "P078"], "summary": "哲学是对个人政治性极强的实践与结果导向的反向摸索，判断标准在实践中的可行性，本质是审美判断。", "role": "claim"},
    {"unit_id": "U015", "paragraph_refs": ["P079", "P080", "P081", "P082", "P083", "P084", "P085", "P086", "P087", "P088"], "summary": "收束：可涉猎但不可自认科班、不可拿哲学书教训人；学哲学而无教养即为白学。", "role": "conclusion"},
    {"unit_id": "U016", "paragraph_refs": ["P089", "P090", "P091", "P092", "P093", "P094", "P095", "P096", "P097", "P098", "P099", "P100", "P101", "P102", "P103", "P104", "P105", "P106"], "summary": "回应反对者：反对本身无妨，但夹枪带棒贴民哲标签者未入门；观点只是观点，缺教养者毫无训练痕迹。", "role": "rebuttal"},
    {"unit_id": "U017", "paragraph_refs": ["P107", "P108", "P109", "P110", "P111", "P112", "P113"], "summary": "指反对者抬高被说服门槛并要求举证；读个博士不过不算文盲；以抑郁症相警。", "role": "rebuttal"},
    {"unit_id": "U018", "paragraph_refs": ["P114", "P115", "P116", "P117", "P118", "P119", "P120"], "summary": "以评论区腔调为验证，说明不建议学哲学是为保命，并称见过多人因此得抑郁症。", "role": "reason"},
    {"unit_id": "U019", "paragraph_refs": ["P121", "P122", "P123", "P124", "P125", "P126", "P127", "P128"], "summary": "收尾劝诫：涉猎可以，但年轻且未经生死者不可自以为有超人智慧；否则前路必有魔鬼。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "学哲学要准备的不是书目而是心态：涉猎哲学，而不是学哲学。", "evidence": ["E01", "E02"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "抱着涉猎自觉的人不会看完就自认懂了；学哲学的人不戴上懂一点哲学的小红花无法甘心。", "evidence": ["E03"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "涉猎者的实际收益远大于学哲学者；后者常无收益，反而在性格、社交能力、认识能力上出现明显缺陷。", "evidence": ["E04", "E05"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "哲学犹如牛吃草：吃下去的不算，反刍之后消化的才算。", "evidence": ["E06"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "中国人学哲学最大的害处是被预定的统一思想需要造成的对经典著作与主流观点的下意识崇拜，政治正确已内化到元问题层面。", "evidence": ["E07", "E08", "E09"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "作者并不是在批评这种偏狭如何不对或不好，这是历史分配给中国的不可选择的命运，不能视为阴谋诡计或学术失范。", "evidence": ["E10", "E11"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "这种偏狭已融入文化环境骨髓，老师、编者译者、评审与阅卷组都不能例外，读者也不要指望自己例外；自称自由的西方学界也五十步笑一百步。", "evidence": ["E12", "E13"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "读者只掌握极窄的、被启蒙派别鼓吹为正统主流的东西的一点摘要，这就是应届博士毕业的真实水平。", "evidence": ["E14"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "哲学存在学派问题：派内也不再谈元命题，只在第二三四级树枝上修补；真对元命题有异议，就去盖隔壁那栋楼。", "evidence": ["E15"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "学哲学最大的困难是流派太多而人生有限，只能摘要式地看一门两门的目录。", "evidence": ["E16"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "年轻人自认为搞懂了哲学，只有一种可能：像新生小鸡把第一眼看到的老母鸡加封为真理之母，有时那对象连鸡都不是而是狗。", "evidence": ["E17"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人一天只有二十四小时、到三十岁只有一万天，必然止步于此；不存在三十岁看懂哲学大彻大悟的可能，唯一区别只在于承认与否。", "evidence": ["E18", "E19", "E20"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "决定不懂的是人的天然限制、超出处理能力的信息量和根本没有的时间，是数学，不是老人家的傲慢。", "evidence": ["E21", "E22"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "哲学不是年轻人能宣称掌握甚至了解的学问；只有彻底认清这一点，才可能避开学着学着自以为懂了这一最大问题。", "evidence": ["E23", "E24"]},
    {"claim_id": "C015", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "自以为懂了就意味着在连门都没入的地方安营扎寨准备颐养天年。", "evidence": ["E25"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "本文没有拿任何个人的偶然经验或学术资格来压人，必然性由像砖头一样列出的论证逻辑支持。", "evidence": ["E26", "E27"]},
    {"claim_id": "C017", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "所谓少年成名、足不出户的哲学家：按经历不是少年，按交游不是足不出户，其少年时被传颂的见解他们自己当时也不懂；握笔者只是代言人，译解者是听到并咀嚼这些话的人。", "evidence": ["E28", "E29"]},
    {"claim_id": "C018", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不推荐大学生业余学哲学，因为哲学是学不好的；专业书籍只讲哲学史与研究工具，而哲学的本质是思想的艺术。", "evidence": ["E30", "E31", "E32"]},
    {"claim_id": "C019", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "哲学不能依赖与前辈无矛盾加正确使用工具来保证结论的价值和意义；其真正标准不在对不对，而在够不够美。", "evidence": ["E33", "E34"]},
    {"claim_id": "C020", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "人类根本不知道什么是真和善，只有对美的直觉，并事实上被越美越真、越美越善的逻辑绝对统治。", "evidence": ["E35"]},
    {"claim_id": "C021", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "哲学家必须是久历人世、心龄三千年、见过生老病死盛衰兴亡的老人；检验思想生命力靠人海沉浮形成的理性直觉与审美能力，否则易成满嘴名词的废人甚至混蛋。", "evidence": ["E36", "E37", "E38"]},
    {"claim_id": "C022", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "学哲学若为经世致用，先学当马克吐温比学当康德黑格尔好；应把哲学著作放在次要位置，先学自然科学、学手艺、去人海沉浮，阅尽千山后再谈哲学。", "evidence": ["E39", "E40"]},
    {"claim_id": "C023", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "哲学涉及基本方法论，是对个人而言政治性极强的实践，也是结果导向的反向摸索；理论有无生命力由立场能否行得通决定，答案在实践里而非哲学书中。", "evidence": ["E41", "E42", "E43"]},
    {"claim_id": "C024", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "不是说哲学著作不可读或不宜涉猎，只是要绝掉哲学可以学、学了哲学就会哲学的念头。", "evidence": ["E44"]},
    {"claim_id": "C025", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "学工程学、数学、物理可以没有教养，但学哲学的人没有教养就是白学了。", "evidence": ["E45"]},
    {"claim_id": "C026", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "对该观点表示忧虑和反对并无不好，但因此夹枪带棒、含沙射影地贴标签的所谓科班生根本没有真正迈进这个门。", "evidence": ["E46"]},
    {"claim_id": "C027", "claim_type": "opponent_view", "attribution": "opponent", "modality": "asserted", "statement": "被作者反驳的说法：仅仅因为不喜欢该观点，就断言这必定是不懂哲学的人胡说、没有任何别的可能性。", "evidence": ["E47"]},
    {"claim_id": "C028", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "缺乏这种敏感性只可能是因为哲学总被用作解释自己的权威性、让人闭嘴屈服，而从来没有真的拿来指导自己的生活。", "evidence": ["E49"]},
    {"claim_id": "C029", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "满口名词与妙辩无碍的经文不是懂哲学的证明，反而会成为根本不懂哲学的反证。", "evidence": ["E50"]},
    {"claim_id": "C030", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "反对者把被说服的门槛抬得很高，要求对方既给出不同意见又承担提供证据的义务；这不是有前途的习惯，被说服受益的是他们自己。", "evidence": ["E51", "E60"]},
    {"claim_id": "C031", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "只看评论区部分人的腔调就已验证大学生还是不要学哲学为好；不建议学哲学是为了保命，作者几十年见过因此得抑郁症救不回来的人已数不过来。", "evidence": ["E52", "E53", "E54"]},
    {"claim_id": "C032", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者自称不是以哲学前辈的老资格吓唬人，而是作为见过累累白骨的归人叫年轻人知道死活。", "evidence": ["E56"]},
    {"claim_id": "C033", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "自认为学哲学却没有因此获得教养、对可能性的敬畏、对不认可事物的本能谨慎，就直接预示着在走邪路，前路必有拿着你名字的魔鬼。", "evidence": ["E57", "E58", "E59"]},
    {"claim_id": "C034", "claim_type": "quoted_or_cited", "attribution": "opponent", "modality": "asserted", "statement": "作者转述反对者使用的标签措辞：民哲、胡说八道、误人子弟。", "evidence": ["E48"]},
    {"claim_id": "C035", "claim_type": "open_question", "attribution": "author", "modality": "questioned", "statement": "作者以连串质问逼问读者：你死过没、见人死过没，知道什么是贫穷、绝望、背叛、冤屈、公平、仁慈吗，没尝过没见过就敢凭阅读断言对错吗。", "evidence": ["E61"]}
   ],
   "argument_steps": [
    "先否定书目推荐的意义，改为谈接触哲学的心态（P001-P002）。",
    "区分涉猎哲学与学哲学：前者不自认懂，后者需要自我认证；并断言前者收益更大、后者常有性格与能力缺陷（P004-P006）。",
    "以牛吃草、反刍消化为喻，说明读下去不算、消化才算（P007-P008）。",
    "指出中国语境下学哲学的最大害处是对经典与主流的无意识崇拜，政治正确已深入教育体系并内化到元问题（P009-P011）。",
    "让步与自限：作者不评判这种偏狭的对错，称其为历史命运而非阴谋；同时说无人能例外、西方学界亦然（P012-P015）。",
    "以应届博士的真实水平与学派修枝作喻，说明个人只能得到极窄摘要（P016-P019）。",
    "以新生小鸡认母鸡为真理之母作喻（P020）。",
    "以二十四小时、三十岁一万天、信息量超载作为算术论据，推出年轻人不可能真懂（P021-P026）。",
    "给出结论：哲学不是年轻人能宣称掌握的学问；自以为懂了等于在没入门处安营扎寨（P027-P031）。",
    "以死亡、贫穷、绝望等经验反问凭阅读断言对错者，并声明未用个人经验与学术资格压人（P032-P039）。",
    "解释少年成名之谜：经历上不是少年、交游上不是足不出户、其见解当时自己也不懂；握笔者只是代言人（P040-P051）。",
    "转为不建议业余学哲学，并说明哲学书籍只提供历史与工具，本质是思想的艺术（P052-P058）。",
    "提出标准转移：哲学的标准不是对不对，而是够不够美；人类只有对美的直觉（P059-P062）。",
    "以行货与艺术之别说明只练技巧者不能成为哲学家；哲学家须是久历人世者（P063-P069）。",
    "给出行动建议：先学当马克吐温，先学自然科学与手艺、先去人海沉浮（P070-P072）。",
    "把哲学界定为对个人政治性极强的实践与结果导向的反向摸索，判断标准在实践中（P073-P078）。",
    "收束：可涉猎但不可自认科班；学哲学而无教养即为白学（P079-P088）。",
    "回应反对者：反对无妨，但贴标签者未入门；观点只是观点，无教养者毫无训练痕迹（P089-P106）。",
    "进一步反驳：对方抬高被说服门槛并要求举证；读个博士不过不算文盲；并警告抑郁症风险（P107-P113）。",
    "以评论区腔调为验证，说明不建议学哲学是为保命（P114-P120）。",
    "最后劝诫：涉猎可以，年轻且未经生死者不可自以为有超人智慧，否则前路必有魔鬼（P121-P128）。"
   ],
   "concept_usage": [
    {"term": "涉猎哲学／学哲学", "meaning": "两种接触哲学的心态：前者只作涉猎、不自我认证；后者以掌握为目标并要求自我认可", "evidence": "P002/P003/P004", "ambiguity": "作者未给出两者的明确分界，仅以是否自认懂区分"},
    {"term": "经典著作、主流观点", "meaning": "中国哲学教育中被下意识崇拜的对象", "evidence": "P009", "ambiguity": "未列举具体书目或观点"},
    {"term": "元问题／元命题", "meaning": "被内化到不再被意识、也不再被谈论的基础问题", "evidence": "P010/P017", "ambiguity": "未举例说明哪些问题属于元问题"},
    {"term": "五十步笑一百步", "meaning": "用于说明西方学界并不比中国学界更自由", "evidence": "P014/P031", "ambiguity": "属修辞性判断，未给出比较标准"},
    {"term": "教养", "meaning": "因学哲学而获得的、用于指导自己生活的基本本能与谨慎", "evidence": "P101/P099", "ambiguity": "未给出可操作定义，仅以生活应用为判据"},
    {"term": "思想的艺术／够不够美", "meaning": "作者给哲学设定的本质与评判标准，与对不对相对", "evidence": "P056/P061", "ambiguity": "美的标准由谁判定未说明"},
    {"term": "反向摸索", "meaning": "以什么样的立场能行得通来确定有生命力的理论", "evidence": "P075/P076", "ambiguity": "行得通的判据与实践范围未界定"},
    {"term": "民哲", "meaning": "反对者用来否定作者观点的标签", "evidence": "P090/P094", "ambiguity": "作者未给出该标签的判定标准，只质疑其普世适用性"},
    {"term": "open mind", "meaning": "作者用以指称对冒犯性观点的最低接受能力", "evidence": "P105", "ambiguity": "英文夹用，未定义其水平标准"}
   ],
   "examples_and_targets": [
    "牛吃草与反刍：作者的核心比喻（P007-P008）。",
    "新生小鸡把第一眼看到的老母鸡加封为真理之母：比喻年轻人自认懂哲学（P020）。",
    "盖楼与树枝修剪：比喻学派在第二三四级问题上修补、不碰元命题（P017）。",
    "康德、黑格尔、马克吐温：作者以马克吐温为应学的榜样、以康德黑格尔为不宜先学的对象（P070）。",
    "达芬奇与蒙娜丽莎：说明临摹技巧不等于成为艺术家（P080）。",
    "百度百科五百字、高中老师读课本四百字：比喻对佛教、基督教、共产主义的浅层自认理解（P031）。",
    "工程学、数学、物理、管理学、心理学、财务、法学、神学：作为教养要求的对比例证（P085-P087）。",
    "拳经与挥拳：比喻背熟名词而缺乏实际能力（P104）。",
    "评论区与科班生：作者的反驳对象，其标签为民哲、胡说八道、误人子弟（P090、P114）。",
    "抑郁症与见过累累白骨：作者用以警告后果的经验性说法（P113、P119、P123），属作者自述见闻，无法由本文核验。"
   ],
   "conditions": [
    "限定：观点只在大学四年、业余涉猎的语境下提出，作者称不推荐的是大学生业余学哲学（P052）。",
    "条件：只要年纪尚轻、没有经历过生死沉浮，就不可自以为获得超人智慧（P122）。",
    "条件：哲学著作不可读、不宜涉猎的说法被作者明确否认，只否定学了就会哲学（P079）。",
    "让步条件：到这里来表示忧虑和反对，作者不觉得有什么不好（P089）。",
    "前提：人一天只有二十四小时、到三十岁只有一万天，故必然止步（P021）。",
    "前提：决定不懂的是天然限制、信息量与时间，作者称之为数学（P025-P026）。",
    "条件：判断理论的标准被限定为立场能否行得通，而答案只在实践里（P076-P077）。",
    "对象条件：劝诫对象为年轻学生与自称热爱哲学的科班生（P083、P090）。"
   ],
   "rhetoric_and_tone": "训诫与激将并用，第二人称你／你们直接施压；大量反问与质问（P033、P044、P115、P117）；粗俗詈语与夸张（你特么的就完了、你知道个屁、废人甚至混蛋、傻x式的贬抑）；以比喻链贯穿（牛吃草、小鸡认母鸡、盖楼、行货与艺术、拳经）；以数学、逻辑必然等词强化论断；末尾用魔鬼、白骨、地狱等意象与勿谓言之不预收束；全文分点编号仅在少年成名三问处出现（P041-P043）。",
   "unresolved_questions": [
    "作者称人类只有对美的直觉、并主张够不够美是哲学标准，但未给出判定美的标准或例证。",
    "教养被作为核心判据，但除生活应用外未给出可操作定义。",
    "评论区与科班生的具体言论未在正文引用，只有标签措辞，作者转述是否完整无法由本文核验。",
    "作者称见过多人因学哲学得抑郁症，属自述见闻，需外部核查。",
    "元问题的具体所指未举例，读者难以判断哪些问题属于被跳过的层级。",
    "少年成名三问（P041-P043）未指名任何具体哲学家，所指对象不明。",
    "open mind 一语为英文夹用，其水平标准未定义。",
    "brief 为140字截断文本（末尾为一种我是在涉猎哲学，而不），只能作导航，不能支持任何主张。",
    "本篇无图片节点，图片维度核验不适用；全文128段与提问均已阅读。"
   ],
   "evidence": [
    {"key": "E01", "paragraph_id": "P002", "quote": "真正要准备的是接触这些东西的心态", "relation": "supports"},
    {"key": "E02", "paragraph_id": "P003", "quote": "一种“我是在涉猎哲学”，而不是“学哲学”的心态。", "relation": "supports"},
    {"key": "E03", "paragraph_id": "P004", "quote": "抱着涉猎自觉的人，不会看完那些东西就觉得自己懂了", "relation": "supports"},
    {"key": "E04", "paragraph_id": "P005", "quote": "前者从这番涉猎里所得到的实际收益要远大于抱着“学哲学”心态的人。", "relation": "supports"},
    {"key": "E05", "paragraph_id": "P006", "quote": "反而会在性格、社交能力、认识能力上出现相当明显的缺陷。", "relation": "supports"},
    {"key": "E06", "paragraph_id": "P008", "quote": "你吃下去的不算，反刍之后消化的才算。", "relation": "supports"},
    {"key": "E07", "paragraph_id": "P009", "quote": "造成的对“经典著作”“主流观点”的下意识崇拜。", "relation": "supports"},
    {"key": "E08", "paragraph_id": "P010", "quote": "内化到了不再被意识到", "relation": "supports"},
    {"key": "E09", "paragraph_id": "P011", "quote": "开始只谈论二楼以上的问题。", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P012", "quote": "我并不是在批评说这个如何不对或者不好", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P012", "quote": "这是历史分配给中国的不可选择的命运", "relation": "qualifies"},
    {"key": "E12", "paragraph_id": "P013", "quote": "你不要指望你可以例外。", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P014", "quote": "自认为“自由”的西方学界也只不过五十步笑一百步罢了。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P016", "quote": "这才是你读到应届博士毕业的真实水平。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P017", "quote": "你真的直接对元命题有异议，那你去盖隔壁那栋楼。", "relation": "supports"},
    {"key": "E16", "paragraph_id": "P018", "quote": "你只能摘要式的看那么一门两门的目录。", "relation": "supports"},
    {"key": "E17", "paragraph_id": "P020", "quote": "把第一个自己看到的老母鸡加封为真理之母", "relation": "supports"},
    {"key": "E18", "paragraph_id": "P021", "quote": "到三十岁只有一万天，你必然只能止步于此", "relation": "supports"},
    {"key": "E19", "paragraph_id": "P022", "quote": "不存在你三十岁就看懂了哲学的世界然后大彻大悟的任何可能性。", "relation": "supports"},
    {"key": "E20", "paragraph_id": "P023", "quote": "唯一的区别，只在于你承认和不承认。", "relation": "supports"},
    {"key": "E21", "paragraph_id": "P025", "quote": "是超出你处理能力的信息量和你根本没有的时间。", "relation": "supports"},
    {"key": "E22", "paragraph_id": "P026", "quote": "是数学，不是什么“老人家的傲慢”。", "relation": "supports"},
    {"key": "E23", "paragraph_id": "P027", "quote": "哲学不是年轻人能宣称掌握甚至了解的学问。", "relation": "supports"},
    {"key": "E24", "paragraph_id": "P028", "quote": "就是学着学着“自以为懂了”。", "relation": "supports"},
    {"key": "E25", "paragraph_id": "P030", "quote": "那意味着你在一个连门都没入的鬼地方安营扎寨准备颐养天年了。", "relation": "supports"},
    {"key": "E26", "paragraph_id": "P038", "quote": "到这里没有拿任何个人的偶然经验或者什么“学术资格”来压人。", "relation": "supports"},
    {"key": "E27", "paragraph_id": "P039", "quote": "论证逻辑简单得像砖头一样列出来给你们看了。", "relation": "supports"},
    {"key": "E28", "paragraph_id": "P043", "quote": "他们自己当时也不懂。", "relation": "supports"},
    {"key": "E29", "paragraph_id": "P049", "quote": "是这些人真正把这口信译解出来，成为一个新的事物。", "relation": "supports"},
    {"key": "E30", "paragraph_id": "P052", "quote": "实际上，我不推荐大学生业余“学哲学”。", "relation": "supports"},
    {"key": "E31", "paragraph_id": "P053", "quote": "因为“哲学”这个东西是“学”不好的。", "relation": "supports"},
    {"key": "E32", "paragraph_id": "P056", "quote": "但是哲学的本质是思想的艺术。", "relation": "supports"},
    {"key": "E33", "paragraph_id": "P057", "quote": "哲学并不能依赖“和前辈的东西没矛盾 + 正确使用工具”来保证其结论的价值和意义。", "relation": "supports"},
    {"key": "E34", "paragraph_id": "P061", "quote": "它真正的标准是够不够美。", "relation": "supports"},
    {"key": "E35", "paragraph_id": "P062", "quote": "人类根本不知道什么是真和善，人类只有对美的直觉。", "relation": "supports"},
    {"key": "E36", "paragraph_id": "P066", "quote": "哲学家必须是久历人世，心龄三千年，见过生老病死、盛衰兴亡的“老人”。", "relation": "supports"},
    {"key": "E37", "paragraph_id": "P067", "quote": "而是从那些人海沉浮中形成的强烈的理性直觉，那种对思想的审美能力。", "relation": "supports"},
    {"key": "E38", "paragraph_id": "P068", "quote": "极其容易搞成一个满嘴哲学名词和圣贤语录的废人——甚至——一个混蛋。", "relation": "supports"},
    {"key": "E39", "paragraph_id": "P070", "quote": "最好不要学当康德黑格尔，倒是应该先去学当马克吐温。", "relation": "supports"},
    {"key": "E40", "paragraph_id": "P071", "quote": "先学好自然科学，学好手艺，先去人海沉浮。", "relation": "supports"},
    {"key": "E41", "paragraph_id": "P073", "quote": "其实是一项对个人而言政治性极强的实践。", "relation": "supports"},
    {"key": "E42", "paragraph_id": "P075", "quote": "它事实上是一门结果导向的反向摸索。", "relation": "supports"},
    {"key": "E43", "paragraph_id": "P077", "quote": "而“行不行得通”的答案，并不在哲学书里，而是在实践里面。", "relation": "supports"},
    {"key": "E44", "paragraph_id": "P079", "quote": "只是要绝掉“哲学可以学，学了哲学就会哲学”的念头。", "relation": "supports"},
    {"key": "E45", "paragraph_id": "P086", "quote": "但学哲学的人没有教养，就是白学了。", "relation": "supports"},
    {"key": "E46", "paragraph_id": "P090", "quote": "根本就没有真正的迈进这个门。", "relation": "supports"},
    {"key": "E47", "paragraph_id": "P093", "quote": "就断言“这必定是不懂哲学的人胡说，没有任何别的可能性”", "relation": "context"},
    {"key": "E48", "paragraph_id": "P090", "quote": "开始“民哲”“胡说八道”“误人子弟”", "relation": "context"},
    {"key": "E49", "paragraph_id": "P099", "quote": "而从来没有真的拿来指导你自己的生活。", "relation": "supports"},
    {"key": "E50", "paragraph_id": "P103", "quote": "反而会成为你“根本不懂哲学”的反证！", "relation": "supports"},
    {"key": "E51", "paragraph_id": "P107", "quote": "你们把自己被说服的门槛抬得很高。", "relation": "supports"},
    {"key": "E52", "paragraph_id": "P114", "quote": "就已经完美的验证了“大学生还是不要学哲学为好”。", "relation": "supports"},
    {"key": "E53", "paragraph_id": "P118", "quote": "就是为了保你们一条命。", "relation": "supports"},
    {"key": "E54", "paragraph_id": "P119", "quote": "得抑郁症救都救不回来的已经两只手都数不过来了。", "relation": "supports"},
    {"key": "E55", "paragraph_id": "P122", "quote": "拜托你不要自以为已经获得了傲视群氓的“超人智慧”。", "relation": "supports"},
    {"key": "E56", "paragraph_id": "P123", "quote": "我这是作为一个见过累累白骨的归人叫你们知道死活。", "relation": "supports"},
    {"key": "E57", "paragraph_id": "P126", "quote": "就直接预示着你在走邪路。", "relation": "supports"},
    {"key": "E58", "paragraph_id": "P127", "quote": "前路必有拿着你名字的魔鬼。", "relation": "supports"},
    {"key": "E59", "paragraph_id": "P128", "quote": "勿谓言之不预。", "relation": "supports"},
    {"key": "E60", "paragraph_id": "P109", "quote": "被说服受益的人是你们，而不是我。", "relation": "supports"},
    {"key": "E61", "paragraph_id": "P033", "quote": "你就敢凭阅读断言什么是对的，什么是错的？", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["哲学教育与学术体制", "认识论与方法论", "青年成长与教育", "学术批评"],
   "issue_candidates": ["大学生如何接触哲学", "哲学能否被学会", "学术权威与元问题", "民哲与科班之争", "教养与学术训练", "经验与判断力", "学术评价标准"],
   "text_function_candidates": ["答疑", "论辩与批驳", "训诫劝勉", "经验总结"],
   "object_candidates": ["中国哲学教育体系", "西方学界", "康德", "黑格尔", "马克吐温", "达芬奇", "百度百科", "评论区科班生"],
   "working_keywords": ["涉猎哲学", "学哲学", "牛吃草", "反刍", "元问题", "元命题", "学派", "真理之母", "思想的艺术", "够不够美", "反向摸索", "教养", "民哲", "open mind", "毫无训练痕迹", "勿谓言之不预"]
  },
  "notes": "本篇为长篇答帖，正文含大量针对评论区反对者的回应（P089 起），反对者言论未原文引用，只有标签措辞，已按 opponent_view 与 quoted_or_cited 分开登记。全文128段与提问均已阅读，无图片节点，图片核验不适用。brief 为140字截断文本，仅作导航。"
 },
 "e6b593e6": {
  "analysis": {
   "question_context": "提问者以张桂梅拒绝一位全职太太（女高学生）捐款、当事人回应「张老师话丑理正，她是从我们女高学生立场说的」为背景发问。事件与当事人引语均属提问字段提供的信息，不归给作者。作者正文未复述事件，而是先给全职太太设定门槛条件，再据此判定张校长的看法对绝大多数中国女性成立，并劝诫未来的丈夫与父亲。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "界定可接受的全职太太：不是保姆／清洁工替代物，不能脱离事业，须有接触社会、专业能力、专业声誉与人脉的平台。", "role": "definition"},
    {"unit_id": "U002", "paragraph_refs": ["P004"], "summary": "家庭主妇应是保姆与小时工的管理者而非自己干家务；无能力雇佣保姆的家庭不应拥有全职主妇；应因富有而非因贫穷。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P005", "P006", "P007"], "summary": "按门槛条件张校长的看法对绝大多数中国女性成立；能符合条件的家庭凤毛麟角，但不可绝对否定、也不可高估比例。", "role": "conclusion"},
    {"unit_id": "U004", "paragraph_refs": ["P008", "P009"], "summary": "告诫未来的丈夫与父亲：家庭中最重要的是配偶而非子女，不能保证对方底线就不要强行生娃或让对方做家庭主妇。", "role": "action_advice"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "全职太太可以做，但不是那种保姆／清洁工综合替代物。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "全职太太不能脱离事业，只是不必是朝九晚五的坐班事业，例如文学创作、艺术创作、文学翻译、课题研究、财务管理、策划咨询、组织社会活动等。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "全职太太要和社会接触、参与社会价值的构建，要有磨练专业能力、建立专业声誉与人脉网络的必要平台。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "做家庭主妇也是作为保姆与小时工人的管理者，而不是自己干家务活。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "如果这个家庭没有能力支持保姆和小时工，那么它不应该拥有全职家庭主妇，那本身就太勉强了。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "做家庭主妇应该是因为富有，而不能是因为贫穷。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "按照作者列出的门槛条件，张校长的看法对绝大多数中国女性都是成立的。", "evidence": ["E7"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "能让你安心选择家庭主妇并尊重支持你追求个人事业的家庭堪称凤毛麟角，概率小到不能做严肃的指望。", "evidence": ["E8"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "这样的家庭肯定是有，所以不能绝对地说家庭主妇不能做，但绝对不要高估这个比例。", "evidence": ["E9"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "家庭中最重要的不是将来的子女，而是配偶——那个因为相信你而把命交给你、与你没有血缘关系、不欠你任何东西的人。", "evidence": ["E10"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "如果不能保证对方的生活质量和人生价值的必要底线，就不要强行按传统、惯例或大流去生娃、强行让对方做家庭主妇。", "evidence": ["E11"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "否则家庭主妇本身就会直接离你而去，强行也没用。", "evidence": ["E12"]},
    {"claim_id": "C013", "claim_type": "quoted_or_cited", "attribution": "cited_source", "modality": "asserted", "statement": "提问者转述被拒捐款的全职太太的回应：张老师话丑理正，她是从我们女高学生立场说的。该引语只在提问字段，正文未提及。", "evidence": []}
   ],
   "argument_steps": [
    "先给出可接受形态：全职太太可以做，但不能是保姆／清洁工综合替代物（P001）。",
    "补充事业条件并举出可算事业的例子（P002）。",
    "补充社会接触与专业平台条件（P003）。",
    "界定家务分工：主妇是保姆与小时工的管理者，并给出经济门槛（P004）。",
    "据此把张校长的看法适用于绝大多数中国女性（P005）。",
    "以凤毛麟角的比例判断限定该结论（P006）。",
    "再作双向限定：不能绝对否定，也不能高估比例（P007）。",
    "转向劝诫未来的丈夫与父亲：配偶优先于子女，保不住底线就不要强行安排（P008）。",
    "以家庭主妇会离你而去作结（P009）。"
   ],
   "concept_usage": [
    {"term": "全职太太／家庭主妇", "meaning": "以家庭为主要场域但仍须保有事业与专业能力的角色", "evidence": "P001/P002/P004", "ambiguity": "两词在文中交替使用，是否完全同义未说明"},
    {"term": "事业", "meaning": "不必是朝九晚五的坐班工作，作者以文学创作、翻译、课题研究、财务管理、策划咨询、组织社会活动等举例", "evidence": "P002", "ambiguity": "边界仅由举例给出，未提供判准"},
    {"term": "保姆/清洁工综合替代物", "meaning": "作者明确否定的全职太太形态，即自己承担全部家务", "evidence": "P001", "ambiguity": "属作者自造的描述性说法"},
    {"term": "门槛条件", "meaning": "作者据以判定张校长看法适用性的条件集合", "evidence": "P005", "ambiguity": "作者称这些门槛条件，但未逐条编号列出"},
    {"term": "必要底线", "meaning": "配偶的生活质量与人生价值的最低保障", "evidence": "P008", "ambiguity": "未说明底线的具体内容"}
   ],
   "examples_and_targets": [
    "张桂梅（文中称张校长）：出现在提问背景中，作者在P005有条件地认同其看法，正文未描述事件经过。",
    "被拒捐款的全职太太及其回应：只出现在提问字段，正文未提及。",
    "严肃的文学创作、艺术创作、文学翻译、社会学科的课题研究、财务管理、策划咨询、组织社会活动：作者列举的可算事业的活动（P002）。",
    "保姆、小时工：作者设定的家庭主妇管理对象与家庭经济门槛的标志（P004）。",
    "小男生们：作者的劝诫对象（P008）。",
    "凤毛麟角：对符合条件的家庭比例的修辞（P006）。"
   ],
   "conditions": [
    "全部结论以作者所列门槛条件为前提，但条件未逐条列出（P005）。",
    "条件句：家庭无能力支持保姆和小时工，则不应拥有全职家庭主妇（P004）。",
    "因果限定：做家庭主妇应因富有，不能因贫穷（P004）。",
    "比例限定：对绝大多数中国女性成立（P005）；符合条件的家庭凤毛麟角、概率小到不能做严肃的指望（P006）；不能绝对否定但不要高估（P007）。",
    "底线条件：不能保证配偶生活质量与人生价值的必要底线时，不要强行生娃或强行让对方做家庭主妇（P008）。"
   ],
   "rhetoric_and_tone": "条件式界定加告诫口吻；以引号标示保姆/清洁工综合替代物、传统、惯例、大流、家庭主妇等词；用凤毛麟角、小男生们等口语化措辞；反复用强行一词加引号施压；末句以家庭主妇会离你而去的拟人说法收束。",
   "unresolved_questions": [
    "张桂梅拒捐与当事人回应的细节只见于提问字段，正文未复述，事件本身需外部核查。",
    "作者称按门槛条件张校长看法对绝大多数中国女性成立，但门槛条件未逐条列出，绝大多数也无数化依据。",
    "全职太太与家庭主妇两词混用，是否同义未说明。",
    "事业的范围仅以举例给出，缺少判准，无法判断其他活动是否算事业。",
    "生活质量和人生价值的必要底线未给出具体内容。",
    "brief 为140字截断文本（末尾为建），只能作导航，不能支持任何主张。",
    "本篇无图片节点，图片维度核验不适用；全文9段与提问均已阅读。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "全职太太可以做，但是不是那种“保姆/清洁工综合替代物”。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "全职太太不能脱离事业，只是不必是朝九晚五的坐班的事业", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "要和社会接触、参与社会价值的构建，要有磨练自己的某种专业能力、建立专业声誉以及建立自己的人脉网络的必要平台。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "但也是作为一个保姆、小时工人的管理者，而不是自己干家务活。", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P004", "quote": "如果这个家庭没有能力支持保姆和小时工，那么它是不应该拥有全职家庭主妇的", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P004", "quote": "做家庭主妇，应该是因为富有，而不能是因为贫穷。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P005", "quote": "按照这些门槛条件，张校长的看法对绝大多数中国女性都是成立的。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P006", "quote": "堪称凤毛麟角，概率小到不能做严肃的指望。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P007", "quote": "不能绝对的说家庭主妇不能做，但是绝对不要高估这个比例。", "relation": "qualifies"},
    {"key": "E10", "paragraph_id": "P008", "quote": "事实上家庭中最重要的不是将来的子女，而是你的配偶", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P008", "quote": "请不要强行按“传统”和“惯例”或者“大流”的指引去强行生娃、强行让对方做“家庭主妇”。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P009", "quote": "否则“家庭主妇”本身就会直接离你而去", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["性别与家庭", "社会议题评论", "职业与劳动"],
   "issue_candidates": ["全职太太的正当性", "女性经济独立", "家务劳动与雇佣劳动", "生育与婚姻选择", "寒门女学生出路"],
   "text_function_candidates": ["时评", "答疑", "告诫"],
   "object_candidates": ["张桂梅", "全职太太", "家庭主妇", "保姆", "小时工", "中国女性", "小男生们"],
   "working_keywords": ["全职太太", "家庭主妇", "保姆/清洁工综合替代物", "事业", "专业声誉", "人脉网络", "门槛条件", "凤毛麟角", "必要底线"]
  },
  "notes": "事件与当事人回应只见于提问字段（question 不在机械生成的段落结构中），相关内容按提问者／引述来源归属，未算作作者主张；本篇无图片节点，图片核验不适用。brief 为140字截断文本，仅作导航。"
 },
 "56e3a9cc": {
  "analysis": {
   "question_context": "提问者自述感觉画得不错有点飘，求人把自己骂醒。提问者的自我评价只在提问字段，不归给作者。作者未直接评价提问者或其作品，而是从客户视角说明画工一般不是被关注的主要因素、真正致命的是答不出为什么这样画，并把能否回答作为是否算设计的判据。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001"], "summary": "客户一般不会质疑画工，因为没有收藏需求；不必要抠画工者或头脑不清醒，或在栽培你先交货后自改。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P002", "P003"], "summary": "真正被抠的是画错了（比例、光感、风向、透视、接地），并说明常识直觉与改稿成本的关系。", "role": "reason"},
    {"unit_id": "U003", "paragraph_refs": ["P004", "P005", "P006", "P007", "P008", "P009", "P010", "P011", "P012", "P013", "P014"], "summary": "以连续质问列举客户会追问的选择项，指出答不出来才是真正致命的东西。", "role": "rebuttal"},
    {"unit_id": "U004", "paragraph_refs": ["P015", "P016"], "summary": "排除以我觉得这样更好看作答，并断言答不出来就不叫设计。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "客户一般不太会质疑画工不行。", "evidence": ["E1"]},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "产品并不是客户自己要买来挂到家里去的收藏品，所以根本没有多大必要去抠画工。", "evidence": ["E2"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "不必要去抠画工的人，要么属于自己脑子不太清醒，要么是在栽培你；栽培者一般会要你先交货，回头自己拿自己的时间改进。", "evidence": ["E3"]},
    {"claim_id": "C004", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正被抠的问题不是画工，而是干脆画错了，例如两条腿不一样长、光感互相矛盾、布料弄出两种风向、透视画歪、脚没沾地。", "evidence": ["E4"]},
    {"claim_id": "C005", "claim_type": "author_explicit", "attribution": "author", "modality": "hypothetical", "statement": "幸亏现在什么角色都会飞，否则把一群人都站在一个平面上这一条就能难死一片画师。", "evidence": ["E5"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "只要不犯没受过训练的凡人仅凭日常观察经验就能直觉到的明显错误，画工就不是被关注的主要因素。", "evidence": ["E6"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "不要轻忽人类的常识直觉：很多画师自己觉察不出来的问题，观众无法用语言明确表达，却能明确感到缺陷和不适。", "evidence": ["E7"]},
    {"claim_id": "C008", "claim_type": "author_explicit", "attribution": "author", "modality": "qualified", "statement": "业界这个标准不算严格，一些小问题直接放过；修改观众看不出来也直觉不到的毛病属于无效的成本投入。", "evidence": ["E8"]},
    {"claim_id": "C009", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "真正致命的问题，是客户会问你为什么要画成这样。", "evidence": ["E9"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "以我觉得这样更好看作答是绝对不及格的。", "evidence": ["E10"]},
    {"claim_id": "C011", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "回答不出来这些问题才是真正致命的东西；回答不出来就根本不叫设计。", "evidence": ["E11", "E12"]},
    {"claim_id": "C012", "claim_type": "quoted_or_cited", "attribution": "questioner", "modality": "asserted", "statement": "提问者自述感觉自己画得不错、有点飘，求人把自己骂醒。该自我评价只在提问字段，正文未回应。", "evidence": []}
   ],
   "argument_steps": [
    "先给出经验判断：客户一般不会质疑画工（P001）。",
    "给出理由：作品不是客户自己收藏的东西，故无必要抠画工（P001）。",
    "区分两类苛求者：头脑不清醒者与栽培者，后者要你先交货（P001）。",
    "把焦点从画工移到画错了，并列举比例、光感、风向、透视、接地等错误（P002）。",
    "以角色都会飞作调侃，说明站在同一平面之难（P002）。",
    "给出条件式结论：不犯凡人凭常识可直觉的错误，画工就不是主要因素（P003）。",
    "补一层限定：观众虽不能言说，却能直觉到缺陷，故不可轻忽常识（P003）。",
    "给出成本理由：改观众看不出的毛病是无效投入（P003）。",
    "转向真正的致命点：客户会问为什么要画成这样（P004）。",
    "以排比质问列举具体选择项（P005-P013）。",
    "排除我觉得更好看的答案，并断言答不出就不叫设计（P015-P016）。"
   ],
   "concept_usage": [
    {"term": "画工", "meaning": "绘画的技术水平；作者称其一般不是客户关注的主要因素", "evidence": "P001/P003", "ambiguity": "未定义，与画错了的界限由常识直觉划定"},
    {"term": "常识直觉", "meaning": "没受过训练的凡人凭日常观察经验即可察觉错误的能力", "evidence": "P003", "ambiguity": "未给出可操作的判准，承认观众无法用语言表达"},
    {"term": "无效的成本投入", "meaning": "修改观众看不出来也直觉不到的毛病所花的功夫", "evidence": "P003", "ambiguity": "成本由谁承担、如何计量未说明"},
    {"term": "设计", "meaning": "能为每个画面选择给出理由的工作", "evidence": "P016", "ambiguity": "只有反面判据，未给出正面定义"},
    {"term": "业界这个标准", "meaning": "作者称其对小问题直接放过的行业标准", "evidence": "P003", "ambiguity": "标准的具体内容与来源未说明"}
   ],
   "examples_and_targets": [
    "客户：作者论证的出发视角与追问者（P001、P004）。",
    "两条腿不一样长、光感互相矛盾、布料弄出两种风向、透视画歪了、脚没沾地：作者列举的画错了的例子（P002）。",
    "什么角色都会飞：对行业现状的调侃性说法（P002）。",
    "萝莉装、角上要加的猫、猫尾巴竖着还是盘着、构图、主光角度、配色、表情、飘带、字体：作者列举的客户质问项（P005-P013）。",
    "提问者的自述与求骂醒：只在提问字段，正文未评价其人或其作品。"
   ],
   "conditions": [
    "判断以客户一般不太会质疑画工为限定（P001）。",
    "分类条件：不必要抠画工者要么脑子不清醒，要么在栽培你（P001）。",
    "条件：只要不犯凡人凭日常观察能直觉到的明显错误，画工就不是主要因素（P003）。",
    "因果条件：因观众不是专业画画的，修改其看不出的毛病属无效投入（P003）。",
    "转折条件：不要轻忽人类的常识直觉（P003）。",
    "例外条件：真正致命的是回答不出为什么要这样画（P004、P014、P016）。"
   ],
   "rhetoric_and_tone": "行业内部口吻的直言与调侃；以连续排比质问模拟客户追问（P005-P013）；直白詈俗式表述（干脆画错了、脑子不太清醒）；以绝对不及格作评断；用引号标示画工、画师、毛病、设计等词；结尾以根本不叫设计作断语。",
   "unresolved_questions": [
    "提问者自述有点飘并求骂醒，但正文未直接评价提问者或其作品，也未提及其画作信息。",
    "画工与画错了的界限由常识直觉给出，缺少明确判据。",
    "设计只有反面判据，未获正面定义。",
    "作者所称业界这个标准的具体内容与来源未说明，需外部核查。",
    "本篇段落结构中无图片节点，无法核验提问者是否附图；图片维度核验不适用。",
    "brief 为139字，末尾落在句末，但仍属节选，仅作导航。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "客户一般不太会质疑你“画工不行”。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P001", "quote": "根本没有多大的必要去抠你的“画工”。", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P001", "quote": "要么属于自己脑子不太清醒，要么是在栽培你", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P002", "quote": "而是干脆画错了，比如两条腿不一样长，光感互相矛盾，布料弄出两种风向，透视画歪了，脚没沾地", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P002", "quote": "不然“把一群人都站在一个平面上”这一条就能难死一片“画师”。", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P003", "quote": "只要你不犯没受过训练的凡人仅凭对日常事务观察经验就能直觉到的明显错误，坦白说画工就不是被关注的主要因素。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P003", "quote": "很多画师自己都觉察不出来的问题，观众虽然无法明确的用语言表达出来，但却可以明确的感到缺陷和不适感的存在。", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P003", "quote": "修改ta们看不出来也直觉不到的“毛病”，属于无效的成本投入。", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P004", "quote": "真正致命的问题，是你的客户会问你“为什么要画成这样？”", "relation": "supports"},
    {"key": "E10", "paragraph_id": "P015", "quote": "“我觉得这样更好看”这种答案是绝对不及格的。", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P014", "quote": "回答不出来这些问题，才是真正致命的东西。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P016", "quote": "回答不出来，那就根本不叫“设计”。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["绘画与视觉艺术", "商业美术行业", "职业经验"],
   "issue_candidates": ["客户与画师的关系", "画工与设计之别", "绘画常识性错误", "改稿成本", "创作选择的说理"],
   "text_function_candidates": ["答疑", "经验总结", "建议", "批评式提醒"],
   "object_candidates": ["客户", "画师", "观众", "业界"],
   "working_keywords": ["画工", "画错了", "常识直觉", "光感", "透视", "布料风向", "构图", "主光", "配色", "飘带", "字体", "设计"]
  },
  "notes": "本篇无图片节点，图片核验不适用；全文16段与提问均已阅读。提问者的自我评价与诉求只在question字段，未归给作者。brief 较短且属节选，仅作导航。"
 },
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
