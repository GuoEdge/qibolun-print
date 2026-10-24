import json

with open('v4_entries_for_audit.json') as f:
    entries = json.load(f)

b19 = [e for e in entries if e['slot'] == 'B19']

for i, e in enumerate(b19[40:], 41):
    print(f"[{i}/75] ID:{e['id']} | TITLE:{e['title']}")
    print(f"  Q: {e['question']}")
    print(f"  L: {e['text_len']}")
    print(f"  T: {e['text'][:250].replace(chr(10), ' ')}")
    print("-" * 60)
