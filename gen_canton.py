import json, subprocess, os, sys
ROOT = os.path.dirname(os.path.abspath(__file__))
FONTS = "/home/claude/fonts"

L = {
 "en": dict(dir="ltr", font="'Inter Display','Inter'", body="'Inter'",
   kicker="Canton Fair · Guangzhou · Nov 2026",
   h1='352,000 buyers<br>came to <em>Guangzhou.</em>',
   sub="The 140th Canton Fair just closed with a record crowd. Here’s what it means for importers.",
   stats=[("+12.2%","more overseas buyers than the previous session",""),("219","countries & regions",""),("32,000+","exhibitors",""),("4.88M","products on show","")],
   ins=["<b>64%</b> of products use AI or industrial-internet tech","Green products hit a record <b>26%</b> of exhibits"],
   lbl="What to do now",
   tip="Factories are busy following up with new buyers. Place orders by early December to ship before Chinese New Year (6 Feb 2027).",
   foot="LinkWin sources, verifies and ships from Guangzhou", src="Source: Xinhua, 4 Nov 2026"),
 "fa": dict(dir="rtl", font="'Vazirmatn','Inter'", body="'Vazirmatn','Inter'",
   kicker="نمایشگاه کانتون · گوانگجو · آبان ۱۴۰۵",
   h1='۳۵۲ هزار خریدار<br>به <em>گوانگجو</em> آمدند.',
   sub="صد و چهلمین دوره نمایشگاه کانتون با رکورد حضور خریداران خارجی به پایان رسید. پیامش برای واردکنندگان چیست؟",
   stats=[("+۱۲٫۲٪","خریدار خارجی بیشتر از دوره قبل",""),("۲۱۹","کشور و منطقه",""),("+۳۲٬۰۰۰","غرفه‌دار",""),("۴٫۸۸ میلیون","محصول",""),],
   ins=["<b>۶۴٪</b> محصولات از هوش مصنوعی یا اینترنت صنعتی بهره می‌برند","محصولات سبز با <b>۲۶٪</b> رکورد تازه‌ای زدند"],
   lbl="الان چه باید کرد؟",
   tip="کارخانه‌ها سرگرم پیگیری خریداران تازه‌اند. سفارش‌ها را تا نیمه آذر ثبت کنید تا پیش از سال نو چینی (۱۷ بهمن) بارگیری شوند.",
   foot="تأمین، بازرسی و ارسال کالا از گوانگجو با LinkWin", src="منبع: خبرگزاری شینهوا، ۱۳ آبان ۱۴۰۵"),
 "ru": dict(dir="ltr", font="'Inter Display','Inter'", body="'Inter'",
   kicker="Кантонская ярмарка · Гуанчжоу · ноябрь 2026",
   h1='352 000 покупателей<br>приехали в <em>Гуанчжоу.</em>',
   sub="140-я Кантонская ярмарка завершилась с рекордной посещаемостью. Что это значит для импортёров.",
   stats=[("+12,2%","больше иностранных покупателей, чем на прошлой сессии",""),("219","стран и регионов",""),("32 000+","экспонентов",""),("4,88 млн","товаров",""),],
   ins=["<b>64%</b> товаров используют ИИ или промышленный интернет","Доля «зелёных» товаров — рекордные <b>26%</b>"],
   lbl="Что делать сейчас",
   tip="Фабрики заняты новыми покупателями. Размещайте заказы до начала декабря, чтобы отгрузить их до Китайского Нового года (6 февраля 2027).",
   foot="LinkWin: поиск, проверка и отгрузка из Гуанчжоу", src="Источник: Синьхуа, 4 ноября 2026"),
 "ar": dict(dir="rtl", font="'Vazirmatn','Inter'", body="'Vazirmatn','Inter'",
   kicker="معرض كانتون · قوانغتشو · نوفمبر 2026",
   h1='352 ألف مشترٍ<br>توافدوا إلى <em>قوانغتشو.</em>',
   sub="اختُتمت الدورة الـ140 لمعرض كانتون بحضور قياسي للمشترين الأجانب. إليك ما يعنيه ذلك للمستوردين.",
   stats=[("+12.2%","زيادة في عدد المشترين الأجانب مقارنة بالدورة السابقة",""),("219","دولة ومنطقة",""),("+32,000","عارض",""),("4.88 مليون","منتج",""),],
   ins=["<b>64%</b> من المنتجات تعتمد على الذكاء الاصطناعي أو الإنترنت الصناعي","المنتجات الخضراء سجّلت رقمًا قياسيًا بنسبة <b>26%</b>"],
   lbl="ماذا تفعل الآن؟",
   tip="المصانع منشغلة بمتابعة المشترين الجدد. قدّم طلباتك بحلول مطلع ديسمبر لتُشحن قبل رأس السنة الصينية (6 فبراير 2027).",
   foot="توريد وفحص وشحن من قوانغتشو مع LinkWin", src="المصدر: وكالة شينخوا، 4 نوفمبر 2026"),
}

CSS = f"""
@font-face{{font-family:'Vazirmatn';src:url('file://{FONTS}/fontsource-vazirmatn-5.3.0/files/vazirmatn-arabic-400-normal.woff2');font-weight:400}}
@font-face{{font-family:'Vazirmatn';src:url('file://{FONTS}/fontsource-vazirmatn-5.3.0/files/vazirmatn-arabic-600-normal.woff2');font-weight:600}}
@font-face{{font-family:'Vazirmatn';src:url('file://{FONTS}/fontsource-vazirmatn-5.3.0/files/vazirmatn-arabic-800-normal.woff2');font-weight:800}}
@font-face{{font-family:'Vazirmatn';src:url('file://{FONTS}/fontsource-vazirmatn-5.3.0/files/vazirmatn-arabic-900-normal.woff2');font-weight:900}}
:root{{--ink:#12161D;--paper:#F4EEE4;--seal:#AC3E33;--seal2:#D0604F;--gold:#C8A96A;--muted:#98A1AD;--line:rgba(244,238,228,.13)}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1350px}}
body{{background:var(--ink);color:var(--paper);position:relative;overflow:hidden}}
.bg{{position:absolute;inset:0;background:
  radial-gradient(1100px 700px at 100% 0%,rgba(172,62,51,.42),transparent 62%),
  radial-gradient(800px 600px at 0% 100%,rgba(200,169,106,.14),transparent 60%),
  linear-gradient(170deg,#161B24,#0E1117)}}
.routes{{position:absolute;inset:0;opacity:.5}}
.wrap{{position:relative;height:100%;padding:76px 80px 0;display:flex;flex-direction:column}}
.top{{display:flex;justify-content:space-between;align-items:center;direction:ltr}}
.name{{font-family:'Inter';font-weight:700;font-size:24px;letter-spacing:.32em}}
.name small{{display:block;font-weight:500;font-size:13px;letter-spacing:.42em;color:var(--muted);margin-top:6px}}
.live{{font-family:'Inter';font-size:15px;font-weight:700;letter-spacing:.24em;color:#fff;background:var(--seal);padding:11px 18px;border-radius:40px}}
.kicker{{margin-top:44px;font-size:21px;font-weight:600;letter-spacing:.2em;text-transform:uppercase;color:var(--gold)}}
[dir=rtl] .kicker{{letter-spacing:0;font-size:24px;margin-top:36px}}
h1{{margin-top:20px;font-weight:800;font-size:84px;line-height:1.02;letter-spacing:-.03em}}
[dir=rtl] h1{{letter-spacing:0;line-height:1.25;font-size:72px}}
h1 em{{font-style:normal;color:var(--seal2)}}
.sub{{margin-top:20px;font-size:27px;line-height:1.45;color:#CDD2D9;max-width:900px}}
[dir=rtl] .sub{{line-height:1.6;font-size:25px}}
.stats{{margin-top:44px;display:grid;grid-template-columns:1.25fr 1fr;grid-template-rows:auto auto;gap:18px}}
.st{{background:rgba(255,255,255,.045);border:1px solid var(--line);border-radius:22px;padding:24px 28px}}
.st.hero{{grid-row:span 3;background:linear-gradient(160deg,rgba(172,62,51,.9),rgba(120,38,31,.9));border:none;display:flex;flex-direction:column;justify-content:flex-end}}
.num{{font-family:'Inter Display','Inter',{'Vazirmatn'};font-weight:800;font-size:40px;letter-spacing:-.02em;direction:ltr;unicode-bidi:isolate}}
[dir=rtl] .num{{font-family:'Vazirmatn','Inter';text-align:right}}
[dir=rtl] .st{{padding:18px 26px}}
[dir=rtl] .stats{{margin-top:32px}}
[dir=rtl] .tip{{margin-top:22px}}
.hero .num{{font-size:104px;line-height:1}}
.lab{{font-size:19px;color:var(--muted);margin-top:6px}}
.hero .lab{{color:#F6D9D3;font-size:25px;margin-top:12px;line-height:1.35}}
.chg{{align-self:flex-start;font-family:'Inter';direction:ltr;font-weight:700;font-size:22px;background:var(--paper);color:var(--seal);padding:8px 14px;border-radius:12px;margin-bottom:auto}}
[dir=rtl] .chg{{align-self:flex-start;font-family:'Vazirmatn'}}
.ins{{margin-top:22px;list-style:none}}
.ins li{{display:flex;gap:16px;align-items:flex-start;font-size:23px;line-height:1.4;padding:10px 0;border-top:1px solid var(--line)}}
.ins li:last-child{{border-bottom:1px solid var(--line)}}
.ins li i{{flex:0 0 12px;height:12px;margin-top:12px;background:var(--gold);transform:rotate(45deg)}}
.ins b{{color:#fff;font-weight:800}}
.tip{{margin-top:30px;background:var(--paper);color:var(--ink);border-radius:22px;padding:22px 26px;display:flex;gap:22px;align-items:flex-start}}
.tip .lbl{{flex:0 0 auto;font-size:16px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;color:#fff;background:var(--seal);padding:10px 14px;border-radius:10px;max-width:190px;line-height:1.3}}
[dir=rtl] .tip .lbl{{letter-spacing:0;font-size:19px}}
.tip p{{font-size:22px;line-height:1.45;font-weight:600}}
[dir=rtl] .tip p{{line-height:1.65}}
.foot{{margin-top:auto;padding:20px 0 34px;display:flex;justify-content:space-between;align-items:center;font-size:20px;color:var(--muted)}}
.foot b{{color:var(--paper);font-weight:600}}
.src{{font-size:16px;opacity:.75;margin-top:4px}}
.logo{{background:#fff;border-radius:16px;padding:10px 14px;box-shadow:0 8px 24px rgba(0,0,0,.35)}}
.logo img{{display:block;height:112px}}
.url{{font-family:'Inter';letter-spacing:.06em;color:var(--paper);direction:ltr}}
"""

ROUTES = """<svg class="routes" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg" fill="none">
<g stroke="rgba(244,238,228,.10)" stroke-width="1.2">
<path d="M-40 420 C 260 300, 520 330, 760 210 S 1080 120, 1140 160"/>
<path d="M-40 520 C 300 440, 560 470, 820 330 S 1060 260, 1140 300"/>
<path d="M-40 640 C 340 590, 620 600, 880 470 S 1080 420, 1140 440"/>
</g>
<g fill="rgba(208,96,79,.55)"><circle cx="760" cy="210" r="5"/><circle cx="820" cy="330" r="5"/><circle cx="880" cy="470" r="5"/></g>
</svg>"""

def page(c):
    stats = c["stats"]
    hero = stats[0]
    rest = "".join(f'<div class="st"><div class="num">{n}</div><div class="lab">{l}</div></div>' for n,l,_ in stats[1:])
    ins = "".join(f"<li><i></i><span>{x}</span></li>" for x in c["ins"])
    return f"""<!doctype html><html dir="{c['dir']}"><head><meta charset="utf-8"><style>{CSS}
body{{font-family:{c['body']}}} h1{{font-family:{c['font']}}}</style></head>
<body><div class="bg"></div>{ROUTES}<div class="wrap">
<div class="top"><div class="logo"><img src="file://{ROOT}/brand/linkwin-logo-original-cropped.png"></div><div class="live">MARKET BRIEF</div></div>
<div class="kicker">{c['kicker']}</div>
<h1>{c['h1']}</h1>
<p class="sub">{c['sub']}</p>
<div class="stats">
 <div class="st hero"><div class="num">{hero[0]}</div><div class="lab">{hero[1]}</div></div>
 {rest}
</div>
<div class="tip"><span class="lbl">{c['lbl']}</span><p>{c['tip']}</p></div>
<div class="foot"><div><b>{c['foot']}</b><div class="src">{c['src']}</div></div><span class="url">linkwinco.com</span></div>
</div></body></html>"""

os.makedirs(f"{ROOT}/templates", exist_ok=True)
for k, c in L.items():
    p = f"{ROOT}/templates/2026-11-06-canton-{k}.html"
    open(p, "w").write(page(c))
    subprocess.run([sys.executable, f"{ROOT}/render.py", p, f"{ROOT}/posts/2026-11-06-canton-fair-{k}.jpg"], check=True)
print("ok")
