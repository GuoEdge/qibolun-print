import json,sys
p='research-rebuild/reports/rebuild-20260926/round171/round171-fulltext.json'
d=json.load(open(p,encoding='utf-8'))
idx=int(sys.argv[1]); start=int(sys.argv[2]); end=int(sys.argv[3])
a=d[idx]
lines=a['text'].split('\n')
print(f"### {a['title']} | {a['id']} | total_lines={len(lines)} | body_char_count={a['body_char_count']}")
for n in range(start,min(end,len(lines))):
    if lines[n].strip():
        print(f"[{n+1}] {lines[n]}")
