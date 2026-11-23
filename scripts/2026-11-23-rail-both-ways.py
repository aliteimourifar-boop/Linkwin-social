"""LinkWin daily carousel, 23 Nov 2026 — China–Europe freight trains now run full in both directions.

CREATIVE BRIEF
Concept name: "Two-Way Board" (a CR Express container train photo bleeds into a warm graphite page; under the headline a
  station-style split-flap board shows the two directions side by side: outbound 9,301 vs return 9,360 trains).
Idea: rail as a real middle option between sea and air; the news is that return trains now outnumber outbound ones.
Background tone: dark (warm graphite) after light sand (22 Nov), gunmetal mid (21 Nov), mist light (20 Nov).
Palette: graphite #17191C, panel #202327, chalk #F1EFEA, ice blue #8DB8FF (outbound), signal mint #5ED3A4 (return),
  warm grey #9A9893; seal tone-on-tone chalk.
Composition (new archetype): full-bleed photo top 600 px with masthead on photo → headline → split-flap board panel
  (two rows, arrow + label + flap digits) → 3-figure strip → one-line news tip → footer (sources | url + signature).
Type: Inter 800 headline + Inter text (EN/RU), IBM Plex Mono 600 flap digits/labels; Vazirmatn 900/400 (FA);
  IBM Plex Sans Arabic 600/400 (AR). No Cormorant/Playfair/Space Grotesk (used 20–22 Nov).
Imagery: photos/cr-express-zhengzhou-putian.jpg (Windmemories, CC BY-SA 4.0, Wikimedia Commons). No maps, no flags.
Logo: "Seal signature" tone-on-tone chalk seal + chalk wordmarks at the footer end; no echo (tried behind the board,
  read as clutter; dropped).
Carousel order (random, first != RU of 22 Nov): FA, EN, AR, RU.

FACTS (fetched 23 Nov 2026)
- Xinhua, 11 Nov 2026 (NDRC official Liang Linchong at press conference): Jan–Oct 2026 China–Europe freight trains
  18,661 trips (+14.6% y/y), 1.865 million TEU (+11.2%); return 9,360 vs outbound 9,301; loaded container ratio 100%
  for 50 consecutive months as of October; trans-Caspian line now daily.
- Xinhua, 20 Nov 2026: Wuhan sent its 500th China–Europe train of 2026 on 20 Nov, bound for Moscow; 454,800 t this
  year, +44.2% y/y; 64 routes, 167 cities in 46 countries.
"""
import os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from linkwin_mark import MARK_CSS, signature, echo
DATE = "2026-11-23"; SLUG = "rail-both-ways"
ORDER = ["fa", "en", "ar", "ru"]
NB = "\u00a0"

T = {
"en": dict(dir="ltr", kicker="Rail freight · China–Europe", date="23 Nov 2026",
  h="China–Europe trains now run full both ways",
  board="Trains · Jan–Oct 2026", out=("Outbound", "9,301"), ret=("Return", "9,360"),
  strip=[("18,661", "trains, +14.6% y/y"), ("1.865M", "TEU, +11.2% y/y"), ("100%", "loaded, 50 months running")],
  tip="Wuhan sent its 500th train of 2026 on 20 Nov, bound for Moscow.",
  src="Sources: NDRC via Xinhua, 11 Nov 2026<br>Xinhua, 20 Nov 2026",
  photo="Photo: CR Express container train, Zhengzhou · Windmemories, CC BY-SA 4.0, Wikimedia Commons"),
"ru": dict(dir="ltr", kicker="Ж/д перевозки · Китай — Европа", date="23.11.2026",
  h="Поезда Китай — Европа идут полными в обе стороны",
  board="Поезда · январь–октябрь 2026", out=("Из Китая", f"9{NB}301"), ret=("В Китай", f"9{NB}360"),
  strip=[(f"18{NB}661", f"поезд, +14,6{NB}% г/г"), (f"1,865{NB}млн", f"TEU, +11,2{NB}% г/г"), (f"100{NB}%", "загрузка 50 месяцев подряд")],
  tip="20 ноября Ухань отправил 500-й поезд 2026 года — в Москву.",
  src="Источники: ГКРР КНР через Синьхуа, 11.11.2026<br>Синьхуа, 20.11.2026",
  photo="Фото: контейнерный поезд CR Express, Чжэнчжоу · Windmemories, CC BY-SA 4.0, Wikimedia Commons"),
"fa": dict(dir="rtl", kicker="حمل ریلی · چین–اروپا", date="۲ آذر ۱۴۰۵",
  h="قطارهای چین–اروپا حالا در هر دو مسیر پُر حرکت می‌کنند",
  board="تعداد قطارها · ژانویه تا اکتبر ۲۰۲۶", out=("رفت", "۹٬۳۰۱"), ret=("برگشت", "۹٬۳۶۰"),
  strip=[("۱۸٬۶۶۱", "قطار، ۱۴٫۶٪ رشد سالانه"), ("۱٫۸۶۵ میلیون", "<bdi>TEU</bdi>، ۱۱٫۲٪ رشد سالانه"), ("۱۰۰٪", "ظرفیت پُر، ۵۰ ماه پیاپی")],
  tip="ووهان ۲۹ آبان پانصدمین قطار امسالِ خود را راهی مسکو کرد.",
  src="منابع: کمیسیون ملی توسعه و اصلاحات چین به نقل از شین‌هوا، ۲۰ آبان ۱۴۰۵<br>شین‌هوا، ۲۹ آبان ۱۴۰۵",
  photo="عکس: قطار کانتینری <bdi>CR Express</bdi>، ژنگ‌ژو · <bdi>Windmemories, CC BY-SA 4.0</bdi>، ویکی‌مدیا کامنز"),
"ar": dict(dir="rtl", kicker="الشحن بالسكك الحديدية · الصين–أوروبا", date="<bdi>23</bdi> نوفمبر <bdi>2026</bdi>",
  h="قطارات الصين–أوروبا تسير الآن محمّلة بالكامل في الاتجاهين",
  board="عدد القطارات · يناير–أكتوبر <bdi>2026</bdi>", out=("ذهاباً", "9,301"), ret=("إياباً", "9,360"),
  strip=[("18,661", "قطاراً، بزيادة <bdi>14.6%</bdi> سنوياً"), ("<bdi>1.865</bdi> مليون", "حاوية نمطية <bdi>TEU</bdi>، بزيادة <bdi>11.2%</bdi>"), ("100%", "نسبة التحميل لـ<bdi>50</bdi> شهراً متتالياً")],
  tip="أطلقت ووهان في <bdi>20</bdi> نوفمبر قطارها الـ<bdi>500</bdi> لعام <bdi>2026</bdi> متجهاً إلى موسكو.",
  src="المصادر: اللجنة الوطنية للتنمية والإصلاح عبر شينخوا، <bdi>11</bdi> نوفمبر <bdi>2026</bdi><br>شينخوا، <bdi>20</bdi> نوفمبر <bdi>2026</bdi>",
  photo="الصورة: قطار حاويات <bdi>CR Express</bdi>، تشنغتشو · <bdi>Windmemories, CC BY-SA 4.0</bdi>، ويكيميديا كومنز"),
}

ARROW = '<svg viewBox="0 0 120 24" class="arr"><path d="M2 12H112" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M100 2L114 12L100 22" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def flaps(num):
    out = []
    for ch in num:
        if ch in ",٬. " + NB:
            out.append(f'<span class="sep">{ch if ch not in (" ", NB) else ""}</span>')
        else:
            out.append(f'<span class="fl">{ch}</span>')
    return "".join(out)

def html(lang):
    t = T[lang]; rtl = t["dir"] == "rtl"
    if lang == "fa": hf, bf, hw = "'Vazirmatn','Inter',sans-serif", "'Vazirmatn','Inter',sans-serif", 900
    elif lang == "ar": hf, bf, hw = "'IBM Plex Sans Arabic','Inter',sans-serif", "'IBM Plex Sans Arabic','Inter',sans-serif", 600
    else: hf, bf, hw = "'Inter',sans-serif", "'Inter',sans-serif", 800
    hsize = {"en": 70, "ru": 62, "fa": 54, "ar": 54}[lang]
    hlh = {"en": 1.04, "ru": 1.06, "fa": 1.5, "ar": 1.45}[lang]
    s, e = ("right", "left") if rtl else ("left", "right")
    ls = "0" if rtl else ".16em"
    row = lambda cls, lab, num, flip: f'<div class="row {cls}"><div class="lab">{"<span class=a style=transform:scaleX(-1)>" if flip else "<span class=a>"}{ARROW}</span><span>{lab}</span></div><div class="num" dir="ltr">{flaps(num)}</div></div>'
    # outbound arrow points in reading direction; return arrow points back
    out_flip = rtl; ret_flip = not rtl
    strip = "".join(f'<div class="c"><div class="v">{v}</div><div class="l">{l}</div></div>' for v, l in t["strip"])
    return f"""<!doctype html><html lang="{lang}" dir="{t['dir']}"><head><meta charset="utf-8">
<link rel="stylesheet" href="../brand/fonts.css"><style>
:root{{--bg:#17191C;--panel:#202327;--chalk:#F1EFEA;--ice:#8DB8FF;--mint:#5ED3A4;--warm:#9A9893;--lw-ink:#F1EFEA;--lw-seal:#F1EFEA}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1350px;overflow:hidden;background:var(--bg);color:var(--chalk);font-family:{bf}}}
bdi{{direction:ltr;unicode-bidi:isolate}}
.ph{{position:absolute;left:0;top:0;width:1080px;height:610px;overflow:hidden}}
.ph img{{width:100%;height:100%;object-fit:cover;object-position:50% 62%;filter:saturate(.9) contrast(1.04) brightness(.93)}}
.ph:after{{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(23,25,28,.62) 0%,rgba(23,25,28,0) 26%,rgba(23,25,28,0) 52%,rgba(23,25,28,.88) 86%,#17191C 100%)}}
.mast{{position:absolute;top:58px;left:72px;right:72px;display:flex;justify-content:space-between;align-items:center;z-index:2;font:600 19px/1 {bf};letter-spacing:{ls};text-transform:uppercase;color:rgba(241,239,234,.92)}}
.mast .k{{display:flex;align-items:center;gap:14px}}
.mast .k:before{{content:"";width:10px;height:10px;border-radius:50%;background:var(--mint);box-shadow:0 0 0 5px rgba(94,211,164,.22)}}
.cr{{position:absolute;top:96px;{s}:72px;z-index:2;font:400 14px/1.4 'Inter',{bf};color:rgba(241,239,234,.7)}}
.main{{position:absolute;left:72px;right:72px;top:446px;bottom:56px;display:flex;flex-direction:column;z-index:1}}
h1{{font:{hw} {hsize}px/{hlh} {hf};letter-spacing:{'0' if rtl else '-.025em'};max-width:900px;text-wrap:balance}}
.board{{margin-top:40px;background:var(--panel);border:1px solid rgba(241,239,234,.1);border-radius:20px;padding:26px 34px 30px;position:relative;overflow:hidden}}
.board .bl{{font:500 17px/1 'IBM Plex Mono',{bf};letter-spacing:{'0' if rtl else '.12em'};text-transform:uppercase;color:var(--warm);padding-bottom:18px;border-bottom:1px dashed rgba(241,239,234,.16)}}
.row{{display:flex;align-items:center;justify-content:space-between;padding-top:22px}}
.row .lab{{display:flex;align-items:center;gap:20px;font:{'600 30px/1.3' if rtl else '600 30px/1'} {bf}}}
.row .a{{display:inline-flex}} .arr{{width:84px;height:18px}}
.out .a{{color:var(--ice)}} .ret .a{{color:var(--mint)}}
.num{{display:flex;align-items:center;gap:6px}}
.fl{{position:relative;width:60px;height:84px;border-radius:8px;background:linear-gradient(180deg,#2C3035 0%,#24272B 49.6%,#1B1D20 50.4%,#212428 100%);display:flex;align-items:center;justify-content:center;font:600 56px/1 'IBM Plex Mono','Vazirmatn',monospace;box-shadow:inset 0 1px 0 rgba(255,255,255,.06),0 2px 0 rgba(0,0,0,.35)}}
.fl:after{{content:"";position:absolute;left:0;right:0;top:50%;height:1.5px;background:rgba(0,0,0,.55)}}
.out .fl{{color:var(--ice)}} .ret .fl{{color:var(--mint)}}
.sep{{width:16px;text-align:center;font:600 44px/1 'IBM Plex Mono','Vazirmatn',monospace;color:var(--warm);align-self:flex-end;padding-bottom:6px}}
.board .lw-echo{{--lw-echo:#F1EFEA;--lw-echo-op:.035;--lw-echo-size:400px}}
.board>*{{position:relative;z-index:1}}
.strip{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:28px;margin-top:34px}}
.c{{border-top:2px solid rgba(241,239,234,.22);padding-top:16px}}
.c:first-child{{border-top-color:var(--mint)}}
.c .v{{font:{'800 40px/1.25' if rtl else '800 42px/1'} {hf};letter-spacing:{'0' if rtl else '-.02em'};white-space:nowrap}}
.c .l{{font:{'400 20px/1.55' if rtl else '400 20px/1.35'} {bf};color:rgba(241,239,234,.74);margin-top:10px}}
.tip{{margin-top:30px;font:{'600 23px/1.6' if rtl else '600 23px/1.4'} {bf};display:flex;gap:16px;align-items:baseline}}
.tip:before{{content:"";flex:none;width:12px;height:12px;background:var(--mint);transform:translateY(-2px)}}
.foot{{margin-top:auto;display:flex;align-items:flex-end;justify-content:space-between;gap:30px;padding-top:22px;border-top:1px solid rgba(241,239,234,.12)}}
.foot .src{{font:{'400 14px/1.65' if rtl else '400 14px/1.5'} {bf};color:var(--warm);max-width:520px}}
.foot .end{{display:flex;align-items:center;gap:26px}}
.foot .url{{font:600 22px/1 'IBM Plex Mono',monospace;letter-spacing:.02em;color:var(--chalk)}}
.lw-sig{{--lw-sig-h:58px}}
__MARKCSS__
</style></head><body>
<div class="ph"><img src="../photos/cr-express-zhengzhou-putian.jpg"></div>
<div class="mast"><span class="k">{t['kicker']}</span><span>{t['date']}</span></div>
<div class="main">
  <h1>{t['h']}</h1>
  <div class="board"><div class="bl">{t['board']}</div>{row('out', *t['out'], out_flip)}{row('ret', *t['ret'], ret_flip)}</div>
  <div class="strip">{strip}</div>
  <div class="tip"><span>{t['tip']}</span></div>
  <div class="foot"><div class="src">{t['src']}<br>{t['photo']}</div><div class="end"><span class="url">linkwinco.com</span>{signature()}</div></div>
</div></body></html>""".replace('__MARKCSS__', MARK_CSS)

if __name__ == "__main__":
    langs = sys.argv[1:] or ORDER
    os.makedirs(os.path.join(ROOT, "posts", DATE), exist_ok=True)
    for lang in langs:
        tpl = os.path.join(ROOT, "templates", f"{DATE}-{SLUG}-{lang}.html")
        open(tpl, "w", encoding="utf-8").write(html(lang))
        n = ORDER.index(lang) + 1
        out = os.path.join(ROOT, "posts", DATE, f"{DATE}-{SLUG}-{n}-{lang}.jpg")
        subprocess.run([sys.executable, os.path.join(ROOT, "tools", "render.py"), tpl, out, "feed"], check=False)
