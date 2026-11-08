"""2026-11-08 · China export-control pause: key dates (timeline). EN/FA/RU/AR, feed + story.
Sources: MOFCOM/GAC Announcement No. 70 (7 Nov 2025, pause to 10 Nov 2026); MOFCOM Announcement No. 72
(9 Nov 2025, pause to 27 Nov 2026); MOFCOM statement 28 Sep 2026 (Kuala Lumpur arrangement to 10 Jan 2027)."""
import os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLUG = "2026-11-08-export-controls"

T = {
 "en": dict(dir="ltr", pill="TRADE RULES",
   kicker="China export controls · Key dates",
   h1="Three dates every<br>metals buyer should <em>watch.</em>",
   sub="China’s one-year pause on its tougher export controls is running out. Here’s the timeline and what it covers.",
   items=[
     ("Nov 2025", "One-year pause", "After the Busan summit, Beijing paused its October 2025 controls and its US-only export ban for a year."),
     ("10 Nov 2026", "Pause on the Oct 2025 package ends", "Five rare earths (incl. erbium, holmium), rare-earth equipment and tech, lithium-battery and graphite-anode items. No extension notice published as of 5 Nov."),
     ("27 Nov 2026", "Pause on the US-only ban ends", "Gallium, germanium, antimony and superhard materials."),
     ("10 Jan 2027", "US–China truce deadline", "MOFCOM says the Kuala Lumpur trade arrangement now runs to this date."),
   ],
   chip="<b>Never paused:</b> export licences for gallium, germanium, antimony and seven rare earths, for every destination.",
   lbl="Buyer’s tip",
   tip="Importing critical minerals or magnets from China? Confirm your supplier’s export-licence status before paying a deposit, and allow extra lead time on winter orders.",
   foot="LinkWin sources metals and minerals from China", src="Source: MOFCOM Ann. No. 70 & 72 (2025); MOFCOM, 28 Sep 2026"),
 "fa": dict(dir="rtl", pill="TRADE RULES",
   kicker="کنترل صادرات چین · تاریخ‌های کلیدی",
   h1="سه تاریخ مهم<br>برای خریداران <em>فلزات</em>",
   sub="مهلت یک‌ساله تعلیق کنترل‌های سخت‌گیرانه صادراتی چین رو به پایان است. جدول زمانی و دامنه آن را ببینید.",
   items=[
     ("آبان ۱۴۰۴", "تعلیق یک‌ساله", "پس از نشست بوسان، پکن کنترل‌های مهر ۱۴۰۴ و ممنوعیت صادرات ویژه آمریکا را یک سال معلق کرد."),
     ("۱۹ آبان ۱۴۰۵", "پایان تعلیق بسته مهر ۱۴۰۴", "پنج عنصر خاکی کمیاب (از جمله اربیوم و هولمیوم)، تجهیزات و فناوری خاکی کمیاب، باتری لیتیومی و آند گرافیتی. تا ۱۴ آبان اطلاعیه تمدیدی منتشر نشده بود."),
     ("۶ آذر ۱۴۰۵", "پایان تعلیق ممنوعیت صادرات به آمریکا", "گالیم، ژرمانیم، آنتیموان و مواد فوق‌سخت."),
     ("۲۰ دی ۱۴۰۵", "سررسید آتش‌بس تجاری چین و آمریکا", "به اعلام وزارت بازرگانی چین، توافق کوالالامپور تا این تاریخ تمدید شده است."),
   ],
   chip="<b>بدون تعلیق:</b> صادرات گالیم، ژرمانیم، آنتیموان و هفت عنصر خاکی کمیاب به هر مقصدی همچنان مجوز می‌خواهد.",
   lbl="نکته خرید",
   tip="فلزات حیاتی یا آهن‌ربا از چین وارد می‌کنید؟ پیش از واریز پیش‌پرداخت، وضعیت مجوز صادرات تأمین‌کننده را بررسی کنید و برای سفارش‌های زمستانی زمان تحویل بیشتری در نظر بگیرید.",
   foot="تأمین فلزات و مواد معدنی از چین با LinkWin", src="منبع: وزارت بازرگانی چین، اطلاعیه‌های ۷۰ و ۷۲ (۲۰۲۵) و ۶ مهر ۱۴۰۵"),
 "ru": dict(dir="ltr", pill="TRADE RULES",
   kicker="Экспортный контроль Китая · Ключевые даты",
   h1="Три даты, важные<br>для <em>покупателей металлов</em>",
   sub="Годовая пауза в ужесточённом экспортном контроле Китая подходит к концу. Вот хронология и что она затрагивает.",
   items=[
     ("Ноябрь 2025", "Пауза на год", "После саммита в Пусане Пекин на год приостановил октябрьские меры 2025 года и запрет на экспорт в США."),
     ("10 ноября 2026", "Конец паузы для пакета октября 2025", "Пять РЗЭ (в т. ч. эрбий и гольмий), оборудование и технологии РЗЭ, литиевые батареи и графитовые аноды. На 5 ноября уведомления о продлении не было."),
     ("27 ноября 2026", "Конец паузы для запрета экспорта в США", "Галлий, германий, сурьма и сверхтвёрдые материалы."),
     ("10 января 2027", "Срок торгового перемирия", "По данным Минкоммерции КНР, договорённости Куала-Лумпура продлены до этой даты."),
   ],
   chip="<b>Без паузы:</b> экспорт галлия, германия, сурьмы и семи РЗЭ в любую страну по-прежнему требует лицензии.",
   lbl="Совет покупателю",
   tip="Закупаете критические металлы или магниты в Китае? Проверьте экспортную лицензию поставщика до предоплаты и заложите запас по срокам для зимних заказов.",
   foot="LinkWin: поставки металлов и минералов из Китая", src="Источник: Минкоммерции КНР, объявления № 70 и 72 (2025); 28 сентября 2026"),
 "ar": dict(dir="rtl", pill="TRADE RULES",
   kicker="ضوابط التصدير الصينية · مواعيد رئيسية",
   h1="ثلاثة مواعيد مهمة<br>لمستوردي <em>المعادن</em>",
   sub="يقترب انتهاء التعليق المؤقت لمدة عام لضوابط التصدير الصينية المشدّدة. إليك الجدول الزمني وما يشمله.",
   items=[
     ("نوفمبر 2025", "تعليق لمدة عام", "بعد قمة بوسان، علّقت بكين ضوابط أكتوبر 2025 وحظر التصدير الخاص بالولايات المتحدة لمدة عام."),
     ("10 نوفمبر 2026", "انتهاء تعليق حزمة أكتوبر 2025", "خمسة عناصر أرضية نادرة (منها الإربيوم والهولميوم)، ومعدات وتقنيات العناصر النادرة، وبطاريات الليثيوم وأنود الغرافيت. لم يصدر إشعار تمديد حتى 5 نوفمبر."),
     ("27 نوفمبر 2026", "انتهاء تعليق الحظر على الولايات المتحدة", "الغاليوم والجرمانيوم والأنتيمون والمواد فائقة الصلابة."),
     ("10 يناير 2027", "موعد انتهاء الهدنة التجارية", "بحسب وزارة التجارة الصينية، مُدّد ترتيب كوالالمبور التجاري حتى هذا التاريخ."),
   ],
   chip="<b>دون تعليق:</b> لا يزال تصدير الغاليوم والجرمانيوم والأنتيمون وسبعة عناصر أرضية نادرة يتطلب ترخيصًا لجميع الوجهات.",
   lbl="نصيحة للمشتري",
   tip="تستورد معادن حيوية أو مغناطيسات من الصين؟ تحقّق من ترخيص التصدير لدى المورّد قبل دفع العربون، وأضف وقتًا إضافيًا للتسليم في طلبات الشتاء.",
   foot="توريد المعادن والخامات من الصين مع LinkWin", src="المصدر: وزارة التجارة الصينية، الإعلانان 70 و72 (2025)؛ 28 سبتمبر 2026"),
}

CSS = """
.wrap>*{flex-shrink:0}
.tl{margin-top:30px;position:relative;padding-inline-start:46px}
.tl::before{content:"";position:absolute;inset-inline-start:13px;top:14px;bottom:20px;width:3px;border-radius:3px;background:linear-gradient(180deg,var(--gold),rgba(200,169,106,.25))}
.it{position:relative;padding:0 0 20px}
.it::before{content:"";position:absolute;inset-inline-start:-42px;top:8px;width:20px;height:20px;border-radius:50%;background:var(--ink);border:4px solid var(--gold)}
.it.hot::before{background:var(--seal2);border-color:var(--seal2);box-shadow:0 0 0 7px rgba(208,96,79,.25)}
.it .d{display:inline-block;font-size:19px;font-weight:800;letter-spacing:.06em;color:var(--gold);text-transform:uppercase}
.it.hot .d{color:var(--seal2)}
[dir=rtl] .it .d{letter-spacing:0;font-size:21px}
.it h3{font-size:28px;font-weight:700;margin-top:3px;line-height:1.25}
.it p{font-size:21px;line-height:1.42;color:#C4CAD2;margin-top:5px}
[dir=rtl] .it p{line-height:1.6}
.chip{margin-top:6px;display:flex;gap:14px;align-items:flex-start;font-size:21px;line-height:1.45;color:#CDD2D9}
.chip::before{content:"";flex:0 0 12px;height:12px;margin-top:11px;background:var(--seal2);transform:rotate(45deg)}
.chip b{color:#fff}
[dir=rtl] .chip{line-height:1.65}
.tip{margin-top:20px}

html:not(.story) .wrap{padding-top:64px}
html:not(.story) .logo img{height:88px}
html:not(.story) .kicker{margin-top:26px}
html:not(.story) h1{font-size:66px;margin-top:12px}
html[dir=rtl]:not(.story) h1{font-size:60px}
html:not(.story) .sub{font-size:23px;margin-top:12px}
html:not(.story) .tl{margin-top:20px}
html:not(.story) .it{padding-bottom:11px}
html:not(.story) .it h3{font-size:25px}
html:not(.story) .it p{font-size:20px}
html:not(.story) .tip{margin-top:14px;padding:16px 22px}
html:not(.story) .tip p{font-size:20px}
html:not(.story) .foot{padding:14px 0 28px}
html.story .wrap{padding-top:190px} html.story .foot{padding-bottom:230px}
html.story .kicker{margin-top:40px} html.story h1{font-size:76px} html[dir=rtl].story h1{font-size:68px}
html.story .sub{font-size:25px} html.story .tl{margin-top:34px} html.story .it{padding-bottom:20px}
html.story .tip{margin-top:26px}
"""

def page(lang, c):
    items = ""
    for i, (d, h, p) in enumerate(c["items"]):
        cls = "it hot" if i == 1 else "it"
        items += f'<div class="{cls}"><span class="d">{d}</span><h3>{h}</h3><p>{p}</p></div>'
    return f"""<!doctype html><html lang="{lang}" dir="{c['dir']}"><head><meta charset="utf-8">
<link rel="stylesheet" href="../brand/brand.css"><style>{CSS}</style></head>
<body><div class="bg"></div><div class="wrap">
<div class="top"><div class="logo"><img src="../brand/linkwin-logo-original-cropped.png"></div><div class="pill">{c['pill']}</div></div>
<div class="kicker">{c['kicker']}</div>
<h1>{c['h1']}</h1>
<p class="sub">{c['sub']}</p>
<div class="tl">{items}</div>
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
