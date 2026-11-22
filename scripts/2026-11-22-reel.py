#!/usr/bin/env python3
"""2026-11-22 — Reel "20ft, 40ft or 40ft High Cube? The key numbers" (EN, 24 s, key-numbers format).

Creative brief
- Concept: "Blueprint Box". A deep blueprint page with a fine grid; one container is drawn as a white line elevation
  (true scale, 1 m = 71.5 px) and morphs 20' -> 40' -> 40' HC while dimension lines and two big counters
  (capacity m3, max payload kg) roll to the new values. Insight scene: two bar rows show the twist — the 40' has about
  twice the space of the 20', but nearly the same weight limit. Photo hook and photo end card (Yangshan, Commons).
- Tone / palette (mid-dark, after the light ivory reel of 21 Nov): blueprint #15324A -> #0F2638, line white #EAF2F7,
  amber #F2A541 (space), mint #7FD1B9 (weight), seal red #AC3E33 on the seal only.
  Type: Oswald 600 (names, numbers) + Manrope (text) + Playfair Display italic (end line). No Space Grotesk (used 21 Nov).
- Facts: Hapag-Lloyd container specifications (hapag-lloyd.com, fetched 22 Nov 2026; example values, vary by manufacturer):
  20' Standard: inside L 5,900 mm, W 2,352, H 2,395; capacity 33.2 m3; max gross 30,480 kg; tare 2,350; max payload 28,130 kg.
  40' Standard: inside L 12,032, W 2,352, H 2,395; 67.7 m3; max gross 32,500; tare 3,750; max payload 28,750 kg.
  40' High Cube: inside L 12,032, W 2,350, H 2,700; 76.3 m3; max gross 32,500; tare 3,900; max payload 28,600 kg.
- Timing (30 fps, 24.0 s): hook 0-2.6 (title on frame 1); 20' 2.6-7.4; 40' 7.4-12.2; 40' HC 12.2-17.0;
  insight 17.0-20.2; end card 20.2-24; 23.55-24 fade to blueprint; hook photo fades in over 0-0.35 s (text on frame 1), so the loop point is blueprint->blueprint. Cover = frame at 1.0 s.
- Safe zones: text between y 240 and 1590, x 72..940.
- Photos: photos/reel-yangshan-container-lanes.jpg (Reb42, CC BY 3.0), photos/reel-yangshan-yard-overview.jpg
  (Gmbsfd, CC BY-SA 4.0), both Wikimedia Commons, credited on frame and in caption.
- Logo: tools/linkwin_mark.py signature + faint echo on the end card only.
- PRC compliance: neutral logistics education; no politics, maps, flags or people.
usage: python3 scripts/2026-11-22-reel.py [--preview t1,t2,...]
"""
import os, sys, subprocess, time
from PIL import Image
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from linkwin_mark import MARK_CSS, signature, echo
OUT = os.path.join(ROOT, "posts", "2026-11-22", "reel")
WORK = "/tmp/reel-2026-11-22"
FPS, DUR = 30, 24.0
SLUG = "2026-11-22-reel-container-key-numbers-en"
HOOK = ("reel-yangshan-container-lanes.jpg", .5, "Yangshan Port · Reb42 · CC BY 3.0")
ENDP = ("reel-yangshan-yard-overview.jpg", .5, "Yangshan Port · Gmbsfd · CC BY-SA 4.0")

def crop(f, fx, name, W, H):
    os.makedirs(WORK, exist_ok=True)
    W2, H2 = int(W * 1.12), int(H * 1.12)
    im = Image.open(os.path.join(ROOT, "photos", f)).convert("RGB")
    sc = max(W2 / im.width, H2 / im.height)
    im = im.resize((round(im.width * sc), round(im.height * sc)), Image.LANCZOS)
    x = min(max(0, round(im.width * fx - W2 / 2)), im.width - W2); y = (im.height - H2) // 2
    p = os.path.join(WORK, name); im.crop((x, y, x + W2, y + H2)).save(p, quality=94); return p

def html(hook, endp):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<link rel="stylesheet" href="../brand/fonts.css"><style>
:root{{--bp:#15324A;--bp2:#0F2638;--ln:#EAF2F7;--amb:#F2A541;--mint:#7FD1B9;--lw-ink:#EAF2F7;--lw-seal:#AC3E33}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1920px;overflow:hidden;background:var(--bp);color:var(--ln);font-family:Manrope,sans-serif}}
#page{{position:absolute;inset:0;background:radial-gradient(120% 80% at 50% 35%,#1A3D59,#15324A 55%,#0F2638)}}
#grid{{position:absolute;inset:0;background-image:linear-gradient(rgba(234,242,247,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(234,242,247,.06) 1px,transparent 1px),linear-gradient(rgba(234,242,247,.11) 1px,transparent 1px),linear-gradient(90deg,rgba(234,242,247,.11) 1px,transparent 1px);background-size:36px 36px,36px 36px,180px 180px,180px 180px;background-position:0 0,0 0,-1px -1px,-1px -1px}}
.k{{font:800 24px/1 Manrope;letter-spacing:.2em;text-transform:uppercase}}
/* hook */
#hook{{position:absolute;inset:0;z-index:40}}
#hph{{position:absolute;left:0;top:0;width:1080px;height:980px;overflow:hidden}}
#hph img{{width:1080px;height:980px;object-fit:cover;transform-origin:50% 60%}}
#hph:after{{content:"";position:absolute;inset:0;background:linear-gradient(rgba(15,38,56,.45),rgba(15,38,56,0) 30%,rgba(21,50,74,0) 60%,#15324A 99%)}}
#hph .cr,#eph .cr{{position:absolute;right:150px;top:240px;font-size:17px;color:rgba(255,255,255,.85);z-index:2;white-space:nowrap}}
#htext{{position:absolute;left:72px;top:900px;width:880px}}
#htext .k{{color:var(--amb)}}
#htext h1{{font:600 150px/0.98 Oswald;letter-spacing:-.01em;margin-top:24px;text-transform:uppercase}}
#htext h1 span{{color:var(--amb)}} #htext h1 em{{font-style:normal;color:var(--mint)}}
#htext p{{font:600 40px/1.3 Manrope;color:rgba(234,242,247,.85);margin-top:30px}}
/* spec stage */
#stage{{position:absolute;inset:0;z-index:20;opacity:0}}
#shead{{position:absolute;left:72px;top:300px;width:880px}}
#sn{{font:800 24px/1 Manrope;letter-spacing:.2em;color:var(--amb)}}
.nm{{position:absolute;left:0;top:44px;font:600 128px/1 Oswald;text-transform:uppercase;white-space:nowrap}}
.iso{{position:absolute;left:0;top:190px;font:600 30px/1 Manrope;color:rgba(234,242,247,.7);white-space:nowrap}}
#draw{{position:absolute;left:0;top:0;width:1080px;height:1920px}}
#stats{{position:absolute;left:72px;top:1120px;width:880px;display:flex;gap:40px}}
.st{{flex:1;border-top:2px solid rgba(234,242,247,.3);padding-top:26px}}
.st .lb{{font:800 21px/1.2 Manrope;letter-spacing:.16em;text-transform:uppercase;color:rgba(234,242,247,.72)}}
.st .v{{font:600 112px/1 Oswald;margin-top:16px;white-space:nowrap}} .st .v small{{font:600 46px/1 Oswald;margin-left:10px;opacity:.85}}
#s1 .v{{color:var(--amb)}} #s2 .v{{color:var(--mint)}}
#fact{{position:absolute;left:72px;top:1420px;width:880px;font:600 29px/1.35 Manrope;color:rgba(234,242,247,.88)}}
/* insight */
#ins{{position:absolute;inset:0;z-index:30;opacity:0}}
#itext{{position:absolute;left:72px;top:300px;width:880px}}
#itext .k{{color:var(--mint)}}
#itext h2{{font:600 104px/1.0 Oswald;text-transform:uppercase;margin-top:24px}}
#itext h2 span{{color:var(--amb)}} #itext h2 em{{font-style:normal;color:var(--mint)}}
.row{{position:absolute;left:72px;width:880px}}
.row .lb{{font:800 22px/1 Manrope;letter-spacing:.16em;text-transform:uppercase;color:rgba(234,242,247,.75);margin-bottom:22px}}
.bar{{display:flex;align-items:center;gap:20px;height:58px;margin-bottom:14px}}
.bar b{{width:120px;flex:none;font:600 34px/1 Oswald}}
.bar i{{display:block;height:40px;border-radius:4px;width:0}}
.bar span{{font:600 34px/1 Oswald;white-space:nowrap;opacity:0}}
#rv i{{background:var(--amb)}} #rw i{{background:var(--mint)}}
#tipt{{position:absolute;left:72px;top:1370px;width:880px;font:600 32px/1.4 Manrope;color:rgba(234,242,247,.9)}}
#tipt p{{padding-left:26px;border-left:5px solid var(--amb);margin-bottom:24px}} #tipt p.w{{border-color:var(--mint)}}
/* end */
#end{{position:absolute;inset:0;z-index:50;opacity:0;overflow:hidden;background:var(--bp2)}}
#eph{{position:absolute;left:0;top:0;width:1080px;height:900px;overflow:hidden}}
#eph img{{width:1080px;height:900px;object-fit:cover}}
#eph:after{{content:"";position:absolute;inset:0;background:linear-gradient(rgba(15,38,56,.5),rgba(15,38,56,.1) 35%,rgba(15,38,56,.2) 60%,#0F2638 99%)}}
#end .lw-echo{{--lw-echo:#EAF2F7;--lw-echo-op:.028;--lw-echo-size:1150px}}
#endtext{{position:absolute;left:72px;top:760px;width:860px}}
#endtext .k{{color:var(--amb)}}
#endtext h2{{font:italic 700 92px/1.04 'Playfair Display';margin-top:26px}}
#endtext h2 span{{color:var(--mint)}}
#endtext p{{font:500 34px/1.45 Manrope;margin-top:32px;color:rgba(234,242,247,.85)}}
#endrule{{width:860px;height:2px;background:var(--ln);opacity:.25;margin:52px 0 44px;transform-origin:0 50%}}
#endsig{{display:flex;align-items:center;justify-content:space-between;width:860px}}
#endsig .url{{font:600 44px/1 Oswald;letter-spacing:.03em}}
#endsrc{{font:500 20px/1.45 Manrope;color:rgba(234,242,247,.65);margin-top:38px}}
#fade{{position:absolute;inset:0;background:var(--bp);opacity:0;z-index:60}}
{MARK_CSS}
</style></head><body>
<div id="page"></div><div id="grid"></div>
<div id="stage">
 <div id="shead"><div id="sn">01 / 03</div>
  <div class="nm" id="n0">20′ Standard</div><div class="nm" id="n1">40′ Standard</div><div class="nm" id="n2">40′ High Cube</div>
  <div class="iso" id="i0">ISO 22G1 · the “twenty”</div><div class="iso" id="i1">ISO 42G1 · double the length</div><div class="iso" id="i2">ISO 45G1 · 30 cm taller inside</div></div>
 <svg id="draw" viewBox="0 0 1080 1920"><g id="box"></g></svg>
 <div id="stats"><div class="st" id="s1"><div class="lb">Capacity</div><div class="v"><span id="vc">33.2</span><small>m³</small></div></div>
  <div class="st" id="s2"><div class="lb">Max payload</div><div class="v"><span id="vw">28,130</span><small>kg</small></div></div></div>
 <div id="fact"></div>
</div>
<div id="ins"><div id="itext"><div class="k" id="ik">The twist</div><h2 id="ih">40′ = <span>2× the space</span>.<br>Not <em>2× the weight</em>.</h2></div>
 <div class="row" id="rv" style="top:760px"><div class="lb">Space · m³</div>
  <div class="bar"><b>20′</b><i data-w="33.2"></i><span>33.2</span></div><div class="bar"><b>40′</b><i data-w="67.7"></i><span>67.7</span></div><div class="bar"><b>40′ HC</b><i data-w="76.3"></i><span>76.3</span></div></div>
 <div class="row" id="rw" style="top:1060px"><div class="lb">Max payload · tonnes</div>
  <div class="bar"><b>20′</b><i data-w="28.13"></i><span>28.1</span></div><div class="bar"><b>40′</b><i data-w="28.75"></i><span>28.8</span></div><div class="bar"><b>40′ HC</b><i data-w="28.6"></i><span>28.6</span></div></div>
 <div id="tipt"><p id="t1">Dense cargo like ferroalloys and metals hits the weight limit first: a 20′ often does the job.</p><p class="w" id="t2">Light, bulky goods fill space first: go 40′ or 40′ HC.</p></div>
</div>
<div id="hook"><div id="hph"><img id="himg" src="file://{hook}"><div class="cr">Photo: {HOOK[2]} · Wikimedia Commons</div></div>
 <div id="htext"><div class="k">Container key numbers</div><h1><span>20′</span>, <em>40′</em><br>or 40′ HC?</h1><p>4 numbers that decide which box you book.</p></div></div>
<div id="end"><div id="eph"><img id="eimg" src="file://{endp}"><div class="cr">Photo: {ENDP[2]} · Wikimedia Commons</div></div>{echo("right","-300px","-360px")}
 <div id="endtext"><div class="k" id="ek">Before you book</div>
 <h2 id="eh">Weigh it first. <span>Then pick the box.</span></h2>
 <p id="ep">LinkWin Trading plans loads for ferroalloys, metals and industrial goods shipped from China.</p>
 <div id="endrule"></div><div id="endsig">{signature()}<div class="url">linkwinco.com</div></div>
 <div id="endsrc">Source: Hapag-Lloyd container specifications (typical values; boxes vary by manufacturer)</div></div></div>
<div id="fade"></div>
<script>
const SPEC=[{{L:5.900,H:2.395,cap:33.2,pay:28130,fact:"Inside 5.90 × 2.35 × 2.39 m. Tare 2,350 kg, max gross 30,480 kg."}},
 {{L:12.032,H:2.395,cap:67.7,pay:28750,fact:"Inside 12.03 × 2.35 × 2.39 m. Tare 3,750 kg, max gross 32,500 kg."}},
 {{L:12.032,H:2.700,cap:76.3,pay:28600,fact:"Inside 12.03 × 2.35 × 2.70 m. Tare 3,900 kg, max gross 32,500 kg."}}];
const ST=[2.6,7.4,12.2], INS=17.0, END=20.2, PXM=71.5, X0=107, BASE=960;
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x)), ease=x=>{{x=cl(x);return x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2}}, eo=x=>1-Math.pow(1-cl(x),3);
const $=id=>document.getElementById(id), lerp=(a,b,k)=>a+(b-a)*k;
function boxSVG(L,H,draw,ghost,gop,glab){{
  const w=L*PXM, h=H*PXM, x=X0, y=BASE-h; let s='';
  if(ghost&&gop>0){{ const gw=ghost.L*PXM, gh=ghost.H*PXM; s+=`<g opacity="${{gop}}"><rect x="${{X0}}" y="${{BASE-gh}}" width="${{gw}}" height="${{gh}}" fill="rgba(127,209,185,.10)" stroke="#7FD1B9" stroke-width="3" stroke-dasharray="12 9"/><text x="${{X0+18}}" y="${{BASE-gh+44}}" font-family="Oswald" font-weight="600" font-size="30" fill="#7FD1B9">${{glab}}</text></g>` }}
  const dash=(len)=>`stroke-dasharray="${{len}}" stroke-dashoffset="${{len*(1-draw)}}"`;
  const per=2*(w+h);
  s+=`<rect x="${{x}}" y="${{y}}" width="${{w}}" height="${{h}}" fill="rgba(234,242,247,.04)" stroke="#EAF2F7" stroke-width="4" ${{dash(per)}}/>`;
  const n=Math.round(w/16); const op=cl(draw*1.4-0.4);
  for(let k=1;k<n;k++){{ const xx=x+k*w/n; s+=`<line x1="${{xx}}" y1="${{y+10}}" x2="${{xx}}" y2="${{BASE-10}}" stroke="rgba(234,242,247,${{(k%2?.10:.18)*op}})" stroke-width="2"/>` }}
  // door end with lock bars
  s+=`<g opacity="${{op}}"><line x1="${{x+w-6}}" y1="${{y}}" x2="${{x+w-6}}" y2="${{BASE}}" stroke="#EAF2F7" stroke-width="3"/>`;
  for(const dx of [-22,-44]) s+=`<line x1="${{x+w+dx}}" y1="${{y+8}}" x2="${{x+w+dx}}" y2="${{BASE-8}}" stroke="rgba(234,242,247,.6)" stroke-width="3"/>`;
  // corner castings
  for(const [cx,cy] of [[x,y],[x+w-22,y],[x,BASE-16],[x+w-22,BASE-16]]) s+=`<rect x="${{cx}}" y="${{cy}}" width="22" height="16" fill="#EAF2F7"/>`;
  s+=`</g>`;
  // dimension lines: length below, height label above the top-right corner
  const dy=BASE+46;
  s+=`<g opacity="${{op}}" stroke="#F2A541" stroke-width="2.5">
   <line x1="${{x}}" y1="${{dy}}" x2="${{x+w}}" y2="${{dy}}"/><line x1="${{x}}" y1="${{dy-14}}" x2="${{x}}" y2="${{dy+14}}"/><line x1="${{x+w}}" y1="${{dy-14}}" x2="${{x+w}}" y2="${{dy+14}}"/></g>
   <text opacity="${{op}}" x="${{x+w/2}}" y="${{dy+50}}" text-anchor="middle" font-family="Oswald" font-weight="600" font-size="38" fill="#F2A541">${{(Math.floor(L*100+1e-6)/100).toFixed(2)}} m inside</text>
   <text opacity="${{op}}" x="${{x+w-20}}" y="${{y-24}}" text-anchor="end" font-family="Oswald" font-weight="600" font-size="38" fill="#F2A541">${{(Math.floor(H*100+1e-6)/100).toFixed(2)}} m high</text>`;
  return s;
}}
function render(t){{
  // spec state
  let k=0, i=0; if(t>=ST[2]) {{i=2;k=ease((t-ST[2])/0.8)}} else if(t>=ST[1]) {{i=1;k=ease((t-ST[1])/0.8)}}
  const a=SPEC[Math.max(0,i-1)], b=SPEC[i], kk=i==0?1:k;
  const L=lerp(a.L,b.L,kk), H=lerp(a.H,b.H,kk);
  const draw=i==0?ease((t-ST[0]-0.2)/1.1):1;
  const gop=i==0?0:eo((t-ST[i]-0.7)/0.5)*0.95, glab=['','20′ inside','40′ standard height'][i];
  $('box').innerHTML=boxSVG(L,H,draw,i>0?SPEC[i-1]:null,gop,glab);
  const sk=i==0?eo((t-ST[0]-0.8)/1.0):kk;
  const cap=i==0?b.cap*sk:lerp(a.cap,b.cap,kk), pay=i==0?b.pay*sk:lerp(a.pay,b.pay,kk);
  $('vc').textContent=cap.toFixed(1); $('vw').textContent=Math.round(pay/10)*10>=1000?Math.round(i==0&&sk<1?pay:pay).toLocaleString('en-US'):Math.round(pay);
  if(sk>=1||i>0&&kk>=1) $('vw').textContent=b.pay.toLocaleString('en-US');
  $('sn').textContent='0'+(i+1)+' / 03';
  for(let j=0;j<3;j++){{
    let o=0; if(j==i) o=i==0?eo((t-ST[0])/0.45):eo((t-ST[i]-0.1)/0.45); if(j==i-1) o=1-eo((t-ST[i])/0.3);
    for(const p of ['n','i']){{ const e=$(p+j); e.style.opacity=o; e.style.transform=`translateY(${{(1-o)*(j==i?30:-30)}}px)`}}
  }}
  const fo=i==0?eo((t-ST[0]-1.6)/0.5):eo((t-ST[i]-0.9)/0.5);
  $('fact').textContent=b.fact; $('fact').style.opacity=fo; $('fact').style.transform=`translateY(${{(1-fo)*20}}px)`;
  const so=i==0?eo((t-ST[0]-0.6)/0.5):1; $('stats').style.opacity=so; $('stats').style.transform=`translateY(${{(1-so)*30}}px)`;
  $('stage').style.opacity=t<ST[0]?0:(t<INS?eo((t-ST[0])/0.35):1-eo((t-INS)/0.35));
  // hook
  const ho=t<2.35?1:1-eo((t-2.35)/0.35); $('hook').style.opacity=ho;
  $('himg').style.transform=`scale(${{1.0+0.06*cl(t/2.6)}})`; $('hph').style.opacity=eo(t/0.35); $('htext').style.transform=`translateY(${{-(1-ho)*40}}px)`;
  // insight
  const io=t<INS?0:(t<END?eo((t-INS)/0.4):1); $('ins').style.opacity=io;
  const it=(id,d)=>{{const v=eo((t-INS-d)/0.45); $(id).style.opacity=v; $(id).style.transform=`translateY(${{(1-v)*26}}px)`}};
  it('ik',0.1); it('ih',0.25);
  document.querySelectorAll('#rv .bar,#rw .bar').forEach((el,n)=>{{const row=n<3?0:1, d=0.6+row*0.55+(n%3)*0.12, v=ease((t-INS-d)/0.6);
    const w=+el.querySelector('i').dataset.w, max=row==0?76.3:30.0; el.querySelector('i').style.width=(560*w/max*v)+'px'; el.querySelector('span').style.opacity=eo((t-INS-d-0.4)/0.3)}});
  it('t1',1.6); it('t2',2.2);
  // end
  const en=t<END?0:eo((t-END)/0.45); $('end').style.opacity=en; $('eimg').style.transform=`scale(${{1.02+0.05*cl((t-END)/3.8)}})`;
  it2=(id,d)=>{{const v=eo((t-END-d)/0.45); $(id).style.opacity=v; $(id).style.transform=`translateY(${{(1-v)*28}}px)`}};
  it2('ek',0.25); it2('eh',0.4); it2('ep',0.85); it2('endsig',1.25); it2('endsrc',1.5);
  $('endrule').style.transform=`scaleX(${{eo((t-END-1.1)/0.6)}})`;
  $('fade').style.opacity=t>23.55?eo((t-23.55)/0.45):0;
}}
</script></body></html>'''

def main():
    from playwright.sync_api import sync_playwright
    preview = None
    if "--preview" in sys.argv: preview = [float(x) for x in sys.argv[sys.argv.index("--preview") + 1].split(",")]
    hook = crop(HOOK[0], HOOK[1], "hook.jpg", 1080, 980); endp = crop(ENDP[0], ENDP[1], "end.jpg", 1080, 900)
    tpl = os.path.join(ROOT, "templates", SLUG + ".html")
    open(tpl, "w", encoding="utf-8").write(html(hook, endp))
    os.makedirs(OUT, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=os.environ.get("CHROME", "/usr/bin/google-chrome"),
                              args=["--font-render-hinting=none", "--force-color-profile=srgb"])
        pg = b.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
        pg.goto("file://" + tpl, wait_until="networkidle")
        pg.evaluate("document.fonts.ready.then(()=>true)"); pg.wait_for_timeout(500)
        bad = pg.evaluate("[...document.fonts].filter(f=>f.status==='error').map(f=>f.family)")
        imgs = pg.evaluate("[...document.images].filter(i=>!i.complete||i.naturalWidth===0).map(i=>i.src)")
        if bad or imgs: print("FONT/IMG problems:", bad, imgs); sys.exit(2)
        if preview:
            os.makedirs(os.path.join(WORK, "preview"), exist_ok=True)
            for t in preview:
                pg.evaluate(f"render({t})"); pg.screenshot(path=os.path.join(WORK, "preview", f"t{t:05.2f}.png"))
                print(t, pg.evaluate("""(()=>{const o=[];document.querySelectorAll('h1,h2,p,.nm,.iso,.st,.bar,#fact,#endsig,.cr,#endsrc,text').forEach(e=>{const s=getComputedStyle(e);let v=e,op=1;while(v&&v.nodeType==1){op*=+getComputedStyle(v).opacity;v=v.parentElement}if(op<.05)return;const r=e.getBoundingClientRect();if(r.width&&(r.top<220||r.bottom>1600||r.right>950||r.left<60))o.push((e.id||e.tagName)+':'+[r.left,r.top,r.right,r.bottom].map(Math.round))});return o})()"""))
            print("previews in", os.path.join(WORK, "preview")); b.close(); return
        silent = os.path.join(WORK, "video.mp4")
        ff = subprocess.Popen(["ffmpeg", "-loglevel", "error", "-y", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "mjpeg",
                               "-i", "-", "-vf", "scale=in_range=pc:out_range=tv,format=yuv420p", "-color_range", "tv", "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", "-c:v", "libx264", "-preset", "slow", "-crf", "17", "-pix_fmt", "yuv420p",
                               "-profile:v", "high", "-level", "4.1", "-r", str(FPS), silent], stdin=subprocess.PIPE)
        n = int(round(DUR * FPS)); t0 = time.time()
        for f in range(n):
            t = f / FPS
            pg.evaluate(f"render({t})")
            ff.stdin.write(pg.screenshot(type="jpeg", quality=96))
            if f == 30: pg.screenshot(path=os.path.join(WORK, "cover.png"))
            if f % 90 == 0: print(f"frame {f}/{n}  {time.time()-t0:.0f}s", flush=True)
        ff.stdin.close(); ff.wait(); b.close()
    wav = os.path.join(WORK, "bed.wav")
    subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "2026-11-22-reel-audio.py"), wav], check=True)
    mp4 = os.path.join(OUT, SLUG + ".mp4")
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", silent, "-i", wav, "-map", "0:v", "-map", "1:a",
                    "-c:v", "copy", "-af", "loudnorm=I=-18:TP=-2:LRA=7", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                    "-movflags", "+faststart", "-shortest", mp4], check=True)
    cover = os.path.join(OUT, SLUG + "-cover.jpg")
    Image.open(os.path.join(WORK, "cover.png")).convert("RGB").save(cover, "JPEG", quality=92, subsampling=0, optimize=True)
    story = os.path.join(OUT, SLUG + "-story.mp4")
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", mp4, "-c:v", "libx264", "-pix_fmt", "yuv420p", "-b:v", "5M", "-maxrate", "6M",
                    "-bufsize", "10M", "-g", "30", "-c:a", "aac", "-b:a", "128k", "-ar", "44100", "-movflags", "+faststart", story], check=True)
    print(mp4, os.path.getsize(mp4) // 1024, "KB"); print(cover); print(story, os.path.getsize(story) // 1024, "KB")

if __name__ == "__main__":
    main()
