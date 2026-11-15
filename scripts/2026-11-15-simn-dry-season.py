"""LinkWin daily post, 15 Nov 2026 — Silicomanganese: Yunnan's dry season splits China's supply (south idles, north runs).

CREATIVE BRIEF
Concept name: "Dry Season Horizon" (river-valley photograph fading into a dry sand page, with a three-column figure strip).
Idea: the end of Yunnan's hydropower season. A desaturated photo of the Jinsha River valley (transmission pylons on the
  ridge) dissolves into a sun-bleached sand page; the headline sits on the horizon where water meets dry ground.
  Three figures underneath: furnaces idled in the south, the HBIS November inquiry, northern spot price.
Background tone: mid-light (sand) after 14 Nov chalk ledger, 13 Nov dark blue-hour photo, 12 Nov manila.
Palette: sand #E7DFCF, deep slate ink #1F2A2B, dry ochre #B0692A, river grey-jade #5C7670; seal red #AC3E33 on seal only.
Composition: photo band (top ~52 %) with mast on the photo -> headline on the fade line -> deck -> 3-column figure strip
  (ochre rule over the 'south' column) -> footer with credit, sources and signature. Archetype: horizon split + figure
  strip (not a ledger route, not a full-bleed night photo, not a still life).
Story (9:16): taller photo band; headline, deck; figures stacked as rows (numeral | label); footer. Content y 220–1650.
Type: Space Grotesk 700 headline/figures + Manrope text (EN/RU); Noto Kufi Arabic 700 headline + Vazirmatn (FA, also FA numerals) /
  IBM Plex Sans Arabic (AR) text, Space Grotesk for Latin digits.
Imagery: photos/yunnan-jinsha-river-ludila.jpg (Zhangmoon618, CC BY-SA 3.0, Wikimedia Commons).
Logo: "Seal signature + echo": seal #AC3E33 + hairline + slate wordmarks, footer end side; 6 % slate echo cropped by the
  bottom corner of the sand page (left in RTL).

FACTS (sources fetched 15 Nov 2026)
- Business Society / 100ppi.com (PriceSeek), 3 Nov 2026 (also SunSirs): Yunnan wet season over, Nov power expected
  > RMB 0.5/kWh; since late Oct Yunnan SiMn plants halted; by 3 Nov 11 submerged-arc furnaces stopped; daily SiMn output
  down 1,380 t.
- Mysteel daily, 12 Nov 2026: south: few alloy plants still running, spot tight; Inner Mongolia production resilient, Oct
  settled power down 1-2 fen; SiMn futures 2701 closed 5,830 (-46); a Guangxi mill priced 5,900 RMB/t for 5,000 t.
- Mysteel via Xinhua Finance (cnfin.com) 13 Nov 2026 and SMM 12-13 Nov 2026: HBIS Nov SiMn first-round inquiry
  RMB 5,900/t; Oct final 5,980; Nov 2025 5,820; Nov volume 13,350 t (excl. 6,000 t plate) vs 15,250 t in Oct.
- Mysteel / 10jqka iFinD spot 13 Nov 2026: FeMn65Si17 Inner Mongolia 5,700, Tianjin 5,800 RMB/t.
"""
import os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from linkwin_mark import MARK_CSS, signature, echo
DATE = "2026-11-15"
SLUG = "simn-dry-season"
NB = "\u00a0"

T = {
"en": dict(dir="ltr", lang="en", kicker="Ferroalloys · Silicomanganese", date="15 Nov 2026",
  h="Dry season splits China's silicomanganese supply",
  deck="Yunnan's hydropower season is over. Pricier electricity has idled southern furnaces, Inner Mongolia keeps producing, and steel mills are bidding lower.",
  figs=[("11", "furnaces", "idled in Yunnan by 3 Nov, about 1,380 t less SiMn a day"),
        ("5,900", "RMB/t", "HBIS first-round SiMn inquiry for November, vs 5,980 in October"),
        ("5,700", "RMB/t", "FeMn65Si17 spot in Inner Mongolia on 13 Nov; Tianjin 5,800")],
  hook="LinkWin · ferroalloy sourcing from China",
  photo="Photo: Jinsha River near Ludila Hydropower Station, Yunnan · Zhangmoon618, CC BY-SA 3.0, Wikimedia Commons",
  src="Sources: Business Society (100ppi.com), 3 Nov; Mysteel, 12 Nov; SMM and Xinhua Finance, 13 Nov 2026"),
"fa": dict(dir="rtl", lang="fa", kicker="فروآلیاژ · سیلیکومنگنز", date="۲۴ آبان ۱۴۰۵",
  h="فصل کم‌آبی، عرضهٔ سیلیکومنگنز چین را دوپاره کرد",
  deck="فصل پرآبی یون‌نان تمام شده است. با گران‌شدن برق، کوره‌های جنوب خاموش شده‌اند، مغولستان داخلی همچنان تولید می‌کند و فولادسازها قیمت پایین‌تری پیشنهاد می‌دهند.",
  figs=[("۱۱", "کوره", "تا ۱۲ آبان در یون‌نان متوقف شد؛ یعنی روزانه حدود ۱٬۳۸۰ تن تولید کمتر"),
        ("۵٬۹۰۰", "یوان/تن", "نخستین استعلام قیمت گروه فولاد هبی برای نوامبر؛ رقم اکتبر ۵٬۹۸۰ بود"),
        ("۵٬۷۰۰", "یوان/تن", "قیمت نقدی گرید ۶۵/۱۷ در مغولستان داخلی در ۲۲ آبان؛ تیانجین ۵٬۸۰۰")],
  hook="LinkWin، تأمین فروآلیاژ از چین",
  photo="عکس: رود جین‌شا نزدیک نیروگاه آبی لودیلا، یون‌نان · Zhangmoon618، مجوز CC BY-SA 3.0، ویکی‌مدیا کامانز",
  src="منابع: بیزینس سوسایتی (100ppi)، ۱۲ آبان؛ مای‌استیل، ۲۱ آبان؛ SMM و شین‌هوا فایننس، ۲۲ آبان ۱۴۰۵"),
"ru": dict(dir="ltr", lang="ru", kicker="Ферросплавы · силикомарганец", date="15.11.2026",
  h="Сухой сезон расколол рынок силикомарганца в Китае",
  deck="Сезон дешёвой гидроэнергии в Юньнани закончился: из-за дорогого электричества южные печи встали, Внутренняя Монголия продолжает плавить, а сталевары снижают закупочные цены.",
  figs=[("11", "печей", "остановлены в Юньнани к 03.11 — минус около 1" + NB + "380 т SiMn в сутки"),
        ("5" + NB + "900", "юаней/т", "первая ноябрьская заявка HBIS на SiMn; в октябре — 5" + NB + "980"),
        ("5" + NB + "700", "юаней/т", "спот FeMn65Si17 во Внутренней Монголии 13.11; Тяньцзинь — 5" + NB + "800")],
  hook="LinkWin — ферросплавы из Китая",
  photo="Фото: река Цзиньшацзян у ГЭС Лудила, Юньнань · Zhangmoon618, CC BY-SA 3.0, Wikimedia Commons",
  src="Источники: Business Society (100ppi.com), 03.11; Mysteel, 12.11; SMM и Xinhua Finance, 13.11.2026"),
"ar": dict(dir="rtl", lang="ar", kicker="السبائك الحديدية · السيليكومنغنيز", date="<bdi>15</bdi> نوفمبر <bdi>2026</bdi>",
  h="موسم الجفاف يقسم إمدادات السيليكومنغنيز في الصين",
  deck="انتهى موسم الوفرة المائية في يونّان؛ فأوقف غلاء الكهرباء أفران الجنوب، بينما تواصل منغوليا الداخلية الإنتاج، وتعرض مصانع الصلب أسعار شراء أدنى.",
  figs=[("11", "فرنًا", "توقفت في يونّان حتى <bdi>3</bdi> نوفمبر، أي نحو <bdi>1,380</bdi> طنًا أقل يوميًا"),
        ("5,900", "يوان/طن", "أول استفسار سعري من مجموعة HBIS لشهر نوفمبر، مقابل <bdi>5,980</bdi> في أكتوبر"),
        ("5,700", "يوان/طن", "السعر الفوري لدرجة <bdi>65/17</bdi> في منغوليا الداخلية في <bdi>13</bdi> نوفمبر؛ وتيانجين <bdi>5,800</bdi>")],
  hook="LinkWin، توريد السبائك الحديدية من الصين",
  photo="الصورة: نهر جينشا قرب محطة لوديلا الكهرومائية، يونّان · Zhangmoon618، ترخيص <bdi>CC BY-SA 3.0</bdi>، ويكيميديا كومنز",
  src="المصادر: Business Society ‏(100ppi.com)، <bdi>3</bdi> نوفمبر؛ Mysteel، ‏<bdi>12</bdi> نوفمبر؛ SMM وXinhua Finance، ‏<bdi>13</bdi> نوفمبر <bdi>2026</bdi>"),
}
LAT_H, LAT_B = "'Space Grotesk','Manrope',sans-serif", "'Manrope',sans-serif"
FONTS = {"en": (LAT_H, LAT_B, LAT_H), "ru": (LAT_H, LAT_B, LAT_H),
         "fa": ("'Noto Kufi Arabic','Space Grotesk',sans-serif", "'Vazirmatn','Manrope',sans-serif", "'Vazirmatn',sans-serif"),
         "ar": ("'Noto Kufi Arabic','Space Grotesk',sans-serif", "'IBM Plex Sans Arabic','Manrope',sans-serif", LAT_H)}
TUNE = {"en": dict(h=74, hlh=1.06, deck=27), "ru": dict(h=66, hlh=1.08, deck=26),
        "fa": dict(h=60, hlh=1.55, deck=26), "ar": dict(h=60, hlh=1.55, deck=26)}

def html(lang):
    t = T[lang]; hf, bf, nf = FONTS[lang]; k = TUNE[lang]
    rtl = t["dir"] == "rtl"
    ls = "0" if rtl else ".18em"; tt = "none" if rtl else "uppercase"
    start, end = ("right", "left") if rtl else ("left", "right")
    figs = "".join(f'<div class="fig f{i}"><div class="num"><b>{n}</b><em>{u}</em></div><p>{l}</p></div>' for i, (n, u, l) in enumerate(t["figs"]))
    return f"""<!doctype html><html lang="{t['lang']}" dir="{t['dir']}"><head><meta charset="utf-8">
<link rel="stylesheet" href="../brand/fonts.css">
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1080px;height:1350px;overflow:hidden;background:#E7DFCF}}
body{{position:relative;font-family:{bf};color:#1F2A2B;-webkit-font-smoothing:antialiased;
  --lw-ink:#1F2A2B;--lw-echo:#1F2A2B;--lw-echo-op:.045;--lw-echo-size:520px}}
.photo{{position:absolute;left:0;right:0;top:0;height:720px;background:url(../photos/yunnan-jinsha-river-ludila.jpg) center 42%/cover;
  filter:saturate(.5) contrast(1.06) sepia(.12)}}
.fade{{position:absolute;left:0;right:0;top:0;height:722px;background:linear-gradient(180deg,rgba(231,223,207,.80) 0%,rgba(231,223,207,.35) 14%,rgba(231,223,207,0) 30%,rgba(231,223,207,0) 46%,rgba(231,223,207,.85) 80%,#E7DFCF 99%)}}
body:before{{content:"";position:absolute;inset:0;z-index:0;background:radial-gradient(900px 500px at 100% 100%,rgba(176,105,42,.10),transparent 60%)}}
.page{{position:absolute;inset:60px 72px 54px;display:flex;flex-direction:column;z-index:1}}
.mast{{display:flex;justify-content:space-between;align-items:center;padding-bottom:18px;border-bottom:1px solid rgba(31,42,43,.35);
  font:600 20px/1.2 {bf};letter-spacing:{ls};text-transform:{tt};color:#1F2A2B}}
.mast .d{{letter-spacing:{'0' if rtl else '.08em'};color:#1F2A2B}}
h1{{margin-top:auto;font:700 {k['h']}px/{k['hlh']} {hf};letter-spacing:{'0' if rtl else '-.02em'};text-wrap:balance;color:#1F2A2B;max-width:900px}}
.deck{{margin-top:22px;font:400 {k['deck']}px/1.5 {bf};color:#3C4847;max-width:900px}}
.figs{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:0;margin-top:40px}}
.fig{{padding:22px 26px 0 0;border-top:2px solid rgba(31,42,43,.7)}}
[dir=rtl] .fig{{padding:22px 0 0 26px}}
.fig+.fig{{padding-{start}:26px;border-{start}:1px solid rgba(31,42,43,.22)}}
.fig.f0{{border-top-color:#B0692A}}
.num{{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap}}
.num b{{font:{'800' if lang=='fa' else '700'} 64px/1 {nf};color:#1F2A2B;letter-spacing:{'0' if rtl else '-.02em'}}}
.fig.f0 .num b{{color:#B0692A}}
.num em{{font:600 20px/1.2 {bf};font-style:normal;color:#5C7670}}
.fig p{{margin-top:14px;font:400 19px/1.45 {bf};color:#3C4847}}
.foot{{margin-top:34px;display:flex;align-items:flex-end;justify-content:space-between;gap:28px;padding-top:20px;border-top:1px solid rgba(31,42,43,.22)}}
.ft{{font:400 14.5px/1.5 {bf};color:#5A6463;max-width:700px}}
.ft .hook{{font:600 19px/1.4 {bf};color:#1F2A2B}}
.ft .url{{font:700 19px/1.4 'Manrope',sans-serif;color:#B0692A;letter-spacing:.02em}}
.ft .src{{margin-top:6px}}
__MARKCSS__
.lw-sig{{--lw-sig-h:60px}}
html.story,html.story body{{width:1080px;height:1920px}}
html.story .photo{{height:1080px;background-position:center 40%}}
html.story .fade{{height:1082px}}
html.story .page{{inset:220px 80px 270px}}
html.story h1{{font-size:{k['h']+8}px}}
html.story .deck{{font-size:{k['deck']+2}px}}
html.story .figs{{grid-template-columns:1fr;margin-top:40px}}
html.story .fig,html.story .fig+.fig{{display:grid;grid-template-columns:330px 1fr;align-items:center;gap:24px;padding:20px 0;border-{start}:0;border-top:1px solid rgba(31,42,43,.22)}}
html.story .fig.f0{{border-top:2px solid #B0692A}}
html.story .num b{{font-size:72px}}
html.story .fig p{{margin-top:0;font-size:22px}}
html.story .ft{{max-width:640px;font-size:16px}}
html.story .lw-echo{{bottom:auto !important;top:1200px;--lw-echo-size:440px}}
</style></head><body>
<div class="photo"></div><div class="fade"></div>
{echo(end, '-170px', '-150px')}
<div class="page">
  <div class="mast"><span>{t['kicker']}</span><span class="d">{t['date']}</span></div>
  <h1>{t['h']}</h1>
  <p class="deck">{t['deck']}</p>
  <div class="figs">{figs}</div>
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
