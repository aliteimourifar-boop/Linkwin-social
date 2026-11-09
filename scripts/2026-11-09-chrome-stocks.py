"""LinkWin daily post, 9 Nov 2026.

CREATIVE BRIEF
Concept name: "Element 24" (periodic-table poster).
Idea: chromium as a polished metal tile on warm paper, with its neighbours Mn and Fe marching off the page.
  Calm, expert, material; the feel of a science-museum print, not a market dashboard.
Background tone: light (warm paper).
Palette: paper #EEE9E0, graphite #1F2328, polished steel greys #8E959E-#F4F6F8, seal red #AC3E33 on the key number only.
Composition: minimal editorial poster: oversized element tile (material hero), ghost neighbours cropped by the canvas,
  serif headline, one key number.
Type: Playfair Display + Manrope (EN/RU, sharp editorial against a steel tile) / Noto Naskh Arabic + IBM Plex Sans Arabic (FA/AR).
Imagery: none. Photo library empty and photo sites blocked (8 Nov note). Material CSS texture (polished chrome) as the hero.
Logo: A, printed seal, multiply on paper, bottom corner (first time; not top-left box).
RTL plan: tile row and footer mirror; Mn/Fe ghosts crop off the left edge; text right-aligned, Naskh headline re-sized.
"""
import os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLUG = "2026-11-09-chrome-stocks"
NB = " "
T = {
"en": dict(dir="ltr", kick="Chromium market", date="November 2026",
  name="Chromium", mn="Manganese", fe="Iron", z=("24","25","26"), m=("51.996","54.938","55.845"),
  h="Chrome is piling up at China’s ports.",
  n="5.24", u="million tonnes",
  l="of chrome ore in port on 30 Oct, above June's <span style=\"white-space:nowrap\">4.7 million-tonne</span> record.",
  s="TISCO's November ferrochrome tender: RMB 7,395 per 50% Cr tonne, down 200.",
  b="Buyers hold the leverage, for now.",
  foot="LinkWin sources ferroalloys from China", src="Source: SMM reports, Jul–Oct 2026"),
"fa": dict(dir="rtl", kick="بازار کروم", date="آبان ۱۴۰۵",
  name="کروم", mn="منگنز", fe="آهن", z=("۲۴","۲۵","۲۶"), m=("۵۱٫۹۹۶","۵۴٫۹۳۸","۵۵٫۸۴۵"),
  h="کوه کروم در بنادر چین بلندتر شد.",
  n="۵٫۲۴", u="میلیون تن",
  l="سنگ کروم در بنادر چین تا ۸ آبان؛ بالاتر از رکورد ۴٫۷ میلیون تنی تیرماه.",
  s="مناقصه این ماه فروکروم تیسکو: ۷٬۳۹۵ یوان برای هر تن با پایه ۵۰٪ کروم، ۲۰۰ یوان ارزان‌تر.",
  b="فعلاً دست خریدار بالاست.",
  foot="تأمین فروآلیاژ از چین با LinkWin", src="منبع: گزارش‌های SMM، تیر تا آبان ۱۴۰۵"),
"ru": dict(dir="ltr", kick="Рынок хрома", date="ноябрь 2026",
  name="Хром", mn="Марганец", fe="Железо", z=("24","25","26"), m=("51,996","54,938","55,845"),
  h="Хромовая руда копится в портах Китая.",
  n="5,24", u="млн тонн",
  l="руды в портах на 30 октября — выше июньского рекорда (4,7 млн т).",
  s=f"Тендер TISCO на феррохром в ноябре: 7{NB}395 юаней/т (база 50% Cr), минус 200.",
  b="Пока козыри у покупателя.",
  foot="LinkWin: поставки ферросплавов из Китая", src="Источник: отчёты SMM, июль–октябрь 2026"),
"ar": dict(dir="rtl", kick="سوق الكروم", date="نوفمبر 2026",
  name="الكروم", mn="المنغنيز", fe="الحديد", z=("24","25","26"), m=("51.996","54.938","55.845"),
  h="جبال الكروم تتراكم في موانئ الصين.",
  n="5.24", u="مليون طن",
  l="من خام الكروم في الموانئ حتى 30 أكتوبر، فوق رقم يونيو القياسي <span style=\"white-space:nowrap\">(4.7 مليون طن)</span>.",
  s="مناقصة تيسكو للفيروكروم في نوفمبر: 7,395 يوانًا للطن (أساس 50% كروم)، بتراجع 200 يوان.",
  b="الكفّة حاليًا لصالح المشتري.",
  foot="توريد السبائك الحديدية من الصين مع LinkWin", src="المصدر: تقارير SMM، يوليو – أكتوبر 2026"),
}

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px;overflow:hidden}
html.story,html.story body{height:1920px}
body{background:#EEE9E0;color:#1F2328;font-family:var(--body);position:relative}
/* paper warmth */
body:before{content:"";position:absolute;inset:0;background:radial-gradient(900px 700px at 22% 18%,#F6F2EA 0%,rgba(246,242,234,0) 70%)}
.stage{position:absolute;inset:0;padding:64px;display:flex;flex-direction:column;overflow:hidden}
html.story .stage{padding:230px 72px 264px}
.top{display:flex;justify-content:space-between;align-items:baseline;font-size:25px;color:#1F2328;margin-bottom:30px;position:relative}
.top b{font-weight:600}
.top span{color:#6C7076}
.ltr .top{letter-spacing:.14em;text-transform:uppercase;font-size:22px}
.row{display:flex;gap:18px;height:var(--rf);position:relative;flex:none}
html.story .row{height:var(--rs)}
.tile{flex:none;position:relative;width:470px;height:100%;border-radius:6px;padding:26px 30px}
html.story .tile{width:470px}
.cr{background:linear-gradient(118deg,#F4F6F8 0%,#BCC3CB 16%,#F8FAFB 30%,#8E959E 47%,#D9DEE3 60%,#A4ABB4 78%,#EFF2F5 100%);
    box-shadow:0 34px 60px -28px rgba(31,35,40,.48),0 2px 3px rgba(31,35,40,.18),inset 0 0 0 1px rgba(255,255,255,.55)}
.cr:after{content:"";position:absolute;inset:0;border-radius:6px;pointer-events:none;
    background:repeating-linear-gradient(90deg,rgba(255,255,255,.055) 0 1px,rgba(31,35,40,.03) 1px 3px)}
.ghost{width:300px;border:1.5px solid rgba(31,35,40,.26);color:rgba(31,35,40,.42)}
html.story .ghost{width:300px}
.t-z{font-family:'Manrope',var(--body);font-size:44px;font-weight:600;position:relative;z-index:1}
.t-sym{position:absolute;left:0;right:0;top:50%;transform:translateY(-54%);text-align:center;font-family:'Playfair Display',serif;font-weight:700;font-size:250px;line-height:1;z-index:1;color:#1F2328;text-shadow:0 1px 0 rgba(255,255,255,.75)}
html.story .t-sym{font-size:250px}
.ghost .t-sym{font-size:150px;color:rgba(31,35,40,.32);text-shadow:none;font-weight:400}
html.story .ghost .t-sym{font-size:150px}
.t-name{position:absolute;bottom:26px;left:30px;right:30px;display:flex;justify-content:space-between;align-items:baseline;font-size:27px;z-index:1;font-weight:600}
.ghost .t-name{font-size:23px;font-weight:400}
.t-name i{font-style:normal;font-weight:400;font-size:22px;opacity:.72}
html.story .t-z{font-size:52px}
html.story .t-name{font-size:32px}
html.story .ghost .t-name{font-size:25px}
.row,h1,.num,.l,.s,.b{flex:none}
h1{font-family:var(--head);font-weight:700;font-size:var(--h);line-height:var(--lh);margin-top:32px;max-width:940px}
html.story h1{font-size:var(--hs);margin-top:44px}
.num{display:flex;align-items:baseline;gap:18px;margin-top:22px}
html.story .num{margin-top:36px}
.num b{font-family:'Playfair Display',var(--head);font-weight:700;font-size:112px;line-height:1;color:#AC3E33}
html.story .num b{font-size:130px}
.num em{font-style:normal;font-size:36px;font-weight:600}
html.story .num em{font-size:42px}
.l{font-size:27px;line-height:1.42;margin-top:6px;max-width:900px}
.s{font-size:23px;line-height:1.5;color:#44484E;margin-top:14px;max-width:900px}
html.story .l{font-size:33px;margin-top:14px}
html.story .s{font-size:27px;margin-top:22px}
.b{font-family:var(--head);font-weight:700;font-size:var(--bs);margin-top:14px}
html.story .b{font-size:calc(var(--bs) * 1.22);margin-top:26px}
.foot{margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end;gap:24px;border-top:1px solid rgba(31,35,40,.22);padding-top:14px}
.ft{font-size:21px;line-height:1.42;color:#44484E}
.ft b{color:#1F2328;font-weight:600}
.ft .url{color:#1F2328;font-weight:600}
.logo{height:118px;width:auto;mix-blend-mode:multiply;filter:brightness(1.015);flex:none}
html.story .logo{height:136px}
.rtl{--head:'Noto Naskh Arabic','Playfair Display',serif;--body:'IBM Plex Sans Arabic','Manrope',sans-serif}
.ltr{--head:'Playfair Display',serif;--body:'Manrope',sans-serif}
.rtl h1{line-height:1.5}
.rtl .l,.rtl .s{line-height:1.6}
.rtl .l{font-size:30px}
.rtl .s{font-size:25px}
html.story.rtl .l{font-size:35px}
html.story.rtl .s{font-size:29px}
"""

def page(lang, c):
    cls = "rtl" if c["dir"] == "rtl" else "ltr"
    h, lh, hs, bs = {"en":("78px","1.1","96px","38px"),"ru":("68px","1.12","80px","36px"),"fa":("74px","1.5","76px","40px"),"ar":("64px","1.5","68px","38px")}[lang]
    rf, rs = {"en":("486px","440px"),"ru":("470px","430px"),"fa":("486px","470px"),"ar":("486px","470px")}[lang]
    z, m = c["z"], c["m"]
    def tile(k, sym, name, i):
        return f'<div class="tile {k}"><div class="t-z">{z[i]}</div><div class="t-sym">{sym}</div><div class="t-name"><span>{name}</span><i>{m[i]}</i></div></div>'
    return f"""<!doctype html><html lang="{lang}" dir="{c['dir']}" class="{cls}" style="--h:{h};--lh:{lh};--hs:{hs};--bs:{bs};--rf:{rf};--rs:{rs}"><head><meta charset="utf-8">
<link rel="stylesheet" href="../brand/fonts.css"><style>{CSS}</style></head><body><div class="stage">
<div class="top"><b>{c['kick']}</b><span>{c['date']}</span></div>
<div class="row">{tile('cr','Cr',c['name'],0)}{tile('ghost','Mn',c['mn'],1)}{tile('ghost','Fe',c['fe'],2)}</div>
<h1>{c['h']}</h1>
<div class="num"><b>{c['n']}</b><em>{c['u']}</em></div>
<div class="l">{c['l']}</div>
<div class="s">{c['s']}</div>
<div class="b">{c['b']}</div>
<div class="foot"><div class="ft"><b>{c['foot']}</b><br>{c['src']}<br><span class="url">linkwinco.com</span></div><img class="logo" src="../brand/linkwin-logo-original-cropped.png"></div>
</div></body></html>"""

for lang, c in T.items():
    tpl = f"{ROOT}/templates/{SLUG}-{lang}.html"
    open(tpl, "w").write(page(lang, c))
    for mode, suffix in (("feed",""),("story","-story")):
        subprocess.run([sys.executable, f"{ROOT}/render.py", tpl, f"{ROOT}/posts/{SLUG}-{lang}{suffix}.jpg", mode], check=True)
