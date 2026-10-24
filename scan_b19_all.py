import json

with open('v4_entries_for_audit.json') as f:
    entries = json.load(f)

b19 = [e for e in entries if e['slot'] == 'B19']

for i, e in enumerate(b19, 1):
    q = e['question'].replace('\n', ' ')
    first_lines = e['text'][:250].replace('\n', ' ')
    print(f"=== [{i}/{len(b19)}] B19: 《{e['title']}》 ({e['text_len']}字) ===")
    print(f"  问: {q}")
    print(f"  首段: {first_lines}\n")
