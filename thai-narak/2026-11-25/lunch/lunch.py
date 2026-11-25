# Thai Narak Story 2026-11-25 LUNCH - "Lemongrass: / bruise, don't chop." Daylight Editorial
# Layout: "botanical plate" still life. Real lemongrass + root props (top-left of food-garlic-bread.png,
# bread/paper excluded) enlarged, the dark stone re-toned to soft sand so the props sit on a bright
# sand page and dissolve seamlessly into it; centred bottom-heavy type stack (headline, CN tip,
# hairline, hours) with a small gold-foil traced wordmark as signature. No boxes, no borders, no AI.
import sys;sys.path.insert(0,'/workspace/tn-run/rd')
from dlib import *
from scipy.ndimage import gaussian_filter
import cv2
W,H=1080,1920; OUT=sys.argv[1] if len(sys.argv)>1 else 'story-2026-11-25-lunch.jpg'
P='/cursor/stores/store-71c2a87a-216e-4174-bacc-f3ef6c2eaf39/thai-narak/assets/owner-photos/food-garlic-bread.png'
src=np.asarray(Image.open(P).convert('RGB'))[:1150,:1150].astype(np.float32)
k=2.098                                # coords below measured on a 655px preview of the 1374px crop
# --- remove bread/paper: inpaint that zone with stone (low-res Telea), it then dissolves into the page
paper=np.zeros(src.shape[:2],np.uint8)
cv2.fillPoly(paper,[(np.array([(286,174),(320,157),(700,180),(700,600),(276,600)])*k).astype(np.int32)],1)
q=4; sm=cv2.resize(src.astype(np.uint8),None,fx=1/q,fy=1/q,interpolation=cv2.INTER_AREA)
pm=cv2.resize(paper,(sm.shape[1],sm.shape[0]),interpolation=cv2.INTER_NEAREST)
pm=cv2.dilate(pm,np.ones((5,5)))
inp=cv2.inpaint(sm,pm,9,cv2.INPAINT_TELEA)
inp=cv2.GaussianBlur(inp,(0,0),3)
inp=cv2.resize(inp,(src.shape[1],src.shape[0]),interpolation=cv2.INTER_CUBIC).astype(np.float32)
pf=gaussian_filter(cv2.dilate(paper,np.ones((15,15))).astype(np.float32),6)[...,None]
src=src*(1-pf)+inp*pf+np.random.default_rng(2).normal(0,4,src.shape[:2]+(1,))*pf
# --- daylight re-tone: screen with warm sand (lifts the dark stone to sand, keeps texture), re-saturate
p=src/255.; T=np.array([0.60,0.53,0.42])
p=1-(1-p)*(1-T)
lum=(p*[0.299,0.587,0.114]).sum(2,keepdims=True); p=lum+(p-lum)*1.3
p=np.clip(p*1.04,0,1)**1.16
ph=p*255
# white-balance so the re-toned stone lands on warm cream-sand (not peach); soft shoulder protects highlights
m0=np.median(ph[1000:1150,0:200].reshape(-1,3),0); g=np.array([232,221,203.])/m0
x=ph/255*g; ph=np.where(x<0.8,x,0.8+0.2*np.tanh((x-0.8)/0.2))*255
SAND=np.median(ph[1000:1150,0:200].reshape(-1,3),0)*1.0   # page = re-toned stone, so the dissolve is seamless
print('SAND',SAND)
reg=np.zeros(src.shape[:2],np.float32)
cv2.fillPoly(reg,[(np.array([(0,0),(655,0),(655,150),(330,190),(300,330),(225,410),(120,480),(0,495)])*k).astype(np.int32)],1)
w=gaussian_filter(reg,55)[...,None]
ph=ph*w+SAND*(1-w)
sc=1.12; ph=cv2.resize(ph.astype(np.float32),None,fx=sc,fy=sc,interpolation=cv2.INTER_LANCZOS4)
bl=cv2.GaussianBlur(ph,(0,0),1.6); ph=np.clip(ph+0.5*(ph-bl),0,255)
ws=cv2.resize(w[...,0],None,fx=sc,fy=sc)
page=np.ones((H,W,3),np.float32)*SAND
Y,X=np.mgrid[0:H,0:W]
ox,oy=40,0
hh,ww=min(ph.shape[0],H-oy),W
rs=ws[:hh,ox:ox+ww][...,None]
page[oy:oy+hh]=ph[:hh,ox:ox+ww]*rs+page[oy:oy+hh]*(1-rs)
page*= (1.0+0.04*np.clip((Y-700)/900,0,1))[...,None]   # page brightens gently toward the type (daylight)
page+=np.random.default_rng(4).normal(0,2.4,(H,W,1))
img=Image.fromarray(np.clip(page,0,255).astype(np.uint8)).convert('RGBA')
BROWN=(58,42,30); GOLD=(178,132,52)
d=ImageDraw.Draw(img); boxes={}; CX=W//2
f1=corm(112,300); f2=corm(100,400,italic=True)
d.text((CX,1218),'Lemongrass:',font=f1,fill=BROWN,anchor='ms'); boxes['h1']=d.textbbox((CX,1218),'Lemongrass:',font=f1,anchor='ms')
# gold-foil italic emphasis line (text mask -> foil, darkened slightly for legibility on sand)
tm=Image.new('L',(W,220),0); ImageDraw.Draw(tm).text((CX,150),"bruise, don’t chop.",font=f2,fill=255,anchor='ms')
bb=tm.getbbox(); tm=tm.crop(bb); fo=foil(tm,seed=5)
fa=np.asarray(fo).astype(float); fa[...,:3]*=0.80; fo=Image.fromarray(fa.astype(np.uint8),'RGBA')
s0,p0=soft_shadow(tm,3,60,(0,2)); ty=1340-150+bb[1]
img.alpha_composite(s0,(bb[0]-p0,ty-p0)); img.alpha_composite(fo,(bb[0],ty)); boxes['h2']=(bb[0],ty,bb[2],ty+tm.height)
d=ImageDraw.Draw(img)
def C(key,y,s_,f,fill,sp=0):
    w_=sum(d.textlength(ch,font=f) for ch in s_)+sp*(len(s_)-1); x0=CX-w_/2
    track(d,(x0,y),s_,f,fill,sp); b=d.textbbox((x0,y),s_,font=f); boxes[key]=(x0,b[1],x0+w_,b[3])
C('cn',1376,'香茅先拍裂，香气才出来',scserif(42),BROWN,6)
d.line([(CX-36,1458),(CX+36,1458)],fill=GOLD,width=2)
# hours line: Montserrat caps + CJK, measured as one centred row
fm=mont(22,500); fc=scsans(22); a='LUNCH 11:00–15:00'; b_='午市'
wa=sum(d.textlength(ch,font=fm) for ch in a)+5*(len(a)-1); wb=d.textlength(b_,font=fc)+2
x0=CX-(wa+16+wb)/2; track(d,(x0,1480),a,fm,BROWN,5); track(d,(x0+wa+16,1478),b_,fc,BROWN,2)
boxes['hours']=(x0,d.textbbox((x0,1480),a,font=fm)[1],x0+wa+16+wb,d.textbbox((x0+wa+16,1478),b_,font=fc)[3])
# gold-foil traced wordmark signature, small, centred under the stack
wm=logo_mask('word',50); fo=foil(wm); sx,sy=CX-wm.width//2,1518
s0,p0=soft_shadow(wm,4,70,(0,2)); img.alpha_composite(s0,(sx-p0,sy-p0)); img.alpha_composite(fo,(sx,sy))
boxes['sig']=(sx,sy,sx+wm.width,sy+wm.height)
for kk,b in boxes.items(): assert b[1]>=250 and b[3]<=1570,(kk,b)
print({kk:tuple(int(v) for v in b) for kk,b in boxes.items()})
img.convert('RGB').save(OUT,quality=94,subsampling=0)
img.convert('RGB').resize((216,384)).save('/tmp/thumb.png')
