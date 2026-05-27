#!/usr/bin/env python3
"""
Generate the StoryTime app icon (1024x1024 PNG) in the project's aesthetic:
buttery yellow background, hand-drawn ink-navy clapperboard + sparkle.

Run: python3 scripts/make_appicon.py
"""
import math
from pathlib import Path
from PIL import Image, ImageDraw

BUTTER = (246, 239, 212, 255)   # #F6EFD4
MIST   = (216, 222, 232, 255)   # #D8DEE8
INK    = (26, 39, 68, 255)      # #1A2744

OUT_DIR = (
    Path(__file__).resolve().parent.parent
    / "StoryTime2.0" / "Preview Content"
    / "Assets.xcassets" / "AppIcon.appiconset"
)

SIZE = 1024


def wobble_line(draw, p1, p2, width, color, segments=12, jitter=4):
    """Draw a slightly imperfect line between p1 and p2."""
    pts = []
    for i in range(segments + 1):
        t = i / segments
        x = p1[0] + (p2[0] - p1[0]) * t
        y = p1[1] + (p2[1] - p1[1]) * t
        if 0 < i < segments:
            seed = (x * 12.9898 + y * 78.233)
            jx = (math.sin(seed) * 43758.5453) % 1.0 - 0.5
            jy = (math.cos(seed) * 43758.5453) % 1.0 - 0.5
            x += jx * jitter
            y += jy * jitter
        pts.append((x, y))
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i + 1]], fill=color, width=width)


def wobble_polygon(draw, points, width, color, fill=None, jitter=3, samples=14):
    """Stroke a polygon with wobbly segments (samples per side)."""
    if fill is not None:
        draw.polygon(points, fill=fill)
    for i in range(len(points)):
        p1, p2 = points[i], points[(i + 1) % len(points)]
        wobble_line(draw, p1, p2, width, color, segments=samples, jitter=jitter)


def make_icon():
    img = Image.new("RGBA", (SIZE, SIZE), BUTTER)
    d = ImageDraw.Draw(img)

    # Faint mist tile in the lower-right to give the icon depth without
    # using shadows.
    tile = [(SIZE * 0.32, SIZE * 0.30),
            (SIZE * 0.92, SIZE * 0.34),
            (SIZE * 0.88, SIZE * 0.92),
            (SIZE * 0.28, SIZE * 0.88)]
    wobble_polygon(d, tile, width=8, color=INK, fill=MIST, jitter=6, samples=18)

    # Clapperboard arm (top diagonal stripes)
    arm_pts = [
        (SIZE * 0.22, SIZE * 0.46),
        (SIZE * 0.32, SIZE * 0.22),
        (SIZE * 0.51, SIZE * 0.31),
        (SIZE * 0.41, SIZE * 0.46),
    ]
    wobble_polygon(d, arm_pts, width=10, color=INK, jitter=5, samples=14)

    arm_pts2 = [
        (SIZE * 0.51, SIZE * 0.31),
        (SIZE * 0.71, SIZE * 0.26),
        (SIZE * 0.62, SIZE * 0.46),
        (SIZE * 0.41, SIZE * 0.46),
    ]
    wobble_polygon(d, arm_pts2, width=10, color=INK, jitter=5, samples=14)

    arm_pts3 = [
        (SIZE * 0.71, SIZE * 0.26),
        (SIZE * 0.86, SIZE * 0.24),
        (SIZE * 0.80, SIZE * 0.46),
        (SIZE * 0.62, SIZE * 0.46),
    ]
    wobble_polygon(d, arm_pts3, width=10, color=INK, jitter=5, samples=14)

    # Body of the clapperboard
    body_pts = [
        (SIZE * 0.18, SIZE * 0.46),
        (SIZE * 0.84, SIZE * 0.46),
        (SIZE * 0.82, SIZE * 0.84),
        (SIZE * 0.20, SIZE * 0.84),
    ]
    wobble_polygon(d, body_pts, width=12, color=INK, jitter=6, samples=22)

    # Body horizontal lines (script lines)
    for y_frac in (0.58, 0.68, 0.78):
        wobble_line(d,
                    (SIZE * 0.28, SIZE * y_frac),
                    (SIZE * 0.74, SIZE * y_frac),
                    width=6, color=INK, segments=22, jitter=3)

    # Sparkle (top-right corner)
    cx, cy, r = SIZE * 0.84, SIZE * 0.16, SIZE * 0.06
    wobble_line(d, (cx, cy - r), (cx, cy + r), 8, INK, segments=10, jitter=2)
    wobble_line(d, (cx - r, cy), (cx + r, cy), 8, INK, segments=10, jitter=2)
    wobble_line(d, (cx - r * 0.7, cy - r * 0.7),
                   (cx + r * 0.7, cy + r * 0.7),
                   6, INK, segments=10, jitter=2)

    # Tiny secondary sparkle
    cx2, cy2, r2 = SIZE * 0.94, SIZE * 0.30, SIZE * 0.03
    wobble_line(d, (cx2, cy2 - r2), (cx2, cy2 + r2), 5, INK, segments=6, jitter=1)
    wobble_line(d, (cx2 - r2, cy2), (cx2 + r2, cy2), 5, INK, segments=6, jitter=1)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / "icon-1024.png"
    img.save(out, "PNG")
    print(f"wrote {out}")


if __name__ == "__main__":
    make_icon()
