#!/usr/bin/env python3
"""2026-11-21 — Reel "FOB vs CIF vs DDP: who pays, and when is the risk yours?" (EN, 24 s, how-it-works / X vs Y).

Creative brief
- Concept: "Route Ruler". A photo window on top (Ken Burns), below it one horizontal route ruler with five stations
  (Factory · China port · At sea · Your port · Your door). For each term a teal bar fills the part the SELLER pays,
  the rest stays amber (YOU pay), and a seal-red pin drops where the RISK passes to the buyer. CIF is the twist:
  cost runs to your port, but the pin lands back in China.
- Tone / palette (light, after the 20 Nov dark reel): ivory #F3EEE5, harbour ink #13202B, teal #1F7A74 (seller),
  amber #D9822B (buyer), seal red #AC3E33 (risk pin). Type: Space Grotesk 700 (terms, headings), Manrope (text).
- Facts: ICC Incoterms(R) 2020 (iccwbo.org, fetched 21 Nov 2026): FOB = delivered on board the vessel at the port of
  shipment, risk passes then, buyer pays main carriage; CIF = seller pays carriage + minimum insurance (Institute Cargo
  Clauses (C) default) to the destination port, risk passes when on board at the port of shipment; DDP = seller delivers
  at the named destination, cleared for import with duties paid, ready for unloading. FOB/CIF are sea/inland-waterway
  rules; for containers ICC guidance points to FCA/CIP.
- Timing (30 fps, 24.0 s): hook 0-2.2 over scene 1 (title visible on frame 1); FOB 2.2-7.2; CIF 7.2-12.2; DDP 12.2-17.0;
  container tip 17.0-19.6; end card 19.6-24; 23.55-24 fade to ivory for the loop (frame 0 = ivory-based hook).
- Safe zones: text between y 230 and 1600 and left of x 940.
- Photos: existing Commons files (photos/CREDITS.md), credit on each frame.
- Logo: tools/linkwin_mark.py signature + faint echo on the end card only.
- PRC compliance: neutral trade education, no politics, no maps, no flags.
usage: python3 scripts/2026-11-21-reel.py [--preview t1,t2,...]
"""
import os, sys, subprocess, time
from PIL import Image
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from linkwin_mark import MARK_CSS, signature, echo
OUT = os.path.join(ROOT, "posts", "2026-11-21", "reel")
WORK = "/tmp/reel-2026-11-21"
FPS, DUR = 30, 24.0
PW, PH = 1080, 860
SLUG = "2026-11-21-reel-fob-cif-ddp-en"
STATIONS = ["Factory", "China port", "At sea", "Your port", "Your door"]
X = [130, 312, 494, 676, 858]   # station x on the ruler (inside 72..940)
# term, full name, photo, focal x, credit, cost-to station, risk station, seller line, you line
SCENES = [
 ("FOB", "Free On Board", "tn-yangshan-port-2013.jpg", .55, "Yangshan Port · Bruno Corpet · CC BY-SA 3.0", 1, 1,
  "Seller: export clearance and loading on board in China.", "You: ocean freight, insurance, import duties."),
 ("CIF", "Cost, Insurance & Freight", "reel-cosco-shipping-himalayas-hamburg.jpg", .5, "Hummelhummel · CC BY-SA 4.0", 3, 1,
  "Seller pays freight and basic insurance to your port…", "…but the risk is yours once the goods are on board in China."),
 ("DDP", "Delivered Duty Paid", "shenzhen-shennan-east-road-dusk.jpg", .5, "Dinkun Chen · CC BY-SA 4.0", 4, 4,
  "Seller: everything to your door, import duties included.", "You: unload the goods."),
]
TIP_PHOTO = ("ningbo-zhenhai-port-dusk.jpg", .58, "Ningbo-Zhoushan Port · Nbfreeh · CC BY-SA 4.0")
STARTS = [0.0, 7.2, 12.2]; WIN = [2.2, 0.0, 0.0]   # scene 1 animates after the hook
TIP_T, END_T = 17.0, 19.6

def crop(f, fx, name):
    os.makedirs(WORK, exist_ok=True)
    W, H = int(PW * 1.15), int(PH * 1.15)
    im = Image.open(os.path.join(ROOT, "photos", f)).convert("RGB")
    sc = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * sc), round(im.height * sc)), Image.LANCZOS)
    x = min(max(0, round(im.width * fx - W / 2)), im.width - W); y = (im.height - H) // 2
    p = os.path.join(WORK, name); im.crop((x, y, x + W, y + H)).save(p, quality=94); return p

def ruler(i):
    st = "".join(f'<div class="st" style="left:{x}px"><i></i><span>{n}</span></div>' for x, n in zip(X, STATIONS))
    return f'''<div class="ruler" id="ru{i}"><div class="track"></div><div class="you" id="yo{i}"></div><div class="sel" id="se{i}"></div>{st}
  <div class="pin" id="pi{i}" style="left:{X[SCENES[i][6]]}px"><b></b><span>Risk passes to you</span></div></div>'''

def html(shots, tip, endbg):
    sc = ""
    for i, s in enumerate(SCENES):
        sc += f'''<div class="scene" id="sc{i}"><div class="ph"><img id="im{i}" src="file://{shots[i]}"><div class="cr">Photo: {s[4]} · Wikimedia Commons</div></div>
 <div class="hd" id="hd{i}"><div class="n">0{i+1} / 03</div><div class="t">{s[0]}</div><div class="f">{s[1]}</div></div>
 {ruler(i)}
 <div class="lines"><p class="l1" id="la{i}"><i class="dot t"></i>{s[7]}</p><p class="l2" id="lb{i}"><i class="dot a"></i>{s[8]}</p></div></div>'''
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<link rel="stylesheet" href="../brand/fonts.css"><style>
:root{{--iv:#F3EEE5;--ink:#13202B;--teal:#1F7A74;--amb:#D9822B;--red:#AC3E33;--lw-ink:#13202B;--lw-seal:#AC3E33}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1920px;overflow:hidden;background:var(--iv);color:var(--ink);font-family:Manrope,sans-serif}}
.scene{{position:absolute;inset:0;opacity:0;background:var(--iv)}}
.ph{{position:absolute;left:0;top:0;width:{PW}px;height:{PH}px;overflow:hidden}}
.ph img{{position:absolute;left:0;top:0;width:{PW}px;height:{PH}px;object-fit:cover;transform-origin:50% 50%}}
.ph:after{{content:"";position:absolute;inset:0;background:linear-gradient(rgba(19,32,43,.55),rgba(19,32,43,0) 30%,rgba(19,32,43,0) 80%,rgba(19,32,43,.35))}}
.cr{{position:absolute;left:72px;bottom:18px;font-size:17px;color:rgba(255,255,255,.85);z-index:2;white-space:nowrap}}
.hd{{position:absolute;left:72px;top:890px;width:860px}}
.hd .n{{font:800 22px/1 Manrope;letter-spacing:.2em;color:var(--red)}}
.hd .t{{font:700 150px/1 'Space Grotesk';letter-spacing:-.03em;margin-top:14px}}
.hd .f{{font:600 38px/1.2 Manrope;color:#4A5A66;margin-top:6px}}
.ruler{{position:absolute;left:0;top:1262px;width:1080px;height:170px}}
.track{{position:absolute;left:{X[0]}px;width:{X[-1]-X[0]}px;top:60px;height:14px;border-radius:7px;background:rgba(19,32,43,.10)}}
.sel,.you{{position:absolute;left:{X[0]}px;top:60px;height:14px;border-radius:7px;width:0}}
.sel{{background:var(--teal)}} .you{{background:var(--amb)}}
.st{{position:absolute;top:52px;width:0}}
.st i{{position:absolute;left:-15px;top:0;width:30px;height:30px;border-radius:50%;background:var(--iv);border:4px solid var(--ink)}}
.st span{{position:absolute;top:46px;left:-80px;width:160px;text-align:center;font:700 22px/1.2 Manrope;color:#3B4A55}}
.pin{{position:absolute;top:-58px;width:0;opacity:0}}
.pin b{{position:absolute;left:-16px;top:0;width:32px;height:32px;border-radius:50% 50% 50% 0;transform:rotate(-45deg);background:var(--red)}}
.pin b:after{{content:"";position:absolute;left:10px;top:10px;width:12px;height:12px;border-radius:50%;background:var(--iv)}}
.pin span{{position:absolute;top:-44px;left:-20px;white-space:nowrap;font:800 22px/1 Manrope;letter-spacing:.06em;text-transform:uppercase;color:var(--red)}}
#pi2 span{{left:auto;right:-20px}}
.lines{{position:absolute;left:72px;top:1430px;width:850px}}
.lines p{{font:600 31px/1.3 Manrope;padding-left:44px;position:relative;margin-bottom:18px}}
.dot{{position:absolute;left:0;top:9px;width:24px;height:24px;border-radius:50%}} .dot.t{{background:var(--teal)}} .dot.a{{background:var(--amb)}}
#legend{{position:absolute;left:72px;top:1568px;font:700 20px/1 Manrope;color:#5A6873;display:flex;gap:28px}}
#legend i{{display:inline-block;width:16px;height:16px;border-radius:50%;margin-right:8px;vertical-align:-2px}}
#hook{{position:absolute;left:72px;top:930px;width:860px}}
#hook .k{{font:800 24px/1 Manrope;letter-spacing:.2em;color:var(--red)}}
#hook h1{{font:700 150px/0.96 'Space Grotesk';letter-spacing:-.03em;color:var(--ink);margin-top:22px}} #hook h1 span{{color:var(--teal)}} #hook h1 em{{font-style:normal;color:var(--amb)}}
#hook p{{font:600 40px/1.3 Manrope;color:#3B4A55;margin-top:30px}}
#tip{{position:absolute;inset:0;background:var(--ink);opacity:0;overflow:hidden}}
#tip img{{position:absolute;left:0;top:0;width:1080px;height:1920px;object-fit:cover;filter:brightness(.38) saturate(.8)}}
#tip .cr{{left:72px;bottom:auto;top:1560px}}
#tiptext{{position:absolute;left:72px;top:620px;width:850px;color:var(--iv)}}
#tiptext .k{{font:800 24px/1 Manrope;letter-spacing:.2em;color:#F0B27A}}
#tiptext h2{{font:700 92px/1.02 'Space Grotesk';letter-spacing:-.02em;margin-top:26px}}
#tiptext h2 em{{font-style:normal;color:#7FD1C7}}
#tiptext p{{font:500 36px/1.4 Manrope;margin-top:30px;color:rgba(243,238,229,.88)}}
#end{{position:absolute;inset:0;background:var(--iv);opacity:0;overflow:hidden}}
#end .lw-echo{{--lw-echo:#13202B;--lw-echo-op:.035;--lw-echo-size:1150px}}
#endtext{{position:absolute;left:72px;top:520px;width:860px}}
#endtext .k{{font:800 24px/1 Manrope;letter-spacing:.2em;color:var(--teal)}}
#endtext h2{{font:700 96px/1.02 'Space Grotesk';letter-spacing:-.02em;margin-top:28px}}
#endtext h2 span{{color:var(--teal)}}
#endtext p{{font:500 34px/1.45 Manrope;margin-top:34px;color:#3B4A55}}
#endrule{{width:860px;height:2px;background:var(--ink);opacity:.2;margin:56px 0 48px;transform-origin:0 50%}}
#endsig{{display:flex;align-items:center;justify-content:space-between;width:860px}}
#endsig .url{{font:700 40px/1 'Space Grotesk';letter-spacing:.01em}}
#endsrc{{font:500 20px/1.4 Manrope;color:#5A6873;margin-top:40px}}
#fade{{position:absolute;inset:0;background:var(--iv);opacity:0}}
{MARK_CSS}
</style></head><body>
{sc}
<div id="hook"><div class="k">INCOTERMS® 2020 · 20-SECOND GUIDE</div><h1>FOB, <span>CIF</span><br>or <em>DDP</em>?</h1><p>Who pays for what, and when the risk becomes yours.</p></div>
<div id="tip"><img src="file://{tip}"><div class="cr">Photo: {TIP_PHOTO[2]} · Wikimedia Commons</div>
 <div id="tiptext"><div class="k" id="tk">PRO TIP</div><h2 id="th">Shipping in containers? Look at <em>FCA</em> and <em>CIP</em>.</h2>
 <p id="tp">FOB and CIF are sea rules for goods loaded on board. For containers handed to the carrier at a terminal, ICC guidance points to FCA and CIP instead.</p></div></div>
<div id="end">{echo("right","-260px","-330px")}
 <div id="endtext"><div class="k" id="ek">Before you sign</div>
 <h2 id="eh">Agree the term. <span>Then the price.</span></h2>
 <p id="ep">LinkWin Trading quotes FOB, CIF, DDP and more for ferroalloys, metals and industrial goods from China.</p>
 <div id="endrule"></div><div id="endsig">{signature()}<div class="url">linkwinco.com</div></div>
 <div id="endsrc">Source: ICC, Incoterms® 2020 rules</div></div></div>
<div id="fade"></div>
<script>
const S={STARTS}, W={WIN}, TIP={TIP_T}, END={END_T}, X={X}, COST={[s[5] for s in SCENES]};
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x)), ease=x=>{{x=cl(x);return x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2}}, eo=x=>1-Math.pow(1-cl(x),3);
const $=id=>document.getElementById(id);
function render(t){{
  for(let i=0;i<S.length;i++){{
    const t0=S[i], t1=(i+1<S.length?S[i+1]:TIP), on=(t>=t0-1e-4&&t<t1+0.4), lt=t-t0-W[i];
    let op=0; if(on){{op=i==0?1:eo((t-t0)/0.4); if(t>t1) op=1-eo((t-t1)/0.4)}}
    $('sc'+i).style.opacity=op; $('sc'+i).style.zIndex=10+i;
    $('im'+i).style.transform=`scale(${{1.0+0.07*cl((t-t0)/5.5)}}) translateX(${{(i%2?12:-12)*cl((t-t0)/5.5)}}px)`;
    const h=$('hd'+i), hin=i==0?eo((t-2.2)/0.45):eo((t-t0)/0.45);
    h.style.opacity=hin; h.style.transform=`translateY(${{(1-hin)*30}}px)`;
    const full=X[4]-X[0], cost=X[COST[i]]-X[0];
    const pa=ease((lt-0.35)/0.9); $('yo'+i).style.width=(full*ease((lt-0.2)/0.6))+'px';
    $('se'+i).style.width=(cost*pa)+'px';
    const pp=eo((lt-1.3)/0.45), pi=$('pi'+i); pi.style.opacity=pp; pi.style.transform=`translateY(${{(1-pp)*-40}}px)`;
    if(i==0) $('ru0').style.opacity=t<2.2?0:eo((t-2.2)/0.3);
    const l=(id,d)=>{{const v=eo((lt-d)/0.45); $(id).style.opacity=v; $(id).style.transform=`translateX(${{(1-v)*-30}}px)`}};
    l('la'+i,1.6); l('lb'+i,2.4);
    if(i==0&&t<2.2){{ $('hd0').style.opacity=0; $('yo0').style.width='0px'; $('se0').style.width='0px'; pi.style.opacity=0; $('ru0').style.opacity=0; $('la0').style.opacity=0; $('lb0').style.opacity=0 }}
  }}
  const hk=$('hook'); hk.style.zIndex=40; const ho=t<1.95?1:1-eo((t-1.95)/0.3); hk.style.opacity=ho; hk.style.transform=`translateY(${{-(1-ho)*30}}px)`;
  const tp=$('tip'); tp.style.zIndex=45; tp.style.opacity=t<TIP?0:(t<END?eo((t-TIP)/0.4):1);
  tp.querySelector('img').style.transform=`scale(${{1.03+0.05*cl((t-TIP)/2.6)}})`;
  const st=(id,base,d)=>{{const v=eo((t-base-d)/0.45); $(id).style.opacity=v; $(id).style.transform=`translateY(${{(1-v)*28}}px)`}};
  st('tk',TIP,0.2); st('th',TIP,0.35); st('tp',TIP,0.8);
  const en=$('end'); en.style.zIndex=50; en.style.opacity=t<END?0:eo((t-END)/0.45);
  st('ek',END,0.25); st('eh',END,0.4); st('ep',END,0.85); st('endsig',END,1.25); st('endsrc',END,1.5);
  $('endrule').style.transform=`scaleX(${{eo((t-END-1.1)/0.6)}})`;
  const f=$('fade'); f.style.zIndex=60; f.style.opacity=t>23.55?eo((t-23.55)/0.45):0;
}}
</script></body></html>'''

def main():
    from playwright.sync_api import sync_playwright
    preview = None
    if "--preview" in sys.argv: preview = [float(x) for x in sys.argv[sys.argv.index("--preview") + 1].split(",")]
    shots = [crop(s[2], s[3], f"s{i}.jpg") for i, s in enumerate(SCENES)]
    tip = crop(TIP_PHOTO[0], TIP_PHOTO[1], "tip.jpg")
    tpl = os.path.join(ROOT, "templates", SLUG + ".html")
    open(tpl, "w", encoding="utf-8").write(html(shots, tip, None))
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
        print("boxes:", pg.evaluate("""(()=>{const o={};document.querySelectorAll('.hd .t,.hd .f,.lines p,.st span,.pin span,#hook h1,#hook p,#tiptext h2,#tiptext p,#endtext h2,#endtext p,#endsig,.cr').forEach((e,i)=>{const r=e.getBoundingClientRect();o[i+':'+(e.id||e.className)]=[Math.round(r.left),Math.round(r.top),Math.round(r.right),Math.round(r.bottom)]});return o})()"""))
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
            if f == 0: pg.screenshot(path=os.path.join(WORK, "cover.png"))
            if f % 90 == 0: print(f"frame {f}/{n}  {time.time()-t0:.0f}s", flush=True)
        ff.stdin.close(); ff.wait(); b.close()
    wav = os.path.join(WORK, "bed.wav")
    subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "2026-11-21-reel-audio.py"), wav], check=True)
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
