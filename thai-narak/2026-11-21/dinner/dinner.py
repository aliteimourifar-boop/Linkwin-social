# Thai Narak Story 2026-11-21 DINNER - "Bring the whole crew." top-heavy centred, Rattan & Wood Warmth
import sys;sys.path.insert(0,'/workspace/tn-run/rd')
from dlib import *
W,H=1080,1920; OUT=sys.argv[1] if len(sys.argv)>1 else 'story-2026-11-21-dinner.jpg'
CREAM=(246,236,218); GOLD=(222,177,80); SOFT=(238,220,190)
SRC='/cursor/stores/store-71c2a87a-216e-4174-bacc-f3ef6c2eaf39/thai-narak/assets/owner-photos/interior-dining-room-wide-03.jpg'
src=np.asarray(Image.open(SRC).convert('RGB')).astype(float)
# retouch: neutralise + burn the green exit sign (x3780-4010, y1290-1420)
yy,xx=np.mgrid[0:src.shape[0],0:src.shape[1]]
e=np.exp(-(((xx-3895)/170.)**2+((yy-1355)/110.)**2))[...,None]
lum=src.mean(2,keepdims=True); warm=np.concatenate([lum*0.55,lum*0.42,lum*0.30],2)
src=src*(1-e)+warm*e
del yy,xx,e
PT=560; PH=H-PT                     # photo area height
CX0=int(sys.argv[2]) if len(sys.argv)>2 else 1900
cw=int(4000*W/PH); crop=src[:, CX0:CX0+cw]
c=Image.fromarray(np.clip(crop,0,255).astype(np.uint8)).resize((W,PH),Image.LANCZOS)
# bright warm grade (Rattan & Wood): exposure ~1.05, gentle contrast, warm highlights, no heavy vignette
c=grade(c,exposure=1.06,contrast=0.22,sat=0.95,warm=1.5,vignette=0.0,lift=6,grain=0,gamma=0.95)
ph=np.asarray(c).astype(float)
yl=np.arange(PH)[:,None,None]; ph=ph*(1+0.30*np.clip(1-yl/(0.45*PH),0,1))
def ss(t): t=np.clip(t,0,1); return t*t*(3-2*t)
Y,X=np.mgrid[0:H,0:W]
# honey/rattan field sampled from the thatch at the top of the photo
th=ph[40:260].reshape(-1,3).mean(0); print('thatch',th)
top=np.array([150,98,54.]); mid=np.array([128,82,46.])
t=ss(np.clip((Y-300)/700.,0,1))[...,None]
field=top*(1-t)+mid*t
glow=np.exp(-(((X-W*0.5)/(W*0.55))**2+((Y-470)/260.)**2))[...,None]
field=field+glow*np.array([30,20,4.])
full=np.zeros((H,W,3)); full[PT:]=ph
m=ss((Y-PT)/(0.34*PH))[...,None]
out=field*(1-m)+full*m
out=out+noise(W,H,4.0,21)[...,None]
img=Image.fromarray(np.clip(out,0,255).astype(np.uint8)).convert('RGBA')
d=ImageDraw.Draw(img); boxes={}
def T(key,xy,s_,f,fill,anchor='ms'):
    d.text(xy,s_,font=f,fill=fill,anchor=anchor); boxes[key]=d.textbbox(xy,s_,font=f,anchor=anchor)
def TRC(key,cx,y,s_,f,fill,sp):
    w=sum(d.textlength(ch,font=f) for ch in s_)+sp*(len(s_)-1); x0=cx-w/2
    track(d,(x0,y),s_,f,fill,sp); bb=d.textbbox((x0,y),s_,font=f); boxes[key]=(x0,bb[1],x0+w,bb[3])
# 1 signature: gold foil traced wordmark, centred
wm=logo_mask('word',56); fo=foil(wm); sx,sy=(W-wm.width)//2,272
sh,pad=soft_shadow(wm,3,110,(0,2)); img.alpha_composite(sh,(sx-pad,sy-pad)); img.alpha_composite(fo,(sx,sy))
boxes['sig']=(sx,sy,sx+wm.width,sy+wm.height)
# 2 headline (centred, roman + gold italic) + Chinese
sh_layer=Image.new('RGBA',img.size,(0,0,0,0)); sd=ImageDraw.Draw(sh_layer)
for s_,y,f in [('Bring the',470,corm(104,300)),('whole crew.',572,corm(110,400,italic=True))]:
    sd.text((W//2,y+3),s_,font=f,fill=(60,32,12,150),anchor='ms')
sh_layer=sh_layer.filter(ImageFilter.GaussianBlur(6)); img.alpha_composite(sh_layer)
T('h1',(W//2,470),'Bring the',corm(104,300),CREAM)
T('h2',(W//2,572),'whole crew.',corm(110,400,italic=True),GOLD)
T('cn',(W//2,648),'周末聚餐，约上一桌好友',scserif(40),CREAM)
# 3 info: hairline + bilingual hours + metro
d.line((W//2-60,690,W//2+60,690),fill=GOLD,width=1); boxes['rule']=(W//2-60,690,W//2+60,691)
LAT=mont(22,500); CJK=scsans(24)
def RUNSC(key,cx,y,runs,fill):
    wl=[(sum(d.textlength(ch,font=f) for ch in t)+sp*(len(t)-1)) if sp else d.textlength(t,font=f) for t,f,sp in runs]
    x=cx-sum(wl)/2; x0=x; top_=9e9; bot=0
    for (t,f,sp),w in zip(runs,wl):
        if sp:
            cx_=x
            for ch in t: d.text((cx_,y),ch,font=f,fill=fill,anchor='ls'); cx_+=d.textlength(ch,font=f)+sp
        else: d.text((x,y),t,font=f,fill=fill,anchor='ls')
        bb=d.textbbox((x,y),t,font=f,anchor='ls'); top_=min(top_,bb[1]); bot=max(bot,bb[3]); x+=w
    boxes[key]=(x0,top_,x0+sum(wl),bot)
RUNSC('hours',W//2,734,[('DINNER 17:00–22:00',LAT,4),('   晚市 17:00–22:00',CJK,0)],CREAM)
RUNSC('metro',W//2,772,[('地铁1号线 西门口站',CJK,0),('   METRO LINE 1 · XIMENKOU',LAT,4)],SOFT)
for kk,b in boxes.items(): assert b[1]>=250 and b[3]<=1570,(kk,b)
print(boxes)
img.convert('RGB').save(OUT,quality=94,subsampling=0)
