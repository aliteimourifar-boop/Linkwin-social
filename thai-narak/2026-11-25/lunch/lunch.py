# Thai Narak Story 2026-11-25 LUNCH v2 - "Lemongrass: / bruise, don't chop." Daylight Editorial (typographic hero)
# v2 (CD rejection of v1: root hero mismatched headline, blown root highlights, inpaint smudge, tiny logo, dead bottom):
# ONLY the green lemongrass blades from top-left of food-garlic-bread.png are keyed out (HSV green key + bright-highlight
# fill, geometric guard far above the roots, dark stone pixels zeroed, 1.2px feather) - zero root / newspaper pixels.
# Layout: cream-sand page; blade sweep diagonally across the upper third bleeding off the top/right edge (photo's own
# cropped edge sits on the canvas edge), a smaller 180-deg counter-sweep bleeding off the bottom edge; centred mid-frame
# type stack + gold-foil traced wordmark (90px). No boxes, borders, collage or AI imagery.
import sys;sys.path.insert(0,'/workspace/tn-run/rd')
from dlib import *
from scipy.ndimage import gaussian_filter
import cv2
W,H=1080,1920; OUT=sys.argv[1] if len(sys.argv)>1 else 'story-2026-11-25-lunch-v2.jpg'
P='/cursor/stores/store-71c2a87a-216e-4174-bacc-f3ef6c2eaf39/thai-narak/assets/owner-photos/food-garlic-bread.png'
im=np.asarray(Image.open(P).convert('RGB'))[:420,:1600]
hsv=cv2.cvtColor(im,cv2.COLOR_RGB2HSV_FULL).astype(float)
h=hsv[...,0]*360/256; s=hsv[...,1]/255; v=hsv[...,2]/255
a=np.clip((h-52)/10,0,1)*np.clip((150-h)/10,0,1)*np.clip((s-0.35)/0.2,0,1)*np.clip((v-0.10)/0.12,0,1)
a=np.maximum(a,np.clip((v-0.40)/0.08,0,1)*np.clip((h-40)/8,0,1)*np.clip((170-h)/8,0,1)*np.clip((s-0.10)/0.08,0,1))
reg=np.zeros(a.shape,np.uint8)   # guard polygon: well above the roots (upper root top ~y140 at x520+)
cv2.fillPoly(reg,[np.array([(0,0),(1600,0),(1600,60),(900,60),(640,135),(420,215),(0,300)],np.int32)],1)
a*=reg
b=(a>0.5).astype(np.uint8)
n,lab,st,_=cv2.connectedComponentsWithStats(b); keep=np.zeros_like(b)
for i in range(1,n):
    if st[i,4]>2500: keep[lab==i]=1
keep=cv2.morphologyEx(keep,cv2.MORPH_CLOSE,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(15,15)))
from scipy.ndimage import binary_fill_holes, label as nlabel
holes=binary_fill_holes(keep)&(keep==0); hl,hn=nlabel(holes)
for i in range(1,hn+1):
    mm=hl==i
    if v[mm].mean()>0.30: keep[mm]=1        # blown leaf highlights, not stone
gap=((keep>0)&(v<0.24)&(a<0.3)).astype(np.uint8)   # tiny stone slivers between overlapping blades
im=cv2.inpaint(im,cv2.dilate(gap,np.ones((3,3))),5,cv2.INPAINT_TELEA)   # re-filled with neighbouring leaf colour (no stone left)
keep*=reg
keep=cv2.erode(keep,np.ones((3,3)))
alpha=gaussian_filter(keep.astype(np.float32),1.2)
ys,xs=np.where(alpha>0.02); x0,x1,y1=xs.min(),xs.max()+1,ys.max()+1
f=im.astype(np.float32)
f=np.clip(f*1.22+14,0,255)                      # light daylight brighten, natural colour
lum=(f*[0.299,0.587,0.114]).sum(2,keepdims=True); f=np.clip(lum+(f-lum)*1.05,0,255)
leaf=np.dstack([f,alpha[...,None]*255]).astype(np.uint8)[0:y1,x0:x1]
leaf=Image.fromarray(leaf,'RGBA')
def place(img,lf,sc,pos,rot180=False,sh=(14,22),sha=70):
    L=lf.resize((int(lf.width*sc),int(lf.height*sc)),Image.LANCZOS)
    if rot180: L=L.rotate(180)
    m=L.split()[3]
    s0,p0=soft_shadow(m,10,sha,sh)
    img.alpha_composite(s0,(pos[0]-p0,pos[1]-p0)); img.alpha_composite(L,pos)
SAND=np.array([239,230,214.])
Y,X=np.mgrid[0:H,0:W]
page=np.ones((H,W,3),np.float32)*SAND
r=np.sqrt(((X-W/2)/W)**2+((Y-H*0.5)/H)**2)
page*=(1.015-0.06*r**2)[...,None]                 # gentle daylight falloff, no dark corners
page+=gaussian_filter(np.random.default_rng(4).normal(0,5,(H,W)),1.0)[...,None]*0.6   # paper tooth
img=Image.fromarray(np.clip(page,0,255).astype(np.uint8)).convert('RGBA')
# main sweep: photo's cropped top edge on canvas top, tips toward lower-left, bundle runs off the top/right
place(img,leaf,1.62,(int(40-0*1.62),0))
# counter-sweep (rotated 180): cropped edge on canvas bottom, tips toward upper-right
L2=leaf.resize((int(leaf.width*0.95),int(leaf.height*0.95)))
place(img,leaf,0.95,(W-L2.width-30+0,H-L2.height),rot180=True,sh=(10,14),sha=55)
BROWN=(58,42,30); GOLD=(178,132,52)
d=ImageDraw.Draw(img); boxes={}; CX=W//2
f1=corm(168,300); f2=corm(140,500,italic=True)
yb=880
d.text((CX,yb),'Lemongrass:',font=f1,fill=BROWN,anchor='ms'); boxes['h1']=d.textbbox((CX,yb),'Lemongrass:',font=f1,anchor='ms')
tm=Image.new('L',(W,300),0); ImageDraw.Draw(tm).text((CX,200),"bruise, don’t chop.",font=f2,fill=255,anchor='ms')
bb=tm.getbbox(); tm=tm.crop(bb); fo=foil(tm,seed=5)
fa=np.asarray(fo).astype(float); fa[...,:3]*=0.80; fo=Image.fromarray(fa.astype(np.uint8),'RGBA')
s0,p0=soft_shadow(tm,3,60,(0,2)); ty=1035-200+bb[1]
img.alpha_composite(s0,(bb[0]-p0,ty-p0)); img.alpha_composite(fo,(bb[0],ty)); boxes['h2']=(bb[0],ty,bb[2],ty+tm.height)
d=ImageDraw.Draw(img)
def C(key,y,s_,f,fill,sp=0):
    w_=sum(d.textlength(ch,font=f) for ch in s_)+sp*(len(s_)-1); x0=CX-w_/2
    track(d,(x0,y),s_,f,fill,sp); b=d.textbbox((x0,y),s_,font=f); boxes[key]=(x0,b[1],x0+w_,b[3])
C('cn',1095,'香茅先拍裂，香气才出来',scserif(54),BROWN,8)
d.line([(CX-44,1200),(CX+44,1200)],fill=GOLD,width=2)
fm=mont(26,500); fc=scsans(26); a_='LUNCH 11:00–15:00'; b_='午市'
wa=sum(d.textlength(ch,font=fm) for ch in a_)+6*(len(a_)-1); wb=d.textlength(b_,font=fc)+3
x0=CX-(wa+18+wb)/2; track(d,(x0,1230),a_,fm,BROWN,6); track(d,(x0+wa+18,1228),b_,fc,BROWN,3)
boxes['hours']=(x0,d.textbbox((x0,1230),a_,font=fm)[1],x0+wa+18+wb,d.textbbox((x0+wa+18,1228),b_,font=fc)[3])
wm=logo_mask('word',92); fo=foil(wm); sx,sy=CX-wm.width//2,1390
s0,p0=soft_shadow(wm,4,70,(0,2)); img.alpha_composite(s0,(sx-p0,sy-p0)); img.alpha_composite(fo,(sx,sy))
boxes['logo']=(sx,sy,sx+wm.width,sy+wm.height)
for kk,b in boxes.items(): assert b[1]>=250 and b[3]<=1570,(kk,b)
print({kk:tuple(int(v) for v in b) for kk,b in boxes.items()}, 'logo size',wm.size)
img.convert('RGB').save(OUT,quality=94,subsampling=0)
img.convert('RGB').resize((540,960)).save('/tmp/v2half.png')
