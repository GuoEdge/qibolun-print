import json

with open('v4_entries_for_audit.json') as f:
    entries = json.load(f)

b18 = [e for e in entries if e['slot'] == 'B18']
for idx, e in enumerate(b18, 1):
    print(f"=== [{idx}/22] B18: {e['title']} ===")
    print(f"问: {e['question']}")
    print(f"正文: {e['text']}\n")
