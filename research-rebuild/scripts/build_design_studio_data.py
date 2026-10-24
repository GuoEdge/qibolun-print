#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build layered local data for the Qibo design studio."""
from __future__ import annotations
import csv, hashlib, json, re
from collections import defaultdict
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
R = ROOT / "research-rebuild"
OUT = R / "print-design-20260927/design-studio/data"
CORPUS = ROOT / "sooon-q9adg-articles-v2.jsonl"
INDEX = R / "reports/print-index/print-research-index.csv"
REGISTRY = R / "data/print-topic-registry-v2.csv"
IMG_INV = R / "data/image-inventory.csv"
IMG_AUDIT = R / "reports/image-article-audit-v1.csv"
MANIFEST = R / "print-20260926-rebuilt-v2/PRINT-MANIFEST.json"
PKG = R / "print-20260926-rebuilt-v2"
CST = timezone(timedelta(hours=8))
SAMPLE_ORDS = [4044, 2387, 3926, 2967, 3820]


def rows(path: Path, delimiter=','):
    with path.open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f, delimiter=delimiter))


def corpus_rows():
    out = {}
    with CORPUS.open(encoding='utf-8') as f:
        for line in f:
            if line.strip():
                x = json.loads(line); out[x['id']] = x
    return out


def topic_dir(row):
    return re.sub(r'[／/]', '-', f"{row['primary_print_topic']}-{row['primary_print_topic_name']}")


def image_records(index_row, inv_by_id):
    aid = index_row['id']
    folder = PKG / topic_dir(index_row) / 'images'
    files = {}
    if folder.exists():
        pat = re.compile(rf"{int(index_row['source_ordinal'])}-{re.escape(aid)}-(\d+)\.jpg$")
        for p in folder.glob(f"{int(index_row['source_ordinal'])}-{aid}-*.jpg"):
            m = pat.match(p.name)
            if m: files[int(m.group(1))] = p
    out = []
    for idx in sorted(files):
        p = files[idx]
        out.append({'index': idx, 'src': str(p.relative_to(R)).replace('\\', '/'), 'width': None, 'height': None})
    # If a package file is not present, it is intentionally absent from reading edition.
    return out


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    corpus = corpus_rows()
    idx = rows(INDEX)
    reg = rows(REGISTRY)
    inv = rows(IMG_INV)
    audit = {x['id']: x for x in rows(IMG_AUDIT)}
    topics = [{'code': x['code'], 'name': x['name'], 'description': x['description'], 'sortOrder': int(x['sort_order'])} for x in reg]
    meta = []
    samples = []
    bodies = defaultdict(list)
    errors = []
    for r in idx:
        ordn = int(r['source_ordinal'])
        aid = r['id']
        article = corpus.get(aid, {})
        imgs = image_records(r, inv)
        archive = r['primary_print_topic'] == 'A00' or r['classification_status'] == 'manual_provisional' or r['title'] in {'兼得','最大成长速度','战马阉割','活成这样','各行其道','基督教与食血'}
        reason = '待审' if r['classification_status'] == 'manual_provisional' else ('排除候选' if r['title'] in {'兼得','最大成长速度','战马阉割','活成这样','各行其道','基督教与食血'} else None)
        item = {
            'ordinal': ordn, 'id': aid, 'title': r['title'], 'date': r.get('published_date',''),
            'bodyChars': int(r.get('body_char_count') or len(article.get('text') or '')),
            'bodyState': r.get('source_body_state',''), 'primaryTopic': r['primary_print_topic'],
            'primaryName': r['primary_print_topic_name'],
            'secondaryTopics': r.get('secondary_print_topic_codes','').split(';') if r.get('secondary_print_topic_codes') else [],
            'secondaryNames': r.get('secondary_print_topic_names','').split(';') if r.get('secondary_print_topic_names') else [],
            'imageTotal': int(audit.get(aid, {}).get('image_count') or r.get('deepseek_image_count') or 0),
            'reviewedImageCount': int(audit.get(aid, {}).get('reviewed_image_count') or len(imgs)),
            'availableImageCount': len(imgs), 'archive': archive, 'archiveReason': reason,
            'classificationStatus': r.get('classification_status',''), 'readingStatus': r.get('reading_status',''),
            'images': imgs,
        }
        meta.append(item)
        body = {'ordinal': ordn, 'id': aid, 'question': article.get('question',''), 'body': article.get('text',''), 'url': article.get('url',''), 'nativePaths': r.get('native_object_paths','').split(';') if r.get('native_object_paths') else [], 'concepts': r.get('concept_tags','').split(';') if r.get('concept_tags') else [], 'evidenceNote': r.get('evidence_basis','')}
        bodies[r['primary_print_topic']].append(body)
        if ordn in SAMPLE_ORDS:
            samples.append(body | {'title': r['title'], 'date': r.get('published_date',''), 'primaryName': r['primary_print_topic_name'], 'meta': item})
        if not aid in corpus: errors.append(f'missing corpus id {aid}')
    meta.sort(key=lambda x: x['ordinal'])
    if [x['ordinal'] for x in meta] != list(range(1, 4306)): errors.append('ordinal sequence mismatch')
    for code in bodies: bodies[code].sort(key=lambda x: x['ordinal'])
    plan = json.loads(MANIFEST.read_text(encoding='utf-8'))
    base = {'generatedAt': datetime.now(CST).isoformat(), 'corpusSha256': hashlib.sha256(CORPUS.read_bytes()).hexdigest(), 'articleCount': len(meta), 'sources': {'corpus': str(CORPUS), 'index': str(INDEX), 'registry': str(REGISTRY), 'manifest': str(MANIFEST)}, 'sampleOrdinals': SAMPLE_ORDS}
    (OUT/'manifest.json').write_text(json.dumps(base, ensure_ascii=False, indent=2), encoding='utf-8')
    (OUT/'topics.json').write_text(json.dumps(topics, ensure_ascii=False, indent=2), encoding='utf-8')
    (OUT/'article-meta.json').write_text(json.dumps(meta, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    (OUT/'samples.json').write_text(json.dumps(samples, ensure_ascii=False, indent=2), encoding='utf-8')
    (OUT/'images.json').write_text(json.dumps({str(x['ordinal']): x['images'] for x in meta}, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    (OUT/'plan-baseline.json').write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding='utf-8')
    for code, data in bodies.items(): (OUT/f'bodies-{code}.json').write_text(json.dumps(data, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    report = {'ok': not errors, 'errors': errors, 'articleCount': len(meta), 'topicCounts': {t['code']: sum(x['primaryTopic']==t['code'] for x in meta) for t in topics}, 'sampleOrdinals': SAMPLE_ORDS, 'generatedAt': base['generatedAt']}
    (OUT/'validation-report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=2))

if __name__ == '__main__': main()
