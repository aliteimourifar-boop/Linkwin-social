"""LinkWin daily post, 11 Nov 2026.

CREATIVE BRIEF
Concept name: "Two Tides".
Idea: China's October trade as two tides in one circle: an outbound jade arc (exports) and an inbound copper arc
  (imports) chasing each other round a fine dial, with the two growth figures set inside like an emblem on a
  magazine cover. Feeling: calm expertise, a two-way market, imports suddenly the faster tide.
Background tone: light-mid celadon (not the cobalt mid tone of 10 Nov; cool green, not the warm paper of 9 Nov).
Palette: celadon #DDE7E0, deep jade #1D4A3D, copper #B4612C, porcelain band #F6F4EF (+ ink #16201C for text).
Composition: editorial magazine cover: masthead kicker row, large serif headline, centred circular emblem
  (dial rings + two arrowed arcs) with the two numbers inside, short deck below, porcelain footer band with signature.
  Not an oversized-numeral poster (10 Nov), not a periodic tile (9 Nov), no stat grid.
Type: Cormorant Garamond 700 headline + figures (luxury editorial serif, new this week) + Manrope for text (EN/RU);
  Noto Naskh Arabic 700 headline/figures + IBM Plex Sans Arabic text (FA/AR). Headline face differs from 10 Nov (Oswald/Plex).
Imagery: none (photos/ library still empty; photo sites blocked). Pure SVG geometry, no stock illustration.
Logo: A, printed seal on a porcelain footer band: full-colour original multiplied onto the band (no box),
  bottom-left LTR / bottom-right RTL. (A faint watermark was tried and dropped: it fought the headline.)
  (10 Nov: B tab top-left; 9 Nov: A printed seal bottom-right.)
RTL plan: dir=rtl mirrors masthead, footer and watermark; the emblem is flipped so the tides run right-to-left;
  figures kept as isolated LTR runs (Arabic) or Persian digits with ٫ and ٪ (Persian).
"""
import os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLUG = "2026-11-11-china-oct-trade"
NN = " "  # narrow no-break space

T = {
"en": dict(dir="ltr", kick="China customs data", date="October 2026",
  h="China’s imports outran its exports in October.",
  xl="Exports", xv="$412.3bn", xn="+35.2%",
  ml="Imports", mv="$307.1bn", mn="+41.6%",
  p="Imports beat the +32% forecast. Year on year, in US dollars.",
  p2="Surplus: $105.3bn, smaller than markets expected.",
  hook="LinkWin · your sourcing and trade partner in China",
  src="Source: China GAC data via Reuters &amp; Trading Economics, 10 Nov 2026"),
"fa": dict(dir="rtl", kick="داده‌های گمرک چین", date="اکتبر ۲۰۲۶",
  h="رشد واردات چین در اکتبر از صادراتش پیشی گرفت",
  xl="صادرات", xv="۴۱۲٫۳ میلیارد دلار", xn="۳۵٫۲٪+",
  ml="واردات", mv="۳۰۷٫۱ میلیارد دلار", mn="۴۱٫۶٪+",
  p="پیش‌بینی بازار برای رشد واردات ۳۲٪ بود. ارقام سالانه و دلاری است.",
  p2="مازاد تجاری: ۱۰۵٫۳ میلیارد دلار، کمتر از انتظار بازار.",
  hook="LinkWin، شریک شما در تأمین کالا و تجارت با چین",
  src="منبع: گمرک چین به نقل از رویترز و <bdi>Trading Economics</bdi>، ۱۹ آبان ۱۴۰۵"),
"ru": dict(dir="ltr", kick="Таможня КНР", date="октябрь 2026",
  h="Импорт Китая в октябре рос быстрее экспорта.",
  xl="Экспорт", xv=f"412,3{NN}млрд $", xn=f"+35,2{NN}%",
  ml="Импорт", mv=f"307,1{NN}млрд $", mn=f"+41,6{NN}%",
  p=f"Прогноз по импорту был +32{NN}%. Год к году, в долларах США.",
  p2=f"Профицит — 105,3{NN}млрд $, меньше ожиданий рынка.",
  hook="LinkWin — ваш партнёр по закупкам и торговле с Китаем",
  src="Источник: ГТУ КНР, данные Reuters и Trading Economics, 10.11.2026"),
"ar": dict(dir="rtl", kick="بيانات الجمارك الصينية", date="أكتوبر 2026",
  h="واردات الصين نمت أسرع من صادراتها في أكتوبر",
  xl="الصادرات", xv="412.3 مليار دولار", xn="+35.2%",
  ml="الواردات", mv="307.1 مليار دولار", mn="+41.6%",
  p="توقعات السوق لنمو الواردات كانت 32%، والأرقام سنوية وبالدولار الأمريكي.",
  p2="الفائض التجاري 105.3 مليار دولار، أقل مما توقعته الأسواق.",
  hook="LinkWin شريككم في التوريد والتجارة مع الصين",
  src="المصدر: الجمارك الصينية عبر رويترز و<bdi>Trading Economics</bdi>، ‏10 نوفمبر 2026"),
}

CSS = r"""
:root{--cel:#DDE7E0;--jade:#1D4A3D;--cop:#B4612C;--por:#F6F4EF;--ink:#16201C}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;overflow:hidden}
html.story,html.story body{height:1920px}
body{background:var(--cel);color:var(--ink);font-family:'Manrope',sans-serif;position:relative;
  background-image:radial-gradient(1200px 800px at 50% 42%,#E8EFEA 0%,rgba(232,239,234,0) 70%)}
.rtl body{font-family:'IBM Plex Sans Arabic','Manrope',sans-serif}
.wm{position:absolute;width:var(--wmw);top:var(--wmt);inset-inline-end:var(--wme);
  mix-blend-mode:multiply;opacity:.07;filter:brightness(1.015)}
.stage{position:absolute;left:72px;right:72px;top:var(--top)}
.kick{display:flex;justify-content:space-between;align-items:center;font-weight:600;font-size:22px;
  letter-spacing:.2em;text-transform:uppercase;color:var(--jade);padding-bottom:22px;border-bottom:1.5px solid rgba(29,74,61,.35)}
.kick span{font-weight:400;opacity:.8}
.rtl .kick{letter-spacing:0;font-size:26px}
h1{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:var(--h);line-height:var(--hl);
  margin-top:var(--hm);color:var(--ink);letter-spacing:-.01em;max-width:var(--hw)}
.rtl h1{font-family:'Noto Naskh Arabic','Cormorant Garamond',serif;letter-spacing:0}
.emb{position:relative;width:var(--ew);height:var(--ew);margin:var(--em) auto 0}
.emb svg{position:absolute;inset:0;width:100%;height:100%}
.rtl .emb svg{transform:scaleX(-1)}
.in{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.blk{display:flex;flex-direction:column;align-items:center}
.lab{font-size:var(--lf);font-weight:600;letter-spacing:.18em;text-transform:uppercase}
.rtl .lab{letter-spacing:0;font-weight:600}
.lab i{font-style:normal;font-weight:400;opacity:.75;letter-spacing:.04em;text-transform:none}
.rtl .lab i{letter-spacing:0}
.num{font-family:'Cormorant Garamond',serif;font-weight:700;font-size:var(--nf);line-height:1;letter-spacing:-.01em}
.rtl .num{font-family:'Noto Naskh Arabic','Cormorant Garamond',serif;line-height:1.25;letter-spacing:0}
.x{color:var(--jade)} .m{color:var(--cop)}
.x .num{margin-top:6px} .m .num{margin-bottom:6px}
.mid{width:46%;height:1.5px;background:linear-gradient(90deg,transparent,rgba(22,32,28,.35),transparent);margin:var(--mg) 0}
.deck{margin-top:var(--dm);font-size:var(--pf);line-height:var(--pl);max-width:var(--pw);color:#26332E}
.deck b{display:block;font-weight:600;color:var(--jade)}
.foot{position:absolute;left:0;right:0;bottom:0;height:var(--fh);background:var(--por);
  border-top:1.5px solid rgba(29,74,61,.25);padding:var(--fp) 72px 0;display:flex;gap:36px;align-items:flex-start}
.sig{height:var(--lg);mix-blend-mode:multiply;filter:brightness(1.015);flex:none}
.ft{display:flex;flex-direction:column;gap:8px;padding-top:6px;font-size:21px;line-height:1.4;color:#3A4842}
.ft b{font-size:23px;color:var(--ink);font-weight:600}
.ft .u{font-weight:600;color:var(--jade);letter-spacing:.06em;margin-top:4px}
.rtl .ft{font-size:21px;line-height:1.6;gap:4px}
.rtl .ft .u{letter-spacing:.06em;font-family:'Manrope',sans-serif;text-align:right}
"""

def emblem():
    # 600x600 viewbox; centre 300,300; arcs on r=262 with small gaps; dial rings
    import math
    def pt(a, r=262):
        t = math.radians(a)
        return 300 + r * math.cos(t), 300 + r * math.sin(t)
    # SVG angles: 0 = right, 90 = down. Upper arc (exports) runs from 188 deg (left) to 352 deg (right) clockwise over top.
    x1, y1 = pt(188); x2, y2 = pt(350)
    x3, y3 = pt(8); x4, y4 = pt(170)
    ticks = []
    for i in range(72):
        a = i * 5
        r1, r2 = (226, 238) if i % 6 else (220, 240)
        p1, p2 = pt(a, r1), pt(a, r2)
        ticks.append(f'<line x1="{p1[0]:.1f}" y1="{p1[1]:.1f}" x2="{p2[0]:.1f}" y2="{p2[1]:.1f}"/>')
    return f"""<svg viewBox="0 0 600 600" xmlns="http://www.w3.org/2000/svg">
<defs>
 <marker id="aj" viewBox="0 0 12 12" refX="6" refY="6" markerWidth="4.2" markerHeight="4.2" orient="auto-start-reverse">
  <path d="M1,1 L11,6 L1,11 L4,6 Z" fill="#1D4A3D"/></marker>
 <marker id="ac" viewBox="0 0 12 12" refX="6" refY="6" markerWidth="4.2" markerHeight="4.2" orient="auto-start-reverse">
  <path d="M1,1 L11,6 L1,11 L4,6 Z" fill="#B4612C"/></marker>
</defs>
<circle cx="300" cy="300" r="292" fill="none" stroke="#1D4A3D" stroke-opacity=".22" stroke-width="1.2"/>
<circle cx="300" cy="300" r="214" fill="#F3F6F2" fill-opacity=".55" stroke="#1D4A3D" stroke-opacity=".18" stroke-width="1"/>
<g stroke="#1D4A3D" stroke-opacity=".35" stroke-width="1.4">{''.join(ticks)}</g>
<path d="M{x1:.1f},{y1:.1f} A262,262 0 0 1 {x2:.1f},{y2:.1f}" fill="none" stroke="#1D4A3D" stroke-width="9" stroke-linecap="round" marker-end="url(#aj)"/>
<path d="M{x3:.1f},{y3:.1f} A262,262 0 0 1 {x4:.1f},{y4:.1f}" fill="none" stroke="#B4612C" stroke-width="9" stroke-linecap="round" marker-end="url(#ac)"/>
</svg>"""

V = {
 "en": dict(top="64px", h="96px", hl="1.0", hm="44px", hw="900px", ew="600px", em="34px", lf="20px", nf="128px", mg="18px",
            dm="30px", pf="27px", pl="1.45", pw="760px", fh="190px", fp="40px", lg="104px", wmw="380px", wmt="250px", wme="36px"),
 "ru": dict(top="64px", h="88px", hl="1.02", hm="44px", hw="920px", ew="600px", em="34px", lf="20px", nf="120px", mg="18px",
            dm="30px", pf="26px", pl="1.45", pw="800px", fh="190px", fp="40px", lg="104px", wmw="380px", wmt="250px", wme="36px"),
 "fa": dict(top="64px", h="74px", hl="1.5", hm="36px", hw="936px", ew="600px", em="22px", lf="25px", nf="104px", mg="8px",
            dm="22px", pf="27px", pl="1.75", pw="900px", fh="190px", fp="40px", lg="104px", wmw="380px", wmt="250px", wme="36px"),
 "ar": dict(top="64px", h="72px", hl="1.5", hm="36px", hw="936px", ew="600px", em="22px", lf="25px", nf="104px", mg="8px",
            dm="22px", pf="26px", pl="1.75", pw="900px", fh="190px", fp="40px", lg="104px", wmw="380px", wmt="250px", wme="36px"),
}
# Story overrides (safe zones: nothing above 200px or below 1670px)
VS = {
 "en": dict(top="214px", h="104px", hm="44px", ew="620px", em="40px", nf="138px", lf="22px", mg="10px", pf="30px", dm="40px", pw="960px",
            fh="450px", fp="44px", lg="118px"),
 "ru": dict(top="214px", h="96px", hm="44px", ew="620px", em="40px", nf="130px", lf="22px", mg="10px", pf="29px", dm="40px", pw="960px",
            fh="450px", fp="44px", lg="118px"),
 "fa": dict(top="214px", h="84px", hm="40px", ew="640px", em="44px", nf="112px", lf="27px", mg="10px", pf="30px", dm="44px",
            fh="450px", fp="44px", lg="118px"),
 "ar": dict(top="214px", h="82px", hm="40px", ew="640px", em="44px", nf="112px", lf="27px", mg="10px", pf="29px", dm="44px",
            fh="450px", fp="44px", lg="118px"),
}

def page(lang, c):
    cls = "rtl" if c["dir"] == "rtl" else "ltr"
    style = ";".join(f"--{k}:{v}" for k, v in V[lang].items())
    story = "html.story{" + ";".join(f"--{k}:{v}" for k, v in VS[lang].items()) + "}"
    iso = (lambda s: f'<bdi dir="ltr">{s}</bdi>') if lang == "ar" else (lambda s: s)
    return f"""<!doctype html><html lang="{lang}" dir="{c['dir']}" class="{cls}"><head><meta charset="utf-8">
<link rel="stylesheet" href="../brand/fonts.css"><style>{CSS}html{{{style}}}{story}</style></head><body>
<div class="stage">
 <div class="kick">{c['kick']}<span>{c['date']}</span></div>
 <h1>{c['h']}</h1>
 <div class="emb">{emblem()}
  <div class="in">
   <div class="blk x"><div class="lab">{c['xl']} <i>· {c['xv']}</i></div><div class="num">{iso(c['xn'])}</div></div>
   <div class="mid"></div>
   <div class="blk m"><div class="num">{iso(c['mn'])}</div><div class="lab">{c['ml']} <i>· {c['mv']}</i></div></div>
  </div>
 </div>
 <div class="deck">{c['p']}<b>{c['p2']}</b></div>
</div>
<div class="foot"><img class="sig" src="../brand/linkwin-logo-original-cropped.png">
 <div class="ft"><b>{c['hook']}</b><span>{c['src']}</span><span class="u">linkwinco.com</span></div></div>
</body></html>"""


if __name__ == "__main__":
    langs = sys.argv[1:] or list(T)
    for lang in langs:
        c = T[lang]
        tpl = f"{ROOT}/templates/{SLUG}-{lang}.html"
        open(tpl, "w").write(page(lang, c))
        for mode, suffix in (("feed", ""), ("story", "-story")):
            subprocess.run([sys.executable, f"{ROOT}/render.py", tpl, f"{ROOT}/posts/{SLUG}-{lang}{suffix}.jpg", mode], check=True)
