"""LinkWin daily post, 12 Nov 2026.

CREATIVE BRIEF
Concept name: "Stamped Pause" (customs-dossier still life).
Idea: China's tariff truce extension shown as an official notice lying on a manila customs folder: the 10% that
  stays is printed solid; the 24% that is paused is printed in outline and overstamped with a blue-violet rubber
  stamp "Suspended until 10 Jan 2027". Feeling: calm, procedural clarity: "here is the rule, here is the date".
Background tone: mid-light warm (manila folder ochre), not the celadon of 11 Nov or the cobalt of 10 Nov.
Palette: manila #D8C08E, cream sheet #FBF7EE, ink brown-black #241E1A, stamp ink violet-blue #3A3F9A
  (+ seal red #AC3E33 only as a hairline on the sheet header).
Composition: still life: folder tab at the top carrying the kicker, a slightly rotated cream notice sheet with a
  letterhead row, headline, two rate rows (solid 10% / outlined 24%) and a rubber stamp crossing the 24% row;
  footer printed straight onto the folder. Not a magazine cover/emblem (11 Nov), not an oversized-numeral poster
  over a line drawing (10 Nov), not a periodic tile (9 Nov).
Type: Manrope 800 headline + figures, Manrope 400/600 text (EN/RU) — a modern sans headline after three days of
  serif / condensed; Lalezar headline + figures (Persian-designed poster face, first use) with IBM Plex Sans Arabic
  text (FA/AR). Stamp lettering: Oswald (EN/RU) / Noto Kufi Arabic (FA/AR).
Imagery: none (photos/ still empty, photo sites blocked). CSS/SVG material study: paper grain, folder tab, rubber
  stamp with SVG ink-roughness filter.
Logo: A, printed seal used as the letterhead of the notice: full-colour original multiplied onto the cream sheet,
  top-right of the sheet LTR / top-left RTL (11 Nov: A on footer band bottom-left; 10 Nov: B tab top-left).
RTL plan: dir=rtl mirrors the tab, letterhead (logo moves left), rate rows and the sheet/stamp rotations;
  Persian uses Persian digits and Solar Hijri dates (18 Aban / 20 Dey 1405); Arabic Western digits in LTR isolates.
"""
import os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLUG = "2026-11-12-tariff-pause"
NN = " "

T = {
"en": dict(dir="ltr", tab="Tariff notice · 9 Nov 2026", hdr="China · imports of US origin",
  h="China extends its tariff truce with the US to 10&nbsp;January.",
  a="10%", al="Additional tariff stays in force",
  b="24%", bl="Still suspended for two more months",
  s1="SUSPENDED", s2="UNTIL 10 JAN 2027",
  note="The 24% stays paused for two more months. Special port fees on <span style=\"white-space:nowrap\">US-linked</span> ships are paused to the same date.",
  hook="LinkWin · your sourcing and trade partner in China",
  src="Source: State Council Customs Tariff Commission via Xinhua; TT News, 9 Nov 2026"),
"fa": dict(dir="rtl", tab="اطلاعیه تعرفه · ۱۸ آبان ۱۴۰۵", hdr="چین · کالاهای با مبدأ آمریکا",
  h="چین آتش‌بس تعرفه‌ای با آمریکا را تا ۲۰ دی تمدید کرد",
  a="۱۰٪", al="تعرفه اضافی همچنان اجرا می‌شود",
  b="۲۴٪", bl="دو ماه دیگر معلق ماند",
  s1="معلق", s2="تا ۲۰ دی ۱۴۰۵",
  note="تعرفه ۲۴٪ دو ماه دیگر معلق می‌ماند. عوارض ویژه بندری برای کشتی‌های مرتبط با آمریکا هم تا همین تاریخ معلق است.",
  hook="LinkWin، شریک شما در تأمین کالا و تجارت با چین",
  src="منبع: کمیسیون تعرفه گمرکی شورای دولتی چین به نقل از شین‌هوا؛ <bdi>TT News</bdi>، ۱۸ آبان ۱۴۰۵"),
"ru": dict(dir="ltr", tab="Тарифное уведомление · 9.11.2026", hdr="Китай · товары из США",
  h="Китай продлил тарифное перемирие с США до 10&nbsp;января.",
  a=f"10{NN}%", al="Дополнительная пошлина действует",
  b=f"24{NN}%", bl="Приостановлена ещё на два месяца",
  s1="ПРИОСТАНОВЛЕНО", s2="ДО 10.01.2027",
  note="Пошлина 24 % отложена ещё на два месяца. Спецсборы в портах для судов, связанных с США, тоже приостановлены до этой даты.",
  hook="LinkWin — ваш партнёр по закупкам и торговле с Китаем",
  src="Источник: Таможенно-тарифная комиссия Госсовета КНР (Синьхуа); TT News, 9.11.2026"),
"ar": dict(dir="rtl", tab="إشعار جمركي · 9 نوفمبر 2026", hdr="الصين · السلع ذات المنشأ الأمريكي",
  h="الصين تمدد هدنتها الجمركية مع أمريكا حتى <bdi dir=\"ltr\">10</bdi> يناير",
  a="10%", al="الرسوم الإضافية ما زالت سارية",
  b="24%", bl="معلّقة لشهرين إضافيين",
  s1="معلّق", s2="حتى 10 يناير 2027",
  note="تبقى رسوم <bdi dir=\"ltr\">24%</bdi> معلّقة لشهرين إضافيين، وكذلك رسوم الموانئ الخاصة على السفن المرتبطة بأمريكا حتى التاريخ نفسه.",
  hook="LinkWin شريككم في التوريد والتجارة مع الصين",
  src="المصدر: لجنة التعريفات الجمركية بمجلس الدولة الصيني عبر شينخوا؛ <bdi>TT News</bdi>، ‏9 نوفمبر 2026"),
}

CSS = r"""
:root{--man:#D8C08E;--cream:#FBF7EE;--ink:#241E1A;--stamp:#3A3F9A;--red:#AC3E33}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;overflow:hidden}
html.story,html.story body{height:1920px}
body{position:relative;color:var(--ink);font-family:'Manrope',sans-serif;
  background:
   radial-gradient(900px 700px at 30% 20%,rgba(255,240,205,.55),rgba(255,240,205,0) 70%),
   radial-gradient(1000px 900px at 85% 95%,rgba(120,86,40,.22),rgba(120,86,40,0) 70%),
   var(--man)}
.rtl body{font-family:'IBM Plex Sans Arabic','Manrope',sans-serif}
.grain{position:absolute;inset:0;opacity:.28;mix-blend-mode:multiply;pointer-events:none}
/* folder tab */
.tab{position:absolute;top:0;inset-inline-start:64px;height:var(--tabh);padding:0 40px;display:flex;align-items:flex-end;
  padding-bottom:20px;background:#E6D2A6;border-radius:0 0 18px 18px;box-shadow:0 6px 14px rgba(70,50,20,.18);
  font-weight:600;font-size:21px;letter-spacing:.16em;text-transform:uppercase;color:#4A3B26}
.rtl .tab{letter-spacing:0;font-size:24px;font-weight:600}
/* notice sheet */
.sheet{position:absolute;left:64px;right:64px;top:var(--st);background:var(--cream);
  transform:rotate(var(--rot));border-radius:4px;
  box-shadow:0 2px 0 rgba(255,255,255,.7) inset,0 30px 60px rgba(60,40,15,.28),0 6px 14px rgba(60,40,15,.18);
  padding:var(--sp) 64px var(--spb)}
.sheet:before{content:"";position:absolute;inset:0;border-radius:4px;opacity:.5;
  background:repeating-linear-gradient(0deg,rgba(36,30,26,.0) 0 47px,rgba(36,30,26,.035) 47px 48px)}
.lh{position:relative;display:flex;justify-content:space-between;align-items:center;padding-bottom:22px;
  border-bottom:2px solid var(--red)}
.lh .t{font-size:21px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:#5B4E40}
.rtl .lh .t{letter-spacing:0;font-size:25px}
.logo{height:var(--lg);mix-blend-mode:multiply;filter:brightness(1.015)}
h1{position:relative;font-family:'Manrope',sans-serif;font-weight:800;font-size:var(--h);line-height:var(--hl);
  letter-spacing:-.025em;margin-top:var(--hm);max-width:var(--hw)}
.rtl h1{font-family:'Lalezar','Manrope',sans-serif;font-weight:400;letter-spacing:0}
.rows{position:relative;margin-top:var(--rm)}
.row2{position:relative;height:var(--r2h)}
.row{display:flex;align-items:center;gap:40px;padding:var(--rp) 0;border-top:1.5px solid rgba(36,30,26,.18)}
.row:last-child{border-bottom:1.5px solid rgba(36,30,26,.18)}
.fig{font-family:'Manrope',sans-serif;font-weight:800;font-size:var(--ff);line-height:1;letter-spacing:-.04em;
  width:var(--fw);flex:none}
.rtl .fig{font-family:'Lalezar','Manrope',sans-serif;font-weight:400;letter-spacing:0;line-height:1.15}
.rtl .fig bdi,.rtl h1 bdi{font-family:'Manrope',sans-serif;font-weight:800;letter-spacing:-.03em}
.out{color:transparent;-webkit-text-stroke:2.5px var(--ink)}
.lab{font-size:var(--lf);line-height:1.35;font-weight:600;max-width:var(--lw)}
.lab small{display:block;font-weight:400;font-size:.8em;color:#6A5C4C;margin-top:4px}
.stamp{position:absolute;width:var(--sw);inset-inline-start:var(--sx);top:50%;margin-top:calc(var(--sw) * -0.24);transform:rotate(var(--srot));
  mix-blend-mode:multiply;opacity:.9}
.note{position:relative;margin-top:var(--nm);font-size:var(--nf);line-height:1.5;color:#3E342B;max-width:var(--nw)}
.rtl .note{line-height:1.7}
.foot{position:absolute;left:64px;right:64px;bottom:var(--fb);color:#3A2E20}
.fr{display:flex;justify-content:space-between;align-items:baseline;gap:30px;padding-bottom:12px;margin-bottom:12px;
  border-bottom:1.5px solid rgba(58,46,32,.35)}
.fr b{font-size:23px;font-weight:700;color:var(--ink)}
.src{font-size:20px;line-height:1.45}
.rtl .src{line-height:1.6}
.u{font-weight:800;font-size:24px;letter-spacing:.04em;color:var(--ink);font-family:'Manrope',sans-serif;white-space:nowrap}
"""

GRAIN = """<svg class="grain" xmlns="http://www.w3.org/2000/svg" width="100%" height="100%">
<filter id="g"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="3" stitchTiles="stitch"/>
<feColorMatrix values="0 0 0 0 .35  0 0 0 0 .27  0 0 0 0 .15  0 0 0 .55 0"/></filter>
<rect width="100%" height="100%" filter="url(#g)"/></svg>"""

def stamp(s1, s2, rtl, big):
    f1 = "'Noto Kufi Arabic','Oswald',sans-serif" if rtl else "'Oswald',sans-serif"
    fw1 = 900 if rtl else 700
    ls = "0" if rtl else ("4" if len(s1) < 10 else "1")
    fs1 = 96 if rtl else (82 if len(s1) < 10 else 50)
    fs2 = 40 if rtl else 36
    y1 = 132 if rtl else 128
    return f"""<svg class="stamp" viewBox="0 0 520 250" xmlns="http://www.w3.org/2000/svg">
<defs><filter id="ink" x="-5%" y="-5%" width="110%" height="110%">
 <feTurbulence type="fractalNoise" baseFrequency="1.6" numOctaves="2" seed="7" result="n"/>
 <feColorMatrix in="n" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -1.3 1.3" result="m"/>
 <feComposite in="SourceGraphic" in2="m" operator="in" result="c"/>
 <feTurbulence type="fractalNoise" baseFrequency=".035" numOctaves="2" seed="3" result="w"/>
 <feDisplacementMap in="c" in2="w" scale="5"/></filter></defs>
<g filter="url(#ink)" fill="none" stroke="#3A3F9A">
 <rect x="10" y="10" width="500" height="230" rx="22" stroke-width="9"/>
 <rect x="28" y="28" width="464" height="194" rx="12" stroke-width="3"/>
 <g fill="#3A3F9A" stroke="none" text-anchor="middle">
  <text x="260" y="{y1}" font-family="{f1}" font-weight="{fw1}" font-size="{fs1}" letter-spacing="{ls}">{s1}</text>
  <rect x="70" y="152" width="380" height="3"/>
  <text x="260" y="200" font-family="{f1}" font-weight="700" font-size="{fs2}" letter-spacing="{0 if rtl else 3}" {'direction="rtl"' if rtl else ''}>{s2}</text>
 </g>
</g></svg>"""

V = {  # feed
 "en": dict(spb="52px", sx="250px", r2h="auto", tabh="96px", st="148px", sh="900px", rot="-1.2deg", sp="48px", lg="96px", h="70px", hl="1.06", hm="38px", hw="860px",
            rm="40px", rp="26px", ff="132px", fw="300px", lf="30px", lw="520px", sw="430px", se="40px", sty="520px", srot="-9deg",
            nm="30px", nf="25px", nw="820px", fb="44px"),
 "ru": dict(spb="52px", sx="270px", r2h="auto", tabh="96px", st="148px", sh="900px", rot="-1.2deg", sp="48px", lg="96px", h="64px", hl="1.08", hm="38px", hw="880px",
            rm="40px", rp="26px", ff="124px", fw="320px", lf="29px", lw="500px", sw="420px", se="34px", sty="520px", srot="-9deg",
            nm="30px", nf="24px", nw="820px", fb="44px"),
 "fa": dict(spb="48px", sx="210px", r2h="auto", tabh="96px", st="148px", sh="900px", rot="1.2deg", sp="48px", lg="96px", h="72px", hl="1.45", hm="30px", hw="880px",
            rm="30px", rp="16px", ff="128px", fw="240px", lf="31px", lw="560px", sw="380px", se="60px", sty="540px", srot="8deg",
            nm="26px", nf="25px", nw="840px", fb="40px"),
 "ar": dict(spb="48px", sx="220px", r2h="auto", tabh="96px", st="148px", sh="900px", rot="1.2deg", sp="48px", lg="96px", h="70px", hl="1.45", hm="30px", hw="880px",
            rm="30px", rp="16px", ff="124px", fw="260px", lf="31px", lw="540px", sw="380px", se="60px", sty="540px", srot="8deg",
            nm="26px", nf="25px", nw="840px", fb="40px"),
}
VS = {  # story: nothing above 200px or below 1670px
 "en": dict(spb="56px", sx="270px", tabh="270px", st="318px", sp="52px", lg="104px", h="78px", hm="40px", rm="46px", rp="28px", ff="140px",
            fw="310px", lf="32px", lw="520px", sw="460px", nm="34px", nf="28px", fb="262px"),
 "ru": dict(spb="56px", sx="290px", tabh="270px", st="318px", sp="52px", lg="104px", h="72px", hm="40px", rm="46px", rp="28px", ff="132px",
            fw="330px", lf="31px", lw="440px", sw="460px", nm="34px", nf="27px", fb="262px"),
 "fa": dict(spb="52px", sx="240px", tabh="270px", st="318px", sp="52px", lg="104px", h="80px", hm="34px", rm="38px", rp="22px", ff="144px",
            fw="270px", lf="33px", sw="420px", nm="32px", nf="28px", fb="262px"),
 "ar": dict(spb="52px", sx="250px", tabh="270px", st="318px", sp="52px", lg="104px", h="78px", hm="34px", rm="38px", rp="22px", ff="140px",
            fw="290px", lf="33px", sw="420px", nm="32px", nf="28px", fb="262px"),
}

def page(lang, c):
    rtl = c["dir"] == "rtl"
    cls = "rtl" if rtl else "ltr"
    style = ";".join(f"--{k}:{v}" for k, v in V[lang].items())
    story = "html.story{" + ";".join(f"--{k}:{v}" for k, v in VS[lang].items()) + "}"
    iso = (lambda s: f'<bdi dir="ltr">{s}</bdi>') if lang == "ar" else (lambda s: s)
    return f"""<!doctype html><html lang="{lang}" dir="{c['dir']}" class="{cls}"><head><meta charset="utf-8">
<link rel="stylesheet" href="../brand/fonts.css"><style>{CSS}html{{{style}}}{story}</style></head><body>
{GRAIN}
<div class="tab">{c['tab']}</div>
<div class="sheet">
 <div class="lh"><span class="t">{c['hdr']}</span><img class="logo" src="../brand/linkwin-logo-original-cropped.png"></div>
 <h1>{c['h']}</h1>
 <div class="rows">
  <div class="row"><div class="fig">{iso(c['a'])}</div><div class="lab">{c['al']}</div></div>
  <div class="row row2"><div class="fig out">{iso(c['b'])}</div>{stamp(c['s1'], c['s2'], rtl, False)}</div>
 </div>
 <div class="note">{c['note']}</div>
</div>
<div class="foot"><div class="fr"><b>{c['hook']}</b><span class="u">linkwinco.com</span></div><div class="src">{c['src']}</div></div>
</body></html>"""


if __name__ == "__main__":
    langs = sys.argv[1:] or list(T)
    for lang in langs:
        c = T[lang]
        tpl = f"{ROOT}/templates/{SLUG}-{lang}.html"
        open(tpl, "w").write(page(lang, c))
        for mode, suffix in (("feed", ""), ("story", "-story")):
            subprocess.run([sys.executable, f"{ROOT}/render.py", tpl, f"{ROOT}/posts/{SLUG}-{lang}{suffix}.jpg", mode], check=True)
