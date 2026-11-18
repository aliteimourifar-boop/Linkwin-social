import sys;sys.path.insert(0,'/workspace/tn-run/rd')
from dlib import *
W,H=1080,1920; OUT=sys.argv[1]
BG=(19,18,21); CREAM=(240,230,212); GOLD=(222,177,80); MUTE=(200,188,168)
SRC='/cursor/stores/store-71c2a87a-216e-4174-bacc-f3ef6c2eaf39/thai-narak/assets/food/signature-grilled-pork-neck_portrait_453x536.jpg'
im=Image.open(SRC).convert('RGB')
# macro crop on the charred slices (uniform scale only)
CB=tuple(int(v) for v in (sys.argv[3].split(",") if len(sys.argv)>3 else (8,214,323,500))); c=im.crop(CB); k=W/c.width
PH=int(c.height*k+.5); PY=int(sys.argv[2]) if len(sys.argv)>2 else 580
ph=c.resize((W,PH),Image.LANCZOS)
pa=np.asarray(ph).astype(float); Y,X=np.mgrid[0:PH,0:W]
lum=pa.mean(2)
# tame bright bamboo tray + grey stone + pineapple: burn by hue/brightness away from meat
r,g,b=pa[...,0],pa[...,1],pa[...,2]
hs=np.asarray(c.convert('HSV')).astype(float); hue=hs[...,0]*360/255; sv=hs[...,1]/255; vv=hs[...,2]/255
tray=((hue>34)&(hue<75)&(vv>0.45)&(sv>0.15)).astype(float)          # bamboo tray + pineapple (wood-yellow hue)
tray=ndimage.binary_opening(tray>0,iterations=2)
lab_,n_=ndimage.label(tray); sz=ndimage.sum(tray,lab_,range(1,n_+1)); tray=np.isin(lab_,1+np.where(sz>400)[0]).astype(float)
stone=((sv<0.2)&(vv>0.55)).astype(float)                              # pale stone tabletop
def up(mk,bl): return np.asarray(Image.fromarray((ndimage.gaussian_filter(mk,bl)*255).astype(np.uint8)).resize((W,PH),Image.BILINEAR)).astype(float)/255
tm=up(tray,1.2); sm=up(stone,1.5)
tl=(pa*[0.299,0.587,0.114]).sum(2,keepdims=True)
pa=pa*(1-0.55*tm[...,None])
pa=pa*(1-0.55*sm[...,None])
# leaf: pull green toward deep olive
green=np.clip((g-r-8)/40,0,1)
gm=ndimage.gaussian_filter(green,3)[...,None]
olive=np.stack([pa[...,1]*0.55,pa[...,1]*0.62,pa[...,1]*0.30],2)
pa=pa*(1-0.6*gm)+olive*0.6*gm
# focal burn: keep the slices, darken corners (macro falloff)
fcx,fcy=W*0.44,PH*0.50
dd=np.sqrt(((X-fcx)/(W*0.58))**2+((Y-fcy)/(PH*0.52))**2)
pa=pa*(1-0.6*np.clip(dd-0.55,0,1)**1.2)[...,None]
ph=Image.fromarray(np.clip(pa,0,255).astype(np.uint8))
# shallow depth of field: sharp along slice diagonal, softer toward top/bottom
sharp=ph.filter(ImageFilter.UnsharpMask(2.2,80,2))
soft=ph.filter(ImageFilter.GaussianBlur(7))
foc=np.exp(-((Y-PH*0.52)/(PH*0.34))**4)
fa=np.asarray(sharp).astype(float)*foc[...,None]+np.asarray(soft).astype(float)*(1-foc[...,None])
ph=Image.fromarray(np.clip(fa,0,255).astype(np.uint8))
ph=grade(ph,exposure=0.82,contrast=0.42,sat=0.92,warm=1.7,vignette=0.0,lift=6,grain=0)
# ember: warm the char highlights
pa=np.asarray(ph).astype(float); l2=pa.mean(2)
emb=np.clip((l2-90)/120,0,1)*foc
pa=pa+emb[...,None]*np.array([16,5,-10])
meat=up(((hue<32)|(hue>340)).astype(float)*(sv>0.25),2)*foc
ml=pa.mean(2,keepdims=True); pa=ml+(pa-ml)*(1+0.22*meat[...,None]); pa=pa*(1+np.array([0.04,0.0,-0.05])*meat[...,None])
def ss(t): t=np.clip(t,0,1); return t*t*(3-2*t)
m=ss((Y-PH*0.04)/(PH*0.34))*ss((PH-Y-PH*0.02)/(PH*0.46))*ss(X/(W*0.08))**0.4*ss((W-X)/(W*0.08))**0.4
base=np.full((H,W,3),BG,float); Yg,Xg=np.mgrid[0:H,0:W]
glow=np.exp(-(((Xg-W*0.45)/(W*0.7))**2+((Yg-(PY+PH*0.5))/560)**2))
base+=glow[...,None]*np.array([30,13,3])
seg=base[PY:PY+PH]; seg[:]=seg*(1-m[...,None])+pa*m[...,None]
vd=np.sqrt(((Xg-W/2)/(W*0.75))**2+((Yg-H*0.5)/(H*0.6))**2)
base=base*(1-0.35*np.clip(vd-0.4,0,1))[...,None]+noise(W,H,5.5,21)[...,None]
img=Image.fromarray(np.clip(base,0,255).astype(np.uint8)).convert('RGBA')
d=ImageDraw.Draw(img); boxes={}; L=96; R=W-96
def T(key,xy,s_,f,fill,anchor='ls'):
    d.text(xy,s_,font=f,fill=fill,anchor=anchor); boxes[key]=d.textbbox(xy,s_,font=f,anchor=anchor)
def TR(key,xy,s_,f,fill,sp,anchor='l'):
    w=track(d,xy,s_,f,fill,sp,anchor); x=xy[0]-(w if anchor=='r' else 0)
    bb=d.textbbox((x,xy[1]),s_,font=f); boxes[key]=(x,bb[1],x+w,bb[3])
# group 1: editorial top-left
TR('label',(L,300),'SIGNATURE GRILLED PORK NECK',mont(21,500),GOLD,5)
T('h1',(L-5,448),'Dinner is',corm(112,300),CREAM)
T('h2',(L-5,556),'open.',corm(112,400,italic=True),GOLD)
T('cn',(L,632),'招牌炭烧猪颈肉',scserif(38),CREAM)
# group 2: hours bottom-right
B=1488
d.line([(R-90,B-40),(R,B-40)],fill=GOLD+(255,),width=2)
TR('hours',(R,B),'DINNER  17:00–22:00',mont(23,500),CREAM,5,'r')
T('cnhours',(R,B+66),'晚市 17:00–22:00',scserif(30),MUTE,'rs')
# group 3: foil signature bottom-left on the same row
wm=logo_mask('word',58); fo=foil(wm); sx=L; sy=B+66-wm.height+4
sh,pad=soft_shadow(wm,3,130,(0,2)); img.alpha_composite(sh,(sx-pad,sy-pad)); img.alpha_composite(fo,(sx,sy))
boxes['sig']=(sx,sy,sx+wm.width,sy+wm.height)
for kk,b in boxes.items(): assert b[1]>=250 and b[3]<=1570,(kk,b)
print({k:tuple(int(v) for v in b) for k,b in boxes.items()}, 'photo',PY,PY+PH)
img.convert('RGB').save(OUT,quality=94,subsampling=0)
