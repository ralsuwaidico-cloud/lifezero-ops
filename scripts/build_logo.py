#!/usr/bin/env python3
"""Draw the LIFE ZERO mark and export every size an app icon needs.

THE MARK. A zero with a line through it. The line is flat, because the company
is at zero, and it lifts into one beat on the right — the first sale it has not
had yet. It is a graph that has not started, which is the honest shape of this
business today and the exact thing the whole organization exists to change.

Drawn with primitives rather than traced from anything. No third-party artwork.

Icons are exported FULL-BLEED and square with no rounded corners and no
transparency: iOS applies its own mask, and a pre-rounded icon ends up with
double corners. A separate rounded version is exported for anywhere that does
not mask.
"""

import io
import os

from PIL import Image, ImageDraw

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(REPO, "brand")

NAVY_TOP = (20, 30, 54)
NAVY_BOT = (9, 14, 28)
GOLD = (232, 184, 75)
GREEN = (74, 222, 128)

SS = 4  # supersample factor; drawn big, then reduced, so edges stay clean


def draw(size, rounded=False):
    S = size * SS
    img = Image.new("RGB", (S, S), NAVY_BOT)
    d = ImageDraw.Draw(img)

    # background: a quiet vertical gradient so the tile is not a flat block
    for y in range(S):
        t = y / max(1, S - 1)
        d.line([(0, y), (S, y)], fill=(
            int(NAVY_TOP[0] + (NAVY_BOT[0] - NAVY_TOP[0]) * t),
            int(NAVY_TOP[1] + (NAVY_BOT[1] - NAVY_TOP[1]) * t),
            int(NAVY_TOP[2] + (NAVY_BOT[2] - NAVY_TOP[2]) * t)))

    cx = cy = S / 2
    r = S * 0.262          # ring radius (centre of the stroke)
    w = S * 0.115          # ring thickness -- heavy, so it survives at 32px
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=GOLD, width=int(round(w)))

    # A flat line that finally turns up and leaves the zero. It starts inside
    # the ring, runs flat — which is where this company is — and breaks upward
    # through the top right. It deliberately does NOT run straight across: a
    # horizontal bar through a circle reads as a prohibition sign at 32px.
    lw = int(round(S * 0.070))
    y0 = cy + S * 0.055
    pts = [(cx - r * 0.62, y0),
           (cx + r * 0.05, y0),
           (S * 0.885, S * 0.212)]
    d.line(pts, fill=GREEN, width=lw, joint="curve")
    d.ellipse([cx - r * 0.62 - lw / 2, y0 - lw / 2,
               cx - r * 0.62 + lw / 2, y0 + lw / 2], fill=GREEN)
    # a solid head on the rising end, so it terminates instead of trailing off
    hx, hy, hs = S * 0.885, S * 0.212, S * 0.072
    d.polygon([(hx + hs * 0.62, hy - hs * 0.52), (hx - hs * 0.72, hy - hs * 0.30),
               (hx - hs * 0.10, hy + hs * 0.78)], fill=GREEN)

    img = img.resize((size, size), Image.LANCZOS)

    if rounded:
        rad = int(size * 0.225)
        mask = Image.new("L", (size * 4, size * 4), 0)
        ImageDraw.Draw(mask).rounded_rectangle(
            [0, 0, size * 4 - 1, size * 4 - 1], radius=rad * 4, fill=255)
        mask = mask.resize((size, size), Image.LANCZOS)
        out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        out.paste(img, (0, 0), mask)
        return out
    return img


def main():
    os.makedirs(OUT, exist_ok=True)
    made = []
    # full-bleed squares: iOS masks these itself
    for s in (32, 48, 64, 120, 152, 167, 180, 192, 256, 512, 1024):
        p = os.path.join(OUT, "icon-%d.png" % s)
        draw(s).save(p, "PNG", optimize=True)
        made.append((os.path.basename(p), os.path.getsize(p)))
    # rounded, for surfaces that do not mask
    for s in (180, 512, 1024):
        p = os.path.join(OUT, "icon-rounded-%d.png" % s)
        draw(s, rounded=True).save(p, "PNG", optimize=True)
        made.append((os.path.basename(p), os.path.getsize(p)))

    # a contact sheet, to judge the mark at the sizes it will actually be seen
    sheet = Image.new("RGB", (620, 230), (24, 28, 38))
    x = 20
    for s in (32, 48, 64, 120, 180):
        sheet.paste(draw(s), (x, 40 + (180 - s) // 2))
        x += s + 24
    sheet.save(os.path.join(OUT, "contact-sheet.png"), "PNG")

    for n, b in made:
        print("  %-24s %6.1f KB" % (n, b / 1024.0))
    print("%d icons + contact sheet in brand/" % len(made))


if __name__ == "__main__":
    main()
