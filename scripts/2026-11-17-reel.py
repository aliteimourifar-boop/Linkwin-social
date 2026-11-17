#!/usr/bin/env python3
"""2026-11-17 — Reel "Flag Hoist": Where are the world's top container lines from? (EN only, per Ali's scope change)

Creative brief
- Concept: "Flag Hoist". A fast, loopable quiz in LinkWin's editorial style. Reference idea: @pres.english
  "Where are these shipping companies from?" (two presenters, ship photo + pop-up label + flag). Ours is pure
  motion graphics: cinematic ship photography on top, a calm sea-salt paper deck below, one carrier per bar of music.
- Tone / palette: light (sea-salt paper #EFEBE3), harbour ink #14222F, seal red #AC3E33 (progress, wipe edge, seal), slate #5E6873.
- Type: Oswald 600 (carrier names, hook — condensed, signage-like, echoes hull lettering) + Manrope (labels) +
  Playfair Display 700 (end line).
- Structure (30 fps, 24.0 s, 120 BPM, 2 s per bar):
    0–2 s   hook: 3×3 mosaic of all nine ships + "Where are the world's top container lines from?" (fully visible on frame 1)
    2–20 s  nine carriers × 2 s: MSC tile expands to full panel; then right-to-left wipe with a seal-red edge per carrier;
            name pops up at 0.1 s, rule + flag chip + country + HQ city reveal at 0.85–1.35 s; Ken Burns on every photo
    20–23.4 end card: "Your cargo, any carrier." + LinkWin seal signature + linkwinco.com, faint seal echo cropped by the edge
    23.4–24 loop-back: mosaic tiles cascade back and the hook title returns, so the last frame ≈ the first frame.
- Safe zones: all text between y 220 and y 1600, and left of x 940 (Reels right rail).
- Logo: "Seal signature + echo" (tools/linkwin_mark.py) on the end card only.
- PRC compliance: no Taiwan entities/flags (Evergreen, Yang Ming, Wan Hai dropped); ZIM dropped; OOCL shown as
  "Hong Kong, China" with the national flag of the PRC. No carrier logos (names as text only; hull lettering is in the
  editorial photos). Strictly commercial.
- Facts (HQ, checked 17 Nov 2026 on Wikipedia infoboxes + press): MSC Geneva, Switzerland; Maersk Copenhagen, Denmark;
  CMA CGM Marseille, France; COSCO Shipping Shanghai, China; Hapag-Lloyd Hamburg, Germany; ONE global HQ Singapore,
  owned by Japan's NYK/MOL/K Line; HMM registered HQ moved to Busan, South Korea (EGM May 2026, Busan HQ opened
  12 Oct 2026 — Seoul Economic Daily, Herald Business); PIL Singapore; OOCL Hong Kong, China (COSCO Shipping group).
usage: python3 scripts/2026-11-17-reel.py [--preview t1,t2,...]   (default: full render to posts/2026-11-17/reel/)
"""
import os, sys, json, subprocess, shutil
from PIL import Image
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from linkwin_mark import MARK_CSS, signature, echo
OUT = os.path.join(ROOT, "posts", "2026-11-17", "reel")
WORK = "/tmp/reel-2026-11-17"
FPS, DUR = 30, 24.0
PANEL_W, PANEL_H = 1080, 1150

SHIPS = [  # name, country, line2, flag, photo file, focal x (0..1), credit
 ("MSC", "Switzerland", "Geneva", "ch", "reel-msc-harmony-iii-koper.jpg", .42, "Petar Milošević · CC BY-SA 4.0"),
 ("Maersk", "Denmark", "Copenhagen", "dk", "reel-maersk-hanoi-koper.jpg", .50, "Petar Milošević · CC BY-SA 4.0"),
 ("CMA CGM", "France", "Marseille", "fr", "reel-cma-cgm-kerguelen-hamburg.jpg", .72, "Matti Blume · CC BY-SA 4.0"),
 ("COSCO Shipping", "China", "Shanghai", "cn", "reel-cosco-shipping-himalayas-hamburg.jpg", .45, "Hummelhummel · CC BY-SA 4.0"),
 ("Hapag-Lloyd", "Germany", "Hamburg", "de", "reel-hapag-lloyd-tokyo-express-colon.jpg", .62, "Paul Harrison · CC BY-SA 4.0"),
 ("ONE", "Singapore", "Owned by Japan’s NYK, MOL and K Line", "sg", "reel-one-ship-tokyo-harbour.jpg", .45, "Syced · CC0"),
 ("HMM", "South Korea", "Busan", "kr", "reel-hmm-garam-barcelona.jpg", .50, "Ximonic (Simo Räsänen) · CC BY-SA 4.0"),
 ("PIL", "Singapore", "Pacific International Lines", "sg", "reel-pil-kota-rakyat.jpg", .62, "Flickr user 102748040@N03 · CC BY 2.0"),
 ("OOCL", "Hong Kong, China", "Part of the COSCO Shipping group", "cn", "reel-oocl-dalian.jpg", .60, "Bernard Spragg · CC0"),
]

ZOOM = {"ONE": (1.7, .36)}  # (extra zoom, focal y) where the ship sits small in the frame

def crops():
    os.makedirs(WORK, exist_ok=True)
    W, H = int(PANEL_W * 1.25), int(PANEL_H * 1.25)
    out = []
    for i, s in enumerate(SHIPS):
        im = Image.open(os.path.join(ROOT, "photos", s[4])).convert("RGB")
        z, fy = ZOOM.get(s[0], (1.0, .5))
        sc = max(W / im.width, H / im.height) * z
        im = im.resize((round(im.width * sc), round(im.height * sc)), Image.LANCZOS)
        x = min(max(0, round(im.width * s[5] - W / 2)), im.width - W)
        y = min(max(0, round(im.height * fy - H / 2)), im.height - H)
        p = os.path.join(WORK, f"shot{i}.jpg"); im.crop((x, y, x + W, y + H)).save(p, quality=94); out.append(p)
    return out

def html(shots):
    flag = lambda c: "../brand/flags/%s.svg" % c
    tiles = "".join(f'<div class="tile" id="tile{i}"><img src="file://{p}"></div>' for i, p in enumerate(shots))
    shotdivs = "".join(f'<div class="shot" id="shot{i}"><img src="file://{p}"></div>' for i, p in enumerate(shots))
    segs = "".join(f'<i class="seg"><b id="seg{i}"></b></i>' for i in range(len(SHIPS)))
    scenes = "".join(f'''<div class="scene" id="sc{i}">
  <div class="mask"><div class="name" id="nm{i}">{s[0]}</div></div>
  <div class="rule" id="ru{i}"></div>
  <div class="ctry"><img class="flag" id="fl{i}" src="{flag(s[3])}"><div class="ctxt"><div class="cn" id="cn{i}">{s[1]}</div><div class="city" id="ci{i}">{s[2]}</div></div></div>
</div>''' for i, s in enumerate(SHIPS))
    credits = "".join(f'<div class="credit" id="cr{i}">Photo: {s[6]} · Wikimedia Commons</div>' for i, s in enumerate(SHIPS))
    counters = "".join(f'<div class="kick" id="ck{i}"><span class="num">{i+1:02d} / {len(SHIPS):02d}</span><span class="dot"></span>Headquarters</div>' for i in range(len(SHIPS)))
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<link rel="stylesheet" href="../brand/fonts.css"><style>
:root{{--paper:#EFEBE3;--ink:#14222F;--red:#AC3E33;--slate:#5E6873}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1920px;overflow:hidden;background:var(--paper);color:var(--ink);font-family:Manrope,sans-serif}}
#stage{{position:absolute;inset:0;overflow:hidden}}
#panel{{position:absolute;left:0;top:0;width:{PANEL_W}px;height:{PANEL_H}px;overflow:hidden;background:#cfd3d4}}
.tile,.shot{{position:absolute;overflow:hidden;will-change:transform}}
.tile img,.shot img{{width:100%;height:100%;object-fit:cover;display:block;transform-origin:50% 55%}}
.shot{{left:0;top:0;width:{PANEL_W}px;height:{PANEL_H}px;opacity:0}}
#edge{{position:absolute;top:0;width:8px;height:{PANEL_H}px;background:var(--red);opacity:0;box-shadow:0 0 24px rgba(172,62,51,.45)}}
#fadeB{{position:absolute;left:0;right:0;top:{PANEL_H-330}px;height:330px;background:linear-gradient(rgba(239,235,227,0),rgba(239,235,227,.55) 55%,var(--paper));pointer-events:none}}
#fadeT{{position:absolute;left:0;right:0;top:0;height:300px;background:linear-gradient(rgba(10,18,26,.38),rgba(10,18,26,0));pointer-events:none}}
.credit{{position:absolute;left:72px;top:1158px;font-size:20px;font-weight:400;color:var(--slate);opacity:0;white-space:nowrap}}
#prog{{position:absolute;left:72px;width:864px;top:1200px;height:4px;display:flex;gap:8px;opacity:0}}
.seg{{flex:1;background:rgba(20,34,47,.14);position:relative;overflow:hidden;border-radius:2px}}
.seg b{{position:absolute;inset:0;background:var(--ink);transform-origin:0 50%;transform:scaleX(0)}}
.kick{{position:absolute;left:72px;top:1230px;font-size:24px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;color:var(--red);opacity:0;display:flex;align-items:center;gap:16px;white-space:nowrap}}
.kick .num{{color:var(--ink);letter-spacing:.1em}}
.kick .dot{{width:6px;height:6px;border-radius:50%;background:var(--slate);opacity:.6}}
#hook{{position:absolute;left:72px;top:1150px;width:870px}}
#hook .kick{{position:static;opacity:1}}
#htitle{{font-family:Oswald,sans-serif;font-weight:600;font-size:92px;line-height:1.02;text-transform:uppercase;margin-top:20px;letter-spacing:.005em}}
#htitle em{{font-style:normal;color:var(--red)}}
.scene{{position:absolute;left:72px;top:1272px;width:868px;height:320px}}
.mask{{overflow:hidden;height:176px;padding-top:4px}}
.name{{font-family:Oswald,sans-serif;font-weight:600;font-size:164px;line-height:1;text-transform:uppercase;white-space:nowrap;display:inline-block;transform:translateY(110%)}}
.rule{{position:absolute;top:192px;left:0;width:868px;height:2px;background:var(--ink);opacity:.25;transform-origin:0 50%;transform:scaleX(0)}}
.ctry{{position:absolute;top:216px;left:0;display:flex;align-items:center;gap:26px}}
.flag{{width:96px;height:72px;border-radius:9px;box-shadow:0 0 0 1px rgba(20,34,47,.16),0 8px 18px rgba(20,34,47,.14);object-fit:cover;opacity:0;transform:scale(.5)}}
.cn{{font-size:54px;font-weight:800;line-height:1.04;letter-spacing:-.01em;opacity:0;white-space:nowrap}}
.city{{font-size:26px;font-weight:600;color:var(--slate);line-height:1.3;margin-top:4px;opacity:0;white-space:nowrap}}
#end{{position:absolute;inset:0;background:var(--paper);overflow:hidden;clip-path:inset(0 0 0 100%)}}
#endedge{{position:absolute;top:0;width:8px;height:1920px;background:var(--red);opacity:0}}
#end .lw-echo{{--lw-echo:#14222F;--lw-echo-op:.04;--lw-echo-size:1100px}}
#endtext{{position:absolute;left:72px;top:640px;width:860px}}
#endtext .k{{font-size:24px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;color:var(--red)}}
#endtext h2{{font-family:'Playfair Display',serif;font-weight:700;font-size:118px;line-height:1.04;margin-top:30px;letter-spacing:-.01em}}
#endtext h2 span{{display:block}}
#endtext h2 .b{{color:var(--red)}}
#endrule{{width:860px;height:2px;background:var(--ink);opacity:.22;margin:64px 0 52px;transform-origin:0 50%}}
#endsig{{display:flex;align-items:center;justify-content:space-between;width:860px}}
#endsig .lw-sig{{--lw-ink:#14222F;--lw-sig-h:104px;gap:24px}}
#url{{font-size:36px;font-weight:800;letter-spacing:.02em}}
{MARK_CSS}
</style></head><body><div id="stage">
<div id="panel">{tiles}{shotdivs}<div id="edge"></div><div id="fadeT"></div><div id="fadeB"></div></div>
{credits}
<div id="prog">{segs}</div>
{counters}
<div id="hook"><div class="kick"><span class="num">Quick quiz</span><span class="dot"></span>9 container lines</div>
<div id="htitle">Where are the world’s top container lines <em>from?</em></div></div>
{scenes}
<div id="end">{echo("right", "380px", "-430px")}<div id="endtext"><div class="k">Any line · any lane</div>
<h2><span class="a">Your cargo,</span><span class="b">any carrier.</span></h2><div id="endrule"></div>
<div id="endsig">{signature()}<div id="url">linkwinco.com</div></div></div></div>
<div id="endedge"></div>
</div>
<script>
const N={len(SHIPS)}, PW={PANEL_W}, PH={PANEL_H}, G=8;
const $=id=>document.getElementById(id);
const cl=x=>Math.max(0,Math.min(1,x));
const ease=x=>{{x=cl(x);return x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2}};
const out3=x=>{{x=cl(x);return 1-Math.pow(1-x,3)}};
const back=x=>{{x=cl(x);const c1=1.5,c3=c1+1;return 1+c3*Math.pow(x-1,3)+c1*Math.pow(x-1,2)}};
const seg=(t,a,b)=>cl((t-a)/(b-a));
const TW=(PW-2*G)/3, TH=(PH-2*G)/3;
function tileRect(k){{return [ (k%3)*(TW+G), Math.floor(k/3)*(TH+G), TW, TH ]}}
// fit names to width
window.fit=()=>{{for(let i=0;i<N;i++){{const e=$('nm'+i);let fs=164;e.style.fontSize=fs+'px';while(e.scrollWidth>860&&fs>60){{fs-=2;e.style.fontSize=fs+'px'}}}}}};
function place(el,r){{el.style.left=r[0]+'px';el.style.top=r[1]+'px';el.style.width=r[2]+'px';el.style.height=r[3]+'px'}}
function render(t){{
  const S=i=>2+2*i;
  // ---- hook mosaic ----
  const loopIn=t>=23.4;
  for(let k=0;k<N;k++){{
    const el=$('tile'+k), r=tileRect(k); place(el,r);
    let op=1, sc=1, kb=1+0.05*cl(t/2);
    if(t>=2&&!loopIn) op = k==0?0:1-seg(t,2.1,2.45);
    if(t>=2.5&&!loopIn) op=0;
    if(loopIn){{const p=back(seg(t,23.42+k*0.035,23.67+k*0.035)); op=cl(seg(t,23.42+k*0.035,23.6+k*0.035)); sc=.86+.14*p; kb=1}}
    el.style.opacity=op; el.style.transform=`scale(${{sc}})`; el.firstChild.style.transform=`scale(${{kb}})`;
  }}
  // ---- shots ----
  let edgeX=null;
  for(let i=0;i<N;i++){{
    const el=$('shot'+i), s=S(i), u=t-s; let vis=(t>=s && t<s+2+0.45 && t<20.5);
    el.style.opacity=vis?1:0; if(!vis)continue;
    const dir=i%2?-1:1, p=cl((t-s)/2.4);
    let kbS=1.045+0.07*p, kbX=dir*(-14+28*p);
    let tx=0;
    if(i==0){{ const e=ease(seg(t,2.0,2.45)), r0=tileRect(0);
      place(el,[r0[0]*(1-e), r0[1]*(1-e), r0[2]+(PW-r0[2])*e, r0[3]+(PH-r0[3])*e]); el.style.clipPath='none';
      el.style.zIndex=5; }}
    else {{ place(el,[0,0,PW,PH]); const w=ease(seg(t,s,s+0.38)); el.style.clipPath=`inset(0 0 0 ${{(1-w)*100}}%)`; el.style.zIndex=5+i;
      tx=(1-w)*70; if(w>0&&w<1) edgeX=(1-w)*PW-4; }}
    const nx=t-S(i+1); if(nx>=0) tx-=70*ease(cl(nx/0.38));
    el.style.transform=`translateX(${{tx}}px)`;
    el.firstChild.style.transform=`translateX(${{kbX}}px) scale(${{kbS}})`;
  }}
  $('edge').style.opacity=edgeX===null?0:1; if(edgeX!==null)$('edge').style.left=edgeX+'px';
  // ---- hook text ----
  let hop = t<2 ? 1-seg(t,1.82,2.0) : (loopIn? out3(seg(t,23.55,23.85)) : 0);
  let hy = t<2 ? -40*ease(seg(t,1.82,2.0)) : (loopIn? 30*(1-out3(seg(t,23.55,23.85))) : 0);
  $('hook').style.opacity=hop; $('hook').style.transform=`translateY(${{hy}}px)`;
  // the red "from?" flashes once on the hook
  const fl = t<1.2 ? 0.55+0.45*Math.abs(Math.cos(Math.PI*cl(t/0.6))) : 1; $('htitle').querySelector('em').style.opacity=fl;
  // ---- progress / kicker ----
  const quiz=t>=2&&t<20;
  $('prog').style.opacity = t<2?0: t<20? seg(t,2,2.2) : 1-seg(t,20,20.25);
  for(let i=0;i<N;i++){{
    const s=S(i), b=$('seg'+i);
    b.style.transform=`scaleX(${{t>=s+2?1:cl((t-s)/2)}})`;
    const on = t>=s && t<s+2; const kop = on ? Math.min(seg(t,s,s+0.2), 1-seg(t,s+1.85,s+2.0)) : 0;
    $('ck'+i).style.opacity = (i==0? kop : (on? 1 : 0)) * (i==N-1? 1 : 1);
    if(i>0 && on) $('ck'+i).style.opacity=1;
    if(i==N-1 && on) $('ck'+i).style.opacity=1-seg(t,s+1.85,s+2.0);
    $('cr'+i).style.opacity = on ? Math.min(seg(t,s+0.2,s+0.45), 1-seg(t,s+1.8,s+1.95)) : 0;
    // scene text
    const u=t-s, nm=$('nm'+i);
    const inP=back(seg(u,0.10,0.46)), outP=ease(seg(u,1.84,2.0));
    nm.style.transform=`translateY(${{(1-inP)*110 - outP*110}}%)`;
    $('ru'+i).style.transform=`scaleX(${{out3(seg(u,0.80,1.12))*(1-outP)}})`;
    const fp=back(seg(u,0.86,1.12)); const f=$('fl'+i);
    f.style.opacity=cl(seg(u,0.86,0.98))*(1-outP); f.style.transform=`scale(${{.5+.5*fp}})`;
    const c=$('cn'+i), cp=out3(seg(u,0.94,1.24)); c.style.opacity=cp*(1-outP); c.style.transform=`translateX(${{-28*(1-cp)}}px)`;
    const y=$('ci'+i), yp=out3(seg(u,1.04,1.34)); y.style.opacity=yp*(1-outP); y.style.transform=`translateX(${{-22*(1-yp)}}px)`;
    $('sc'+i).style.visibility=(u>-0.05&&u<2.05)?'visible':'hidden';
  }}
  // ---- end card ----
  const ew=ease(seg(t,20,20.4)); const eo=1-seg(t,23.4,23.62);
  $('end').style.clipPath=`inset(0 0 0 ${{(1-ew)*100}}%)`; $('end').style.opacity=eo;
  $('endedge').style.opacity=(ew>0&&ew<1)?1:0; $('endedge').style.left=((1-ew)*1080-4)+'px';
  const e1=out3(seg(t,20.25,20.7)), e2=out3(seg(t,20.45,20.9)), e3=out3(seg(t,20.8,21.3)), e4=out3(seg(t,21.0,21.5));
  const q=document.querySelector('#endtext .k'); q.style.opacity=e1;
  const a=document.querySelector('#endtext .a'); a.style.opacity=e1; a.style.transform=`translateY(${{40*(1-e1)}}px)`;
  const bb=document.querySelector('#endtext .b'); bb.style.opacity=e2; bb.style.transform=`translateY(${{40*(1-e2)}}px)`;
  $('endrule').style.transform=`scaleX(${{e3}})`;
  const sg=$('endsig'); sg.style.opacity=e4; sg.style.transform=`translateY(${{24*(1-e4)}}px)`;
  const ec=document.querySelector('#end .lw-echo'); ec.style.transform=`rotate(${{-8+6*cl((t-20)/3.4)}}deg)`;
}}
window.render=render; render(0);
</script></body></html>'''

def main():
    import time
    from playwright.sync_api import sync_playwright
    shots = crops()
    tpl = os.path.join(ROOT, "templates", "2026-11-17-reel-en.html")
    open(tpl, "w", encoding="utf-8").write(html(shots))
    preview = None
    if "--preview" in sys.argv:
        preview = [float(x) for x in sys.argv[sys.argv.index("--preview") + 1].split(",")]
    os.makedirs(OUT, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=os.environ.get("CHROME", "/usr/bin/google-chrome"),
                              args=["--font-render-hinting=none", "--force-color-profile=srgb"])
        pg = b.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
        pg.goto("file://" + tpl, wait_until="networkidle")
        pg.evaluate("document.fonts.ready.then(()=>true)")
        pg.wait_for_timeout(500)
        bad = pg.evaluate("[...document.fonts].filter(f=>f.status==='error').map(f=>f.family)")
        imgs = pg.evaluate("[...document.images].filter(i=>!i.complete||i.naturalWidth===0).map(i=>i.src)")
        if bad or imgs: print("FONT/IMG problems:", bad, imgs); sys.exit(2)
        pg.evaluate("fit()")
        print("name sizes:", pg.evaluate("[...Array(9).keys()].map(i=>document.getElementById('nm'+i).style.fontSize)"))
        print("text boxes:", pg.evaluate("""(()=>{const o={};for(const id of ['hook','htitle','sc0','sc3','cr7','ck0','endtext','prog']){const r=document.getElementById(id).getBoundingClientRect();o[id]=[Math.round(r.left),Math.round(r.top),Math.round(r.right),Math.round(r.bottom)]}
 for(let i=0;i<9;i++){const n=document.getElementById('nm'+i).getBoundingClientRect(), c=document.getElementById('ci'+i).getBoundingClientRect(); o['nm'+i]=Math.round(n.right); o['ci'+i]=[Math.round(c.right),Math.round(c.bottom)]} return o})()"""))
        if preview:
            os.makedirs(os.path.join(WORK, "preview"), exist_ok=True)
            for t in preview:
                pg.evaluate(f"render({t})")
                pg.screenshot(path=os.path.join(WORK, "preview", f"t{t:05.2f}.png"))
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
            if f in (0, 27): pg.screenshot(path=os.path.join(WORK, f"frame{f}.png"))
            if f % 90 == 0: print(f"frame {f}/{n}  {time.time()-t0:.0f}s", flush=True)
        ff.stdin.close(); ff.wait(); b.close()
    # cover = hook frame (t = 0.9 s, "from?" fully lit)
    wav = os.path.join(WORK, "bed.wav")
    subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "2026-11-17-reel-audio.py"), wav], check=True)
    mp4 = os.path.join(OUT, "2026-11-17-reel-container-lines-en.mp4")
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", silent, "-i", wav, "-map", "0:v", "-map", "1:a",
                    "-c:v", "copy", "-af", "loudnorm=I=-18:TP=-2:LRA=7", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                    "-movflags", "+faststart", "-shortest", mp4], check=True)
    cover = os.path.join(OUT, "2026-11-17-reel-container-lines-en-cover.jpg")
    Image.open(os.path.join(WORK, "frame27.png")).convert("RGB").save(cover, "JPEG", quality=92, subsampling=0, optimize=True)
    print(mp4, os.path.getsize(mp4) // 1024, "KB"); print(cover)

if __name__ == "__main__":
    main()
