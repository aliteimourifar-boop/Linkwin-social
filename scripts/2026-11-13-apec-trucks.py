"""LinkWin daily post, 13 Nov 2026 — APEC week in Shenzhen: temporary truck restrictions 16–20 Nov.

CREATIVE BRIEF
Concept name: "Blue Hour Corridor" (first photographic post).
Idea: a long-exposure blue-hour photo of Shennan East Road, Shenzhen, its light trails running into the CBD,
  is the hero; a frosted-glass "week strip" at the bottom shows the five days 16–20 Nov and three hairline bars for
  the three truck restrictions. Feeling: calm, practical foresight: "the city will slow down; here is when".
Background tone: dark photographic (blue hour). 12 Nov was mid-light manila, 11 Nov light celadon, 10 Nov mid cobalt
  graphic: tone, palette and medium all change.
Palette: night navy #0B1730, sodium amber #F3A93B (from the light trails), frost white rgba(246,244,239,.9),
  seal red #AC3E33 only on the "today" hairline of the strip.
Composition: full-bleed photo; top scrim with kicker + headline (top-left LTR / top-right RTL); bottom frosted panel
  with the 5-day strip (columns mirror automatically for RTL) and footer. Not a still life (12 Nov), not a magazine
  cover/emblem (11 Nov), not an oversized numeral (10 Nov).
Type: IBM Plex Sans 600/400 (EN/RU) — first use as headline face; Vazirmatn 800/400 (FA, the face of linkwinco.com);
  IBM Plex Sans Arabic 600/400 (AR) stacked with IBM Plex Sans for Latin and digits.
Imagery: photos/shenzhen-shennan-east-road-dusk.jpg — Dinkun Chen, Wikimedia Commons, CC BY-SA 4.0 (credited on image).
Logo: B seal tab — paper tab with the full-colour original multiplied onto it, sitting in the footer bottom-right
  LTR / bottom-left RTL (10 Nov: B tab top-left; 11 Nov: A bottom-left; 12 Nov: A top-right).
RTL plan: dir=rtl mirrors headline block, strip column order (days read right-to-left), bar alignment and logo side.
  Persian uses Persian digits and Solar Hijri dates (16–20 Nov 2026 = 25–29 Aban 1405); Arabic uses Western digits.

FACTS (all from sources fetched 13 Nov 2026)
- 33rd APEC Economic Leaders' Meeting, Shenzhen, 18–19 Nov 2026; theme "Building an Asia-Pacific Community to Prosper
  Together"; APEC CEO Summit 17–18 Nov (Xinhua / MFA spokesperson, 13 Nov 2026).
- Shenzhen Public Security Bureau notice of 3 Nov 2026, in force 16–20 Nov:
  * hazardous-goods vehicles banned on all city roads incl. expressways, 00:00–24:00, 16–20 Nov;
  * large trucks (heavy/medium, tractors, special vehicles) 17–18 Nov 08:00–20:00 banned from Yuehai/Moon Bay Ave
    (north of Guangshen Yanjiang Expwy), Beihuan Ave (west of Longzhu interchange) and Tanglangshan Tunnel; plus one
    ramp (Nanping Expwy eastbound to G107, west-to-north) closed all day; detours via Guangshen Yanjiang Expwy,
    Mawan cross-sea passage, Nanping Expwy;
  * small trucks (light/mini; enclosed light/mini vans exempt) banned 06:00–22:00 on 18–19 Nov across all of Futian,
    Luohu and Nanshan, incl. the expressways inside those districts (Nanping Expwy east of G107 not restricted);
  * emergency, medical, fresh-food, repair and municipal vehicles can apply for a temporary pass on the
    "Shenzhen Traffic Police" WeChat account or the Minsheng Jingwu platform; existing standing truck rules still apply.
"""
import os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATE = "2026-11-13"
SLUG = "apec-trucks"
PHOTO = "../photos/shenzhen-shennan-east-road-dusk.jpg"
LOGO = "../brand/linkwin-logo-original-cropped.png"

T = {
"en": dict(dir="ltr", lang="en",
  kicker="APEC week · Shenzhen",
  h="APEC comes to Shenzhen. Plan your truck moves now.",
  days=[("Mon","16"),("Tue","17"),("Wed","18"),("Thu","19"),("Fri","20")], month="November 2026",
  rows=[("Hazardous goods","Banned citywide, all day",1,5),
        ("Large trucks","Key roads closed, 08:00–20:00",2,3),
        ("Small trucks","Out of Futian, Luohu, Nanshan, 06:00–22:00",3,4)],
  hook="LinkWin · trade and logistics partner in Hong Kong & Guangzhou",
  src="Sources: Shenzhen Public Security Bureau notice, 3 Nov 2026; Xinhua, 13 Nov 2026",
  photo="Photo: Dinkun Chen / Wikimedia Commons, CC BY-SA 4.0"),
"fa": dict(dir="rtl", lang="fa",
  kicker="هفتهٔ <bdi>APEC</bdi> در شنژن",
  h="اجلاس <bdi>APEC</bdi> در شنژن؛ حمل بار را از همین حالا برنامه‌ریزی کنید",
  days=[("دوشنبه","۲۵"),("سه‌شنبه","۲۶"),("چهارشنبه","۲۷"),("پنجشنبه","۲۸"),("جمعه","۲۹")], month="آبان ۱۴۰۵",
  rows=[("کالای خطرناک","تردد در کل شهر ممنوع، شبانه‌روزی",1,5),
        ("کامیون سنگین","چند محور اصلی بسته، ساعت ۸ تا ۲۰",2,3),
        ("کامیون سبک","ممنوع در فوتیان، لوهو و نان‌شان، ساعت ۶ تا ۲۲",3,4)],
  hook="LinkWin، شریک تجاری و لجستیکی شما در هنگ‌کنگ و گوانگجو",
  src="منبع: اطلاعیهٔ ادارهٔ پلیس شنژن، ۱۲ آبان ۱۴۰۵؛ خبرگزاری شین‌هوا، ۲۲ آبان ۱۴۰۵",
  photo="عکس: <bdi>Dinkun Chen / Wikimedia Commons, CC BY-SA 4.0</bdi>"),
"ru": dict(dir="ltr", lang="ru",
  kicker="Неделя АТЭС · Шэньчжэнь",
  h="АТЭС в Шэньчжэне: перевозки лучше спланировать уже сейчас",
  days=[("Пн","16"),("Вт","17"),("Ср","18"),("Чт","19"),("Пт","20")], month="Ноябрь 2026",
  rows=[("Опасные грузы","Запрет по всему городу, круглосуточно",1,5),
        ("Крупные грузовики","Часть магистралей закрыта, 8:00–20:00",2,3),
        ("Малые грузовики","Запрет в Футяне, Лоху и Наньшане, 6:00–22:00",3,4)],
  hook="LinkWin — партнёр по торговле и логистике в Гонконге и Гуанчжоу",
  src="Источники: уведомление полиции Шэньчжэня от 3.11.2026; Синьхуа, 13.11.2026",
  photo="Фото: Dinkun Chen / Wikimedia Commons, CC BY-SA 4.0"),
"ar": dict(dir="rtl", lang="ar",
  kicker="أسبوع <bdi>APEC</bdi> في شنتشن",
  h="قمة <bdi>APEC</bdi> في شنتشن: خطّط لنقل بضائعك من الآن",
  days=[("الاثنين","16"),("الثلاثاء","17"),("الأربعاء","18"),("الخميس","19"),("الجمعة","20")], month="نوفمبر 2026",
  rows=[("البضائع الخطرة","ممنوعة في المدينة كلها على مدار الساعة",1,5),
        ("الشاحنات الكبيرة","إغلاق طرق رئيسية من <bdi dir=\"ltr\">8:00</bdi> إلى <bdi dir=\"ltr\">20:00</bdi>",2,3),
        ("الشاحنات الصغيرة","ممنوعة في فوتيان ولوهو ونانشان من <bdi dir=\"ltr\">6:00</bdi> إلى <bdi dir=\"ltr\">22:00</bdi>",3,4)],
  hook="LinkWin، شريكك في التجارة والخدمات اللوجستية في هونغ كونغ وقوانغتشو",
  src="المصدر: إشعار شرطة شنتشن، 3 نوفمبر 2026؛ وكالة شينخوا، 13 نوفمبر 2026",
  photo="الصورة: <bdi>Dinkun Chen / Wikimedia Commons, CC BY-SA 4.0</bdi>"),
}

FONTS = {
  "en": ("'IBM Plex Sans',sans-serif", "'IBM Plex Sans',sans-serif"),
  "ru": ("'IBM Plex Sans',sans-serif", "'IBM Plex Sans',sans-serif"),
  "fa": ("'Vazirmatn','IBM Plex Sans',sans-serif", "'Vazirmatn','IBM Plex Sans',sans-serif"),
  "ar": ("'IBM Plex Sans Arabic','IBM Plex Sans',sans-serif", "'IBM Plex Sans Arabic','IBM Plex Sans',sans-serif"),
}
# per-language tuning so each version is balanced, not just text-swapped
TUNE = {
  "en": dict(hsize=78, hlh=1.06, hmax=860, lab=21, row=26),
  "ru": dict(hsize=70, hlh=1.08, hmax=900, lab=21, row=25),
  "fa": dict(hsize=70, hlh=1.45, hmax=900, lab=22, row=26),
  "ar": dict(hsize=74, hlh=1.4, hmax=900, lab=22, row=26),
}

def html(lang):
    t, (hf, bf), k = T[lang], FONTS[lang], TUNE[lang]
    rtl = t["dir"] == "rtl"
    ls = "0" if rtl else ".14em"   # never letter-space Arabic script
    tt = "none" if rtl else "uppercase"
    days = "".join(f'<div class="day"><span class="wd">{w}</span><span class="dn">{d}</span></div>' for w, d in t["days"])
    rows = ""
    for lab, txt, a, b in t["rows"]:
        rows += (f'<div class="row"><div class="rl"><b>{lab}</b><span>{txt}</span></div>'
                 f'<div class="track"><i style="grid-column:{a} / {b+1}"></i></div></div>')
    return f"""<!doctype html><html lang="{t['lang']}" dir="{t['dir']}"><head><meta charset="utf-8">
<link rel="stylesheet" href="../brand/fonts.css">
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1080px;height:1350px;overflow:hidden;background:#0B1730}}
body{{position:relative;font-family:{bf};color:#F6F4EF;-webkit-font-smoothing:antialiased}}
.photo{{position:absolute;left:50%;top:-250px;height:1600px;transform:translateX(-50%)}}
.scrim{{position:absolute;inset:0;background:
  linear-gradient(180deg,rgba(8,16,34,.92) 0%,rgba(8,16,34,.66) 22%,rgba(8,16,34,.08) 40%,rgba(8,16,34,0) 50%,rgba(8,16,34,.25) 70%,rgba(8,16,34,.80) 92%)}}
.top{{position:absolute;top:72px;{'right' if rtl else 'left'}:72px;width:{k['hmax']}px}}
.kicker{{font:600 22px/1 {bf};letter-spacing:{ls};text-transform:{tt};color:#F3A93B;display:flex;align-items:center;gap:16px}}
.kicker:before{{content:"";width:46px;height:2px;background:#F3A93B;display:block}}
h1{{margin-top:30px;font:{'800' if lang=='fa' else '600'} {k['hsize']}px/{k['hlh']} {hf};letter-spacing:{'0' if rtl else '-.012em'};text-wrap:balance;color:#FFFFFF;text-shadow:0 2px 24px rgba(0,0,0,.35)}}
.panel{{position:absolute;left:48px;right:48px;bottom:48px;padding:34px 40px 28px;border-radius:22px;
  background:rgba(10,20,42,.52);backdrop-filter:blur(14px) saturate(1.1);-webkit-backdrop-filter:blur(18px);
  border:1px solid rgba(246,244,239,.16)}}
.ph{{display:flex;justify-content:space-between;align-items:baseline;font:600 {k['lab']}px/1.2 {bf};color:rgba(246,244,239,.72);letter-spacing:{ls};text-transform:{tt}}}
.grid{{display:grid;grid-template-columns:repeat(5,1fr)}}
.days{{margin:20px 0 6px;padding-bottom:14px;border-bottom:1px solid rgba(246,244,239,.22)}}
.day{{text-align:center}}
.wd{{display:block;font:400 {k['lab']-2}px/1.2 {bf};color:rgba(246,244,239,.66);letter-spacing:{'0' if rtl else '.08em'};text-transform:{tt}}}
.dn{{display:block;margin-top:6px;font:600 38px/1 {hf};color:#FFFFFF}}
.row{{padding:16px 0 4px}}
.rl{{display:flex;gap:14px;align-items:baseline;font:400 {k['row']}px/1.35 {bf};color:rgba(246,244,239,.92)}}
.rl b{{font-weight:600;color:#F3A93B;white-space:nowrap}}
.track{{display:grid;grid-template-columns:repeat(5,1fr);height:10px;margin-top:12px;border-radius:5px;background:rgba(246,244,239,.10)}}
.track i{{display:block;height:10px;border-radius:5px;background:linear-gradient({'270deg' if rtl else '90deg'},#F3A93B,#F6C978)}}
.foot{{display:flex;align-items:flex-end;justify-content:space-between;gap:28px;margin-top:26px;padding-top:20px;border-top:1px solid rgba(246,244,239,.22)}}
.ft{{font:400 17px/1.5 {bf};color:rgba(246,244,239,.70)}}
.ft .hook{{font:600 20px/1.4 {bf};color:#FFFFFF}}
.ft .url{{font:600 20px/1.4 'IBM Plex Sans',sans-serif;color:#F3A93B;letter-spacing:.02em}}
.tab{{flex:none;background:#F4F0E8;padding:12px 14px;border-radius:10px;box-shadow:0 10px 26px rgba(0,0,0,.35), inset 0 0 0 1px rgba(0,0,0,.05)}}
.tab img{{display:block;height:96px;mix-blend-mode:multiply;filter:brightness(1.015)}}
</style></head><body>
<img class="photo" src="{PHOTO}" alt=""><div class="scrim"></div>
<div class="top"><div class="kicker"><span>{t['kicker']}</span></div><h1>{t['h']}</h1></div>
<div class="panel">
  <div class="ph"><span>{t['month']}</span></div>
  <div class="grid days">{days}</div>
  {rows}
  <div class="foot"><div class="ft"><div class="hook">{t['hook']}</div><div class="url">linkwinco.com</div><div>{t['src']}</div><div>{t['photo']}</div></div>
  <div class="tab"><img src="{LOGO}" alt="LinkWin"></div></div>
</div></body></html>"""

if __name__ == "__main__":
    langs = sys.argv[1:] or ["en", "fa", "ru", "ar"]
    for lang in langs:
        tpl = os.path.join(ROOT, "templates", f"{DATE}-{SLUG}-{lang}.html")
        open(tpl, "w", encoding="utf-8").write(html(lang))
        out = os.path.join(ROOT, "posts", DATE, f"{DATE}-{SLUG}-{lang}.jpg")
        subprocess.run([sys.executable, os.path.join(ROOT, "tools", "render.py"), tpl, out, "feed", "--no-strict"], check=True)
