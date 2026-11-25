import os, sys

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)

G = "#1D9470"; T = "#2dd4bf"; M = "#b8f5dc"; BG = "#0d1117"; BG2 = "#07110e"
MONO = "'JetBrains Mono',SFMono-Regular,Consolas,'Liberation Mono',Menlo,monospace"
SANS = "'Segoe UI',Ubuntu,'Helvetica Neue',Helvetica,Arial,sans-serif"
CW = 0.6  # monospace advance per font-size unit (enforced via textLength)


def w(name, s):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + s)


def mlen(text, size):
    return round(len(text) * size * CW, 1)


BASE_DEFS = f"""
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{BG2}"/><stop offset="1" stop-color="{BG}"/></linearGradient>
    <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="{G}" stroke-opacity="0.08"/></pattern>
    <radialGradient id="glow" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="{G}" stop-opacity=".45"/><stop offset="1" stop-color="{G}" stop-opacity="0"/></radialGradient>
    <linearGradient id="sweep" x1="0" x2="1"><stop offset="0" stop-color="{T}" stop-opacity="0"/><stop offset=".5" stop-color="{T}"/><stop offset="1" stop-color="{T}" stop-opacity="0"/></linearGradient>"""

BASE_CSS = f"""
      .mono{{font-family:{MONO}}} .sans{{font-family:{SANS}}}
      @keyframes rise{{from{{opacity:0;transform:translateY(14px)}}to{{opacity:1;transform:translateY(0)}}}}
      @keyframes blink{{0%,49%{{opacity:1}}50%,100%{{opacity:0}}}}
      @keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.25}}}}
      @keyframes draw{{to{{stroke-dashoffset:0}}}}
      @keyframes drift{{0%,100%{{transform:translate(0,0)}}50%{{transform:translate(60px,-12px)}}}}
      .cur{{animation:blink 1s step-end infinite}}
      .dot{{animation:pulse 2s ease-in-out infinite}}
      .drift{{animation:drift 12s ease-in-out infinite}}"""


# ---------------------------------------------------------------- header
def header():
    who = "drlnx@github:~$"
    w("header.svg", f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 340" width="1200" height="340" role="img" aria-label="Leon — Dr.Lnx, Developer at N3XT Agency">
  <defs>{BASE_DEFS}
    <linearGradient id="title" x1="0" x2="1"><stop offset="0" stop-color="#fff"/><stop offset=".6" stop-color="{M}"/><stop offset="1" stop-color="{G}"/></linearGradient>
    <radialGradient id="glow2" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="{T}" stop-opacity=".3"/><stop offset="1" stop-color="{T}" stop-opacity="0"/></radialGradient>
    <linearGradient id="scan" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{G}" stop-opacity="0"/><stop offset=".85" stop-color="{G}" stop-opacity=".16"/><stop offset="1" stop-color="{T}" stop-opacity="0"/></linearGradient>
    <clipPath id="frame"><rect width="1200" height="340" rx="18"/></clipPath>
    <style>{BASE_CSS}
      @keyframes drift2{{0%,100%{{transform:translate(0,0)}}50%{{transform:translate(-80px,30px)}}}}
      @keyframes scan{{from{{transform:translateY(-120px)}}to{{transform:translateY(340px)}}}}
      @keyframes spin{{to{{transform:rotate(360deg)}}}}
      @keyframes spinr{{to{{transform:rotate(-360deg)}}}}
      @keyframes ping{{0%{{transform:scale(1);opacity:.8}}100%{{transform:scale(3);opacity:0}}}}
      @keyframes flow{{to{{stroke-dashoffset:-40}}}}
      .o2{{animation:drift2 18s ease-in-out infinite}}
      .scan{{animation:scan 6s linear infinite}}
      .r1{{opacity:0;animation:rise .8s cubic-bezier(.2,.8,.2,1) .1s forwards}}
      .r2{{opacity:0;animation:rise .8s cubic-bezier(.2,.8,.2,1) .35s forwards}}
      .r3{{opacity:0;animation:rise .8s cubic-bezier(.2,.8,.2,1) .6s forwards}}
      .r4{{opacity:0;animation:rise .8s cubic-bezier(.2,.8,.2,1) .85s forwards}}
      .line{{stroke-dasharray:260;stroke-dashoffset:260;animation:draw 1.4s ease-out .5s forwards}}
      .ring1{{transform-origin:965px 170px;animation:spin 22s linear infinite}}
      .ring2{{transform-origin:965px 170px;animation:spinr 14s linear infinite}}
      .ring3{{transform-origin:965px 170px;animation:spin 9s linear infinite}}
      .ping{{transform-origin:92px 286px;animation:ping 2s ease-out infinite}}
      .wire{{stroke-dasharray:6 14;animation:flow 1.6s linear infinite}}
    </style>
  </defs>
  <g clip-path="url(#frame)">
    <rect width="1200" height="340" fill="url(#bg)"/>
    <rect width="1200" height="340" fill="url(#grid)"/>
    <circle class="drift" cx="260" cy="90" r="260" fill="url(#glow)"/>
    <circle class="o2" cx="980" cy="290" r="240" fill="url(#glow2)"/>
    <rect class="scan" width="1200" height="120" fill="url(#scan)"/>
    <circle class="ring1" cx="965" cy="170" r="118" fill="none" stroke="{G}" stroke-opacity=".45" stroke-width="1.5" stroke-dasharray="2 10"/>
    <g class="ring2"><circle cx="965" cy="170" r="88" fill="none" stroke="{T}" stroke-opacity=".55" stroke-width="2" stroke-dasharray="120 60 30 60"/><circle cx="1053" cy="170" r="5" fill="{T}"/></g>
    <g class="ring3"><circle cx="965" cy="170" r="56" fill="none" stroke="{G}" stroke-width="2.5" stroke-dasharray="60 28"/><circle cx="965" cy="114" r="4" fill="{M}"/></g>
    <rect x="935" y="140" width="60" height="60" rx="14" fill="{BG}" stroke="{G}" stroke-width="2"/>
    <text x="965" y="178" text-anchor="middle" class="mono" font-size="20" font-weight="700" fill="{M}">N3</text>
    <g fill="none" stroke="{G}" stroke-opacity=".7" stroke-width="1.5"><path class="wire" d="M847 170H790"/><path class="wire" d="M965 52V20"/><path class="wire" d="M965 288V320"/></g>
    <g class="r1"><text x="70" y="88" class="mono" font-size="16" fill="{G}">{who} <tspan fill="#c9d1d9">whoami</tspan><tspan class="cur" fill="{G}">▍</tspan></text></g>
    <g class="r2"><text x="64" y="178" class="sans" font-size="96" font-weight="800" letter-spacing="-2" fill="url(#title)">Leon</text></g>
    <path class="line" d="M70 200H330" stroke="{G}" stroke-width="3" stroke-linecap="round"/>
    <g class="r3"><text x="70" y="240" class="sans" font-size="24" fill="#e6edf3"><tspan font-weight="700" fill="{M}">Dr.Lnx</tspan> <tspan fill="{G}">·</tspan> Developer at <tspan font-weight="700" fill="{M}">N3XT Agency</tspan></text></g>
    <g class="r4">
      <rect x="70" y="268" width="292" height="36" rx="18" fill="{G}" fill-opacity=".12" stroke="{G}" stroke-opacity=".5"/>
      <circle class="ping" cx="92" cy="286" r="5" fill="none" stroke="{T}" stroke-width="2"/>
      <circle class="dot" cx="92" cy="286" r="5" fill="{T}"/>
      <text x="108" y="291" class="mono" font-size="14" fill="#c9d1d9">currently building <tspan fill="{M}" font-weight="700">N3XT.sys</tspan></text>
    </g>
  </g>
  <rect x=".75" y=".75" width="1198.5" height="338.5" rx="17.5" fill="none" stroke="{G}" stroke-opacity=".35" stroke-width="1.5"/>
</svg>
""")


# ---------------------------------------------------------------- typing line
def typing():
    lines = [
        "Discord systems · Automation · Internal tooling",
        "Private platforms for communities",
        "One codebase. One dataset. One instance.",
        "If it runs twice, it runs on a cron.",
    ]
    size, W, H = 20, 760, 60
    n, slot = len(lines), 5.0
    cyc = n * slot
    css, body = [], []
    for i, ln in enumerate(lines):
        L = mlen(ln, size)
        x0 = (W - L) / 2
        a_type = 1.6 / cyc * 100       # typing
        a_hold = (slot - 0.9) / cyc * 100  # end of hold
        a_del = (slot - 0.3) / cyc * 100   # erased
        a_end = slot / cyc * 100
        css.append(f"""@keyframes c{i}{{0%{{transform:translateX(0);animation-timing-function:steps({len(ln)})}}{a_type:.3f}%{{transform:translateX({L}px)}}{a_hold:.3f}%{{transform:translateX({L}px);animation-timing-function:steps({len(ln)})}}{a_del:.3f}%,100%{{transform:translateX(0)}}}}
      @keyframes v{i}{{0%,{a_end-0.01:.3f}%{{visibility:visible}}{a_end:.3f}%,100%{{visibility:hidden}}}}
      .g{i}{{visibility:hidden;animation:v{i} {cyc}s linear {i*slot}s infinite}}
      .k{i}{{animation:c{i} {cyc}s linear {i*slot}s infinite}}""")
        body.append(f"""<g class="g{i}">
      <text x="{x0:.1f}" y="37" class="mono" font-size="{size}" font-weight="600" fill="{G}" textLength="{L}" lengthAdjust="spacingAndGlyphs">{ln}</text>
      <g class="k{i}"><rect x="{x0:.1f}" y="8" width="{L+40}" height="44" fill="{BG}"/><rect x="{x0+1:.1f}" y="18" width="3" height="26" fill="{T}" class="cur"/></g>
    </g>""")
    w("typing.svg", f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{' / '.join(lines)}">
  <defs><clipPath id="c"><rect x="1" y="1" width="{W-2}" height="{H-2}" rx="29"/></clipPath>
    <style>{BASE_CSS}
      {chr(10).join(css)}
    </style></defs>
  <rect x="1" y="1" width="{W-2}" height="{H-2}" rx="29" fill="{BG}" stroke="{G}" stroke-opacity=".4"/>
  <g clip-path="url(#c)">
    {chr(10).join(body)}
  </g>
</svg>
""")


# ---------------------------------------------------------------- buttons
GLOBE = '<circle cx="0" cy="0" r="9" fill="none" stroke="currentColor" stroke-width="1.8"/><ellipse cx="0" cy="0" rx="4" ry="9" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M-9 0H9" stroke="currentColor" stroke-width="1.8"/>'
MAIL = '<rect x="-10" y="-7" width="20" height="14" rx="2.5" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M-9 -5.5L0 1.5L9 -5.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/>'
ARROW = '<path d="M-5 0H5M1 -4L5 0L1 4" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>'


def button(name, icon, label, value, primary):
    ls, vs = 12, 15
    lw, vw = mlen(label, ls), mlen(value, vs)
    W = round(56 + lw + 18 + vw + 50)
    H = 52
    fill = G if primary else "#161b22"
    vcol = "#ffffff" if primary else M
    lcol = "#d9fff0" if primary else "#8b949e"
    icol = "#ffffff" if primary else G
    w(name, f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{label}: {value}">
  <defs>{BASE_DEFS}
    <clipPath id="c"><rect width="{W}" height="{H}" rx="12"/></clipPath>
    <style>{BASE_CSS}
      @keyframes shine{{0%,55%{{transform:translateX(-120px) skewX(-20deg)}}100%{{transform:translateX({W+120}px) skewX(-20deg)}}}}
      @keyframes nudge{{0%,70%,100%{{transform:translateX(0)}}85%{{transform:translateX(4px)}}}}
      .shine{{animation:shine 4s ease-in-out infinite}}
      .nudge{{animation:nudge 2.4s ease-in-out infinite}}
    </style></defs>
  <g clip-path="url(#c)">
    <rect width="{W}" height="{H}" fill="{fill}"/>
    {'' if primary else f'<rect width="{W}" height="{H}" fill="url(#grid)"/>'}
    <rect class="shine" x="-100" y="-10" width="60" height="{H+20}" fill="#fff" fill-opacity="{.18 if primary else .07}"/>
  </g>
  <rect x=".75" y=".75" width="{W-1.5}" height="{H-1.5}" rx="11.25" fill="none" stroke="{T if primary else G}" stroke-opacity="{.7 if primary else .55}" stroke-width="1.5"/>
  <g transform="translate(30 26)" color="{icol}">{icon}</g>
  <text x="56" y="31" class="mono" font-size="{ls}" font-weight="600" letter-spacing="1" fill="{lcol}" textLength="{lw}" lengthAdjust="spacingAndGlyphs">{label}</text>
  <text x="{56+lw+18}" y="32" class="mono" font-size="{vs}" font-weight="700" fill="{vcol}" textLength="{vw}" lengthAdjust="spacingAndGlyphs">{value}</text>
  <g transform="translate({W-24} 26)" color="{vcol}"><g class="nudge">{ARROW}</g></g>
</svg>
""")


# ---------------------------------------------------------------- nav pills
def nav(name, idx, label):
    s = 14
    lw = mlen(label, s)
    W, H = round(lw + 70), 40
    w(name, f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{label}">
  <defs><style>{BASE_CSS}
      @keyframes glow{{0%,100%{{stroke-opacity:.35}}50%{{stroke-opacity:.9}}}}
      .b{{animation:glow 3s ease-in-out {idx*0.4:.1f}s infinite}}
  </style></defs>
  <rect class="b" x=".75" y=".75" width="{W-1.5}" height="{H-1.5}" rx="19.25" fill="{BG}" stroke="{G}" stroke-width="1.5"/>
  <text x="18" y="25" class="mono" font-size="12" fill="{G}">{idx:02d}</text>
  <text x="44" y="25.5" class="mono" font-size="{s}" font-weight="600" fill="#e6edf3" textLength="{lw}" lengthAdjust="spacingAndGlyphs">{label}</text>
</svg>
""")


# ---------------------------------------------------------------- section headlines
def section(name, idx, title, tag, deco):
    W, H = 1200, 120
    tw = len(title) * 40 * 0.56  # rough sans width for line start
    line_x = 150 + tw + 30
    deco_svg = {
        "bars": "".join(f'<rect class="eq" style="animation-delay:{i*0.13:.2f}s" x="{1040+i*14}" y="40" width="7" height="40" rx="2" fill="{G if i%2 else T}"/>' for i in range(9)),
        "nodes": f'<g fill="none" stroke="{G}" stroke-width="1.5"><path class="flow" d="M1030 60H1080V36H1130M1080 60V84H1150"/></g>'
                 + "".join(f'<circle class="dot" style="animation-delay:{d}s" cx="{x}" cy="{y}" r="5" fill="{T}"/>' for x, y, d in [(1030,60,0),(1130,36,.5),(1150,84,1)])
                 + f'<rect x="1068" y="48" width="24" height="24" rx="6" fill="{BG}" stroke="{M}" stroke-width="1.5"/>',
        "stack": "".join(f'<g class="stk" style="animation-delay:{i*0.25:.2f}s"><path d="M1095 {38+i*16}l40 12-40 12-40-12z" fill="{G}" fill-opacity="{.25+i*.2:.2f}" stroke="{T}" stroke-width="1.2"/></g>' for i in range(3)),
        "gear": f'<g class="spin"><circle cx="1095" cy="60" r="22" fill="none" stroke="{G}" stroke-width="7" stroke-dasharray="8 6.4"/><circle cx="1095" cy="60" r="15" fill="none" stroke="{T}" stroke-width="2"/></g><circle class="dot" cx="1095" cy="60" r="4" fill="{M}"/>',
        "signal": "".join(f'<circle class="wave" style="animation-delay:{i*0.6:.1f}s" cx="1095" cy="60" r="8" fill="none" stroke="{T}" stroke-width="2"/>' for i in range(3)) + f'<circle cx="1095" cy="60" r="6" fill="{T}"/>',
    }[deco]
    w(name, f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{title}">
  <defs>{BASE_DEFS}
    <clipPath id="frame"><rect width="{W}" height="{H}" rx="16"/></clipPath>
    <linearGradient id="tt" x1="0" x2="1"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="{M}"/></linearGradient>
    <style>{BASE_CSS}
      @keyframes sweep{{from{{transform:translateX(-300px)}}to{{transform:translateX({W}px)}}}}
      @keyframes eq{{0%,100%{{transform:scaleY(.25)}}50%{{transform:scaleY(1)}}}}
      @keyframes flowk{{to{{stroke-dashoffset:-36}}}}
      @keyframes stk{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-5px)}}}}
      @keyframes spin{{to{{transform:rotate(360deg)}}}}
      @keyframes wave{{0%{{transform:scale(1);opacity:.9}}100%{{transform:scale(4.5);opacity:0}}}}
      .sw{{animation:sweep 5s cubic-bezier(.6,0,.4,1) infinite}}
      .t1{{opacity:0;animation:rise .7s cubic-bezier(.2,.8,.2,1) .1s forwards}}
      .t2{{opacity:0;animation:rise .7s cubic-bezier(.2,.8,.2,1) .3s forwards}}
      .ln{{stroke-dasharray:1000;stroke-dashoffset:1000;animation:draw 1.6s ease-out .5s forwards}}
      .eq{{transform-box:fill-box;transform-origin:center;animation:eq 1.2s ease-in-out infinite}}
      .flow{{stroke-dasharray:6 12;animation:flowk 1.4s linear infinite}}
      .stk{{animation:stk 2.4s ease-in-out infinite}}
      .spin{{transform-origin:1095px 60px;animation:spin 8s linear infinite}}
      .wave{{transform-origin:1095px 60px;animation:wave 1.8s ease-out infinite}}
    </style>
  </defs>
  <g clip-path="url(#frame)">
    <rect width="{W}" height="{H}" fill="url(#bg)"/>
    <rect width="{W}" height="{H}" fill="url(#grid)"/>
    <circle class="drift" cx="120" cy="60" r="160" fill="url(#glow)"/>
    <rect class="sw" x="0" y="{H-3}" width="300" height="3" fill="url(#sweep)"/>
  </g>
  <rect x=".75" y=".75" width="{W-1.5}" height="{H-1.5}" rx="15.25" fill="none" stroke="{G}" stroke-opacity=".35" stroke-width="1.5"/>
  <text x="44" y="78" class="mono" font-size="48" font-weight="700" fill="none" stroke="{G}" stroke-width="1.5">{idx:02d}</text>
  <path d="M128 30V90" stroke="{G}" stroke-opacity=".5"/>
  <g class="t1"><text x="150" y="46" class="mono" font-size="14" fill="{G}">{tag}<tspan class="cur">▍</tspan></text></g>
  <g class="t2"><text x="148" y="88" class="sans" font-size="40" font-weight="800" letter-spacing="-.5" fill="url(#tt)">{title}</text></g>
  <path class="ln" d="M{line_x:.0f} 74H990" stroke="{G}" stroke-opacity=".6" stroke-width="1.5" stroke-dasharray="4 6"/>
  {deco_svg}
</svg>
""")


# ---------------------------------------------------------------- divider
def divider():
    w("divider.svg", f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 12" width="1200" height="12" preserveAspectRatio="none">
  <defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="{G}" stop-opacity="0"/><stop offset=".5" stop-color="{T}"/><stop offset="1" stop-color="{G}" stop-opacity="0"/></linearGradient>
  <style>@keyframes s{{from{{transform:translateX(-400px)}}to{{transform:translateX(1200px)}}}}.s{{animation:s 3.5s cubic-bezier(.6,0,.4,1) infinite}}</style></defs>
  <rect y="5" width="1200" height="2" rx="1" fill="{G}" fill-opacity=".22"/>
  <rect class="s" y="4" width="400" height="4" rx="2" fill="url(#g)"/>
</svg>
""")


# ---------------------------------------------------------------- terminal
def terminal():
    cmd = "n3xt deploy --guild community"
    s = 15
    cl = mlen(cmd, s)
    cx = 46
    w("terminal.svg", f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 360" width="880" height="360" role="img" aria-label="N3XT.sys boot sequence">
  <defs><style>
      .m{{font-family:{MONO};font-size:15px}}
      @keyframes in{{from{{opacity:0;transform:translateX(-8px)}}to{{opacity:1;transform:translateX(0)}}}}
      @keyframes blink{{0%,49%{{opacity:1}}50%,100%{{opacity:0}}}}
      @keyframes type{{from{{transform:translateX(0)}}to{{transform:translateX({cl}px)}}}}
      @keyframes hide{{to{{opacity:0}}}}
      @keyframes fill{{from{{transform:scaleX(0)}}to{{transform:scaleX(1)}}}}
      @keyframes glow{{0%,100%{{opacity:.35}}50%{{opacity:1}}}}
      .l{{opacity:0;animation:in .35s ease-out forwards}}
      .d1{{animation-delay:2.3s}}.d2{{animation-delay:2.9s}}.d3{{animation-delay:3.5s}}.d4{{animation-delay:4.1s}}
      .d5{{animation-delay:4.7s}}.d6{{animation-delay:5.9s}}.d7{{animation-delay:6.5s}}.d8{{animation-delay:7.2s}}
      .cur{{animation:blink 1s step-end infinite}}
      .typer{{animation:type 1.5s steps({len(cmd)}) .4s forwards}}
      .tcur{{animation:blink 1s step-end infinite, hide 0s linear 2.1s forwards}}
      .bar{{transform-box:fill-box;transform-origin:left center;transform:scaleX(0);animation:fill 1.1s ease-in-out 4.8s forwards}}
      .live{{animation:glow 1.8s ease-in-out 7.2s infinite}}
  </style></defs>
  <rect width="880" height="360" rx="14" fill="#0d1117"/>
  <rect x=".75" y=".75" width="878.5" height="358.5" rx="13.5" fill="none" stroke="#30363d" stroke-width="1.5"/>
  <path d="M14 .75H866A13.25 13.25 0 0 1 879.25 14V40H.75V14A13.25 13.25 0 0 1 14 .75Z" fill="#161b22"/>
  <circle cx="24" cy="21" r="6" fill="#ff5f57"/><circle cx="44" cy="21" r="6" fill="#febc2e"/><circle cx="64" cy="21" r="6" fill="#28c840"/>
  <text x="440" y="26" text-anchor="middle" class="m" font-size="13" fill="#8b949e">n3xt — operator console</text>
  <g class="m">
    <text x="28" y="78" fill="{G}">❯</text>
    <text x="{cx}" y="78" fill="#e6edf3" textLength="{cl}" lengthAdjust="spacingAndGlyphs">{cmd}</text>
    <g class="typer"><rect x="{cx}" y="60" width="{cl+20}" height="26" fill="#0d1117"/><rect class="tcur" x="{cx+1}" y="64" width="8" height="18" fill="#e6edf3"/></g>
    <text class="l d1" x="28" y="112" fill="#8b949e">▸ loading config <tspan fill="#484f58">··················</tspan> <tspan fill="{T}">ok</tspan></text>
    <text class="l d2" x="28" y="140" fill="#8b949e">▸ guild lock <tspan fill="#484f58">······················</tspan> <tspan fill="{T}">verified</tspan></text>
    <g class="l d3">
      <text x="28" y="168" fill="#8b949e">▸ modules</text>
      <text x="58" y="192" fill="{M}">tickets · moderation · recruitment · engagement · tempvoice</text>
      <text x="58" y="214" fill="{M}">surveys · anti-raid · appeals · audit-logs · panels</text>
    </g>
    <text class="l d4" x="28" y="246" fill="#8b949e">▸ restoring scheduled jobs <tspan fill="#484f58">········</tspan> <tspan fill="{T}">state recovered</tspan></text>
    <g class="l d5">
      <text x="28" y="274" fill="#8b949e">▸ tsc · eslint · vitest</text>
      <rect x="280" y="262" width="236" height="14" rx="3" fill="#161b22" stroke="#30363d"/>
      <rect class="bar" x="280" y="262" width="236" height="14" rx="3" fill="{G}"/>
    </g>
    <text class="l d6" x="530" y="274" fill="{T}">passed</text>
    <text class="l d7" x="28" y="312" fill="#e6edf3"><tspan fill="{T}" font-weight="700">✓</tspan> N3XT.sys online <tspan fill="#484f58">—</tspan> one bot, one dataset, one instance</text>
    <g class="l d8">
      <circle class="live" cx="836" cy="307" r="6" fill="{T}"/>
      <text x="28" y="340" fill="{G}">❯ <tspan class="cur" fill="#e6edf3">▍</tspan></text>
    </g>
  </g>
</svg>
""")


# ---------------------------------------------------------------- footer
def footer():
    W, H = 1200, 120
    w("footer.svg", f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" preserveAspectRatio="none" role="img" aria-label="N3XT Agency">
  <defs><linearGradient id="f" x1="0" x2="1"><stop offset="0" stop-color="{BG}"/><stop offset=".5" stop-color="{G}"/><stop offset="1" stop-color="{T}"/></linearGradient>
  <style>
    @keyframes wv{{from{{transform:translateX(0)}}to{{transform:translateX(-600px)}}}}
    .a{{animation:wv 9s linear infinite}} .b{{animation:wv 14s linear infinite}}
  </style></defs>
  <path class="b" opacity=".35" fill="url(#f)" d="M0 70 Q150 30 300 70 T600 70 T900 70 T1200 70 T1500 70 T1800 70 V120 H0Z"/>
  <path class="a" fill="url(#f)" d="M0 85 Q150 55 300 85 T600 85 T900 85 T1200 85 T1500 85 T1800 85 V120 H0Z"/>
</svg>
""")


header(); typing(); divider(); terminal(); footer()
button("btn-website.svg", GLOBE, "WEBSITE", "n3xt-agency.com", True)
button("btn-contact.svg", MAIL, "CONTACT", "leon.holetz@n3xt-agency.com", False)
for i, n in enumerate(["Overview", "Work", "Stack", "How I build", "Contact"], 1):
    nav(f"nav-{n.lower().replace(' ', '-')}.svg", i, n)
section("h-overview.svg", 1, "Overview", "// whoami --long", "signal")
section("h-work.svg", 2, "Work", "// projects/n3xt.sys", "nodes")
section("h-stack.svg", 3, "Stack", "// package.json", "stack")
section("h-how-i-build.svg", 4, "How I build", "// principles.md", "gear")
section("h-contact.svg", 5, "Contact", "// open for work", "bars")
print("ok")
