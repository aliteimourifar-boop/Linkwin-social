#!/usr/bin/env python3
"""2026-11-23 — Reel "Can you read this code? 7202.41, decoded" (EN, 23 s, HS-code explainer).

Creative brief
- Art direction: "Swiss Kinetic" — International Typographic Style on a cobalt field: visible 6-column hairline grid,
  oversized grotesque numerals as the main graphic, monospace labels, one lime signal colour that moves like a cursor.
  Photos appear only as navy/paper DUOTONE plates (ferro-alloy specimens), revealed by a grid-column shutter.
- Palette (new): cobalt #1F35D6, ink navy #0A1033, paper #F3F2EC, signal lime #D9FF5B. No seal red, no ivory page,
  no blueprint/brass/teal.
- Type (new pairing): Inter Tight 900/700 (display) + IBM Plex Mono 500/600 (labels, codes). No Oswald/Manrope/Playfair/Space Grotesk.
- Motion: per-glyph masked slide-ups (expo-out), the code splitting into its 3 digit pairs, a lime underline cursor that
  travels between pairs, grid-column shutter reveals, a polarity flip to a paper page (zoom-through on the code),
  a centre "barn-door" split back to cobalt, count-up stats, typed mono line, grid retracting into the end card.
  Transition types used: masked line swap, split/spread, travelling cursor, column shutter, zoom-through + polarity flip,
  barn-door split, retract. All cuts on the beat (120 BPM).
- Music: original sample-based nu-jazz groove, 120 BPM (scripts/2026-11-23-reel-music.py, FluidSynth + FluidR3_GM).
- Structure (23 s): hook 0–3 · what HS is 3–5 · 72 chapter 5–7.5 · 02 heading 7.5–10 · 41 subheading 10–12.5 ·
  sibling codes list 12.5–15.5 · scale stats 15.5–18 · tip 18–20 · end card 20–23 (text fades to cobalt 22.4–23 for loop).
- Facts: WCO "What is the Harmonized System (HS)?" (wcoomd.org, fetched 23 Nov 2026): >5,000 commodity groups, six-digit
  code, used by >200 countries and economies, >98% of merchandise in international trade. WCO HS Nomenclature 2022,
  Chapter 72 (wcoomd.org PDF, fetched 23 Nov 2026): Chapter 72 Iron and steel; 72.02 Ferro-alloys; 7202.11 ferro-manganese
  >2% carbon; 7202.21 ferro-silicon >55% silicon; 7202.30 ferro-silico-manganese; 7202.41 ferro-chromium >4% carbon.
- Photos: photos/reel-ferrosilicon-lump-focalpoint.jpg, photos/reel-ferrochrome-lump-focalpoint.jpg (FocalPoint, CC BY-SA 4.0,
  Wikimedia Commons), duotone-toned (credited as modified).
- Safe zones: text y 250–1590, x 72–940.
- Logo: tools/linkwin_mark.py signature (tone-on-tone paper seal + paper wordmarks) set on the grid in the end card.
- PRC compliance: neutral customs-classification education; no maps, flags, politics, people.
usage: python3 scripts/2026-11-23-reel.py [--preview t1,t2,...]
"""
import os, sys, subprocess, time
from PIL import Image
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from linkwin_mark import MARK_CSS, signature
OUT = os.path.join(ROOT, "posts", "2026-11-23", "reel")
WORK = "/tmp/reel23"
FPS, DUR = 30, 23.0
SLUG = "2026-11-23-reel-hs-code-decoded-en"

def glyphs(s, cls="g"):
    return "".join(f'<span class="m"><span class="{cls}">{c}</span></span>' for c in s)

def html():
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<link rel="stylesheet" href="../brand/fonts.css"><style>
:root{{--co:#1F35D6;--ink:#0A1033;--pa:#F3F2EC;--li:#D9FF5B;--lw-ink:#F3F2EC;--lw-seal:#F3F2EC}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1920px;overflow:hidden;background:var(--co);color:var(--pa);font-family:'Inter Tight',sans-serif}}
.mono{{font-family:'IBM Plex Mono',monospace}}
#bg{{position:absolute;inset:0;background:var(--co)}}
#paper{{position:absolute;inset:0;background:var(--pa);transform-origin:50% 50%}}
#doorL,#doorR{{position:absolute;top:0;bottom:0;width:540px;background:var(--co)}} #doorL{{left:0}} #doorR{{right:0}}
#grid{{position:absolute;left:72px;right:140px;top:0;bottom:0;display:flex;justify-content:space-between}}
#grid i{{display:block;width:1px;height:100%;background:currentColor;opacity:.13;transform-origin:50% 0}}
.top{{position:absolute;left:72px;right:140px;top:250px;display:flex;justify-content:space-between;font:500 22px/1 'IBM Plex Mono';letter-spacing:.08em;text-transform:uppercase}}
.m{{display:inline-block;overflow:hidden;vertical-align:top}}
.g{{display:inline-block;will-change:transform}}
#head{{position:absolute;left:72px;width:860px;top:420px;font:700 76px/1.02 'Inter Tight';letter-spacing:-.03em}}
#head .ln{{display:block;overflow:hidden;padding-bottom:6px}} #head .ln span{{display:block}}
#code{{position:absolute;left:72px;top:760px;height:260px;white-space:nowrap;font:900 232px/1 'Inter Tight';letter-spacing:-.04em}}
#code .pair{{display:inline-block;position:relative}}
#code .dot{{display:inline-block}}
#cursor{{position:absolute;top:908px;height:12px;background:var(--li);left:72px;width:0}}
#sub{{position:absolute;left:72px;top:1120px;width:860px;font:500 26px/1.45 'IBM Plex Mono';color:rgba(243,242,236,.82)}}
#lvl{{position:absolute;left:72px;top:1000px;width:860px}}
#lvl .k{{font:600 24px/1 'IBM Plex Mono';letter-spacing:.1em;color:var(--li)}}
#lvl .v{{font:700 84px/1.0 'Inter Tight';letter-spacing:-.03em;margin-top:22px}}
#lvl .n{{font:500 24px/1.4 'IBM Plex Mono';margin-top:16px;color:rgba(243,242,236,.8)}}
.lv{{position:absolute;left:0;top:0;width:860px}}
#plate{{position:absolute;left:72px;top:1080px;width:868px;height:420px;overflow:hidden}}
#plate .ph{{position:absolute;inset:0;background-size:cover;background-position:50% 50%}}
#plate .sh{{position:absolute;inset:0;display:flex}} #plate .sh b{{flex:1;background:var(--co);transform-origin:50% 0}}
#pcr{{position:absolute;left:72px;top:1522px;font:500 17px/1 'IBM Plex Mono';color:rgba(243,242,236,.7)}}
/* list scene (paper) */
#list{{position:absolute;inset:0;color:var(--ink)}}
#list .t{{position:absolute;left:72px;top:330px;width:860px;font:700 80px/1.02 'Inter Tight';letter-spacing:-.03em}}
#list .t .ln{{display:block;overflow:hidden;padding-bottom:6px}} #list .t .ln span{{display:block}}
#list .hd{{position:absolute;left:72px;top:600px;font:600 24px/1 'IBM Plex Mono';letter-spacing:.1em;color:var(--co)}}
.row{{position:absolute;left:72px;width:868px;height:170px;border-top:2px solid rgba(10,16,51,.85);display:flex;flex-direction:column;justify-content:center;padding:0 26px}}
.row .c{{font:600 52px/1 'IBM Plex Mono';letter-spacing:-.01em}}
.row .d{{font:500 37px/1.2 'Inter Tight';margin-top:12px}}
.row.hl{{background:var(--co);color:var(--pa);border-top-color:var(--co)}} .row.hl .c{{color:var(--li)}}
/* stats */
#stats{{position:absolute;inset:0}}
.st{{position:absolute;left:72px;width:868px;border-top:1px solid rgba(243,242,236,.35);padding-top:18px}}
.st .n{{font:900 170px/0.95 'Inter Tight';letter-spacing:-.045em;font-variant-numeric:tabular-nums}}
.st .l{{font:500 26px/1.35 'IBM Plex Mono';margin-top:12px;color:rgba(243,242,236,.85)}}
.st .n em{{font-style:normal;color:var(--li)}}
/* tip */
#tip{{position:absolute;left:72px;top:520px;width:868px}}
#tip .a{{font:900 118px/0.98 'Inter Tight';letter-spacing:-.03em;word-spacing:.06em}}
#tip .a .ln{{display:block;overflow:hidden;padding-bottom:8px}} #tip .a .ln span{{display:block}}
#tip .b{{font:500 34px/1.5 'IBM Plex Mono';margin-top:60px;color:var(--pa);min-height:160px}}
#tip .b .caret{{display:inline-block;width:18px;height:38px;background:var(--li);vertical-align:-6px;margin-left:4px}}
#tip .tag{{display:inline-block;font:600 24px/1 'IBM Plex Mono';letter-spacing:.1em;color:var(--ink);background:var(--li);padding:10px 14px;margin-bottom:44px}}
/* end */
#end{{position:absolute;inset:0}}
#end .code{{position:absolute;left:72px;top:330px;font:600 34px/1 'IBM Plex Mono';letter-spacing:.06em;color:var(--li)}}
#end .h{{position:absolute;left:72px;top:420px;width:868px;font:900 112px/0.98 'Inter Tight';letter-spacing:-.03em;word-spacing:.08em}}
#end .h .ln{{display:block;overflow:hidden;padding-bottom:8px}} #end .h .ln span{{display:block}}
#end .eplate{{position:absolute;left:72px;top:720px;width:868px;height:330px;background:url(duo-fecr.jpg) 50% 50%/cover}}
#end .rule{{position:absolute;left:72px;top:1110px;width:868px;height:2px;background:var(--pa);transform-origin:0 50%}}
#end .sig{{position:absolute;left:72px;top:1160px}}
#end .url{{position:absolute;right:140px;top:1185px;font:700 44px/1 'Inter Tight';letter-spacing:-.01em}}
#end .src{{position:absolute;left:72px;top:1340px;width:868px;font:500 18px/1.55 'IBM Plex Mono';color:rgba(243,242,236,.72)}}
.lw-sig{{--lw-sig-h:86px}}
#fade{{position:absolute;inset:0;background:var(--co);opacity:0;pointer-events:none}}
{MARK_CSS}
</style></head><body>
<div id="bg"></div>
<div id="paper"></div>
<div id="grid">{"".join("<i></i>" for _ in range(7))}</div>
<div class="top mono" id="top"><span>HS codes, decoded</span><span id="topr">WCO · HS 2022</span></div>

<div id="s1">
  <div id="head"><span class="ln"><span id="h1a">Can you read</span></span><span class="ln"><span id="h1b">this code?</span></span></div>
  <div id="code"><span class="pair" id="p1">{glyphs("72")}</span><span class="pair" id="p2">{glyphs("02")}</span><span class="dot" id="dt">{glyphs(".")}</span><span class="pair" id="p3">{glyphs("41")}</span></div>
  <div id="cursor"></div>
  <div id="sub"></div>
  <div id="lvl">
    <div class="lv" id="l1"><div class="k">CHAPTER 72</div><div class="v">Iron and steel</div><div class="n">The first two digits: the broad family.</div></div>
    <div class="lv" id="l2"><div class="k">HEADING 72.02</div><div class="v">Ferro-alloys</div><div class="n">Four digits: the product group.</div></div>
    <div class="lv" id="l3"><div class="k">SUBHEADING 7202.41</div><div class="v">Ferro-chromium</div><div class="n">Six digits: containing by weight more than 4% of carbon.</div></div>
  </div>
  <div id="plate"><div class="ph" id="ph1" style="background-image:url(duo-fesi.jpg)"></div><div class="ph" id="ph2" style="background-image:url(duo-fecr.jpg)"></div><div class="sh" id="sh">{"".join("<b></b>" for _ in range(6))}</div></div>
  <div id="pcr"></div>
</div>

<div id="list">
  <div class="t"><span class="ln"><span id="lt1">Same heading,</span></span><span class="ln"><span id="lt2">different alloys</span></span></div>
  <div class="hd">HEADING 72.02 · FERRO-ALLOYS</div>
  <div class="row" id="r1" style="top:680px"><div class="c">7202.11</div><div class="d">Ferro-manganese, more than 2% carbon</div></div>
  <div class="row" id="r2" style="top:850px"><div class="c">7202.21</div><div class="d">Ferro-silicon, more than 55% silicon</div></div>
  <div class="row" id="r3" style="top:1020px"><div class="c">7202.30</div><div class="d">Ferro-silico-manganese</div></div>
  <div class="row hl" id="r4" style="top:1190px"><div class="c">7202.41</div><div class="d">Ferro-chromium, more than 4% carbon</div></div>
</div>
<div id="doorL"></div><div id="doorR"></div>

<div id="stats">
  <div class="st" id="st1" style="top:400px"><div class="n" id="n1">0</div><div class="l">commodity groups, each with a six-digit code</div></div>
  <div class="st" id="st2" style="top:780px"><div class="n" id="n2">0</div><div class="l">countries and economies build their tariffs on it</div></div>
  <div class="st" id="st3" style="top:1160px"><div class="n" id="n3">0</div><div class="l">of goods in world trade are classified in HS</div></div>
</div>

<div id="tip"><div class="tag">BEFORE YOU SHIP</div><div class="a"><span class="ln"><span id="ta1">After six digits,</span></span><span class="ln"><span id="ta2">codes go national.</span></span></div><div class="b" id="tb"></div></div>

<div id="end">
  <div class="code" id="ec">7202.41 = ferro-chromium</div>
  <div class="h"><span class="ln"><span id="eh1">Right code.</span></span><span class="ln"><span id="eh2">Right duty.</span></span></div>
  <div class="eplate" id="ep"></div>
  <div class="rule" id="er"></div>
  <div class="sig" id="esig">{signature()}</div>
  <div class="url" id="eurl">linkwinco.com</div>
  <div class="src" id="esrc">Sources: World Customs Organization, HS overview and HS Nomenclature 2022, Chapter 72.<br>Photos: Ferrosilicon, Ferrochrome · FocalPoint · CC BY-SA 4.0 · Wikimedia Commons (duotone).<br>Music: original, LinkWin.</div>
</div>
<div id="fade"></div>
<script>
const $=id=>document.getElementById(id);
const cl=x=>Math.max(0,Math.min(1,x));
const eo=x=>{{x=cl(x);return x===1?1:1-Math.pow(2,-10*x)}};          // expo out
const eio=x=>{{x=cl(x);return x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2}};  // cubic in-out
const ei=x=>{{x=cl(x);return x*x*x}};
const lin=(t,a,b)=>cl((t-a)/(b-a));
function vis(id,on){{$(id).style.display=on?'block':'none'}}
function lineIn(id,t,t0,d=.55,out=null){{ // masked line slide-up, optional slide-out
  let y=(1-eo((t-t0)/d))*110; if(out!==null&&t>=out) y=-eio((t-out)/.35)*110;
  $(id).style.transform=`translateY(${{y}}%)`; }}
const SUBS=[[3.0,"Harmonized System: one global language for goods,"+"<br>"+"run by the World Customs Organization."]];
function render(t){{
  // ---- page polarity ----
  const flip=eio(lin(t,12.5,13.05)), back=eio(lin(t,15.5,16.0));
  $('paper').style.opacity = (t>=12.5&&t<16.1)?1:0;
  $('paper').style.clipPath = t<13.05? `circle(${{flip*2250}}px at 800px 470px)` : 'none';
  const door=t>=15.5&&t<16.05; vis('doorL',door); vis('doorR',door);
  $('doorL').style.transform=`translateX(${{-(1-back)*540}}px)`; $('doorR').style.transform=`translateX(${{(1-back)*540}}px)`;
  const onPaper = t>=13.05 && t<15.75;
  $('grid').style.color = onPaper? '#0A1033':'#F3F2EC';
  $('top').style.color = onPaper? '#0A1033':'#F3F2EC';
  // grid draw in / retract at end
  document.querySelectorAll('#grid i').forEach((e,i)=>{{
    let s=eo((t-0.02*i)/0.7); if(t>20) s=1-eio((t-20-0.04*i)/0.6);
    e.style.transform=`scaleY(${{s}})`; e.style.transformOrigin= t>20?'50% 100%':'50% 0'; }});
  $('top').style.opacity = t>20? 1-eio((t-20)/0.4) : 1;
  $('topr').textContent = t<12.5? 'WCO · HS 2022' : (t<15.5? 'Chapter 72' : (t<18? 'Scale' : 'Tip'));
  // ---- scene 1 group (0-12.5) ----
  const s1 = t<13.05; vis('s1',s1);
  if(s1){{
    // headline
    lineIn('h1a',t,-0.5,0.5,2.85); lineIn('h1b',t,-0.42,0.5,2.9);
    if(t>=3.0){{ $('h1a').textContent='An HS code.'; $('h1b').textContent='Six digits, three levels.'; lineIn('h1a',t,3.05,.5,4.85); lineIn('h1b',t,3.12,.5,4.9); }}
    else {{ $('h1a').textContent='Can you read'; $('h1b').textContent='this code?'; }}
    $('head').style.display = t<5.0?'block':'none';
    // code glyphs slam in 0-0.7 (first glyph already moving at frame 0)
    const gs=[...document.querySelectorAll('#code .g')];
    gs.forEach((g,i)=>{{ const p=eo((t+0.18-0.07*i)/0.6); g.style.transform=`translateY(${{(1-p)*105}}%)`; }});
    // code moves up + splits into pairs at 5.0
    const sp=eio(lin(t,5.0,5.55));
    const codeTop = 760 - sp*400;   // 760 -> 360
    const csc = 1 - sp*0.15;
    $('code').style.top=codeTop+'px';
    const gap = sp*44;
    $('p2').style.marginLeft=gap+'px'; $('dt').style.marginLeft=gap*0.25+'px'; $('dt').style.marginRight=gap*0.75+'px';
    $('dt').style.opacity = 1-sp*0.75;
    // zoom-through at 12.5: code scales toward camera
    $('code').style.transformOrigin='0 0'; $('code').style.transform=`scale(${{csc}})`;
    $('code').style.opacity = 1-eio(lin(t,12.4,12.7));
    // pair highlighting
    const act = t<5.3? -1 : (t<7.5?0:(t<10?1:2));
    ['p1','p2','p3'].forEach((id,i)=>{{ $(id).style.color = act<0? '#F3F2EC' : (i===act? '#D9FF5B' : 'rgba(243,242,236,.32)'); }});
    // cursor travels under the active pair
    const pr=[$('p1').getBoundingClientRect(),$('p2').getBoundingClientRect(),$('p3').getBoundingClientRect()];
    const seg=(a,b,t0)=>{{const k=eio(lin(t,t0,t0+0.45));return [a.left+(b.left-a.left)*k, a.width+(b.width-a.width)*k]}};
    let cx=pr[0].left,cw=0;
    if(t>=5.3){{ cw=pr[0].width*eo((t-5.3)/0.45); cx=pr[0].left; }}
    if(t>=7.5){{ [cx,cw]=seg(pr[0],pr[1],7.5); }}
    if(t>=10){{ [cx,cw]=seg(pr[1],pr[2],10); }}
    $('cursor').style.left=cx+'px'; $('cursor').style.width=cw+'px'; $('cursor').style.top=(codeTop+252*csc)+'px';
    $('cursor').style.opacity = 1-eio(lin(t,12.4,12.7));
    // sub line (scene 2)
    $('sub').innerHTML = SUBS[0][1]; $('sub').style.top='960px';
    const so=eo((t-3.25)/0.5)*(1-lin(t,4.75,5.0)); $('sub').style.opacity=so; $('sub').style.transform=`translateY(${{(1-eo((t-3.25)/.5))*24}}px)`;
    // level labels: masked swaps
    const L=[['l1',5.45,7.5],['l2',7.7,10.0],['l3',10.2,12.25]];
    L.forEach(([id,a,b])=>{{ const on=t>=a-0.01&&t<b+0.3; vis(id,on); if(!on)return;
      const kids=[...$(id).children]; kids.forEach((k,j)=>{{ const p=eo((t-a-0.08*j)/0.5); const o=eio(lin(t,b-0.05,b+0.25));
        k.style.transform=`translateY(${{(1-p)*40 - o*30}}px)`; k.style.opacity=p*(1-o); }}); }});
    $('lvl').style.top=(1100 - sp*480)+'px';  // 1100 -> 620
    // photo plate: column shutter open at 7.7, swap at 10.0, close at 12.2
    const plateOn=t>=7.6&&t<12.45; $('plate').style.display=plateOn?'block':'none'; $('pcr').style.opacity=plateOn? eo((t-8.1)/.4)*(1-lin(t,12.1,12.35)):0;
    $('ph1').style.opacity = t<10.25?1:0; $('ph2').style.opacity = t>=10.25?1:0;
    $('pcr').textContent = t<10.25? 'Ferro-silicon, also heading 72.02 · FocalPoint, CC BY-SA 4.0' : 'Ferro-chromium · FocalPoint, CC BY-SA 4.0';
    const kb = t<10.25? lin(t,7.7,10.25): lin(t,10.25,12.5);
    document.querySelectorAll('#plate .ph').forEach(p=>p.style.transform=`scale(${{1.06-0.05*kb}}) translateX(${{(kb-.5)*-14}}px)`);
    [...document.querySelectorAll('#sh b')].forEach((b,i)=>{{
      let s;
      if(t<10.0) s=1-eo((t-7.7-0.05*i)/0.5);                 // open
      else if(t<10.25) s=eio((t-10.0-0.02*i)/0.2);            // close for swap
      else if(t<12.1) s=1-eo((t-10.25-0.05*(5-i))/0.5);       // open again (reverse order)
      else s=eio((t-12.1-0.02*i)/0.25);
      b.style.transform=`scaleY(${{cl(s)}})`; b.style.transformOrigin = (t>=10.0&&t<10.25)||t>=12.1 ? '50% 100%':'50% 0';
    }});
  }}
  // ---- list scene (12.9-15.6) ----
  const ls = t>=12.9 && t<15.6; vis('list',ls);
  if(ls){{
    lineIn('lt1',t,13.0,.5); lineIn('lt2',t,13.08,.5);
    document.querySelector('#list .hd').style.opacity=eo((t-13.3)/.4);
    ['r1','r2','r3','r4'].forEach((id,i)=>{{ const a=13.4+0.35*i; const p=eo((t-a)/0.5);
      $(id).style.opacity=p; $(id).style.transform=`translateX(${{(1-p)*-60}}px)`; $(id).style.clipPath=`inset(0 ${{(1-p)*100}}% 0 0)`; }});
  }}
  // ---- stats (15.9-18) ----
  const ss=t>=15.85&&t<18.05; vis('stats',ss);
  if(ss){{
    const D=[[ 'n1',5000,'',',+',16.0],['n2',200,'','+',16.4],['n3',98,'%','+',16.8]];
    D.forEach(([id,v,suf,plus,a],i)=>{{ const p=eo((t-a)/0.9); const st=$('st'+(i+1));
      st.style.opacity=eo((t-a+0.1)/0.35)*(1-lin(t,17.8,18.0)); st.style.transform=`translateY(${{(1-eo((t-a+0.1)/0.45))*50}}px)`;
      const n=Math.round(v*p); const s=n.toLocaleString('en-US');
      $(id).innerHTML = s+suf+(p>0.995?'<em>+</em>':'<em style="opacity:0">+</em>'); }});
  }}
  // ---- tip (18-20) ----
  const ts=t>=18&&t<20.05; vis('tip',ts);
  if(ts){{
    lineIn('ta1',t,18.02,.45); lineIn('ta2',t,18.1,.45);
    document.querySelector('#tip .tag').style.opacity=eo((t-18)/.3);
    const full='Confirm the full local code with your customs broker before you ship.';
    const n=Math.floor(cl((t-18.5)/1.05)*full.length);
    $('tb').innerHTML = full.slice(0,n)+'<span class="caret" style="opacity:'+((Math.floor(t*4)%2)||n<full.length?1:0)+'"></span>';
    $('tip').style.opacity=1-lin(t,19.85,20.05);
  }}
  // ---- end (20-23) ----
  const es=t>=20.0; vis('end',es);
  if(es){{
    const fi=(id,d,dy=30)=>{{const p=eo((t-20-d)/0.5);$(id).style.opacity=p;$(id).style.transform=`translateY(${{(1-p)*dy}}px)`}};
    fi('ec',0.1); lineIn('eh1',t,20.2,.5); lineIn('eh2',t,20.3,.5);
    $('er').style.transform=`scaleX(${{eio((t-20.7)/0.6)}})`;
    $('ep').style.clipPath=`inset(0 0 ${{(1-eio((t-20.35)/0.6))*100}}% 0)`; $('ep').style.backgroundSize=`${{100+ (1-lin(t,20.35,23))*6}}% auto`;
    fi('esig',0.95,20); fi('eurl',1.05,20); fi('esrc',1.3,14);
  }}
  $('fade').style.opacity = t>22.4? eio((t-22.4)/0.6):0;
}}
render(0);
</script></body></html>'''

def main():
    from playwright.sync_api import sync_playwright
    preview = None
    if "--preview" in sys.argv: preview = [float(x) for x in sys.argv[sys.argv.index("--preview") + 1].split(",")]
    os.makedirs(WORK, exist_ok=True)
    tpl = os.path.join(ROOT, "templates", SLUG + ".html")
    for f in ("duo-fesi.jpg", "duo-fecr.jpg"):
        os.makedirs(os.path.join(ROOT, "templates"), exist_ok=True)
        Image.open(os.path.join(WORK, f)).save(os.path.join(ROOT, "templates", f), quality=94)
    open(tpl, "w", encoding="utf-8").write(html())
    os.makedirs(OUT, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=os.environ.get("CHROME", "/usr/bin/google-chrome"),
                              args=["--font-render-hinting=none", "--force-color-profile=srgb"])
        pg = b.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
        pg.goto("file://" + tpl, wait_until="networkidle")
        pg.evaluate("document.fonts.ready.then(()=>true)"); pg.wait_for_timeout(600)
        bad = pg.evaluate("[...document.fonts].filter(f=>f.status==='error').map(f=>f.family)")
        if bad: print("FONT problems:", bad); sys.exit(2)
        if preview:
            os.makedirs(os.path.join(WORK, "preview"), exist_ok=True)
            for t in preview:
                pg.evaluate(f"render({t})"); pg.screenshot(path=os.path.join(WORK, "preview", f"t{t:05.2f}.png"))
                print(t, pg.evaluate("""(()=>{const o=[];document.querySelectorAll('#head,#code,#sub,.lv,#pcr,#list .t,.row,.st,#tip,#end .h,#esig,#eurl,#esrc,#ec,.top').forEach(e=>{let v=e,op=1;while(v&&v.nodeType==1){const s=getComputedStyle(v);if(s.display=='none'){op=0;break}op*=+s.opacity;v=v.parentElement}if(op<.05)return;const r=e.getBoundingClientRect();if(r.width&&(r.top<220||r.bottom>1600||r.right>945||r.left<60))o.push((e.id||e.className)+':'+[r.left,r.top,r.right,r.bottom].map(Math.round))});return o})()"""))
            b.close(); return
        silent = os.path.join(WORK, "video.mp4")
        ff = subprocess.Popen(["ffmpeg", "-loglevel", "error", "-y", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "png",
                               "-i", "-", "-vf", "scale=in_range=pc:out_range=tv,format=yuv420p", "-color_range", "tv", "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709",
                               "-c:v", "libx264", "-preset", "slow", "-crf", "16", "-tune", "animation", "-pix_fmt", "yuv420p",
                               "-profile:v", "high", "-level", "4.1", "-r", str(FPS), silent], stdin=subprocess.PIPE)
        n = int(round(DUR * FPS)); t0 = time.time()
        for f in range(n):
            t = f / FPS
            pg.evaluate(f"render({t})")
            shot = pg.screenshot(type="png")
            ff.stdin.write(shot)
            if f == 33: open(os.path.join(WORK, "cover.png"), "wb").write(shot)
            if f % 90 == 0: print(f"frame {f}/{n}  {time.time()-t0:.0f}s", flush=True)
        ff.stdin.close(); ff.wait(); b.close()
    wav = os.path.join(WORK, "music.wav")
    mp4 = os.path.join(OUT, SLUG + ".mp4")
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", silent, "-i", wav, "-map", "0:v", "-map", "1:a",
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", "-shortest", mp4], check=True)
    cover = os.path.join(OUT, SLUG + "-cover.jpg")
    Image.open(os.path.join(WORK, "cover.png")).convert("RGB").save(cover, "JPEG", quality=92, subsampling=0, optimize=True)
    story = os.path.join(OUT, SLUG + "-story.mp4")
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", mp4, "-c:v", "libx264", "-pix_fmt", "yuv420p", "-b:v", "5M", "-maxrate", "6M",
                    "-bufsize", "10M", "-g", "30", "-c:a", "aac", "-b:a", "128k", "-ar", "44100", "-movflags", "+faststart", story], check=True)
    print(mp4, os.path.getsize(mp4) // 1024, "KB"); print(cover); print(story, os.path.getsize(story) // 1024, "KB")

if __name__ == "__main__":
    main()
