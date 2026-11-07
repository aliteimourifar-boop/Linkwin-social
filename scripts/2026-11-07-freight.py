"""2026-11-07 · Freight Watch: Drewry WCI 5 Nov 2026 (EN/FA/RU/AR, feed + story)."""
import os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLUG = "2026-11-07-freight-rates"

# rate, change%  (Drewry WCI, 5 Nov 2026, US$ per 40ft)
LANES = [("ny", 9303, -3), ("la", 7539, 0), ("ge", 4166, 0), ("ro", 3615, -2)]
MAX = 9303

FA_DIG = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")

def money(v, lang):
    if lang == "fa": return f"{v:,}".replace(",", "٬").translate(FA_DIG) + " دلار"
    if lang == "ru": return "$" + f"{v:,}".replace(",", " ")
    if lang == "ar": return f"{v:,} دولار"
    return f"${v:,}"

def chg(c, lang):
    if c == 0:
        return {"en": "Flat", "fa": "بدون تغییر", "ru": "без изм.", "ar": "دون تغيير"}[lang]
    n = str(abs(c))
    if lang == "fa": return f"▼ {n.translate(FA_DIG)}٪"
    return f"▼ {n}%"

T = {
 "en": dict(dir="ltr", pill="FREIGHT WATCH",
   kicker="Drewry World Container Index · 5 Nov 2026",
   h1="Container rates<br>are <em>cooling.</em>",
   sub="The global composite slipped 1% this week. Here’s where the main China lanes stand.",
   comp_lbl="Global composite · all rates in US$ per 40ft container", comp_chg="▼ 1% on the week",
   lanes={"ny": "Shanghai → New York", "la": "Shanghai → Los Angeles", "ge": "Shanghai → Genoa", "ro": "Shanghai → Rotterdam"},
   unit="US$ per 40ft",
   chip="<b>Suez is back.</b> 60% of Asia–Europe capacity now sails through the canal.",
   lbl="Before you book",
   tip="Get quotes from 2–3 forwarders and check which surcharges are included. Carriers are pushing Asia–Europe increases for mid-November.",
   foot="LinkWin handles sourcing and shipping from China", src="Source: Drewry WCI, 5 Nov 2026"),
 "fa": dict(dir="rtl", pill="FREIGHT WATCH",
   kicker="شاخص جهانی کانتینر دروری · ۱۴ آبان ۱۴۰۵",
   h1="کرایه کانتینر<br>رو به <em>کاهش</em> است.",
   sub="شاخص ترکیبی این هفته ۱٪ پایین آمد. وضعیت مسیرهای اصلی حمل از چین را ببینید.",
   comp_lbl="شاخص ترکیبی جهانی · همه نرخ‌ها به دلار برای هر کانتینر ۴۰ فوتی", comp_chg="۱٪ ▼ نسبت به هفته قبل",
   lanes={"ny": "شانگهای ← نیویورک", "la": "شانگهای ← لس‌آنجلس", "ge": "شانگهای ← جنوا", "ro": "شانگهای ← روتردام"},
   unit="دلار برای هر کانتینر ۴۰ فوتی",
   chip="<b>کانال سوئز دوباره فعال شد.</b> اکنون ۶۰٪ ظرفیت مسیر آسیا–اروپا از این کانال عبور می‌کند.",
   lbl="پیش از رزرو",
   tip="از دو یا سه فورواردر قیمت بگیرید و ببینید کدام هزینه‌های جانبی در قیمت آمده است. خطوط کشتیرانی برای اواخر آبان افزایش نرخ مسیر آسیا–اروپا را دنبال می‌کنند.",
   foot="تأمین کالا و حمل از چین با LinkWin", src="منبع: Drewry، ۱۴ آبان ۱۴۰۵"),
 "ru": dict(dir="ltr", pill="FREIGHT WATCH",
   kicker="Индекс Drewry WCI · 5 ноября 2026",
   h1="Ставки фрахта<br><em>снижаются.</em>",
   sub="Сводный индекс за неделю опустился на 1%. Вот ситуация на главных направлениях из Китая.",
   comp_lbl="Сводный мировой индекс · все ставки в $ за 40-футовый контейнер", comp_chg="▼ 1% за неделю",
   lanes={"ny": "Шанхай → Нью-Йорк", "la": "Шанхай → Лос-Анджелес", "ge": "Шанхай → Генуя", "ro": "Шанхай → Роттердам"},
   unit="$ за 40-футовый контейнер",
   chip="<b>Суэц снова работает:</b> через него идёт 60% мощностей Азия–Европа.",
   lbl="Перед бронированием",
   tip="Запросите ставки у 2–3 экспедиторов и уточните, какие надбавки включены. С середины ноября перевозчики хотят поднять ставки Азия–Европа.",
   foot="LinkWin: закупка и доставка из Китая", src="Источник: Drewry WCI, 5 ноября 2026"),
 "ar": dict(dir="rtl", pill="FREIGHT WATCH",
   kicker="مؤشر دروري العالمي للحاويات · 5 نوفمبر 2026",
   h1="أسعار شحن الحاويات<br>تتجه إلى <em>الانخفاض.</em>",
   sub="تراجع المؤشر المركّب 1% هذا الأسبوع. إليك وضع أهم خطوط الشحن من الصين.",
   comp_lbl="المؤشر العالمي المركّب · جميع الأسعار بالدولار للحاوية 40 قدمًا", comp_chg="▼ 1% عن الأسبوع الماضي",
   lanes={"ny": "شنغهاي ← نيويورك", "la": "شنغهاي ← لوس أنجلوس", "ge": "شنغهاي ← جنوة", "ro": "شنغهاي ← روتردام"},
   unit="دولار للحاوية 40 قدمًا",
   chip="<b>قناة السويس تعود.</b> 60% من سعة خط آسيا–أوروبا تعبر القناة الآن.",
   lbl="قبل الحجز",
   tip="اطلب عروض أسعار من شركتين أو ثلاث شركات شحن، وتحقّق من الرسوم الإضافية المشمولة. شركات الملاحة تسعى لرفع أسعار خط آسيا–أوروبا في منتصف نوفمبر.",
   foot="التوريد والشحن من الصين مع LinkWin", src="المصدر: Drewry، 5 نوفمبر 2026"),
}

CSS = """
.wrap>*{flex-shrink:0}
.board{margin-top:30px;background:rgba(255,255,255,.04);border:1px solid var(--line);border-radius:26px;overflow:hidden}
.comp{display:flex;justify-content:space-between;align-items:flex-end;gap:20px;padding:22px 30px;background:linear-gradient(150deg,rgba(172,62,51,.92),rgba(118,37,30,.92))}
.comp .v{font-weight:800;font-size:74px;line-height:.95;letter-spacing:-.03em}
.comp .l{font-size:19px;color:#F6D9D3;margin-top:8px;max-width:520px;line-height:1.35}
.comp .c{flex:0 0 auto;font-weight:700;font-size:22px;background:var(--paper);color:var(--seal);padding:9px 14px;border-radius:12px}
.unit{padding:16px 32px 4px;font-size:16px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
[dir=rtl] .unit{letter-spacing:0;font-size:18px}
.lane{padding:13px 30px 14px;border-top:1px solid var(--line)}
.unit + .lane{border-top:none}
.row{display:flex;justify-content:space-between;align-items:baseline;gap:16px}
.row .n{font-size:23px;font-weight:600}
.row .r{display:flex;align-items:baseline;gap:16px}
.row .r b{font-size:29px;font-weight:800;letter-spacing:-.01em}
.row .r span{font-size:18px;font-weight:700;color:var(--gold);min-width:92px;text-align:end}
.row .r span.flat{color:var(--muted)}
.bar{margin-top:9px;height:7px;border-radius:8px;background:rgba(244,238,228,.08);overflow:hidden}
.bar i{display:block;height:100%;border-radius:8px;background:linear-gradient(90deg,var(--gold),#E2C68F)}
[dir=rtl] .bar i{margin-inline-start:0;background:linear-gradient(270deg,var(--gold),#E2C68F)}
.chip{margin-top:20px;display:flex;gap:14px;align-items:flex-start;font-size:22px;line-height:1.45;color:#CDD2D9}
.chip::before{content:"";flex:0 0 12px;height:12px;margin-top:11px;background:var(--seal2);transform:rotate(45deg)}
.chip b{color:#fff}
[dir=rtl] .chip{line-height:1.65}
.tip{margin-top:20px}

html:not(.story) .logo img{height:96px}
html:not(.story) .kicker{margin-top:32px}
html:not(.story) [dir=rtl] h1, html[dir=rtl]:not(.story) h1{font-size:68px}
html:not(.story) .lane{padding:10px 30px 11px}
html:not(.story) .comp{padding:18px 30px}
html:not(.story) .comp .v{font-size:66px}
html:not(.story) .board{margin-top:24px}
html:not(.story) .chip{margin-top:16px;font-size:21px}
html:not(.story) .tip{margin-top:16px;padding:18px 24px}
html:not(.story) .tip p{font-size:21px}
html:not(.story) .foot{padding:16px 0 30px}
html.story .board{margin-top:56px} html.story .tip{margin-top:40px} html.story .kicker{margin-top:70px}
"""

def page(lang, c):
    lanes = ""
    for key, v, ch in LANES:
        cls = "flat" if ch == 0 else ""
        lanes += (f'<div class="lane"><div class="row"><span class="n">{c["lanes"][key]}</span>'
                  f'<span class="r"><b>{money(v, lang)}</b><span class="{cls}">{chg(ch, lang)}</span></span></div>'
                  f'<div class="bar"><i style="width:{v / MAX * 100:.1f}%"></i></div></div>')
    comp = money(4389, lang)
    return f"""<!doctype html><html lang="{lang}" dir="{c['dir']}"><head><meta charset="utf-8">
<link rel="stylesheet" href="../brand/brand.css"><style>{CSS}</style></head>
<body><div class="bg"></div><div class="wrap">
<div class="top"><div class="logo"><img src="../brand/linkwin-logo-original-cropped.png"></div><div class="pill">{c['pill']}</div></div>
<div class="kicker">{c['kicker']}</div>
<h1>{c['h1']}</h1>
<p class="sub">{c['sub']}</p>
<div class="board">
 <div class="comp"><div><div class="v">{comp}</div><div class="l">{c['comp_lbl']}</div></div><div class="c">{c['comp_chg']}</div></div>
 {lanes}
</div>
<div class="chip"><span>{c['chip']}</span></div>
<div class="tip"><span class="lbl">{c['lbl']}</span><p>{c['tip']}</p></div>
<div class="foot"><div><b>{c['foot']}</b><div class="src">{c['src']}</div></div><span class="url">linkwinco.com</span></div>
</div></body></html>"""

for lang, c in T.items():
    tpl = f"{ROOT}/templates/{SLUG}-{lang}.html"
    open(tpl, "w").write(page(lang, c))
    for mode, suffix in (("feed", ""), ("story", "-story")):
        subprocess.run([sys.executable, f"{ROOT}/render.py", tpl, f"{ROOT}/posts/{SLUG}-{lang}{suffix}.jpg", mode], check=True)
print("rendered", SLUG)
