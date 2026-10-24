from pathlib import Path

p = Path(__file__).resolve().parents[1] / "data" / "print-topic-manual-decisions-v2.csv"
b = p.read_bytes()
old = b"09477164-b4a1-599c-8236-c54cd8b6790e,"
i = b.find(old)
if i < 0:
    raise SystemExit("target not found")
end = b.find(b"\n", i)
line = b[i:end]
line2 = line.replace(b",A09;A01;A10;A04,manual_confirmed,", b",A09;A01;A10,manual_confirmed,")
if line2 == line:
    raise SystemExit("expected field not found")
p.write_bytes(b[:i] + line2 + b[end:])
print("repaired", p)
