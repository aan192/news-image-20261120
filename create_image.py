import os
import math
from PIL import Image, ImageDraw, ImageFont

# Create 1024x1024 image
width, height = 1024, 1024
image = Image.new("RGB", (width, height), color=(10, 12, 22))
draw = ImageDraw.Draw(image)

# Draw a surreal cosmic background gradient and stars
for y in range(height):
    r = int(10 + (y / height) * 15)
    g = int(12 + (y / height) * 8)
    b = int(22 + (y / height) * 25)
    draw.line([(0, y), (width, y)], fill=(r, g, b))

# Add glowing stars / nebula particles
import random
random.seed(42)
for _ in range(300):
    x = random.randint(0, width)
    y = random.randint(0, height)
    size = random.choice([1, 1, 2, 2, 3])
    brightness = random.randint(100, 255)
    color = (brightness, brightness, random.randint(220, 255))
    draw.ellipse([x, y, x + size, y + size], fill=color)

# Draw central surreal visual element: a glowing cosmic ring / monolith / data portal
center_x, center_y = width // 2, height // 2 - 40

# Outer glow circles
for r in range(320, 180, -20):
    alpha_color = (30 + (320-r)//3, 80 + (320-r)//2, 140 + (320-r)//2)
    draw.ellipse([center_x - r, center_y - r, center_x + r, center_y + r], outline=alpha_color, width=3)

# Central glowing golden monolith & data streams using RGBA overlay
image_rgba = image.convert("RGBA")
overlay = Image.new("RGBA", image.size, (0,0,0,0))
overlay_draw = ImageDraw.Draw(overlay)

# Draw glowing data charts / waves crashing
for i in range(-200, 200, 15):
    pts = []
    for x in range(center_x - 350, center_x + 350, 20):
        y = center_y + int(i + 50 * math.sin((x - center_x) * 0.01 + i * 0.1))
        pts.append((x, y))
    if len(pts) > 1:
        overlay_draw.line(pts, fill=(255, 140, 50, 100), width=2)

# Add golden monolith
overlay_draw.rectangle([center_x - 50, center_y - 120, center_x + 50, center_y + 120], fill=(255, 200, 50, 220))
# Inner dark core
overlay_draw.rectangle([center_x - 30, center_y - 100, center_x + 30, center_y + 100], fill=(15, 15, 25, 255))

image = Image.alpha_composite(image_rgba, overlay).convert("RGB")
draw = ImageDraw.Draw(image)

# Try loading fonts
try:
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
    font_subtitle = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
    font_body = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
except:
    font_title = font_subtitle = font_body = ImageFont.load_default()

# Draw Header / Date Banner at top
banner_box = [50, 40, width - 50, 140]
draw.rectangle(banner_box, fill=(15, 20, 35), outline=(60, 100, 180), width=2)
draw.text((width // 2, 65), "THURSDAY, 20 NOVEMBER 2026", fill=(255, 220, 100), font=font_title, anchor="mm")
draw.text((width // 2, 110), "WORLD NEWS, MARKETS & SPACE MILESTONES", fill=(200, 210, 230), font=font_subtitle, anchor="mm")

# Draw News Stories Card at bottom
card_box = [50, 680, width - 50, 980]
draw.rectangle(card_box, fill=(20, 25, 45), outline=(80, 120, 200), width=2)

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

# Save as entry.png
output_path = "entry.png"
image.save(output_path, "PNG", optimize=True)
print(f"Saved {output_path}, size: {os.path.getsize(output_path)} bytes")
