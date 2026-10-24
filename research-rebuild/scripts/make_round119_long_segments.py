from pathlib import Path
from PIL import Image, ImageDraw

src = Path(__file__).resolve().parents[1] / "image-review" / "round119"
out = src / "segments"
out.mkdir(exist_ok=True)
for path in sorted(src.glob("*.jpg")):
    if path.name.startswith("contact-sheet-"):
        continue
    with Image.open(path) as im:
        if im.height <= 800:
            continue
        im = im.convert("RGB")
        for part, top in enumerate(range(0, im.height, 600), 1):
            crop = im.crop((0, top, im.width, min(top + 600, im.height)))
            scale = min(900 / crop.width, 600 / crop.height, 1.0)
            if scale < 1:
                crop = crop.resize((round(crop.width * scale), round(crop.height * scale)))
            canvas = Image.new("RGB", (crop.width, crop.height + 28), "white")
            canvas.paste(crop, (0, 28))
            ImageDraw.Draw(canvas).text((4, 5), f"{path.name} segment {part} y={top}:{min(top + 600, im.height)}", fill="black")
            canvas.save(out / f"{path.stem}-seg{part}.jpg", quality=92)
            print(out / f"{path.stem}-seg{part}.jpg")
