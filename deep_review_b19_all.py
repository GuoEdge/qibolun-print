import json

with open('v4_entries_for_audit.json') as f:
    entries = json.load(f)

b19 = [e for e in entries if e['slot'] == 'B19']

print(f"=== B19 全量 {len(b19)} 篇全文通读与主旨分析 ===")

for i, e in enumerate(b19, 1):
    print(f"--- [{i}/{len(b19)}] B19: 《{e['title']}》 ({e['text_len']}字) ---")
    print(f"原问: {e['question']}")
    print(f"全文内容:")
    print(e['text'])
    print("\n" + "="*70 + "\n")
