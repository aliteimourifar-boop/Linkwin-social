# Thai Narak Story 2026-11-22 LUNCH - "Sunday comfort." Spice Market Colour
# Layout: bottom-heavy, asymmetric left-aligned. Real dish full-bleed top 60%, turmeric
# colour field rising in a tilted wave (high left, low right) with chili + lemongrass ribbons.
import sys;sys.path.insert(0,'/workspace/tn-run/rd')
from dlib import *
W,H=1080,1920; OUT=sys.argv[1] if len(sys.argv)>1 else 'story-2026-11-22-lunch.jpg'
TURM=np.array([227,162,26.]); CHILI=(200,52,31); LEMON=(184,194,90)
INK=(58,30,14); INK2=(92,48,20)
A='/cursor/stores/store-71c2a87a-216e-4174-bacc-f3ef6c2eaf39/thai-narak/assets/food/'
src=Image.open(A+'yellow-curry-beef-pot_gallery_900x600.jpg').convert('RGB')
CROP=(200,0,840,600)            # excludes the watermark (x<190,y<90) and the side dish top-left
PH=1240                         # photo height on canvas
c=src.crop(CROP); k=PH/c.height
c=c.resize((int(c.width*k+.5),PH),Image.LANCZOS)
x0=(c.width-W)//2-40; c=c.crop((x0,0,x0+W,PH)).filter(ImageFilter.UnsharpMask(1.6,60,2))
c=grade(c,exposure=1.06,contrast=0.24,sat=1.05,warm=1.3,vignette=0.0,lift=4,grain=0,gamma=0.95)
ph=np.asarray(c).astype(float)
def ss(t): t=np.clip(t,0,1); return t*t*(3-2*t)
Y,X=np.mgrid[0:H,0:W]
# turmeric field with a soft daylight gradient
field=TURM[None,None,:]*np.ones((H,W,1))
field=field+(np.exp(-(((X-260)/700.)**2+((Y-1300)/420.)**2))*24)[...,None]*np.array([1,0.8,0.2])
field=field-(np.clip((Y-1500)/420.,0,1)*18)[...,None]*np.array([0.6,1,1])
full=np.zeros((H,W,3)); full[:PH]=ph
# wave edge: high on the left, sweeping down to the right
def edge(x,off=0): return 1040+0.17*x+38*np.sin(x/W*np.pi*1.6+0.4)+off
E=edge(X)
out=full.copy()
def band(e_top,e_bot,col):
    global out
    a=np.clip(Y-e_top+1,0,1)*np.clip(e_bot-Y+1,0,1)
    out=out*(1-a[...,None])+np.array(col,float)*a[...,None]
band(edge(X,-58),edge(X,-40),LEMON)      # thin lemongrass ribbon
band(edge(X,-40),edge(X,0),CHILI)        # chili ribbon
a=np.clip(Y-E+1,0,1)[...,None]; out=out*(1-a)+field*a
# soft contact shadow of the ribbons onto the photo
sh=np.exp(-np.clip(edge(X,-58)-Y,0,None)/18.)*(Y<edge(X,-58)); out=out*(1-0.22*sh[...,None])
out=out+noise(W,H,3.0,22)[...,None]
img=Image.fromarray(np.clip(out,0,255).astype(np.uint8)).convert('RGBA')
fl=logo_mask('dancer',560)
img=deboss(img,fl,(W-fl.width+90,H-fl.height+250),depth=1.6,opacity=1.0)
d=ImageDraw.Draw(img); boxes={}; M=96
def T(key,xy,s_,f,fill,anchor='ls'):
    d.text(xy,s_,font=f,fill=fill,anchor=anchor); boxes[key]=d.textbbox(xy,s_,font=f,anchor=anchor)
def TR(key,x,y,s_,f,fill,sp):
    w=sum(d.textlength(ch,font=f) for ch in s_)+sp*(len(s_)-1)
    track(d,(x,y),s_,f,fill,sp); bb=d.textbbox((x,y),s_,font=f); boxes[key]=(x,bb[1],x+w,bb[3])
# 1 headline, left editorial margin, ink serif + chili italic
T('h1',(M-6,1262),'Sunday',corm(150,500),INK)
T('h2',(M+64,1382),'comfort.',corm(156,500,italic=True),CHILI)
T('cn',(M+4,1460),'周日暖心 · 黄咖喱牛腩',scserif(40,bold=True),INK)
# 2 dish name (verified menu name)
LAT=mont(22,600); CJK=scsans(24)
TR('dish',M+4,1484,'YELLOW CURRY BEEF POT',LAT,INK2,5)
# 3 info lines
def RUN(key,x,y,runs,fill):
    x0=x; top=9e9; bot=0
    for t,f,sp in runs:
        if sp:
            for ch in t: d.text((x,y),ch,font=f,fill=fill,anchor='ls'); x+=d.textlength(ch,font=f)+sp
            bb=d.textbbox((x0,y),t,font=f,anchor='ls')
        else:
            d.text((x,y),t,font=f,fill=fill,anchor='ls'); bb=d.textbbox((x,y),t,font=f,anchor='ls'); x+=d.textlength(t,font=f)
        top=min(top,bb[1]); bot=max(bot,bb[3])
    boxes[key]=(x0,top,x,bot)
RUN('hours',M+4,1538,[('LUNCH 11:00–15:00',LAT,4),('   午市 11:00–15:00',CJK,0)],INK)
RUN('metro',M+4,1566,[('METRO LINE 1 · XIMENKOU',mont(20,500),4),('   地铁1号线 西门口站',scsans(22),0)],INK2)
# signature: gold-foil traced wordmark, right side on the turmeric field, debossed shadow
wm=logo_mask('word',64); fo=foil(wm); sx,sy=W-M-wm.width,1500
s0,pad0=soft_shadow(wm,6,120,(0,4)); img.alpha_composite(s0,(sx-pad0,sy-pad0))
s1,pad=soft_shadow(wm,1,200,(0,2)); img.alpha_composite(s1,(sx-pad,sy-pad)); img.alpha_composite(fo,(sx,sy))
boxes['sig']=(sx,sy,sx+wm.width,sy+wm.height)
for kk,b in boxes.items(): assert b[1]>=250 and b[3]<=1570,(kk,b)
print(boxes)
img.convert('RGB').save(OUT,quality=94,subsampling=0)
