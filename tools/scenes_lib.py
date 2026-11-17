"""Tiny flat-illustration kit used to draw the speaking scenes (viewBox 0 0 400 260)."""
import math

SKIN = ["#f1c7a5", "#d9a27a", "#a8704a", "#7a4b2e", "#f6d5bd"]
HAIR = ["#2b1d14", "#5a3a22", "#c8a165", "#1a1a1a", "#9a9a9a", "#8b3a1e"]
INK = "#1f2937"


def f(n):
    return ("%.1f" % n).rstrip("0").rstrip(".")


def rect(x, y, w, h, fill, rx=0, extra=""):
    return f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" rx="{f(rx)}" fill="{fill}" {extra}/>'


def circ(x, y, r, fill, extra=""):
    return f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r)}" fill="{fill}" {extra}/>'


def ell(x, y, rx, ry, fill, extra=""):
    return f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(rx)}" ry="{f(ry)}" fill="{fill}" {extra}/>'


def path(d, fill="none", stroke=None, sw=0, extra=""):
    s = f' stroke="{stroke}" stroke-width="{f(sw)}" stroke-linecap="round" stroke-linejoin="round"' if stroke else ""
    return f'<path d="{d}" fill="{fill}"{s} {extra}/>'


def line(x1, y1, x2, y2, stroke, sw=2):
    return f'<line x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}" stroke="{stroke}" stroke-width="{f(sw)}" stroke-linecap="round"/>'


def poly(pts, fill, extra=""):
    return f'<polygon points="{" ".join(f(a) + "," + f(b) for a, b in pts)}" fill="{fill}" {extra}/>'


def text(x, y, t, size=10, fill=INK, weight=700, anchor="middle"):
    return f'<text x="{f(x)}" y="{f(y)}" font-size="{size}" font-family="system-ui,sans-serif" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{t}</text>'


# ---------------- backgrounds ----------------
def sky(top="#bfe3ff", bottom="#e8f5ff", ground="#9ed38a", hy=185, ground2=None):
    g = f'<defs><linearGradient id="sk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{top}"/><stop offset="1" stop-color="{bottom}"/></linearGradient></defs>'
    return g + rect(0, 0, 400, hy, "url(#sk)") + rect(0, hy, 400, 260 - hy, ground) + (rect(0, hy, 400, 6, ground2) if ground2 else "")


def room(wall="#f3ead8", floor="#c9a77c", fy=190, skirting="#e2d3b8"):
    return rect(0, 0, 400, fy, wall) + rect(0, fy - 5, 400, 5, skirting) + rect(0, fy, 400, 260 - fy, floor)


def window(x, y, w, h, outside="#bfe3ff", frame="#ffffff", rain=False, night=False, sun=False):
    o = night and "#1e3a5f" or outside
    s = rect(x - 4, y - 4, w + 8, h + 8, frame, 3) + rect(x, y, w, h, o)
    if sun:
        s += circ(x + w * 0.72, y + h * 0.3, min(w, h) * 0.13, "#ffd54a")
    if rain:
        for i in range(int(w / 9)):
            xx = x + 5 + i * 9
            s += line(xx, y + 6 + (i % 3) * 9, xx - 3, y + 14 + (i % 3) * 9, "#7fa6c9", 1.5)
            s += line(xx + 2, y + h - 22 + (i % 2) * 6, xx - 1, y + h - 14 + (i % 2) * 6, "#7fa6c9", 1.5)
    s += rect(x + w / 2 - 2, y, 4, h, frame) + rect(x, y + h / 2 - 2, w, 4, frame)
    return s


def clock(x, y, r, hour, minute=0, face="#ffffff"):
    a_h = math.radians((hour % 12 + minute / 60) * 30 - 90)
    a_m = math.radians(minute * 6 - 90)
    return (circ(x, y, r + 2, INK) + circ(x, y, r, face)
            + "".join(circ(x + math.cos(math.radians(k * 30)) * r * 0.8, y + math.sin(math.radians(k * 30)) * r * 0.8, r * 0.07, INK) for k in range(12))
            + line(x, y, x + math.cos(a_h) * r * 0.5, y + math.sin(a_h) * r * 0.5, INK, max(1.5, r * 0.12))
            + line(x, y, x + math.cos(a_m) * r * 0.75, y + math.sin(a_m) * r * 0.75, INK, max(1, r * 0.08)))


def plant(x, y, s=1, pot="#c46b3c"):
    leaves = "".join(ell(x + dx * s, y - 22 * s + dy * s, 6 * s, 13 * s, c, f'transform="rotate({rot} {f(x + dx * s)} {f(y - 22 * s + dy * s)})"')
                     for dx, dy, rot, c in [(-8, 0, -30, "#3f9a4a"), (8, 0, 30, "#3f9a4a"), (0, -6, 0, "#55b35e"), (-4, -2, -12, "#4caa55"), (5, -3, 14, "#4caa55")])
    return leaves + poly([(x - 10 * s, y - 12 * s), (x + 10 * s, y - 12 * s), (x + 7 * s, y), (x - 7 * s, y)], pot)


def tree(x, y, s=1, crown="#4caf50", trunk="#7a5230"):
    return rect(x - 5 * s, y - 40 * s, 10 * s, 40 * s, trunk) + circ(x, y - 58 * s, 26 * s, crown) + circ(x - 18 * s, y - 45 * s, 16 * s, crown) + circ(x + 18 * s, y - 45 * s, 16 * s, crown) + circ(x - 8 * s, y - 66 * s, 10 * s, "#ffffff", 'opacity=".12"')


def cloud(x, y, s=1, c="#ffffff"):
    return circ(x, y, 12 * s, c) + circ(x + 14 * s, y - 6 * s, 15 * s, c) + circ(x + 30 * s, y, 12 * s, c) + rect(x, y, 30 * s, 12 * s, c)


def sun(x, y, r=16):
    rays = "".join(line(x + math.cos(math.radians(a)) * (r + 4), y + math.sin(math.radians(a)) * (r + 4), x + math.cos(math.radians(a)) * (r + 11), y + math.sin(math.radians(a)) * (r + 11), "#ffc93c", 3) for a in range(0, 360, 45))
    return rays + circ(x, y, r, "#ffd54a")


def rain(x0=0, x1=400, y0=0, y1=190, n=60, seed=3):
    s, k = "", seed
    for i in range(n):
        k = (k * 73 + 41) % 997
        x = x0 + (k % 1000) / 1000 * (x1 - x0)
        y = y0 + ((k * 7) % 997) / 997 * (y1 - y0)
        s += line(x, y, x - 3, y + 9, "#8fb0cc", 1.4)
    return s


# ---------------- furniture & objects ----------------
def table(x, y, w, top="#8b5e3c", legs="#6b4529", h=None, cloth=None):
    h = h or 48
    s = rect(x + 6, y, 6, h, legs) + rect(x + w - 12, y, 6, h, legs)
    if cloth:
        s += rect(x - 4, y - 4, w + 8, 22, cloth, 3)
    return s + rect(x - 4, y - 6, w + 8, 8, top, 3)


def desk(x, y, w, top="#e5e7eb", legs="#9ca3af"):
    return table(x, y, w, top, legs)


def chair(x, y, c="#374151", back=True):
    s = rect(x - 16, y, 32, 6, c, 2) + rect(x - 14, y + 6, 4, 28, c) + rect(x + 10, y + 6, 4, 28, c)
    if back:
        s += rect(x - 16, y - 34, 32, 30, c, 6)
    return s


def laptop(x, y, facing=1, c="#9ca3af", screen="#1e293b", glow="#60a5fa"):
    """x,y = bottom centre on a table. facing=1: screen faces viewer; -1: back of lid towards viewer."""
    if facing == 1:
        return poly([(x - 22, y - 30), (x + 22, y - 30), (x + 20, y - 2), (x - 20, y - 2)], c) + rect(x - 18, y - 27, 36, 22, screen) + rect(x - 14, y - 23, 20, 3, glow) + rect(x - 14, y - 17, 26, 3, glow, 0, 'opacity=".6"') + rect(x - 26, y - 3, 52, 4, "#6b7280", 2)
    return poly([(x - 22, y - 30), (x + 22, y - 30), (x + 20, y - 2), (x - 20, y - 2)], c) + circ(x, y - 16, 3, "#e5e7eb") + rect(x - 26, y - 3, 52, 4, "#6b7280", 2)


def monitor(x, y, w=60, h=38, screen="#0f172a", content=""):
    return rect(x - 4, y - 4 - 6, 8, 10, "#4b5563") + rect(x - 14, y - 2, 28, 3, "#4b5563") + rect(x - w / 2, y - h - 8, w, h, "#374151", 3) + rect(x - w / 2 + 3, y - h - 5, w - 6, h - 6, screen) + content


def cup(x, y, c="#ffffff", steam=True):
    s = rect(x - 5, y - 10, 10, 10, c, 2) + path(f"M{f(x + 5)} {f(y - 8)} q5 1 0 6", stroke=c, sw=2)
    if steam:
        s += path(f"M{f(x - 2)} {f(y - 13)} q-3 -4 0 -8 q3 -4 0 -8", stroke="#cbd5e1", sw=1.5)
    return s


def paper(x, y, w=22, h=28, rot=0, lines=4):
    s = f'<g transform="rotate({rot} {f(x + w / 2)} {f(y + h / 2)})">' + rect(x, y, w, h, "#ffffff", 1, f'stroke="#cbd5e1" stroke-width="1"')
    for i in range(lines):
        s += rect(x + 3, y + 5 + i * 5, w - 6 - (i % 2) * 5, 1.6, "#94a3b8")
    return s + "</g>"


def clipboard(x, y):
    return rect(x, y, 18, 24, "#a16207", 2) + rect(x + 2, y + 4, 14, 18, "#fff") + rect(x + 5, y - 2, 8, 4, "#6b7280", 1) + "".join(rect(x + 4, y + 8 + i * 4, 10, 1.4, "#94a3b8") for i in range(3))


def phone(x, y, c="#111827"):
    return rect(x - 4, y - 7, 8, 14, c, 2) + rect(x - 3, y - 5.5, 6, 10, "#60a5fa")


def whiteboard(x, y, w, h, chart=True, kind="bars"):
    s = rect(x, y, w, h, "#ffffff", 3, 'stroke="#9ca3af" stroke-width="3"')
    if chart and kind == "bars":
        for i, v in enumerate([0.35, 0.55, 0.45, 0.8]):
            bh = (h - 22) * v
            s += rect(x + 12 + i * (w - 24) / 4, y + h - 10 - bh, (w - 24) / 4 - 8, bh, ["#60a5fa", "#34d399", "#fbbf24", "#f87171"][i])
        s += path(f"M{f(x + 14)} {f(y + h - 30)} L{f(x + w * 0.45)} {f(y + h * 0.45)} L{f(x + w - 16)} {f(y + 14)}", stroke="#1f2937", sw=2)
    elif chart and kind == "plan":
        s += path(f"M{f(x + 12)} {f(y + h - 12)} h{f(w - 24)} M{f(x + 20)} {f(y + h - 12)} v-{f(h * 0.5)} h{f(w * 0.35)} v{f(h * 0.5)} M{f(x + w * 0.55)} {f(y + h - 12)} l{f(w * 0.15)} -{f(h * 0.55)} l{f(w * 0.15)} {f(h * 0.55)}", stroke="#2563eb", sw=1.6)
    return s


def ladder(x, y_top, y_bot, w=26, c="#b45309"):
    s = rect(x, y_top, 4, y_bot - y_top, c) + rect(x + w, y_top, 4, y_bot - y_top, c)
    yy = y_top + 10
    while yy < y_bot:
        s += rect(x, yy, w + 4, 3, c)
        yy += 16
    return s


def toolbox(x, y, c="#dc2626"):
    return rect(x - 18, y - 16, 36, 16, c, 2) + path(f"M{f(x - 8)} {f(y - 16)} v-6 h16 v6", stroke="#374151", sw=2.5) + rect(x - 18, y - 11, 36, 2, "#991b1b")


def ceiling_lamp(x, y_top, y, on=True):
    s = line(x, y_top, x, y - 10, "#374151", 2) + path(f"M{f(x - 16)} {f(y)} Q{f(x)} {f(y - 22)} {f(x + 16)} {f(y)} Z", "#fbbf24")
    if on:
        s += poly([(x - 16, y), (x + 16, y), (x + 48, y + 70), (x - 48, y + 70)], "#fff6c2", 'opacity=".45"')
    return s


def house(x, y, w=110, h=70, wall="#fde7c8", roof="#b91c1c", solar=False):
    s = rect(x, y - h, w, h, wall) + poly([(x - 10, y - h), (x + w / 2, y - h - 45), (x + w + 10, y - h)], roof)
    if solar:
        for i in range(3):
            s += poly([(x + 18 + i * 22, y - h - 10 - i * 0), (x + 38 + i * 22, y - h - 10), (x + 36 + i * 22, y - h - 26 + abs(1 - i) * 0), (x + 16 + i * 22, y - h - 26)], "#1e3a8a", 'stroke="#93c5fd" stroke-width="1"')
    s += rect(x + w / 2 - 12, y - 40, 24, 40, "#7c4a25", 2) + circ(x + w / 2 + 7, y - 20, 2, "#fde68a")
    s += window(x + 12, y - h + 14, 22, 20) + window(x + w - 34, y - h + 14, 22, 20)
    return s


def car(x, y, c="#2563eb", ev=False):
    s = path(f"M{f(x - 44)} {f(y - 10)} v-14 q0 -6 8 -8 l14 -4 l12 -14 q4 -4 12 -4 h26 q8 0 12 6 l10 14 q14 2 14 10 v14 z", c)
    s += poly([(x - 14, y - 38), (x - 2, y - 52), (x + 12, y - 52), (x + 12, y - 38)], "#cfe8ff") + poly([(x + 16, y - 38), (x + 16, y - 52), (x + 30, y - 52), (x + 38, y - 38)], "#cfe8ff")
    s += circ(x - 24, y - 8, 10, "#111827") + circ(x - 24, y - 8, 4, "#9ca3af") + circ(x + 30, y - 8, 10, "#111827") + circ(x + 30, y - 8, 4, "#9ca3af")
    if ev:
        s += path(f"M{f(x + 4)} {f(y - 30)} l-5 8 h5 l-3 7", stroke="#facc15", sw=2)
    return s


def battery_wall(x, y):
    return rect(x, y - 46, 26, 46, "#e5e7eb", 4, 'stroke="#9ca3af" stroke-width="1.5"') + rect(x + 5, y - 38, 16, 26, "#d1d5db", 2) + rect(x + 5, y - 22, 16, 10, "#22c55e", 2) + rect(x + 5, y - 30, 16, 7, "#22c55e", 1)


def charger(x, y):
    return rect(x - 7, y - 50, 14, 50, "#374151", 3) + rect(x - 5, y - 44, 10, 8, "#22c55e", 1)


def bus(x, y, c="#e11d48"):
    s = rect(x, y - 52, 150, 44, c, 8) + "".join(rect(x + 10 + i * 27, y - 46, 22, 16, "#dbeafe", 2) for i in range(5))
    s += rect(x + 138, y - 46, 8, 30, "#dbeafe", 2) + circ(x + 30, y - 8, 10, "#111827") + circ(x + 120, y - 8, 10, "#111827") + text(x + 75, y - 18, "42", 9, "#fff")
    return s


def bus_stop(x, y):
    return rect(x, y - 80, 4, 80, "#475569") + rect(x - 30, y - 82, 70, 6, "#475569", 2) + rect(x + 6, y - 74, 30, 40, "#bae6fd", 2, 'opacity=".6"') + circ(x + 2, y - 92, 9, "#16a34a") + text(x + 2, y - 89, "B", 9, "#fff")


def umbrella(x, y, c="#7c3aed"):
    """x,y = handle grip (hand position)."""
    return line(x, y, x, y - 46, "#374151", 2) + path(f"M{f(x - 32)} {f(y - 40)} Q{f(x)} {f(y - 80)} {f(x + 32)} {f(y - 40)} Q{f(x + 16)} {f(y - 48)} {f(x)} {f(y - 40)} Q{f(x - 16)} {f(y - 48)} {f(x - 32)} {f(y - 40)} Z", c) + path(f"M{f(x)} {f(y)} q0 5 -5 5", stroke="#374151", sw=2)


def stall(x, y, w=160, awning=("#ef4444", "#ffffff")):
    s = rect(x, y - 110, 6, 110, "#78350f") + rect(x + w - 6, y - 110, 6, 110, "#78350f")
    n = 8
    for i in range(n):
        s += path(f"M{f(x - 6 + i * (w + 12) / n)} {f(y - 118)} h{f((w + 12) / n)} v14 q-{f((w + 12) / n / 2)} 10 -{f((w + 12) / n)} 0 z", awning[i % 2])
    s += rect(x - 6, y - 50, w + 12, 50, "#a16207", 2)
    return s


def produce(x, y, kind):
    if kind == "apples":
        return "".join(circ(x + i * 9 - 18, y - 6 - (i % 2) * 6, 5.5, "#dc2626") for i in range(5))
    if kind == "oranges":
        return "".join(circ(x + i * 9 - 18, y - 6 - (i % 2) * 6, 5.5, "#f97316") for i in range(5))
    if kind == "broccoli":
        return "".join(circ(x + i * 10 - 15, y - 9 - (i % 2) * 4, 7, "#15803d") + rect(x + i * 10 - 17, y - 5, 4, 5, "#65a30d") for i in range(4))
    if kind == "cheese":
        return poly([(x - 16, y), (x + 16, y), (x + 16, y - 12), (x - 6, y - 18)], "#facc15") + circ(x + 4, y - 7, 2.5, "#eab308") + circ(x - 6, y - 4, 2, "#eab308")
    if kind == "tomatoes":
        return "".join(circ(x + i * 9 - 13, y - 6 - (i % 2) * 5, 5.5, "#ef4444") + rect(x + i * 9 - 14, y - 12 - (i % 2) * 5, 3, 2, "#16a34a") for i in range(4))
    return ""


def crate(x, y, w=40, c="#c08a4b"):
    return rect(x, y - 16, w, 16, c, 1) + rect(x, y - 10, w, 2, "#8b5e34")


def stove(x, y, fire=True):
    s = rect(x, y - 60, 80, 60, "#d1d5db", 3) + rect(x + 6, y - 44, 68, 36, "#9ca3af", 2) + rect(x - 2, y - 64, 84, 6, "#4b5563", 2)
    if fire:
        s += path(f"M{f(x + 22)} {f(y - 64)} q-6 -8 0 -14 q2 6 6 2 q2 6 -2 12 z", "#f97316") + path(f"M{f(x + 56)} {f(y - 64)} q-5 -7 0 -12 q2 5 5 2 q2 5 -1 10 z", "#f97316")
    return s


def pan(x, y, food=None):
    s = ell(x, y, 22, 6, "#1f2937") + rect(x + 20, y - 3, 26, 4, "#1f2937", 2)
    if food == "egg":
        s += ell(x, y - 2, 12, 4, "#ffffff") + circ(x, y - 3, 4, "#facc15")
    elif food == "sauce":
        s += ell(x, y - 2, 18, 4, "#dc2626")
    return s


def pot(x, y, steam=True):
    s = rect(x - 18, y - 24, 36, 24, "#94a3b8", 3) + rect(x - 22, y - 26, 44, 4, "#64748b", 2)
    if steam:
        s += "".join(path(f"M{f(x - 8 + i * 8)} {f(y - 30)} q-4 -6 0 -12 q4 -6 0 -12", stroke="#e2e8f0", sw=2) for i in range(3))
    return s


def board(x, y, items=""):
    return rect(x - 26, y - 6, 52, 6, "#d6a76b", 2) + items


def knife(x, y):
    return rect(x, y - 3, 22, 4, "#e5e7eb", 2) + rect(x - 12, y - 3, 12, 4, "#1f2937", 2)


def plate(x, y, food="#f59e0b"):
    return ell(x, y, 18, 5, "#ffffff", 'stroke="#d1d5db" stroke-width="1"') + ell(x, y - 2, 10, 3.5, food)


def glass(x, y, c="#7f1d1d"):
    return path(f"M{f(x - 5)} {f(y - 20)} h10 q0 10 -5 12 q-5 -2 -5 -12 z", "#e0f2fe") + path(f"M{f(x - 4)} {f(y - 15)} h8 q-1 6 -4 7 q-3 -1 -4 -7 z", c) + rect(x - 0.8, y - 8, 1.6, 8, "#cbd5e1") + rect(x - 4, y - 1, 8, 1.5, "#cbd5e1")


def candle(x, y):
    return rect(x - 3, y - 18, 6, 18, "#fef3c7") + path(f"M{f(x)} {f(y - 26)} q-4 4 0 8 q4 -4 0 -8 z", "#f59e0b") + circ(x, y - 22, 9, "#fde68a", 'opacity=".35"')


def bottle(x, y, c="#14532d"):
    return rect(x - 5, y - 28, 10, 28, c, 3) + rect(x - 2, y - 36, 4, 9, c) + rect(x - 5, y - 18, 10, 8, "#fef3c7")


def grill(x, y):
    s = rect(x - 40, y - 50, 80, 26, "#1f2937", 3) + rect(x - 36, y - 26, 4, 26, "#374151") + rect(x + 32, y - 26, 4, 26, "#374151")
    s += "".join(circ(x - 30 + i * 9, y - 52, 4, "#f97316", 'opacity=".9"') for i in range(7))
    s += rect(x - 30, y - 60, 24, 8, "#7c2d12", 3) + rect(x - 2, y - 60, 20, 8, "#991b1b", 3) + rect(x + 20, y - 59, 12, 6, "#b45309", 3)
    s += "".join(path(f"M{f(x - 20 + i * 18)} {f(y - 64)} q-5 -8 0 -16 q5 -8 0 -16", stroke="#cbd5e1", sw=2, extra='opacity=".7"') for i in range(3))
    return s


def ball(x, y, r=7):
    return circ(x, y, r, "#ffffff", f'stroke="{INK}" stroke-width="1"') + poly([(x, y - r * 0.4), (x + r * 0.38, y - r * 0.1), (x + r * 0.24, y + r * 0.35), (x - r * 0.24, y + r * 0.35), (x - r * 0.38, y - r * 0.1)], INK)


def goal(x, y, w=110, h=56):
    s = rect(x, y - h, 5, h, "#ffffff") + rect(x + w - 5, y - h, 5, h, "#ffffff") + rect(x, y - h, w, 5, "#ffffff")
    for i in range(1, 10):
        s += line(x + i * w / 10, y - h + 5, x + i * w / 10, y, "#e5e7eb", 0.8)
    for j in range(1, 5):
        s += line(x + 5, y - h + j * h / 5, x + w - 5, y - h + j * h / 5, "#e5e7eb", 0.8)
    return s


def crowd(y, n=26, colors=("#2563eb", "#ffffff", "#2563eb", "#facc15"), y_rows=3):
    s = rect(0, y - 70, 400, 70, "#475569")
    k = 0
    for r in range(y_rows):
        for i in range(n):
            x = 8 + i * (400 / n) + (r % 2) * 7
            yy = y - 58 + r * 20
            c = colors[(i + r) % len(colors)]
            s += circ(x, yy, 5, SKIN[(i * 3 + r) % 5]) + rect(x - 6, yy + 5, 12, 9, c, 3)
            if (i * 7 + r) % 5 == 0:
                s += line(x + 5, yy + 6, x + 9, yy - 6, c, 2.5)
            k += 1
    return s


def cone(x, y, c="#f97316"):
    return poly([(x - 7, y), (x + 7, y), (x + 2, y - 16), (x - 2, y - 16)], c) + rect(x - 4, y - 9, 8, 3, "#ffffff") + rect(x - 9, y - 2, 18, 3, c, 1)


def tv(x, y, w=110, h=64, content=""):
    return rect(x - w / 2 - 4, y - h - 4, w + 8, h + 8, "#111827", 4) + rect(x - w / 2, y - h, w, h, "#16a34a") + content + rect(x - 3, y + 4, 6, 10, "#374151")


def box(x, y, w=40, h=32, label=None):
    s = rect(x, y - h, w, h, "#c9965b", 2) + rect(x, y - h, w, 6, "#b07d43") + rect(x + w / 2 - 4, y - h, 8, h * 0.45, "#e7c79b")
    if label:
        s += text(x + w / 2, y - h / 2 + 6, label, 7, "#5b3a17")
    return s


def van(x, y, c="#f8fafc"):
    s = path(f"M{f(x)} {f(y - 12)} v-56 q0 -6 6 -6 h96 q6 0 8 6 l14 26 q8 2 8 10 v20 z", c, extra='stroke="#cbd5e1" stroke-width="1.5"')
    s += poly([(x + 108, y - 66), (x + 118, y - 44), (x + 104, y - 44), (x + 104, y - 66)], "#cfe8ff") + rect(x + 10, y - 54, 80, 3, "#2563eb")
    s += circ(x + 26, y - 10, 11, "#111827") + circ(x + 110, y - 10, 11, "#111827") + circ(x + 26, y - 10, 4, "#9ca3af") + circ(x + 110, y - 10, 4, "#9ca3af")
    return s


def sofa(x, y, c="#0d9488"):
    return rect(x, y - 30, 90, 26, c, 6) + rect(x - 8, y - 38, 14, 34, c, 5) + rect(x + 84, y - 38, 14, 34, c, 5) + rect(x + 4, y - 46, 82, 20, c, 6, 'opacity=".85"')


def bench(x, y, c="#92400e"):
    return rect(x, y - 24, 80, 6, c, 2) + rect(x, y - 40, 80, 5, c, 2) + rect(x + 6, y - 18, 4, 18, "#374151") + rect(x + 70, y - 18, 4, 18, "#374151")


def dog(x, y, c="#b45309"):
    return ell(x, y - 14, 16, 8, c) + circ(x + 16, y - 22, 7, c) + ell(x + 19, y - 28, 3, 5, "#78350f") + circ(x + 19, y - 23, 1.2, INK) + rect(x - 12, y - 8, 4, 8, c) + rect(x + 8, y - 8, 4, 8, c) + path(f"M{f(x - 16)} {f(y - 16)} q-8 -6 -6 -12", stroke=c, sw=3)


def cat(x, y, c="#6b7280"):
    return ell(x, y - 8, 12, 8, c) + circ(x + 10, y - 16, 6, c) + poly([(x + 6, y - 20), (x + 8, y - 26), (x + 10, y - 20)], c) + poly([(x + 11, y - 20), (x + 14, y - 26), (x + 15, y - 19)], c) + path(f"M{f(x - 12)} {f(y - 8)} q-8 -2 -6 -12", stroke=c, sw=3)


def crane(x, y, h=150):
    s = ""
    for i in range(int(h / 14)):
        yy = y - i * 14
        s += path(f"M{f(x)} {f(yy)} l12 -14 M{f(x + 12)} {f(yy)} l-12 -14", stroke="#f59e0b", sw=1.5)
    s += rect(x - 1, y - h, 3, h, "#f59e0b") + rect(x + 11, y - h, 3, h, "#f59e0b")
    s += rect(x - 40, y - h - 6, 150, 6, "#f59e0b") + rect(x - 40, y - h, 22, 14, "#64748b") + line(x + 90, y - h, x + 90, y - h + 60, "#374151", 1.5) + rect(x + 82, y - h + 60, 16, 10, "#9ca3af")
    return s


def bridge_wip(x, y, w=260):
    s = rect(x, y - 30, w * 0.62, 10, "#9ca3af") + rect(x + 20, y - 20, 12, 20, "#9ca3af") + rect(x + w * 0.45, y - 20, 12, 20, "#9ca3af") + rect(x + w * 0.85, y - 20, 12, 20, "#9ca3af")
    s += path(f"M{f(x + w * 0.62)} {f(y - 30)} h{f(w * 0.15)}", stroke="#9ca3af", sw=2, extra='stroke-dasharray="4 4"')
    return s


def barrier(x, y, w=70):
    s = rect(x, y - 22, w, 10, "#ffffff", 2)
    for i in range(int(w / 14)):
        s += poly([(x + i * 14, y - 12), (x + i * 14 + 7, y - 22), (x + i * 14 + 14, y - 22), (x + i * 14 + 7, y - 12)], "#ef4444")
    return s + rect(x + 4, y - 12, 4, 12, "#374151") + rect(x + w - 8, y - 12, 4, 12, "#374151")


def machine(x, y):
    s = rect(x, y - 70, 90, 70, "#64748b", 4) + rect(x + 10, y - 60, 40, 30, "#334155", 3) + rect(x + 14, y - 56, 32, 22, "#22d3ee", 2, 'opacity=".55"')
    s += circ(x + 70, y - 52, 9, "#ef4444") + circ(x + 70, y - 28, 9, "#22c55e") + rect(x + 6, y - 20, 50, 8, "#475569", 2)
    s += circ(x + 20, y - 16, 4, "#94a3b8") + circ(x + 40, y - 16, 4, "#94a3b8")
    return s


def robot_arm(x, y):
    return rect(x - 18, y - 12, 36, 12, "#f59e0b", 3) + path(f"M{f(x)} {f(y - 12)} L{f(x - 10)} {f(y - 60)} L{f(x + 32)} {f(y - 82)}", stroke="#f59e0b", sw=10) + circ(x, y - 12, 7, "#d97706") + circ(x - 10, y - 60, 7, "#d97706") + path(f"M{f(x + 32)} {f(y - 82)} l8 6 M{f(x + 32)} {f(y - 82)} l10 -4", stroke="#374151", sw=3)


def conveyor(x, y, w=180):
    s = rect(x, y - 20, w, 12, "#374151", 6) + "".join(circ(x + 8 + i * 20, y - 14, 4, "#6b7280") for i in range(int(w / 20)))
    s += rect(x + 20, y - 34, 22, 14, "#a16207", 2) + rect(x + 90, y - 34, 22, 14, "#a16207", 2)
    return s + rect(x + 10, y - 8, 6, 8, "#4b5563") + rect(x + w - 16, y - 8, 6, 8, "#4b5563")


def turbine(x, y, h=150, s=1, rot=15):
    out = poly([(x - 4 * s, y), (x + 4 * s, y), (x + 2 * s, y - h), (x - 2 * s, y - h)], "#f8fafc", 'stroke="#cbd5e1" stroke-width="1"')
    for a in (rot, rot + 120, rot + 240):
        out += f'<g transform="rotate({a} {f(x)} {f(y - h)})">' + path(f"M{f(x)} {f(y - h)} q{f(6 * s)} -{f(30 * s)} 0 -{f(62 * s)} q-{f(4 * s)} {f(30 * s)} 0 {f(62 * s)} z", "#ffffff", extra='stroke="#cbd5e1" stroke-width="1"') + "</g>"
    return out + circ(x, y - h, 4 * s, "#e2e8f0", 'stroke="#94a3b8" stroke-width="1"')


def pylon(x, y, h=150):
    s = path(f"M{f(x - 22)} {f(y)} L{f(x - 5)} {f(y - h)} L{f(x + 5)} {f(y - h)} L{f(x + 22)} {f(y)}", stroke="#64748b", sw=2.5)
    for k in range(5):
        yy = y - k * h / 5
        w = 22 - k * 17 / 5
        s += line(x - w, yy, x + w * 0.8, yy - h / 5, "#64748b", 1.2) + line(x + w, yy, x - w * 0.8, yy - h / 5, "#64748b", 1.2)
    for yy, w in ((y - h * 0.78, 44), (y - h * 0.6, 34)):
        s += rect(x - w, yy, 2 * w, 3, "#64748b") + line(x - w, yy + 3, x - w, yy + 12, "#94a3b8", 2) + line(x + w, yy + 3, x + w, yy + 12, "#94a3b8", 2)
    return s


def bucket_truck(x, y, boom_to):
    bx, by = boom_to
    s = rect(x, y - 40, 120, 30, "#f59e0b", 4) + rect(x + 120, y - 50, 40, 40, "#f59e0b", 5) + rect(x + 128, y - 46, 24, 16, "#cfe8ff", 2)
    s += circ(x + 26, y - 8, 11, "#111827") + circ(x + 130, y - 8, 11, "#111827") + circ(x + 26, y - 8, 4, "#9ca3af") + circ(x + 130, y - 8, 4, "#9ca3af")
    s += line(x + 40, y - 40, bx, by + 14, "#e5e7eb", 7) + rect(bx - 16, by, 32, 22, "#f8fafc", 3, 'stroke="#94a3b8" stroke-width="1.5"')
    return s


def headset(cx, cy, s=1):
    return path(f"M{f(cx - 13 * s)} {f(cy)} q0 -18 {f(13 * s)} -18 q{f(13 * s)} 0 {f(13 * s)} 18", stroke="#111827", sw=2.5 * s) + rect(cx - 15 * s, cy - 4 * s, 5 * s, 9 * s, "#111827", 2) + rect(cx + 10 * s, cy - 4 * s, 5 * s, 9 * s, "#111827", 2)


def screen_wall(x, y, w, h):
    s = rect(x, y, w, h, "#0f172a", 4)
    cw = (w - 16) / 3
    for i in range(3):
        sx = x + 4 + i * (cw + 4)
        s += rect(sx, y + 4, cw, h - 8, "#111827", 2)
        if i == 0:
            s += path(f"M{f(sx + 6)} {f(y + h - 14)} l{f(cw * 0.2)} -{f(h * 0.3)} l{f(cw * 0.2)} {f(h * 0.15)} l{f(cw * 0.2)} -{f(h * 0.35)} l{f(cw * 0.25)} {f(h * 0.1)}", stroke="#22c55e", sw=2)
        elif i == 1:
            for k in range(6):
                s += circ(sx + 10 + (k * 37) % (cw - 20), y + 12 + (k * 23) % (h - 26), 3, "#facc15" if k != 3 else "#ef4444")
            s += path(f"M{f(sx + 10)} {f(y + 12)} L{f(sx + cw - 12)} {f(y + h - 16)} M{f(sx + 12)} {f(y + h - 18)} L{f(sx + cw - 14)} {f(y + 16)}", stroke="#38bdf8", sw=1.2)
        else:
            for k in range(5):
                s += rect(sx + 6, y + 8 + k * (h - 16) / 5, cw * (0.3 + (k * 0.17) % 0.6), 4, "#60a5fa")
    return s


def sign(x, y, t, w=70, c="#1e3a8a", fg="#ffffff"):
    return rect(x - w / 2, y - 16, w, 16, c, 3) + text(x, y - 5, t, 8, fg)


def sweat(x, y):
    return path(f"M{f(x)} {f(y)} q-3 5 0 7 q3 -2 0 -7 z", "#7dd3fc")


def card_yellow(x, y):
    return rect(x - 4, y - 12, 9, 12, "#facc15", 1)


def wall_tiles(y0, y1, c1="#e0f2fe", c2="#f0f9ff"):
    s = ""
    for r in range(int((y1 - y0) / 16)):
        for i in range(25):
            s += rect(i * 16 + (r % 2) * 8 - 8, y0 + r * 16, 15, 15, c1 if (i + r) % 2 else c2)
    return s


def fridge(x, y):
    return rect(x, y - 110, 50, 110, "#e5e7eb", 5) + rect(x, y - 72, 50, 2, "#9ca3af") + rect(x + 40, y - 100, 3, 18, "#9ca3af", 1) + rect(x + 40, y - 62, 3, 24, "#9ca3af", 1)


def shelf_items(x, y, w):
    s = rect(x, y, w, 4, "#8b5e3c")
    cols = ["#ef4444", "#22c55e", "#3b82f6", "#f59e0b", "#a855f7", "#14b8a6"]
    for i in range(int(w / 14)):
        s += rect(x + 2 + i * 14, y - 16 + (i % 3) * 3, 10, 16 - (i % 3) * 3, cols[i % 6], 2)
    return s


# ---------------- people ----------------
ARMS = {
    "down": ((20, -64), (21, -44)), "up": ((24, -104), (26, -124)), "out": ((32, -76), (48, -74)),
    "point": ((30, -90), (46, -104)), "hold": ((20, -62), (8, -66)), "shake": ((30, -68), (44, -64)),
    "ear": ((24, -72), (12, -98)), "hip": ((28, -66), (14, -54)), "type": ((22, -60), (12, -52)),
    "wave": ((32, -96), (38, -118)), "front": ((22, -66), (30, -58)), "cheer": ((26, -100), (34, -122)),
}


def person(x, y, skin=0, hair=0, top="#2563eb", bottom="#1e293b", hairstyle="short", arms=("down", "down"), s=1.0,
           sit=False, legs=True, face="smile", hat=None, glasses=False, beard=False, headphones=False, skirt=False,
           shoes="#111827", vest=None, tie=None, holding=None, lean=0, flip=False):
    """Front-facing figure. x,y = point between the feet (or hip when sit=True). Returns svg string."""
    S = SKIN[skin] if isinstance(skin, int) else skin
    H = HAIR[hair] if isinstance(hair, int) else hair
    out = []
    hip_y = y - 48 * s if not sit else y
    sh_y = hip_y - 40 * s
    head_y = sh_y - 16 * s
    if legs and not sit:
        if skirt:
            out.append(poly([(x - 15 * s, hip_y), (x + 15 * s, hip_y), (x + 20 * s, hip_y + 26 * s), (x - 20 * s, hip_y + 26 * s)], bottom))
            out.append(rect(x - 10 * s, hip_y + 26 * s, 6 * s, 20 * s, S) + rect(x + 4 * s, hip_y + 26 * s, 6 * s, 20 * s, S))
        else:
            out.append(rect(x - 14 * s, hip_y - 2 * s, 13 * s, 48 * s, bottom, 3 * s) + rect(x + 1 * s, hip_y - 2 * s, 13 * s, 48 * s, bottom, 3 * s))
        out.append(ell(x - 9 * s, y - 2 * s, 9 * s, 4 * s, shoes) + ell(x + 9 * s, y - 2 * s, 9 * s, 4 * s, shoes))
    if sit and legs:
        out.append(rect(x - 15 * s, hip_y - 4 * s, 30 * s, 12 * s, bottom, 5 * s))
        out.append(rect(x - 14 * s, hip_y + 6 * s, 12 * s, 30 * s, bottom, 3 * s) + rect(x + 2 * s, hip_y + 6 * s, 12 * s, 30 * s, bottom, 3 * s))
        out.append(ell(x - 9 * s, hip_y + 37 * s, 9 * s, 4 * s, shoes) + ell(x + 9 * s, hip_y + 37 * s, 9 * s, 4 * s, shoes))
    # arms behind torso when hands are low and in front? draw arms after torso so they read clearly
    torso = path(f"M{f(x - 17 * s)} {f(hip_y)} L{f(x - 18 * s)} {f(sh_y + 6 * s)} Q{f(x - 18 * s)} {f(sh_y)} {f(x - 10 * s)} {f(sh_y)} L{f(x + 10 * s)} {f(sh_y)} Q{f(x + 18 * s)} {f(sh_y)} {f(x + 18 * s)} {f(sh_y + 6 * s)} L{f(x + 17 * s)} {f(hip_y)} Z", top)
    out.append(rect(x - 4 * s, sh_y - 6 * s, 8 * s, 8 * s, S))
    out.append(torso)
    if vest:
        out.append(path(f"M{f(x - 17 * s)} {f(hip_y)} L{f(x - 18 * s)} {f(sh_y + 6 * s)} L{f(x - 7 * s)} {f(sh_y)} L{f(x - 4 * s)} {f(hip_y)} Z M{f(x + 17 * s)} {f(hip_y)} L{f(x + 18 * s)} {f(sh_y + 6 * s)} L{f(x + 7 * s)} {f(sh_y)} L{f(x + 4 * s)} {f(hip_y)} Z", vest))
        if vest in ("#f97316", "#facc15", "#a3e635"):
            out.append(rect(x - 17 * s, hip_y - 14 * s, 34 * s, 3 * s, "#e5e7eb"))
    if tie:
        out.append(poly([(x - 2.5 * s, sh_y + 1 * s), (x + 2.5 * s, sh_y + 1 * s), (x + 3.5 * s, sh_y + 22 * s), (x, sh_y + 26 * s), (x - 3.5 * s, sh_y + 22 * s)], tie))
        out.append(poly([(x - 7 * s, sh_y), (x, sh_y + 6 * s), (x + 7 * s, sh_y)], "#ffffff"))
    out.append(rect(x - 17 * s, hip_y - 3 * s, 34 * s, 4 * s, bottom, 1))
    sl = arms if not flip else (arms[1], arms[0])
    for side, a in ((-1, sl[0]), (1, sl[1])):
        (ex, ey), (hx, hy) = ARMS[a]
        sx, sy = x + side * 15 * s, sh_y + 5 * s
        e = (x + side * ex * s, hip_y + 48 * s + ey * s - (0 if not sit else 0))
        hnd = (x + side * hx * s, hip_y + 48 * s + hy * s)
        out.append(path(f"M{f(sx)} {f(sy)} L{f(e[0])} {f(e[1])} L{f(hnd[0])} {f(hnd[1])}", stroke=top, sw=9 * s))
        out.append(circ(hnd[0], hnd[1], 4.6 * s, S))
    # head
    hx, hy, r = x + lean * s, head_y - 2 * s, 13.5 * s
    if hairstyle == "long":
        out.append(rect(hx - 16 * s, hy - 6 * s, 9 * s, 30 * s, H, 4 * s) + rect(hx + 7 * s, hy - 6 * s, 9 * s, 30 * s, H, 4 * s))
    out.append(circ(hx - 13 * s, hy + 1 * s, 3 * s, S) + circ(hx + 13 * s, hy + 1 * s, 3 * s, S))
    out.append(circ(hx, hy, r, S))
    if hairstyle in ("short", "long", "bun", "side", "pony"):
        out.append(path(f"M{f(hx - r)} {f(hy + 1 * s)} Q{f(hx - r - 1 * s)} {f(hy - r - 3 * s)} {f(hx)} {f(hy - r - 1 * s)} Q{f(hx + r + 1 * s)} {f(hy - r - 3 * s)} {f(hx + r)} {f(hy + 1 * s)} Q{f(hx + 4 * s)} {f(hy - 9 * s)} {f(hx - 6 * s)} {f(hy - 7 * s)} Q{f(hx - 10 * s)} {f(hy - 4 * s)} {f(hx - r)} {f(hy + 1 * s)} Z", H))
    if hairstyle == "bun":
        out.append(circ(hx, hy - r - 4 * s, 6 * s, H))
    if hairstyle == "pony":
        out.append(ell(hx + r + 2 * s, hy + 4 * s, 4 * s, 10 * s, H))
    if hairstyle == "curly":
        out.append("".join(circ(hx + math.cos(math.radians(a)) * r * 0.95, hy + math.sin(math.radians(a)) * r * 0.95, 5 * s, H) for a in range(180, 361, 30)))
    if hairstyle == "bald":
        out.append(path(f"M{f(hx - r)} {f(hy)} q-1 -6 2 -8 M{f(hx + r)} {f(hy)} q1 -6 -2 -8", stroke=H, sw=3 * s))
    # face
    ey_ = hy + 1 * s
    if face == "closed":
        out.append(path(f"M{f(hx - 7 * s)} {f(ey_)} q2 -2 4 0 M{f(hx + 3 * s)} {f(ey_)} q2 -2 4 0", stroke=INK, sw=1.4 * s))
    else:
        out.append(circ(hx - 5 * s, ey_, 1.5 * s, INK) + circ(hx + 5 * s, ey_, 1.5 * s, INK))
    if face == "smile":
        out.append(path(f"M{f(hx - 5 * s)} {f(hy + 6 * s)} Q{f(hx)} {f(hy + 10 * s)} {f(hx + 5 * s)} {f(hy + 6 * s)}", stroke=INK, sw=1.4 * s))
    elif face in ("laugh", "shout"):
        out.append(path(f"M{f(hx - 5 * s)} {f(hy + 5 * s)} Q{f(hx)} {f(hy + 14 * s)} {f(hx + 5 * s)} {f(hy + 5 * s)} Z", "#7f1d1d"))
    elif face == "worried":
        out.append(path(f"M{f(hx - 4 * s)} {f(hy + 9 * s)} Q{f(hx)} {f(hy + 5 * s)} {f(hx + 4 * s)} {f(hy + 9 * s)}", stroke=INK, sw=1.4 * s))
        out.append(path(f"M{f(hx - 8 * s)} {f(ey_ - 5 * s)} l5 -2 M{f(hx + 8 * s)} {f(ey_ - 5 * s)} l-5 -2", stroke=INK, sw=1.3 * s))
    elif face == "focus":
        out.append(line(hx - 3 * s, hy + 7 * s, hx + 3 * s, hy + 7 * s, INK, 1.4 * s))
        out.append(path(f"M{f(hx - 8 * s)} {f(ey_ - 4 * s)} l5 1 M{f(hx + 8 * s)} {f(ey_ - 4 * s)} l-5 1", stroke=INK, sw=1.3 * s))
    elif face == "neutral":
        out.append(line(hx - 3 * s, hy + 7 * s, hx + 3 * s, hy + 7 * s, INK, 1.4 * s))
    out.append(circ(hx - 8 * s, hy + 5 * s, 2.2 * s, "#f87171", 'opacity=".35"') + circ(hx + 8 * s, hy + 5 * s, 2.2 * s, "#f87171", 'opacity=".35"'))
    if beard:
        out.append(path(f"M{f(hx - r + 1 * s)} {f(hy + 2 * s)} Q{f(hx - r + 2 * s)} {f(hy + r + 3 * s)} {f(hx)} {f(hy + r + 2 * s)} Q{f(hx + r - 2 * s)} {f(hy + r + 3 * s)} {f(hx + r - 1 * s)} {f(hy + 2 * s)} Q{f(hx + 6 * s)} {f(hy + 10 * s)} {f(hx)} {f(hy + 9 * s)} Q{f(hx - 6 * s)} {f(hy + 10 * s)} {f(hx - r + 1 * s)} {f(hy + 2 * s)} Z", H))
        if face == "smile":
            out.append(path(f"M{f(hx - 4 * s)} {f(hy + 6 * s)} Q{f(hx)} {f(hy + 9 * s)} {f(hx + 4 * s)} {f(hy + 6 * s)}", stroke="#fff", sw=1.2 * s))
    if glasses:
        out.append(circ(hx - 5 * s, ey_, 4 * s, "none", f'stroke="{INK}" stroke-width="{f(1.2 * s)}"') + circ(hx + 5 * s, ey_, 4 * s, "none", f'stroke="{INK}" stroke-width="{f(1.2 * s)}"') + line(hx - 1 * s, ey_, hx + 1 * s, ey_, INK, 1.2 * s))
    if hat == "helmet":
        out.append(path(f"M{f(hx - r - 3 * s)} {f(hy - 3 * s)} Q{f(hx)} {f(hy - r * 2.1)} {f(hx + r + 3 * s)} {f(hy - 3 * s)} Z", "#facc15") + rect(hx - r - 5 * s, hy - 5 * s, 2 * r + 10 * s, 4 * s, "#eab308", 2))
    elif hat == "helmet_w":
        out.append(path(f"M{f(hx - r - 3 * s)} {f(hy - 3 * s)} Q{f(hx)} {f(hy - r * 2.1)} {f(hx + r + 3 * s)} {f(hy - 3 * s)} Z", "#f8fafc") + rect(hx - r - 5 * s, hy - 5 * s, 2 * r + 10 * s, 4 * s, "#e2e8f0", 2))
    elif hat == "chef":
        out.append(rect(hx - 11 * s, hy - r - 6 * s, 22 * s, 9 * s, "#ffffff") + circ(hx - 8 * s, hy - r - 10 * s, 7 * s, "#ffffff") + circ(hx + 8 * s, hy - r - 10 * s, 7 * s, "#ffffff") + circ(hx, hy - r - 14 * s, 8 * s, "#ffffff"))
    elif hat == "cap":
        out.append(path(f"M{f(hx - r)} {f(hy - 3 * s)} Q{f(hx)} {f(hy - r * 2)} {f(hx + r)} {f(hy - 3 * s)} Z", "#dc2626") + rect(hx - 2 * s, hy - 5 * s, r + 8 * s, 3.5 * s, "#b91c1c", 2))
    if headphones:
        out.append(headset(hx, hy, s))
    if holding:
        out.append(holding)
    return "".join(out)


def svg(*parts):
    return '<svg viewBox="0 0 400 260" xmlns="http://www.w3.org/2000/svg" role="img">' + "".join(parts) + "</svg>"
