from pathlib import Path
from PIL import Image, ImageDraw

src = Path(__file__).resolve().parents[1] / "image-review" / "round118"
files = sorted(src.glob("*.jpg"))
thumb_w, thumb_h, label_h, cols = 260, 190, 30, 5
rows = (len(files) + cols - 1) // cols
sheet = Image.new("RGB", (cols * thumb_w, rows * (thumb_h + label_h)), "white")
draw = ImageDraw.Draw(sheet)
for i, path in enumerate(files):
    with Image.open(path) as im:
        im = im.convert("RGB")
        im.thumbnail((thumb_w - 8, thumb_h - 8))
        x = (i % cols) * thumb_w + (thumb_w - im.width) // 2
        y = (i // cols) * (thumb_h + label_h) + (thumb_h - im.height) // 2
        sheet.paste(im, (x, y))
    draw.text(((i % cols) * thumb_w + 4, (i // cols) * (thumb_h + label_h) + thumb_h + 4), path.name[:34], fill="black")
sheet.save(src / "contact-sheet.jpg", quality=90)
print(src / "contact-sheet.jpg")
