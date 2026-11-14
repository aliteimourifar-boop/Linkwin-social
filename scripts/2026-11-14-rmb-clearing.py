"""LinkWin daily post, 14 Nov 2026 — Paying China in RMB: Indonesia's RMB clearing bank opens; Guangdong RMB settlement > RMB 10 tn.

CREATIVE BRIEF
Concept name: "Clearing Route" (light editorial ledger with a settlement route diagram).
Idea: money moving along a short, direct line. A single brass hairline route with three nodes (your bank -> RMB
  clearing bank -> supplier in China) runs across a chalk page; two ledger figures sit under it. Feeling: calm,
  precise, private-bank stationery; "the route is getting shorter".
Background tone: light (chalk #F3F0EA) after 13 Nov dark photographic blue hour; 12 Nov manila, 11 Nov celadon.
Palette: chalk #F3F0EA, aubergine ink #2E1D33, brass #A88234, muted mauve grey #6E6170; seal red #AC3E33 on the seal only.
Composition: masthead row (kicker + date, hairline) -> large serif headline -> deck -> route diagram band -> two-column
  ledger figures split by a hairline -> footer with signature. Not a photo (13 Nov), not a still life (12 Nov), not an
  emblem cover (11 Nov).
Story (9:16): same masthead, headline, route and figures recomposed vertically: route becomes a vertical line with
  nodes, figures stacked; all content between y=236 and y=1650.
Type: Playfair Display 700 headline/figures + Manrope (EN/RU); Noto Naskh Arabic 700 headline + IBM Plex Sans Arabic
  (FA/AR), Playfair for Latin digits in AR.
Imagery: none (graphic; daytime licensed photo not found in time; dark BOC Tower night shots rejected to avoid a second dark day).
Logo: "Seal signature + echo": seal #AC3E33 + hairline + wordmarks in aubergine ink, footer bottom-right LTR /
  bottom-left RTL; a 5 % aubergine echo of the seal cropped by the top-right (LTR) / top-left (RTL) canvas corner.
RTL: dir=rtl mirrors masthead, route direction (reads right-to-left), figure order and signature.

FACTS (sources fetched 14 Nov 2026)
- Xinhua, Jakarta, 13 Nov 2026: RMB clearing bank in Indonesia began operations on Thursday (12 Nov 2026), Bank of China
  designated clearing bank; 12 local and foreign banks (incl. BOC, ICBC, CCB, Bank Mandiri, BNI) are participating banks
  as appointed cross-currency dealers; businesses can now settle trade with China directly in RMB. China is Indonesia's
  largest trading partner for 13 consecutive years.
- PBOC Guangdong Branch via Guangzhou Daily (dayoo.com), 13 Nov 2026: Guangdong cross-border RMB settlement Jan–Oct 2026
  RMB 10.15 tn, +26.3% y/y, 57.8% of all cross-border receipts and payments; goods-trade RMB settlement RMB 3.1 tn,
  +30.5%, 33.4% of goods-trade receipts and payments.
"""
import os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from linkwin_mark import MARK_CSS, signature, echo
DATE = "2026-11-14"
SLUG = "rmb-clearing"

T = {
"en": dict(dir="ltr", lang="en", kicker="Payments · Cross-border RMB", date="14 Nov 2026",
  h="Settling trade with China in RMB just got easier",
  deck="Indonesia opened an RMB clearing bank this week, and Guangdong's cross-border RMB settlement topped RMB 10 trillion in ten months.",
  route=["Your bank", "RMB clearing bank", "Supplier in China"],
  figs=[("10.15", "tn yuan", "Guangdong cross-border RMB settlement, Jan–Oct 2026, +26.3% y/y"),
        ("12", "banks", "participating in Indonesia's new RMB clearing bank, open since 12 Nov")],
  hook="LinkWin · your trade partner in Hong Kong & Guangzhou",
  src="Sources: Xinhua, 13 Nov 2026; PBOC Guangdong Branch via Guangzhou Daily, 13 Nov 2026"),
"fa": dict(dir="rtl", lang="fa", kicker="پرداخت · تسویهٔ فرامرزی یوان", date="۲۳ آبان ۱۴۰۵",
  h="تسویهٔ تجارت با چین به یوان آسان‌تر شد",
  deck="اندونزی این هفته بانک تسویهٔ یوان راه انداخت و تسویهٔ فرامرزی یوان در گوانگدونگ در ده ماه از ۱۰ هزار میلیارد یوان گذشت.",
  route=["بانک شما", "بانک تسویهٔ یوان", "تأمین‌کننده در چین"],
  figs=[("۱۰٫۱۵", "هزار میلیارد یوان", "تسویهٔ فرامرزی یوان در گوانگدونگ از ژانویه تا اکتبر ۲۰۲۶، با رشد سالانهٔ ۲۶٫۳ درصد"),
        ("۱۲", "بانک", "عضو سامانهٔ تازهٔ تسویهٔ یوان در اندونزی که از ۲۱ آبان به کار افتاده است")],
  hook="LinkWin، شریک تجاری شما در هنگ‌کنگ و گوانگجو",
  src="منابع: شین‌هوا، ۲۲ آبان ۱۴۰۵؛ شعبهٔ گوانگدونگ بانک مرکزی چین به نقل از گوانگجو دیلی، ۲۲ آبان ۱۴۰۵"),
"ru": dict(dir="ltr", lang="ru", kicker="Платежи · расчёты в юанях", date="14.11.2026",
  h="Рассчитываться с Китаем в юанях стало проще",
  deck="На этой неделе в Индонезии заработал клиринговый банк по юаню, а трансграничные расчёты в юанях в Гуандуне за десять месяцев превысили 10 трлн.",
  route=["Ваш банк", "Клиринговый банк по юаню", "Поставщик в Китае"],
  figs=[("10,15", "трлн юаней", "трансграничные расчёты в юанях в Гуандуне, январь–октябрь 2026, +26,3\u00a0% г/г"),
        ("12", "банков", "участвуют в работе нового клирингового банка по юаню в Индонезии (с 12.11)")],
  hook="LinkWin — торговый партнёр в Гонконге и Гуанчжоу",
  src="Источники: Синьхуа, 13.11.2026; отделение НБК по Гуандуну (Guangzhou Daily), 13.11.2026"),
"ar": dict(dir="rtl", lang="ar", kicker="المدفوعات · التسوية باليوان", date="<bdi>14</bdi> نوفمبر <bdi>2026</bdi>",
  h="تسوية التجارة مع الصين باليوان أصبحت أسهل",
  deck="افتتحت إندونيسيا هذا الأسبوع بنك مقاصة لليوان، وتجاوزت التسويات العابرة للحدود باليوان في قوانغدونغ <bdi>10</bdi> تريليونات يوان خلال عشرة أشهر.",
  route=["بنكك", "بنك مقاصة اليوان", "المورّد في الصين"],
  figs=[("10.15", "تريليون يوان", "تسويات اليوان العابرة للحدود في قوانغدونغ، يناير–أكتوبر <bdi>2026</bdi>، بنمو <bdi dir=\"ltr\">26.3%</bdi> سنويًا"),
        ("12", "بنكًا", "تشارك في بنك مقاصة اليوان الجديد في إندونيسيا، العامل منذ <bdi>12</bdi> نوفمبر")],
  hook="LinkWin، شريكك التجاري في هونغ كونغ وقوانغتشو",
  src="المصادر: شينخوا، <bdi>13</bdi> نوفمبر <bdi>2026</bdi>؛ فرع بنك الشعب الصيني في قوانغدونغ عبر «قوانغتشو اليومية»، <bdi>13</bdi> نوفمبر <bdi>2026</bdi>"),
}
LAT_H, LAT_B = "'Playfair Display',serif", "'Manrope',sans-serif"
AR_H, AR_B = "'Noto Naskh Arabic','Playfair Display',serif", "'IBM Plex Sans Arabic','Manrope',sans-serif"
FONTS = {"en": (LAT_H, LAT_B, LAT_H), "ru": (LAT_H, LAT_B, LAT_H),
         "fa": (AR_H, AR_B, "'Noto Naskh Arabic',serif"), "ar": (AR_H, AR_B, LAT_H)}
TUNE = {"en": dict(h=84, hlh=1.08, deck=29), "ru": dict(h=78, hlh=1.1, deck=28),
        "fa": dict(h=80, hlh=1.5, deck=29), "ar": dict(h=80, hlh=1.5, deck=29)}

def html(lang):
    t = T[lang]; hf, bf, nf = FONTS[lang]; k = TUNE[lang]
    rtl = t["dir"] == "rtl"
    ls = "0" if rtl else ".16em"; tt = "none" if rtl else "uppercase"
    nodes = "".join(f'<div class="node n{i}"><i></i><span>{r}</span></div>' for i, r in enumerate(t["route"]))
    figs = "".join(f'<div class="fig"><div class="num"><b>{n}</b><em>{u}</em></div><p>{l}</p></div>' for n, u, l in t["figs"])
    start, end = ("right", "left") if rtl else ("left", "right")
    return f"""<!doctype html><html lang="{t['lang']}" dir="{t['dir']}"><head><meta charset="utf-8">
<link rel="stylesheet" href="../brand/fonts.css">
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1080px;height:1350px;overflow:hidden;background:#F3F0EA}}
body{{position:relative;font-family:{bf};color:#2E1D33;-webkit-font-smoothing:antialiased;
  --lw-ink:#2E1D33;--lw-echo:#2E1D33;--lw-echo-op:.05;--lw-echo-size:560px}}
body:before{{content:"";position:absolute;inset:0;background:radial-gradient(1200px 700px at 80% 0%,rgba(168,130,52,.10),transparent 60%),
  radial-gradient(900px 600px at 0% 100%,rgba(46,29,51,.06),transparent 60%)}}
.page{{position:absolute;inset:72px 80px 64px;display:flex;flex-direction:column}}
.mast{{display:flex;justify-content:space-between;align-items:center;padding-bottom:22px;border-bottom:1px solid rgba(46,29,51,.25);
  font:600 21px/1.2 {bf};letter-spacing:{ls};text-transform:{tt};color:#A88234}}
.mast .d{{color:#6E6170;letter-spacing:{'0' if rtl else '.08em'}}}
h1{{margin-top:56px;font:700 {k['h']}px/{k['hlh']} {hf};letter-spacing:{'0' if rtl else '-.012em'};text-wrap:balance;color:#2E1D33}}
.deck{{margin-top:30px;font:400 {k['deck']}px/1.5 {bf};color:#4A3B4E;max-width:880px}}
.route{{position:relative;display:grid;grid-template-columns:1fr 1fr 1fr;margin-top:64px}}
.route:before{{content:"";position:absolute;top:13px;{start}:calc(16.66% - 0px);{end}:16.66%;height:2px;background:linear-gradient({'270deg' if rtl else '90deg'},#A88234,#2E1D33)}}
.node{{position:relative;text-align:center}}
.node i{{display:block;margin:0 auto;width:28px;height:28px;border-radius:50%;background:#F3F0EA;border:2px solid #A88234}}
.node.n1 i{{background:#A88234;box-shadow:0 0 0 8px rgba(168,130,52,.16)}}
.node span{{display:block;margin-top:18px;font:600 22px/1.3 {bf};color:#2E1D33}}
.figs{{display:grid;grid-template-columns:1fr 1fr;margin-top:84px;border-top:1px solid rgba(46,29,51,.25)}}
.fig{{padding:34px 0 0;padding-{end}:36px}}
.fig+.fig{{border-{start}:1px solid rgba(46,29,51,.25);padding-{start}:40px;padding-{end}:0}}
.num{{display:flex;align-items:baseline;gap:14px;flex-wrap:wrap}}
.num b{{font:700 104px/1 {nf};color:#2E1D33;letter-spacing:-.01em}}
.num em{{font:600 26px/1.2 {bf};font-style:normal;color:#A88234}}
.fig p{{margin-top:20px;font:400 23px/1.5 {bf};color:#4A3B4E}}
.foot{{margin-top:auto;display:flex;align-items:center;justify-content:space-between;gap:28px;padding-top:24px;border-top:1px solid rgba(46,29,51,.25)}}
.ft{{font:400 16px/1.5 {bf};color:#6E6170;max-width:680px}}
.ft .hook{{font:600 20px/1.4 {bf};color:#2E1D33}}
.ft .url{{font:700 20px/1.4 'Manrope',sans-serif;color:#A88234;letter-spacing:.02em}}
.page>*{{position:relative;z-index:1}}
__MARKCSS__
.lw-sig{{--lw-sig-h:64px}}
html.story,html.story body{{width:1080px;height:1920px}}
html.story .page{{inset:236px 84px 262px}}
html.story h1{{margin-top:54px;font-size:{k['h']+6}px}}
html.story .deck{{margin-top:30px;font-size:{k['deck']+1}px}}
html.story .route{{margin-top:64px}}
html.story .node span{{font-size:23px}}
html.story .figs{{grid-template-columns:1fr;margin-top:60px}}
html.story .fig{{padding:30px 0 26px}}
html.story .fig+.fig{{border-{start}:0;padding-{start}:0;border-top:1px solid rgba(46,29,51,.25)}}
html.story .num b{{font-size:112px}}
html.story .fig p{{font-size:24px}}
html.story .ft{{max-width:600px}}
html.story .lw-echo{{top:560px !important;--lw-echo-op:.045}}
</style></head><body>
{echo(end, '1090px' if False else 'auto', '-150px')}
<div class="page">
  <div class="mast"><span>{t['kicker']}</span><span class="d">{t['date']}</span></div>
  <h1>{t['h']}</h1>
  <p class="deck">{t['deck']}</p>
  <div class="route">{nodes}</div>
  <div class="figs">{figs}</div>
  <div class="foot"><div class="ft"><div class="hook">{t['hook']}</div><div class="url">linkwinco.com</div><div class="src">{t['src']}</div></div>{signature()}</div>
</div></body></html>""".replace('__MARKCSS__', MARK_CSS).replace('bottom:auto;', 'top:-170px;')

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a]
    modes = [a for a in args if a in ("feed", "story")] or ["feed", "story"]
    langs = [a for a in args if a not in ("feed", "story")] or ["en", "fa", "ru", "ar"]
    for lang in langs:
        tpl = os.path.join(ROOT, "templates", f"{DATE}-{SLUG}-{lang}.html")
        open(tpl, "w", encoding="utf-8").write(html(lang))
        for mode in modes:
            suffix = "" if mode == "feed" else "-story"
            out = os.path.join(ROOT, "posts", DATE, f"{DATE}-{SLUG}-{lang}{suffix}.jpg")
            subprocess.run([sys.executable, os.path.join(ROOT, "tools", "render.py"), tpl, out, mode], check=False)
