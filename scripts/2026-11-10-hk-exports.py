"""LinkWin daily post, 10 Nov 2026.

CREATIVE BRIEF
Concept name: "Harbour Chart".
Idea: Hong Kong drawn as a nautical chart at dusk: a cobalt sea-chart field with a faint lat/long grid,
  a fine white line drawing of the harbour skyline, cranes and a laden container ship, and one huge number.
  Feeling: confident momentum, a port city in full swing.
Background tone: mid (cobalt blue; not the light paper of 9 Nov, not the dark ink of 6-8 Nov).
Palette: cobalt #2A5C93, harbour deep #1A426F, mist #D6E5F4, paper tab #F3EFE6 (logo red carried by the logo itself).
Composition: oversized numeral poster over a line-art panorama; text block top, skyline + water across the lower third,
  footer set on the water.
Type: Oswald 600 for the numeral (condensed, industrial, port signage) + IBM Plex Sans for headline and text
  (EN/RU); Noto Kufi Arabic 900 numeral/headline + IBM Plex Sans Arabic text (FA/AR). Headline face differs from 9 Nov (Playfair).
Imagery: none (photo library empty; photo sites blocked). Hand-built SVG line illustration, generic skyline, no real-building replicas.
Logo: B, seal tab: paper tab hanging from the top edge (feed) / from a hairline (Story), logo multiplied onto the tab.
  Top-left LTR, top-right RTL. (9 Nov was A, printed seal, bottom-right.)
RTL plan: whole composition mirrors: tab right, text right-aligned, panorama flipped so the ship sails right-to-left,
  coordinates label moves left.
"""
import os, subprocess, sys, random
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLUG = "2026-11-10-hk-exports"
NNB = " "

T = {
"en": dict(dir="ltr", kick="Hong Kong trade", date="September 2026",
  num="+64.9%", cap="Hong Kong’s merchandise exports, year on year",
  h="The fastest export growth in over 40 years.",
  p="AI-related electronics led the surge, the 20th straight month of <span style=\"white-space:nowrap\">double-digit</span> growth.",
  nxt="Coming up: Hong Kong Maritime Week, 15–21 November.",
  hook="LinkWin · your trading partner in Hong Kong &amp; Guangzhou",
  src="Source: HKSAR Census and Statistics Department, 28 Oct 2026"),
"fa": dict(dir="rtl", kick="تجارت هنگ‌کنگ", date="آبان ۱۴۰۵",
  num="۶۴٫۹٪", cap="رشد صادرات کالای هنگ‌کنگ در سپتامبر، نسبت به سال قبل",
  h="سریع‌ترین رشد صادرات در بیش از چهار دهه",
  p="کالاهای الکترونیکی مرتبط با هوش مصنوعی موتور این جهش بودند؛ بیستمین ماه پیاپی با رشد دورقمی.",
  nxt="پیش رو: هفته دریانوردی هنگ‌کنگ، ۲۴ تا ۳۰ آبان",
  hook="LinkWin، شریک تجاری شما در هنگ‌کنگ و گوانگجو",
  src="منبع: اداره آمار و سرشماری هنگ‌کنگ، ۶ آبان ۱۴۰۵"),
"ru": dict(dir="ltr", kick="Торговля Гонконга", date="сентябрь 2026",
  num=f"+64,9{NNB}%", cap="рост товарного экспорта Гонконга, год к году",
  h="Самый быстрый рост экспорта за 40 с лишним лет.",
  p="Рывок обеспечила электроника для ИИ. Уже 20-й месяц подряд экспорт растёт двузначными темпами.",
  nxt="Впереди: Гонконгская морская неделя, 15–21 ноября.",
  hook="LinkWin — ваш торговый партнёр в Гонконге и Гуанчжоу",
  src="Источник: C&amp;SD, статистическая служба Гонконга, 28.10.2026"),
"ar": dict(dir="rtl", kick="تجارة هونغ كونغ", date="سبتمبر 2026",
  num="+64.9%", cap="نمو الصادرات السلعية لهونغ كونغ على أساس سنوي",
  h="أسرع نمو للصادرات منذ أكثر من 40 عامًا",
  p="قادت الإلكترونيات المرتبطة بالذكاء الاصطناعي هذه القفزة، وهو الشهر العشرون على التوالي بنمو من خانتين.",
  nxt="قريبًا: أسبوع هونغ كونغ البحري، من 15 إلى 21 نوفمبر",
  hook="LinkWin شريككم التجاري في هونغ كونغ وقوانغتشو",
  src="المصدر: دائرة الإحصاء والتعداد في هونغ كونغ، 28 أكتوبر 2026"),
}


def panorama():
    """Generic harbour panorama, 1080 x 380, line art. Ridge, towers, cranes, ship, water."""
    W, H, base = 1080, 380, 220  # base = waterline
    s = []
    # mountain ridge
    s.append(f'<path d="M0 130 C 90 106, 160 66, 250 76 S 400 42, 470 56 S 610 106, 700 94 S 860 58, 940 84 S 1040 114, 1080 106" '
             f'fill="none" stroke="#D6E5F4" stroke-opacity=".38" stroke-width="2"/>')
    s.append(f'<path d="M0 160 C 120 140, 220 116, 330 124 S 520 108, 640 132 S 860 124, 1080 150" '
             f'fill="none" stroke="#D6E5F4" stroke-opacity=".22" stroke-width="1.5"/>')
    rnd = random.Random(11)
    x = 18
    towers = []
    while x < 760:
        w = rnd.choice([34, 40, 46, 52, 58])
        h = rnd.choice([56, 70, 84, 96, 110, 124])
        if 300 < x < 360: h = 178  # landmark-height tower, generic stepped crown
        if 520 < x < 570: h = 150
        towers.append((x, w, h))
        x += w + rnd.choice([4, 6, 8])
    for (x, w, h) in towers:
        top = base - h
        op = ".9" if h > 120 else ".62"
        d = f"M{x} {base} V{top} H{x+w} V{base}"
        if h > 160:  # stepped crown
            d = (f"M{x} {base} V{top+30} H{x+6} V{top+14} H{x+12} V{top} H{x+w-12} V{top+14} H{x+w-6} V{top+30} H{x+w} V{base}"
                 f" M{x+w/2} {top} V{top-26}")
        s.append(f'<path d="{d}" fill="#1E4B7E" fill-opacity=".55" stroke="#F4F8FC" stroke-opacity="{op}" stroke-width="1.6"/>')
        # window lines
        for k in range(1, max(1, w // 12)):
            xx = x + k * 12
            s.append(f'<line x1="{xx}" y1="{top+10 if h<=160 else top+36}" x2="{xx}" y2="{base-6}" stroke="#D6E5F4" stroke-opacity=".16" stroke-width="1"/>')
    # quay
    s.append(f'<line x1="770" y1="{base}" x2="1080" y2="{base}" stroke="#F4F8FC" stroke-opacity=".7" stroke-width="2"/>')
    # ship-to-shore cranes
    for cx in (820, 950):
        c = (f"M{cx} {base} V{base-124} M{cx+46} {base} V{base-124} M{cx} {base-50} L{cx+46} {base-92} M{cx+46} {base-50} L{cx} {base-92}"
             f" M{cx-70} {base-124} H{cx+130} M{cx+46} {base-124} L{cx+23} {base-162} L{cx} {base-124} M{cx+23} {base-162} L{cx+130} {base-124}"
             f" M{cx-40} {base-124} V{base-96}")
        s.append(f'<path d="{c}" fill="none" stroke="#F4F8FC" stroke-opacity=".78" stroke-width="2" stroke-linejoin="round"/>')
    # container ship, sailing
    sx, sy = 300, base + 74
    hull = f"M{sx} {sy} L{sx+560} {sy} L{sx+600} {sy-42} L{sx-26} {sy-42} Z"
    s.append(f'<path d="{hull}" fill="#173B63" stroke="#F4F8FC" stroke-width="2.2" stroke-linejoin="round"/>')
    # bridge
    bx = sx + 470
    s.append(f'<path d="M{bx} {sy-42} V{sy-118} H{bx+52} V{sy-42} M{bx-6} {sy-118} H{bx+58} M{bx+30} {sy-118} V{sy-140}" fill="#173B63" stroke="#F4F8FC" stroke-width="2"/>')
    # container stacks
    cx = sx + 6
    rnd2 = random.Random(5)
    while cx < bx - 40:
        rows = rnd2.choice([2, 3, 3, 4])
        for r in range(rows):
            y = sy - 42 - (r + 1) * 20
            s.append(f'<rect x="{cx}" y="{y}" width="38" height="20" fill="none" stroke="#F4F8FC" stroke-opacity=".86" stroke-width="1.5"/>')
        cx += 40
    # water lines
    for i, y in enumerate(range(base + 12, H, 16)):
        op = max(0.06, 0.34 - i * 0.03)
        dash = f"{60+i*14} {22+i*6}"
        off = (i * 37) % 90
        s.append(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="#D6E5F4" stroke-opacity="{op:.2f}" stroke-width="1.5" stroke-dasharray="{dash}" stroke-dashoffset="{off}"/>')
    return f'<svg class="pano" viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg">{"".join(s)}</svg>'


CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px;overflow:hidden}
html.story,html.story body{height:1920px}
body{color:#F4F8FC;font-family:var(--body);position:relative;
  background:linear-gradient(180deg,#2E629A 0%,#2A5C93 45%,#1F4C7F 72%,#1A426F 100%)}
/* chart grid */
.grid{position:absolute;inset:0;pointer-events:none;
  background-image:linear-gradient(rgba(214,229,244,.075) 1px,transparent 1px),linear-gradient(90deg,rgba(214,229,244,.075) 1px,transparent 1px);
  background-size:108px 108px;background-position:-1px -1px}
.glow{position:absolute;inset:0;background:radial-gradient(760px 560px at 70% 24%,rgba(255,255,255,.10),rgba(255,255,255,0) 70%)}
html[dir=rtl] .glow{background:radial-gradient(760px 560px at 30% 24%,rgba(255,255,255,.10),rgba(255,255,255,0) 70%)}
.coord{position:absolute;top:44px;right:64px;font-family:'IBM Plex Sans',sans-serif;font-size:20px;letter-spacing:.12em;color:rgba(214,229,244,.62);direction:ltr}
html[dir=rtl] .coord{right:auto;left:64px}
html.story .coord{top:212px}
/* seal tab */
.tab{position:absolute;top:0;left:64px;width:214px;height:206px;background:#F3EFE6;border-radius:0 0 14px 14px;
  display:flex;align-items:flex-end;justify-content:center;padding-bottom:22px;
  box-shadow:0 22px 40px -18px rgba(8,24,46,.65),0 2px 0 rgba(255,255,255,.4) inset}
.tab:before{content:"";position:absolute;left:0;right:0;top:0;height:30px;background:linear-gradient(180deg,rgba(26,66,111,.16),rgba(26,66,111,0))}
.tab img{height:132px;width:auto;mix-blend-mode:multiply;filter:brightness(1.015)}
html[dir=rtl] .tab{left:auto;right:64px}
html.story .tab{top:226px;border-radius:14px;height:196px;padding-bottom:30px}
html.story .tab:before{display:none}
html.story .tab:after{content:"";position:absolute;left:50%;top:-226px;height:226px;width:1.5px;background:rgba(244,248,252,.55)}
html.story .tab i{position:absolute;top:12px;left:50%;width:12px;height:12px;margin-left:-6px;border-radius:50%;background:#1F4C7F;box-shadow:inset 0 1px 2px rgba(0,0,0,.35)}
.stage{position:absolute;left:64px;right:64px;top:240px}
html.story .stage{top:444px}
.kick{display:flex;gap:18px;align-items:center;font-size:22px;font-weight:600;color:#D6E5F4}
.kick span{font-weight:400;opacity:.8}
.kick:before{content:"";width:46px;height:2px;background:#D6E5F4;opacity:.7}
.ltr .kick{letter-spacing:.16em;text-transform:uppercase;font-size:20px}
.num{font-family:var(--num);font-weight:var(--numw);font-size:var(--nf);line-height:var(--nl);margin-top:18px;letter-spacing:-.01em;color:#FFFFFF;
  text-shadow:0 18px 40px rgba(8,24,46,.28);white-space:nowrap}
html.story .num{font-size:var(--ns);margin-top:30px}
.cap{font-size:25px;color:#D6E5F4;margin-top:var(--capm);}
html.story .cap{font-size:29px}
.rule{width:100%;height:1.5px;background:rgba(214,229,244,.35);margin:22px 0 22px}
html.story .rule{margin:34px 0 32px}
h1{text-wrap:balance;font-family:var(--head);font-weight:var(--hw);font-size:var(--h);line-height:var(--lh);max-width:900px}
html.story h1{font-size:var(--hs)}
.p{text-wrap:pretty;font-size:var(--pf);line-height:var(--pl);color:#E7EFF8;margin-top:16px;max-width:860px}
html.story .p{font-size:calc(var(--pf) * 1.16);margin-top:24px}
.nxt{display:none}
html.story .nxt{display:flex;align-items:center;gap:16px;margin-top:34px;font-size:30px;font-weight:600;color:#FFFFFF;
  border:1.5px solid rgba(214,229,244,.55);border-radius:999px;padding:16px 30px;width:max-content;max-width:100%}
.nxt b{width:12px;height:12px;border-radius:50%;background:#F3EFE6;flex:none}
.pano{position:absolute;left:0;bottom:62px}
html.story .pano{bottom:250px}
html.story .foot:before{content:"";position:absolute;left:-64px;right:-64px;top:-26px;bottom:-30px;background:linear-gradient(180deg,rgba(26,66,111,0),rgba(26,66,111,.85) 40%);z-index:-1}
html[dir=rtl] .pano{transform:scaleX(-1)}
.foot{position:absolute;left:64px;right:64px;bottom:34px;display:flex;justify-content:space-between;align-items:flex-end;gap:30px;font-size:20px;line-height:1.45;color:rgba(231,239,248,.86)}
.foot b{display:block;color:#FFFFFF;font-weight:600;font-size:21px}
.foot .url{font-weight:600;color:#FFFFFF;font-size:24px;letter-spacing:.04em;font-family:'IBM Plex Sans',sans-serif;white-space:nowrap}
html.story .foot{bottom:262px;font-size:23px;z-index:1}
html.story .foot b{font-size:25px}
html.story .foot .url{font-size:27px}
.ltr{--num:'Oswald',sans-serif;--numw:600;--head:'IBM Plex Sans',sans-serif;--hw:600;--body:'IBM Plex Sans',sans-serif}
.rtl{--num:'Noto Kufi Arabic','Oswald',sans-serif;--numw:900;--head:'Noto Kufi Arabic','IBM Plex Sans',sans-serif;--hw:700;--body:'IBM Plex Sans Arabic','IBM Plex Sans',sans-serif}
.ltr .num{text-transform:none}
"""


def page(lang, c):
    cls = "rtl" if c["dir"] == "rtl" else "ltr"
    v = {
        "en": dict(nl="1", nf="250px", ns="290px", capm="4px", h="58px", hs="66px", lh="1.12", pf="27px", pl="1.45"),
        "ru": dict(nl="1", nf="236px", ns="276px", capm="26px", h="52px", hs="60px", lh="1.14", pf="26px", pl="1.45"),
        "fa": dict(nl="1.15", nf="190px", ns="220px", capm="0px", h="50px", hs="58px", lh="1.6", pf="27px", pl="1.75"),
        "ar": dict(nl="1.15", nf="190px", ns="220px", capm="0px", h="48px", hs="56px", lh="1.6", pf="26px", pl="1.75"),
    }[lang]
    style = ";".join(f"--{k}:{val}" for k, val in v.items())
    num = f'<bdi dir="ltr">{c["num"]}</bdi>'
    return f"""<!doctype html><html lang="{lang}" dir="{c['dir']}" class="{cls}" style="{style}"><head><meta charset="utf-8">
<link rel="stylesheet" href="../brand/fonts.css"><style>{CSS}</style></head><body>
<div class="grid"></div><div class="glow"></div>
<div class="coord">22°17′N · 114°10′E</div>
<div class="tab"><i></i><img src="../brand/linkwin-logo-original-cropped.png"></div>
<div class="stage">
<div class="kick">{c['kick']}<span>{c['date']}</span></div>
<div class="num">{num}</div>
<div class="cap">{c['cap']}</div>
<div class="rule"></div>
<h1>{c['h']}</h1>
<div class="p">{c['p']}</div>
<div class="nxt"><b></b>{c['nxt']}</div>
</div>
{panorama()}
<div class="foot"><div><b>{c['hook']}</b>{c['src']}</div><div class="url">linkwinco.com</div></div>
</body></html>"""


if __name__ == "__main__":
    langs = sys.argv[1:] or list(T)
    for lang in langs:
        c = T[lang]
        tpl = f"{ROOT}/templates/{SLUG}-{lang}.html"
        open(tpl, "w").write(page(lang, c))
        for mode, suffix in (("feed", ""), ("story", "-story")):
            subprocess.run([sys.executable, f"{ROOT}/render.py", tpl, f"{ROOT}/posts/{SLUG}-{lang}{suffix}.jpg", mode], check=True)
