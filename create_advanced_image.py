import os
import math
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

width, height = 1024, 1024
image = Image.new("RGB", (width, height), color=(5, 8, 18))
draw = ImageDraw.Draw(image)

# 1. Detailed cosmic background gradient & nebula clouds
for y in range(height):
    r = int(5 + (y / height) * 12)
    g = int(8 + (y / height) * 10)
    b = int(18 + (y / height) * 35)
    draw.line([(0, y), (width, y)], fill=(r, g, b))

# Add procedural nebula dust / cloud layers using ellipses with blur
nebula = Image.new("RGBA", (width, height), (0, 0, 0, 0))
neb_draw = ImageDraw.Draw(nebula)
random.seed(1337)
for _ in range(40):
    nx = random.randint(-100, width + 100)
    ny = random.randint(-100, height + 100)
    nr = random.randint(150, 350)
    col = random.choice([
        (100, 40, 160, 25),  # purple nebula
        (30, 90, 180, 25),   # blue nebula
        (180, 80, 40, 20),   # golden/orange nebula
    ])
    neb_draw.ellipse([nx - nr, ny - nr, nx + nr, ny + nr], fill=col)

nebula = nebula.filter(ImageFilter.GaussianBlur(50))
image.paste(Image.alpha_composite(image.convert("RGBA"), nebula).convert("RGB"))
draw = ImageDraw.Draw(image)

# 2. Rich Starry field
for _ in range(600):
    x = random.randint(0, width)
    y = random.randint(0, height)
    size = random.choice([1, 1, 1, 2, 2, 3])
    brightness = random.randint(120, 255)
    # Give some stars a slight blue or golden tint
    if random.random() < 0.2:
        st_col = (255, 220, 150)
    elif random.random() < 0.4:
        st_col = (180, 220, 255)
    else:
        st_col = (brightness, brightness, brightness)
    draw.ellipse([x, y, x + size, y + size], fill=st_col)

# 3. Planet Earth curvature at the bottom
earth_overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
eo_draw = ImageDraw.Draw(earth_overlay)
# Earth sphere center far below canvas
earth_center_x = width // 2
earth_center_y = height + 1200
earth_radius = 1400
eo_draw.ellipse([
    earth_center_x - earth_radius, earth_center_y - earth_radius,
    earth_center_x + earth_radius, earth_center_y + earth_radius
], fill=(20, 50, 110, 255))

# Atmosphere glow rim
atmosphere = Image.new("RGBA", (width, height), (0, 0, 0, 0))
at_draw = ImageDraw.Draw(atmosphere)
at_draw.ellipse([
    earth_center_x - earth_radius - 15, earth_center_y - earth_radius - 15,
    earth_center_x + earth_radius + 15, earth_center_y + earth_radius + 15
], outline=(80, 180, 255, 180), width=8)
atmosphere = atmosphere.filter(ImageFilter.GaussianBlur(10))

image = Image.alpha_composite(image.convert("RGBA"), earth_overlay).convert("RGB")
image = Image.alpha_composite(image.convert("RGBA"), atmosphere).convert("RGB")
draw = ImageDraw.Draw(image)

# 4. Aurora market charts across the night sky
aurora_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
au_draw = ImageDraw.Draw(aurora_layer)
for wave_idx in range(5):
    pts = []
    base_y = 350 + wave_idx * 50
    for x in range(0, width + 10, 15):
        y = base_y + int(40 * math.sin(x * 0.008 + wave_idx * 1.2) + 20 * math.cos(x * 0.02 - wave_idx))
        pts.append((x, y))
    # Draw glowing ribbon
    full_pts = pts + [(width, height), (0, height)]
    au_draw.polygon(full_pts, fill=(30, 220, 140, 12 + wave_idx * 4))

aurora_layer = aurora_layer.filter(ImageFilter.GaussianBlur(25))
image = Image.alpha_composite(image.convert("RGBA"), aurora_layer).convert("RGB")
draw = ImageDraw.Draw(image)

# 5. Glowing golden monolith / cosmic gateway in the center
center_x, center_y = width // 2, height // 2 - 20
# Gateway outer glow ring
for r in range(280, 160, -15):
    glow_col = (255, int(180 + (280-r)*0.2), int(50 + (280-r)*0.5), int(30 + (280-r)*0.5))
    # We can draw circles on an RGBA overlay
    pass

# Monolith structure
monolith_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
m_draw = ImageDraw.Draw(monolith_layer)
# Golden pillar / monolith
m_draw.rectangle([center_x - 55, center_y - 180, center_x + 55, center_y + 180], fill=(255, 210, 70, 240))
# Inner dark rift portal
m_draw.rectangle([center_x - 35, center_y - 160, center_x + 35, center_y + 160], fill=(10, 15, 30, 255))
# Glowing rune lines inside portal
for py in range(center_y - 140, center_y + 140, 20):
    m_draw.line([(center_x - 25, py), (center_x + 25, py)], fill=(255, 150, 50, 180), width=2)

monolith_layer = monolith_layer.filter(ImageFilter.GaussianBlur(1))
image = Image.alpha_composite(image.convert("RGBA"), monolith_layer).convert("RGB")
draw = ImageDraw.Draw(image)

# 6. Typography & UI Cards (Header & News Stories)
try:
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
    font_subtitle = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
    font_body = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
except:
    font_title = font_subtitle = font_body = ImageFont.load_default()

# Header Banner
banner_box = [50, 40, width - 50, 140]
draw.rectangle(banner_box, fill=(10, 14, 28, 230), outline=(80, 140, 220), width=2)
draw.text((width // 2, 65), "THURSDAY, 20 NOVEMBER 2026", fill=(255, 220, 100), font=font_title, anchor="mm")
draw.text((width // 2, 110), "WORLD NEWS, MARKETS & SPACE MILESTONES", fill=(200, 210, 240), font=font_subtitle, anchor="mm")

# News Stories Card
card_box = [50, 680, width - 50, 980]
draw.rectangle(card_box, fill=(10, 14, 28, 240), outline=(80, 140, 220), width=2)

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
