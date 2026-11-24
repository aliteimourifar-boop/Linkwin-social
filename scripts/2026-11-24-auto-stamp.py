"""LinkWin daily carousel, 24 Nov 2026 — China's Single Window now prints customs forms with the declaration seal.

CREATIVE BRIEF
Concept name: "Print Registration" (a press-proof page: crop marks in the corners, a registration target, one process-cyan
  ink; the old offline routine print → stamp by hand → scan is struck through and replaced by one cyan "printed, stamped"
  pill; an oversized cyan 13 and a 13-chip index of the pilot customs districts, 2 outlined (since 11 Nov), 11 filled (new)).
Background tone: light cool press white after dark graphite (23 Nov), sand (22 Nov), gunmetal (21 Nov).
Palette: paper #F7F7F4, registration black #121417, process cyan #009FD1, cyan tint #DDF0F7, grey #858B91; seal red on seal only.
Composition (new archetype): crop-mark proof page → mast → headline → struck process row → big numeral + label + legend →
  4-column chip index → cyan-ruled tip → footer (sources | url + signature).
Type: Unbounded 700 headline/numeral + Golos Text (EN/RU); Noto Kufi Arabic 700 + Vazirmatn (FA);
  Noto Naskh Arabic 700 + IBM Plex Sans Arabic (AR). No Inter/Cormorant/Playfair/Space Grotesk (used 20–23 Nov).
Imagery: none (graphic proof page; no maps, no flags).
Logo: "Seal signature" seal red + black wordmarks at the footer end; 3 % black echo cropped by the lower end corner.
Carousel order (random, first != FA of 23 Nov): EN, AR, FA, RU.

FACTS (fetched 24 Nov 2026)
- China E-Port Data Center notice, 11 Nov 2026 (via singlewindow.hn.cn / Anhui Single Window): from 20:00 on 11 Nov the
  Single Window cargo-declaration app adds a "affix customs declaration seal" option to one-click printing; applies to the
  declaration check sheet, inspection/release notice, import goods permitted-removal notice, paperless-clearance release
  notice and agency declaration agreement; pilot first in Qingdao and Hangzhou customs districts.
- China E-Port Data Center notice, 23 Nov 2026 (via The Paper / Fujian Single Window): from 20:00 on 23 Nov the pilot adds
  Beijing, Tianjin, Dalian, Shanghai, Nanjing, Ningbo, Xiamen, Jinan, Guangzhou, Shenzhen, Huangpu customs districts.
- Operation guide (Hebei E-Port PDF): seal is created with the legal-representative card (user management → seal
  management), bound to an operator card; replaces offline print → manual stamp → scan; stamps only documents where the
  logged-in company is the declaring unit.
"""
import os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from linkwin_mark import MARK_CSS, signature, echo
DATE = "2026-11-24"; SLUG = "auto-stamp"
ORDER = ["en", "ar", "fa", "ru"]
NB = "\u00a0"

OLD = ["qd", "hz"]
T = {
"en": dict(cov="Covers: declaration check sheet, inspection/release notice, permitted‑removal notice, paperless release notice, agency agreement.", dir="ltr", kicker="Customs · China Single Window", date="24 Nov 2026",
  h="Customs printouts now come pre‑stamped",
  proc=["Print", "Stamp by hand", "Scan"], new="Print, stamped",
  num="13", numl="customs districts in the pilot", leg=("Since 11 Nov", "New from 23 Nov"),
  d=dict(qd="Qingdao", hz="Hangzhou", bj="Beijing", tj="Tianjin", dl="Dalian", sh="Shanghai", nj="Nanjing", nb="Ningbo",
         xm="Xiamen", jn="Jinan", gz="Guangzhou", sz="Shenzhen", hp="Huangpu"),
  tip="Set the seal up once with the legal‑rep card. It stamps only forms your company declared.",
  src="Source: China E‑Port Data Center notices, 11 &amp; 23 Nov 2026"),
"ru": dict(cov="Охватывает: контрольный лист декларации, уведомления о досмотре/выпуске и о разрешении вывоза, уведомление о безбумажном выпуске, договор с таможенным представителем.", dir="ltr", kicker="Таможня · «Единое окно» Китая", date="24.11.2026",
  h="Таможенные бланки теперь выходят уже с&nbsp;печатью",
  proc=["Распечатать", "Штамп вручную", "Скан"], new="Сразу с печатью",
  num="13", numl="таможенных округов в пилоте", leg=("С 11 ноября", "Новые с 23 ноября"),
  d=dict(qd="Циндао", hz="Ханчжоу", bj="Пекин", tj="Тяньцзинь", dl="Далянь", sh="Шанхай", nj="Нанкин", nb="Нинбо",
         xm="Сямэнь", jn="Цзинань", gz="Гуанчжоу", sz="Шэньчжэнь", hp="Хуанпу"),
  tip="Печать один раз настраивается картой законного представителя. Ставится только на документы, поданные вашей компанией.",
  src="Источник: уведомления China E‑Port Data Center, 11.11 и 23.11.2026"),
"fa": dict(cov="شامل: برگه کنترل اظهارنامه، اعلامیه بازرسی/ترخیص، مجوز خروج کالای وارداتی، اعلامیه ترخیص بدون کاغذ و قرارداد وکالت ترخیص.", dir="rtl", kicker="گمرک · پنجره واحد تجارت چین", date="۳ آذر ۱۴۰۵",
  h="برگه‌های گمرکی حالا مُهرخورده چاپ می‌شوند",
  proc=["چاپ", "مُهر دستی", "اسکن"], new="چاپ با مُهر",
  num="۱۳", numl="حوزه گمرکی در طرح آزمایشی", leg=("از ۲۰ آبان", "جدید از ۲ آذر"),
  d=dict(qd="چینگدائو", hz="هانگژو", bj="پکن", tj="تیانجین", dl="دالیان", sh="شانگهای", nj="نانجینگ", nb="نینگبو",
         xm="شیامن", jn="جینان", gz="گوانگژو", sz="شنژن", hp="هوانگپو"),
  tip="مُهر را یک‌بار با کارت نماینده قانونی تعریف کنید؛ فقط روی اسنادی می‌نشیند که شرکت خودتان اظهار کرده است.",
  src="منبع: اطلاعیه‌های مرکز داده بندر الکترونیک چین، ۲۰ آبان و ۲ آذر ۱۴۰۵"),
"ar": dict(cov="يشمل: ورقة مطابقة البيان، وإشعار المعاينة/الإفراج، وإذن سحب البضائع المستوردة، وإشعار الإفراج الإلكتروني، واتفاقية التخليص بالوكالة.", dir="rtl", kicker="الجمارك · النافذة الواحدة في الصين", date="<bdi>24</bdi> نوفمبر <bdi>2026</bdi>",
  h="الاستمارات الجمركية تُطبع الآن مختومة تلقائياً",
  proc=["طباعة", "ختم يدوي", "مسح ضوئي"], new="طباعة مع الختم",
  num="13", numl="منطقة جمركية ضمن التجربة", leg=("منذ <bdi>11</bdi> نوفمبر", "جديدة منذ <bdi>23</bdi> نوفمبر"),
  d=dict(qd="تشينغداو", hz="هانغتشو", bj="بكين", tj="تيانجين", dl="داليان", sh="شانغهاي", nj="نانجينغ", nb="نينغبو",
         xm="شيامن", jn="جينان", gz="قوانغتشو", sz="شنتشن", hp="هوانغبو"),
  tip="يُعدّ الختم مرة واحدة ببطاقة الممثل القانوني، ولا يُطبع إلا على المستندات التي صرّحت بها شركتك.",
  src="المصدر: إشعارات مركز بيانات الميناء الإلكتروني الصيني، <bdi>11</bdi> و<bdi>23</bdi> نوفمبر <bdi>2026</bdi>"),
}
KEYS = ["qd", "hz", "bj", "tj", "dl", "sh", "nj", "nb", "xm", "jn", "gz", "sz", "hp"]

REG = '<svg viewBox="0 0 60 60" class="reg"><circle cx="30" cy="30" r="15" fill="none" stroke="currentColor" stroke-width="1.6"/><circle cx="30" cy="30" r="7" fill="currentColor"/><path d="M30 2V58M2 30H58" stroke="currentColor" stroke-width="1.6"/></svg>'
CHECK = '<svg viewBox="0 0 24 24" class="ck"><path d="M4 12.5l5 5L20 6.5" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def html(lang):
    t = T[lang]; rtl = t["dir"] == "rtl"
    if lang == "fa": hf, bf, hw, nf = "'Noto Kufi Arabic','Unbounded',sans-serif", "'Vazirmatn','Golos Text',sans-serif", 700, "'Vazirmatn',sans-serif"
    elif lang == "ar": hf, bf, hw, nf = "'Noto Naskh Arabic','Unbounded',serif", "'IBM Plex Sans Arabic','Golos Text',sans-serif", 700, "'Unbounded',sans-serif"
    else: hf, bf, hw, nf = "'Unbounded',sans-serif", "'Golos Text',sans-serif", 700, "'Unbounded',sans-serif"
    hsize = {"en": 60, "ru": 52, "fa": 56, "ar": 64}[lang]
    hlh = {"en": 1.12, "ru": 1.14, "fa": 1.6, "ar": 1.5}[lang]
    ls = "0" if rtl else ".14em"
    arrow_rot = "180deg" if rtl else "0deg"
    chips = "".join(f'<div class="chip {"old" if k in OLD else "nw"}">{t["d"][k]}</div>' for k in KEYS)
    proc = "".join(f'<span class="p">{p}</span>' for p in t["proc"])
    return f"""<!doctype html><html lang="{lang}" dir="{t['dir']}"><head><meta charset="utf-8">
<link rel="stylesheet" href="../brand/fonts.css"><style>
:root{{--pa:#F7F7F4;--ink:#121417;--cy:#009FD1;--ct:#DDF0F7;--gr:#858B91;--lw-ink:#121417;--lw-seal:#AC3E33}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1350px;overflow:hidden;background:var(--pa);color:var(--ink);font-family:{bf}}}
body{{position:relative}}
bdi{{direction:ltr;unicode-bidi:isolate}}
.crop{{position:absolute;width:44px;height:44px;border-color:rgba(18,20,23,.55);border-style:solid;border-width:0}}
.c1{{left:22px;top:22px;border-right-width:1px;border-bottom-width:1px}}
.c2{{right:22px;top:22px;border-left-width:1px;border-bottom-width:1px}}
.c3{{left:22px;bottom:22px;border-right-width:1px;border-top-width:1px}}
.c4{{right:22px;bottom:22px;border-left-width:1px;border-top-width:1px}}
.reg{{position:absolute;width:34px;height:34px;top:28px;left:523px;color:rgba(18,20,23,.6)}}
.bars{{position:absolute;bottom:30px;left:50%;transform:translateX(-50%);display:flex;gap:0}}
.bars i{{width:26px;height:10px;display:block}}
.main{{position:absolute;left:84px;right:84px;top:92px;bottom:84px;display:flex;flex-direction:column}}
.mast{{display:flex;justify-content:space-between;align-items:center;font:600 18px/1 {bf};letter-spacing:{ls};text-transform:uppercase;color:var(--ink);padding-bottom:18px;border-bottom:1.5px solid var(--ink)}}
.mast .k{{display:flex;align-items:center;gap:12px}}
.mast .k:before{{content:"";width:14px;height:14px;background:var(--cy)}}
h1{{margin-top:{38 if rtl else 44}px;font:{hw} {hsize}px/{hlh} {hf};letter-spacing:{'0' if rtl else '-.02em'};text-wrap:balance}}
.proc{{margin-top:{30 if rtl else 38}px;display:flex;align-items:center;gap:12px;flex-wrap:nowrap}}
.proc .p{{font:500 21px/1 {bf};color:var(--gr);padding:12px 16px;border:1.5px solid rgba(133,139,145,.5);border-radius:40px;text-decoration:line-through;text-decoration-thickness:2px;text-decoration-color:rgba(18,20,23,.55);white-space:nowrap}}
.proc .ar{{width:46px;height:16px;color:var(--ink);flex:none;transform:rotate({arrow_rot})}}
.proc .n{{display:flex;align-items:center;gap:10px;font:600 22px/1 {bf};color:#fff;background:var(--cy);padding:12px 20px 12px 16px;border-radius:40px;white-space:nowrap}}
[dir=rtl] .proc .n{{padding:12px 16px 12px 20px}}
.ck{{width:22px;height:22px}}
.mid{{margin-top:{34 if rtl else 44}px;display:flex;align-items:flex-end;gap:34px}}
.num{{font:700 {230 if lang!='fa' else 250}px/.78 {nf};color:var(--cy);letter-spacing:-.04em}}
[dir=rtl] .num{{letter-spacing:0}}
.ml{{padding-bottom:6px}}
.ml .l{{font:600 {'32px/1.45' if rtl else '32px/1.15'} {bf};max-width:520px;text-wrap:balance}}
.leg{{margin-top:18px;display:flex;gap:22px;font:500 18px/1.3 {bf};color:#3A3F45}}
.leg span{{display:flex;align-items:center;gap:9px}}
.leg span:before{{content:"";width:16px;height:16px;border-radius:50%;flex:none}}
.leg .o:before{{border:2px solid var(--cy)}} .leg .f:before{{background:var(--cy)}}
.grid{{margin-top:40px;display:grid;grid-template-columns:repeat(4,1fr);gap:12px}}
.chip{{font:600 {'21px/1.5' if rtl else '21px/1.2'} {bf};padding:{'11px 16px' if rtl else '15px 16px'};border-radius:12px;white-space:nowrap}}
.chip.old{{border:2px solid var(--cy);color:#006E91;padding:{'9px 14px' if rtl else '13px 14px'}}}
.chip.nw{{background:var(--ct);color:var(--ink)}}
.cov{{margin-top:22px;font:400 {'19px/1.6' if rtl else '19px/1.42'} {bf};color:#4A5056;max-width:900px}}
.tip{{margin-top:34px;padding-{'right' if rtl else 'left'}:22px;border-{'right' if rtl else 'left'}:4px solid var(--cy);font:500 {'23px/1.65' if rtl else '23px/1.42'} {bf};max-width:880px}}
.foot{{margin-top:auto;display:flex;align-items:flex-end;justify-content:space-between;gap:30px;padding-top:20px;border-top:1px solid rgba(18,20,23,.2)}}
.foot .src{{font:{'400 15px/1.6' if rtl else '400 15px/1.45'} {bf};color:#5D6369;max-width:480px}}
.foot .end{{display:flex;align-items:center;gap:24px}}
.foot .url{{font:500 20px/1 'Unbounded',sans-serif;letter-spacing:.01em}}
.lw-sig{{--lw-sig-h:56px}}
.lw-echo{{--lw-echo:#121417;--lw-echo-op:.03;--lw-echo-size:460px}}
__MARKCSS__
</style></head><body>
{echo('left' if rtl else 'right', '330px', '-170px')}
<i class="crop c1"></i><i class="crop c2"></i><i class="crop c3"></i><i class="crop c4"></i>{REG}
<div class="bars"><i style="background:#009FD1"></i><i style="background:#5FC3E4"></i><i style="background:#B4E2F1"></i><i style="background:#121417"></i><i style="background:#858B91"></i><i style="background:#C9CCCF"></i></div>
<div class="main">
  <div class="mast"><span class="k">{t['kicker']}</span><span>{t['date']}</span></div>
  <h1>{t['h']}</h1>
  <div class="proc">{proc}<svg viewBox="0 0 46 16" class="ar"><path d="M1 8H42M34 1L43 8L34 15" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="n">{CHECK}{t['new']}</span></div>
  <div class="mid"><div class="num">{t['num']}</div><div class="ml"><div class="l">{t['numl']}</div><div class="leg"><span class="o">{t['leg'][0]}</span><span class="f">{t['leg'][1]}</span></div></div></div>
  <div class="grid">{chips}</div>
  <div class="cov">{t['cov']}</div>
  <div class="tip">{t['tip']}</div>
  <div class="foot"><div class="src">{t['src']}</div><div class="end"><span class="url">linkwinco.com</span>{signature()}</div></div>
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
