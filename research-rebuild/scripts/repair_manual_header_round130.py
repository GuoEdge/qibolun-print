from pathlib import Path

path = Path(__file__).resolve().parents[1] / "data/print-topic-manual-decisions-v2.csv"
header = "id,title,primary_print_topic_code,secondary_print_topic_codes,classification_status,decision_basis,review_note,reviewer,reviewed_at\n"
data = path.read_text(encoding="utf-8-sig")
if not data.startswith("id,title,primary_print_topic_code,"):
    path.write_text(header + data, encoding="utf-8-sig")
print({"repaired": True, "lines": len(path.read_text(encoding="utf-8-sig").splitlines())})
