# Thai Narak Story 2026-11-23 LUNCH - "Roasted / to gold." Daylight Editorial
# Layout: asymmetric magazine page on warm linen. Big left-aligned headline (96px margin) top-left,
# real roast-chicken photo hung off the RIGHT edge (bleeds right only), info set flush-right under it,
# gold foil wordmark top-right, generous empty linen below. No dark tones, no colour fields.
import sys;sys.path.insert(0,'/workspace/tn-run/rd')
from dlib import *
W,H=1080,1920; OUT=sys.argv[1] if len(sys.argv)>1 else 'story-2026-11-23-lunch.jpg'
LINEN=np.array([244,237,225.]); INK=(58,42,30); INK2=(110,88,66); GOLDT=(170,122,40); GOLD=(222,177,80)
P='/cursor/stores/store-71c2a87a-216e-4174-bacc-f3ef6c2eaf39/thai-narak/assets/food/thai-roasted-chicken_hero-darkened_1890x1260.jpg'
src=Image.open(P).convert('RGB')
PX,PY,PW,PH=96,790,W-96,650                 # photo: bleeds off right edge
c=cover(src,PW,PH,cx=0.40,cy=0.52,zoom=1.12)
# undo baked-in dark overlay: lift exposure, gentle curve, warm daylight
a=np.asarray(c).astype(float)/255
a=1-(1-np.clip(a*1.7,0,1))**1.25            # brighten, soft shoulder
c=Image.fromarray((a*255).astype(np.uint8))
c=grade(c,exposure=1.02,lift=14,contrast=0.12,sat=1.05,warm=1.2,vignette=0.0,grain=2,gamma=0.9)
c=c.filter(ImageFilter.UnsharpMask(1.4,60,2))
Y,X=np.mgrid[0:H,0:W]
field=LINEN[None,None,:]*np.ones((H,W,1))
# soft daylight: brighter window light from top-left, faint warm falloff to bottom-right
field=field+(np.exp(-(((X-150)/700.)**2+((Y-300)/700.)**2))*8)[...,None]
field=field-(((X+Y)/(W+H))**2*8)[...,None]*np.array([0.6,0.9,1.2])
out=field+noise(W,H,2.0,41,blur=0.6)[...,None]
# very soft contact shadow to the photo's left/bottom (print laid on linen)
m=np.zeros((H,W)); m[PY+10:PY+PH+14,PX-6:W]=1
from scipy.ndimage import gaussian_filter
sh=gaussian_filter(m,22)*0.07; out=out*(1-sh[...,None])
out[PY:PY+PH,PX:W]=np.asarray(c).astype(float)
img=Image.fromarray(np.clip(out,0,255).astype(np.uint8)).convert('RGBA')
d=ImageDraw.Draw(img); boxes={}
def L(key,x,y,s_,f,fill,sp=0,anchor='l'):
    w=sum(d.textlength(ch,font=f) for ch in s_)+sp*(len(s_)-1)
    x0=x-w if anchor=='r' else x
    track(d,(x0,y),s_,f,fill,sp); bb=d.textbbox((x0,y),s_,font=f); boxes[key]=(x0,bb[1],x0+w,bb[3])
M=96
# kicker: hairline gold rule + 今日推荐
d.line([(M,316),(M+64,316)],fill=GOLD,width=2)
L('kick',M+84,292,'今日推荐',scserif(30,bold=True),INK2,6)
# headline, big, left-aligned, italic stepped in
f1=corm(168,300); f2=corm(168,400,italic=True)
d.text((M-6,520),'Roasted',font=f1,fill=INK,anchor='ls'); boxes['h1']=d.textbbox((M-6,520),'Roasted',font=f1,anchor='ls')
d.text((M+150,680),'to gold.',font=f2,fill=GOLDT,anchor='ls'); boxes['h2']=d.textbbox((M+150,680),'to gold.',font=f2,anchor='ls')
# dish name as magazine caption under photo, left; info flush-right
L('cn',M,1474,'泰式烧鸡（升级版）',scserif(40),INK,2)
# gold foil signature top-right
wm=logo_mask('word',54); fo=foil(wm); sx,sy=W-M-wm.width,276
s0,pad0=soft_shadow(wm,4,70,(0,2)); img.alpha_composite(s0,(sx-pad0,sy-pad0)); img.alpha_composite(fo,(sx,sy))
boxes['sig']=(sx,sy,sx+wm.width,sy+wm.height)
d=ImageDraw.Draw(img)
# info flush-right under photo
R=W-M
L('hours',R,1478,'LUNCH 11:00–15:00',mont(22,500),INK,5,'r')
hb=boxes['hours']
L('hcn',hb[0]-16,1476,'午市',scsans(22),INK2,2,'r')
d.line([(R-150,1524),(R,1524)],fill=GOLD,width=1)
L('metro',R,1540,'地铁1号线 西门口站',scsans(22),INK2,2,'r')
for kk,b in boxes.items(): assert b[1]>=250 and b[3]<=1570,(kk,b)
print({k:tuple(int(v) for v in b) for k,b in boxes.items()})
img.convert('RGB').save(OUT,quality=94,subsampling=0)
