from PIL import Image, ImageDraw, ImageFont
import os

base_path = "base.png"
if not os.path.exists(base_path):
    raise FileNotFoundError("base.png not found!")

img = Image.open(base_path).convert("RGB")
if img.size != (1024, 1024):
    img = img.resize((1024, 1024), Image.Resampling.LANCZOS)

overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
draw = ImageDraw.Draw(overlay)

try:
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
    font_subtitle = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
    font_body = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
except:
    font_title = font_subtitle = font_body = ImageFont.load_default()

width, height = 1024, 1024

banner_box = [50, 40, width - 50, 140]
draw.rounded_rectangle(banner_box, radius=10, fill=(10, 14, 28, 220), outline=(80, 140, 220, 255), width=2)
draw.text((width // 2, 68), "THURSDAY, 20 NOVEMBER 2026", fill=(255, 220, 100), font=font_title, anchor="mm")
draw.text((width // 2, 112), "WORLD NEWS, MARKETS & SPACE MILESTONES", fill=(200, 210, 240), font=font_subtitle, anchor="mm")

card_box = [50, 680, width - 50, 980]
draw.rounded_rectangle(card_box, radius=10, fill=(10, 14, 28, 230), outline=(80, 140, 220, 255), width=2)

stories = [
    "• AI Stock Rout: S&P 500 enters correction amid tech valuation sell-off.",
    "• Deep Space: NASA Voyager 1 reaches milestone 1 light-day from Earth.",
    "• Record Gaming: GTA 6 shatters entertainment history with $3.8B day one.",
    "• Geopolitics: US and Venezuela restore cooperation; Denmark secures Arctic."
]

y_text = 715
for story in stories:
    draw.text((80, y_text), story, fill=(240, 240, 250), font=font_body)
    y_text += 62

final_img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")

output_path = "entry.png"
# Save PNG with optimize and compressed levels, or resize/compress to be under 1MB while remaining PNG
final_img.save(output_path, "PNG", optimize=True, compress_level=9)
size = os.path.getsize(output_path)
print(f"Composited PNG {output_path}, size: {size} bytes")

# If still over 1MB, resize slightly or save with palette reduction
if size > 1024 * 1024:
    quantized = final_img.quantize(colors=256, method=Image.Quantize.MEDIANCUT).convert("RGB")
    quantized.save(output_path, "PNG", optimize=True, compress_level=9)
    size = os.path.getsize(output_path)
    print(f"Quantized PNG size: {size} bytes")

assert size <= 1024 * 1024, "PNG size exceeds 1 MiB!"
