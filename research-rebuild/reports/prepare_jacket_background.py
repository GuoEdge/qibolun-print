from PIL import Image, ImageDraw, ImageFilter, ImageOps

ROOT = "/storage/Users/currentUser/Documents/岐伯论"
SOURCE = ROOT + "/research-rebuild/assets/star_map_base.jpg"
OUTPUT = ROOT + "/research-rebuild/assets/qibo_jacket_background.png"

# Real spread: 80 mm flap + 170 mm back + 42.3 mm spine + 170 mm front + 80 mm flap.
DPI = 300
MM = DPI / 25.4
SPINE_MM = 42.3
WIDTH_MM = 80 + 170 + SPINE_MM + 170 + 80
HEIGHT_MM = 240
W = round(WIDTH_MM * MM)
H = round(HEIGHT_MM * MM)

source = Image.open(SOURCE).convert("L")
# Fit the landscape engraving to the cover height without distortion, then crop excess sides.
source = ImageOps.fit(source, (W, H), method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))
# Keep the original engraving intact in proportion, but lower its contrast so type stays legible.
white = Image.new("L", (W, H), 255)
base = Image.blend(source, white, 0.77).convert("RGB")

# Gently clear two broad text fields without adding hard-edged panels.
# Their soft transitions preserve the single continuous star-map image.
mask = Image.new("L", (W, H), 0)
md = ImageDraw.Draw(mask)
for center_mm, radius_x_mm, radius_y_mm, fill in [
    (165, 72, 77, 52),  # back-cover copy field
    (373, 75, 82, 48),  # front-cover title field
]:
    box = (
        round((center_mm - radius_x_mm) * MM),
        round((120 - radius_y_mm) * MM),
        round((center_mm + radius_x_mm) * MM),
        round((120 + radius_y_mm) * MM),
    )
    md.ellipse(box, fill=fill)
mask = mask.filter(ImageFilter.GaussianBlur(round(18 * MM)))
base = Image.composite(Image.new("RGB", (W, H), (255, 254, 251)), base, mask)

# Spine is differentiated by a quiet, translucent ink wash, retaining map detail beneath it.
spine_x0 = round(250 * MM)
spine_x1 = round((250 + SPINE_MM) * MM)
spine_overlay = Image.new("RGB", (W, H), (35, 32, 30))
spine_mask = Image.new("L", (W, H), 0)
smd = ImageDraw.Draw(spine_mask)
smd.rectangle((spine_x0, 0, spine_x1, H), fill=34)
spine_mask = spine_mask.filter(ImageFilter.GaussianBlur(round(2.2 * MM)))
base = Image.composite(spine_overlay, base, spine_mask)

# Fold lines are intentionally fine, dashed, and low-contrast for proofing.
draw = ImageDraw.Draw(base)
fold_color = (170, 165, 158)
for x_mm in (80, 250, 250 + SPINE_MM, 250 + SPINE_MM + 170):
    x = round(x_mm * MM)
    y = 0
    while y < H:
        draw.line((x, y, x, min(y + round(2 * MM), H)), fill=fold_color, width=max(1, round(0.15 * MM)))
        y += round(3.5 * MM)

base.save(OUTPUT, "PNG", dpi=(DPI, DPI), optimize=True)
print(f"Saved {OUTPUT} ({W}x{H}px, {WIDTH_MM}x{HEIGHT_MM}mm @ {DPI}dpi)")
