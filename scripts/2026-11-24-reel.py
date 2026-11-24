#!/usr/bin/env python3
"""2026-11-24 — Reel "Letter of credit, in 5 steps" (EN, 26.7 s, trade-finance explainer).

Creative brief
- Art direction: "Glass Ledger" — glassmorphism depth over night-time financial districts (Pudong, Zhujiang New Town):
  defocused city lights, drifting aurora light (emerald + violet), frosted-glass cards floating in 2.5D perspective,
  a four-node money/document flow on a tilted glass stage that the camera orbits step by step.
- Palette (new): night #070B14, aurora emerald #3FE0B0, aurora violet #8C7BFF, frost white #F4F6FB, glass rgba(255,255,255,.08–.14).
  No cobalt/lime, no ivory/paper, no blueprint/brass/teal, no seal red except the seal.
- Type (new pairing): Syne 800/700 (display) + DM Sans 400/500/700 (text). No Oswald/Manrope/Playfair/Inter Tight/IBM Plex.
- Motion: spring (damped) card entries in z-depth, per-word focus-pull (blur → sharp) text, stroke-draw glowing paths
  with travelling glass tokens and comet trails, orbiting 3D camera between steps, countdown ring, light sweeps over glass;
  rendered at 60 fps and blended to 30 fps (2-frame shutter motion blur), film grain against banding.
  Transitions: zoom-through (push through the hook card), focus-pull rack, camera orbit/match-move between steps,
  iris reveal from the token into the twist, venetian-blind mask into the tip, pull-back + light sweep into the end card.
- Music: original neo-classical cinematic minimalism, 90 BPM, D minor → F major (scripts/2026-11-24-reel-music.py:
  FluidSynth + FluidR3_GM piano, strings, cello, contrabass, celesta, tremolo, timpani). One scene per bar (2.667 s).
- Structure (26.67 s, 10 bars): hook · title · 5 steps · twist (Art. 5) · tip · end card.
- Facts: ICC UCP 600 (library.iccwbo.org, fetched 24 Nov 2026): Art. 5 banks deal with documents and not with goods;
  Art. 14(b) each bank has a maximum of five banking days following the day of presentation to examine;
  Art. 14(c) presentation of original transport documents not later than 21 calendar days after shipment (and within expiry).
- Photos: photos/reel-pudong-night-huangpu.jpg (DvTor8303, CC0), photos/reel-zhujiang-new-town-night.jpg (钉钉, CC BY-SA 4.0),
  Wikimedia Commons; shown defocused (modified).
- Safe zones: text y 250–1600, x 72–940.
- Logo: tools/linkwin_mark.py signature (frost-white seal tone-on-tone + frost wordmarks) etched into the end-card glass.
- PRC compliance: neutral trade-finance education (ICC rules), Chinese city photos without people/politics, no maps or flags.
usage: python3 scripts/2026-11-24-reel.py [--preview t1,t2,...]
"""
import os, sys, subprocess, time, shutil
from multiprocessing import Process
from PIL import Image
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from linkwin_mark import MARK_CSS, signature
OUT = os.path.join(ROOT, "posts", "2026-11-24", "reel")
WORK = "/tmp/reel24"
FPS_R, FPS = 60, 30
B = 8 / 3
DUR = 10 * B
SLUG = "2026-11-24-reel-letter-of-credit-en"

ICON = {
 "you": '<svg viewBox="0 0 48 48"><circle cx="24" cy="16" r="8"/><path d="M8 42c2-9 8.5-13 16-13s14 4 16 13"/></svg>',
 "bank": '<svg viewBox="0 0 48 48"><path d="M6 18L24 7l18 11H6z"/><path d="M11 22v14M19 22v14M29 22v14M37 22v14M6 41h36"/></svg>',
 "ship": '<svg viewBox="0 0 48 48"><path d="M6 30h36l-5 10H11z"/><path d="M12 30V20h10v10M22 30V14h12v16"/><path d="M4 44c4 0 4-2 8-2s4 2 8 2 4-2 8-2 4 2 8 2 4-2 8-2"/></svg>',
}
STEPS = [
 ("01", "You apply", "Ask your bank to issue an L/C in your seller's favour."),
 ("02", "Your bank promises", "The L/C reaches the seller's bank: pay if the documents comply."),
 ("03", "Seller ships", "Then presents the documents, by default within 21 days of shipment."),
 ("04", "Banks check", "Each bank has up to 5 banking days to examine them."),
 ("05", "Everyone gets paid", "The seller is paid. You get the documents to collect the goods."),
]

def words(s, cls="w"):
    return " ".join(f'<span class="{cls}">{w}</span>' for w in s.split(" "))

def html():
    tiles = [("tyou", "Buyer", "You", "you"), ("tsel", "Exporter", "Seller", "ship"),
             ("tbnk", "Issuing bank", "Your bank", "bank"), ("tsbk", "Advising bank", "Seller's bank", "bank")]
    tile_html = "".join(f'<div class="tile" id="{i}"><div class="ic">{ICON[ic]}</div><div class="tl">{lab}</div><div class="tn">{nm}</div><i class="sweep"></i></div>' for i, lab, nm, ic in tiles)
    steps_html = "".join(f'<div class="step" id="s{k}"><div class="sn"><span class="m"><span class="i">{n}</span></span><span class="of">/05</span></div><div class="st"><span class="m"><span class="i">{a}</span></span></div><div class="sl">{words(b)}</div></div>' for k, (n, a, b) in enumerate(STEPS))
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<link rel="stylesheet" href="../brand/fonts.css"><style>
:root{{--night:#070B14;--em:#3FE0B0;--vi:#8C7BFF;--fr:#F4F6FB;--lw-ink:#F4F6FB;--lw-seal:#F4F6FB}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1920px;overflow:hidden;background:var(--night);color:var(--fr);font-family:'DM Sans',sans-serif}}
.layer{{position:absolute;inset:0;overflow:hidden}}
.bg{{position:absolute;inset:-80px;background-size:cover;background-position:50% 50%;will-change:transform,filter}}
#bgA{{background-image:url(../photos/reel-pudong-night-huangpu.jpg);background-position:58% 50%}}
#bgB{{background-image:url(../photos/reel-zhujiang-new-town-night.jpg);background-position:50% 40%}}
.shade{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(7,11,20,.72) 0%,rgba(7,11,20,.38) 40%,rgba(7,11,20,.55) 70%,rgba(7,11,20,.9) 100%)}}
.blob{{position:absolute;border-radius:50%;filter:blur(90px);mix-blend-mode:screen;opacity:.55}}
#b1{{width:760px;height:760px;background:radial-gradient(circle,#3FE0B0 0%,rgba(63,224,176,0) 70%)}}
#b2{{width:820px;height:820px;background:radial-gradient(circle,#8C7BFF 0%,rgba(140,123,255,0) 70%)}}
#grain{{position:absolute;inset:0;opacity:.07;mix-blend-mode:overlay;pointer-events:none}}
.glass{{background:linear-gradient(135deg,rgba(255,255,255,.16) 0%,rgba(255,255,255,.06) 55%,rgba(255,255,255,.1) 100%);
  backdrop-filter:blur(26px) saturate(150%);-webkit-backdrop-filter:blur(26px) saturate(150%);
  border:1.5px solid rgba(255,255,255,.26);box-shadow:0 30px 80px rgba(0,0,0,.35),inset 0 1px 0 rgba(255,255,255,.35);border-radius:36px;overflow:hidden}}
.sweep{{position:absolute;top:-20%;bottom:-20%;width:38%;left:-60%;background:linear-gradient(100deg,rgba(255,255,255,0),rgba(255,255,255,.22),rgba(255,255,255,0));transform:skewX(-18deg);pointer-events:none}}
.kick{{font:500 22px/1 'DM Sans';letter-spacing:.22em;text-transform:uppercase;color:rgba(244,246,251,.78);display:flex;align-items:center;gap:14px}}
.kick:before{{content:"";width:12px;height:12px;border-radius:50%;background:var(--em);box-shadow:0 0 18px var(--em)}}
.w{{display:inline-block;will-change:filter,transform,opacity}}
.m{{display:inline-block;overflow:hidden;vertical-align:top;padding-bottom:.08em}} .i{{display:inline-block}}
/* hook */
#persp{{position:absolute;inset:0;perspective:1400px}}
#hook{{position:absolute;left:72px;width:868px;top:520px;padding:64px 60px 70px;transform-origin:50% 50%}}
#hook .kick{{margin-bottom:46px}}
#hk1{{font:800 98px/1.02 'Syne';letter-spacing:-.025em}}
#hk2{{margin-top:34px;font:500 38px/1.3 'DM Sans';color:rgba(244,246,251,.86)}}
#hk2 b{{font-weight:700;color:var(--em)}}
/* title */
#title{{position:absolute;left:72px;width:868px;top:560px}}
#t1{{font:800 132px/.98 'Syne';letter-spacing:-.035em}}
#t2{{margin-top:26px;font:700 64px/1 'Syne';color:var(--em);letter-spacing:-.02em}}
#t3{{margin-top:40px;font:400 34px/1.35 'DM Sans';color:rgba(244,246,251,.85);max-width:760px}}
#lc{{position:absolute;left:72px;top:1260px;width:250px;height:150px;display:flex;align-items:center;justify-content:center;font:800 64px/1 'Syne';border-radius:28px}}
/* steps */
.step{{position:absolute;left:72px;width:868px;top:270px}}
.sn{{font:700 30px/1 'DM Sans';letter-spacing:.08em;color:var(--em);display:flex;align-items:baseline;gap:4px}}
.sn .of{{color:rgba(244,246,251,.5);font-weight:500}}
.st{{margin-top:22px;font:800 84px/1 'Syne';letter-spacing:-.03em}}
.sl{{margin-top:24px;font:400 36px/1.32 'DM Sans';color:rgba(244,246,251,.88);max-width:830px}}
#cam{{position:absolute;left:0;top:640px;width:1080px;height:1000px;perspective:1700px;perspective-origin:50% 30%}}
#stage{{position:absolute;inset:0;transform-style:preserve-3d;transform-origin:50% 55%}}
.tile{{position:absolute;width:350px;height:250px;padding:30px 32px;border-radius:30px;
  background:linear-gradient(140deg,rgba(255,255,255,.15),rgba(255,255,255,.05));border:1.5px solid rgba(255,255,255,.24);
  backdrop-filter:blur(22px) saturate(150%);box-shadow:0 26px 60px rgba(0,0,0,.4),inset 0 1px 0 rgba(255,255,255,.3);overflow:hidden}}
.tile .ic{{width:58px;height:58px}} .tile svg{{width:100%;height:100%;fill:none;stroke:currentColor;stroke-width:2.6;stroke-linejoin:round;stroke-linecap:round}}
.tile .tl{{margin-top:22px;font:500 21px/1 'DM Sans';letter-spacing:.16em;text-transform:uppercase;color:rgba(244,246,251,.62)}}
.tile .tn{{margin-top:12px;font:700 44px/1 'Syne';letter-spacing:-.02em;white-space:nowrap}}
#tyou{{left:100px;top:60px}} #tsel{{left:590px;top:60px}} #tbnk{{left:100px;top:560px}} #tsbk{{left:590px;top:560px}}
#flow{{position:absolute;left:0;top:0;width:1080px;height:1000px;overflow:visible}}
#flow path{{fill:none;stroke-linecap:round}}
.tok{{position:absolute;left:0;top:0;padding:16px 26px;border-radius:40px;font:700 28px/1 'DM Sans';white-space:nowrap;
  background:linear-gradient(135deg,rgba(255,255,255,.3),rgba(255,255,255,.1));border:1.5px solid rgba(255,255,255,.5);
  backdrop-filter:blur(14px);box-shadow:0 0 34px rgba(63,224,176,.55),0 10px 30px rgba(0,0,0,.35)}}
#ring{{position:absolute;left:0;top:0;width:200px;height:200px}}
/* twist / tip / end */
#twist,#tip,#end{{visibility:hidden}}
#twc{{position:absolute;left:72px;width:868px;top:600px;padding:66px 58px 64px}}
#twc .kick{{margin-bottom:40px}}
#tw1{{font:800 88px/1.02 'Syne';letter-spacing:-.03em}}
#tw2{{margin-top:10px;font:800 88px/1.02 'Syne';letter-spacing:-.03em;color:var(--em)}}
#tw3{{margin-top:40px;font:500 26px/1 'DM Sans';letter-spacing:.12em;text-transform:uppercase;color:rgba(244,246,251,.65)}}
#tipc{{position:absolute;left:72px;width:868px;top:560px;padding:64px 58px}}
#tip1{{font:800 72px/1.06 'Syne';letter-spacing:-.025em}}
#tip2{{margin-top:34px;font:400 36px/1.35 'DM Sans';color:rgba(244,246,251,.88)}}
#endc{{position:absolute;left:72px;width:868px;top:500px;height:860px;padding:70px 60px;display:flex;flex-direction:column}}
#e1{{font:800 96px/1.02 'Syne';letter-spacing:-.03em}}
#e1 em{{font-style:normal;color:var(--em)}}
#e2{{margin-top:30px;font:400 34px/1.35 'DM Sans';color:rgba(244,246,251,.85)}}
#ebot{{margin-top:auto;display:flex;align-items:flex-end;justify-content:space-between;padding-top:34px;border-top:1px solid rgba(255,255,255,.22)}}
#eurl{{font:700 40px/1 'Syne';letter-spacing:-.01em}}
.lw-sig{{--lw-sig-h:74px}}
#credit{{position:absolute;left:72px;top:1420px;width:868px;font:400 19px/1.5 'DM Sans';color:rgba(244,246,251,.55)}}
{MARK_CSS}
</style></head><body>
<div class="layer" id="bgL"><div class="bg" id="bgA"></div><div class="bg" id="bgB" style="opacity:0"></div><div class="shade"></div>
  <div class="blob" id="b1"></div><div class="blob" id="b2"></div></div>
<div class="layer" id="main"><div id="persp">
  <div id="hook" class="glass"><div class="kick">Trade finance, in 25 seconds</div><div id="hk1">{words("Paying a supplier you've never met?")}</div>
    <div id="hk2">{words("Let the banks hold the promise.")}</div><i class="sweep" id="hsw"></i></div>
  <div id="title"><div class="kick" id="tk">Trade finance 101</div><div style="height:40px"></div><div id="t1"><span class="m"><span class="i">Letter</span></span><br><span class="m"><span class="i">of credit</span></span></div>
    <div id="t2"><span class="m"><span class="i">in 5 steps</span></span></div><div id="t3">{words("A bank's promise to pay your seller, once the right documents arrive.")}</div></div>
  <div id="lc" class="glass">L/C</div>
</div>
  {steps_html}
  <div id="cam"><div id="stage">{tile_html}
    <svg id="flow" viewBox="0 0 1080 1000"><defs><filter id="gl" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="7"/></filter></defs><g id="paths"></g></svg>
    <svg id="ring" viewBox="0 0 200 200"><circle cx="100" cy="100" r="86" fill="none" stroke="rgba(255,255,255,.18)" stroke-width="6"/><circle id="rc" cx="100" cy="100" r="86" fill="none" stroke="#3FE0B0" stroke-width="6" stroke-linecap="round" transform="rotate(-90 100 100)" stroke-dasharray="540.35" stroke-dashoffset="540.35"/></svg>
    <div class="tok" id="tokA">Application</div><div class="tok" id="tokB">L/C</div></div></div>
</div>
<div class="layer" id="twist"><div class="bg" id="bgT" style="background-image:url(../photos/reel-zhujiang-new-town-night.jpg);background-position:50% 40%"></div><div class="shade"></div>
  <div id="twc" class="glass"><div class="kick">The twist</div><div id="tw1">{words("Banks check documents.")}</div><div id="tw2">{words("Not goods.")}</div><div id="tw3">ICC UCP 600 · Article 5</div><i class="sweep" id="twsw"></i></div></div>
<div class="layer" id="tip"><div class="bg" id="bgP" style="background-image:url(../photos/reel-zhujiang-new-town-night.jpg);background-position:50% 40%"></div><div class="shade"></div>
  <div id="tipc" class="glass"><div class="kick">Tip</div><div style="height:40px"></div><div id="tip1">{words("Make an inspection certificate one of the required documents.")}</div>
    <div id="tip2">{words("Then quality is checked before the bank pays.")}</div></div></div>
<div class="layer" id="end"><div class="bg" id="bgE" style="background-image:url(../photos/reel-pudong-night-huangpu.jpg);background-position:58% 50%"></div><div class="shade"></div>
  <div id="endc" class="glass"><div class="kick">LinkWin Trading</div><div style="height:46px"></div><div id="e1">Pay on <em>proof</em>,<br>not on trust.</div>
    <div id="e2">Sourcing from China? We help you structure the deal and the paperwork.</div>
    <div id="ebot"><span id="eurl">linkwinco.com</span>{signature()}</div><i class="sweep" id="esw"></i></div>
  <div id="credit">Source: ICC UCP 600 (Art. 5, 14). Photos: Pudong at night, DvTor8303 (CC0); Zhujiang New Town at night, 钉钉 (CC BY-SA 4.0); Wikimedia Commons, defocused.</div></div>
<svg width="0" height="0" style="position:absolute"><filter id="nz"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="SEED"/><feColorMatrix values="0 0 0 0 .5  0 0 0 0 .5  0 0 0 0 .5  0 0 0 1 0"/></filter></svg>
<svg id="grain" width="1080" height="1920"><rect width="1080" height="1920" filter="url(#nz)"/></svg>
<script>
const B=8/3, DUR=10*B;
const $=id=>document.getElementById(id), Q=s=>[...document.querySelectorAll(s)];
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x)), seg=(t,a,b)=>cl((t-a)/(b-a));
const eo=x=>x>=1?1:1-Math.pow(2,-10*x), eio=x=>x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2, ei=x=>x*x*x;
const spr=x=>x<=0?0:x>=1.6?1:1-Math.exp(-6.5*x)*Math.cos(10.5*x);
const lerp=(a,b,k)=>a+(b-a)*k;
function show(id,v){{$(id).style.visibility=v?'visible':'hidden'}}
function focusWords(sel,t,t0,stag,dur){{Q(sel).forEach((w,i)=>{{const k=eo(seg(t,t0+i*stag,t0+i*stag+dur));
  w.style.opacity=k; w.style.filter=`blur(${{(1-k)*14}}px)`; w.style.transform=`translateY(${{(1-k)*26}}px)`;}})}}
function maskIn(sel,t,t0,stag,dur,out0){{Q(sel).forEach((e,i)=>{{const k=eo(seg(t,t0+i*stag,t0+i*stag+dur));
  let y=(1-k)*110; if(out0!==undefined){{const o=eio(seg(t,out0+i*stag*.5,out0+i*stag*.5+.4)); y-=o*110}} e.style.transform=`translateY(${{y}}%)`}})}}
// tile centres in stage coords (tile 350x250)
const C={{tyou:[275,185],tsel:[765,185],tbnk:[275,685],tsbk:[765,685]}};
const PATHS=[ // step, from, to, bend
 [0,'tyou','tbnk',-70],[1,'tbnk','tsbk',70],[2,'tsel','tsbk',70],[3,'tsbk','tbnk',-70],[4,'tbnk','tsbk',0],[4,'tsbk','tsel',-70],[4,'tbnk','tyou',70]];
function edge(a,b){{ // start/end points just outside the tiles
  const [x1,y1]=C[a],[x2,y2]=C[b]; if(x1===x2) return [x1,y1+(y2>y1?135:-135),x2,y2+(y2>y1?-135:135)]; return [x1+(x2>x1?185:-185),y1,x2+(x2>x1?-185:185),y2]}}
const g=$('paths'); const P=[];
PATHS.forEach(([s,a,b,bend],i)=>{{const [x1,y1,x2,y2]=edge(a,b); const mx=(x1+x2)/2+(x1===x2?bend:0), my=(y1+y2)/2+(y1===y2?bend:0);
  const d=`M${{x1}} ${{y1}} Q${{mx}} ${{my}} ${{x2}} ${{y2}}`;
  g.insertAdjacentHTML('beforeend',`<path d="${{d}}" stroke="#3FE0B0" stroke-width="10" opacity="0" filter="url(#gl)"/><path d="${{d}}" stroke="#F4F6FB" stroke-width="3.5" opacity="0"/>`);
  const ps=g.querySelectorAll('path'); const glow=ps[ps.length-2], core=ps[ps.length-1]; const L=core.getTotalLength();
  [glow,core].forEach(p=>{{p.style.strokeDasharray=L; p.style.strokeDashoffset=L}}); P.push({{s,glow,core,L}});}});
const tileIds=['tyou','tsel','tbnk','tsbk'];
const ACTIVE=[['tyou','tbnk'],['tbnk','tsbk'],['tsel','tsbk'],['tsbk','tbnk'],['tbnk','tsbk','tsel','tyou']];
const CAMK=[ // rx, ry, tx, ty, s  per step
 [22,9,30,0,1],[24,0,0,10,1],[22,-9,-30,0,1],[28,0,0,30,1.02],[18,0,0,0,.97]];
function tokenAt(el,pi,k,label){{const p=P[pi]; const pt=p.core.getPointAtLength(p.L*k); el.textContent=label;
  const w=el.offsetWidth,h=el.offsetHeight; el.style.transform=`translate(${{pt.x-w/2}}px,${{pt.y-h/2}}px) translateZ(40px)`; return pt}}
function render(t){{
  // background drift + aurora
  const pz=1.08+.05*t/DUR; $('bgA').style.transform=`scale(${{pz}}) translate(${{-18*t/DUR*10}}px,${{-6*Math.sin(t/4)}}px)`;
  const bl=t<B?lerp(1.5,16,eio(seg(t,.9,B))):16; $('bgA').style.filter=`blur(${{bl}}px) brightness(.75) saturate(1.2)`;
  $('b1').style.transform=`translate(${{-120+220*Math.sin(t*.23)}}px,${{1080+160*Math.cos(t*.19)}}px)`;
  $('b2').style.transform=`translate(${{420+180*Math.cos(t*.21)}}px,${{-80+200*Math.sin(t*.17)}}px)`;
  // ---- hook (0..B) + zoom-through to title
  const hIn=spr(seg(t,0,1.0)*1.6); const zt=eio(seg(t,B-.55,B+.25));
  $('hook').style.visibility=t<B+.3?'visible':'hidden';
  $('hook').style.transform=`translateZ(${{lerp(-500,0,hIn)+zt*1300}}px) rotateX(${{(1-hIn)*28}}deg) rotateY(${{(1-hIn)*-10+Math.sin(t*.8)*1.2}}deg)`;
  $('hook').style.opacity=cl(seg(t,0,.25)*1)*(1-seg(t,B-.15,B+.2));
  $('hook').style.filter=`blur(${{zt*18}}px)`;
  focusWords('#hk1 .w',t,.05,.11,.5); focusWords('#hk2 .w',t,1.05,.08,.5);
  $('hsw').style.left=`${{lerp(-60,140,eio(seg(t,1.5,2.4)))}}%`;
  // ---- title (B..2B)
  const tOn=t>=B-.2&&t<2*B+.5; $('title').style.visibility=tOn?'visible':'hidden'; $('lc').style.visibility=tOn?'visible':'hidden';
  const tz=eo(seg(t,B-.2,B+.6)); $('title').style.transform=`translateZ(${{lerp(-700,0,tz)}}px)`; $('title').style.filter=`blur(${{(1-tz)*20}}px)`;
  const tout=eio(seg(t,2*B-.35,2*B+.15)); $('title').style.opacity=tz*(1-tout);
  maskIn('#title .m .i',t,B,.12,.6); focusWords('#t3 .w',t,B+.7,.05,.45); $('tk').style.opacity=seg(t,B,B+.4)*(1-tout);
  const lk=spr(seg(t,B+.9,2*B)*1.6); $('lc').style.transform=`translateY(${{(1-lk)*120}}px) rotateY(${{(1-lk)*70}}deg) scale(${{lerp(.6,1,lk)}})`; $('lc').style.opacity=cl(lk)*(1-tout);
  // ---- steps 2B..7B
  const s0=2*B, s1=7*B; const stOn=t>=s0-.3&&t<s1+.6;
  show('cam',stOn); const cin=eo(seg(t,s0-.3,s0+.9));
  const si=cl(Math.floor((t-s0)/B),0,4); const sk=(t-s0)/B-si;
  // camera: ease between step poses during first 0.9 s of each bar
  const prev=CAMK[Math.max(0,si-1)], cur=CAMK[si]; const ck=si===0?1:eio(cl(sk/.34));
  const cam=cur.map((v,j)=>lerp(prev[j],v,ck));
  const zin=lerp(-900,0,cin), rxin=lerp(55,0,cin);
  const out=eio(seg(t,s1-.1,s1+.5));
  $('stage').style.transform=`translateZ(${{zin}}px) translate(${{cam[2]}}px,${{cam[3]}}px) rotateX(${{cam[0]+rxin}}deg) rotateY(${{cam[1]}}deg) scale(${{cam[4]}})`;
  $('cam').style.opacity=cin*(1-out*.0); $('cam').style.filter=`blur(${{(1-cin)*16}}px)`;
  tileIds.forEach((id,i)=>{{const act=ACTIVE[si].includes(id); const e=$(id); const ent=spr(seg(t,s0-.2+i*.09,s0+.8+i*.09)*1.6);
    e.style.transform=`translateY(${{(1-ent)*80}}px) translateZ(${{act?30:0}}px)`; e.style.opacity=cl(ent)*(act?1:.45);
    e.style.borderColor=act?'rgba(63,224,176,.85)':'rgba(255,255,255,.22)'; e.style.boxShadow=act?'0 0 44px rgba(63,224,176,.35),0 26px 60px rgba(0,0,0,.4),inset 0 1px 0 rgba(255,255,255,.35)':'0 26px 60px rgba(0,0,0,.4),inset 0 1px 0 rgba(255,255,255,.2)';
    e.querySelector('.sweep').style.left=`${{lerp(-60,160,eio(seg(sk,.05,.5)))*(act?1:0)-(act?0:80)}}%`;}});
  // paths: draw active ones; keep previous faint
  P.forEach(p=>{{let k=0, op=0; if(p.s<si){{k=1;op=.22}} else if(p.s===si){{k=eio(seg(sk,.12,.62));op=1}}
    if(t<s0){{k=0;op=0}} [p.glow,p.core].forEach(x=>{{x.style.strokeDashoffset=p.L*(1-k); x.setAttribute('opacity',x===p.glow?op*.8:op)}})}});
  // tokens
  const ta=$('tokA'), tb=$('tokB'); ta.style.opacity=0; tb.style.opacity=0; $('ring').style.opacity=0;
  if(t>=s0&&t<s1+.6){{const mk=eio(seg(sk,.15,.75)), fade=cl(seg(sk,.1,.2))*(1-seg(sk,.93,1));
    const lab=['Application','L/C','Documents','Documents','Payment'][si]; const pi=[0,1,2,3,4][si];
    tokenAt(ta,pi,mk,lab); ta.style.opacity=fade;
    if(si===4){{ const k2=eio(seg(sk,.45,.9)); tokenAt(tb,6,k2,'Documents'); tb.style.opacity=cl(seg(sk,.45,.55))*(1-seg(sk,.95,1));
      if(sk>.5){{const k3=eio(seg(sk,.5,.92)); tokenAt(ta,5,k3,'Payment')}} }}
    if(si===3){{ const r=$('ring'); const pt=P[3].core.getPointAtLength(P[3].L*.5); r.style.transform=`translate(${{pt.x-100}}px,${{pt.y-100}}px) translateZ(30px)`;
      r.style.opacity=cl(seg(sk,.5,.62))*(1-seg(sk,.94,1)); $('rc').style.strokeDashoffset=540.35*(1-eio(seg(sk,.55,.92))) ; if(sk>.5){{ta.style.opacity=ta.style.opacity*(1-seg(sk,.5,.6))}} }}
  }}
  if(t>=s1){{ /* hold last frame of step 5 while iris opens */ }}
  // step headers (mask swap on each bar)
  STEPSN.forEach((_,k)=>{{const a=s0+k*B; const on=t>=a-.1&&t<a+B+.5; const el=$('s'+k); el.style.visibility=on?'visible':'hidden'; if(!on)return;
    const last=k===4; maskIn('#s'+k+' .m .i',t,a,.08,.55,last?undefined:a+B-.32); focusWords('#s'+k+' .sl .w',t,a+.12,.025,.32);
    const o=last?1-seg(t,s1-.1,s1+.2):1-seg(t,a+B-.25,a+B+.02); Q('#s'+k+' .sl').forEach(e=>e.style.opacity=o);}});
  // ---- twist: iris from token
  const ir=eio(seg(t,s1-.2,s1+.55)); show('twist',t>=s1-.2&&t<8*B+.6);
  if(t>=s1-.2){{ $('twist').style.clipPath=`circle(${{ir*1500}}px at 540px 1300px)`; const tz=eo(seg(t,s1,s1+.8));
    $('bgT').style.transform=`scale(${{1.18-.06*seg(t,s1,8*B)}})`; $('bgT').style.filter=`blur(${{lerp(2,8,tz)}}px) brightness(.9) saturate(1.25)`;
    $('twc').style.transform=`translateY(${{(1-spr(seg(t,s1,s1+1)*1.6))*160}}px)`; $('twc').style.opacity=cl(seg(t,s1,s1+.3));
    focusWords('#tw1 .w',t,s1+.15,.1,.45); focusWords('#tw2 .w',t,s1+.75,.12,.45); $('tw3').style.opacity=seg(t,s1+1.2,s1+1.6);
    $('twsw').style.left=`${{lerp(-60,160,eio(seg(t,s1+1.3,s1+2.1)))}}%`; }}
  // ---- tip: venetian blinds
  const t8=8*B; show('tip',t>=t8-.25&&t<9*B+.6);
  if(t>=t8-.25){{ const k=eio(seg(t,t8-.25,t8+.45)); const h=k*96; $('tip').style.webkitMaskImage=$('tip').style.maskImage=`repeating-linear-gradient(180deg,#000 0px,#000 ${{h}}px,transparent ${{h}}px,transparent 96px)`;
    $('bgP').style.transform=`scale(${{1.12+.05*seg(t,t8,9*B)}}) translateX(${{-30*seg(t,t8,9*B)}}px)`; $('bgP').style.filter='blur(10px) brightness(.8) saturate(1.25)';
    $('tipc').style.transform=`translateX(${{(1-eo(seg(t,t8-.1,t8+.6)))*-120}}px)`;
    focusWords('#tip1 .w',t,t8+.1,.06,.42); focusWords('#tip2 .w',t,t8+.9,.05,.4);}}
  // ---- end card: pull back + light sweep; fade to background at very end for the loop
  const t9=9*B; show('end',t>=t9-.3);
  if(t>=t9-.3){{ const k=eio(seg(t,t9-.3,t9+.4)); $('end').style.opacity=k;
    $('bgE').style.transform=`scale(${{lerp(1.25,1.1,eo(seg(t,t9-.3,DUR)))}})`; $('bgE').style.filter=`blur(${{lerp(24,10,k)}}px) brightness(.72) saturate(1.2)`;
    const ek=spr(seg(t,t9-.15,t9+.9)*1.6); $('endc').style.transform=`perspective(1400px) translateZ(${{lerp(-400,0,ek)}}px) rotateX(${{(1-ek)*-16}}deg)`;
    $('endc').style.opacity=cl(seg(t,t9-.2,t9+.2));
    $('esw').style.left=`${{lerp(-60,160,eio(seg(t,t9+.7,t9+1.6)))}}%`;
    const fo=seg(t,DUR-.55,DUR-.05); $('endc').style.opacity=cl(seg(t,t9-.2,t9+.2))*(1-fo); $('credit').style.opacity=seg(t,t9+.6,t9+1)*(1-fo);
    $('bgE').style.opacity=1; }}
  // hide main layer when covered
  $('main').style.visibility=(t>=s1+.6)?'hidden':'visible';
}}
const STEPSN=[0,1,2,3,4];
</script></body></html>'''.replace("SEED", "7")

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
            if n % 200 == 0: print(f"w{wid} {n}/{len(idx_list)} {time.time()-t0:.0f}s", flush=True)
        b.close()

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
            pg.goto("file://" + tpl, wait_until="networkidle"); pg.evaluate("document.fonts.ready.then(()=>true)"); pg.wait_for_timeout(500)
            bad = pg.evaluate("[...document.fonts].filter(f=>f.status==='error').map(f=>f.family)"); print("font errors:", bad)
            for t in ts:
                pg.evaluate(f"render({t})"); pg.screenshot(path=os.path.join(pdir, f"t{t:05.2f}.png"))
                print(t, pg.evaluate("""(()=>{const o=[];document.querySelectorAll('.kick,#hk1,#hk2,#t1,#t2,#t3,.step .st,.step .sl,.sn,.tile .tn,.tok,#tw1,#tw2,#tw3,#tip1,#tip2,#e1,#e2,#eurl,.lw-sig,#credit').forEach(e=>{let v=e,op=1;while(v&&v.nodeType==1){const s=getComputedStyle(v);if(s.display=='none'||s.visibility=='hidden'){op=0;break}op*=+s.opacity;v=v.parentElement}if(op<.05)return;const r=e.getBoundingClientRect();if(r.width&&(r.top<220||r.bottom>1600||r.right>945||r.left<60))o.push((e.id||e.className)+':'+[r.left,r.top,r.right,r.bottom].map(Math.round))});return o})()"""))
            b.close()
        return
    fdir = os.path.join(WORK, "frames"); shutil.rmtree(fdir, ignore_errors=True); os.makedirs(fdir)
    n = int(round(DUR * FPS_R)); W = 4
    procs = [Process(target=render_frames, args=(list(range(i, n, W)), i, tpl, fdir)) for i in range(W)]
    [p.start() for p in procs]; [p.join() for p in procs]
    silent = os.path.join(WORK, "video.mp4")
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-framerate", str(FPS_R), "-i", os.path.join(fdir, "f%05d.png"),
                    "-vf", "tmix=frames=2:weights='1 1',fps=30,scale=in_range=pc:out_range=tv,format=yuv420p",
                    "-color_range", "tv", "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709",
                    "-c:v", "libx264", "-preset", "slow", "-crf", "17", "-pix_fmt", "yuv420p", "-profile:v", "high", "-level", "4.1", silent], check=True)
    wav = os.path.join(WORK, "music.wav")
    mp4 = os.path.join(OUT, SLUG + ".mp4"); os.makedirs(OUT, exist_ok=True)
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", silent, "-i", wav, "-map", "0:v", "-map", "1:a",
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", "-shortest", mp4], check=True)
    cover = os.path.join(OUT, SLUG + "-cover.jpg")
    Image.open(os.path.join(fdir, f"f{int(1.9*FPS_R):05d}.png")).convert("RGB").save(cover, "JPEG", quality=92, subsampling=0, optimize=True)
    story = os.path.join(OUT, SLUG + "-story.mp4")
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", mp4, "-c:v", "libx264", "-pix_fmt", "yuv420p", "-b:v", "5M", "-maxrate", "6M",
                    "-bufsize", "10M", "-g", "30", "-c:a", "aac", "-b:a", "128k", "-ar", "44100", "-movflags", "+faststart", story], check=True)
    print(mp4, os.path.getsize(mp4) // 1024, "KB"); print(cover); print(story, os.path.getsize(story) // 1024, "KB")

if __name__ == "__main__":
    main()
