import json

with open('v4_entries_for_audit.json') as f:
    entries = json.load(f)

b18 = [e for e in entries if e['slot'] == 'B18']

print("="*80)
print("【B18·作息节律与病理常识】全量 22 篇实质性通读审查")
print("="*80)

# 逐篇详细打印并分析
for i, e in enumerate(b18, 1):
    print(f"\n--- 第 {i}/22 篇: 《{e['title']}》 ---")
    print(f"原问: {e['question']}")
    print(f"全文 ({e['text_len']}字):")
    print(e['text'])
    print("-" * 50)
