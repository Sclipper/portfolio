# Generates the three schematic plates as inline SVG snippets.
import html
def esc(s): return html.escape(s, quote=False)

class D:
    def __init__(s, w, h, title):
        s.w, s.h, s.out = w, h, []
        s.title = title
    def node(s, x, y, w, h, title, lines=(), accent=False, cls=""):
        c = "n n--accent" if accent else "n"
        s.out.append(f'<g class="{c} {cls}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3"/>')
        s.out.append(f'<text class="t" x="{x+16}" y="{y+28}">{esc(title)}</text>')
        for i, l in enumerate(lines):
            s.out.append(f'<text class="s" x="{x+16}" y="{y+50+i*19}">{esc(l)}</text>')
        s.out.append('</g>')
    def zone(s, x, y, w, h, label):
        s.out.append(f'<g class="z"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4"/><text class="zl" x="{x+16}" y="{y-10}">{esc(label)}</text></g>')
    def col(s, x, y, label):
        s.out.append(f'<text class="col" x="{x}" y="{y}">{esc(label)}</text>')
    def arrow(s, pts, label=None, lx=None, ly=None, accent=False, dashed=False):
        d = "M" + " L".join(f"{a},{b}" for a, b in pts)
        cls = "a" + (" a--accent" if accent else "") + (" a--dash" if dashed else "")
        s.out.append(f'<path class="{cls}" d="{d}" marker-end="url(#{"ha" if accent else "h"})"/>')
        if label:
            s.out.append(f'<text class="al" x="{lx}" y="{ly}">{esc(label)}</text>')
    def text(s, x, y, t, cls="s"):
        s.out.append(f'<text class="{cls}" x="{x}" y="{y}">{esc(t)}</text>')
    def block(s, x, y, rows):
        # title block, bottom right, like a drawing sheet
        w = 380; rh = 30
        s.out.append(f'<g class="tb"><rect x="{x}" y="{y}" width="{w}" height="{rh*len(rows)}"/>')
        for i, (k, v) in enumerate(rows):
            yy = y + i*rh
            if i: s.out.append(f'<line x1="{x}" y1="{yy}" x2="{x+w}" y2="{yy}"/>')
            s.out.append(f'<line x1="{x+110}" y1="{yy}" x2="{x+110}" y2="{yy+rh}"/>')
            s.out.append(f'<text class="tbk" x="{x+12}" y="{yy+20}">{esc(k)}</text><text class="tbv" x="{x+124}" y="{yy+20}">{esc(v)}</text>')
        s.out.append('</g>')
    def svg(s, idattr, label):
        defs = ('<defs>'
          '<marker id="h" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9" class="hd"/></marker>'
          '<marker id="ha" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9" class="hd hd--accent"/></marker>'
          '</defs>')
        return (f'<svg class="dg" id="{idattr}" viewBox="0 0 {s.w} {s.h}" role="img" aria-label="{html.escape(label)}">' + defs + "".join(s.out) + '</svg>')

# ---------------- Hyperion ----------------
h = D(1264, 800, "Hyperion")
X = [40, 286, 532, 778, 1024]; W = 200
for x, c in zip(X, ["Sources", "Ingest", "Store and research", "Decide", "Execute"]):
    h.col(x, 58, c)
h.node(X[0], 90, W, 78, "Research portals", ["institutional macro"])
h.node(X[0], 198, W, 78, "Market data", ["historical and live"])
h.node(X[0], 306, W, 78, "News and picks", ["feeds and scrapers"])
h.node(X[1], 90, W, 118, "Research ingestion", ["browser automation", "LLM: PDF to rows", "one module per source"])
h.node(X[1], 238, W, 78, "Data gateways", ["normalised feeds"])
h.node(X[2], 90, W, 78, "PostgreSQL", ["and a data lake"])
h.node(X[2], 198, W, 78, "Backtesting", ["on the LEAN engine"])
h.node(X[2], 306, W, 78, "Simulation", ["Monte Carlo, factors"])
h.node(X[3], 90, W, 78, "Market scanner", ["assets x timeframes"])
h.node(X[3], 198, W, 118, "LLM agents", ["tool calling over", "macro, market regime", "and indicators"], accent=True)
h.node(X[3], 346, W, 78, "Trade signals", ["entry, target, stop"])
h.node(X[4], 90, W, 78, "Order gateway", ["checks, timeouts"])
h.node(X[4], 198, W, 78, "Broker APIs", ["Alpaca and others"])
h.node(X[4], 306, W, 78, "Ledger", ["and reconciler"])
g = 23
h.arrow([(X[0]+W, 129), (X[1]-4, 129)])
h.arrow([(X[0]+W, 237), (X[0]+W+g, 237), (X[0]+W+g, 277), (X[1]-4, 277)])
h.arrow([(X[0]+W, 345), (X[0]+W+g, 345), (X[0]+W+g, 290), (X[1]-4, 290)])
h.arrow([(X[1]+W, 129), (X[2]-4, 129)])
h.arrow([(X[1]+W, 277), (X[1]+W+g, 277), (X[1]+W+g, 150), (X[2]-4, 150)])
h.arrow([(X[2]+W/2, 168), (X[2]+W/2, 194)])
h.arrow([(X[2]+W/2, 276), (X[2]+W/2, 302)])
h.arrow([(X[2]+W, 140), (X[2]+W+g, 140), (X[2]+W+g, 240), (X[3]-4, 240)], accent=True)
h.arrow([(X[2]+W, 345), (X[2]+W+g, 345), (X[2]+W+g, 275), (X[3]-4, 275)])
h.arrow([(X[3]+W/2, 168), (X[3]+W/2, 194)])
h.arrow([(X[3]+W/2, 316), (X[3]+W/2, 342)], accent=True)
h.arrow([(X[3]+W, 385), (X[3]+W+g, 385), (X[3]+W+g, 129), (X[4]-4, 129)])
h.arrow([(X[4]+W/2, 168), (X[4]+W/2, 194)])
h.arrow([(X[4]+W/2, 276), (X[4]+W/2, 302)], "fills", X[4]+W/2+12, 294)
h.zone(40, 486, 1184, 108, "Operations")
for i, (t, sub) in enumerate([("Market-status monitor", "opens, halts, holidays"), ("Logging", "structured, per service"), ("Track record", "dashboards, reports"), ("Slack assistant", "plain-language answers")]):
    h.node(62 + i*292, 508, 270, 66, t, [sub], cls="n--small")
h.block(844, 650, [("Sheet", "3 of 8"), ("Work", "Hyperion, systems schematic"), ("Scale", "None. Boxes are duties"), ("Withheld", "Code, strategy, results")])
h.text(40, 670, "Legend", "lg")
h.out.append('<rect class="n--accent lgbox" x="40" y="688" width="24" height="17" rx="2"/>')
h.text(78, 702, "where language models do the work", "s")
h.out.append('<path class="a" d="M40,736 L64,736" marker-end="url(#h)"/>')
h.text(78, 741, "data and control flow", "s")

# ---------------- MCP: a sequence drawing ----------------
m = D(1264, 740, "MCP")
L = [170, 490, 810, 1110]
heads = [("Assistant", "Claude, ChatGPT"), ("TaxMate issuer", "OAuth 2.1, OIDC"), ("MCP server", "Streamable HTTP"), ("TaxMate API", "public /v1")]
for i, (x, (t, sub)) in enumerate(zip(L, heads)):
    m.node(x-120, 40, 240, 78, t, [sub], accent=(i == 2))
    m.out.append(f'<line class="life" x1="{x}" y1="118" x2="{x}" y2="606"/>')
rows = [
  (0, 1, "1  Sign in, pick companies", False, False),
  (1, 3, "2  Verify each company's API token", False, True),
  (1, 0, "3  Access token: ES256, 300 seconds", False, False),
  (0, 2, "4  Tool call, carrying the token", True, False),
  (2, 1, "5  Is the grant still live?", False, True),
  (2, 3, "6  Call /v1 as that company only", True, False),
  (2, 0, "7  Result", False, True),
]
y = 180
for a, b, lab, acc, dash in rows:
    xa, xb = L[a], L[b]
    end = xb - 6 if xb > xa else xb + 6
    m.arrow([(xa, y), (end, y)], lab, min(xa, xb) + 16, y - 12, accent=acc, dashed=dash)
    y += 66
m.block(844, 640, [("Sheet", "2 of 8"), ("Work", "TaxMate for AI assistants"), ("Scopes", "mcp:read, mcp:write")])
m.text(40, 662, "Refresh tokens rotate; reuse or a wider scope is refused.", "s")
m.text(40, 688, "Revoking a grant stops the very next call.", "s")

# ---------------- opencal ----------------
o = D(1264, 560, "opencal")
o.col(40, 58, "Calendars"); o.col(316, 58, "Broker"); o.col(1024, 58, "Out")
o.node(40, 96, 226, 78, "Google Calendar", ["incremental sync"])
o.node(40, 240, 226, 78, "Outlook", ["whole window, diffed"])
o.node(316, 96, 200, 222, "Composio", ["calendar API calls", "on your own keys", "", "free tier:", "20,000 calls a month"])
o.zone(574, 88, 400, 330, "Your server: one Docker container")
o.node(598, 108, 352, 66, "Poller", ["every 5 minutes, per source calendar"])
o.node(598, 194, 352, 84, "Mapping table", ["SQLite. Makes every write idempotent", "and stops sync loops."], accent=True)
o.node(598, 298, 352, 100, "Writer", ["Busy blockers or full clones, one", "way or both. Free events and", "attendees are never copied."])
o.node(1024, 108, 200, 96, "Availability", ["your merged free", "slots, /a/your-slug"])
o.arrow([(266, 135), (312, 135)]); o.arrow([(266, 279), (312, 279)])
o.arrow([(516, 141), (594, 141)])
o.arrow([(774, 174), (774, 190)]); o.arrow([(774, 278), (774, 294)], accent=True)
o.arrow([(598, 350), (545, 350), (545, 290), (520, 290)], "writes back", 470, 378)
o.arrow([(974, 156), (1020, 156)])
o.block(844, 460, [("Sheet", "7 of 8"), ("Work", "opencal-sync, data flow"), ("Licence", "MIT")])

import json
open("diagrams.json", "w").write(json.dumps({"hyperion": h.svg("dg-hyperion", "x"), "mcp": m.svg("dg-mcp", "x"), "opencal": o.svg("dg-opencal", "x")}))
print("ok")
