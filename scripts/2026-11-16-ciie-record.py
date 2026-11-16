"""LinkWin daily post, 16 Nov 2026 — China's import expo (9th CIIE) closes with a record US$85.45 bn in intended deals.

CREATIVE BRIEF
Concept name: "Clover Print" (the four-leaf-clover expo halls seen from the air, presented as a framed print on clover green).
Idea: China as a buyer. The aerial photo of the National Exhibition and Convention Center (Shanghai), the CIIE venue, sits
  like a gallery print with a pale-gold offset hairline frame; below it a serif headline and one key number in gold,
  then two small facts. Calm confidence, an opportunity for exporters, not a market alarm.
Background tone: mid (clover green) after 15 Nov sand, 14 Nov chalk, 13 Nov dark blue-hour photo.
Palette: clover green #35594A, cream #F4EFE3, pale gold #D8BE7E, sage mist #B9CBBF. Seal tone-on-tone in cream (red clashes on green).
Composition: masthead -> framed photo print (offset gold hairline) -> serif headline -> key number row (gold numeral + label)
  -> two-fact row split by a hairline -> footer (sources, photo credit, signature). Archetype: framed print / gallery plate
  (not a horizon split, not a ledger, not a full-bleed photo).
Story (9:16): taller print, larger headline, facts stacked; content y 220-1650.
Type: Cormorant Garamond 700 headline + numerals, Manrope text (EN/RU); Noto Naskh Arabic 700 headline + Vazirmatn (FA, also
  FA numerals) / IBM Plex Sans Arabic (AR) text, Cormorant for AR Western digits.
Imagery: photos/shanghai-necc-aerial.jpg (SSYoung, CC BY-SA 4.0, Wikimedia Commons).
Logo: "Seal signature + echo" with the seal tone-on-tone in cream + cream wordmarks, footer end side; 5 % cream echo cropped
  by the top corner (left in RTL).
RTL: dir=rtl mirrors mast, key row, fact row, footer and signature; echo on the left.

FACTS (sources fetched 16 Nov 2026)
- Xinhua (english.news.cn) 10 Nov 2026: 9th CIIE concluded in Shanghai on Tuesday (10 Nov); one-year intended deals a
  record US$85.45 bn, +2.3 % on the previous edition; first held 2018; world's first national-level import expo.
- People's Daily Online Shanghai 10 Nov 2026 / Shanghai Commerce Commission 10 Nov: 162 countries, regions and int'l
  organisations; 4,142 exhibiting (overseas) companies, a record; exhibition area >440,000 m2.
- Global Times 10 Nov 2026 / NBD 10 Nov: 143 companies and organisations already signed for the 10th CIIE, >100,000 m2.
"""
import os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from linkwin_mark import MARK_CSS, signature, echo
DATE = "2026-11-16"
SLUG = "ciie-record"
NB = "\u00a0"

T = {
"en": dict(dir="ltr", lang="en", kicker="Import & export · Shanghai", date="16 Nov 2026",
  h="China's import expo closes with a record deal tally",
  num="$85.45" + NB + "bn", lab="one-year intended deals at the 9th CIIE, up 2.3% on last year",
  f1=("4,142", "exhibiting companies, a new high"), f2=("143", "already signed up for the 10th CIIE"),
  hook="LinkWin · your trade partner in China",
  photo="Photo: National Exhibition and Convention Center (Shanghai) · SSYoung, CC BY-SA 4.0, Wikimedia Commons",
  src="Sources: Xinhua; People's Daily Online; Global Times, 10 Nov 2026"),
"fa": dict(dir="rtl", lang="fa", kicker="واردات و صادرات · شانگهای", date="۲۵ آبان ۱۴۰۵",
  h="نمایشگاه واردات چین با رکورد تازهٔ قراردادها به پایان رسید",
  num="۸۵٫۴۵ میلیارد دلار", lab="ارزش توافق‌های اولیهٔ خرید برای یک سال در نهمین CIIE؛ ۲٫۳٪ بیشتر از دورهٔ قبل",
  f1=("۴٬۱۴۲", "شرکت نمایشگر؛ بیشترین تعداد تاکنون"), f2=("۱۴۳", "شرکت و نهاد که برای دورهٔ دهم ثبت‌نام کرده‌اند"),
  hook="LinkWin، شریک تجاری شما در چین",
  photo="عکس: مرکز ملی نمایشگاه و همایش شانگهای · SSYoung، مجوز CC BY-SA 4.0، ویکی‌مدیا کامانز",
  src="منابع: شین‌هوا، پیپلز دیلی آنلاین و گلوبال تایمز، ۱۹ آبان ۱۴۰۵"),
"ru": dict(dir="ltr", lang="ru", kicker="Импорт и экспорт · Шанхай", date="16.11.2026",
  h="Импортная выставка Китая закрылась рекордом по сделкам",
  num="85,45" + NB + "млрд" + NB + "$", lab="намерений о закупках на год на 9-й CIIE — на 2,3" + NB + "% больше, чем годом ранее",
  f1=("4" + NB + "142", "компании-экспонента — новый рекорд"), f2=("143", "участника уже записались на 10-ю CIIE"),
  hook="LinkWin — ваш торговый партнёр в Китае",
  photo="Фото: Национальный выставочный центр (Шанхай) · SSYoung, CC BY-SA 4.0, Wikimedia Commons",
  src="Источники: Синьхуа, «Жэньминь жибао» онлайн, Global Times, 10.11.2026"),
"ar": dict(dir="rtl", lang="ar", kicker="الاستيراد والتصدير · شنغهاي", date="<bdi>16</bdi> نوفمبر <bdi>2026</bdi>",
  h="معرض الصين للاستيراد يختتم دورته بصفقات قياسية",
  num="<bdi>85.45</bdi> مليار دولار", lab="قيمة الصفقات المزمعة لعام كامل في الدورة التاسعة من CIIE، بزيادة <bdi>2.3%</bdi> عن الدورة السابقة",
  f1=("4,142", "شركة عارضة، وهو رقم قياسي"), f2=("143", "شركة ومؤسسة سجّلت بالفعل للدورة العاشرة"),
  hook="LinkWin، شريكك التجاري في الصين",
  photo="الصورة: المركز الوطني للمعارض والمؤتمرات (شنغهاي) · SSYoung، ترخيص <bdi>CC BY-SA 4.0</bdi>، ويكيميديا كومنز",
  src="المصادر: شينخوا، وصحيفة الشعب أونلاين، وغلوبال تايمز، <bdi>10</bdi> نوفمبر <bdi>2026</bdi>"),
}
LAT_H, LAT_B = "'Cormorant Garamond','Manrope',serif", "'Manrope',sans-serif"
FONTS = {"en": (LAT_H, LAT_B, LAT_H), "ru": (LAT_H, LAT_B, LAT_H),
         "fa": ("'Noto Naskh Arabic','Cormorant Garamond',serif", "'Vazirmatn','Manrope',sans-serif", "'Vazirmatn',sans-serif"),
         "ar": ("'Noto Naskh Arabic','Cormorant Garamond',serif", "'IBM Plex Sans Arabic','Manrope',sans-serif", "'Cormorant Garamond','Noto Naskh Arabic',serif")}
TUNE = {"en": dict(h=72, hlh=1.04, num=104), "ru": dict(h=66, hlh=1.06, num=96),
        "fa": dict(h=54, hlh=1.6, num=66), "ar": dict(h=56, hlh=1.6, num=76)}

def html(lang):
    t = T[lang]; hf, bf, nf = FONTS[lang]; k = TUNE[lang]
    rtl = t["dir"] == "rtl"
    ls = "0" if rtl else ".18em"; tt = "none" if rtl else "uppercase"
    start, end = ("right", "left") if rtl else ("left", "right")
    nw = '800' if lang == 'fa' else '700'
    return f"""<!doctype html><html lang="{t['lang']}" dir="{t['dir']}"><head><meta charset="utf-8">
<link rel="stylesheet" href="../brand/fonts.css">
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1080px;height:1350px;overflow:hidden;background:#35594A}}
body{{position:relative;font-family:{bf};color:#F4EFE3;-webkit-font-smoothing:antialiased;
  --lw-ink:#F4EFE3;--lw-seal:#F4EFE3;--lw-echo:#F4EFE3;--lw-echo-op:.04;--lw-echo-size:560px}}
body:before{{content:"";position:absolute;inset:0;z-index:0;background:radial-gradient(1000px 700px at 50% 0%,rgba(255,255,255,.07),transparent 65%),radial-gradient(800px 500px at 50% 100%,rgba(0,0,0,.16),transparent 70%)}}
.page{{position:absolute;inset:58px 72px 52px;display:flex;flex-direction:column;z-index:1}}
.mast{{display:flex;justify-content:space-between;align-items:center;padding-bottom:16px;border-bottom:1px solid rgba(244,239,227,.35);
  font:600 19px/1.2 {bf};letter-spacing:{ls};text-transform:{tt}}}
.mast .d{{letter-spacing:{'0' if rtl else '.08em'};color:#D8BE7E}}
.print{{position:relative;margin:40px 12px 0;height:548px;outline:1px solid rgba(216,190,126,.75);outline-offset:11px;
  background:url(../photos/shanghai-necc-aerial.jpg) center 46%/cover;filter:contrast(1.3) saturate(.85) sepia(.12) brightness(.98);
  box-shadow:0 24px 50px rgba(0,0,0,.28)}}
h1{{margin-top:auto;font:700 {k['h']}px/{k['hlh']} {hf};letter-spacing:{'0' if rtl else '-.01em'};text-wrap:balance;max-width:920px}}
.key{{margin-top:26px;display:flex;align-items:center;gap:30px;padding:22px 0;border-top:1px solid rgba(216,190,126,.6);border-bottom:1px solid rgba(244,239,227,.22)}}
.key b{{flex:none;font:{nw} {k['num']}px/1 {nf};color:#D8BE7E;letter-spacing:{'0' if rtl else '-.01em'};white-space:nowrap}}
.key p{{font:400 21px/1.45 {bf};color:#DCE5DE;max-width:440px}}
.facts{{display:grid;grid-template-columns:1fr 1fr;margin-top:0}}
.fact{{display:flex;align-items:baseline;gap:14px;padding:18px 0 0}}
.fact+.fact{{padding-{start}:28px;border-{start}:1px solid rgba(244,239,227,.22)}}
.fact b{{font:{nw} 46px/1 {nf};color:#F4EFE3;white-space:nowrap}}
.fact span{{font:400 19px/1.4 {bf};color:#B9CBBF}}
.foot{{margin-top:28px;display:flex;align-items:flex-end;justify-content:space-between;gap:28px;padding-top:18px;border-top:1px solid rgba(244,239,227,.22)}}
.ft{{font:400 14px/1.5 {bf};color:#B9CBBF;max-width:690px}}
.ft .hook{{font:600 19px/1.4 {bf};color:#F4EFE3}}
.ft .url{{font:700 19px/1.4 'Manrope',sans-serif;color:#D8BE7E;letter-spacing:.02em}}
.ft .src{{margin-top:6px}}
__MARKCSS__
.lw-sig{{--lw-sig-h:60px}}
html.story,html.story body{{width:1080px;height:1920px}}
html.story .page{{inset:220px 80px 270px}}
html.story .print{{height:640px;margin-top:46px}}
html.story h1{{padding-top:44px}}
html.story h1{{font-size:{k['h']+6}px}}
html.story .key{{flex-direction:column;align-items:flex-start;gap:14px}}
html.story .key p{{font-size:23px}}
html.story .facts{{grid-template-columns:1fr}}
html.story .fact,html.story .fact+.fact{{padding:16px 0 0;border-{start}:0}}
html.story .fact+.fact{{margin-top:14px;border-top:1px solid rgba(244,239,227,.18)}}
html.story .ft{{max-width:620px;font-size:15px}}
html.story .lw-echo{{top:300px !important;bottom:auto !important;--lw-echo-size:460px}}
</style></head><body>
{echo(end, 'auto', '-170px')}
<style>.lw-echo{{top:-190px}}</style>
<div class="page">
  <div class="mast"><span>{t['kicker']}</span><span class="d">{t['date']}</span></div>
  <div class="print"></div>
  <h1>{t['h']}</h1>
  <div class="key"><b>{t['num']}</b><p>{t['lab']}</p></div>
  <div class="facts"><div class="fact"><b>{t['f1'][0]}</b><span>{t['f1'][1]}</span></div><div class="fact"><b>{t['f2'][0]}</b><span>{t['f2'][1]}</span></div></div>
  <div class="foot"><div class="ft"><div class="hook">{t['hook']}</div><div class="url">linkwinco.com</div><div class="src">{t['src']}<br>{t['photo']}</div></div>{signature()}</div>
</div></body></html>""".replace('__MARKCSS__', MARK_CSS)

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a]
    modes = [a for a in args if a in ("feed", "story")] or ["feed", "story"]
    langs = [a for a in args if a not in ("feed", "story")] or ["en", "fa", "ru", "ar"]
    for lang in langs:
        tpl = os.path.join(ROOT, "templates", f"{DATE}-{SLUG}-{lang}.html")
        open(tpl, "w", encoding="utf-8").write(html(lang))
        for mode in modes:
            suffix = "" if mode == "feed" else "-story"
            out = os.path.join(ROOT, "posts", DATE, f"{DATE}-{SLUG}-{lang}{suffix}.jpg")
            subprocess.run([sys.executable, os.path.join(ROOT, "tools", "render.py"), tpl, out, mode], check=False)
