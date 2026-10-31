"""Builds the README images for github.com/pr1ncegupta.
Text is outlined to paths, so the images render the same everywhere on GitHub.
Edit the copy below, then run: python3 build_assets.py [header|numbers|quote|contributions ...]
With no arguments it builds everything. The contributions chart reads the GitHub
contribution calendar, so it needs GITHUB_TOKEN (or a logged-in gh CLI).
Needs: pip install fonttools brotli uharfbuzz
"""
import datetime as dt, io, json, os, subprocess, sys, urllib.request
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = {
    "sans": "fonts/GoogleSansFlex-Variable.woff2",       # anything glanced at
    "serif": "fonts/Literata-Variable.woff2",            # anything read
    "italic": "fonts/Literata-Italic-Variable.woff2",    # the one pull quote
}

# ---------- copy ----------
USER = "pr1ncegupta"
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
QUOTE = [  # (text, highlighted) runs per line; the highlight is the quote's one chartreuse element
    [("When the content work starts repeating itself,", False)],
    [("I write ", False), ("the tool that takes the repetition away.", True)],
]
ENGINE = [["Hooks", "Score: 80+", "Script", "Anti-AI pass"],   # two rows; the last step is the chartreuse box
          ["B-roll pack", "Packaging", "Publish"]]
LOOP_LABEL = "Below 80 goes back for a rewrite"

# ---------- brand v3 role tokens ----------
MODES = {
    "light": dict(canvas="#ffffff", surface="#f8fbf9", rule="#e4e7e5", rule_strong="#8a8d8b", ink="#1f2120",
                  muted="#545655", subtle="#707271", accent="#c4ff1a", on_accent="#1f2120", data1="#0a70ff", diagram="#0a70ff", diagram_fill="#e3eeff",
                  heat=["#f1f4f3", "#d0d3d2", "#acafad", "#707271", "#1f2120"],   # grey ramp 100 to 900
                  border=True, dw=0),
    "dark":  dict(canvas="#1f2120", surface="#313332", rule="#414342", rule_strong="#8a8d8b", ink="#ffffff",
                  muted="#e4e7e5", subtle="#acafad", accent="#c4ff1a", on_accent="#1f2120", data1="#c4ff1a", diagram="#67a1fe", diagram_fill="#012968",
                  heat=["#313332", "#545655", "#8a8d8b", "#d0d3d2", "#ffffff"],   # grey ramp 800 to 0
                  border=False, dw=-40),   # take 40 off display weights on Carbon
}

FACES = {}
def face(family):
    if family not in FACES:
        tt = TTFont(os.path.join(HERE, FONTS[family])); buf = io.BytesIO(); tt.flavor = None; tt.save(buf)
        axes = {a.axisTag: (a.minValue, a.maxValue) for a in tt["fvar"].axes}
        FACES[family] = (hb.Face(hb.Blob(buf.getvalue())), axes)
    return FACES[family]

def font_at(family, weight, size):
    fc, axes = face(family)
    f = hb.Font(fc)
    lo, hi = axes["opsz"]
    f.set_variations({"wght": weight, "opsz": max(lo, min(hi, size))})
    return f, fc.upem

def shape(text, size, weight, tracking=0.0, family="sans"):
    f, upem = font_at(family, weight, size)
    b = hb.Buffer(); b.add_str(text); b.guess_segment_properties()
    hb.shape(f, b, {"kern": True, "liga": True})
    s = size / upem; track = tracking * size
    glyphs, x = [], 0.0
    for info, pos in zip(b.glyph_infos, b.glyph_positions):
        glyphs.append((info.codepoint, x + pos.x_offset * s))
        x += pos.x_advance * s + track
    return f, glyphs, x - track, s

def width(text, size, weight, tracking=0.0, family="sans"):
    return shape(text, size, weight, tracking, family)[2]

def path(text, size, weight, x0, base, fill, tracking=0.0, anchor="start", family="sans"):
    f, glyphs, w, s = shape(text, size, weight, tracking, family)
    if anchor == "end": x0 -= w
    if anchor == "middle": x0 -= w / 2
    ds = []
    for gid, gx in glyphs:
        pen = SVGPathPen(None, ntos=lambda v: f"{v:.1f}".rstrip("0").rstrip("."))
        f.draw_glyph_with_pen(gid, TransformPen(pen, (s, 0, 0, -s, x0 + gx, base)))
        ds.append(pen.getCommands())
    return f'<path fill="{fill}" d="{"".join(ds)}"/>'

def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'role="img" aria-label="{title}"><title>{title}</title>{body}</svg>\n')

def check(label, text, size, weight, room, tracking=0.0, family="sans"):
    used = width(text, size, weight, tracking, family)
    ok = used <= room * 0.92
    print(f"  {'ok  ' if ok else 'FAIL'} {label}: {used:.0f} of {room:.0f}px (8% spare = {room*0.92:.0f})")
    if not ok: sys.exit(1)

def frame(c, W, H):
    b = [f'<rect width="{W}" height="{H}" fill="{c["canvas"]}"/>']
    if c["border"]:
        b.append(f'<rect x="1" y="1" width="{W-2}" height="{H-2}" fill="none" stroke="{c["rule"]}" stroke-width="2"/>')
    return b

def write(name, m, w, h, body, alt):
    with open(os.path.join(HERE, f"assets/{name}-{m}.svg"), "w") as fh:
        fh.write(svg(w, h, "".join(body), alt))

def header(m):
    c = MODES[m]; W, H, P = 1200, 500, 72
    wn, wl, wh = 560 + c["dw"], 480 + c["dw"], 540 + c["dw"]
    print(f"header-{m}")
    check("name", NAME, 104, wn, W - 2*P, -0.025)
    check("line 1", LINE_1, 44, wl, W - 2*P, -0.01)
    check("line 2 + box padding", LINE_2, 44, wl, W - 2*P - 28, -0.01)
    check("footer", HANDLE + PLACE, 28, 540, W - 2*P - 120)
    b = frame(c, W, H)
    b.append(path(NAME, 104, wn, P, 184, c["ink"], -0.025))
    b.append(path(LINE_1, 44, wl, P, 264, c["muted"], -0.01))
    bw = width(LINE_2, 44, wl, -0.01) + 28
    b.append(f'<rect x="{P}" y="{322-42}" width="{bw:.0f}" height="58" fill="{c["accent"]}"/>')
    b.append(path(LINE_2, 44, wl, P + 14, 322, c["on_accent"], -0.01))
    b.append(path(HANDLE, 28, wh, P, H - 64, c["ink"]))
    b.append(path(PLACE, 28, 400, W - P, H - 64, c["subtle"], anchor="end"))
    write("header", m, W, H, b, f"{NAME}. {LINE_1} {LINE_2} {PLACE}.")

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
    write("numbers", m, W, H, b, " ".join(f"{n} {' '.join(l)}." for n, l in STATS))

def quote(m):
    """The one pull quote: Literata Italic, with the highlight box on the payoff."""
    c = MODES[m]; W, P, SIZE, LH, PADX = 1200, 72, 46, 72, 14
    print(f"quote-{m}")
    H = 2 * 64 + LH * len(QUOTE)
    b = frame(c, W, H)
    for i, runs in enumerate(QUOTE):
        base = 64 + 52 + i * LH
        check(f"quote line {i+1}", "".join(t for t, _ in runs), SIZE, 400, W - 2*P - 2*PADX, -0.01, "italic")
        x = P
        for text, hi in runs:
            w = width(text, SIZE, 400, -0.01, "italic")
            if hi:   # leave a few px between the previous word and the box
                x += PADX - 6
                b.append(f'<rect x="{x - PADX:.0f}" y="{base-44}" width="{w + 2*PADX:.0f}" height="62" fill="{c["accent"]}"/>')
                b.append(path(text, SIZE, 400, x, base, c["on_accent"], -0.01, family="italic"))
                x += w
            else:
                b.append(path(text, SIZE, 400, x, base, c["ink"], -0.01, family="italic"))
                x += w
    write("quote", m, W, H, b, " ".join(t for runs in QUOTE for t, _ in runs))

def engine(m):
    """The content pipeline as a brand diagram: diagram-fill boxes, 4 px blue lines, Publish in chartreuse."""
    c = MODES[m]; W, P, G, BH, LW = 1200, 72, 48, 96, 4
    BW = (W - 2*P - 3*G) / 4
    print(f"engine-{m}")
    check("loop label", LOOP_LABEL, 28, 400, W - 2*P)
    rows = [150, 326]; H = rows[1] + BH + 56
    b = frame(c, W, H)
    def arrow(x, y, d):   # filled 14 px head pointing right ("r") or down ("d")
        pts = f"{x},{y} {x-14},{y-8} {x-14},{y+8}" if d == "r" else f"{x},{y} {x-8},{y-14} {x+8},{y-14}"
        return f'<polygon points="{pts}" fill="{c["diagram"]}"/>'
    def line(x1, y1, x2, y2):
        return f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{c["diagram"]}" stroke-width="{LW}" stroke-linecap="square"/>'
    box = {}
    for r, steps in enumerate(ENGINE):
        for i, label in enumerate(steps):
            x, y = P + i * (BW + G), rows[r]; box[(r, i)] = (x, y)
            last = r == len(ENGINE) - 1 and i == len(steps) - 1
            check(f"box '{label}'", label, 28, 400, BW - 32)
            b.append(f'<rect x="{x:.0f}" y="{y}" width="{BW:.0f}" height="{BH}" fill="{c["accent"] if last else c["diagram_fill"]}"/>')
            b.append(path(label, 28, 400, x + 16, y + BH/2 + 10, c["on_accent"] if last else c["ink"]))
            if i:   # arrow from the previous box
                b.append(line(x - G + 2, y + BH/2, x - 6, y + BH/2)); b.append(arrow(x, y + BH/2, "r"))
    # the loop: from the scorer back up and over to hooks
    (x1, y1), (x2, _) = box[(0, 0)], box[(0, 1)]
    top = y1 - 32
    b.append(line(x2 + BW/2, y1 - 2, x2 + BW/2, top)); b.append(line(x2 + BW/2, top, x1 + BW/2, top))
    b.append(line(x1 + BW/2, top, x1 + BW/2, y1 - 14)); b.append(arrow(x1 + BW/2, y1, "d"))
    b.append(path(LOOP_LABEL, 28, 400, x1 + BW/2 + 16, top - 16, c["muted"]))
    # row break: down from the last box of row one, across, and into the first box of row two
    (xa, ya), (xb, yb) = box[(0, 3)], box[(1, 0)]
    mid = ya + BH + (yb - ya - BH) / 2
    b.append(line(xa + BW/2, ya + BH + 2, xa + BW/2, mid)); b.append(line(xa + BW/2, mid, xb + BW/2, mid))
    b.append(line(xb + BW/2, mid, xb + BW/2, yb - 14)); b.append(arrow(xb + BW/2, yb, "d"))
    alt = ("The content engine: " + ", then ".join(s for row in ENGINE for s in row) +
           ". Hooks that score below 80 go back for a rewrite.")
    write("engine", m, W, H, b, alt)

# ---------- contributions ----------
LEVELS = {"NONE": 0, "FIRST_QUARTILE": 1, "SECOND_QUARTILE": 2, "THIRD_QUARTILE": 3, "FOURTH_QUARTILE": 4}

def calendar():
    q = ('{user(login:"%s"){contributionsCollection{restrictedContributionsCount '
         'contributionCalendar{totalContributions weeks{contributionDays{date contributionCount contributionLevel}}}}}}' % USER)
    token = os.environ.get("GITHUB_TOKEN") or subprocess.run(["gh", "auth", "token"], capture_output=True, text=True).stdout.strip()
    req = urllib.request.Request("https://api.github.com/graphql", json.dumps({"query": q}).encode(),
                                 {"Authorization": f"bearer {token}", "Content-Type": "application/json"})
    data = json.load(urllib.request.urlopen(req))["data"]["user"]["contributionsCollection"]
    cal = data["contributionCalendar"]
    weeks = [[(dt.date.fromisoformat(d["date"]), d["contributionCount"], LEVELS[d["contributionLevel"]])
              for d in w["contributionDays"]] for w in cal["weeks"]]
    return weeks, cal["totalContributions"], data["restrictedContributionsCount"]

def fmt(d):
    return f"{d.day} {d:%b %Y}"

def contributions(m, cal):
    c = MODES[m]; weeks, total, private = cal
    W, P = 1200, 72; wn = 560 + c["dw"]
    days = [d for w in weeks for d in w]
    active = sum(1 for d in days if d[1])
    best_i = max(range(len(weeks)), key=lambda i: sum(d[1] for d in weeks[i]))
    best_n = sum(d[1] for d in weeks[best_i])
    best_day = max(days, key=lambda d: d[1])
    streak = run = 0
    for d in days:
        run = run + 1 if d[1] else 0; streak = max(streak, run)
    pct = round(100 * private / total) if total else 0
    print(f"contributions-{m}")

    head = f"{total:,} contributions in the last year"
    sub = f"{pct}% of it happened in private repos, so it shows as a count."
    check("headline", head, 56, wn, W - 2*P, -0.02)
    check("subline", sub, 28, 400, W - 2*P, 0, "serif")
    b = frame(c, W, 0)  # height patched below
    b.append(path(head, 56, wn, P, 128, c["ink"], -0.02))
    b.append(path(sub, 28, 400, P, 180, c["muted"], family="serif"))

    # grid: grey ramp by GitHub's own quartiles, the busiest week in data-1
    pitch = (W - 2*P) // len(weeks); cell = pitch - 4; gx, gy = P, 262
    last_label = -999
    for i, w in enumerate(weeks):
        x = gx + i * pitch
        first = w[0][0]
        if first.day <= 7 and x - last_label >= 72:   # month label on the first week of each month
            b.append(path(f"{first:%b}", 28, 400, x, gy - 16, c["subtle"])); last_label = x
        for d in w:
            fill = c["data1"] if i == best_i and d[1] else c["heat"][d[2]]
            b.append(f'<rect x="{x}" y="{gy + d[0].isoweekday() % 7 * pitch}" width="{cell}" height="{cell}" fill="{fill}"/>')
    gb = gy + 7 * pitch - 4

    # callout under the busiest week
    bx = gx + best_i * pitch + cell / 2
    label = f"Busiest week: {best_n} contributions from {fmt(weeks[best_i][0][0])}"
    lw = width(label, 28, 400)
    anchor = "end" if bx + lw > W - P else "start"
    b.append(f'<rect x="{bx-1:.0f}" y="{gb + 8}" width="2" height="36" fill="{c["rule_strong"]}"/>')
    b.append(path(label, 28, 400, bx + (10 if anchor == "start" else -10), gb + 42, c["ink"], anchor=anchor))

    # stat row
    sy = gb + 76; cw = (W - 2*P) / 3
    stats = [(f"{active}", "active days"), (f"{streak}", "day longest streak"),
             (f"{best_day[1]}", f"top day, {best_day[0].day} {best_day[0]:%b %Y}")]
    b.append(f'<rect x="{P}" y="{sy}" width="{W - 2*P}" height="2" fill="{c["rule"]}"/>')
    for i, (num, lab) in enumerate(stats):
        x = P + i * cw
        check(f"stat {num}", num, 56, wn, cw - 24, -0.02)
        check(f"  label '{lab}'", lab, 28, 400, cw - 24)
        b.append(path(num, 56, wn, x, sy + 80, c["ink"], -0.02))
        b.append(path(lab, 28, 400, x, sy + 120, c["muted"]))

    src = f"Source: GitHub contribution calendar. Rebuilt daily, last on {fmt(dt.date.today())}."
    check("source", src, 28, 400, W - 2*P)
    H = sy + 250
    b.append(path(src, 28, 400, P, H - 56, c["subtle"]))
    b[0] = f'<rect width="{W}" height="{H}" fill="{c["canvas"]}"/>'
    if c["border"]:
        b[1] = f'<rect x="1" y="1" width="{W-2}" height="{H-2}" fill="none" stroke="{c["rule"]}" stroke-width="2"/>'
    alt = (f"{head}. {sub} The busiest week started {fmt(weeks[best_i][0][0])} with {best_n} contributions. "
           f"Longest streak: {streak} days.")
    write("contributions", m, W, H, b, alt)

if __name__ == "__main__":
    jobs = sys.argv[1:] or ["header", "numbers", "quote", "engine", "contributions"]
    cal = calendar() if "contributions" in jobs else None
    for m in MODES:
        for j in jobs:
            contributions(m, cal) if j == "contributions" else globals()[j](m)
    print("done")
