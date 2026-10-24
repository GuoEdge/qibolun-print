"""Read existing project artifacts; write only the dated handoff directory.

This script does not classify articles, rebuild indexes, fetch sources, or
modify the corpus/manual tables. Counters describe stored decisions, not a
new semantic review. Run with: python -B <this-file>
"""
import csv
import hashlib
import io
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

DEST = Path(__file__).resolve().parent
ROOT = DEST.parents[2]
REPORTS = ROOT / 'research-rebuild/reports'
DATA = ROOT / 'research-rebuild/data'
INPUTS = {}


def tracked(path):
    raw = path.read_bytes()
    INPUTS[str(path.relative_to(ROOT))] = {
        'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest(),
        'modified_at': datetime.fromtimestamp(path.stat().st_mtime).astimezone().isoformat(),
    }
    return raw.decode('utf-8-sig')


def table(path, delimiter=','):
    return list(csv.DictReader(io.StringIO(tracked(path)), delimiter=delimiter))


def js(path):
    return json.loads(tracked(path))


def jsonl(path):
    return [json.loads(line) for line in tracked(path).splitlines() if line.strip()]


def counts(rows, key):
    return dict(Counter(row.get(key, '') for row in rows))


def write_table(name, rows):
    if not rows:
        return
    with (DEST / name).open('w', encoding='utf-8-sig', newline='') as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def parts(value):
    return [x for x in value.split(';') if x and x != '-']


def textcell(value):
    return str(value).replace('|', '\\|').replace('\n', ' ')


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    corpus = jsonl(ROOT / 'sooon-q9adg-articles-v2.jsonl')
    old = jsonl(ROOT / 'sooon-q9adg-articles.jsonl')
    corpus_by_id = {r['id']: r for r in corpus}
    manual = table(DATA / 'print-topic-manual-decisions-v2.csv')
    formal = table(REPORTS / 'article-classification-v2.csv')
    registry = table(DATA / 'print-topic-registry-v2.csv')
    queue = table(REPORTS / 'live-manual-classification-queue-v2.csv')
    images = table(REPORTS / 'image-article-audit-v1.csv')
    sample = table(REPORTS / 'print-topic-audit-sample-v2.csv')
    native = table(REPORTS / 'native-article-category-summary.csv')
    native_by_id = {r['article_id']: r for r in native}
    print_index = table(REPORTS / 'print-index/print-research-index.csv')
    manual_by_id = {r['id']: r for r in manual}
    formal_by_id = {r['id']: r for r in formal}
    images_by_id = {r['id']: r for r in images}
    queue_by_id = {r['id']: r for r in queue}
    provisional = [r for r in manual if r['classification_status'] == 'manual_provisional']
    codes = {r['code'] for r in registry}
    errors = []
    for name, rows in [('corpus', corpus), ('manual', manual), ('formal', formal), ('queue', queue)]:
        ids = [r['id'] for r in rows]
        if len(ids) != len(set(ids)):
            errors.append(f'{name}: duplicate IDs')
    for name, rows in [('manual', manual), ('formal', formal)]:
        if {r['id'] for r in rows} != set(corpus_by_id):
            errors.append(f'{name}: ID coverage differs from corpus')
        for r in rows:
            aid = r['id']
            primary = r['primary_print_topic_code']
            secondary = parts(r['secondary_print_topic_codes'])
            if primary not in codes or any(x not in codes for x in secondary):
                errors.append(f'{name}: invalid code {aid}')
            if len(secondary) > 3 or len(set(secondary)) != len(secondary) or primary in secondary:
                errors.append(f'{name}: invalid secondary {aid}')
            if r['title'] != corpus_by_id.get(aid, {}).get('title'):
                errors.append(f'{name}: title mismatch {aid}')
    parity = []
    for r in manual:
        for key in ['title', 'primary_print_topic_code', 'secondary_print_topic_codes', 'classification_status']:
            if r[key] != formal_by_id.get(r['id'], {}).get(key):
                parity.append({'id': r['id'], 'field': key})
    if parity:
        errors.append(f'manual/formal field mismatches: {len(parity)}')
    if {r['id'] for r in queue} != {r['id'] for r in provisional}:
        errors.append('queue IDs differ from provisional IDs')

    batches, membership = [], defaultdict(list)
    for n in range(157, 165):
        bp = REPORTS / f'live-manual-batch-selection-v2-round{n}.csv'
        fp = REPORTS / f'round{n}-fulltext.json'
        dp = REPORTS / f'round{n}-decisions.tsv'
        batch, fulltext = table(bp), js(fp)
        decisions = table(dp, '\t') if dp.exists() else []
        ids = [r['id'] for r in batch]
        for aid in ids:
            membership[aid].append(n)
        mismatch = []
        mapping = {'primary': 'primary_print_topic_code', 'secondary': 'secondary_print_topic_codes',
                   'status': 'classification_status', 'basis': 'decision_basis', 'title': 'title'}
        for d in decisions:
            for dk, mk in mapping.items():
                value = ';'.join(parts(d[dk])) if dk == 'secondary' else d[dk]
                if value != manual_by_id.get(d['id'], {}).get(mk):
                    mismatch.append({'id': d['id'], 'field': dk})
        batches.append({
            'round': n, 'selected': len(batch), 'fulltext': len(fulltext),
            'body_chars': sum(len(r.get('text') or '') for r in fulltext),
            'image_articles_in_selection': sum(int(r.get('deepseek_image_count') or 0) > 0 for r in batch),
            'selection_fulltext_id_order_equal': ids == [r['id'] for r in fulltext],
            'selection_fulltext_lengths_equal': [int(r['body_char_count']) for r in batch] == [len(r.get('text') or '') for r in fulltext],
            'in_manual': sum(aid in manual_by_id for aid in ids),
            'manual_status_counts': dict(Counter(manual_by_id.get(aid, {}).get('classification_status', 'MISSING') for aid in ids)),
            'decision_file_exists': dp.exists(), 'decision_rows': len(decisions),
            'decision_id_order_equal': ids == [r['id'] for r in decisions] if dp.exists() else None,
            'decision_manual_mismatches': mismatch,
        })

    pending_rows = []
    for r in sorted(provisional, key=lambda x: int(formal_by_id[x['id']]['ordinal'])):
        aid = r['id']
        f, im, q = formal_by_id[aid], images_by_id.get(aid, {}), queue_by_id.get(aid, {})
        pending_rows.append({
            'ordinal': f['ordinal'], 'id': aid, 'title': r['title'],
            'primary': r['primary_print_topic_code'], 'secondary': r['secondary_print_topic_codes'],
            'body_char_count': q.get('body_char_count', ''),
            'image_count': im.get('image_count', '0'), 'reviewed_image_count': im.get('reviewed_image_count', '0'),
            'image_review_status': im.get('image_review_status', 'no_image_inventory'),
            'article_decision': im.get('article_decision', ''),
            'round157_164': ';'.join(map(str, membership.get(aid, []))),
            'decision_basis': r['decision_basis'], 'review_note': r['review_note'],
            'queue_priority_reasons': q.get('priority_reasons', ''),
        })
    write_table('pending-92-snapshot.csv', pending_rows)
    write_table('image-254-snapshot.csv', images)
    newer = [r for r in formal if r['id'] not in {x['id'] for x in old}]
    firstpass_missing = [r for r in formal if r['deepseek_available'].lower() != 'true']
    write_table('first-pass-missing-snapshot.csv', [
        {k: r[k] for k in ['ordinal', 'id', 'title', 'published_date', 'primary_print_topic_code', 'classification_status', 'deepseek_available']}
        for r in firstpass_missing])
    manifest = js(ROOT / 'research-rebuild/deepseek-batches/manifest.json')
    independent = jsonl(REPORTS / 'independent-reviews.jsonl')
    write_table('confirmed-with-image-work-snapshot.csv', [
        {**r, 'classification_status': manual_by_id[r['id']]['classification_status']}
        for r in images if r['image_review_status'] != 'complete'
        and manual_by_id[r['id']]['classification_status'] == 'manual_confirmed'])
    published = [r['publishedAt'] for r in corpus if isinstance(r.get('publishedAt'), (int, float))]
    result = {
        'generated_at': datetime.now().astimezone().isoformat(),
        'scope': 'Read-only handoff inventory; no new semantic review; only handoff files written',
        'corpus': {'records': len(corpus), 'unique_ids': len(corpus_by_id), 'old_records': len(old),
                   'new_records': len(newer), 'raw_text_chars': sum(len(r.get('text') or '') for r in corpus),
                   'raw_text_utf16_units': sum(len((r.get('text') or '').encode('utf-16-le'))//2 for r in corpus),
                   'empty_raw_text': sum(not r.get('text') for r in corpus),
                   'published_min': datetime.fromtimestamp(min(published)/1000).astimezone().isoformat(),
                   'published_max': datetime.fromtimestamp(max(published)/1000).astimezone().isoformat()},
        'manual_records': len(manual), 'manual_status_counts': counts(manual, 'classification_status'),
        'formal_status_counts': counts(formal, 'classification_status'),
        'topic_counts': counts(formal, 'primary_print_topic_code'),
        'topics': [{**r, 'articles': sum(x['primary_print_topic_code'] == r['code'] for x in formal),
                    'provisional': sum(x['primary_print_topic_code'] == r['code'] for x in provisional)} for r in registry],
        'new_status_counts': counts(newer, 'classification_status'),
        'queue_records': len(queue), 'queue_equals_provisional': {r['id'] for r in queue} == {r['id'] for r in provisional},
        'manual_formal_mismatches': parity, 'structural_errors': errors,
        'pending_by_image_status': counts(pending_rows, 'image_review_status'),
        'pending_by_article_decision': counts(pending_rows, 'article_decision'),
        'pending_without_157_164': [{'id': r['id'], 'title': r['title']} for r in pending_rows if not r['round157_164']],
        'rounds': batches, 'selected_157_164_unique': len(membership),
        'image_articles': len(images), 'image_nodes': sum(int(r['image_count']) for r in images),
        'image_reviewed_nodes': sum(int(r['reviewed_image_count']) for r in images),
        'image_failed_nodes': sum(int(r['failed_image_count']) for r in images),
        'image_article_status_counts': counts(images, 'image_review_status'),
        'image_article_decision_counts': counts(images, 'article_decision'),
        'image_status_by_classification': dict(Counter(
            r['image_review_status'] + '/' + manual_by_id[r['id']]['classification_status'] for r in images)),
        'image_exception_articles': [r for r in images if r['article_decision'] in {'exclude_article_candidate', 'retain_article_source_incomplete'}],
        'sample_records': len(sample), 'sample_decisions': counts(sample, 'audit_decision'),
        'sample_reviewers': counts(sample, 'reviewer'),
        'independent_review_records': len(independent),
        'independent_review_unique_ids': len({r.get('article_id') for r in independent}),
        'independent_review_conclusions': counts(independent, 'conclusion'),
        'native_summary_records': len(native),
        'native_current_local_status': dict(Counter(native_by_id.get(aid, {}).get('native_assignment_status', 'MISSING') for aid in corpus_by_id)),
        'native_current_local_missing_ids': [aid for aid in corpus_by_id if aid not in native_by_id],
        'native_current_local_multi_category': sum(int(native_by_id.get(aid, {}).get('native_category_count') or 0) > 1 for aid in corpus_by_id),
        'print_index_records': len(print_index),
        'print_index_unique_ids': len({r.get('id') for r in print_index}),
        'print_index_headers': list(print_index[0]) if print_index else [],
        'concept_tag_counts': dict(Counter(t for r in formal for t in parts(r['concept_tags']))),
        'concept_zero_records': sum(not parts(r['concept_tags']) for r in formal),
        'concept_average_tags': sum(len(parts(r['concept_tags'])) for r in formal)/len(formal),
        'first_pass_manifest_batches': len(manifest.get('batches', [])),
        'first_pass_missing': [{'id': r['id'], 'title': r['title']} for r in firstpass_missing],
        'stored_classification_summary': js(REPORTS / 'article-classification-v2-summary.json'),
        'stored_image_summary': js(REPORTS / 'image-article-audit-v1-summary.json'),
        'stored_provisional_reasons': js(REPORTS / 'provisional-reasons-audit-v2.json'),
        'stored_firstpass_validation_summary': js(REPORTS / 'validation-report.json')['summary'],
        'inputs': INPUTS,
    }
    lines = ['# 交接附件：92 篇现存待定分类', '', '生成自当前正式人工决定表；未新增正文判断。完整原因和原有复核备注见同目录 CSV。', '',
             '|序号|标题|ID|主类|图像状态|批次157–164|', '|---:|---|---|---|---|---|']
    lines += ['|' + '|'.join(textcell(r[k]) for k in ['ordinal','title','id','primary','image_review_status','round157_164']) + '|' for r in pending_rows]
    (DEST / 'pending-92-snapshot.md').write_text('\n'.join(lines)+'\n', encoding='utf-8')
    changed = [name for name, meta in INPUTS.items() if hashlib.sha256((ROOT/name).read_bytes()).hexdigest() != meta['sha256']]
    result['inputs_changed_during_collection'] = changed
    (DEST / 'evidence-snapshot.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    compact = {k: v for k, v in result.items() if k not in {'inputs','stored_classification_summary','stored_image_summary','topics','sample_reviewers','image_exception_articles'}}
    print(json.dumps(compact, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
