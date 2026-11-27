"""LinkWin daily carousel, 27 Nov 2026 — China–Iran trade: what actually moves (one-off override, OVERRIDES.md 2026-11-27).

CREATIVE BRIEF
Concept name: "Turquoise Caravan Ledger" — a deep Persian-turquoise trade ledger: rail-freight photo band with the masthead,
  a big key number, a two-tone split bar (saffron = China → Iran, aqua = Iran → China), two ledger columns with dotted
  leaders, and an abstract six-stop rail line (no borders, no map) for the Central Asia route.
Background tone: dark-mid turquoise after press white (24 Nov), graphite (23 Nov), sand (22 Nov).
Palette: turquoise #0C3940, panel #114750, cream #F4ECDD, saffron #E9A93A, aqua #7FD3C9, muted #9DB8B6; seal tone-on-tone cream.
Type: Oswald 600 headline/numerals + IBM Plex Sans (EN/RU); Lalezar headline/numerals + Vazirmatn (FA);
  Noto Kufi Arabic 700 + IBM Plex Sans Arabic (AR).
Imagery: photos/zhengzhou-container-terminal-df8b.jpg (Windmemories, CC BY-SA 4.0, Wikimedia Commons).
Logo: "Seal signature" cream tone-on-tone in the footer end + 4 % cream echo cropped by the route panel edge.
Carousel order (random, first != EN of 24 Nov): RU, AR, FA, EN.
PRC compliance: commercial and neutral only; official GACC figures; no y/y change (avoids any geopolitical reading), no flags,
  no map with borders, no politics/sanctions/leaders/religion.

FACTS (fetched 27 Nov 2026)
- GACC table "(2) Imports and Exports by Country (Region) of Origin/Destination, 9.2026", published 27 Oct 2026
  (english.customs.gov.cn): Iran Jan–Sep total US$3,327,000k, China exports US$2,537,956k, imports US$789,045k
  -> 3.33 bn; 2.54 bn (76.3 %); 0.79 bn (23.7 %).
- ChinaData (chinadata.live/china-trade/iran, GACC data, Jan–Oct 2026): China -> Iran HS84 machinery $534M, HS87 vehicles &
  parts $434M, HS85 electrical $429M; Iran -> China HS3901 polymers of ethylene $287M, HS2601 iron ores $227M,
  HS0303 frozen whole fish $63.9M, HS0910 ginger/saffron/turmeric/spices $22.6M, HS08 fruit & nuts $61.1M.
- Asia-Plus 11 Sep 2026 (citing Uztemirjulcontainer via Interfax Kazakhstan): first China–Iran block train via Central Asia,
  55 containers (auto parts, consumer goods), Khorgos–Altynkol – Kazakhstan – Uzbekistan – Turkmenistan – Sarakhs – Tehran,
  more than 6,000 km, approx. 14–16 days.
"""
import os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from linkwin_mark import MARK_CSS, signature, echo
DATE, SLUG = "2026-11-27", "china-iran-trade"
ORDER = ["ru", "ar", "fa", "en"]
PHOTO = "../photos/zhengzhou-container-terminal-df8b.jpg"
NB = "\u00a0"

T = {
"en": dict(kicker="China ⇄ Iran · Trade map", date="27 Nov 2026",
  h="China–Iran trade: what actually moves",
  num="US$3.33 bn", numl="goods trade, Jan–Sep 2026", numsub="China Customs (GACC)",
  a=("China → Iran", "US$2.54 bn", "76%"), b=("Iran → China", "US$0.79 bn", "24%"),
  ca="China → Iran", cb="Iran → China",
  la=[("Machinery", "$534M"), ("Vehicles & parts", "$434M"), ("Electrical equipment", "$429M")],
  lb=[("Polyethylene", "$287M"), ("Iron ore", "$227M"), ("Frozen fish", "$64M")],
  note="Top goods, Jan–Oct 2026",
  rt="Rail via Central Asia", stops=["Khorgos", "Kazakhstan", "Uzbekistan", "Turkmenistan", "Sarakhs", "Tehran"],
  rf="6,000+ km · about 14–16 days scheduled · first block train via this route, Sep 2026",
  tip="Scheduled is not actual: confirm transit time and border handling with your forwarder before you quote.",
  src="Sources: GACC country table, 27 Oct 2026; GACC data via ChinaData (Jan–Oct); Uztemirjulcontainer via Asia-Plus, 11 Sep 2026. Photo: Windmemories, CC BY-SA 4.0"),
"ru": dict(kicker="Китай ⇄ Иран · карта торговли", date="27.11.2026",
  h="Торговля Китая и Ирана: что везут на самом деле",
  num=f"3,33{NB}млрд{NB}$", numl="товарооборот, январь–сентябрь 2026", numsub="Таможня КНР (GACC)",
  a=("Китай → Иран", f"2,54{NB}млрд{NB}$", f"76{NB}%"), b=("Иран → Китай", f"0,79{NB}млрд{NB}$", f"24{NB}%"),
  ca="Китай → Иран", cb="Иран → Китай",
  la=[("Машины и оборудование", f"534{NB}млн{NB}$"), ("Авто и запчасти", f"434{NB}млн{NB}$"), ("Электрооборудование", f"429{NB}млн{NB}$")],
  lb=[("Полиэтилен", f"287{NB}млн{NB}$"), ("Железная руда", f"227{NB}млн{NB}$"), ("Мороженая рыба", f"64{NB}млн{NB}$")],
  note="Главные товары, январь–октябрь 2026",
  rt="Ж/д через Центральную Азию", stops=["Хоргос", "Казахстан", "Узбекистан", "Туркмения", "Серахс", "Тегеран"],
  rf=f"более 6000{NB}км · около 14–16 дней по графику · первый контейнерный поезд по маршруту, сентябрь 2026",
  tip="График ≠ факт: перед расчётом цены уточните у экспедитора время в пути и прохождение границ.",
  src="Источники: таблица GACC, 27.10.2026; данные GACC через ChinaData (янв.–окт.); Uztemirjulcontainer через Asia-Plus, 11.09.2026. Фото: Windmemories, CC BY-SA 4.0"),
"fa": dict(kicker="چین ⇄ ایران · نقشه تجارت", date="۶ آذر ۱۴۰۵",
  h="تجارت چین و ایران: واقعاً چه کالاهایی جابه‌جا می‌شود؟",
  num="۳٫۳۳ میلیارد دلار", numl="تجارت کالایی، ژانویه تا سپتامبر ۲۰۲۶", numsub='گمرک چین (<bdi dir=ltr>GACC</bdi>)',
  a=("از چین به ایران", "۲٫۵۴ میلیارد دلار", "٪۷۶"), b=("از ایران به چین", "۰٫۷۹ میلیارد دلار", "٪۲۴"),
  ca="از چین به ایران", cb="از ایران به چین",
  la=[("ماشین‌آلات", "۵۳۴ میلیون دلار"), ("خودرو و قطعات", "۴۳۴ میلیون دلار"), ("تجهیزات برقی", "۴۲۹ میلیون دلار")],
  lb=[("پلی‌اتیلن", "۲۸۷ میلیون دلار"), ("سنگ آهن", "۲۲۷ میلیون دلار"), ("ماهی منجمد", "۶۴ میلیون دلار")],
  note="کالاهای اصلی، ژانویه تا اکتبر ۲۰۲۶",
  rt="ریل از مسیر آسیای مرکزی", stops=["خورگوس", "قزاقستان", "ازبکستان", "ترکمنستان", "سرخس", "تهران"],
  rf="بیش از ۶٬۰۰۰ کیلومتر · حدود ۱۴ تا ۱۶ روز طبق برنامه · نخستین قطار بلوکی این مسیر، سپتامبر ۲۰۲۶",
  tip="زمان برنامه با زمان واقعی یکی نیست؛ پیش از قیمت‌دهی، زمان حمل و تشریفات مرزی را با فورواردر خود تأیید کنید.",
  src='منابع: جدول کشوری گمرک چین، ۲۷ اکتبر ۲۰۲۶؛ داده‌های <bdi dir=ltr>GACC</bdi> از طریق <bdi dir=ltr>ChinaData</bdi> (ژانویه تا اکتبر)؛ <bdi dir=ltr>Uztemirjulcontainer</bdi> به نقل از <bdi dir=ltr>Asia-Plus</bdi>، ۱۱ سپتامبر ۲۰۲۶. عکس: <bdi dir=ltr>Windmemories, CC BY-SA 4.0</bdi>'),
"ar": dict(kicker="الصين ⇄ إيران · خريطة التجارة", date="<bdi dir=ltr>27</bdi> نوفمبر <bdi dir=ltr>2026</bdi>",
  h="التجارة بين الصين وإيران: ما الذي يُشحن فعلاً؟",
  num="<bdi dir=ltr>3.33</bdi> مليار دولار", numl="تجارة السلع، يناير–سبتمبر <bdi dir=ltr>2026</bdi>", numsub="الجمارك الصينية (<bdi dir=ltr>GACC</bdi>)",
  a=("من الصين إلى إيران", "<bdi dir=ltr>2.54</bdi> مليار دولار", "<bdi dir=ltr>76%</bdi>"), b=("من إيران إلى الصين", "<bdi dir=ltr>0.79</bdi> مليار دولار", "<bdi dir=ltr>24%</bdi>"),
  ca="من الصين إلى إيران", cb="من إيران إلى الصين",
  la=[("الآلات", "<bdi dir=ltr>534</bdi> مليون دولار"), ("المركبات وقطع الغيار", "<bdi dir=ltr>434</bdi> مليون دولار"), ("المعدات الكهربائية", "<bdi dir=ltr>429</bdi> مليون دولار")],
  lb=[("البولي إيثيلين", "<bdi dir=ltr>287</bdi> مليون دولار"), ("خام الحديد", "<bdi dir=ltr>227</bdi> مليون دولار"), ("الأسماك المجمدة", "<bdi dir=ltr>64</bdi> مليون دولار")],
  note="أهم السلع، يناير–أكتوبر <bdi dir=ltr>2026</bdi>",
  rt="سكك حديدية عبر آسيا الوسطى", stops=["خورغوس", "كازاخستان", "أوزبكستان", "تركمانستان", "سرخس", "طهران"],
  rf="أكثر من <bdi dir=ltr>6,000</bdi> كم · نحو <bdi dir=ltr>14–16</bdi> يوماً وفق الجدول · أول قطار حاويات على هذا المسار، سبتمبر <bdi dir=ltr>2026</bdi>",
  tip="الموعد المجدول ليس الموعد الفعلي: تحقّق من مدة العبور وإجراءات الحدود مع وكيل الشحن قبل تقديم السعر.",
  src="المصادر: جدول الجمارك الصينية حسب الدول، <bdi dir=ltr>27</bdi> أكتوبر <bdi dir=ltr>2026</bdi>؛ بيانات <bdi dir=ltr>GACC</bdi> عبر <bdi dir=ltr>ChinaData</bdi> (يناير–أكتوبر)؛ <bdi dir=ltr>Uztemirjulcontainer</bdi> عبر <bdi dir=ltr>Asia-Plus</bdi>، <bdi dir=ltr>11</bdi> سبتمبر <bdi dir=ltr>2026</bdi>. الصورة: <bdi dir=ltr>Windmemories، CC BY-SA 4.0</bdi>"),
}

def html(lang):
    t = T[lang]; rtl = lang in ("fa", "ar")
    if lang == "fa":
        hf, bf, nf, hw, hs, hlh = "'Lalezar','Oswald',sans-serif", "'Vazirmatn','IBM Plex Sans',sans-serif", "'Vazirmatn','Oswald',sans-serif", 400, 60, 1.3
    elif lang == "ar":
        hf, bf, nf, hw, hs, hlh = "'Noto Kufi Arabic','Oswald',sans-serif", "'IBM Plex Sans Arabic','IBM Plex Sans',sans-serif", "'Noto Kufi Arabic','Oswald',sans-serif", 700, 50, 1.45
    else:
        hf, bf, nf, hw, hs, hlh = "'Oswald',sans-serif", "'IBM Plex Sans',sans-serif", "'Oswald',sans-serif", 600, 64 if lang == "en" else 58, 1.08
    blh = 1.62 if rtl else 1.38
    def rows(items):
        return "".join(f'<div class="r"><span class="n">{n}</span><i></i><span class="v">{v}</span></div>' for n, v in items)
    stops = "".join(f'<div class="st{" end" if i in (0, 5) else ""}"><b></b><span>{s}</span></div>' for i, s in enumerate(t["stops"]))
    upper = "" if rtl else "text-transform:uppercase;letter-spacing:.12em;"
    return f"""<!doctype html><html lang="{lang}" dir="{'rtl' if rtl else 'ltr'}"><head><meta charset="utf-8">
<link rel="stylesheet" href="../brand/fonts.css"><style>
:root{{--bg:#0C3940;--pn:#114750;--cr:#F4ECDD;--sf:#E9A93A;--aq:#7FD3C9;--mu:#9DB8B6}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1080px;height:1350px;overflow:hidden}}
body{{background:var(--bg);color:var(--cr);font-family:{bf};position:relative}}
.ph{{position:absolute;left:0;top:0;width:1080px;height:360px;background:url('{PHOTO}') center 58%/cover;filter:saturate(.85) contrast(1.05)}}
.ph:after{{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(12,57,64,.55) 0%,rgba(12,57,64,.12) 40%,rgba(12,57,64,.35) 72%,#0C3940 100%)}}
.main{{position:absolute;left:72px;right:72px;top:56px;bottom:56px;display:flex;flex-direction:column}}
.mast{{display:flex;justify-content:space-between;align-items:center;font:600 {'19px' if rtl else '17px'}/1.2 {bf};{upper}color:var(--cr);text-shadow:0 1px 10px rgba(0,0,0,.45)}}
.mast .k{{display:flex;align-items:center;gap:12px}}
.mast .k:before{{content:"";width:28px;height:4px;background:linear-gradient(90deg,var(--sf) 50%,var(--aq) 50%)}}
h1{{margin-top:{232 if rtl else 246}px;font:{hw} {hs}px/{hlh} {hf};letter-spacing:{'0' if rtl else '-.005em'};text-wrap:balance;max-width:900px}}
.key{{margin-top:{20 if rtl else 26}px;display:flex;align-items:flex-end;gap:28px}}
.num{{font:{'900' if lang=='fa' else '700' if lang=='ar' else '600'} {80 if lang=='fa' else 64 if lang=='ar' else 92}px/1 {nf};color:var(--sf);white-space:nowrap}}
.kl{{padding-bottom:8px;font:500 {'21px/1.5' if rtl else '21px/1.3'} {bf}}}
.kl small{{display:block;font-size:16px;color:var(--mu);margin-top:2px}}
.bar{{margin-top:20px;display:flex;height:14px;border-radius:7px;overflow:hidden}}
.bar .a{{width:76.3%;background:var(--sf)}} .bar .b{{flex:1;background:var(--aq)}}
.bl{{margin-top:12px;display:flex;justify-content:space-between;font:500 {'19px/1.5' if rtl else '19px/1.3'} {bf}}}
.bl .a b{{color:var(--sf)}} .bl .b b{{color:var(--aq)}} .bl b{{font-weight:600}}
.cols{{margin-top:{34 if rtl else 40}px;display:grid;grid-template-columns:1fr 1fr;gap:40px}}
.col h3{{font:600 {'20px/1.5' if rtl else '18px/1.2'} {bf};{upper}padding-bottom:10px;border-bottom:2px solid currentColor;margin-bottom:6px}}
.col.a h3{{color:var(--sf)}} .col.b h3{{color:var(--aq)}}
.r{{display:flex;align-items:baseline;gap:10px;padding:{'7px 0' if rtl else '10px 0'};font:400 {'20px/1.55' if rtl else '20px/1.3'} {bf}}}
.r i{{flex:1;border-bottom:1.5px dotted rgba(244,236,221,.32);transform:translateY(-5px);min-width:14px}}
.r .v{{font-weight:600;white-space:nowrap}}
.src bdi{{white-space:nowrap}}
.note{{margin-top:8px;font:400 15px/1.4 {bf};color:var(--mu)}}
.route{{margin-top:{34 if rtl else 40}px;position:relative;overflow:hidden;background:var(--pn);border-radius:18px;padding:{'18px 30px 18px' if rtl else '22px 30px 20px'}}}
.route h4{{font:600 {'20px/1.5' if rtl else '18px/1.2'} {bf};{upper}color:var(--aq);position:relative;z-index:1}}
.line{{position:relative;margin:{'16px 6px 0' if rtl else '20px 6px 0'};display:flex;justify-content:space-between;z-index:1}}
.line:before{{content:"";position:absolute;left:8px;right:8px;top:8px;border-top:2.5px dashed rgba(127,211,201,.75)}}
.st{{position:relative;display:flex;flex-direction:column;align-items:center;gap:8px;width:120px}}
.st b{{width:18px;height:18px;border-radius:50%;background:var(--pn);border:3px solid var(--aq)}}
.st.end b{{background:var(--sf);border-color:var(--sf)}}
.st span{{font:500 {'16px/1.5' if rtl else '16px/1.2'} {bf};white-space:nowrap}}
.rf{{margin-top:{10 if rtl else 14}px;font:400 {'17px/1.6' if rtl else '17px/1.4'} {bf};color:var(--cr);position:relative;z-index:1}}
.tip{{margin-top:{28 if rtl else 34}px;padding-{'right' if rtl else 'left'}:20px;border-{'right' if rtl else 'left'}:4px solid var(--sf);font:500 {'20px/1.6' if rtl else '20px/1.4'} {bf}}}
.foot{{margin-top:auto;display:flex;align-items:flex-end;justify-content:space-between;gap:28px;padding-top:16px;border-top:1px solid rgba(244,236,221,.2)}}
.foot .src{{font:400 {'13.5px/1.6' if rtl else '13.5px/1.45'} {bf};color:var(--mu);max-width:560px}}
.foot .end{{display:flex;align-items:center;gap:22px}}
.foot .url{{font:600 22px/1 'Oswald',sans-serif;letter-spacing:.04em}}
.lw-sig{{--lw-sig-h:52px;--lw-ink:#F4ECDD;--lw-seal:#F4ECDD}}
.lw-echo{{--lw-echo:#F4ECDD;--lw-echo-op:.045;--lw-echo-size:360px}}
__MARKCSS__
</style></head><body><div class="ph"></div>
<div class="main">
 <div class="mast"><span class="k">{t['kicker']}</span><span>{t['date']}</span></div>
 <h1>{t['h']}</h1>
 <div class="key"><div class="num">{t['num']}</div><div class="kl">{t['numl']}<small>{t['numsub']}</small></div></div>
 <div class="bar"><i class="a"></i><i class="b"></i></div>
 <div class="bl"><span class="a">{t['a'][0]} · <b>{t['a'][1]}</b> · {t['a'][2]}</span><span class="b">{t['b'][0]} · <b>{t['b'][1]}</b> · {t['b'][2]}</span></div>
 <div class="cols"><div class="col a"><h3>{t['ca']}</h3>{rows(t['la'])}</div><div class="col b"><h3>{t['cb']}</h3>{rows(t['lb'])}</div></div>
 <div class="note">{t['note']}</div>
 <div class="route">{echo('left' if rtl else 'right', '-170px', '-110px')}<h4>{t['rt']}</h4><div class="line">{stops}</div><div class="rf">{t['rf']}</div></div>
 <div class="tip">{t['tip']}</div>
 <div class="foot"><div class="src">{t['src']}</div><div class="end"><span class="url">linkwinco.com</span>{signature()}</div></div>
</div></body></html>""".replace('__MARKCSS__', MARK_CSS)

if __name__ == "__main__":
    langs = sys.argv[1:] or ORDER
    for lang in langs:
        tpl = os.path.join(ROOT, "templates", f"{DATE}-{SLUG}-{lang}.html")
        open(tpl, "w", encoding="utf-8").write(html(lang))
        n = ORDER.index(lang) + 1
        out = os.path.join(ROOT, "posts", DATE, f"{DATE}-{SLUG}-{n}-{lang}.jpg")
        subprocess.run([sys.executable, os.path.join(ROOT, "tools", "render.py"), tpl, out, "feed"], check=False)
