from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1200, 630
img = Image.new("RGB", (W, H))
draw = ImageDraw.Draw(img)

# gradient background
for y in range(H):
    r = int(109 + (37 - 109) * y / H)
    g = int(40 + (99 - 40) * y / H)
    b = int(217 + (233 - 217) * y / H)
    draw.line([(0, y), (W, y)], fill=(r, g, b))

# load wyvern logo
logo_path = "/Users/alex/GIT/GitHub/wyvernlang/wyvernlang.github.io/images/wyvern-logo.png"
logo = Image.open(logo_path).convert("RGBA")
logo_size = 180
logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

# center logo above text
logo_x = (W - logo_size) // 2
logo_y = 80
img.paste(logo, (logo_x, logo_y), logo)

# fonts
try:
    font_title = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 72)
    font_sub = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 28)
    font_tag = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 22)
    font_url = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 20)
except Exception:
    font_title = ImageFont.load_default()
    font_sub = font_title
    font_tag = font_title
    font_url = font_title

# Title
title = "Wyvern"
bbox = draw.textbbox((0, 0), title, font=font_title)
tw = bbox[2] - bbox[0]
draw.text(((W - tw) // 2, 280), title, fill=(255, 255, 255), font=font_title)

# Subtitle
sub = "Programming Language"
bbox = draw.textbbox((0, 0), sub, font=font_sub)
sw = bbox[2] - bbox[0]
draw.text(((W - sw) // 2, 365), sub, fill=(230, 230, 255), font=font_sub)

# Tagline
tag1 = "Type-specific languages  |  Capability-safe modules  |  High assurance"
bbox = draw.textbbox((0, 0), tag1, font=font_tag)
t1w = bbox[2] - bbox[0]
draw.text(((W - t1w) // 2, 420), tag1, fill=(200, 210, 255), font=font_tag)

# URL
url = "wyvernlang.github.io"
bbox = draw.textbbox((0, 0), url, font=font_url)
uw = bbox[2] - bbox[0]
draw.text(((W - uw) // 2, 540), url, fill=(180, 190, 220), font=font_url)

# Bottom accent bar
draw.rectangle([0, H - 6, W, H], fill=(255, 255, 255, 40))

out = "/Users/alex/GIT/GitHub/wyvernlang/wyvernlang.github.io/images/og-image.png"
img.save(out, "PNG")
print(f"OG image saved: {os.path.getsize(out)} bytes")
