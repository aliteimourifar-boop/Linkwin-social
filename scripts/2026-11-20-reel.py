#!/usr/bin/env python3
"""2026-11-20 — Reel "Then / Now": China, then vs now (EN). Idea from Ali (18 Nov reference reel), real photos only.

Creative brief
- Concept: "Contact Sheet". Two stacked archive-style frames per scene: THEN (top) and NOW (bottom), same city,
  the same place where Commons has it. NOW wipes in from the right behind a seal-red edge while the year rolls
  forward (1988 -> 2026). Five scenes, then an end card that links the story to LinkWin's work: sourcing and shipping from China.
- Photos: ONLY real, dated photographs from Wikimedia Commons with a verified date, author and licence (photos/CREDITS.md).
  No AI imagery, no retouching beyond crop/scale. Each frame carries its own credit.
- Tone / palette: darkroom ink #101317, warm paper text #F2EDE4, seal red #AC3E33, muted brass #B89A6A.
  Type: Oswald 600 (years, headers), Playfair Display italic (one-liners), Manrope (labels/credits). Different from
  17 Nov (light paper, quiz).
- Timing (30 fps, 24.0 s): 0-2.0 hook over scene 1 (both frames already visible on frame 1);
  scene k starts at 0, 4.0, 7.8, 11.6, 15.4 (3.8 s each; NOW wipe 0.55-1.25 s); 19.2-24 end card; 23.55-24 fade back to the hook for the loop.
- Safe zones: text between y 230 and 1600 and left of x 940.
- Logo: tools/linkwin_mark.py signature + faint echo on the end card only.
- PRC compliance: positive development story, commercial; Hong Kong/Taiwan not shown; no politics, no people in focus.
usage: python3 scripts/2026-11-20-reel.py [--preview t1,t2,...]
"""
import os, sys, subprocess, time
from PIL import Image
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from linkwin_mark import MARK_CSS, signature, echo
OUT = os.path.join(ROOT, "posts", "2026-11-20", "reel")
WORK = "/tmp/reel-2026-11-20"
FPS, DUR = 30, 24.0
PW, PH = 1080, 600   # photo frame size
SLUG = "2026-11-20-reel-china-then-now-en"

# header, one-liner, (then file, year, focal x, credit), (now file, year, focal x, credit)
SCENES = [
 ("Shanghai · the Huangpu River", "Busy river docks → the Lujiazui skyline",
  ("tn-shanghai-pudong-1988.jpg", 1988, .55, "Jan Kranendonk · CC0"),
  ("tn-shanghai-pudong-2026.jpg", 2026, .50, "DvTor8303 · CC0")),
 ("Shanghai · Suzhou Creek & the Bund", "Same bridge, new horizon",
  ("tn-shanghai-suzhou-creek-1987.jpg", 1987, .50, "Till Niermann · CC BY-SA 3.0"),
  ("tn-shanghai-suzhou-creek-2025.jpg", 2025, .50, "Supanut Arunoprayote · CC BY 4.0")),
 ("Guangzhou · the city", "Trolleybus terminus → Zhujiang New Town",
  ("tn-guangzhou-trolleybuses-1991.jpg", 1991, .50, "lindsaybridge · CC BY-SA 2.0"),
  ("tn-guangzhou-zhujiang-new-town-2017.jpg", 2017, .52, "Nissangeniss · CC BY-SA 4.0")),
 ("Guangzhou · the Canton Fair", "One trade-fair stand → the Pazhou complex",
  ("tn-canton-fair-1986.jpg", 1986, .45, "Vermontalf · CC BY-SA 4.0"),
  ("tn-canton-fair-complex-2023.jpg", 2023, .50, "Tim Wu · CC BY-SA 4.0")),
 ("Shanghai · the port", "Cargo by hand cart → Yangshan deep-water port",
  ("tn-shanghai-port-1976.jpg", 1976, .40, "Karl-Heinz Wellmann · CC BY-SA 4.0"),
  ("tn-yangshan-port-2013.jpg", 2013, .55, "Bruno Corpet · CC BY-SA 3.0")),
]
FY = {"tn-shanghai-pudong-1988.jpg": .30, "tn-shanghai-port-1976.jpg": .45, "tn-canton-fair-1986.jpg": .45}
STARTS = [0.0, 4.0, 7.8, 11.6, 15.4]
END_T = 19.2

def crops():
    os.makedirs(WORK, exist_ok=True)
    W, H = int(PW * 1.18), int(PH * 1.18)
    out = []
    for i, s in enumerate(SCENES):
        pair = []
        for j, (f, yr, fx, cr) in enumerate((s[2], s[3])):
            im = Image.open(os.path.join(ROOT, "photos", f)).convert("RGB")
            sc = max(W / im.width, H / im.height)
            im = im.resize((round(im.width * sc), round(im.height * sc)), Image.LANCZOS)
            x = min(max(0, round(im.width * fx - W / 2)), im.width - W)
            y = min(max(0, round(im.height * FY.get(f, .5) - H / 2)), im.height - H)
            p = os.path.join(WORK, f"s{i}{'tn'[j]}.jpg"); im.crop((x, y, x + W, y + H)).save(p, quality=94); pair.append(p)
        out.append(pair)
    return out

def html(shots):
    scenes = ""
    for i, (s, (pt, pn)) in enumerate(zip(SCENES, shots)):
        scenes += f'''<div class="scene" id="sc{i}"><div class="bd"><img src="file://{pn}"></div>
 <div class="hdr" id="hd{i}"><div class="k"><span class="n">{i+1:02d}</span>{s[0]}</div><div class="one">{s[1]}</div></div>
 <div class="fr top"><img id="it{i}" src="file://{pt}"><div class="shade"></div>
   <div class="lab"><div class="tag">THEN</div><div class="yr">{s[2][1]}</div></div><div class="cr">Photo: {s[2][3]} · Wikimedia Commons</div></div>
 <div class="fr bot"><div class="ghost"><img id="ig{i}" src="file://{pt}"></div>
   <div class="nowclip" id="nc{i}"><img id="in{i}" src="file://{pn}"><div class="shade"></div>
   <div class="lab"><div class="tag red">NOW</div><div class="yr" id="yr{i}">{s[3][1]}</div></div><div class="cr">Photo: {s[3][3]} · Wikimedia Commons</div></div>
   <div class="edge" id="ed{i}"></div></div>
</div>'''
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<link rel="stylesheet" href="../brand/fonts.css"><style>
:root{{--ink:#101317;--paper:#F2EDE4;--red:#AC3E33;--brass:#B89A6A;--lw-ink:rgba(242,237,228,.9)}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1920px;overflow:hidden;background:var(--ink);color:var(--paper);font-family:Manrope,sans-serif}}
#grain{{position:absolute;inset:0;background:radial-gradient(120% 60% at 50% 45%,rgba(184,154,106,.10),rgba(0,0,0,0) 70%)}}
.scene{{position:absolute;inset:0;opacity:0;background:var(--ink)}}
.bd{{position:absolute;inset:-60px;overflow:hidden}} .bd img{{width:100%;height:100%;object-fit:cover;filter:blur(38px) brightness(.28) saturate(.8)}}
.hdr{{position:absolute;left:72px;top:232px;width:860px}}
.hdr .k{{font-family:Oswald,sans-serif;font-weight:600;font-size:40px;letter-spacing:.06em;text-transform:uppercase;color:var(--paper);white-space:nowrap}}
.hdr .k .n{{color:var(--red);margin-right:20px}}
.hdr .one{{font-family:'Playfair Display',serif;font-style:italic;font-size:36px;color:rgba(242,237,228,.78);margin-top:8px;white-space:nowrap}}
.fr{{position:absolute;left:0;width:{PW}px;height:{PH}px;overflow:hidden;background:#1b1f24}}
.fr.top{{top:370px}} .fr.bot{{top:984px}}
.fr img{{position:absolute;left:0;top:0;width:{PW}px;height:{PH}px;object-fit:cover;transform-origin:50% 50%}}
.ghost{{position:absolute;inset:0;filter:grayscale(1) brightness(.35) blur(6px);transform:scale(1.05)}}
.nowclip{{position:absolute;inset:0;clip-path:inset(0 0 0 100%)}}
.shade{{position:absolute;left:0;right:0;bottom:0;height:260px;background:linear-gradient(rgba(16,19,23,0),rgba(16,19,23,.78))}}
.lab{{position:absolute;left:72px;bottom:44px}}
.tag{{font-family:Manrope,sans-serif;font-weight:800;font-size:22px;letter-spacing:.22em;color:var(--brass)}}
.tag.red{{color:#E0705F}}
.yr{{font-family:Oswald,sans-serif;font-weight:600;font-size:112px;line-height:1;margin-top:6px;letter-spacing:.01em;font-variant-numeric:tabular-nums;color:#fff}}
.cr{{position:absolute;right:150px;bottom:20px;font-size:17px;color:rgba(255,255,255,.72);white-space:nowrap;text-align:right}}
.edge{{position:absolute;top:0;width:8px;height:{PH}px;background:var(--red);box-shadow:0 0 26px rgba(172,62,51,.55);opacity:0}}
#prog{{position:absolute;left:72px;top:1612px;width:300px;height:4px;display:flex;gap:8px}}
#prog i{{flex:1;background:rgba(242,237,228,.18);position:relative;overflow:hidden}}
#prog b{{position:absolute;inset:0;background:var(--paper);transform-origin:0 50%;transform:scaleX(0)}}
#hook{{position:absolute;left:0;right:0;top:220px;height:150px}}
#hook .k{{position:absolute;left:72px;top:14px;font-family:Manrope;font-weight:800;font-size:24px;letter-spacing:.2em;color:var(--brass);white-space:nowrap}}
#hook h1{{position:absolute;left:72px;top:46px;font-family:Oswald,sans-serif;font-weight:600;font-size:84px;line-height:1;text-transform:uppercase;letter-spacing:.01em;white-space:nowrap}}
#hook h1 em{{font-style:normal;color:var(--red)}}
#end{{position:absolute;inset:0;background:var(--ink);overflow:hidden;opacity:0}}
#end .bg{{position:absolute;left:0;top:0;width:1080px;height:1920px;object-fit:cover;filter:brightness(.32) saturate(.7)}}
#end .lw-echo{{--lw-echo:#F2EDE4;--lw-echo-op:.05;--lw-echo-size:1150px}}
#endtext{{position:absolute;left:72px;top:600px;width:860px}}
#endtext .k{{font-size:24px;font-weight:800;letter-spacing:.2em;text-transform:uppercase;color:var(--brass)}}
#endtext h2{{font-family:'Playfair Display',serif;font-weight:700;font-size:96px;line-height:1.06;margin-top:28px}}
#endtext h2 span{{display:block}} #endtext h2 .r{{color:#E0705F}}
#endtext p{{font-size:34px;line-height:1.45;margin-top:34px;color:rgba(242,237,228,.86)}}
#endrule{{width:860px;height:2px;background:var(--paper);opacity:.25;margin:56px 0 48px;transform-origin:0 50%}}
#endsig{{display:flex;align-items:center;justify-content:space-between;width:860px}}
#endsig .url{{font-family:Oswald;font-weight:600;font-size:40px;letter-spacing:.04em}}
#fade{{position:absolute;inset:0;background:var(--ink);opacity:0}}
{MARK_CSS}
</style></head><body><div id="grain"></div>
{scenes}
<div id="hook"><div class="k">REAL, DATED PHOTOS · SAME CITIES</div><h1>China: then <em>vs</em> now</h1></div>
<div id="prog">{''.join(f'<i><b id="pg{i}"></b></i>' for i in range(len(SCENES)))}</div>
<div id="end"><img class="bg" src="file://{shots[4][1]}">{echo("right","-260px","-330px")}
 <div id="endtext"><div class="k" id="ek">From these ports to yours</div>
 <h2 id="eh"><span>Sourced in China.</span><span class="r">Shipped to you.</span></h2>
 <p id="ep">LinkWin Trading sources, inspects and ships ferroalloys, metals and industrial goods from China.</p>
 <div id="endrule"></div><div id="endsig">{signature()}<div class="url">linkwinco.com</div></div></div></div>
<div id="fade"></div>
<script>
const S={STARTS}, END={END_T}, DUR={DUR}, YT={[s[2][1] for s in SCENES]}, YN={[s[3][1] for s in SCENES]};
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x)), ease=x=>{{x=cl(x);return x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2}}, eo=x=>1-Math.pow(1-cl(x),3);
const $=id=>document.getElementById(id);
function render(t){{
  for(let i=0;i<S.length;i++){{
    const t0=S[i], t1=(i+1<S.length?S[i+1]:END), lt=t-t0, on=(t>=t0-0.0001&&t<t1+0.35);
    const sc=$('sc'+i);
    // cross-dissolve between scenes over 0.35s
    let op=0; if(on){{op=i==0?1:eo(lt/0.35); if(t>t1) op=1-eo((t-t1)/0.35); if(i==0&&t>t1) op=1-eo((t-t1)/0.35)}}
    sc.style.opacity=op; sc.style.zIndex=10+i;
    const w0=(i==0?2.05:0.55), w1=w0+0.7;  // NOW wipe window (scene 1: starts after hook... but hook frame shows both)
    let p=ease((lt-w0)/(w1-w0)); if(i==0&&t<2.05) p=1;   // hook: both frames visible on frame 1
    if(i==0&&t>=2.05&&t<2.75){{p=ease((lt-2.05)/0.7)}}   // replay the wipe once after the hook
    if(i==0&&t>=2.05&&t<2.08) p=0;
    $('nc'+i).style.clipPath=`inset(0 0 0 ${{(1-p)*100}}%)`;
    const e=$('ed'+i); e.style.left=((1-p)*1080-4)+'px'; e.style.opacity=(p>0.002&&p<0.998)?1:0;
    const yr=Math.round(YT[i]+(YN[i]-YT[i])*p); $('yr'+i).textContent=yr;
    const kb=1+0.06*cl(lt/(t1-t0+0.35));
    $('it'+i).style.transform=`scale(${{1.0+0.05*cl(lt/4)}}) translateX(${{-10*cl(lt/4)}}px)`;
    $('in'+i).style.transform=`scale(${{kb}}) translateX(${{12*cl(lt/4)}}px)`;
    const h=$('hd'+i); const hin=i==0?eo((t-2.0)/0.4):eo(lt/0.45);
    h.style.opacity=hin; h.style.transform=`translateY(${{(1-hin)*24}}px)`;
    $('pg'+i).style.transform=`scaleX(${{cl((t-t0)/(t1-t0))}})`;
  }}
  // hook band (covers scene-1 header zone until 2.0s)
  const hk=$('hook'); const ho=t<1.85?1:1-eo((t-1.85)/0.3); hk.style.opacity=ho; hk.style.zIndex=40;
  hk.querySelector('h1').style.transform=`translateY(${{t<1.85?0:-(1-ho)*30}}px)`;
  // end card
  const en=$('end'); en.style.zIndex=50; const eop=eo((t-END)/0.5); en.style.opacity=t<END?0:eop;
  en.querySelector('.bg').style.transform=`scale(${{1.04+0.05*cl((t-END)/4.8)}})`;
  const st=(id,d)=>{{const v=eo((t-END-d)/0.5); $(id).style.opacity=v; $(id).style.transform=`translateY(${{(1-v)*28}}px)`}};
  st('ek',0.25); st('eh',0.45); st('ep',0.9); st('endsig',1.3);
  $('endrule').style.transform=`scaleX(${{eo((t-END-1.1)/0.6)}})`;
  $('prog').style.opacity=t<END?1:1-eo((t-END)/0.3); $('prog').style.zIndex=45;
  // loop: fade to ink then the hook frame is frame 0
  const f=$('fade'); f.style.zIndex=60; f.style.opacity=t>23.55?eo((t-23.55)/0.45):0;
}}
</script></body></html>'''

def main():
    from playwright.sync_api import sync_playwright
    preview = None
    if "--preview" in sys.argv: preview = [float(x) for x in sys.argv[sys.argv.index("--preview") + 1].split(",")]
    shots = crops()
    tpl = os.path.join(ROOT, "templates", SLUG + ".html")
    open(tpl, "w", encoding="utf-8").write(html(shots))
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
        print("boxes:", pg.evaluate("""(()=>{const o={};document.querySelectorAll('.hdr .k,.hdr .one,.cr,#hook h1,#endtext h2,#endtext p,#endsig').forEach((e,i)=>{const r=e.getBoundingClientRect();o[i+':'+(e.id||e.className)]=[Math.round(r.left),Math.round(r.top),Math.round(r.right),Math.round(r.bottom)]});return o})()"""))
        if preview:
            os.makedirs(os.path.join(WORK, "preview"), exist_ok=True)
            for t in preview:
                pg.evaluate(f"render({t})"); pg.screenshot(path=os.path.join(WORK, "preview", f"t{t:05.2f}.png"))
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
            if f == 15: pg.screenshot(path=os.path.join(WORK, "cover.png"))
            if f % 90 == 0: print(f"frame {f}/{n}  {time.time()-t0:.0f}s", flush=True)
        ff.stdin.close(); ff.wait(); b.close()
    wav = os.path.join(WORK, "bed.wav")
    subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "2026-11-20-reel-audio.py"), wav], check=True)
    mp4 = os.path.join(OUT, SLUG + ".mp4")
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", silent, "-i", wav, "-map", "0:v", "-map", "1:a",
                    "-c:v", "copy", "-af", "loudnorm=I=-18:TP=-2:LRA=7", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                    "-movflags", "+faststart", "-shortest", mp4], check=True)
    cover = os.path.join(OUT, SLUG + "-cover.jpg")
    Image.open(os.path.join(WORK, "cover.png")).convert("RGB").save(cover, "JPEG", quality=92, subsampling=0, optimize=True)
    print(mp4, os.path.getsize(mp4) // 1024, "KB"); print(cover)

if __name__ == "__main__":
    main()
