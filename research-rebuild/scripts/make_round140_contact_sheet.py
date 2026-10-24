from pathlib import Path
from PIL import Image, ImageDraw

src = Path(__file__).resolve().parents[1] / "image-review" / "round140"
files = []
for path in sorted(src.glob("*.jpg")):
    try:
        with Image.open(path) as im: im.verify()
        files.append(path)
    except Exception:
        print(f"skip invalid image: {path}")
thumb_w, thumb_h, label_h, cols, per_sheet = 420, 300, 42, 3, 9
for sheet_no in range((len(files) + per_sheet - 1) // per_sheet):
    part = files[sheet_no * per_sheet:(sheet_no + 1) * per_sheet]
    rows = (len(part) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * thumb_w, rows * (thumb_h + label_h)), "white")
    draw = ImageDraw.Draw(sheet)
    for i, path in enumerate(part):
        with Image.open(path) as im:
            im = im.convert("RGB"); im.thumbnail((thumb_w - 12, thumb_h - 12))
            x = (i % cols) * thumb_w + (thumb_w - im.width) // 2
            y = (i // cols) * (thumb_h + label_h) + (thumb_h - im.height) // 2
            sheet.paste(im, (x, y))
        draw.text(((i % cols) * thumb_w + 4, (i // cols) * (thumb_h + label_h) + thumb_h + 4), path.name[:58], fill="black")
    out = src / f"contact-sheet-{sheet_no + 1}.jpg"; sheet.save(out, quality=92); print(out)
