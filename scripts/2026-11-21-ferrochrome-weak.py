"""LinkWin daily carousel, 21 Nov 2026 — Ferrochrome slips below cost, chrome ore holds (SMM weekly chromium review).

CREATIVE BRIEF
Concept name: "Specimen Readout" (a real chromite specimen floating on a gunmetal page like an assay-lab object, with two
  instrument-style readouts: ferrochrome pointing down, chrome ore steady).
Idea: buyers of chrome alloys want the week in one glance: alloy weak, ore firm, tender expected lower. Neutral, factual.
Background tone: mid (gunmetal) after the 20 Nov light mist carousel and the dark reel.
Palette: gunmetal #3C444C -> #2C3238, chrome white #EEF1F3, steel grey #AEB7BF, coral #E8836B (down), chrome-oxide green
  #8CC7A1 (steady/up); seal tone-on-tone silver.
Composition: masthead with the seal signature (new: logo in the masthead, not the footer) -> specimen cut-out (end side) ->
  headline -> two readout panels with arrow glyph + range + unit + note -> 2-figure strip -> tip -> footer (url, source, credit).
Type: Playfair Display 700 headline + Manrope (EN/RU); Noto Naskh Arabic 700 headline + Vazirmatn text (FA);
  Noto Naskh Arabic 700 + IBM Plex Sans Arabic (AR).
Imagery: photos/chromite-serpentine-geodil-1394-cutout.png (Darla Sondrol, CC0, Wikimedia Commons).
Logo: "Seal signature + echo": silver seal + chrome-white wordmarks in the masthead end; 5 % echo cropped at bottom end.
Carousel order (random, first != RU from 20 Nov): EN, FA, RU, AR.

FACTS (source fetched 21 Nov 2026): SMM, "Weak Demand Drags Ferrochrome Lower; Chrome Ore Prices Stabilize", 20 Nov 2026 17:14 GMT+8
- As of 20 Nov: HC ferrochrome Inner Mongolia 7,200-7,400 yuan/50-base mt; East China 7,650-7,700, down 125 w/w.
- Ferrochrome fell below cost lines into negative-margin territory.
- Steel-tender expectation index 7,400.26; mainstream expectations point to a decline of 200 yuan.
- China's October HC ferrochrome imports +5.11% m/m to 150,000 mt.
- Tianjin Port 40-42% South African fines 49-49.5 yuan/mt-degree, +0.5 w/w; spot stopped falling and stabilised;
  port inventories declined this week; overseas miner offers firm.
"""
import os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from linkwin_mark import MARK_CSS, signature, echo
DATE = "2026-11-21"; SLUG = "ferrochrome-weak"; NB = "\u00a0"
ORDER = ["en", "fa", "ru", "ar"]
DOWN, FLAT = "&#8600;", "&#8599;"

T = {
"en": dict(dir="ltr", kicker="Ferroalloys · China market", date="21 Nov 2026",
  h="Ferrochrome slips below cost. Chrome ore holds.",
  a=("High-carbon ferrochrome", DOWN, "7,200–7,400", "yuan/t, 50% Cr basis · Inner Mongolia", "East China 7,650–7,700, −125 on the week. Producers are now selling below cost."),
  b=("Chrome ore · SA 40–42% fines", FLAT, "49–49.5", "yuan per tonne-degree · Tianjin port", "+0.5 on the week. Spot stopped falling as port stocks eased; miners’ offers stay firm."),
  s1=("150,000 t", "China’s October imports of high-carbon ferrochrome, +5.11% m/m"),
  s2=("about −200", "yuan: what the market expects from the next steel-mill tender"),
  tip="Booking ferrochrome or chrome ore for Q1? Ask us for current offers.",
  src="Source: SMM weekly chromium review, 20 Nov 2026",
  photo="Photo: chromite with serpentine · Darla Sondrol, CC0, Wikimedia Commons"),
"ru": dict(dir="ltr", kicker="Ферросплавы · рынок Китая", date="21.11.2026",
  h="Феррохром ниже себестоимости, хромовая руда держится",
  a=("Высокоуглеродистый феррохром", DOWN, f"7{NB}200–7{NB}400", "юаней/т, база 50% Cr · Внутренняя Монголия", f"Восточный Китай 7{NB}650–7{NB}700, −125 за неделю. Заводы продают ниже себестоимости."),
  b=("Хромовая руда · ЮАР, 40–42%", FLAT, "49–49,5", "юаней за тонно-процент · порт Тяньцзинь", "+0,5 за неделю. Спот перестал падать: портовые запасы снизились, офферы горняков твёрдые."),
  s1=(f"150{NB}тыс.{NB}т", f"импорт высокоуглеродистого феррохрома в Китай в октябре, +5,11{NB}% м/м"),
  s2=("около −200", "юаней — так рынок оценивает следующий тендер сталеваров"),
  tip="Закупаете феррохром или хромовую руду на I квартал? Запросите актуальные предложения.",
  src="Источник: SMM, недельный обзор рынка хрома, 20.11.2026",
  photo="Фото: хромит с серпентином · Darla Sondrol, CC0, Wikimedia Commons"),
"fa": dict(dir="rtl", kicker="فروآلیاژ · بازار چین", date="۳۰ آبان ۱۴۰۵",
  h="فروکروم زیر قیمت تمام‌شده؛ سنگ کروم پایدار",
  a=("فروکروم پرکربن", DOWN, "۷٬۲۰۰ تا ۷٬۴۰۰", "یوان در تن، پایهٔ ۵۰٪ کروم · مغولستان داخلی", "شرق چین ۷٬۶۵۰ تا ۷٬۷۰۰ یوان، ۱۲۵ یوان ارزان‌تر از هفتهٔ پیش. تولیدکنندگان زیر قیمت تمام‌شده می‌فروشند."),
  b=("سنگ کروم · نرمهٔ ۴۰ تا ۴۲٪ آفریقای جنوبی", FLAT, "۴۹ تا ۴۹٫۵", "یوان برای هر تن-درصد · بندر تیانجین", "۰٫۵ یوان بالاتر از هفتهٔ پیش. با کاهش موجودی بندرها افت قیمت متوقف شد؛ پیشنهاد معدن‌داران محکم است."),
  s1=("۱۵۰ هزار تن", "واردات فروکروم پرکربن چین در اکتبر؛ ۵٫۱۱٪ رشد ماهانه"),
  s2=("حدود ۲۰۰ یوان", "کاهشی که بازار از مناقصهٔ بعدی فولادسازان انتظار دارد"),
  tip="برای سه ماههٔ نخست فروکروم یا سنگ کروم می‌خرید؟ پیشنهاد روز را از ما بخواهید.",
  src="منبع: SMM، گزارش هفتگی بازار کروم، ۲۹ آبان ۱۴۰۵",
  photo="عکس: کرومیت همراه سرپانتین · Darla Sondrol، مجوز CC0، ویکی‌مدیا کامانز"),
"ar": dict(dir="rtl", kicker="السبائك الحديدية · السوق الصينية", date="<bdi>21</bdi> نوفمبر <bdi>2026</bdi>",
  h="الفيروكروم دون التكلفة، وخام الكروم يتماسك",
  a=("الفيروكروم عالي الكربون", DOWN, "<bdi>7,200–7,400</bdi>", "يوان/طن، أساس <bdi>50%</bdi> كروم · منغوليا الداخلية", "شرق الصين <bdi>7,650–7,700</bdi>، بانخفاض <bdi>125</bdi> يوانًا خلال الأسبوع. المنتجون يبيعون دون التكلفة."),
  b=("خام الكروم · ناعم جنوب أفريقيا <bdi>40–42%</bdi>", FLAT, "<bdi>49–49.5</bdi>", "يوان لكل طن-درجة · ميناء تيانجين", "ارتفاع <bdi>0.5</bdi> خلال الأسبوع. توقف التراجع مع انخفاض مخزونات الموانئ، وعروض المنتجين ثابتة."),
  s1=("<bdi>150</bdi> ألف طن", "واردات الصين من الفيروكروم عالي الكربون في أكتوبر، بزيادة <bdi>5.11%</bdi> على أساس شهري"),
  s2=("نحو <bdi>200</bdi> يوان", "تراجع يتوقعه السوق في المناقصة المقبلة لمصانع الصلب"),
  tip="تشتري الفيروكروم أو خام الكروم للربع الأول؟ اطلب منا أحدث العروض.",
  src="المصدر: SMM، المراجعة الأسبوعية لسوق الكروم، <bdi>20</bdi> نوفمبر <bdi>2026</bdi>",
  photo="الصورة: كروميت مع سربنتين · Darla Sondrol، ترخيص <bdi>CC0</bdi>، ويكيميديا كومنز"),
}
LAT_H, LAT_B = "'Playfair Display',serif", "'Manrope',sans-serif"
FONTS = {"en": (LAT_H, LAT_B, "'Manrope',sans-serif"), "ru": (LAT_H, LAT_B, "'Manrope',sans-serif"),
         "fa": ("'Noto Naskh Arabic','Playfair Display',serif", "'Vazirmatn','Manrope',sans-serif", "'Vazirmatn','Manrope',sans-serif"),
         "ar": ("'Noto Naskh Arabic','Playfair Display',serif", "'IBM Plex Sans Arabic','Manrope',sans-serif", "'Manrope','IBM Plex Sans Arabic',sans-serif")}
TUNE = {"en": dict(h=76, hlh=1.05, num=70, lab=21), "ru": dict(h=64, hlh=1.1, num=64, lab=21),
        "fa": dict(h=66, hlh=1.5, num=58, lab=22), "ar": dict(h=66, hlh=1.5, num=60, lab=22)}

def html(lang):
    t = T[lang]; hf, bf, nf = FONTS[lang]; k = TUNE[lang]
    rtl = t["dir"] == "rtl"; start, end = ("right", "left") if rtl else ("left", "right")
    ls = "0" if rtl else ".16em"; tt = "none" if rtl else "uppercase"
    def panel(p, cls):
        return (f'<div class="rd {cls}"><div class="tab">{p[0]}</div><div class="row"><span class="ar">{p[1]}</span><b>{p[2]}</b></div>'
                f'<div class="unit">{p[3]}</div><p>{p[4]}</p></div>')
    return f"""<!doctype html><html lang="{lang}" dir="{t['dir']}"><head><meta charset="utf-8">
<link rel="stylesheet" href="../brand/fonts.css"><style>
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1080px;height:1350px;overflow:hidden;background:#363E45}}
body{{position:relative;font-family:{bf};color:#EEF1F3;-webkit-font-smoothing:antialiased;
  background:radial-gradient(900px 700px at {'20%' if rtl else '80%'} 22%,#4C565F 0%,#3A424A 45%,#2B3137 100%);
  --lw-ink:#EEF1F3;--lw-seal:#D3D9DE;--lw-echo:#EEF1F3;--lw-echo-op:.035;--lw-echo-size:560px}}
body:before{{content:"";position:absolute;inset:0;background:repeating-linear-gradient(90deg,rgba(255,255,255,.018) 0 1px,transparent 1px 4px);pointer-events:none}}
.spec{{position:absolute;{end}:-30px;top:118px;width:640px;height:443px;background:url(../photos/chromite-serpentine-geodil-1394-cutout.png) center/contain no-repeat;
  filter:drop-shadow(0 34px 40px rgba(0,0,0,.5)) contrast(1.06);transform:rotate({'4deg' if rtl else '-4deg'});z-index:1}}
.mast{{position:absolute;left:72px;right:72px;top:52px;display:flex;justify-content:space-between;align-items:center;z-index:3}}
.mast .k{{font:700 19px/1.4 {bf};letter-spacing:{ls};text-transform:{tt};color:#AEB7BF}}
.mast .k span{{display:block;color:#EEF1F3;letter-spacing:{'0' if rtl else '.08em'}}}
.page{{position:absolute;left:72px;right:72px;top:455px;bottom:52px;display:flex;flex-direction:column;z-index:2}}
h1{{font:700 {k['h']}px/{k['hlh']} {hf};max-width:{'900px' if lang in ('ru',) else '860px'};text-wrap:balance;text-shadow:0 2px 18px rgba(0,0,0,.35)}}
.rds{{display:grid;grid-template-columns:1fr 1fr;gap:0;margin-top:42px;border-top:1px solid rgba(238,241,243,.35)}}
.rd{{padding:26px 0 0;position:relative}}
.rd.b{{padding-{start}:32px;border-{start}:1px solid rgba(238,241,243,.18)}}
.rd.a{{padding-{end}:32px}}
.tab{{font:700 18px/1.35 {bf};letter-spacing:{'0' if rtl else '.1em'};text-transform:{tt};color:#AEB7BF}}
.row{{display:flex;align-items:center;gap:14px;margin-top:12px}}
.row b{{font:800 {k['num']}px/1.05 {nf};letter-spacing:{'0' if rtl else '-.02em'};white-space:nowrap}}
.ar{{flex:none;width:52px;height:52px;border-radius:50%;display:grid;place-items:center;font:700 30px/1 'Manrope',sans-serif}}
.a .ar{{background:#E8836B;color:#2B3137}} .a .row b{{color:#F2A08C}}
.b .ar{{background:#8CC7A1;color:#2B3137}} .b .row b{{color:#A9D8B8}}
[dir=rtl] .ar{{transform:scaleX(-1)}}
.unit{{margin-top:10px;font:600 18px/1.4 {bf};color:#C9D0D6}}
.rd p{{margin-top:14px;font:400 {k['lab']}px/1.5 {bf};color:#DDE2E6}}
.strip{{display:grid;grid-template-columns:1fr 1fr;margin-top:34px;padding-top:24px;border-top:1px solid rgba(238,241,243,.18)}}
.strip div+div{{padding-{start}:32px}}
.strip b{{display:block;font:800 40px/1.2 {nf};color:#EEF1F3;white-space:nowrap}}
.strip span{{display:block;margin-top:6px;font:400 19px/1.45 {bf};color:#AEB7BF;padding-{end}:18px}}
.tip{{margin-top:auto;font:600 23px/1.45 {bf};color:#EEF1F3;padding:18px 0 18px;padding-{start}:20px;border-{start}:3px solid #8CC7A1;margin-bottom:14px}}
.foot{{padding-top:14px;border-top:1px solid rgba(238,241,243,.25);font:400 14px/1.55 {bf};color:#AEB7BF}}
.foot .url{{font:700 19px/1.4 'Manrope',sans-serif;color:#EEF1F3;letter-spacing:.02em;margin-bottom:2px}}
bdi{{direction:ltr;unicode-bidi:isolate}}
__MARKCSS__
.lw-sig{{--lw-sig-h:56px}}
</style></head><body>
{echo(start, '-200px', '-170px')}
<div class="spec"></div>
<div class="mast"><div class="k">{t['kicker']}<span>{t['date']}</span></div>{signature()}</div>
<div class="page">
  <h1>{t['h']}</h1>
  <div class="rds">{panel(t['a'],'a')}{panel(t['b'],'b')}</div>
  <div class="strip"><div><b>{t['s1'][0]}</b><span>{t['s1'][1]}</span></div><div><b>{t['s2'][0]}</b><span>{t['s2'][1]}</span></div></div>
  <div class="tip">{t['tip']}</div>
  <div class="foot"><div class="url">linkwinco.com</div>{t['src']} · {t['photo']}</div>
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
