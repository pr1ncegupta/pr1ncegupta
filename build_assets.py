"""Builds the README images for github.com/pr1ncegupta.
Text is outlined to paths, so the images render the same everywhere on GitHub.
Edit the copy below, then run: python3 build_assets.py
Needs: pip install fonttools brotli uharfbuzz
"""
import io, sys
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

FONT = sys.argv[1] if len(sys.argv) > 1 else "GoogleSansFlex-Variable.woff2"

# ---------- copy ----------
NAME = "Prince Gupta"
LINE_1 = "I lead social and partnerships at Lyzr AI,"
LINE_2 = "and I build the systems that run it."   # the one chartreuse highlight
HANDLE = "@pr1ncegupta"
PLACE = "Bengaluru, from Nepal"
STATS = [
    ("9M", ["views on the", "Architect creator", "campaign at Lyzr"]),
    ("~100K", ["followers for", "decodedbyprince", "across platforms"]),
    ("1.5 yrs", ["to build it, after", "a few channels", "that did not work"]),
]

# ---------- brand v3 role tokens ----------
MODES = {
    "light": dict(canvas="#ffffff", surface="#f8fbf9", rule="#e4e7e5", ink="#1f2120",
                  muted="#545655", subtle="#707271", accent="#c4ff1a", on_accent="#1f2120",
                  border=True, dw=0),
    "dark":  dict(canvas="#1f2120", surface="#313332", rule="#414342", ink="#ffffff",
                  muted="#e4e7e5", subtle="#acafad", accent="#c4ff1a", on_accent="#1f2120",
                  border=False, dw=-40),   # take 40 off display weights on Carbon
}

tt = TTFont(FONT); buf = io.BytesIO(); tt.flavor = None; tt.save(buf)
blob = hb.Blob(buf.getvalue()); face = hb.Face(blob); UPEM = face.upem

def font_at(weight, size):
    f = hb.Font(face)
    f.set_variations({"wght": weight, "opsz": max(6, min(144, size))})
    return f

def shape(text, size, weight, tracking=0.0):
    f = font_at(weight, size)
    b = hb.Buffer(); b.add_str(text); b.guess_segment_properties()
    hb.shape(f, b, {"kern": True, "liga": True})
    s = size / UPEM; track = tracking * size
    glyphs, x = [], 0.0
    for info, pos in zip(b.glyph_infos, b.glyph_positions):
        glyphs.append((info.codepoint, x + pos.x_offset * s))
        x += pos.x_advance * s + track
    return f, glyphs, x - track

def width(text, size, weight, tracking=0.0):
    return shape(text, size, weight, tracking)[2]

def path(text, size, weight, x0, base, fill, tracking=0.0, anchor="start"):
    f, glyphs, w = shape(text, size, weight, tracking)
    if anchor == "end": x0 -= w
    s = size / UPEM; ds = []
    for gid, gx in glyphs:
        pen = SVGPathPen(None, ntos=lambda v: f"{v:.1f}".rstrip("0").rstrip("."))
        f.draw_glyph_with_pen(gid, TransformPen(pen, (s, 0, 0, -s, x0 + gx, base)))
        ds.append(pen.getCommands())
    return f'<path fill="{fill}" d="{"".join(ds)}"/>'

def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'role="img" aria-label="{title}"><title>{title}</title>{body}</svg>\n')

def check(label, text, size, weight, room, tracking=0.0):
    used = width(text, size, weight, tracking)
    ok = used <= room * 0.92
    print(f"  {'ok  ' if ok else 'FAIL'} {label}: {used:.0f} of {room:.0f}px (8% spare = {room*0.92:.0f})")
    if not ok: sys.exit(1)

def header(m):
    c = MODES[m]; W, H, P = 1200, 500, 72
    wn, wl, wh = 560 + c["dw"], 480 + c["dw"], 540 + c["dw"]
    print(f"header-{m}")
    check("name", NAME, 104, wn, W - 2*P, -0.025)
    check("line 1", LINE_1, 44, wl, W - 2*P, -0.01)
    check("line 2 + box padding", LINE_2, 44, wl, W - 2*P - 28, -0.01)
    check("footer", HANDLE + PLACE, 28, 540, W - 2*P - 120)
    b = [f'<rect width="{W}" height="{H}" fill="{c["canvas"]}"/>']
    if c["border"]:
        b.append(f'<rect x="1" y="1" width="{W-2}" height="{H-2}" fill="none" stroke="{c["rule"]}" stroke-width="2"/>')
    b.append(path(NAME, 104, wn, P, 184, c["ink"], -0.025))
    b.append(path(LINE_1, 44, wl, P, 264, c["muted"], -0.01))
    bw = width(LINE_2, 44, wl, -0.01) + 28
    b.append(f'<rect x="{P}" y="{322-42}" width="{bw:.0f}" height="58" fill="{c["accent"]}"/>')
    b.append(path(LINE_2, 44, wl, P + 14, 322, c["on_accent"], -0.01))
    b.append(path(HANDLE, 28, wh, P, H - 64, c["ink"]))
    b.append(path(PLACE, 28, 400, W - P, H - 64, c["subtle"], anchor="end"))
    alt = f"{NAME}. {LINE_1} {LINE_2} {PLACE}."
    open(f"assets/header-{m}.svg", "w").write(svg(W, H, "".join(b), alt))

def numbers(m):
    c = MODES[m]; W, H, G, PAD = 1200, 292, 24, 40
    cw = (W - 2*G) / 3; wn = 560 + c["dw"]
    print(f"numbers-{m}")
    b = []
    for i, (num, lines) in enumerate(STATS):
        x = i * (cw + G)
        check(f"stat {num}", num, 96, wn, cw - 2*PAD, -0.03)
        for ln in lines: check(f"  label '{ln}'", ln, 28, 400, cw - 2*PAD)
        if c["border"]:
            b.append(f'<rect x="{x+1:.0f}" y="1" width="{cw-2:.0f}" height="{H-2}" fill="{c["surface"]}" stroke="{c["rule"]}" stroke-width="2"/>')
        else:
            b.append(f'<rect x="{x:.0f}" y="0" width="{cw:.0f}" height="{H}" fill="{c["surface"]}"/>')
        b.append(path(num, 96, wn, x + PAD, 40 + 72, c["ink"], -0.03))
        for j, ln in enumerate(lines):
            b.append(path(ln, 28, 400, x + PAD, 164 + j*38, c["muted"]))
    alt = " ".join(f"{n} {' '.join(l)}." for n, l in STATS)
    open(f"assets/numbers-{m}.svg", "w").write(svg(W, H, "".join(b), alt))

for m in MODES:
    header(m); numbers(m)
print("done")
