import json

with open('v4_entries_for_audit.json') as f:
    entries = json.load(f)

b19 = [e for e in entries if e['slot'] == 'B19']
print(f"Total B19 entries: {len(b19)}")

# 打印每篇的详细内容
for i, e in enumerate(b19, 1):
    print(f"--- [{i}/{len(b19)}] B19: {e['title']} ---")
    print(f"Q: {e['question']}")
    print(f"LEN: {e['text_len']}")
    print(f"TEXT: {e['text']}")
    print("\n" + "="*80 + "\n")
