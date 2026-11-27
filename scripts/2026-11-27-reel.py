#!/usr/bin/env python3
"""2026-11-27 — Reel "تجارت چین و ایران در ۶ قاب" (PERSIAN, 21.6 s; one-off override OVERRIDES.md 2026-11-27).

Creative brief
- Art direction: "Saffron Route" — Persian geometric data-viz meets Chinese-modern flat colour fields. An eight-point star
  (two interlaced squares, the classic Persian khatam/girih motif, used as pure geometry) is the recurring device: drawn
  outline in the hook, a tessellated star-tile wave as the transition, star-shaped photo masks, and the end-card frame.
  Full-bleed colour fields switch per scene (pomegranate night → saffron → deep turquoise → pomegranate), no glass, no grids,
  no paper, no cobalt, no blueprint.
- Palette (new): pomegranate night #22090F, garnet #4A1220, saffron #F2B035, turquoise #38C6B8, deep teal #0B3F44, rose-cream #F8EADF.
- Type (new pairing): Lalezar (Persian display) + Vazirmatn 400/800 (Persian text, Persian digits); Unbounded for linkwinco.com only.
- Motion: stroke-drawn rotating star, rolling Persian-digit counter, RTL ink-sweep line reveals (clip-path right→left, the
  reading direction), spring-grown 76/24 columns, staggered RTL row entries with proportional bars, star-masked photo pops
  with counter-rotation, vertical route draw with travelling container token, lattice parallax; 60 fps rendered → 30 fps
  with 2-frame motion blur; temporal film grain in encode.
- Transitions (none used in the last 7 videos): star-tile wave (s1→s2, s5→s6), column-to-field morph (s2→s3),
  horizontal RTL push (s3→s4), saffron line-wipe that becomes the route line (s4→s5).
- Music: scripts/2026-11-27-reel-music.py — original Silk Road chamber fusion, 100 BPM, D Hijaz: hammered dulcimer
  (santur-like) 16ths, koto plucks, shakuhachi/ney-like flute, cello + contrabass drone, bongo/conga/tambourine.
  Cuts on bar / half-bar lines (2.4 s / 1.2 s).
- Structure (21.6 s = 9 bars): hook number (2 bars) → 76/24 split (1.5) → China→Iran goods (1.5) → Iran→China goods (1.5)
  → rail route (1.5) → end card (1).
- Facts: GACC "(2) Imports and Exports by Country (Region), 9.2026" (27 Oct 2026): Iran Jan–Sep total US$3,327.0 m,
  China exports 2,538.0 m (76 %), imports 789.0 m (24 %). ChinaData (GACC data, Jan–Oct 2026): HS84 $534M, HS87 $434M,
  HS85 $429M; HS3901 $287M, HS2601 $227M, HS0802 nuts $41.8M, HS0910 ginger/saffron/turmeric/spices $22.6M.
  Asia-Plus 11 Sep 2026 (Uztemirjulcontainer): block train via Khorgos–Kazakhstan–Uzbekistan–Turkmenistan–Sarakhs–Tehran,
  >6,000 km, ~14–16 days.
- Photos (Wikimedia Commons): iran-trade-iron-ore-pellets-kiruna.jpg (JIP, CC BY-SA 3.0, illustrative), iran-trade-pistachios.jpg
  (Amin, CC BY-SA 4.0), iran-trade-saffron-threads.jpg (Rainer Zenz, public domain).
- Safe zones: text y 240–1590, x 80–930.
- Logo: tools/linkwin_mark.py signature, seal tone-on-tone saffron + rose-cream wordmarks, inside a hairline star frame.
- PRC compliance: neutral commercial data (Chinese official customs), no y/y framing, no flags, no maps/borders (abstract
  vertical route line), no politics/religion/leaders/military; the star is geometric ornament only.
usage: python3 scripts/2026-11-27-reel.py [--preview t1,t2,...]
"""
import os, sys, subprocess, time, shutil
from multiprocessing import Process
from PIL import Image
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from linkwin_mark import MARK_CSS, signature
OUT = os.path.join(ROOT, "posts", "2026-11-27", "reel")
WORK = "/tmp/reel27"
FPS_R, FPS = 60, 30
BAR = 2.4
DUR = 9 * BAR
SLUG = "2026-11-27-reel-china-iran-trade-fa"

def star_pts(R=50, cx=50, cy=50):
    import math
    r = R * math.cos(math.pi / 4) / math.cos(math.pi / 8)
    pts = []
    for k in range(16):
        a = -math.pi / 2 + k * math.pi / 8
        rr = R if k % 2 == 0 else r
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    return pts
SP = star_pts()
STAR_CLIP = "polygon(" + ",".join(f"{x:.3f}% {y:.3f}%" for x, y in SP) + ")"
STAR_PATH = "M" + " L".join(f"{x:.3f} {y:.3f}" for x, y in SP) + " Z"

def html():
    tiles = "".join(f'<i class="tl" data-c="{c}" data-r="{r}" style="left:{c*180-90+ (90 if r%2 else 0)}px;top:{r*160-80}px"></i>'
                    for r in range(14) for c in range(8))
    lattice = (f'<svg width="1080" height="1920" class="lat"><defs><pattern id="pt" width="120" height="120" patternUnits="userSpaceOnUse">'
               f'<path d="{STAR_PATH}" transform="translate(10 10) scale(1)" fill="none" stroke="#F2B035" stroke-width="1.1"/>'
               f'<path d="M0 60 L10 60 M110 60 L120 60 M60 0 L60 10 M60 110 L60 120" stroke="#F2B035" stroke-width="1.1"/></pattern></defs>'
               f'<rect x="-240" y="-240" width="1560" height="2400" fill="url(#pt)"/></svg>')
    stops = [("خورگوس", "مرز چین"), ("قزاقستان", ""), ("ازبکستان", ""), ("ترکمنستان", ""), ("سرخس", "ورود به ایران"), ("تهران", "")]
    stops_html = "".join(f'<div class="stop" id="st{i}" style="top:{i*176}px"><b></b><span class="sn">{a}</span>'
                         + (f'<span class="ss">{b}</span>' if b else "") + '</div>' for i, (a, b) in enumerate(stops))
    rows_cn = [("ماشین‌آلات", 534), ("خودرو و قطعات", 434), ("تجهیزات برقی", 429)]
    rows_cn_html = "".join(f'<div class="row" id="rc{i}"><div class="rt"><span class="rn">{n}</span><span class="rv"><em data-v="{v}">۰</em> میلیون دلار</span></div><div class="rb"><i style="width:{v/534*100:.1f}%"></i></div></div>' for i, (n, v) in enumerate(rows_cn))
    chips = [("../photos/iran-trade-iron-ore-pellets-kiruna.jpg", "سنگ آهن", "۲۲۷ میلیون دلار"),
             ("../photos/iran-trade-pistachios.jpg", "مغزهای خوراکی", "۴۲ میلیون دلار"),
             ("../photos/iran-trade-saffron-threads.jpg", "زعفران و ادویه", "۲۳ میلیون دلار")]
    chips_html = "".join(f'<div class="chip" id="ch{i}"><div class="cimg" style="background-image:url(\'{p}\')"></div><div class="cl">{a}</div><div class="cv">{b}</div></div>' for i, (p, a, b) in enumerate(chips))
    return f"""<!doctype html><html lang="fa" dir="rtl"><head><meta charset="utf-8">
<link rel="stylesheet" href="../brand/fonts.css"><style>
:root{{--pn:#22090F;--gn:#4A1220;--sf:#F2B035;--tq:#38C6B8;--dt:#0B3F44;--cr:#F8EADF}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1080px;height:1920px;overflow:hidden;background:var(--pn)}}
body{{font-family:'Vazirmatn','DM Sans',sans-serif;color:var(--cr);position:relative}}
.sc{{position:absolute;inset:0;overflow:hidden;will-change:transform,opacity}}
.lat{{position:absolute;left:0;top:0;opacity:.07}}
.glow{{position:absolute;width:1400px;height:1400px;border-radius:50%;left:-160px;top:260px;
  background:radial-gradient(circle,rgba(242,176,53,.16) 0%,rgba(242,176,53,.05) 35%,rgba(34,9,15,0) 65%)}}
.sw{{display:inline-block;clip-path:inset(0 0 0 100%)}}
.kick{{font:800 34px/1.5 'Vazirmatn','DM Sans',sans-serif;color:var(--sf);letter-spacing:0}}
/* s1 */
#s1 .bigstar{{position:absolute;left:90px;top:390px;width:900px;height:900px}}
#s1 .bigstar path{{fill:none;stroke:var(--sf);stroke-width:.55;stroke-linejoin:miter}}
#s1 .bigstar .in{{stroke:var(--tq);stroke-width:.35}}
#h1k{{position:absolute;right:140px;top:262px;width:860px;text-align:right}}
#num{{position:absolute;right:80px;left:80px;top:610px;text-align:center;font:400 300px/1.05 'Lalezar','DM Sans',sans-serif;color:var(--cr);direction:rtl}}
#num .ds{{font-family:'Vazirmatn';font-weight:900;font-size:.62em;margin:0 .03em}}
#unit{{position:absolute;left:80px;right:80px;top:950px;text-align:center;font:400 104px/1.2 'Lalezar','DM Sans',sans-serif;color:var(--sf)}}
#sub1{{position:absolute;left:80px;right:80px;top:1130px;text-align:center;font:400 44px/1.55 'Vazirmatn','DM Sans',sans-serif}}
#src1{{position:absolute;left:80px;right:80px;top:1330px;text-align:center;font:400 28px/1.5 'Vazirmatn','DM Sans',sans-serif;color:rgba(248,234,223,.66)}}
/* s2 */
#s2 .t{{position:absolute;right:140px;top:270px;width:860px;font:400 76px/1.35 'Lalezar','DM Sans',sans-serif;text-align:right}}
.col{{position:absolute;bottom:420px;width:330px;border-radius:26px 26px 0 0}}
#cA{{right:150px;background:var(--sf);height:0}}
#cB{{right:540px;background:var(--tq);height:0}}
.cap{{position:absolute;width:380px;text-align:right}}
.cap .p{{font:400 120px/1 'Lalezar','DM Sans',sans-serif}}
.cap .l{{font:800 34px/1.45 'Vazirmatn','DM Sans',sans-serif;margin-top:10px}}
.cap .v{{font:400 32px/1.45 'Vazirmatn','DM Sans',sans-serif;opacity:.85}}
#capA{{right:170px}} #capB{{right:560px}}
#capA .p{{color:var(--pn)}} #capA .l,#capA .v{{color:var(--pn)}}
#capB .p{{color:var(--tq)}}
#base{{position:absolute;left:80px;right:80px;bottom:418px;height:3px;background:rgba(248,234,223,.4)}}
#s2 .note{{position:absolute;right:140px;width:860px;bottom:330px;font:400 28px/1.5 'Vazirmatn','DM Sans',sans-serif;color:rgba(248,234,223,.66);text-align:right}}
/* s3 */
#s3{{background:var(--sf);color:var(--pn)}}
#s3 .kick{{color:var(--gn)}}
#s3 .hd{{position:absolute;right:140px;top:280px;width:860px;text-align:right}}
#s3 .ttl{{font:400 104px/1.25 'Lalezar','DM Sans',sans-serif;margin-top:6px}}
#s3 .rows{{position:absolute;right:140px;top:640px;width:860px}}
.row{{margin-bottom:96px}}
.rt{{display:flex;justify-content:space-between;align-items:baseline;gap:20px}}
.rn{{font:800 60px/1.4 'Vazirmatn','DM Sans',sans-serif}}
.rv{{font:400 36px/1.4 'Vazirmatn','DM Sans',sans-serif}} .rv em{{font:400 96px/1 'Lalezar','DM Sans',sans-serif;font-style:normal;margin-left:10px}}
.rb{{height:16px;margin-top:16px;background:rgba(74,18,32,.14);border-radius:8px;overflow:hidden;direction:rtl}}
.rb i{{display:block;height:100%;background:var(--gn);border-radius:8px;transform-origin:right center}}
#s3 .note{{position:absolute;right:140px;top:1460px;font:400 30px/1.5 'Vazirmatn','DM Sans',sans-serif;color:rgba(34,9,15,.72)}}
/* s4 */
#s4{{background:var(--dt)}}
#s4 .hd{{position:absolute;right:140px;top:280px;width:860px;text-align:right}}
#s4 .kick{{color:var(--tq)}}
#s4 .ttl{{font:400 104px/1.25 'Lalezar','DM Sans',sans-serif;margin-top:6px}}
#lead{{position:absolute;right:140px;top:600px;width:860px;text-align:right;padding:34px 40px;border-radius:28px;background:rgba(56,198,184,.14)}}
#lead .a{{font:800 36px/1.5 'Vazirmatn','DM Sans',sans-serif;color:var(--tq)}}
#lead .b{{font:400 76px/1.3 'Lalezar','DM Sans',sans-serif;margin-top:4px}}
#lead .b small{{font:400 40px/1 'Vazirmatn','DM Sans',sans-serif;margin-right:14px}}
.chips{{position:absolute;right:140px;top:930px;width:860px;display:flex;justify-content:space-between}}
.chip{{width:260px;text-align:center}}
.cimg{{width:260px;height:260px;background-size:cover;background-position:center;clip-path:{STAR_CLIP}}}
#ch1 .cimg{{background-position:25% 35%}}
.cl{{font:800 34px/1.5 'Vazirmatn','DM Sans',sans-serif;margin-top:22px}}
.cv{{font:400 30px/1.5 'Vazirmatn','DM Sans',sans-serif;color:var(--tq)}}
#s4 .note{{position:absolute;right:140px;top:1440px;font:400 28px/1.5 'Vazirmatn','DM Sans',sans-serif;color:rgba(248,234,223,.7);width:860px;text-align:right}}
/* s5 */
#s5 .hd{{position:absolute;right:140px;top:270px;width:860px;text-align:right}}
#s5 .ttl{{font:400 92px/1.25 'Lalezar','DM Sans',sans-serif;margin-top:4px}}
#rline{{position:absolute;right:210px;top:560px;width:4px;height:880px;background:rgba(248,234,223,.16)}}
#rfill{{position:absolute;right:0;top:0;width:4px;height:0;background:var(--sf)}}
#stops{{position:absolute;right:196px;top:560px;width:600px;height:900px}}
.stop{{position:absolute;right:0;display:flex;align-items:center;gap:26px;transform:translateY(-50%)}}
.stop b{{width:32px;height:32px;border-radius:50%;background:var(--pn);border:5px solid var(--tq);flex:none}}
#st0 b,#st5 b{{border-color:var(--sf);background:var(--sf)}}
.sn{{font:800 42px/1.4 'Vazirmatn','DM Sans',sans-serif}}
.ss{{font:400 28px/1.4 'Vazirmatn','DM Sans',sans-serif;color:rgba(248,234,223,.66)}}
#tok{{position:absolute;right:194px;top:560px;width:36px;height:24px;margin-top:-12px;background:var(--cr);border-radius:4px;box-shadow:0 0 30px rgba(242,176,53,.7)}}
#facts{{position:absolute;left:80px;top:720px;width:360px;text-align:left;direction:rtl}}
.fk{{margin-bottom:56px;text-align:right}}
.fk .n{{font:400 92px/1.1 'Lalezar','DM Sans',sans-serif;color:var(--sf)}}
.fk .l{{font:400 32px/1.45 'Vazirmatn','DM Sans',sans-serif}}
#tip5{{position:absolute;right:140px;top:1480px;width:860px;text-align:right;font:400 32px/1.6 'Vazirmatn','DM Sans',sans-serif;padding-right:24px;border-right:5px solid var(--tq)}}
#lw{{position:absolute;left:0;top:0;height:6px;width:0;background:var(--sf)}}
/* s6 */
#s6{{background:var(--gn)}}
#s6 .frame{{position:absolute;left:140px;top:420px;width:800px;height:800px}}
#s6 .frame path{{fill:none;stroke:var(--sf);stroke-width:.3}}
#endc{{position:absolute;left:80px;right:80px;top:640px;display:flex;flex-direction:column;align-items:center;gap:40px}}
#e1{{font:400 64px/1.4 'Lalezar','DM Sans',sans-serif;text-align:center}}
#eurl{{font:500 46px/1 'Unbounded',sans-serif;color:var(--sf);direction:ltr;letter-spacing:.01em}}
#credit{{position:absolute;left:80px;right:80px;top:1400px;text-align:center;font:400 24px/1.6 'Vazirmatn','DM Sans',sans-serif;color:rgba(248,234,223,.6)}}
#endc .lw-sig{{--lw-sig-h:118px;--lw-seal:#F2B035;--lw-ink:#F8EADF;direction:ltr}}
/* tiles */
#tiles{{position:absolute;inset:0;pointer-events:none;z-index:50}}
.tl{{position:absolute;width:260px;height:260px;margin:-40px 0 0 -40px;background:var(--gn);clip-path:{STAR_CLIP};transform:scale(0)}}
#morph{{position:absolute;z-index:40;background:var(--sf);display:none}}
__MARKCSS__
</style></head><body>
<div class="sc" id="bgl">{lattice}<div class="glow"></div></div>
<div class="sc" id="s1">
 <svg class="bigstar" viewBox="0 0 100 100"><path id="bs" d="{STAR_PATH}"/><path class="in" id="bs2" d="{STAR_PATH}" transform="translate(50 50) scale(.62) translate(-50 -50)"/></svg>
 <div id="h1k" class="kick"><span class="sw" id="k1">چین ⇄ ایران · ۹ ماه نخست ۲۰۲۶</span></div>
 <div id="num">۰</div>
 <div id="unit"><span class="sw" id="u1">میلیارد دلار</span></div>
 <div id="sub1"><span class="sw" id="sb1">تجارت کالایی دو کشور، ژانویه تا سپتامبر</span></div>
 <div id="src1"><span class="sw" id="sr1">منبع: گمرک چین (<bdi dir=ltr>GACC</bdi>)، ۲۷ اکتبر ۲۰۲۶</span></div>
</div>
<div class="sc" id="s2">
 <div class="t"><span class="sw" id="t2a">سهم هر طرف</span><br><span class="sw" id="t2b" style="color:var(--sf)">از این ۳٫۳۳ میلیارد</span></div>
 <div class="col" id="cA"></div><div class="col" id="cB"></div><div id="base"></div>
 <div class="cap" id="capA"><div class="p">٪۷۶</div><div class="l">از چین به ایران</div><div class="v">۲٫۵۴ میلیارد دلار</div></div>
 <div class="cap" id="capB"><div class="p">٪۲۴</div><div class="l">از ایران به چین</div><div class="v">۰٫۷۹ میلیارد دلار</div></div>
 <div class="note" id="n2">ژانویه تا سپتامبر ۲۰۲۶ · گمرک چین</div>
</div>
<div class="sc" id="s3">
 <div class="hd"><div class="kick" id="k3">ژانویه تا اکتبر ۲۰۲۶</div><div class="ttl"><span class="sw" id="t3">از چین به ایران</span></div></div>
 <div class="rows">{rows_cn_html}</div>
 <div class="note" id="n3">این سه گروه: ۵۱٪ صادرات چین به ایران</div>
</div>
<div class="sc" id="s4">
 <div class="hd"><div class="kick" id="k4">ژانویه تا اکتبر ۲۰۲۶</div><div class="ttl"><span class="sw" id="t4">از ایران به چین</span></div></div>
 <div id="lead"><div class="a">در صدر فهرست</div><div class="b">پلی‌اتیلن<small>۲۸۷ میلیون دلار</small></div></div>
 <div class="chips">{chips_html}</div>
 <div class="note" id="n4">عکس‌ها: <bdi dir=ltr>JIP, CC BY-SA 3.0 · Amin, CC BY-SA 4.0 · Rainer Zenz, PD</bdi> (ویکی‌مدیا)</div>
</div>
<div class="sc" id="s5">
 <div class="hd"><div class="kick" id="k5">مسیر ریلی از آسیای مرکزی</div><div class="ttl"><span class="sw" id="t5">از خورگوس تا تهران</span></div></div>
 <div id="rline"><div id="rfill"></div></div><div id="stops">{stops_html}</div><div id="tok"></div>
 <div id="facts"><div class="fk" id="f1"><div class="n">۶٬۰۰۰+</div><div class="l">کیلومتر</div></div>
  <div class="fk" id="f2"><div class="n">۱۴–۱۶</div><div class="l">روز طبق برنامه</div></div>
  <div class="fk" id="f3"><div class="l" style="font-size:28px;opacity:.75">نخستین قطار بلوکی این مسیر، سپتامبر ۲۰۲۶ · <bdi dir=ltr>Asia-Plus</bdi></div></div></div>
 <div id="tip5">زمان واقعی حمل را پیش از قیمت‌دهی با فورواردر خود تأیید کنید.</div>
</div>
<div class="sc" id="s6">
 <svg class="frame" viewBox="0 0 100 100"><path id="fr" d="{STAR_PATH}"/></svg>
 <div id="endc">{signature()}<div id="e1">تأمین کالا از چین، با لینک‌وین</div><div id="eurl">linkwinco.com</div></div>
 <div id="credit">داده: گمرک چین (<bdi dir=ltr>GACC</bdi>) · <bdi dir=ltr>ChinaData</bdi> · <bdi dir=ltr>Asia-Plus</bdi> · موسیقی: ساخته‌شده برای لینک‌وین</div>
</div>
<div class="sc" id="lwrap" style="z-index:45;pointer-events:none"><div id="lw"></div></div>
<div id="morph"></div>
<div id="tiles">{tiles}</div>
<script>
const BAR={BAR};
const C=x=>Math.max(0,Math.min(1,x));
const seg=(t,a,b)=>C((t-a)/(b-a));
const eo=x=>1-Math.pow(1-x,3), eio=x=>x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2, eo5=x=>1-Math.pow(1-x,5);
const spring=x=>x<=0?0:x>=1?1:1-Math.exp(-6.5*x)*Math.cos(9.5*x)*(1-x*.0)+0*(x);
const back=x=>{{const c1=1.5,c3=c1+1;return 1+c3*Math.pow(x-1,3)+c1*Math.pow(x-1,2)}};
const fa=s=>String(s).replace(/[0-9]/g,d=>'۰۱۲۳۴۵۶۷۸۹'[d]).replace('.','٫');
const $=id=>document.getElementById(id);
const lerp=(a,b,x)=>a+(b-a)*x;
function sweep(id,t,a,d=.5){{const x=eo(seg(t,a,a+d));$(id).style.clipPath=`inset(0 0 0 ${{(1-x)*100}}%)`;}}
function show(id,on){{$(id).style.visibility=on?'visible':'hidden'}}
function fadeUp(el,t,a,d=.45,dy=40){{const x=eo(seg(t,a,a+d));el.style.opacity=x;el.style.transform=`translateY(${{(1-x)*dy}}px)`}}
const tiles=[...document.querySelectorAll('.tl')];
const PLEN=(()=>{{return document.getElementById('bs').getTotalLength()}})();
function tileWave(t,mid,dir){{ // cover until mid, uncover after
  const d=.36;
  tiles.forEach(e=>{{const c=+e.dataset.c,r=+e.dataset.r;const k=(dir>0?(c*.6+r):(7-c)*.6+(13-r))/18*0.26;
    let s;
    if(t<mid) s=eio(seg(t,mid-d-0.26+k,mid-0.26+k+0.02)); else s=1-eio(seg(t,mid+k,mid+k+d));
    e.style.transform=`scale(${{s*1.62}}) rotate(${{(1-s)*45}}deg)`;}});
}}
function render(t){{
  // lattice parallax
  $('bgl').firstElementChild.style.transform=`translate(${{-t*6}}px,${{-t*14}}px)`;
  const T1=2*BAR, T2=T1+1.5*BAR, T3=T2+1.5*BAR, T4=T3+1.5*BAR, T5=T4+1.5*BAR;
  ['s1','s2','s3','s4','s5','s6'].forEach(s=>show(s,false));
  $('bgl').style.visibility=(t<T2+.01||(t>=T4-.3&&t<T5+.01))?'visible':'hidden';
  // tiles
  tiles.forEach(e=>e.style.transform='scale(0)');
  if(t>T1-.75&&t<T1+.75) tileWave(t,T1,1);
  if(t>T5-.75&&t<T5+.75) tileWave(t,T5,-1);
  $('morph').style.display='none';
  // ---------- S1
  if(t<T1){{show('s1',true);
    const x=.3+.7*eo(seg(t,0,1.4)); $('bs').style.strokeDasharray=PLEN; $('bs').style.strokeDashoffset=PLEN*(1-x);
    $('bs2').style.strokeDasharray=PLEN; $('bs2').style.strokeDashoffset=PLEN*(1-eo(seg(t,.3,1.9)));
    document.querySelector('#s1 .bigstar').style.transform=`rotate(${{-12+t*5}}deg) scale(${{lerp(.94,1.04,eio(seg(t,0,T1)))}})`;
    $('k1').style.clipPath='inset(0 0 0 0)';
    const tq=Math.floor(t*30+1e-6)/30; const v=3.33*eo5(seg(tq,0.05,1.5)); $('num').innerHTML=fa(v.toFixed(2)).replace('٫','<span class="ds">٫</span>');
    $('num').style.transform=`scale(${{lerp(.86,1,eo(seg(t,0,.7)))}})`; $('num').style.opacity=1;
    $('u1').style.clipPath='inset(0 0 0 0)'; sweep('sb1',t,BAR*.5+.3,.6); sweep('sr1',t,BAR,.6);
  }}
  // ---------- S2
  if(t>=T1&&t<T2){{show('s2',true); const a=T1+.2;
    sweep('t2a',t,a,.45); sweep('t2b',t,a+.25,.5);
    const hA=880*0.763, hB=880*0.237;
    const gA=spring(seg(t,a+.25,a+1.35)), gB=spring(seg(t,a+.55,a+1.6));
    $('cA').style.height=(hA*gA)+'px'; $('cB').style.height=(hB*gB)+'px';
    const capA=$('capA'), capB=$('capB');
    capA.style.top=(1920-420-hA*gA+30)+'px'; capA.style.opacity=eo(seg(t,a+.7,a+1.1));
    capB.style.top=(1920-420-hB*gB-290)+'px'; capB.style.opacity=eo(seg(t,a+.9,a+1.3));
    fadeUp($('n2'),t,a+1.2,.4,20);
    // morph: saffron column grows to full field before cut
    const m=eio(seg(t,T2-.55,T2));
    if(m>0){{const M=$('morph');M.style.display='block';
      const L0=1080-150-330, T0=1920-420-hA, W0=330, H0=hA;
      M.style.left=lerp(L0,0,m)+'px'; M.style.top=lerp(T0,0,m)+'px'; M.style.width=lerp(W0,1080,m)+'px'; M.style.height=lerp(H0,1920,m)+'px';
      M.style.borderRadius=lerp(26,0,m)+'px '+lerp(26,0,m)+'px 0 0';}}
  }}
  // ---------- S3 / S4 push
  const P=eio(seg(t,T3-.2,T3+.4)); // push progress
  if(t>=T2&&t<T3+.4){{show('s3',true); const a=T2;
    $('s3').style.transform=`translateX(${{P*1080}}px)`;
    $('k3').style.opacity=eo(seg(t,a+.1,a+.4)); sweep('t3',t,a+.05,.5);
    [0,1,2].forEach(i=>{{const r=$('rc'+i);const st=a+.35+i*.3; const x=eo(seg(t,st,st+.5));
      r.style.opacity=x; r.style.transform=`translateX(${{-(1-x)*-80}}px)`;
      const em=r.querySelector('em'); em.textContent=fa(Math.round(+em.dataset.v*eo5(seg(Math.floor(t*30+1e-6)/30,st,st+.9))));
      r.querySelector('.rb i').style.transform=`scaleX(${{eo5(seg(t,st+.1,st+1.0))}})`;}});
    fadeUp($('n3'),t,a+1.4,.4,16);
  }}
  if(t>=T3-.2&&t<T4){{show('s4',true); const a=T3;
    $('s4').style.transform=`translateX(${{(P-1)*1080}}px)`;
    $('k4').style.opacity=eo(seg(t,a+.1,a+.4)); sweep('t4',t,a+.1,.5);
    fadeUp($('lead'),t,a+.3,.45,30);
    [0,1,2].forEach(i=>{{const c=$('ch'+i);const st=a+.55+i*.24; const x=seg(t,st,st+.6);
      const img=c.querySelector('.cimg'); const s=back(C(x));
      img.style.transform=`scale(${{x<=0?0:s}}) rotate(${{(1-eo(x))*-35}}deg)`;
      img.style.backgroundSize=`${{lerp(150,118,eo(seg(t,st,a+3.6)))}}%`;
      c.querySelector('.cl').style.opacity=eo(seg(t,st+.3,st+.6)); c.querySelector('.cv').style.opacity=eo(seg(t,st+.4,st+.7));}});
    fadeUp($('n4'),t,a+1.4,.4,12);
    // line wipe out: s4 slides up as saffron line sweeps
    const w=eio(seg(t,T4-.5,T4-.05));
    if(w>0){{$('lw').style.width=(w*1080)+'px';$('lw').style.left=((1-w)*1080)+'px';$('lw').style.top='1000px';$('lw').style.opacity=1;
      const up=eio(seg(t,T4-.3,T4)); $('s4').style.clipPath=`inset(0 0 ${{up*100}}% 0)`; }} else {{$('s4').style.clipPath='none';$('lw').style.width='0px'}}
  }}
  // ---------- S5
  if(t>=T4-.3&&t<T5){{show('s5',true); const a=T4;
    if(t<T4){{const up=eio(seg(t,T4-.3,T4)); $('s5').style.clipPath=`inset(${{(1-up)*100}}% 0 0 0)`;}} else $('s5').style.clipPath='none';
    // the wipe line travels to become the route line
    if(t>=T4-.05&&t<T4+.3){{const L=$('lw');L.style.left='0px';L.style.width='1080px';L.style.top='1000px';L.style.opacity=1-eo(seg(t,T4-.05,T4+.3));}}
    else if(t>=T4+.3) $('lw').style.width='0px';
    $('k5').style.opacity=eo(seg(t,a+.05,a+.35)); sweep('t5',t,a+.1,.5);
    const d=eio(seg(t,a+.3,a+2.6)); $('rfill').style.height=(880*d)+'px';
    $('tok').style.top=(560+880*d)+'px'; $('tok').style.opacity=seg(t,a+.3,a+.45);
    [0,1,2,3,4,5].forEach(i=>{{const e=$('st'+i);const k=i/5; const x=eo(seg(d,k-.02,k+.08)); e.style.opacity=i==0?eo(seg(t,a+.2,a+.5)):x;
      e.querySelector('b').style.transform=`scale(${{i==0?1:lerp(.3,1,back(C(seg(d,k-.02,k+.06))))}})`;}});
    fadeUp($('f1'),t,a+.6,.45,30); fadeUp($('f2'),t,a+1.0,.45,30); fadeUp($('f3'),t,a+1.4,.45,20);
    fadeUp($('tip5'),t,a+1.9,.45,20);
  }}
  // ---------- S6
  if(t>=T5){{show('s6',true); const a=T5;
    const fr=$('fr'); fr.style.strokeDasharray=PLEN; fr.style.strokeDashoffset=PLEN*(1-eo(seg(t,a+.1,a+1.5)));
    document.querySelector('#s6 .frame').style.transform=`rotate(${{lerp(-22.5,0,eo(seg(t,a,a+1.8)))}}deg)`;
    const sg=document.querySelector('.lw-sig'); const x=eo(seg(t,a+.25,a+.8)); sg.style.opacity=x; sg.style.transform=`scale(${{lerp(.9,1,x)}})`;
    fadeUp($('e1'),t,a+.5,.5,24); fadeUp($('eurl'),t,a+.7,.5,24); $('credit').style.opacity=eo(seg(t,a+.9,a+1.3));
  }}
}}
render(0);
</script></body></html>""".replace("__MARKCSS__", MARK_CSS)

def render_frames(idx_list, wid, tpl, fdir):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=os.environ.get("CHROME", "/usr/bin/google-chrome"),
                              args=["--font-render-hinting=none", "--force-color-profile=srgb"])
        pg = b.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
        pg.goto("file://" + tpl, wait_until="networkidle"); pg.evaluate("document.fonts.ready.then(()=>true)"); pg.wait_for_timeout(500)
        t0 = time.time()
        for n, f in enumerate(idx_list):
            pg.evaluate(f"render({f / FPS_R})")
            pg.screenshot(path=os.path.join(fdir, f"f{f:05d}.png"))
            if n % 100 == 0: print(f"w{wid} {n}/{len(idx_list)} {time.time()-t0:.0f}s", flush=True)
        b.close()

SAFE_JS = """(()=>{const o=[];document.querySelectorAll('.kick,.sw,#num,.cap,.note,.rn,.rv,#lead,.cl,.cv,.sn,.ss,.fk,#tip5,#e1,#eurl,#credit,.lw-sig').forEach(e=>{let v=e,op=1;while(v&&v.nodeType==1){const s=getComputedStyle(v);if(s.display=='none'||s.visibility=='hidden'){op=0;break}op*=+s.opacity;v=v.parentElement}if(op<.05)return;const r=e.getBoundingClientRect();if(r.width&&(r.top<220||r.bottom>1600||r.right>945||r.left<60))o.push((e.id||e.className)+':'+[r.left,r.top,r.right,r.bottom].map(Math.round))});return o})()"""

def main():
    os.makedirs(WORK, exist_ok=True)
    tpl = os.path.join(ROOT, "templates", SLUG + ".html")
    open(tpl, "w", encoding="utf-8").write(html())
    if "--preview" in sys.argv:
        from playwright.sync_api import sync_playwright
        ts = [float(x) for x in sys.argv[sys.argv.index("--preview") + 1].split(",")]
        pdir = os.path.join(WORK, "preview"); os.makedirs(pdir, exist_ok=True)
        with sync_playwright() as p:
            b = p.chromium.launch(executable_path=os.environ.get("CHROME", "/usr/bin/google-chrome"), args=["--font-render-hinting=none", "--force-color-profile=srgb"])
            pg = b.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
            pg.on("console", lambda m: print("console:", m.text)); pg.on("pageerror", lambda e: print("PAGEERROR", e))
            pg.goto("file://" + tpl, wait_until="networkidle"); pg.evaluate("document.fonts.ready.then(()=>true)"); pg.wait_for_timeout(500)
            bad = pg.evaluate("[...document.fonts].filter(f=>f.status==='error').map(f=>f.family)"); print("font errors:", bad)
            for t in ts:
                pg.evaluate(f"render({t})"); pg.screenshot(path=os.path.join(pdir, f"t{t:05.2f}.png"))
                print(t, pg.evaluate(SAFE_JS))
            b.close()
        return
    fdir = os.path.join(WORK, "frames"); shutil.rmtree(fdir, ignore_errors=True); os.makedirs(fdir)
    n = int(round(DUR * FPS_R)); W = 6
    procs = [Process(target=render_frames, args=(list(range(i, n, W)), i, tpl, fdir)) for i in range(W)]
    [p.start() for p in procs]; [p.join() for p in procs]
    silent = os.path.join(WORK, "video.mp4")
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-framerate", str(FPS_R), "-i", os.path.join(fdir, "f%05d.png"),
                    "-vf", "tmix=frames=2:weights='1 1',select='mod(n\\,2)',setpts=N/30/TB,noise=alls=3:allf=t,scale=in_range=pc:out_range=tv,format=yuv420p",
                    "-color_range", "tv", "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709",
                    "-r", "30", "-c:v", "libx264", "-preset", "slow", "-crf", "17", "-pix_fmt", "yuv420p", "-profile:v", "high", "-level", "4.1", silent], check=True)
    wav = os.path.join(WORK, "music.wav")
    mp4 = os.path.join(OUT, SLUG + ".mp4"); os.makedirs(OUT, exist_ok=True)
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", silent, "-i", wav, "-map", "0:v", "-map", "1:a",
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", "-shortest", mp4], check=True)
    cover = os.path.join(OUT, SLUG + "-cover.jpg")
    Image.open(os.path.join(fdir, f"f{int(4.2*FPS_R):05d}.png")).convert("RGB").save(cover, "JPEG", quality=92, subsampling=0, optimize=True)
    story = os.path.join(OUT, SLUG + "-story.mp4")
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", mp4, "-c:v", "libx264", "-pix_fmt", "yuv420p", "-b:v", "5M", "-maxrate", "6M",
                    "-bufsize", "10M", "-g", "30", "-c:a", "aac", "-b:a", "128k", "-ar", "44100", "-movflags", "+faststart", story], check=True)
    print(mp4, os.path.getsize(mp4) // 1024, "KB"); print(cover); print(story, os.path.getsize(story) // 1024, "KB")

if __name__ == "__main__":
    main()
