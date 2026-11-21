# Thai Narak Story 2026-11-21 LUNCH - "Saturday, on skewers." diagonal bracket layout
import sys;sys.path.insert(0,'/workspace/tn-run/rd')
from dlib import *
W,H=1080,1920; OUT=sys.argv[1] if len(sys.argv)>1 else 'story-2026-11-21-lunch.jpg'
BG=(19,18,21); CREAM=(240,230,212); GOLD=(222,177,80); MUTE=(196,184,164)
A='/cursor/stores/store-71c2a87a-216e-4174-bacc-f3ef6c2eaf39/thai-narak/assets/food/'
src=Image.open(A+'pattaya-pineapple-chicken-bbq-skewers_gallery_900x600.jpg').convert('RGB')
CROP=(96,112,706,600)           # tight on skewers + pineapple; excludes watermark (top-left) and board
PT=500                          # photo top on canvas
c=src.crop(CROP); k=W/c.width
c=c.resize((W,int(c.height*k+.5)),Image.LANCZOS).filter(ImageFilter.UnsharpMask(1.4,55,2))
ph=np.asarray(c).astype(float); ph_h=ph.shape[0]
yy,xx=np.mgrid[0:ph_h,0:W]
# burn the bare stone at the far left/bottom so the eye lands on the skewers
cx,cy=W*0.48,ph_h*0.50
dd=np.sqrt(((xx-cx)/(W*0.62))**2+((yy-cy)/(ph_h*0.55))**2)
ph*=(1-0.45*np.clip((dd-0.7)/0.8,0,1))[...,None]
ph=np.asarray(grade(Image.fromarray(np.clip(ph,0,255).astype(np.uint8)),exposure=0.83,contrast=0.42,sat=0.88,warm=1.6,vignette=0.0,lift=8,grain=0)).astype(float)
def ss(t): t=np.clip(t,0,1); return t*t*(3-2*t)
Y,X=np.mgrid[0:H,0:W]
canvas=np.full((H,W,3),BG,float)
glow=np.exp(-(((X-W*0.5)/(W*0.7))**2+((Y-(PT+ph_h*0.5))/560)**2)); canvas+=glow[...,None]*np.array([20,12,3])
full=np.zeros((H,W,3)); full[PT:PT+ph_h]=ph
m=ss((Y-PT)/(0.30*ph_h))*ss((PT+ph_h-Y)/(0.38*ph_h))
m*=(ss(X/(W*0.10))**0.6)*(ss((W-X)/(W*0.10))**0.6)
out=canvas*(1-m[...,None])+full*m[...,None]
vd=np.sqrt(((X-W/2)/(W*0.75))**2+((Y-H*0.5)/(H*0.6))**2)
out=out*(1-0.35*np.clip(vd-0.4,0,1))[...,None]+noise(W,H,5.5,21)[...,None]
img=Image.fromarray(np.clip(out,0,255).astype(np.uint8)).convert('RGBA')
d=ImageDraw.Draw(img); boxes={}
M=96
def T(key,xy,s_,f,fill,anchor='ls'):
    d.text(xy,s_,font=f,fill=fill,anchor=anchor); boxes[key]=d.textbbox(xy,s_,font=f,anchor=anchor)
def TR(key,x,y,s_,f,fill,sp,align='l'):
    w=sum(d.textlength(ch,font=f) for ch in s_)+sp*(len(s_)-1)
    x0=x if align=='l' else x-w
    track(d,(x0,y),s_,f,fill,sp); bb=d.textbbox((x0,y),s_,font=f); boxes[key]=(x0,bb[1],x0+w,bb[3])
# 1 brand signature: gold-foil traced wordmark, top-left on the editorial margin
wm=logo_mask('word',52); fo=foil(wm); sx,sy=M,270
sh,pad=soft_shadow(wm,3,120,(0,2)); img.alpha_composite(sh,(sx-pad,sy-pad)); img.alpha_composite(fo,(sx,sy))
boxes['sig']=(sx,sy,sx+wm.width,sy+wm.height)
# 2 headline bracketing the photo on the diagonal of the skewers
T('h1',(M-4,560),'Saturday,',corm(118,300),CREAM)
T('h2',(W-M+4,1404),'on skewers.',corm(118,400,italic=True),GOLD,anchor='rs')
TR('dish',W-M,1440,'PATTAYA PINEAPPLE CHICKEN BBQ',mont(20,500),CREAM,4,'r')
T('dishcn',(W-M,1500),'芭提雅菠萝鸡肉串',scserif(30),MUTE,anchor='rs')
# 3 info footer: gold hairline + one bilingual line each side (latin=Montserrat, CJK=Noto Sans CJK)
FY=1562
d.line((M,1526,W-M,1526),fill=GOLD,width=1); boxes['rule']=(M,1526,W-M,1527)
LAT=mont(19,500); CJK=scsans(21)
def runs_w(runs): return sum((sum(d.textlength(ch,font=f) for ch in t)+sp*(len(t)-1)) if sp else d.textlength(t,font=f) for t,f,sp in runs)
def RUNS(key,x,runs,fill,align='l'):
    w=runs_w(runs); x0=x if align=='l' else x-w; xx=x0; top=9e9; bot=0
    for t,f,sp in runs:
        if sp:
            cx_=xx
            for ch in t: d.text((cx_,FY),ch,font=f,fill=fill,anchor='ls'); cx_+=d.textlength(ch,font=f)+sp
            bb=d.textbbox((xx,FY),t,font=f,anchor='ls')
        else: d.text((xx,FY),t,font=f,fill=fill,anchor='ls'); bb=d.textbbox((xx,FY),t,font=f,anchor='ls')
        top=min(top,bb[1]); bot=max(bot,bb[3])
        xx+=(sum(d.textlength(ch,font=f) for ch in t)+sp*(len(t)-1)) if sp else d.textlength(t,font=f)
    boxes[key]=(x0,top,x0+w,bot)
RUNS('lunch',M,[('LUNCH 11:00–15:00',LAT,3),('   午市',CJK,0)],CREAM)
RUNS('metro',W-M,[('METRO 1 · XIMENKOU',LAT,3),('   西门口站',CJK,0)],CREAM,'r')
for kk,b in boxes.items():
    assert b[1]>=250 and b[3]<=1570,(kk,b)
print(boxes)
img.convert('RGB').save(OUT,quality=94,subsampling=0)
