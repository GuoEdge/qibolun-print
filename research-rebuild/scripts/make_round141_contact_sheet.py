from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[2]
source = ROOT / "research-rebuild" / "image-review" / "round141"
files = []
for path in sorted(source.glob("*.jpg")):
    try:
        with Image.open(path) as image:
            image.verify()
        files.append(path)
    except Exception:
        print(f"skip invalid image: {path}")

thumb_w, thumb_h, label_h, columns, per_sheet = 420, 300, 42, 3, 9
for sheet_number in range((len(files) + per_sheet - 1) // per_sheet):
    part = files[sheet_number * per_sheet:(sheet_number + 1) * per_sheet]
    rows = (len(part) + columns - 1) // columns
    sheet = Image.new("RGB", (columns * thumb_w, rows * (thumb_h + label_h)), "white")
    draw = ImageDraw.Draw(sheet)
    for index, path in enumerate(part):
        with Image.open(path) as image:
            image = image.convert("RGB")
            image.thumbnail((thumb_w - 12, thumb_h - 12))
            x = (index % columns) * thumb_w + (thumb_w - image.width) // 2
            y = (index // columns) * (thumb_h + label_h) + (thumb_h - image.height) // 2
            sheet.paste(image, (x, y))
        draw.text(
            ((index % columns) * thumb_w + 4,
             (index // columns) * (thumb_h + label_h) + thumb_h + 4),
            path.name[:58],
            fill="black",
        )
    output = source / f"contact-sheet-{sheet_number + 1}.jpg"
    sheet.save(output, quality=92)
    print(output)
