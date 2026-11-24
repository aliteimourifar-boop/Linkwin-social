# Thai Narak Story 2026-11-24 DINNER - "Find us / at Ximenkou." Rattan & Wood Warmth
# Layout: "wayfinding". Real shopfront photo (amber grade) fills the upper ~half and melts into a
# warm honey-wood field. One continuous thin gold hairline starts at the lit entrance in the photo,
# drops down, turns left under the left-aligned headline and runs down a vertical route with three
# stops (shop -> ~420 m walk -> Metro Line 1). Hours + small gold-foil wordmark sit bottom-right.
import sys;sys.path.insert(0,'/workspace/tn-run/rd')
from dlib import *
import cv2
W,H=1080,1920; OUT=sys.argv[1] if len(sys.argv)>1 else 'story-2026-11-24-dinner.jpg'
P='/cursor/stores/store-71c2a87a-216e-4174-bacc-f3ef6c2eaf39/thai-narak/assets/owner-photos/shopfront-outdoor-seating-01.jpg'
src=Image.open(P).convert('RGB')
PH=1000
X0,Y0,X1=1055,830,4490; Y1=Y0+int((X1-X0)*PH/W)
crop=src.crop((X0,Y0,X1,Y1)).resize((W,PH),Image.LANCZOS)
# amber evening grade: warm, slightly lowered, soft contrast, light vignette
ph=grade(crop,exposure=0.96,lift=12,contrast=0.22,sat=0.92,warm=1.6,vignette=0.18,grain=3.5,gamma=1.02)
a=np.asarray(ph).astype(float)
a=a*np.array([1.06,1.0,0.86])           # amber cast
lum=a.mean(2,keepdims=True); a=lum+(a-lum)*0.95
yy=np.arange(PH)[:,None,None]; a=a*(0.55+0.45*np.clip(yy/110,0,1))
# retouch: quiet the kiosk poster / side signage (feathered elliptical burn + desaturate)
yg,xg=np.mgrid[0:PH,0:W]; e=np.clip(1.5*(1-np.sqrt(((xg-255)/300.)**2+((yg-600)/240.)**2)),0,1); e=(e*e*(3-2*e))[...,None]
l2=a.mean(2,keepdims=True); a=a*(1-e)+(l2+(a-l2)*0.35)*0.62*e
# ---- honey wood field ----
Y,X=np.mgrid[0:H,0:W].astype(float)
t=np.clip((Y-700)/1220,0,1)
c0=np.array([150,98,52.]); c1=np.array([104,64,34.])
base=c0*(1-t[...,None])+c1*t[...,None]
rng=np.random.default_rng(4)
n=rng.normal(0,1,(H,W)); n=cv2.GaussianBlur(n,(0,0),sigmaX=60,sigmaY=1.2); n/=n.std()
warp=cv2.GaussianBlur(rng.normal(0,1,(H,W)),(0,0),80); warp/=warp.std()
rings=np.sin((Y+warp*22)/9.0+n*0.8)
grain=(n*0.5+rings*0.2)
PL=236; pid=((Y-40)//PL).astype(int); tone=np.random.default_rng(7).normal(0,0.025,64)[pid%64]
seam=np.exp(-(((Y-40)%PL)/1.6)**2)*0.10
wood=base*(1+grain[...,None]*0.028+tone[...,None]-seam[...,None])+rng.normal(0,2.2,(H,W,1))
# warm amber glow from the photo spilling down on the left
g=np.exp(-(((X-300)/700)**2+((Y-1000)/420)**2)); wood+=g[...,None]*np.array([22,12,2])
# feather photo into wood
out=wood.copy()
ph_full=np.zeros((H,W,3)); ph_full[:PH]=a
m=np.clip((PH-Y)/260,0,1); m=m*m*(3-2*m)
out=ph_full*m[...,None]+out*(1-m[...,None])
img=Image.fromarray(np.clip(out,0,255).astype(np.uint8)).convert('RGBA')
CREAM=(247,238,222); CREAM2=(238,224,200); GOLD=(226,184,96); boxes={}
d=ImageDraw.Draw(img)
def shadowtext(xy,s_,f,fill,anchor='ls',blur=8,alpha=70):
    mk=Image.new('L',(W,H),0); ImageDraw.Draw(mk).text(xy,s_,font=f,fill=255,anchor=anchor)
    sh=mk.filter(ImageFilter.GaussianBlur(blur)).point(lambda p:int(p*alpha/255))
    l=Image.new('RGBA',(W,H),(60,34,16,255)); l.putalpha(sh); img.alpha_composite(l)
    dd=ImageDraw.Draw(img); dd.text(xy,s_,font=f,fill=fill,anchor=anchor); return dd.textbbox(xy,s_,font=f,anchor=anchor)
LX=96
boxes['h1']=shadowtext((LX,1088),'Find us',corm(112,300),CREAM)
boxes['h2']=shadowtext((LX+4,1196),'at Ximenkou.',corm(118,400,italic=True),GOLD)
# ---- gold hairline route (supersampled) ----
SS=3; ln=Image.new('L',(W*SS,H*SS),0); ld=ImageDraw.Draw(ln)
DX,DY=int(sys.argv[2]) if len(sys.argv)>2 else 772, int(sys.argv[3]) if len(sys.argv)>3 else 640
RX=112; TURN=1232; R_=26; STOPS=[1290,1398,1506]
lw=2*SS
def L_(p,q): ld.line([(p[0]*SS,p[1]*SS),(q[0]*SS,q[1]*SS)],fill=255,width=lw)
L_((DX,DY+14),(DX,TURN-R_)); 
ld.arc([( DX-2*R_)*SS,(TURN-2*R_)*SS,DX*SS,TURN*SS],0,90,fill=255,width=lw)
L_((DX-R_,TURN),(RX+R_,TURN))
ld.arc([RX*SS,TURN*SS,(RX+2*R_)*SS,(TURN+2*R_)*SS],180,270,fill=255,width=lw)
L_((RX,TURN+R_),(RX,STOPS[-1]))
def ring(cx,cy,r,fill=False):
    ld.ellipse([(cx-r)*SS,(cy-r)*SS,(cx+r)*SS,(cy+r)*SS],fill=0,outline=255,width=lw)
    if fill: ld.ellipse([(cx-r+4)*SS,(cy-r+4)*SS,(cx+r-4)*SS,(cy+r-4)*SS],fill=255)
ring(DX,DY,10,True)
for i,s in enumerate(STOPS): ring(RX,s,8,i==len(STOPS)-1)
ln=ln.resize((W,H),Image.LANCZOS)
glow=ln.filter(ImageFilter.GaussianBlur(6)).point(lambda p:int(p*0.5))
gl=Image.new('RGBA',(W,H),(255,200,110,255)); gl.putalpha(glow); img.alpha_composite(gl)
img.alpha_composite(tint_layer(ln,GOLD))
d=ImageDraw.Draw(img)
def T(key,x,y,s_,f,fill,sp=0,anchor='l'):
    w=track(d,(x,y),s_,f,fill,sp,anchor); x0=x-w if anchor=='r' else x
    bb=d.textbbox((x0,y),s_,font=f); boxes[key]=(x0,bb[1],x0+w,bb[3]); return x0
TX=146
# stop 1: the shop
T('s1cn',TX,STOPS[0]-24,'西门口广场一楼外围 137-1、139铺',scserif(32),CREAM)
T('s1ad',TX,STOPS[0]+20,'荔湾区中山七路48号',scserif(23),CREAM2,2)
# stop 2: the walk
T('s2en',TX,STOPS[1]-20,'~420 M',mont(22,500),GOLD,6)
T('s2cn',TX,STOPS[1]+12,'步行约420米',scserif(30),CREAM)
# stop 3: the metro
T('s3en',TX,STOPS[2]-20,'METRO LINE 1 · XIMENKOU',mont(22,500),GOLD,6)
T('s3cn',TX,STOPS[2]+12,'地铁1号线西门口站',scserif(30),CREAM)
# bottom-right: hours + signature
RR=W-96
wm=logo_mask('word',62); fo=foil(wm); sx,sy=RR-wm.width,1566-wm.height
s0,p0=soft_shadow(wm,5,120,(0,2)); img.alpha_composite(s0,(sx-p0,sy-p0)); img.alpha_composite(fo,(sx,sy))
boxes['sig']=(sx,sy,sx+wm.width,sy+wm.height)
d=ImageDraw.Draw(img)
x0=T('hcn',RR,sy-52,'晚市',scsans(22),CREAM,3,'r')
T('hours',x0-14,sy-50,'DINNER 17:00–22:00',mont(22,500),CREAM,5,'r')
for k,b in boxes.items(): assert b[1]>=250 and b[3]<=1570,(k,b)
print({k:tuple(int(v) for v in b) for k,b in boxes.items()})
img.convert('RGB').save(OUT,quality=94,subsampling=0)
