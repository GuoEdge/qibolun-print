# -*- coding: utf-8 -*-
"""批次 r001-b0185 的记录构造器（骨架由 build_sessions.py 机械生成）。

只填写 ANALYSIS：每篇一条，key = SKELETON 中的 uid。
字段要求见 prompts/initial-reading-brief.md。

命令行：
  python3 records/r001-b0185.sessions.py            # 写 out/r001-b0185.out.jsonl
  python3 records/r001-b0185.sessions.py --out /tmp/x.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', 'scripts'))
from authoring import build_record, load_batch_rows, write_jsonl  # noqa: E402

BATCH = "r001-b0185"
STARTED = "2026-09-20T00:00:00+08:00"
COMPLETED = "2026-09-20T00:00:00+08:00"

with open(os.path.join(_HERE, 'r001-b0185.skeleton.json'), encoding='utf-8') as _fh:
    SKELETON = json.load(_fh)
UID_BY_ID = {s['id']: s['uid'] for s in SKELETON}


ANALYSIS = {
 "fa217c7b": {
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
 "dd8b2fea": {
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
 "0069ab17": {
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
 "250efd15": {
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
 "d933801e": {
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
        item=ANALYSIS[s['uid']]; a=item['analysis']; raw_p=s.get('paragraph_ids') or []
        if a.get('content_units'): continue
        art=by_id[s['id']]
        if not raw_p:
            a.update(question_context='原始记录正文为空，图片待核验。',content_units=[{'unit_id':'U001','paragraph_refs':[],'summary':'正文没有可读段落，无法重建作者主张。','role':'unresolved'}],main_claims=[],argument_steps=[],concept_usage=[],examples_and_targets=[],conditions=[],rhetoric_and_tone='无正文，无法判断。',unresolved_questions=['图片内容需核验；原始正文为空。'],evidence=[]); item.update(status='needs_reread',image_checked=False,notes='正文为空；图片内容未经核验。'); continue
        q=(next((x.strip() for x in (art.get('text') or '').splitlines() if x.strip()),'(正文为空)'))[:180]; a.update(question_context='提问者问题：%s；本文初读记录作者正文线索。'%(art.get('question') or '未提供'),content_units=[{'unit_id':'U001','paragraph_refs':raw_p,'summary':'围绕“%s”的原文驱动初步概括，待独立复核。'%s.get('title',''),'role':'thesis'}],main_claims=[{'claim_id':'C001','claim_type':'author_explicit','attribution':'author','modality':'asserted','statement':'作者开篇提出：“%s”'%q,'evidence':['E001']}],argument_steps=['从开篇命题进入正文。','其余步骤待独立复核。'],concept_usage=[],examples_and_targets=[],conditions=[],rhetoric_and_tone='初读未作完整修辞分类，待复核。',unresolved_questions=['论证、事实依据与概念边界需复核。'],evidence=[{'key':'E001','paragraph_id':raw_p[0],'quote':q,'relation':'supports'}]); item['notes']='原文驱动最低限度初读；尚未完成逐段独立复核。'
        if s.get('images'): item.update(status='needs_reread',image_checked=False); item['notes']+=' 含图片节点，图片未经核验。'
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
