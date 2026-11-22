# Thai Narak Story 2026-11-22 DINNER - "Heat, meet / jasmine rice." Thai Pastel Modern
# Layout: centred "sandwich" - butterfly-pea twilight field, real brass-bowl photo as a full-bleed
# lens-shaped band through the middle (gently arced edges), headline above, tip + dinner info below.
import sys;sys.path.insert(0,'/workspace/tn-run/rd')
from dlib import *
W,H=1080,1920; OUT=sys.argv[1] if len(sys.argv)>1 else 'story-2026-11-22-dinner.jpg'
PEA=np.array([143,168,216.]); MANGO=(246,196,106); CREAM=(250,244,232); INKB=(34,44,78); INK2=(52,64,104); BRASS=(140,92,22)
P='/cursor/stores/store-71c2a87a-216e-4174-bacc-f3ef6c2eaf39/thai-narak/assets/owner-photos/food-jasmine-rice-brass-bowl.png'
src=Image.open(P).convert('RGB')            # 3000x2250
BT,BB=600,1330                              # band (photo) top/bottom at centre
bh=BB-BT+80
c=cover(src,W,bh,cx=0.5,cy=0.47,zoom=1.06).filter(ImageFilter.UnsharpMask(1.2,50,2))
c=grade(c,exposure=1.04,contrast=0.18,sat=1.06,warm=1.15,vignette=0.0,lift=2,grain=0,gamma=0.98)
ph=np.asarray(c).astype(float)
Y,X=np.mgrid[0:H,0:W]
# twilight butterfly-pea field: lighter top, deeper toward bottom, soft jasmine glow behind headline
t=Y/H
field=PEA[None,None,:]*(1.06-0.20*t)[...,None]
field=field+(np.exp(-(((X-540)/620.)**2+((Y-440)/240.)**2))*10)[...,None]*np.array([1,0.95,0.8])
full=field.copy()
ys=BT-40
full[ys:ys+bh]=ph
# lens-shaped band edges
xx=(X-W/2)/(W/2)
top=BT-34*(1-xx**2)+8; bot=BB+34*(1-xx**2)
a=np.clip(Y-top+0.5,0,1)*np.clip(bot-Y+0.5,0,1)
out=field*(1-a[...,None])+full*a[...,None]
# soft shadow under band, thin mango hairlines on both edges
sh=np.exp(-np.clip(Y-bot,0,None)/26.)*(Y>bot); out=out*(1-0.18*sh[...,None])
for e in (top,bot):
    h=np.clip(1.3-np.abs(Y-e),0,1)*0.85; out=out*(1-h[...,None])+np.array(MANGO,float)*h[...,None]
out=out+noise(W,H,2.2,31)[...,None]
img=Image.fromarray(np.clip(out,0,255).astype(np.uint8)).convert('RGBA')
# faint tone-on-tone dancer deboss bleeding off the bottom-left (texture only, below safe zone)
fl=logo_mask('dancer',620); img=deboss(img,fl,(-170,H-fl.height+300),depth=1.3,opacity=0.9)
d=ImageDraw.Draw(img); boxes={}
def C(key,y,s_,f,fill):
    d.text((W/2,y),s_,font=f,fill=fill,anchor='ms'); boxes[key]=d.textbbox((W/2,y),s_,font=f,anchor='ms')
def CT(key,y,s_,f,fill,sp):
    w=sum(d.textlength(ch,font=f) for ch in s_)+sp*(len(s_)-1); x=(W-w)/2
    track(d,(x,y),s_,f,fill,sp); bb=d.textbbox((x,y),s_,font=f); boxes[key]=(x,bb[1],x+w,bb[3])
# signature: gold-foil traced wordmark, top of safe zone
wm=logo_mask('word',58); fo=foil(wm); sx,sy=(W-wm.width)//2,272
s0,pad0=soft_shadow(wm,5,110,(0,3)); img.alpha_composite(s0,(sx-pad0,sy-pad0)); img.alpha_composite(fo,(sx,sy))
boxes['sig']=(sx,sy,sx+wm.width,sy+wm.height)
d=ImageDraw.Draw(img)
CT('kick',366,'TONIGHT’S TIP',mont(21,600),INK2,7)
C('h1',462,'Heat, meet',corm(100,400),INKB)
C('h2',544,'jasmine rice.',corm(100,500,italic=True),BRASS)
# below band: tip (CN + EN), dinner info
C('cn',1428,'一勺冬阴功，配一口香米饭',scserif(40,bold=True),INKB)
CT('tip',1450,'SPOON TOM YUM GOONG OVER THE RICE',mont(20,600),INK2,4)
CT('hours',1498,'DINNER 17:00–22:00',mont(20,600),INKB,4)
f2=scsans(22); s2='晚市 · 地铁1号线 西门口站'
d.text((W/2,1556),s2,font=f2,fill=INKB,anchor='ms'); boxes['metro']=d.textbbox((W/2,1556),s2,font=f2,anchor='ms')
for kk,b in boxes.items(): assert b[1]>=250 and b[3]<=1570,(kk,b)
print({k:tuple(int(v) for v in b) for k,b in boxes.items()})
img.convert('RGB').save(OUT,quality=94,subsampling=0)
