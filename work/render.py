#!/usr/bin/env python3
"""Render GLOBAL HERALD - Saturday 21 November 2026 front page (1024x1024).

Fresh artwork drawn from scratch with PIL primitives + real fonts.
Stories are the day's news as first reported 21 Nov 2026 (see README).
No AI image generation: every letter is real, legible text.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (246, 239, 219)
PAPER2 = (255, 253, 244)
INK = (25, 23, 19)
RED = (176, 42, 32)
NAVY = (31, 58, 95)
TEAL = (15, 110, 110)
GREEN = (46, 110, 58)
SLATE = (70, 80, 95)
MAROON = (128, 32, 48)
ORANGE = (196, 96, 20)
GOLD = (184, 134, 30)
SEA = (207, 224, 232)
LAND = (185, 198, 155)
LAND_LINE = (125, 143, 95)
RULE = (201, 191, 165)

FDIR = "/usr/share/fonts/truetype/noto/"


def font(name, size):
    try:
        return ImageFont.truetype(FDIR + name, size)
    except OSError:
        return ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", size)


SERIF_BLACK = lambda s: font("NotoSerif-Black.ttf", s)
SERIF_BOLD = lambda s: font("NotoSerif-Bold.ttf", s)
SERIF = lambda s: font("NotoSerif-Regular.ttf", s)
SERIF_IT = lambda s: font("NotoSerif-Italic.ttf", s)
SANS_BOLD = lambda s: font("NotoSans-Bold.ttf", s)
SANS = lambda s: font("NotoSans-Regular.ttf", s)


def wrap(draw, text, fnt, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= width:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_c(draw, cx, y, s, fnt, fill=INK):
    draw.text((cx - draw.textlength(s, font=fnt) / 2, y), s, font=fnt, fill=fill)


def star(draw, cx, cy, r, fill):
    import math
    pts = []
    for i in range(10):
        ang = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.45
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    draw.polygon(pts, fill=fill, outline=(255, 255, 255))


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---- outer double border -------------------------------------------------
d.rectangle([14, 14, W - 15, H - 15], outline=INK, width=2)
d.rectangle([20, 20, W - 21, H - 21], outline=RULE, width=1)

# ---- masthead ------------------------------------------------------------
text_c(d, 512, 30, "T H E   W O R L D   I N   O N E   P A G E", SANS_BOLD(15), fill=SLATE)
d.line([90, 56, 300, 56], fill=RULE, width=1)
d.line([724, 56, 934, 56], fill=RULE, width=1)
text_c(d, 512, 54, "GLOBAL HERALD", SERIF_BLACK(84))
text_c(d, 512, 150, "SATURDAY,  21 NOVEMBER 2026    •    IN FULL COLOUR    •    FREE",
       SANS_BOLD(17))
d.line([28, 182, 996, 182], fill=INK, width=4)
d.line([28, 188, 996, 188], fill=INK, width=1)

# ---- lead story: Peru quake ----------------------------------------------
d.text((28, 202), "PERU  •  SOUTH AMERICA", font=SANS_BOLD(20), fill=RED)
d.text((28, 232), "EARTH SHAKES", font=SERIF_BLACK(72), fill=INK)
d.text((28, 306), "PERU", font=SERIF_BLACK(72), fill=INK)
d.line([28, 392, 120, 392], fill=RED, width=4)
for i, ln in enumerate(wrap(d, "Magnitude 6.8 quake strikes Junín; tremors felt 320 km away in Lima.",
                            SERIF_IT(24), 590)):
    d.text((28, 406 + i * 32), ln, font=SERIF_IT(24), fill=INK)
body = ("The quake struck the Andean region of Junín, shaking homes across "
        "central Peru, with tremors felt in the capital, Lima, around "
        "320 km away.")
for i, ln in enumerate(wrap(d, body, SERIF(17), 590)):
    d.text((28, 478 - 8 + i * 23), ln, font=SERIF(17), fill=(60, 56, 48))

# lead illustration: quake in the Andes (flat colour panel)
px0, py0, px1, py1 = 644, 202, 996, 540
d.rectangle([px0, py0, px1, py1], outline=INK, width=2)
d.rectangle([px0 + 2, py0 + 2, px1 - 2, py1 - 2], fill=(242, 193, 78))
d.ellipse([px1 - 90, py0 + 18, px1 - 30, py0 + 78], fill=(250, 226, 140),
          outline=(230, 180, 60), width=2)
# mountains
d.polygon([(px0 + 2, py1 - 90), (px0 + 90, py1 - 250), (px0 + 180, py1 - 90)],
          fill=(122, 82, 48))
d.polygon([(px0 + 70, py1 - 222), (px0 + 90, py1 - 250), (px0 + 112, py1 - 220),
           (px0 + 100, py1 - 208), (px0 + 80, py1 - 212)], fill=(255, 250, 240))
d.polygon([(px0 + 120, py1 - 90), (px0 + 230, py1 - 285), (px0 + 330, py1 - 90)],
          fill=(107, 68, 35))
d.polygon([(px0 + 210, py1 - 258), (px0 + 230, py1 - 285), (px0 + 252, py1 - 256),
           (px0 + 240, py1 - 244), (px0 + 222, py1 - 248)], fill=(255, 250, 240))
d.polygon([(px0 + 250, py1 - 90), (px0 + 300, py1 - 180), (px0 + 350, py1 - 90)],
          fill=(138, 107, 69))
# ground + crack
d.rectangle([px0 + 2, py1 - 90, px1 - 2, py1 - 2], fill=(176, 138, 90))
crack = [(px0 + 60, py1 - 90), (px0 + 90, py1 - 55), (px0 + 70, py1 - 30),
         (px0 + 110, py1 - 2), (px0 + 130, py1 - 30), (px0 + 120, py1 - 60),
         (px0 + 150, py1 - 90)]
d.polygon(crack, fill=(60, 40, 24))
# tilting houses
for hx, tilt in ((px0 + 180, -8), (px0 + 250, 10)):
    d.rectangle([hx, py1 - 130, hx + 52, py1 - 92], fill=(214, 96, 60),
                outline=INK, width=2)
    d.polygon([(hx - 4, py1 - 130), (hx + 26, py1 - 152 + tilt), (hx + 56, py1 - 130)],
              fill=(176, 42, 32), outline=INK)
    d.rectangle([hx + 20, py1 - 112, hx + 34, py1 - 92], fill=(60, 40, 24))
# dust puffs
for cx, cy, r in ((px0 + 60, py1 - 110, 16), (px0 + 95, py1 - 100, 12),
                  (px0 + 320, py1 - 120, 14)):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(238, 226, 200),
              outline=(200, 180, 140))
d.text((px0 + 10, py1 - 34), "JUNÍN, PERU", font=SANS_BOLD(15), fill=(255, 255, 255))
# magnitude badge, top-left of the panel
d.ellipse([px0 + 14, py0 + 14, px0 + 74, py0 + 74], fill=RED, outline=(255, 255, 255), width=2)
text_c(d, px0 + 44, py0 + 26, "M 6.8", SANS_BOLD(19), fill=(255, 255, 255))

# ---- world map band -------------------------------------------------------
d.text((28, 556), "THE WORLD TODAY", font=SANS_BOLD(18), fill=INK)
hdr = "LEAD  •  1, 2, 4, 5 PINNED BELOW"
hx = 996 - d.textlength(hdr, font=SANS_BOLD(14))
star(d, hx - 14, 568, 9, RED)
d.text((hx, 560), hdr, font=SANS_BOLD(14), fill=SLATE)
mx0, my0, mx1, my1 = 28, 584, 996, 736
d.rectangle([mx0, my0, mx1, my1], fill=SEA, outline=INK, width=2)


def proj(lon, lat):
    return (mx0 + (lon + 170) / 360 * (mx1 - mx0),
            my0 + (75 - lat) / 130 * (my1 - my0))


CONTINENTS = [
    # North America
    [(-168, 66), (-140, 70), (-125, 72), (-110, 73), (-95, 80), (-85, 70),
     (-75, 72), (-65, 60), (-55, 52), (-60, 45), (-70, 42), (-75, 35),
     (-80, 32), (-85, 30), (-90, 21), (-95, 19), (-105, 20), (-110, 23),
     (-120, 34), (-125, 40), (-125, 49), (-140, 60), (-155, 58), (-165, 60)],
    # Greenland
    [(-58, 64), (-45, 60), (-40, 65), (-30, 68), (-22, 70), (-30, 74),
     (-50, 76), (-60, 74)],
    # South America
    [(-80, 10), (-75, 7), (-70, 12), (-60, 8), (-52, 5), (-50, 0), (-42, -5),
     (-35, -8), (-40, -20), (-48, -28), (-55, -35), (-65, -41), (-70, -50),
     (-73, -54), (-70, -40), (-72, -20), (-78, -10)],
    # Africa
    [(-17, 15), (-10, 30), (0, 36), (10, 37), (20, 32), (30, 31), (35, 28),
     (43, 12), (51, 11), (48, 2), (40, -5), (40, -15), (35, -25), (28, -33),
     (20, -35), (15, -27), (12, -18), (9, -1), (9, 4), (-8, 5), (-15, 12)],
    # Eurasia
    [(-10, 36), (-9, 43), (-2, 49), (3, 51), (8, 57), (12, 56), (18, 56),
     (21, 59), (25, 60), (30, 62), (35, 66), (45, 68), (60, 69), (70, 72),
     (80, 73), (100, 76), (120, 73), (140, 72), (160, 70), (178, 66),
     (170, 60), (162, 56), (158, 52), (142, 50), (140, 40), (135, 35),
     (130, 33), (127, 35), (122, 30), (120, 25), (110, 20), (108, 12),
     (105, 9), (100, 8), (98, 12), (95, 16), (92, 21), (88, 22), (85, 19),
     (80, 15), (78, 8), (76, 10), (72, 20), (66, 25), (62, 25), (58, 26),
     (56, 27), (52, 28), (50, 30), (48, 30), (44, 29), (40, 32), (36, 36),
     (30, 36), (27, 37), (23, 36), (19, 40), (15, 44), (12, 44), (8, 44),
     (3, 43), (0, 40), (-2, 37), (-6, 36), (-9, 37)],
    # Australia
    [(113, -22), (114, -30), (115, -35), (120, -34), (129, -32), (132, -32),
     (135, -35), (137, -35), (140, -38), (142, -39), (147, -39), (150, -37),
     (153, -32), (153, -27), (150, -23), (146, -19), (142, -15), (142, -11),
     (137, -12), (135, -15), (132, -12), (130, -13), (126, -14), (122, -17),
     (118, -20)],
    # Japan
    [(130, 31), (133, 34), (137, 35), (140, 38), (141, 42), (143, 43),
     (145, 44), (142, 42), (140, 36), (136, 33), (132, 33)],
    # Britain
    [(-5, 50), (-3, 53), (-5, 56), (-3, 58), (-1, 57), (0, 53), (1, 51)],
]
for poly in CONTINENTS:
    d.polygon([proj(lon, lat) for lon, lat in poly], fill=LAND, outline=LAND_LINE)


def pin(lon, lat, label, is_star=False, lx=0, ly=0):
    x, y = proj(lon, lat)
    if is_star:
        star(d, x, y, 15, RED)
    else:
        d.ellipse([x - 12, y - 12, x + 12, y + 12], fill=RED, outline=(255, 255, 255), width=2)
        text_c(d, x, y - 9, label, SANS_BOLD(14), fill=(255, 255, 255))
    if lx or ly:
        d.line([x, y, x + lx, y + ly], fill=INK, width=1)
        d.text((x + lx + (4 if lx >= 0 else -4), y + ly - 8), label if is_star else "",
               font=SANS_BOLD(13), fill=INK)


pin(-75, -10, "", is_star=True)
pin(116, 40, "1")
pin(86, 20, "2")
pin(-74, 41, "4")
pin(175, -41, "5")
# place names beside pins
d.text((proj(-75, -10)[0] + 18, proj(-75, -10)[1] - 8), "PERU", font=SANS_BOLD(13), fill=INK)
d.text((proj(116, 40)[0] - 62, proj(116, 40)[1] - 26), "BEIJING 1", font=SANS_BOLD(13), fill=INK)
d.text((proj(86, 20)[0] - 8, proj(86, 20)[1] + 16), "ODISHA 2", font=SANS_BOLD(13), fill=INK)
d.text((proj(-74, 41)[0] + 16, proj(-74, 41)[1] - 8), "NEW YORK 4", font=SANS_BOLD(13), fill=INK)
d.text((proj(175, -41)[0] - 108, proj(175, -41)[1] - 8), "WELLINGTON 5", font=SANS_BOLD(13), fill=INK)

# ---- six story cards ------------------------------------------------------
CARDS = [
    (1, NAVY, "SUMMIT, NO DEAL",
     "Trump, Xi and Putin pledge cooperation — but no breakthroughs.", "flags"),
    (2, TEAL, "CYCLONE HITS ODISHA",
     "Akvan makes landfall with strong winds and heavy rain.", "spiral"),
    (3, GREEN, "NSE GOES FIFTH",
     "India's exchange passes Nasdaq as foreign inflows hit a record.", "chart"),
    (4, SLATE, "RIKERS TO CLOSE 2032",
     "New York's mayor sets a new date to shut the jail complex.", "bars"),
    (5, MAROON, "RAHUL MAKES HISTORY",
     "A Wellington century — first Indian opener with centuries in all SENA countries.", "bat"),
    (6, ORANGE, "NEPAL PM TO DELHI",
     "Balendra Shah's first foreign trip: India, 22–23 November.", "peaks"),
]


def icon(kind, x, y, col):
    if kind == "flags":
        for i, c in enumerate((NAVY, RED, GOLD)):
            d.line([x + 8 + i * 11, y + 4, x + 8 + i * 11, y + 32], fill=INK, width=2)
            d.polygon([(x + 8 + i * 11, y + 4), (x + 20 + i * 11, y + 9),
                       (x + 8 + i * 11, y + 14)], fill=c)
    elif kind == "spiral":
        for r in (5, 9, 13):
            d.arc([x + 17 - r, y + 17 - r, x + 17 + r, y + 17 + r],
                  start=20, end=300, fill=col, width=3)
    elif kind == "chart":
        pts = [(x + 3, y + 26), (x + 12, y + 20), (x + 20, y + 22), (x + 30, y + 8)]
        d.line(pts, fill=col, width=3)
        d.polygon([(x + 30, y + 8), (x + 24, y + 8), (x + 30, y + 14)], fill=col)
        for bx in (4, 13, 22):
            d.rectangle([x + bx, y + 30, x + bx + 5, y + 33], fill=col)
    elif kind == "bars":
        d.rectangle([x + 4, y + 4, x + 30, y + 30], outline=INK, width=2)
        for bx in (10, 16, 22):
            d.line([x + bx, y + 4, x + bx, y + 30], fill=INK, width=2)
    elif kind == "bat":
        d.line([x + 8, y + 28, x + 26, y + 8], fill=(150, 110, 60), width=6)
        d.line([x + 26, y + 8, x + 31, y + 3], fill=INK, width=3)
        d.ellipse([x + 4, y + 4, x + 12, y + 12], fill=RED, outline=INK)
    elif kind == "peaks":
        d.polygon([(x + 2, y + 30), (x + 12, y + 12), (x + 22, y + 30)], fill=col)
        d.polygon([(x + 14, y + 30), (x + 24, y + 16), (x + 33, y + 30)], fill=(150, 90, 40))
        d.ellipse([x + 24, y + 2, x + 32, y + 10], fill=GOLD)


for i, (num, col, head, dek, kind) in enumerate(CARDS):
    cx = 28 + (i % 3) * 326
    cy = 744 + (i // 3) * 120
    cw, ch = 314, 112
    d.rectangle([cx, cy, cx + cw, cy + ch], fill=PAPER2, outline=(170, 160, 135), width=1)
    d.rectangle([cx, cy, cx + cw, cy + 6], fill=col)
    d.ellipse([cx + 10, cy + 16, cx + 34, cy + 40], fill=RED)
    text_c(d, cx + 22, cy + 19, str(num), SANS_BOLD(15), fill=(255, 255, 255))
    icon(kind, cx + cw - 44, cy + 12, col)
    hl = wrap(d, head, SANS_BOLD(20), cw - 96)
    for j, ln in enumerate(hl[:2]):
        d.text((cx + 42, cy + 14 + j * 24), ln, font=SANS_BOLD(20), fill=INK)
    dl = wrap(d, dek, SERIF(14), cw - 20)
    for j, ln in enumerate(dl[:2]):
        d.text((cx + 10, cy + 66 + j * 19), ln, font=SERIF(14), fill=(60, 56, 48))

# ---- footer ---------------------------------------------------------------
d.line([28, 984, 996, 984], fill=RULE, width=1)
text_c(d, 512, 990, "GLOBAL HERALD  •  Saturday, 21 November 2026  •  Stories as first reported on 21 November 2026",
       SANS(12), fill=SLATE)

img.save("/home/hatch/workspace/makefun/news-image-20261121/entry.png", optimize=True)
print("saved")
