#!/usr/bin/env python3
"""Generate a social preview GIF for Awesome Research Data Management."""
from PIL import Image, ImageDraw, ImageFont
import math
import os

WIDTH = 640
HEIGHT = 320
PADDING = 50
CONTENT_HEIGHT = HEIGHT - 2 * PADDING  # 220px for content
NUM_FRAMES = 20
FRAME_DELAY = 100  # ms

# Colors
BG_COLOR = (13, 17, 23)
BLUE = (88, 166, 255)
PURPLE = (163, 113, 247)
PINK = (247, 120, 186)
GRAY = (139, 148, 158)
DARK_CARD = (22, 27, 34)
BORDER = (48, 54, 61)
WHITE = (255, 255, 255)


def lerp_color(c1, c2, t):
    """Linear interpolate between two RGB colors."""
    return tuple(int(a + (b - a) * t) for a, b in zip(c1, c2))


def draw_glow_circle(draw, cx, cy, r, color, alpha=0.3):
    """Draw a soft glowing circle."""
    for i in range(r, 0, -1):
        a = int(alpha * 255 * (i / r))
        c = (*color, a)
        draw.ellipse([cx - i, cy - i, cx + i, cy + i], fill=c)


def draw_text_centered(draw, y, text, font, fill):
    """Draw text centered horizontally."""
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    x = (WIDTH - tw) // 2
    draw.text((x, y), text, font=font, fill=fill)


def generate_frame(frame_num):
    """Generate a single frame of the GIF."""
    img = Image.new("RGBA", (WIDTH, HEIGHT), (*BG_COLOR, 255))
    draw = ImageDraw.Draw(img, "RGBA")

    t = frame_num / NUM_FRAMES  # 0.0 to ~1.0
    angle = t * 2 * math.pi

    # --- Animated grid ---
    grid_alpha = 15
    for y in range(0, HEIGHT, 40):
        wave = math.sin(y * 0.02 + t * 4) * 0.5 + 0.5
        a = int(grid_alpha * wave)
        draw.line([(0, y), (WIDTH, y)], fill=(*BLUE, a), width=1)
    for x in range(0, WIDTH, 60):
        wave = math.sin(x * 0.02 + t * 3) * 0.5 + 0.5
        a = int(grid_alpha * wave)
        draw.line([(x, 0), (x, HEIGHT)], fill=(*BLUE, a), width=1)

    # --- Floating nodes ---
    nodes = [
        (80, 80, BLUE, 4, 3.5),
        (200, 220, PURPLE, 3, 4.0),
        (350, 100, PINK, 5, 2.5),
        (480, 240, BLUE, 3, 4.5),
        (560, 70, PURPLE, 4, 3.0),
        (150, 160, PINK, 3, 5.0),
        (420, 180, BLUE, 3, 3.8),
        (520, 130, PURPLE, 2, 4.2),
    ]

    for nx, ny, color, r, speed in nodes:
        y_off = math.sin(angle * speed + nx * 0.01) * 15
        alpha = 0.4 + 0.3 * math.sin(angle * speed + ny * 0.01)
        draw_glow_circle(draw, nx, int(ny + y_off), r + 2, color, alpha * 0.3)
        draw.ellipse(
            [nx - r, int(ny + y_off) - r, nx + r, int(ny + y_off) + r],
            fill=(*color, int(alpha * 255)),
        )

    # --- Connecting lines ---
    node_positions = [(nx, int(ny + math.sin(angle * sp + nx * 0.01) * 15)) for nx, ny, _, _, sp in nodes]
    for i in range(len(node_positions) - 1):
        x1, y1 = node_positions[i]
        x2, y2 = node_positions[i + 1]
        la = int(30 + 20 * math.sin(angle * 2 + i))
        draw.line([(x1, y1), (x2, y2)], fill=(*BLUE, la), width=1)

    # --- Orbiting ring ---
    ring_cx, ring_cy = WIDTH // 2, HEIGHT // 2 - 10
    ring_r = 75
    num_dots = 12
    for i in range(num_dots):
        a = angle * 2 + (2 * math.pi * i / num_dots)
        dx = ring_cx + int(ring_r * math.cos(a))
        dy = ring_cy + int(ring_r * math.sin(a))
        dot_alpha = int(80 + 40 * math.sin(a * 3))
        draw.ellipse([dx - 1, dy - 1, dx + 1, dy + 1], fill=(*BLUE, dot_alpha))

    # Ring outline
    draw.ellipse(
        [ring_cx - ring_r, ring_cy - ring_r, ring_cx + ring_r, ring_cy + ring_r],
        outline=(*BLUE, 25),
        width=1,
    )

    # --- Title text ---
    try:
        font_title = ImageFont.truetype("arial.ttf", 38)
        font_sub = ImageFont.truetype("arial.ttf", 12)
        font_badge = ImageFont.truetype("arial.ttf", 11)
    except (OSError, IOError):
        try:
            font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 38)
            font_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
            font_badge = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 11)
        except (OSError, IOError):
            font_title = ImageFont.load_default()
            font_sub = ImageFont.load_default()
            font_badge = ImageFont.load_default()

    draw_text_centered(draw, 80, "AWESOME", font_sub, GRAY)
    draw_text_centered(draw, 100, "Research Data", font_title, WHITE)
    draw_text_centered(draw, 145, "Management", font_title, (*BLUE, 240))

    # Subtitle with animated dots
    subtitle_parts = ["SaaS", "Open Source", "FAIR Data", "Preservation"]
    idx = int(t * len(subtitle_parts)) % len(subtitle_parts)
    active_text = " • ".join(subtitle_parts)
    draw_text_centered(draw, 195, active_text, font_sub, GRAY)

    # --- Bottom badges ---
    badges = [
        ("8 SaaS", BLUE),
        ("22 Open Source", PURPLE),
        ("FAIR Compliant", PINK),
    ]
    badge_x = WIDTH // 2 - 160
    for text, color in badges:
        tw = draw.textlength(text, font=font_badge)
        bw = int(tw + 20)
        draw.rounded_rectangle(
            [badge_x, 220, badge_x + bw, 248],
            radius=14,
            fill=(*DARK_CARD, 200),
            outline=(*BORDER, 150),
        )
        draw.text((badge_x + 10, 226), text, font=font_badge, fill=color)
        badge_x += bw + 10

    # --- Bottom accent line ---
    line_w = 300
    line_x = (WIDTH - line_w) // 2
    line_alpha = int(100 + 80 * math.sin(angle * 2))
    draw.rounded_rectangle(
        [line_x, 260, line_x + line_w, 262],
        radius=1,
        fill=(*BLUE, line_alpha),
    )

    return img.convert("RGB")


# Generate frames
frames = []
for i in range(NUM_FRAMES):
    frame = generate_frame(i)
    # Quantize to reduce size
    frame = frame.quantize(colors=128, method=Image.Quantize.MEDIANCUT)
    frames.append(frame)
    print(f"Frame {i + 1}/{NUM_FRAMES} done")

# Save GIF
output_path = os.path.join(os.path.dirname(__file__), "social-preview.gif")
frames[0].save(
    output_path,
    save_all=True,
    append_images=frames[1:],
    duration=FRAME_DELAY,
    loop=0,
    optimize=True,
)

# Check file size
file_size = os.path.getsize(output_path)
print(f"\nGIF saved: {output_path}")
print(f"Size: {file_size / 1024:.1f} KB ({file_size / (1024 * 1024):.2f} MB)")
if file_size > 1024 * 1024:
    print("WARNING: File exceeds 1MB limit!")
else:
    print("OK: File is under 1MB limit")
