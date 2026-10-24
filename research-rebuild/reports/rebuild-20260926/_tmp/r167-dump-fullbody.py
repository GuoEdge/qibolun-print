# -*- coding: utf-8 -*-
"""Round167 temp dump: print full text + metadata for each packet (read-only)."""
import json, io, sys

SRC = 'research-rebuild/reports/rebuild-20260926/round167/round167-fulltext.json'
OUT = 'research-rebuild/reports/rebuild-20260926/_tmp/r167-fullbody.txt'

d = json.load(open(SRC, encoding='utf-8'))
with io.open(OUT, 'w', encoding='utf-8') as f:
    for i, p in enumerate(d):
        f.write('=' * 100 + '\n')
        f.write('### [%02d] id=%s\n' % (i, p.get('id')))
        f.write('title=%s\n' % p.get('title'))
        f.write('question=%s\n' % p.get('question'))
        f.write('published_at=%s\n' % p.get('published_at'))
        f.write('body_char_count=%s (len(text)=%d)\n' % (p.get('body_char_count'), len(p.get('text') or '')))
        f.write('manual_status=%s | manual_primary=%s | manual_secondary=%s\n' % (
            p.get('manual_status'), p.get('manual_primary'), p.get('manual_secondary')))
        f.write('manual_decision_basis=%s\n' % p.get('manual_decision_basis'))
        f.write('manual_review_note=%s\n' % p.get('manual_review_note'))
        idx = p.get('index') or {}
        for k in sorted(idx.keys()):
            f.write('index.%s=%s\n' % (k, idx[k]))
        f.write('-' * 40 + ' TEXT BEGIN ' + '-' * 40 + '\n')
        f.write((p.get('text') or '') + '\n')
        f.write('-' * 40 + ' TEXT END ' + '-' * 42 + '\n\n')
print('wrote', OUT, 'articles=', len(d))
