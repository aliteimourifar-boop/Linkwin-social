"""LinkWin daily carousel, 20 Nov 2026 — Two Chinese ports, two new milestones (Ningbo-Zhoushan 40M TEU early; Nansha Phase IV goes foreign-trade).

CREATIVE BRIEF
Concept name: "Twin Berths" (a dusk photo of a working berth, then two port 'berth cards' side by side like a terminal board).
Idea: practical good news for shippers: more capacity and automation at both ends of China's coast (East: Ningbo-Zhoushan;
  South: Guangzhou Nansha). Calm, factual, useful; no market hype.
Background tone: light (harbour mist) after the 17 Nov light reel and 16 Nov clover green; not a framed print, not a ledger.
Palette: harbour mist #E4E8E9, deep harbour ink #16232B, dusk amber #D8822E (key numbers, from the berth lights), steel #6D7B83;
  seal red #AC3E33 on the seal only.
Composition: full-bleed dusk photo band (top 560 px) with the masthead on it -> headline -> two berth cards (port name tab,
  key number in amber, unit, one-line fact) split by a hairline -> tip line -> footer (sources, photo credit, signature).
Type: Space Grotesk 700 headline + numbers, Manrope text (EN/RU); Vazirmatn 800/400 (FA); Noto Kufi Arabic 700 headline +
  IBM Plex Sans Arabic text (AR), Space Grotesk for Western digits.
Imagery: photos/ningbo-zhenhai-port-dusk.jpg (Zhenhai port area of Ningbo-Zhoushan Port at dusk, 17 May 2020, Nbfreeh, CC BY-SA 4.0).
Logo: "Seal signature + echo": seal in red, ink wordmarks, footer end; 5 % ink echo cropped by the bottom corner (left in RTL).
Carousel order (random, first != EN after the 17 Nov EN reel): RU, EN, AR, FA.

FACTS (sources fetched 20 Nov 2026)
- Xinhua (zj.xinhua.org) 10 Nov 2026: as of 10 Nov, Ningbo-Zhoushan Port 2026 container throughput >40 million TEU, second
  straight year at this level, 22 days earlier than last year; >310 container routes to >700 ports in >200 countries and regions;
  Sept 2026 4.27 million TEU, a record month. Xinhua English photo story 19 Nov 2026 repeats 40M / 310 routes / 700 ports / 200+.
- Guangzhou Port Group (en.gzport.com) 18 Nov 2026: on 29 Oct Nansha Phase IV formally began foreign-trade vessel operations;
  first purpose-built fully automated terminal in the Guangdong-Hong Kong-Macao Greater Bay Area; Nansha foreign-trade container
  throughput +19 % y/y Jan-Sep; 220 container liner services, 185 on foreign-trade routes.
"""
import os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from linkwin_mark import MARK_CSS, signature, echo
DATE = "2026-11-20"; SLUG = "port-milestones"; NB = "\u00a0"
ORDER = ["ru", "en", "ar", "fa"]

T = {
"en": dict(dir="ltr", kicker="Ports & logistics · China", date="20 Nov 2026",
  h="Two Chinese ports, two new milestones",
  c1=("Ningbo-Zhoushan", "40M+", "TEU", "handled in 2026 by 10 Nov, 22 days earlier than last year; 310+ container routes"),
  c2=("Guangzhou · Nansha", "+19%", "foreign-trade boxes", "Jan–Sep; its fully automated Phase IV terminal began serving foreign-trade ships on 29 Oct"),
  m1=("4.27M TEU", "in September alone, a record month"), m2=("185 of 220", "liner services run foreign-trade routes"),
  tip="Shipping from East or South China? Ask us which port fits your cargo.",
  src="Sources: Xinhua, 10 & 19 Nov 2026; Guangzhou Port Group, 18 Nov 2026",
  photo="Photo: Zhenhai port area, Ningbo-Zhoushan Port · Nbfreeh, CC BY-SA 4.0, Wikimedia Commons"),
"ru": dict(dir="ltr", kicker="Порты и логистика · Китай", date="20.11.2026",
  h="Два порта Китая — два новых рубежа",
  c1=("Нинбо-Чжоушань", "40+" + NB + "млн", "TEU", "за 2026 год уже к 10.11 — на 22 дня раньше, чем годом ранее; более 310 контейнерных линий"),
  c2=("Гуанчжоу · Наньша", "+19" + NB + "%", "внешнеторговых контейнеров", "за январь–сентябрь; автоматизированный терминал 4-й очереди с 29.10 принимает суда внешней торговли"),
  m1=("4,27" + NB + "млн TEU", "только в сентябре — месячный рекорд"), m2=("185 из 220", "контейнерных линий — внешнеторговые"),
  tip="Груз из Восточного или Южного Китая? Подскажем, какой порт подойдёт лучше.",
  src="Источники: Синьхуа, 10.11 и 19.11.2026; Guangzhou Port Group, 18.11.2026",
  photo="Фото: портовый район Чжэньхай, порт Нинбо-Чжоушань · Nbfreeh, CC BY-SA 4.0, Wikimedia Commons"),
"fa": dict(dir="rtl", kicker="بندر و لجستیک · چین", date="۲۹ آبان ۱۴۰۵",
  h="دو بندر چین، دو رکورد تازه",
  c1=("نینگبو-جوشان", "بیش از ۴۰ میلیون", "TEU", "جابه‌جایی کانتینر در ۲۰۲۶ تا ۱۹ آبان؛ ۲۲ روز زودتر از پارسال · بیش از ۳۱۰ خط کانتینری"),
  c2=("گوانگجو · نانشا", "۱۹٪ رشد", "کانتینرهای تجارت خارجی", "در ژانویه تا سپتامبر؛ پایانهٔ تمام‌خودکار فاز ۴ از ۷ آبان کشتی‌های تجارت خارجی را می‌پذیرد"),
  m1=("۴٫۲۷ میلیون TEU", "فقط در سپتامبر؛ رکورد ماهانه"), m2=("۱۸۵ از ۲۲۰", "خط منظم کانتینری در مسیر تجارت خارجی"),
  tip="از شرق یا جنوب چین بار دارید؟ بپرسید کدام بندر برای محموله‌تان بهتر است.",
  src="منابع: شین‌هوا، ۱۹ و ۲۸ آبان ۱۴۰۵؛ گروه بندر گوانگجو، ۲۷ آبان ۱۴۰۵",
  photo="عکس: بندرگاه جن‌های، بندر نینگبو-جوشان · Nbfreeh، مجوز CC BY-SA 4.0، ویکی‌مدیا کامانز"),
"ar": dict(dir="rtl", kicker="الموانئ والخدمات اللوجستية · الصين", date="<bdi>20</bdi> نوفمبر <bdi>2026</bdi>",
  h="ميناءان في الصين وإنجازان جديدان",
  c1=("نينغبو-تشوشان", "أكثر من <bdi>40</bdi> مليون", "حاوية نمطية (TEU)", "من يناير إلى <bdi>10</bdi> نوفمبر <bdi>2026</bdi>، أبكر بـ<bdi>22</bdi> يومًا من العام الماضي؛ أكثر من <bdi>310</bdi> خطوط للحاويات"),
  c2=("قوانغتشو · نانشا", "<bdi>+19%</bdi>", "حاويات التجارة الخارجية", "من يناير إلى سبتمبر؛ ومحطة المرحلة الرابعة المؤتمتة بالكامل تستقبل سفن التجارة الخارجية منذ <bdi>29</bdi> أكتوبر"),
  m1=("<bdi>4.27</bdi> مليون TEU", "في سبتمبر وحده، وهو رقم شهري قياسي"), m2=("<bdi>185</bdi> من <bdi>220</bdi>", "خطًا منتظمًا للحاويات على مسارات التجارة الخارجية"),
  tip="تشحن من شرق الصين أو جنوبها؟ اسألنا أي ميناء يناسب شحنتك.",
  src="المصادر: شينخوا، <bdi>10</bdi> و<bdi>19</bdi> نوفمبر <bdi>2026</bdi>؛ مجموعة ميناء قوانغتشو، <bdi>18</bdi> نوفمبر <bdi>2026</bdi>",
  photo="الصورة: منطقة ميناء تشنهاي، ميناء نينغبو-تشوشان · Nbfreeh، ترخيص <bdi>CC BY-SA 4.0</bdi>، ويكيميديا كومنز"),
}
LAT_H, LAT_B = "'Space Grotesk','Manrope',sans-serif", "'Manrope',sans-serif"
FONTS = {"en": (LAT_H, LAT_B, LAT_H), "ru": (LAT_H, LAT_B, LAT_H),
         "fa": ("'Vazirmatn','Space Grotesk',sans-serif", "'Vazirmatn','Manrope',sans-serif", "'Vazirmatn','Space Grotesk',sans-serif"),
         "ar": ("'Noto Kufi Arabic','Space Grotesk',sans-serif", "'IBM Plex Sans Arabic','Manrope',sans-serif", "'Space Grotesk','Noto Kufi Arabic',sans-serif")}
TUNE = {"en": dict(h=70, hlh=1.04, num=92, lab=21), "ru": dict(h=66, hlh=1.06, num=80, lab=20),
        "fa": dict(h=62, hlh=1.5, num=56, lab=21), "ar": dict(h=56, hlh=1.55, num=56, lab=20)}

def html(lang):
    t = T[lang]; hf, bf, nf = FONTS[lang]; k = TUNE[lang]
    rtl = t["dir"] == "rtl"; start, end = ("right", "left") if rtl else ("left", "right")
    ls = "0" if rtl else ".16em"; tt = "none" if rtl else "uppercase"
    hw = "800" if lang == "fa" else "700"
    card = lambda c, m, cls: f'<div class="card {cls}"><div class="tab">{c[0]}</div><div class="num"><b>{c[1]}</b><i>{c[2]}</i></div><p>{c[3]}</p><div class="mini"><b>{m[0]}</b><span>{m[1]}</span></div></div>'
    return f"""<!doctype html><html lang="{lang}" dir="{t['dir']}"><head><meta charset="utf-8">
<link rel="stylesheet" href="../brand/fonts.css"><style>
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1080px;height:1350px;overflow:hidden;background:#E4E8E9}}
body{{position:relative;font-family:{bf};color:#16232B;-webkit-font-smoothing:antialiased;
  --lw-ink:#16232B;--lw-seal:#AC3E33;--lw-echo:#16232B;--lw-echo-op:.05;--lw-echo-size:520px}}
.photo{{position:absolute;left:0;top:0;width:1080px;height:560px;background:url(../photos/ningbo-zhenhai-port-dusk.jpg) 58% 62%/cover}}
.photo:after{{content:"";position:absolute;inset:0;background:linear-gradient(rgba(10,16,22,.55),rgba(10,16,22,0) 34%,rgba(10,16,22,0) 72%,rgba(228,232,233,.0) 88%,#E4E8E9)}}
.mast{{position:absolute;left:72px;right:72px;top:54px;display:flex;justify-content:space-between;align-items:center;padding-bottom:14px;
  border-bottom:1px solid rgba(255,255,255,.45);color:#fff;font:700 19px/1.2 {bf};letter-spacing:{ls};text-transform:{tt};z-index:2}}
.mast .d{{letter-spacing:{'0' if rtl else '.08em'};color:#F3C08A}}
.page{{position:absolute;left:72px;right:72px;top:580px;bottom:50px;display:flex;flex-direction:column;z-index:1}}
h1{{font:{hw} {k['h']}px/{k['hlh']} {hf};letter-spacing:{'0' if rtl else '-.02em'};max-width:930px;text-wrap:balance}}
.cards{{display:grid;grid-template-columns:1fr 1fr;margin-top:34px;border-top:2px solid #16232B}}
.card{{padding:22px 0 0}}
.card.b{{padding-{start}:34px;border-{start}:1px solid rgba(22,35,43,.22)}}
.card.a{{padding-{end}:34px}}
.tab{{font:700 20px/1.2 {bf};letter-spacing:{'0' if rtl else '.12em'};text-transform:{tt};color:#6D7B83}}
.num{{display:flex;align-items:baseline;gap:12px;margin-top:14px;flex-wrap:wrap}}
.num b{{font:{hw} {k['num']}px/1 {nf};color:#D8822E;white-space:nowrap;letter-spacing:{'0' if rtl else '-.02em'}}}
.num i{{font:600 22px/1.2 {bf};font-style:normal;color:#16232B}}
.card p{{margin-top:14px;font:400 {k['lab']}px/1.5 {bf};color:#2E3D46}}
.mini{{margin-top:20px;padding-top:14px;border-top:1px solid rgba(22,35,43,.16)}}
.mini b{{display:block;font:{hw} 30px/1.2 {nf};color:#16232B;white-space:nowrap}}
.mini span{{display:block;margin-top:4px;font:400 18px/1.45 {bf};color:#5A6870}}
.tip{{margin-top:auto;font:600 24px/1.4 {bf};color:#16232B;padding:18px 0;border-top:1px solid rgba(22,35,43,.22)}}
.foot{{display:flex;align-items:flex-end;justify-content:space-between;gap:28px;padding-top:16px;border-top:1px solid rgba(22,35,43,.22)}}
.ft{{font:400 14px/1.5 {bf};color:#5A6870;max-width:680px}}
.ft .url{{font:700 19px/1.4 'Manrope',sans-serif;color:#16232B;letter-spacing:.02em;margin-bottom:4px}}
__MARKCSS__
.lw-sig{{--lw-sig-h:58px}}
</style></head><body>
<div class="photo"></div>
{echo(end, '-170px', '-150px')}
<div class="mast"><span>{t['kicker']}</span><span class="d">{t['date']}</span></div>
<div class="page">
  <h1>{t['h']}</h1>
  <div class="cards">{card(t['c1'],t['m1'],'a')}{card(t['c2'],t['m2'],'b')}</div>
  <div class="tip">{t['tip']}</div>
  <div class="foot"><div class="ft"><div class="url">linkwinco.com</div>{t['src']}<br>{t['photo']}</div>{signature()}</div>
</div></body></html>""".replace('__MARKCSS__', MARK_CSS)

if __name__ == "__main__":
    langs = [a for a in sys.argv[1:]] or ORDER
    os.makedirs(os.path.join(ROOT, "posts", DATE), exist_ok=True)
    for lang in langs:
        tpl = os.path.join(ROOT, "templates", f"{DATE}-{SLUG}-{lang}.html")
        open(tpl, "w", encoding="utf-8").write(html(lang))
        n = ORDER.index(lang) + 1
        out = os.path.join(ROOT, "posts", DATE, f"{DATE}-{SLUG}-{n}-{lang}.jpg")
        subprocess.run([sys.executable, os.path.join(ROOT, "tools", "render.py"), tpl, out, "feed"], check=False)
