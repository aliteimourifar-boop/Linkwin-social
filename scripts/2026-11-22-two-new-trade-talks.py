"""LinkWin daily carousel, 22 Nov 2026 — China opens two new trade-deal talks in one day (Singapore FTA 4.0, Indonesia CEPA).

CREATIVE BRIEF
Concept name: "Crane Column" (a tall vertical strip of Singapore's green container cranes runs the full height of the
  slide like a bookmark; beside it an editorial column with a serif headline and two "agreement plates", each carried
  by one large typographic token: 4.0 and CEPA).
Idea: calm, confident trade intelligence: two new negotiating tracks opened on 20 Nov; what each covers; what to use today.
Background tone: light (porcelain sand) after the 21 Nov mid gunmetal carousel and the ivory reel.
Palette: porcelain sand #F2ECE2, crane green #1F4D3A, signal coral #C8553A (tokens only), slate #55606A, seal red on seal.
Composition (new archetype): vertical split, photo column 380 px full height (start side), text column with masthead,
  headline, two plates separated by hairlines, tip line, footer with the seal signature. RTL mirrors: photo on the right.
Type: Cormorant Garamond 700 headline + tokens, Manrope text (EN/RU); Noto Kufi Arabic 700 headline + Vazirmatn text (FA);
  Noto Kufi Arabic 700 + IBM Plex Sans Arabic (AR). Tokens stay in Cormorant (Latin).
Imagery: photos/singapore-pasir-panjang-cranes.jpg (Jacklee, CC BY-SA 3.0, Wikimedia Commons). No flags, no maps.
Logo: "Seal signature + echo": seal red + green wordmarks at the foot of the text column (end of footer), 4 % green echo
  cropped behind the plates on the end edge.
Carousel order (random, first != EN of 21 Nov): RU, AR, FA, EN.

FACTS (fetched 22 Nov 2026)
- MOFCOM, 20 Nov 2026 16:17: China and Singapore signed an MoU on launching negotiations to upgrade the China-Singapore
  FTA to version 4.0; built on China-ASEAN FTA, RCEP, the China-Singapore FTA and its upgrade protocol; new areas of
  common interest such as government procurement and digital trade rules. FTA signed Oct 2008, upgraded Nov 2018 and Dec 2023.
- MOFCOM, 20 Nov 2026 16:16: China and Indonesia signed an MoU on launching negotiations on a China-Indonesia
  Comprehensive Economic Partnership Agreement (CEPA), on the basis of the China-ASEAN FTA and RCEP, aiming for wider
  coverage, a higher level and mutual benefit.
- Media Indonesia (Antara), 12 Nov 2026: Indonesia targets completing the CEPA talks in early 2029.
- Xinhua, 21 Nov 2026: China ready to accelerate the FTA 4.0 talks (context only).
"""
import os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from linkwin_mark import MARK_CSS, signature, echo
DATE = "2026-11-22"; SLUG = "two-new-trade-talks"; NB = "\u00a0"
ORDER = ["ru", "ar", "fa", "en"]

T = {
"en": dict(dir="ltr", kicker="Trade agreements · Asia", date="22 Nov 2026",
  h="China opens two new trade-deal talks in one day",
  a=("Singapore", "4.0", "FTA upgrade talks", "New ground: government procurement and digital trade rules. The FTA dates from 2008, upgraded in 2018 and 2023."),
  b=("Indonesia", "CEPA", "First bilateral partnership deal", "Built on the China–ASEAN FTA and RCEP, aiming wider and deeper. Jakarta targets early 2029."),
  tip="Until then, ASEAN and RCEP tariff preferences still apply with the right certificate of origin.",
  src="Sources: MOFCOM, 20 Nov 2026<br>Media Indonesia/Antara, 12 Nov 2026",
  photo="Photo: Pasir Panjang Container Terminal, Singapore · Jacklee, CC BY-SA 3.0, Wikimedia Commons"),
"ru": dict(dir="ltr", kicker="Торговые соглашения · Азия", date="22.11.2026",
  h="Два новых торговых трека Китая за один день",
  a=("Сингапур", "4.0", "Переговоры об обновлении ССТ", "Новые темы: госзакупки и правила цифровой торговли. Соглашение подписано в 2008 г., обновлялось в 2018 и 2023 гг."),
  b=("Индонезия", "CEPA", "Первое двустороннее соглашение о партнёрстве", f"На базе ССТ Китай{NB}— АСЕАН и RCEP. Джакарта рассчитывает завершить переговоры в начале 2029 г."),
  tip="Пока идут переговоры, преференции АСЕАН и RCEP действуют при правильном сертификате происхождения.",
  src="Источники: Минкоммерции КНР, 20.11.2026<br>Media Indonesia/Antara, 12.11.2026",
  photo="Фото: контейнерный терминал Пасир-Панджанг, Сингапур · Jacklee, CC BY-SA 3.0, Wikimedia Commons"),
"fa": dict(dir="rtl", kicker="توافق‌های تجاری · آسیا", date="۱ آذر ۱۴۰۵",
  h="چین در یک روز دو مذاکرهٔ تجاری تازه را آغاز کرد",
  a=("سنگاپور", "4.0", "مذاکرات ارتقای موافقت‌نامهٔ تجارت آزاد", "محورهای تازه: خریدهای دولتی و قواعد تجارت دیجیتال. امضا در ۲۰۰۸، ارتقا در ۲۰۱۸ و ۲۰۲۳."),
  b=("اندونزی", "CEPA", "نخستین موافقت‌نامهٔ مشارکت اقتصادی جامع دوجانبه", "بر پایهٔ منطقهٔ تجارت آزاد چین و آسه‌آن و <bdi>RCEP</bdi>. هدف جاکارتا: پایان مذاکرات در اوایل ۲۰۲۹."),
  tip="تا آن زمان، ترجیحات تعرفه‌ای آسه‌آن و <bdi>RCEP</bdi> با گواهی مبدأ معتبر همچنان برقرار است.",
  src="منابع: وزارت بازرگانی چین، ۲۹ آبان ۱۴۰۵<br><bdi>Media Indonesia/Antara</bdi>، ۲۱ آبان ۱۴۰۵",
  photo="عکس: پایانهٔ کانتینری پاسیر پانجانگ، سنگاپور · <bdi>Jacklee, CC BY-SA 3.0</bdi>، ویکی‌مدیا کامنز"),
"ar": dict(dir="rtl", kicker="اتفاقيات تجارية · آسيا", date="<bdi>22</bdi> نوفمبر <bdi>2026</bdi>",
  h="الصين تطلق مفاوضتين تجاريتين جديدتين في يوم واحد",
  a=("سنغافورة", "4.0", "مفاوضات ترقية اتفاقية التجارة الحرة", "محاور جديدة: المشتريات الحكومية وقواعد التجارة الرقمية. وُقّعت عام <bdi>2008</bdi> ورُقّيت في <bdi>2018</bdi> و<bdi>2023</bdi>."),
  b=("إندونيسيا", "CEPA", "أول اتفاقية شراكة اقتصادية شاملة ثنائية", "على أساس منطقة التجارة الحرة بين الصين وآسيان واتفاقية <bdi>RCEP</bdi>. تستهدف جاكرتا إنجازها مطلع <bdi>2029</bdi>."),
  tip="حتى ذلك الحين، تبقى تفضيلات آسيان و<bdi>RCEP</bdi> الجمركية سارية مع شهادة منشأ صحيحة.",
  src="المصادر: وزارة التجارة الصينية، <bdi>20</bdi> نوفمبر <bdi>2026</bdi><br><bdi>Media Indonesia/Antara</bdi>، <bdi>12</bdi> نوفمبر <bdi>2026</bdi>",
  photo="الصورة: محطة باسير بانجانغ للحاويات، سنغافورة · <bdi>Jacklee, CC BY-SA 3.0</bdi>، ويكيميديا كومنز"),
}

def html(lang):
    t = T[lang]; rtl = t["dir"] == "rtl"
    if lang == "fa": hf, bf = "'Noto Kufi Arabic','Cormorant Garamond',serif", "'Vazirmatn','Manrope',sans-serif"
    elif lang == "ar": hf, bf = "'Noto Kufi Arabic','Cormorant Garamond',serif", "'IBM Plex Sans Arabic','Manrope',sans-serif"
    else: hf, bf = "'Cormorant Garamond',serif", "'Manrope',sans-serif"
    hsize = {"en": 76, "ru": 70, "fa": 46, "ar": 46}[lang]
    hlh = 1.0 if not rtl else 1.55
    plate = lambda p: f"""<div class="plate"><div class="tok">{p[1]}</div><div class="pt"><div class="cty">{p[0]}</div><div class="what">{p[2]}</div><p>{p[3]}</p></div></div>"""
    return f"""<!doctype html><html lang="{lang}" dir="{t['dir']}"><head><meta charset="utf-8">
<link rel="stylesheet" href="../brand/fonts.css"><style>
:root{{--sand:#F2ECE2;--green:#1F4D3A;--coral:#C8553A;--slate:#55606A;--lw-ink:#1F4D3A;--lw-seal:#AC3E33}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1350px;overflow:hidden;background:var(--sand);color:var(--green);font-family:{bf}}}
bdi{{direction:ltr;unicode-bidi:isolate}}
.photo{{position:absolute;top:0;bottom:0;{'right' if rtl else 'left'}:0;width:380px;overflow:hidden}}
.photo img{{width:100%;height:100%;object-fit:cover;object-position:{'38%' if rtl else '40%'} 50%;filter:saturate(.92) contrast(1.03)}}
.photo:after{{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(31,77,58,0) 70%,rgba(20,40,32,.55))}}
.photo .cr{{position:absolute;bottom:30px;{'right' if rtl else 'left'}:28px;width:320px;font:500 15px/1.4 Manrope,sans-serif;color:rgba(255,255,255,.88);z-index:2;{'text-align:right;' if rtl else ''}}}
.col{{position:absolute;top:0;bottom:0;{'left' if rtl else 'right'}:0;width:700px;padding:70px 64px 56px 64px;overflow:hidden;display:flex;flex-direction:column}}
.col>*{{position:relative;z-index:1}}
.col .lw-echo{{--lw-echo:#1F4D3A;--lw-echo-op:.045;--lw-echo-size:640px;z-index:0}}
.mast{{display:flex;justify-content:space-between;align-items:baseline;font:700 19px/1 {bf};letter-spacing:{'0' if rtl else '.16em'};text-transform:uppercase;color:var(--slate);padding-bottom:22px;border-bottom:1.5px solid rgba(31,77,58,.35)}}
.mast .k{{color:var(--coral)}}
h1{{font:700 {hsize}px/{hlh} {hf};margin-top:40px;letter-spacing:{'0' if rtl else '-.01em'}}}
.plates{{margin-top:38px}}
.plate{{display:flex;gap:26px;align-items:flex-start;padding:30px 0;border-top:1px solid rgba(31,77,58,.22)}}
.plate:last-child{{border-bottom:1px solid rgba(31,77,58,.22)}}
.tok{{flex:none;width:212px;font:700 80px/0.95 'Cormorant Garamond',serif;color:var(--coral);letter-spacing:-.02em;direction:ltr;text-align:{'right' if rtl else 'left'}}}
.cty{{font:700 20px/1.2 {bf};letter-spacing:{'0' if rtl else '.14em'};text-transform:uppercase;color:var(--slate)}}
.what{{font:700 {'27px/1.45' if rtl else '30px/1.15'} {bf if rtl else "'Cormorant Garamond',serif"};margin-top:8px}}
.plate p{{font:500 {'21px/1.65' if rtl else '21px/1.42'} {bf};color:#2E3A36;margin-top:10px}}
.tip{{margin-top:30px;font:600 {'22px/1.65' if rtl else '22px/1.4'} {bf};color:var(--green);padding-{'right' if rtl else 'left'}:22px;border-{'right' if rtl else 'left'}:4px solid var(--coral)}}
.foot{{margin-top:auto;display:flex;align-items:flex-end;justify-content:space-between;gap:24px}}
.foot .meta{{font:500 {'16px/1.6' if rtl else '16px/1.45'} {bf};color:var(--slate);max-width:380px}}
.foot .url{{font:700 26px/1 'Cormorant Garamond',serif;color:var(--green);margin-bottom:10px;letter-spacing:.02em}}
.lw-sig{{--lw-sig-h:62px}}
__MARKCSS__
</style></head><body>
<div class="photo"><img src="../photos/singapore-pasir-panjang-cranes.jpg"><div class="cr">{t['photo']}</div></div>
<div class="col">{echo('left' if rtl else 'right', '-170px', '-250px')}
  <div class="mast"><span class="k">{t['kicker']}</span><span>{t['date']}</span></div>
  <h1>{t['h']}</h1>
  <div class="plates">{plate(t['a'])}{plate(t['b'])}</div>
  <div class="tip">{t['tip']}</div>
  <div class="foot"><div class="meta"><div class="url">linkwinco.com</div>{t['src']}</div>{signature()}</div>
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
