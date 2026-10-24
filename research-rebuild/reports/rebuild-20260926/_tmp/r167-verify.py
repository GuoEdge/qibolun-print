# -*- coding: utf-8 -*-
"""Independent mechanical verification of the written round167 deliverables.

Reads only the files on disk (audit TSV, decisions TSV, revision CSV, selection CSV,
fulltext JSON, registry CSV) and re-runs every protocol check from scratch.
"""
import csv, io, json, re, sys

BASE = 'research-rebuild/reports/rebuild-20260926/round167'
REG = 'research-rebuild/data/print-topic-registry-v2.csv'
VALID_BLOCK = {'source_empty', 'source_truncated', 'body_is_quotation', 'body_is_pointer',
               'body_question_mismatch', 'body_too_short_for_center', 'a00_registry_gap'}

def norm(s):
    return re.sub(r'[\s“”"\'‘’]+', '', s or '')

def lcs_len(a, b):
    best = 0
    prev = [0] * (len(b) + 1)
    for i in range(1, len(a) + 1):
        cur = [0] * (len(b) + 1)
        ai = a[i - 1]
        for j in range(1, len(b) + 1):
            if ai == b[j - 1]:
                cur[j] = prev[j - 1] + 1
                best = max(best, cur[j])
        prev = cur
    return best

fails, notes = [], []
sel = list(csv.DictReader(io.open(BASE + '/round167-selection.csv', encoding='utf-8-sig', newline='')))
aud = list(csv.DictReader(io.open(BASE + '/round167-body-evidence-audit.tsv', encoding='utf-8', newline=''), delimiter='\t'))
dec = list(csv.DictReader(io.open(BASE + '/round167-decisions.tsv', encoding='utf-8', newline=''), delimiter='\t'))
rev = list(csv.DictReader(io.open(BASE + '/round167-revision-log.csv', encoding='utf-8', newline='')))
ft = {p['id']: p for p in json.load(io.open(BASE + '/round167-fulltext.json', encoding='utf-8'))}
reg = set()
for r in csv.DictReader(io.open(REG, encoding='utf-8-sig', newline='')):
    reg.add(r['code'])

AUD_COLS = ['id', 'title', 'source_ordinal', 'body_char_count', 'old_primary', 'old_secondary',
            'old_status', 'new_primary', 'new_secondary', 'new_status', 'blocking_reason',
            'body_evidence_quote', 'decision_reason', 'reviewer', 'reviewed_at']
DEC_COLS = ['id', 'title', 'primary', 'secondary', 'status', 'basis', 'risk_note']
REV_COLS = ['id', 'title', 'old_primary', 'old_secondary', 'old_status', 'new_primary',
            'new_secondary', 'new_status', 'basis', 'risk_note', 'revision_source', 'revised_at']
for name, rows, cols in (('audit', aud, AUD_COLS), ('decisions', dec, DEC_COLS), ('revision', rev, REV_COLS)):
    if list(rows[0].keys()) != cols:
        fails.append('%s columns mismatch: %s' % (name, list(rows[0].keys())))

sel_ids = [r['id'] for r in sel]
if len(aud) != len(sel) or [r['id'] for r in aud] != sel_ids:
    fails.append('audit rows/order != selection')
if len(dec) != len(sel) or [r['id'] for r in dec] != sel_ids:
    fails.append('decisions rows/order != selection')
if set(r['id'] for r in aud) != set(sel_ids) or set(r['id'] for r in dec) != set(sel_ids):
    fails.append('ID set mismatch')
if len(set(sel_ids)) != len(sel_ids):
    fails.append('duplicate ids in selection')

total = 0
for a in aud:
    pid = a['id']
    p = ft[pid]
    text = p['text']
    total += len(text)
    # order/count
    if a['body_char_count'] != str(len(text)):
        fails.append('%s body_char_count mismatch' % a['title'])
    if a['body_char_count'] != str(p['body_char_count']):
        fails.append('%s body_char_count != packet' % a['title'])
    if a['body_evidence_quote'].strip() == '':
        fails.append('%s empty quote' % a['title'])
    q = norm(a['body_evidence_quote'])
    t = norm(text)
    if lcs_len(q, t) < 12:
        fails.append('%s quote <12 match' % a['title'])
    if q not in t:
        notes.append('%s quote not full-length match (lcs=%d)' % (a['title'], lcs_len(q, t)))
    if q.rstrip('。！？”') == norm(p['title']):
        fails.append('%s quote is just the title' % a['title'])
    if a['body_evidence_quote'].rstrip().endswith('？'):
        fails.append('%s quote ends with question mark' % a['title'])
    # codes
    for code in [a['new_primary']] + [c for c in a['new_secondary'].split(';') if c]:
        if code not in reg:
            fails.append('%s code not in registry: %s' % (a['title'], code))
    if a['new_primary'] in a['new_secondary'].split(';'):
        fails.append('%s primary in secondary' % a['title'])
    if not a['new_primary']:
        fails.append('%s missing primary' % a['title'])
    if len([c for c in a['new_secondary'].split(';') if c]) > 3:
        fails.append('%s >3 secondary' % a['title'])
    # status / blocking
    if a['new_status'] == 'manual_provisional':
        if a['blocking_reason'] not in VALID_BLOCK:
            fails.append('%s invalid blocking_reason' % a['title'])
    elif a['new_status'] == 'manual_confirmed':
        if a['blocking_reason'] != '':
            fails.append('%s confirmed row has blocking_reason' % a['title'])
    else:
        fails.append('%s unexpected status %s' % (a['title'], a['new_status']))
    if a['reviewer'] != 'subagent+round167-body-review' or a['reviewed_at'] != '2026-09-26':
        fails.append('%s reviewer/date wrong' % a['title'])
    # old values must match packet
    if a['old_primary'] != (p.get('manual_primary') or ''):
        fails.append('%s old_primary != packet' % a['title'])
    if a['old_secondary'] != (p.get('manual_secondary') or ''):
        fails.append('%s old_secondary != packet' % a['title'])
    if a['old_status'] != (p.get('manual_status') or ''):
        fails.append('%s old_status != packet' % a['title'])
    if a['title'] != p['title']:
        fails.append('%s title != packet' % a['title'])
    if a['source_ordinal'] != [r for r in sel if r['id'] == pid][0]['source_ordinal']:
        fails.append('%s source_ordinal != selection' % a['title'])

# decisions vs audit agreement
for a, d in zip(aud, dec):
    if (a['new_primary'], a['new_secondary'], a['new_status']) != (d['primary'], d['secondary'], d['status']):
        fails.append('%s decisions != audit' % a['title'])
    if not d['risk_note'].strip():
        fails.append('%s empty risk_note' % a['title'])

# revision log: exactly the changed rows
changed = [r['id'] for r in aud if (r['old_primary'] != r['new_primary']
                                    or r['old_secondary'] != r['new_secondary']
                                    or r['old_status'] != r['new_status'])]
if [r['id'] for r in rev] != changed:
    fails.append('revision-log rows != changed rows (%d vs %d)' % (len(rev), len(changed)))

print('articles=%d total_body_chars=%d' % (len(aud), total))
print('confirmed=%d provisional=%d' % (sum(1 for r in aud if r['new_status'] == 'manual_confirmed'),
                                       sum(1 for r in aud if r['new_status'] == 'manual_provisional')))
print('primary_changed=%d secondary_changed=%d revision_rows=%d' % (
    sum(1 for r in aud if r['old_primary'] != r['new_primary']),
    sum(1 for r in aud if r['old_secondary'] != r['new_secondary']), len(rev)))
print('FAILS: %d' % len(fails))
for f in fails:
    print('  FAIL', f)
print('NOTES: %d' % len(notes))
for n in notes:
    print('  note', n)
sys.exit(1 if fails else 0)
