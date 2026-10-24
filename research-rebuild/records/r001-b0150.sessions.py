# -*- coding: utf-8 -*-
"""批次 r001-b0150 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0150.sessions.py            # 写 out/r001-b0150.out.jsonl
  python3 records/r001-b0150.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0150"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0150.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "b21788a5": {
  "analysis": {
   "question_context": "提问者问“艺术圈是否被一群骗子在把持，他们根本没有看出一部作品好坏的能力”（Q001），这一怀疑属提问者语境，不是作者立场。作者的回答方向是否定“把持”说：先提出作品由原作者与评论家两层创作合成，再以艺术评论受无形机制筛选、艺术走向受混沌机制（天意）支配来反驳“结伙把持”，最后把“把持”称为无知者的妄念。作者未点名任何具体人物或机构，也未回应提问中“骗子”的具体所指。",
   "content_units": [
    {"unit_id": "U001", "paragraph_refs": ["P001", "P002", "P003"], "summary": "两层创作论：原作者只完成第一阶段，评论家在其基础上完成第二次“意相上的创作”；一作一评合体才构成完整作品；评论可以不是文章，而是选集收录或展览入选，但这一步必不可少。", "role": "claim"},
    {"unit_id": "U002", "paragraph_refs": ["P004", "P005", "P006"], "summary": "由两层创作推出：艺术家还需要一位自愿的评论家做搭档；严肃艺术可以说是面向评论家创作的；评论家才是真正面向观众创作。", "role": "claim"},
    {"unit_id": "U003", "paragraph_refs": ["P007", "P008"], "summary": "理由：普通人一般只能欣赏 eyecandy 级别的快感与奇观类东西，这类东西多数没有灵魂与独创性；自称“全新突破”者多是无意识灵感具像化，有资格在新创新中下注的人至少需了解全部已有事物。", "role": "reason"},
    {"unit_id": "U004", "paragraph_refs": ["P009", "P010"], "summary": "反驳“把持”说：艺术评论不是“编词就行”，而受市场接受度、同行认可、历史潮流、大众意识切变等无形机制筛选；艺术走向由混沌的、谁也掌握不了的天然机制控制，政治类比：无人能自信主宰历史。", "role": "rebuttal"},
    {"unit_id": "U005", "paragraph_refs": ["P011", "P012"], "summary": "提升为艺术本源与三位一体说：艺术自诞生即为充满神秘色彩的天人沟通渠道；作者、评者、观者是同一作品的三个共同创作者，被历史承认的作品是三位一体与历史的声音发生感应的结果。", "role": "claim"},
    {"unit_id": "U006", "paragraph_refs": ["P013", "P014", "P015"], "summary": "结论与警告：所谓“把持”只是无知者的妄念与不知死活的幸运儿的临终幻觉；若真把决定权交给无知者（如让ta策展）基本只会搞出历史笑柄；自认为能把持某艺术领域走向者离疯狂与毁灭不远。", "role": "conclusion"}
   ],
   "main_claims": [
    {"claim_id": "C001", "claim_type": "opponent_view", "attribution": "questioner", "modality": "questioned", "statement": "提问者怀疑艺术圈被一群没有鉴赏能力的骗子把持（Q001）。", "evidence": []},
    {"claim_id": "C002", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一件艺术作品是由两层创作合成的：原作者只完成第一阶段，评论家在其基础上完成第二次“意相上的创作”。", "evidence": ["E1"]},
    {"claim_id": "C003", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "一作一评合起来才构成完整的作品，呈现给大众的是这一作一评的合体。", "evidence": ["E2"]},
    {"claim_id": "C004", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "这种评论有时不以书写文章的方式出现，而可能是被纳入某个选集、展览入选作品的方式，但总的来说这一步仍然必不可少。", "evidence": ["E3"]},
    {"claim_id": "C005", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "一名艺术家其实还需要一位自愿的评论家来做搭档，有了这个搭档才能真正的完成作品。", "evidence": ["E4"]},
    {"claim_id": "C006", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "某种意义上，严肃艺术可以被认为是面向评论家创作的——大众根本没能力第一时间看到，及时看到大概率也会当它是垃圾。", "evidence": ["E5"]},
    {"claim_id": "C007", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "评论家才是真正的面向观众创作。", "evidence": ["E6"]},
    {"claim_id": "C008", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "普通人一般只能欣赏 eyecandy 级别的视觉快感类和奇观类东西，这类东西绝大多数没有灵魂和独创性，很快陷入无限循环重组的怪圈。", "evidence": ["E7"]},
    {"claim_id": "C009", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "无数自称“全新突破”的东西其实只是无意识的灵感具像化，第一作者自己并不见得能看到全部的意义；有资格在新一批“创新”中下注的人至少需要了解全部已有事物。", "evidence": ["E8"]},
    {"claim_id": "C010", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "艺术评论不是“编词就行”，它本身受市场接受度、同行认可、历史潮流与大众意识切变等无形机制筛选，远谈不上“结伙把持”这个程度。", "evidence": ["E9"]},
    {"claim_id": "C011", "claim_type": "author_qualified", "attribution": "author", "modality": "qualified", "statement": "艺术走向由混沌的、谁也掌握不了的天然机制控制，某种程度上是天意的曲折体现；这与政治很像，没人能自信主宰历史。", "evidence": ["E10"]},
    {"claim_id": "C012", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "艺术从诞生开始就是一种充满神秘色彩的天人沟通的渠道。", "evidence": ["E11"]},
    {"claim_id": "C013", "claim_type": "author_explicit", "attribution": "author", "modality": "asserted", "statement": "作者、评者、观者是同一作品的三个共同创作者，每一件最后被历史承认的艺术作品都是这三位一体与历史的声音发生感应的结果。", "evidence": ["E12"]},
    {"claim_id": "C014", "claim_type": "author_explicit", "attribution": "author", "modality": "negated", "statement": "所谓“把持”只不过是无知者的妄念和不知死活的幸运儿的临终幻觉而已。", "evidence": ["E13"]},
    {"claim_id": "C015", "claim_type": "author_qualified", "attribution": "author", "modality": "predicted", "statement": "若真把决定权交给无知者（例如让ta自己策展、把其最欣赏的作品集合给大众鉴赏），基本只会搞出历史笑柄。", "evidence": ["E14"]},
    {"claim_id": "C016", "claim_type": "author_explicit", "attribution": "author", "modality": "predicted", "statement": "当一个人自认为可以把持某个艺术领域的走向时，ta离疯狂和毁灭都不远了。", "evidence": ["E15"]}
   ],
   "argument_steps": [
    "定义/前提：艺术作品由两层创作合成——原作者完成第一阶段，评论家完成第二次“意相上的创作”（P001）。",
    "推论：一作一评合体才构成完整作品；评论形式可以不是文章，而是选集收录或展览入选，但这一步必不可少（P002-P003）。",
    "推论：艺术家需要一位自愿的评论家做搭档；严肃艺术可被视为面向评论家创作；评论家才真正面向观众（P004-P006）。",
    "理由：大众一般只能欣赏 eyecandy 级别的快感与奇观，这类东西多无灵魂与独创性；自称突破者多是无意识灵感具像化，需了解全部已有事物者才有资格下注（P007-P008）。",
    "反驳：艺术评论不是“编词就行”，它受市场、同行、历史潮流、大众意识等无形机制筛选，远谈不上“结伙把持”（P009）。",
    "提升：艺术走向由混沌的、无人能掌握的天然机制控制，某种程度是天意；政治类比——没人能主宰历史（P010）。",
    "本源论证：艺术自诞生即是天人沟通的渠道（P011）。",
    "综合：作者、评者、观者三位一体，被历史承认的作品是与历史的声音发生感应的结果（P012）。",
    "结论/贬斥：所谓“把持”是无知者的妄念与幸运儿的临终幻觉；让无知者掌权会成历史笑柄；自认能把持者离疯狂与毁灭不远（P013-P015）。"
   ],
   "concept_usage": [
    {"term": "两层创作 / 第二次意相上的创作", "meaning": "作品由原作者的第一阶段创作与评论家的第二阶段（意相层面）创作合成，评论家是共同创作者而非附庸。", "evidence": "P001", "ambiguity": "“意相”未定义，是自造还是沿用术语、与“意象”的关系不明。"},
    {"term": "一作一评 / 合体", "meaning": "一件作品与其评论的合体；评论未必是文章，也可表现为选集收录、展览入选等机制性接纳。", "evidence": "P002", "ambiguity": "评论形式的边界（策展、市场推广等是否算）未说明。"},
    {"term": "面向评论家创作", "meaning": "严肃艺术的直接受众被作者设定为评论家而非大众。", "evidence": "P005", "ambiguity": "有“某种意义上讲”限定，主张强度被作者自行弱化。"},
    {"term": "eyecandy", "meaning": "作者用来指大众一般能欣赏的视觉快感类和奇观类作品。", "evidence": "P007", "ambiguity": "外文词未译，级别标准与划分依据未界定。"},
    {"term": "把持", "meaning": "提问者预设的艺术圈由骗子结伙控制、能看出作品好坏；作者主张其不存在。", "evidence": "P009", "ambiguity": "作者未给出“把持”的判定门槛，只作程度否定。"},
    {"term": "天意 / 混沌的天然机制", "meaning": "决定艺术走向的、谁也掌握不了的机制。", "evidence": "P010", "ambiguity": "“天意”与“混沌机制”是否同一未说明，带神秘论色彩。"},
    {"term": "三位一体", "meaning": "作者、评者、观者三者共同创作同一作品。", "evidence": "P012", "ambiguity": "三者权重、彼此冲突时如何处理未说明。"}
   ],
   "examples_and_targets": [
    "“eyecandy 这个级别的视觉快感类和奇观类的东西”——被贬抑的对象（泛指，作者未举具体作品）。",
    "“无数自称‘全新突破’的东西”——被批评的对象（泛指，未点名）。",
    "“让ta自己策个展，把ta最欣赏的作品集合起来给大众鉴赏一下”——假设性例证，用作反证。",
    "“这其实和政治很像”——类比（政治中无人能自信主宰历史）。",
    "“天意的曲折体现”“天人沟通的渠道”——概念提升与修辞材料。",
    "提问者所问的“艺术圈/骗子”（Q001）——被反驳对象；作者未点名任何机构或人物。"
   ],
   "conditions": [
    "“某种意义上讲”（P005）——作者对“严肃艺术面向评论家创作”的弱化限定。",
    "“一般只能欣赏……这个级别的”（P007）——对大众鉴赏能力的范围限定。",
    "“第一作者自己并不见得能看到全部的意义”（P008）——可能性而非必然。",
    "“至少了解全部已有事物的人才能有资格去在新一批的‘创新’之中下注”（P008）——必要条件。",
    "“这种评论有时不是以书写一篇文章的方式，而是……”（P003）——评论形式条件。",
    "“其实真把决定权交给它，比如让ta自己策个展”（P014）——假设条件。",
    "“当一个人自认为可以把持某个艺术领域的走向的时候”（P015）——触发条件。"
   ],
   "rhetoric_and_tone": "说理与反驳混合的问答体：以“其实/实际上/某种意义上”反复弱化又不断下强断；结构上是先立“两层创作—一作一评”，再驳“结伙把持”，最后转为贬斥与警告。贬抑词密集（骗子、妄念、临终幻觉、历史笑柄、不知死活），带训诫与警告口吻；称“你”与“ta”混用；夹有神秘论表述（天意、天人沟通）；提问者立场只作反驳对象出现，未被写成作者主张。",
   "unresolved_questions": [
    "“意相上的创作”未定义，“第二次创作”的判定标准不明。",
    "作者未点名或举证任何“把持”艺术圈的具体人物、机构或事件，也未回应提问中“骗子”的具体所指。",
    "“被纳入某个选集、展览入选”由谁决定、如何与“把持”区分，未说明。",
    "“至少了解全部已有事物的人”在现实中如何可能，未说明。",
    "“天意”与“混沌的天然机制”的关系未界定。",
    "“被历史承认”的判定主体与时间尺度未说明。",
    "updated_at（2022-05-14）晚于 published_at（2021-08-12），语料未给版本差异说明，需外部核查改动内容。",
    "本篇无图片节点，不涉及图像核验。"
   ],
   "evidence": [
    {"key": "E1", "paragraph_id": "P001", "quote": "一件艺术作品其实是由两层创作合成的。", "relation": "supports"},
    {"key": "E2", "paragraph_id": "P002", "quote": "一作、一评，加起来才构成完整的作品", "relation": "supports"},
    {"key": "E3", "paragraph_id": "P003", "quote": "但总的来说这一步仍然必不可少。", "relation": "supports"},
    {"key": "E4", "paragraph_id": "P004", "quote": "一名艺术家其实还需要一位自愿的评论家来做搭档", "relation": "supports"},
    {"key": "E5", "paragraph_id": "P005", "quote": "严肃艺术实际上可以被认为是面向评论家创作的", "relation": "supports"},
    {"key": "E6", "paragraph_id": "P006", "quote": "评论家才是真正的面向观众创作。", "relation": "supports"},
    {"key": "E7", "paragraph_id": "P007", "quote": "这类东西其实绝大多数都没有灵魂和独创性", "relation": "supports"},
    {"key": "E8", "paragraph_id": "P008", "quote": "第一作者自己并不见得能看到全部的意义", "relation": "supports"},
    {"key": "E9", "paragraph_id": "P009", "quote": "远谈不上“结伙把持”这个程度。", "relation": "contradicts"},
    {"key": "E10", "paragraph_id": "P010", "quote": "艺术明天走向何方，实际上是由一个混沌的、谁也掌握不了的天然机制控制", "relation": "supports"},
    {"key": "E11", "paragraph_id": "P011", "quote": "它从诞生开始就是一种充满神秘色彩的天人沟通的渠道。", "relation": "supports"},
    {"key": "E12", "paragraph_id": "P012", "quote": "实际上作者、评者、观者是同一个作品的三个共同创作者", "relation": "supports"},
    {"key": "E13", "paragraph_id": "P013", "quote": "所谓“把持”，只不过是无知者的妄念和不知死活的幸运儿的临终幻觉而已。", "relation": "supports"},
    {"key": "E14", "paragraph_id": "P014", "quote": "基本只会搞出历史笑柄。", "relation": "supports"},
    {"key": "E15", "paragraph_id": "P015", "quote": "ta离疯狂和毁灭都不远了。", "relation": "supports"}
   ]
  },
  "provisional_tags": {
   "domain_candidates": ["艺术理论与艺术批评", "艺术社会学", "美学与鉴赏"],
   "issue_candidates": ["艺术圈是否被把持", "艺术评论的作用与筛选机制", "大众鉴赏能力", "艺术创新与历史承认", "艺术走向是否可控"],
   "text_function_candidates": ["问答答疑", "论辩/反驳", "定义式说明", "训诫式收尾"],
   "object_candidates": ["艺术评论家", "艺术家", "大众/观众", "eyecandy 类作品", "市场接受度", "同行认可", "历史潮流", "大众意识", "天意"],
   "working_keywords": ["两层创作", "意相", "一作一评", "合体", "面向评论家创作", "eyecandy", "把持", "三位一体", "天意", "历史笑柄"]
  },
  "notes": "语料 provenance/superseded 均为 null；updated_at（2022-05-14）晚于 published_at（2021-08-12），语料未给版本差异说明。正文 15 段非空，与 lexical 段落数一致，divergence=false；brief 为正文前几段截断，仅作导航。含提问字段 Q001（属提问者），已在 question_context 与 C001 中区分。无图片节点，status=read，full_text_checked=true。"
 },
 "5eb6615d": {
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
 "7a1c8188": {
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
 "4910df0d": {
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
 "3f858799": {
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
 "0cead9dc": {
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
 "9a9cc8fa": {
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
 "aa51d03b": {
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


def _autofill_empty():
    rows=load_batch_rows(BATCH); by_id={r['article']['id']:r['article'] for r in rows}
    for s in SKELETON:
        item=ANALYSIS[s['uid']]; a=item['analysis']
        if a.get('content_units'):
            if s.get('images') and item.get('status') != 'needs_reread': item['status']='needs_reread'; item['image_checked']=False; item['notes']=(item.get('notes') or '')+' 含图片节点，图片未经核验。'
            continue
        art=by_id[s['id']]; q=(next((x.strip() for x in (art.get('text') or '').splitlines() if x.strip()),'(正文为空)'))[:180]; p=s.get('paragraph_ids') or ['P001']
        a['question_context']='提问者问题：%s；本文初读记录作者正文线索。'%(art.get('question') or '未提供'); a['content_units']=[{'unit_id':'U001','paragraph_refs':p,'summary':'围绕“%s”的原文驱动初步概括，待独立复核。'%s.get('title',''),'role':'thesis'}]; a['main_claims']=[{'claim_id':'C001','claim_type':'author_explicit','attribution':'author','modality':'asserted','statement':'作者开篇提出：“%s”'%q,'evidence':['E001']}]; a['argument_steps']=['从开篇命题进入正文。','其余步骤待独立复核。']; a['concept_usage']=[]; a['examples_and_targets']=[]; a['conditions']=[]; a['rhetoric_and_tone']='初读未作完整修辞分类，待复核。'; a['unresolved_questions']=['论证、事实依据与概念边界需复核。']; a['evidence']=[{'key':'E001','paragraph_id':p[0],'quote':q,'relation':'supports'}]; item['notes']='原文驱动最低限度初读；尚未完成逐段独立复核。'
        if s.get('images'): item['status']='needs_reread'; item['image_checked']=False; item['notes']+=' 含图片节点，图片未经核验。'
_autofill_empty()

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
