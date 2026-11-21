#!/usr/bin/env python3
"""Original synthesized music bed + transition whooshes for the 2026-11-21 "FOB vs CIF vs DDP" Reel (adapted from 2026-11-20).
Everything is generated from scratch here (numpy oscillators + noise), so there is no third-party copyright:
licence = original work by LinkWin / Grok Bot, free to use. 120 BPM, 24.0 s = 12 bars; brighter progression (Fmaj7-Dm7-Bbmaj7-C).
Whoosh on every scene change, a soft 'ping' when each risk pin drops.
The bed is rendered cyclically (the tail wraps to the start) so the Reel loops without a click.
usage: python3 scripts/2026-11-21-reel-audio.py out.wav
"""
import sys, numpy as np
from scipy.signal import butter, sosfilt
from scipy.io import wavfile
SR=48000; T=24.0; N=int(SR*T); TAIL=int(SR*3)
BEAT=0.5
rng=np.random.default_rng(21)
out=np.zeros((N+TAIL,2))
def add(sig,t0,gain=1.0,pan=0.0):
    i=int(t0*SR); n=min(len(sig),len(out)-i)
    l=np.cos((pan+1)*np.pi/4); r=np.sin((pan+1)*np.pi/4)
    out[i:i+n,0]+=sig[:n]*gain*l*1.414; out[i:i+n,1]+=sig[:n]*gain*r*1.414
def env(n,a,d,s=0.0,r=0.0):
    e=np.ones(n)
    na=max(1,int(a*SR)); e[:na]=np.linspace(0,1,na)
    nd=int(d*SR); e[na:na+nd]=np.linspace(1,s,len(e[na:na+nd]))
    e[na+nd:]=s
    if r: nr=int(r*SR); e[-nr:]*=np.linspace(1,0,nr)
    return e
def lp(x,f,o=2): return sosfilt(butter(o,f,'low',fs=SR,output='sos'),x)
def hp(x,f,o=2): return sosfilt(butter(o,f,'high',fs=SR,output='sos'),x)
def bp(x,f1,f2): return sosfilt(butter(2,[f1,f2],'band',fs=SR,output='sos'),x)
def midi(m): return 440*2**((m-69)/12)
# chords (Am - F - C - G), 1 bar each, repeating; voicings in midi
CH=[[53,57,60,64],[50,53,57,60],[46,50,53,57],[48,52,55,60]]
BASS=[53,50,46,48]
for bar in range(12):
    t0=bar*2.0; c=CH[bar%4]
    # warm pad: detuned saws, low-passed, slow attack
    n=int(2.6*SR); tt=np.arange(n)/SR; pad=np.zeros(n)
    for m in c:
        for det in (-0.08,0.08):
            f=midi(m+det); pad+=2*((tt*f)%1)-1
    pad=lp(pad,1400,4)*env(n,0.35,0.3,0.7,0.6)/8
    add(pad,t0,0.16,0.0)
    # bass: soft sine + a little 2nd harmonic, on beats 1 and 3
    for b in (0,2):
        n=int(0.9*SR); tt=np.arange(n)/SR; f=midi(BASS[bar%4]-12)
        s=(np.sin(2*np.pi*f*tt)+0.25*np.sin(4*np.pi*f*tt))*env(n,0.01,0.8,0.0)
        add(s,t0+b*BEAT,0.28)
    # kick on 1 and 3, very soft
    for b in (0,2):
        n=int(0.35*SR); tt=np.arange(n)/SR
        f=50+90*np.exp(-tt*30); ph=2*np.pi*np.cumsum(f)/SR
        add(np.sin(ph)*np.exp(-tt*9),t0+b*BEAT,0.30)
    # closed hat on offbeats + light 16th shaker
    for k in range(8):
        n=int(0.06*SR); h=hp(rng.standard_normal(n),7000)*np.exp(-np.arange(n)/SR*70)
        add(h,t0+k*0.25+0.125 if k%2==0 else t0+k*0.25+0.125,0.045 if k%2 else 0.03,0.25)
    # pluck arpeggio (16ths) up the chord, quiet, panned
    arp=c+[c[1]+12]
    for k in range(8):
        m=arp[k%len(arp)]+12; n=int(0.4*SR); tt=np.arange(n)/SR; f=midi(m)
        s=(np.sin(2*np.pi*f*tt)+0.3*np.sin(6*np.pi*f*tt)*np.exp(-tt*20))*np.exp(-tt*9)
        add(s,t0+k*0.25,0.035,-0.4+0.8*(k%2))
def whoosh(t_center,dur=0.55,gain=0.22):
    n=int(dur*SR); x=rng.standard_normal(n); tt=np.linspace(0,1,n)
    # sweep a band-pass upward by processing in chunks
    y=np.zeros(n); ch=1024
    for i in range(0,n,ch):
        fc=300+5000*(tt[i]**1.6); y[i:i+ch]=bp(x[i:i+ch],fc*0.6,min(fc*1.6,20000))
    e=np.sin(np.pi*tt)**2
    add(lp(y,9000)*e,t_center-dur*0.6,gain,-0.3); add(lp(y,9000)*e,t_center-dur*0.55,gain*0.8,0.3)
def ping(t0,m,gain=0.10):
    n=int(1.2*SR); tt=np.arange(n)/SR; f=midi(m)
    s=(np.sin(2*np.pi*f*tt)+0.4*np.sin(2*np.pi*2*f*tt)*np.exp(-tt*6))*np.exp(-tt*4.5)
    add(s,t0,gain)
CUTS=[2.2,7.2,12.2,17.0,19.6]
for c in CUTS: whoosh(c+0.15,0.6,0.18)
for k,t in enumerate([3.5,8.5,13.5]): ping(t,[81,84,88][k],0.10)
ping(20.9,77,0.08); ping(21.3,81,0.07); ping(21.7,84,0.06)
whoosh(23.7,0.6,0.14)  # fade back to the hook for the loop
# wrap tail for seamless loop
mix=out[:N].copy(); mix[:TAIL]+=out[N:N+TAIL]
mix=np.tanh(mix*1.2)/1.2
mix/=np.max(np.abs(mix))*1.12
wavfile.write(sys.argv[1] if len(sys.argv)>1 else "bed.wav",SR,(mix*32767).astype(np.int16))
