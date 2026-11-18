#!/usr/bin/env python3
"""Draw the front page for Wednesday 18 November 2026 with PIL.

One square page, 1024x1024, classic newspaper layout: masthead, a lead
story on the Shenzhen APEC summit, two secondary stories (Gulf strikes,
Kerch Bridge) and a briefs column. All headlines verified against
multiple news sources on the day.
"""

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 243, 233)
INK = (18, 18, 18)
ACCENT = (146, 22, 22)
RULE = (60, 60, 60)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, width, leading, fill=INK):
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def headline(draw, x, y, text, fnt, width, leading):
    return para(draw, x, y, text, fnt, width, leading)


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

M = 44  # margin
CW = W - 2 * M

# ---- Masthead -------------------------------------------------------------
d.text((M, 22), "EST. 2026 · ONE PAGE, THE WHOLE PLANET", font=font(SANS_B, 17), fill=RULE)
f_title = font(SERIF_B, 66)
title = "THE WORLD IN A DAY"
tw = d.textlength(title, font=f_title)
d.text(((W - tw) / 2, 46), title, font=f_title, fill=INK)
d.line([(M, 128), (W - M, 128)], fill=INK, width=5)
d.line([(M, 138), (W - M, 138)], fill=INK, width=2)
f_date = font(SERIF, 21)
date_line = "Wednesday, November 18, 2026"
dw = d.textlength(date_line, font=f_date)
d.text(((W - dw) / 2, 148), date_line, font=f_date, fill=INK)
d.line([(M, 182), (W - M, 182)], fill=RULE, width=2)

# ---- Lead story -----------------------------------------------------------
y = 198
d.text((M, y), "SHENZHEN · APEC SUMMIT", font=font(SANS_B, 18), fill=ACCENT)
y += 30
y = headline(d, M, y, "THREE PRESIDENTS, ONE CITY", font(SERIF_B, 46), CW, 53)
y += 6
y = para(
    d, M, y,
    "Xi Jinping rolled out the red carpet in Shenzhen as Donald Trump "
    "arrived for the APEC leaders' meeting and Vladimir Putin shook his "
    "hand at the welcome banquet. On Thursday the three men sit down for "
    "the first trilateral summit of the US, Chinese and Russian "
    "presidents — with Ukraine, Iran and trade on the table.",
    font(SERIF, 21), CW, 27,
)
y += 12
d.line([(M, y), (W - M, y)], fill=RULE, width=2)
y += 16

# ---- Two columns ----------------------------------------------------------
col_w = (CW - 28) // 2
x2 = M + col_w + 28

d.text((M, y), "THE GULF", font=font(SANS_B, 17), fill=ACCENT)
d.text((x2, y), "UKRAINE", font=font(SANS_B, 17), fill=ACCENT)
y += 26
hy = headline(d, M, y, "IRAN STRIKES GULF BASES AFTER US HITS QESHM ISLAND",
              font(SERIF_B, 28), col_w, 34)
hy2 = headline(d, x2, y, "UKRAINE HITS KERCH BRIDGE FOR A SECOND DAY",
               font(SERIF_B, 28), col_w, 34)
y = max(hy, hy2) + 8
by = para(
    d, M, y,
    "Iran fired drones and missiles at Kuwait's Ali Al Salem air base "
    "and at Bahrain hours after US jets struck a Revolutionary Guard "
    "missile site on Qeshm Island. Houthi drones also targeted Saudi "
    "pipeline pumping stations near Riyadh.",
    font(SERIF, 19), col_w, 24,
)
by2 = para(
    d, x2, y,
    "Ukrainian strikes partly collapsed a road span of the bridge "
    "linking Russia to occupied Crimea, dropping it into the strait. "
    "In Moscow, sources said Putin is not ready for serious peace "
    "negotiations — even as the Shenzhen summit looms.",
    font(SERIF, 19), col_w, 24,
)
y = max(by, by2) + 12
d.line([(M, y), (W - M, y)], fill=RULE, width=2)
y += 16

# ---- Briefs ---------------------------------------------------------------
d.text((M, y), "AROUND THE WORLD", font=font(SANS_B, 19), fill=ACCENT)
y += 30
briefs = [
    ("ALASKA", "Peltola beats Senator Sullivan — Democrats take a 56–44 Senate majority."),
    ("DR CONGO", "Ebola cases more than double in three months: 11,000 cases, 5,400 deaths."),
    ("UNITED STATES", "America loses its measles-free status after 26 years: 5,400 cases, 10 deaths."),
    ("JERUSALEM", "The Knesset elects Kahana as speaker — a win for PM-elect Eisenkot over Netanyahu."),
    ("SIBERIA", "A Russian military plane crashes in the Kemerovo region, killing all 19 aboard."),
    ("MARKETS", "Nvidia's quarterly revenue doubles on AI demand, beating expectations."),
    ("WORD OF THE YEAR", "Cambridge Dictionary names 'Human' its word of 2026, in the age of AI."),
]
f_b = font(SERIF, 17)
for tag, text in briefs:
    tag_w = d.textlength(tag + "  ", font=font(SANS_B, 17))
    d.text((M, y + 1), tag, font=font(SANS_B, 17), fill=INK)
    y = para(d, M + tag_w, y, text, f_b, CW - tag_w, 22)
    y += 5

# ---- Footer ---------------------------------------------------------------
d.line([(M, H - 58), (W - M, H - 58)], fill=INK, width=3)
f_foot = font(SERIF, 17)
foot = "Shenzhen decides · The Gulf burns · A bridge falls — Wednesday, in one page."
fw = d.textlength(foot, font=f_foot)
d.text(((W - fw) / 2, H - 44), foot, font=f_foot, fill=RULE)

img.save("/home/hatch/workspace/makefun/news-image-20261118-entry/entry.png", optimize=True)
print("saved")
