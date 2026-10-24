import json

with open('v4_entries_for_audit.json') as f:
    entries = json.load(f)

b17 = [e for e in entries if e['slot'] == 'B17']
print(f"Total B17 entries: {len(b17)}")

# 打印每篇的详细内容
for i, e in enumerate(b17, 1):
    print(f"--- [{i}/{len(b17)}] B17: {e['title']} ---")
    print(f"Q: {e['question']}")
    print(f"LEN: {e['text_len']}")
    print(f"TEXT: {e['text']}")
    print("\n" + "="*80 + "\n")
