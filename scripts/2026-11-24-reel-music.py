#!/usr/bin/env python3
"""2026-11-24 Reel music — original, sample-based (FluidSynth + FluidR3_GM SoundFont, MIT licence).

Genre: neo-classical cinematic minimalism (no drum kit), 90 BPM, D minor → F major resolution on the end card.
Instruments (real-instrument samples): grand piano 8th-note ostinato, string ensemble pad, cello + contrabass long lines,
celesta glints on each step, string tremolo riser into the twist, soft timpani hits on scene cuts.
Different from 23 Nov (nu-jazz groove, 120 BPM, marimba/pizz/finger bass/Rhodes/kit) and the 17–22 Nov synth beds.
One scene per bar: cuts every 2.667 s (bar = 4 beats at 90 BPM); total 10 bars = 26.67 s.
Mix: synthetic hall reverb (2.2 s) on piano/strings/celesta, EQ, gentle bus compression, −14 LUFS, true peak ≤ −1 dBFS,
10 ms fade-in, 1.2 s cosine fade-out.
"""
import os, subprocess, numpy as np, mido, pyloudnorm as pyln
from scipy.io import wavfile
from scipy.signal import fftconvolve, butter, sosfilt, resample_poly
BPM, TPB = 90, 480
BAR = 4 * 60 / BPM
DUR = 10 * BAR
OUT = "/tmp/reel24"
SF = "/usr/share/sounds/sf2/FluidR3_GM.sf2"
def tk(b): return int(round(b * TPB))
events = {}
def note(tr, ch, beat, dur, n, vel):
    events.setdefault(tr, []).append((tk(beat), mido.Message('note_on', channel=ch, note=n, velocity=vel)))
    events.setdefault(tr, []).append((tk(beat + dur), mido.Message('note_off', channel=ch, note=n, velocity=0)))
def prog(tr, ch, p, vol=100, pan=64, rev=40):
    for c, v in ((7, vol), (10, pan), (91, rev)):
        events.setdefault(tr, []).append((0, mido.Message('control_change', channel=ch, control=c, value=v)))
    events.setdefault(tr, []).append((0, mido.Message('program_change', channel=ch, program=p)))
# 0 piano, 1 strings, 2 cello, 3 contrabass, 4 celesta, 5 tremolo, 6 timpani
prog('pno', 0, 0, 100, 60, 30); prog('str', 1, 48, 84, 70, 60); prog('vc', 2, 42, 88, 50, 40); prog('cb', 3, 43, 90, 64, 20)
prog('cel', 4, 8, 80, 84, 70); prog('trm', 5, 44, 80, 64, 60); prog('tim', 6, 47, 96, 64, 30)
# D minor progression: Dm, Bb, F, C (i–VI–III–VII); twist bar 7 Gm, tip bar 8 A(sus→maj), end bar 9 F major add9
H = {
 'Dm': (38, [62, 65, 69], [50, 57, 62, 65]),
 'Bb': (34, [62, 65, 70], [46, 53, 58, 62]),
 'F':  (41, [60, 65, 69], [53, 57, 60, 65]),
 'C':  (36, [60, 64, 67], [48, 55, 60, 64]),
 'Gm': (43, [62, 67, 70], [55, 58, 62, 67]),
 'A':  (45, [61, 64, 69], [57, 61, 64, 69]),
 'Fadd9': (41, [65, 67, 69, 72], [53, 60, 65, 69]),
}
seq = ['Dm', 'Bb', 'Dm', 'Bb', 'F', 'C', 'Dm', 'Gm', 'A', 'Fadd9']
for bar, ch in enumerate(seq):
    b0 = bar * 4; root, up, pad = H[ch]
    # piano ostinato: 8ths, broken pattern; hook bar sparse quarter notes; end bar a rolled chord
    if bar == 9:
        for i, n in enumerate([41, 53, 60, 65, 69, 72, 76]): note('pno', 0, b0 + i * .12, 3.6 - i * .12, n, 78 - i * 3)
    else:
        pat = [up[0] - 12, up[1], up[2], up[1], up[0], up[1], up[2], up[1]]
        step = 1 if bar == 0 else .5
        for i in range(int(4 / step)):
            n = pat[i % 8] if bar else pat[(i * 2) % 8]
            v = (82 if i % 4 == 0 else 66) if bar else 74
            if bar == 7 and i >= 4: v -= 14  # breathe before twist
            note('pno', 0, b0 + i * step, step * .95, n, v)
    # strings pad from bar 1
    if bar >= 1:
        for n in pad: note('str', 1, b0, 3.98 if bar < 9 else 4.0, n, 66 if bar < 9 else 72)
    # cello long line + contrabass root from bar 2
    if bar >= 2:
        note('vc', 2, b0, 3.95, root + 12, 76)
        note('cb', 3, b0, 3.95, root, 84)
    # celesta glint: one 3-note figure on each step bar (2–6) and end
    if 2 <= bar <= 6 or bar == 9:
        for i, n in enumerate([up[2] + 12, up[1] + 12, up[2] + 17 if ch != 'C' else up[2] + 12]):
            note('cel', 4, b0 + .25 + i * .5, .6, n, 70 - i * 6)
    # tremolo riser across bars 7–8
    if bar in (7, 8):
        for n in (pad[-1] + 12, pad[-2] + 12): note('trm', 5, b0, 3.95, n, 52 if bar == 7 else 64)
    # timpani: soft hit on each cut (bar line) from bar 1, roll into end card
    if 1 <= bar <= 9:
        note('tim', 6, b0, 1.5, root if root >= 41 else root + 12, 70 if bar not in (7, 9) else 92)
    if bar == 8:
        for i in range(8): note('tim', 6, b0 + 2 + i * .25, .25, 45, 40 + i * 5)

mid = mido.MidiFile(ticks_per_beat=TPB)
tempo = mido.MidiTrack(); tempo.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(BPM), time=0)); mid.tracks.append(tempo)
tracks = {}
for name, ev in events.items():
    tr = mido.MidiTrack(); ev.sort(key=lambda x: (x[0], 0 if x[1].type != 'note_on' else 1)); last = 0
    for t, msg in ev: tr.append(msg.copy(time=t - last)); last = t
    tracks[name] = tr; mid.tracks.append(tr)
os.makedirs(OUT, exist_ok=True); mid.save(f"{OUT}/music.mid")
SR = 48000
def render(keep, wav):
    m2 = mido.MidiFile(ticks_per_beat=TPB); m2.tracks.append(tempo)
    for k in keep: m2.tracks.append(tracks[k])
    m2.save(f"{OUT}/tmp.mid")
    subprocess.run(["fluidsynth", "-ni", "-g", "0.6", "-r", str(SR), "-R", "0", "-C", "0", "-F", wav, SF, f"{OUT}/tmp.mid"], check=True, capture_output=True)
    sr, x = wavfile.read(wav); x = x.astype(np.float64) / 32768.0
    n = int(SR * (DUR + 3)); return np.pad(x, ((0, max(0, n - len(x))), (0, 0)))[:n]
pno = render(['pno'], f"{OUT}/pno.wav"); strg = render(['str', 'trm'], f"{OUT}/str.wav")
low = render(['vc', 'cb'], f"{OUT}/low.wav"); cel = render(['cel'], f"{OUT}/cel.wav"); tim = render(['tim'], f"{OUT}/tim.wav")
hp = lambda f: butter(2, f, 'hp', fs=SR, output='sos'); lp = lambda f: butter(2, f, 'lp', fs=SR, output='sos')
pno = sosfilt(hp(90), pno, axis=0); strg = sosfilt(hp(140), strg, axis=0); cel = sosfilt(hp(400), cel, axis=0)
low = sosfilt(lp(3000), low, axis=0); tim = sosfilt(lp(5000), tim, axis=0)
# gentle pulse ducking of the pad on each beat (breathing, not EDM pumping)
env = np.ones(len(strg)); bt = int(60 / BPM * SR)
for k in range(0, len(env), bt):
    L = min(int(.18 * SR), len(env) - k); env[k:k + L] = 1 - .12 * np.exp(-np.linspace(0, 4, L))
strg *= env[:, None]
dry = 1.0 * pno + 0.85 * strg + 0.9 * low + 0.6 * cel + 0.8 * tim
rng = np.random.default_rng(24); L = int(2.2 * SR); t = np.arange(L) / SR
ir = rng.standard_normal((L, 2)) * np.exp(-t * 3.2)[:, None]; ir[:int(.025 * SR)] = 0
ir = sosfilt(butter(2, [250, 7000], 'bp', fs=SR, output='sos'), ir, axis=0); ir /= np.abs(ir).sum(0).max() / 5
send = 0.9 * pno + strg + 1.2 * cel + 0.3 * tim
wet = np.stack([fftconvolve(send[:, c], ir[:, c])[:len(dry)] for c in range(2)], 1)
mix = dry + 0.22 * wet
rms = np.sqrt(np.convolve((mix ** 2).mean(1), np.ones(1440) / 1440, 'same')) + 1e-9
g = np.where(rms > 0.12, (rms / 0.12) ** (-0.3), 1.0); mix *= g[:, None]
mix = mix[:int(DUR * SR)]
fi, fo = int(.01 * SR), int(1.2 * SR)
mix[:fi] *= np.linspace(0, 1, fi)[:, None]; mix[-fo:] *= (np.cos(np.linspace(0, np.pi, fo)) * .5 + .5)[:, None]
meter = pyln.Meter(SR); mix = pyln.normalize.loudness(mix, meter.integrated_loudness(mix), -14.0)
lim = 10 ** (-1.2 / 20); k = lim * .85
mix = np.where(np.abs(mix) > k, np.sign(mix) * (k + (lim - k) * np.tanh((np.abs(mix) - k) / (lim - k))), mix)
print(f"LUFS {meter.integrated_loudness(mix):.1f}  truepeak {20*np.log10(np.abs(resample_poly(mix,4,1,axis=0)).max()):.1f} dBFS  dur {len(mix)/SR:.2f}s  first {np.abs(mix[0]).max():.4f} last {np.abs(mix[-1]).max():.4f}")
wavfile.write(f"{OUT}/music.wav", SR, (mix * 32767).astype(np.int16))
