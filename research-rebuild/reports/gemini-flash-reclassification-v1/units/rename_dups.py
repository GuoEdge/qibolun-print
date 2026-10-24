#!/usr/bin/env python3
"""全书单元名唯一化：每组重名保留首处，其余按内容改名；同步从 B39.tsv 去掉 971。"""
import json, shutil, time, collections
from pathlib import Path

D = Path(__file__).parent
TS = time.strftime('%Y%m%d_%H%M%S')
RENAME = {  # (册, 旧名) -> 新名
    ('B38H', '自處心性'): '持守本心',
    ('B07', '家門風波'): '家難自持',
    ('B38F', '處世分寸'): '交遊進退',
    ('B22B', '立身處世'): '商外人生',
    ('B20B', '同事相處'): '同僚攻守',
    ('B38F', '家門情愛'): '親子婚戀',
    ('B38B', '時事評議'): '寰宇百業',
    ('B38I', '時事評議'): '產業輿情',
    ('B22B', '投資理財'): '漲跌貧富',
    ('B26', '兩性對立'): '性別論戰',
    ('B38G', '時局評議'): '戰事法治',
    ('B31B', '情愛人倫'): '愛與離合',
    ('B38H', '人際情愛'): '人情往來',
    ('B38G', '格物雜識'): '雜學拾遺',
    ('B38J', '格物雜識'): '飲食器物',
    ('B38D', '待人分寸'): '禮數拿捏',
    ('B38L', '待人分寸'): '交往名聲',
    ('B38B', '修己心法'): '自救自修',
    ('B38E', '格物博聞'): '理化地氣',
    ('B38K', '格物博聞'): '天工萬象',
    ('B38E', '家門親子'): '孝養和睦',
    ('B38G', '處世應對'): '冷語應對',
    ('B38I', '處世應對'): '自證恩怨',
}

# B39.tsv 去掉 971
tsv = D / 'input' / 'B39.tsv'
lines = tsv.read_text(encoding='utf-8').splitlines()
keep = [l for l in lines if l.split('\t')[0] != '971']
if len(keep) != len(lines):
    shutil.copy2(tsv, str(tsv) + '.bak_dedup_' + TS)
    tsv.write_text('\n'.join(keep) + '\n', encoding='utf-8')
    print('B39.tsv 去掉 971')

done = set()
for (code, old), new in RENAME.items():
    p = D / 'out' / f'{code}.json'
    j = json.loads(p.read_text(encoding='utf-8'))
    hit = [u for u in j['units'] if u['name'] == old]
    assert len(hit) == 1, (code, old)
    if code not in done:
        shutil.copy2(p, str(p) + '.bak_rename_' + TS); done.add(code)
    hit[0]['name'] = new
    p.write_text(json.dumps(j, ensure_ascii=False, indent=1), encoding='utf-8')
    print(f'{code} {old} → {new}')

cnt = collections.Counter(u['name'] for p in (D / 'out').glob('*.json')
                          for u in json.loads(p.read_text(encoding='utf-8'))['units'])
dups = {k: v for k, v in cnt.items() if v > 1}
print('单元总数', sum(cnt.values()), '重名', dups or '无')
