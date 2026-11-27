"""2026-11-27 Reel music — original, sample-based (FluidSynth + FluidR3_GM SoundFont, MIT licence).

Genre: Silk Road chamber fusion — Persian-flavoured hammered dulcimer (santur-like) ostinato, koto plucks (Chinese
  zither colour), shakuhachi/ney-like flute melody, cello + contrabass drone, hand percussion (bongo/conga/tambourine,
  frame-drum feel). No piano, no strings ensemble, no drum kit, no marimba/Rhodes (all used 23–24 Nov).
Mode: D Phrygian dominant (Hijaz) → resolves on D major-colour drone at the end card. 100 BPM, 4/4, 9 bars = 21.6 s.
Cuts: on bar lines / half bars (2.4 s / 1.2 s grid). Mix: hall reverb on melodic parts, EQ, bus compression,
  −14 LUFS integrated, true peak ≤ −1 dBFS (limiter ceiling −2.8 dBTP before AAC), 40 ms fade-in (avoids AAC priming overshoot on the first transient), 1.0 s cosine fade-out.
"""
import os, subprocess, numpy as np, mido, pyloudnorm as pyln
from scipy.io import wavfile
from scipy.signal import fftconvolve, butter, sosfilt, resample_poly
BPM, TPB = 100, 480
BAR = 4 * 60 / BPM
NBARS = 9
DUR = NBARS * BAR
OUT = "/tmp/reel27"
SF = "/usr/share/sounds/sf2/FluidR3_GM.sf2"
def tk(b): return int(round(b * TPB))
events = {}
def note(tr, ch, beat, dur, n, vel):
    events.setdefault(tr, []).append((tk(beat), mido.Message('note_on', channel=ch, note=n, velocity=max(1, min(127, vel)))))
    events.setdefault(tr, []).append((tk(beat + dur), mido.Message('note_off', channel=ch, note=n, velocity=0)))
def prog(tr, ch, p, vol=100, pan=64, rev=40):
    for c, v in ((7, vol), (10, pan), (91, rev)):
        events.setdefault(tr, []).append((0, mido.Message('control_change', channel=ch, control=c, value=v)))
    if ch != 9: events.setdefault(tr, []).append((0, mido.Message('program_change', channel=ch, program=p)))
prog('dul', 0, 15, 100, 50, 40); prog('koto', 1, 107, 92, 84, 40); prog('fl', 2, 77, 88, 64, 70)
prog('vc', 3, 42, 84, 56, 40); prog('cb', 4, 43, 86, 64, 20); prog('perc', 9, 0, 100, 64, 25)
# D Hijaz: D Eb F# G A Bb C
D = 62
# harmony per bar (root for drone, 4-note dulcimer cell)
cells = {
 'D':  (38, [62, 66, 69, 74]),
 'Eb': (39, [63, 67, 70, 75]),
 'Cm': (36, [60, 63, 67, 72]),
 'Gm': (43, [62, 67, 70, 74]),
}
seq = ['D', 'D', 'Eb', 'D', 'Cm', 'D', 'Gm', 'Eb', 'D']
for bar, c in enumerate(seq):
    b0 = bar * 4; root, cell = cells[c]
    # santur-like 16th ostinato (lighter in bar 0 = hook, full from bar 1)
    pat = [0, 2, 1, 3, 2, 1, 3, 1] if bar % 2 == 0 else [0, 1, 2, 3, 1, 2, 3, 2]
    step = .25 if bar >= 1 else .5
    if bar < NBARS - 1:
        for i in range(int(4 / step)):
            n = cell[pat[i % 8]] + (12 if (i % 8 == 3 and bar >= 4) else 0)
            v = 84 if i % 4 == 0 else 62 + (i % 2) * 6
            note('dul', 0, b0 + i * step, step * 1.6, n, v)
    else:
        for i, n in enumerate([50, 57, 62, 66, 69, 74, 78]): note('dul', 0, b0 + i * .1, 3.8 - i * .1, n, 80 - i * 3)
    # koto: two plucks per bar answering on beats 2.5 and 4
    if 1 <= bar < NBARS - 1:
        note('koto', 1, b0 + 1.5, 1.2, cell[3] + 12, 78); note('koto', 1, b0 + 3.0, 1.0, cell[2] + 12, 70)
    # drone from bar 0
    note('vc', 3, b0, 3.95, root + 12, 64 if bar == 0 else 74)
    if bar >= 1: note('cb', 4, b0, 3.95, root, 82)
# flute (ney-like) melody bars 2-7
mel = [(2, 0, 1.5, 74), (2, 1.5, .5, 75), (2, 2, 2, 78),
       (3, 0, 1, 77), (3, 1, 1, 75), (3, 2, 2, 74),
       (4, 0, 1.5, 72), (4, 1.5, .5, 70), (4, 2, 2, 72),
       (5, 0, 1, 75), (5, 1, 1, 74), (5, 2, 2, 69),
       (6, 0, 2, 70), (6, 2, 2, 74),
       (7, 0, 1, 75), (7, 1, 1, 78), (7, 2, 2, 79)]
for b, s, d, n in mel: note('fl', 2, b * 4 + s, d * .97, n, 74)
note('fl', 2, 8 * 4, 3.8, 78, 70)
# hand percussion: doumbek-like pattern on bongos/congas + tambourine
for bar in range(NBARS):
    b0 = bar * 4
    if bar == 0:
        for s in (0, 1.5, 2, 3, 3.5): note('perc', 9, b0 + s, .2, 64, 90 if s == 0 else 70)
        continue
    if bar == NBARS - 1:
        note('perc', 9, b0, .4, 64, 100); note('perc', 9, b0, .4, 54, 70); continue
    for s, n, v in [(0, 64, 104), (1, 63, 80), (1.5, 62, 64), (2, 64, 96), (2.5, 63, 70), (3, 62, 84), (3.5, 60, 64), (3.75, 60, 54)]:
        note('perc', 9, b0 + s, .2, n, v)
    for i in range(8): note('perc', 9, b0 + i * .5 + .5, .1, 54, 44 + (i % 2) * 10)
    if bar == NBARS - 2:
        for i in range(8): note('perc', 9, b0 + 2 + i * .25, .1, 61, 50 + i * 7)

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
dul = render(['dul'], f"{OUT}/dul.wav"); koto = render(['koto'], f"{OUT}/koto.wav"); fl = render(['fl'], f"{OUT}/fl.wav")
low = render(['vc', 'cb'], f"{OUT}/low.wav"); perc = render(['perc'], f"{OUT}/perc.wav")
hp = lambda f: butter(2, f, 'hp', fs=SR, output='sos'); lp = lambda f: butter(2, f, 'lp', fs=SR, output='sos')
dul = sosfilt(hp(160), dul, axis=0); koto = sosfilt(hp(200), koto, axis=0); fl = sosfilt(hp(250), fl, axis=0)
low = sosfilt(lp(2500), low, axis=0); perc = sosfilt(hp(60), perc, axis=0)
dry = 0.9 * dul + 0.75 * koto + 0.7 * fl + 0.85 * low + 0.95 * perc
rng = np.random.default_rng(27); L = int(2.6 * SR); t = np.arange(L) / SR
ir = rng.standard_normal((L, 2)) * np.exp(-t * 2.8)[:, None]; ir[:int(.03 * SR)] = 0
ir = sosfilt(butter(2, [300, 8000], 'bp', fs=SR, output='sos'), ir, axis=0); ir /= np.abs(ir).sum(0).max() / 5
send = 0.8 * dul + koto + 1.3 * fl + 0.25 * perc
wet = np.stack([fftconvolve(send[:, c], ir[:, c])[:len(dry)] for c in range(2)], 1)
mix = dry + 0.24 * wet
rms = np.sqrt(np.convolve((mix ** 2).mean(1), np.ones(1440) / 1440, 'same')) + 1e-9
g = np.where(rms > 0.12, (rms / 0.12) ** (-0.3), 1.0); mix *= g[:, None]
mix = mix[:int(DUR * SR)]
fi, fo = int(.04 * SR), int(1.0 * SR)
mix[:fi] *= np.linspace(0, 1, fi)[:, None]; mix[-fo:] *= (np.cos(np.linspace(0, np.pi, fo)) * .5 + .5)[:, None]
from scipy.ndimage import maximum_filter1d, uniform_filter1d
meter = pyln.Meter(SR)
def limit(x, ceil_db=-2.8):
    c = 10 ** (ceil_db / 20); up = np.abs(resample_poly(x, 4, 1, axis=0)).max(1)
    pk = up.reshape(-1, 4).max(1)[:len(x)]
    need = np.minimum(1.0, c / np.maximum(pk, 1e-9))
    g = -maximum_filter1d(-need, size=int(.004 * SR))          # 4 ms look-around (min gain)
    g = uniform_filter1d(g, size=int(.003 * SR))
    g = np.minimum(g, need)
    return x * g[:, None]
for _ in range(4):
    mix = pyln.normalize.loudness(mix, meter.integrated_loudness(mix), -14.0)
    mix = limit(mix)
mix[:fi] *= np.linspace(0, 1, fi)[:, None]
print(f"LUFS {meter.integrated_loudness(mix):.1f}  truepeak {20*np.log10(np.abs(resample_poly(mix,4,1,axis=0)).max()):.1f} dBFS  dur {len(mix)/SR:.2f}s  first {np.abs(mix[0]).max():.4f} last {np.abs(mix[-1]).max():.4f}")
wavfile.write(f"{OUT}/music.wav", SR, (mix * 32767).astype(np.int16))
