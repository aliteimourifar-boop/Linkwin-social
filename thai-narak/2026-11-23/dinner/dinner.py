# Thai Narak Story 2026-11-23 DINNER - "How hot / tonight?" Graphic Typographic (spice poll)
# Layout: single chili-red field, oversized staggered headline (left 'How hot' / right 'tonight?'),
# real chili cut-out from owner photo tucked under the headline, CJK question, two hairline poll pills,
# info line left; gold-foil traced wordmark top-left. No photo panel, no black, no boxes.
import sys;sys.path.insert(0,'/workspace/tn-run/rd')
from dlib import *
from scipy.ndimage import gaussian_filter, binary_erosion
W,H=1080,1920; OUT=sys.argv[1] if len(sys.argv)>1 else 'story-2026-11-23-dinner.jpg'
RED=np.array([200,52,31.]); CREAM=(248,236,214); GOLDT=(240,200,120); DEEP=(150,34,20)
Y,X=np.mgrid[0:H,0:W]
f=RED[None,None,:]*np.ones((H,W,1))
f=f+(np.exp(-(((X-760)/650.)**2+((Y-620)/620.)**2))*16)[...,None]*np.array([1,0.6,0.4])
f=f-(((Y/H)**2)*22)[...,None]*np.array([1,0.5,0.4])
f=f+noise(W,H,2.2,7,blur=0.6)[...,None]
img=Image.fromarray(np.clip(f,0,255).astype(np.uint8)).convert('RGBA')
# tone-on-tone giant question mark (background texture, not text content)
qm=Image.new('L',(W,H),0); ImageDraw.Draw(qm).text((1140,1210),'?',font=corm(1200,500,italic=True),fill=255,anchor='rs')
ql=tint_layer(qm.point(lambda p:int(p*0.16)),(120,22,12)); img.alpha_composite(ql)
d=ImageDraw.Draw(img); boxes={}
def L(key,x,y,s_,f,fill,sp=0,anchor='l'):
    w=sum(d.textlength(ch,font=f) for ch in s_)+sp*(len(s_)-1)
    x0=x-w if anchor=='r' else (x-w/2 if anchor=='c' else x)
    track(d,(x0,y),s_,f,fill,sp); bb=d.textbbox((x0,y),s_,font=f); boxes[key]=(x0,bb[1],x0+w,bb[3]); return w
M=84
# wordmark top-left (gold foil, traced vector)
wm=logo_mask('word',68); fo=foil(wm); sx,sy=M,282
s0,p0=soft_shadow(wm,4,110,(0,3)); img.alpha_composite(s0,(sx-p0,sy-p0)); img.alpha_composite(fo,(sx,sy))
boxes['sig']=(sx,sy,sx+wm.width,sy+wm.height)
d=ImageDraw.Draw(img)
L('kick',W-M,300,"TONIGHT'S POLL",mont(22,600),CREAM,6,'r')
L('kickcn',W-M,334,'今晚投票',scsans(22),CREAM,8,'r')
# headline
f1=corm(270,600); f2=corm(270,500,italic=True)
d.text((M-14,690),'How hot',font=f1,fill=CREAM,anchor='ls'); boxes['h1']=d.textbbox((M-14,690),'How hot',font=f1,anchor='ls')
d.text((W-M+6,900),'tonight?',font=f2,fill=GOLDT,anchor='rs'); boxes['h2']=d.textbbox((W-M+6,900),'tonight?',font=f2,anchor='rs')
# real chili accent (owner photo cut-out), tucked left under 'How hot'
ch=Image.open('chili_cut.png'); a=np.asarray(ch.split()[-1])>128
a=gaussian_filter(binary_erosion(a,iterations=3).astype(float),1.0); ch.putalpha(Image.fromarray((a*255).astype(np.uint8)))
ch=ch.resize((250,int(250*ch.height/ch.width)),Image.LANCZOS).rotate(-8,resample=Image.BICUBIC,expand=True)
cx,cy=760,978
sh,ps=soft_shadow(ch.split()[-1],10,120,(6,12)); img.alpha_composite(sh,(cx-ps,cy-ps)); img.alpha_composite(ch,(cx,cy))
d=ImageDraw.Draw(img)
# CJK question
L('cn',M,1000,'今晚，辣一点还是不辣？',scserif(54,bold=True),CREAM,4)
# poll pills (hairline, elegant)
def pill(key,y,label,cn,filled,dots):
    x0,x1,h=M,W-M,104
    if filled: d.rounded_rectangle((x0,y,x1,y+h),radius=h//2,fill=CREAM)
    else: d.rounded_rectangle((x0,y,x1,y+h),radius=h//2,outline=CREAM,width=2)
    col=(170,40,24) if filled else CREAM
    L(key,x0+52,y+h/2-15,label,mont(28,600),col,6)
    L(key+'cn',x1-52,y+h/2-22,cn,scsans(30),col,4,'r')
    boxes[key+'pill']=(x0,y,x1,y+h)
w=L('vote',M,1148,'TAP TO VOTE ·',mont(18,500),CREAM,5)
L('votecn',M+w+12,1144,'选一个',scsans(20),CREAM,4)
pill('o1',1192,'BRING THE HEAT','来点辣',True,3)
pill('o2',1322,'KEEP IT MILD','不要辣',False,0)
# info
d.line([(M,1490),(M+60,1490)],fill=GOLDT,width=2)
w=L('hours',M,1514,'DINNER 17:00–22:00',mont(22,600),CREAM,5)
L('info',M+w+18,1511,'晚市 · 地铁1号线 西门口站',scsans(23),CREAM,3)
for kk,b in boxes.items(): assert b[1]>=250 and b[3]<=1570,(kk,b)
print({k:tuple(int(v) for v in b) for k,b in boxes.items()})
img.convert('RGB').save(OUT,quality=94,subsampling=0)
