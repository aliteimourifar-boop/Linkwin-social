#!/usr/bin/env python3
"""2026-11-23 Reel music — original, sample-based (FluidSynth + FluidR3_GM SoundFont, MIT licence).

Genre: minimal nu-jazz / "Swiss precision" groove, 120 BPM, F major (Fmaj9 – Dm9 – Bbmaj7 – C9sus).
Instruments (real-instrument samples): marimba lead motif, pizzicato strings answering, finger electric bass,
Rhodes chord stabs, brushed/tight kit (closed hats, rim, kick, shaker), crash only on scene cuts.
Different from the 17–22 Nov reels (bare synthesized beds from numpy, no samples).
Cuts at 3.0, 5.0, 7.5, 10.0, 12.5, 15.5, 18.0, 20.0 s are all on beats (beat = 0.5 s).
Mix: convolution room reverb (synthetic IR), kick-keyed ducking on Rhodes/strings, −14 LUFS, true peak ≤ −1 dBFS,
10 ms fade in, 0.8 s fade out at 23.0 s.
"""
import os, subprocess, numpy as np, mido, pyloudnorm as pyln
from scipy.io import wavfile
from scipy.signal import fftconvolve, butter, sosfilt
BPM, TPB = 120, 480
DUR = 23.0
OUT = "/tmp/reel23"
SF = "/usr/share/sounds/sf2/FluidR3_GM.sf2"
CUTS = [3.0, 5.0, 7.5, 10.0, 12.5, 15.5, 18.0, 20.0]
def tk(beats): return int(round(beats * TPB))
def sec2beat(s): return s * BPM / 60

mid = mido.MidiFile(ticks_per_beat=TPB)
events = {}  # track -> list of (tick, msg)
def note(tr, ch, beat, dur, n, vel):
    events.setdefault(tr, []).append((tk(beat), mido.Message('note_on', channel=ch, note=n, velocity=vel)))
    events.setdefault(tr, []).append((tk(beat + dur), mido.Message('note_off', channel=ch, note=n, velocity=0)))
def prog(tr, ch, p, vol=100, pan=64, rev=40):
    for c, v in ((7, vol), (10, pan), (91, rev)):
        events.setdefault(tr, []).append((0, mido.Message('control_change', channel=ch, control=c, value=v)))
    events.setdefault(tr, []).append((0, mido.Message('program_change', channel=ch, program=p)))

# channels: 0 marimba, 1 pizz, 2 bass, 3 rhodes, 9 drums
prog('mar', 0, 12, 92, 52, 50); prog('piz', 1, 45, 78, 84, 60); prog('bas', 2, 33, 100, 64, 10); prog('rho', 3, 4, 70, 70, 70)
prog('drm', 9, 0, 100, 64, 30)
BARS = 12
chords = [  # (bass root, rhodes voicing)
    (41, [57, 60, 64, 67]),   # Fmaj9: A C E G over F
    (38, [53, 57, 60, 64]),   # Dm9:  F A C E over D
    (46, [57, 62, 65, 69]),   # Bbmaj7: A D F A over Bb
    (36, [55, 58, 62, 65]),   # C9sus: G Bb D F over C
]
end_beat = sec2beat(20.0)  # end card: groove resolves
for bar in range(BARS):
    b0 = bar * 4
    root, voic = chords[bar % 4]
    if b0 >= end_beat:
        root, voic = 41, [57, 60, 64, 67, 72]
    # bass: syncopated finger bass, sparse in first bar (hook), resolves on end card
    if b0 >= end_beat:
        if b0 == end_beat: note('bas', 2, b0, 3.5, root, 96)
    else:
        pat = [(0, .45, 0, 104), (1.5, .4, 12, 86), (2, .45, 0, 98), (3, .3, 7, 84), (3.5, .4, 10, 80)] if bar > 0 else [(0, 1.5, 0, 100), (2.5, .4, 7, 84), (3.5, .4, 10, 80)]
        for o, d, iv, v in pat: note('bas', 2, b0 + o, d, root + iv, v)
    # rhodes stabs on the off-beats from bar 1
    if b0 >= end_beat:
        if b0 == end_beat:
            for n in voic: note('rho', 3, b0, 5.5, n, 70)
    elif bar >= 1:
        for o in (0.5, 2.5):
            for n in voic: note('rho', 3, b0 + o, .35, n, 62 if o == .5 else 56)
    # marimba motif (4-bar call), pizz answer
    motif = [(0, 72), (.5, 76), (1, 79), (1.75, 77), (2.5, 76), (3, 72)]
    motif2 = [(0, 74), (.5, 77), (1, 81), (1.75, 79), (2.5, 77), (3.25, 74)]
    m = motif if bar % 2 == 0 else motif2
    if b0 < end_beat:
        if bar % 4 in (0, 2):
            for o, n in m: note('mar', 0, b0 + o, .45, n - (0 if bar % 4 == 0 else 2), 88 if o == 0 else 74)
        else:
            for o in (0, .75, 1.5, 2, 3):
                note('piz', 1, b0 + o, .25, voic[(int(o * 4)) % 4] + 12, 74)
    else:
        if b0 == end_beat:
            for i, n in enumerate([72, 76, 79, 84]): note('mar', 0, b0 + i * .25, 1.2, n, 84 - i * 4)
    # drums
    if b0 < end_beat:
        for i in range(8):
            o = i * .5
            note('drm', 9, b0 + o, .1, 42, 64 if i % 2 else 50)           # closed hat
            if bar >= 1: note('drm', 9, b0 + o + .25, .1, 70, 40)         # maracas/shaker 16ths
        for o in ((0, 2.75) if bar == 0 else (0, 1.75, 2, 3.5 if bar % 2 else 2.75)):
            note('drm', 9, b0 + o, .1, 36, 108)                            # kick
        if bar >= 1:
            for o in (1, 3): note('drm', 9, b0 + o, .1, 37, 92)            # side stick
    elif b0 == end_beat:
        note('drm', 9, b0, .1, 36, 100)
# accents on cuts: crash (49) on major cuts, splash/ride bell otherwise
for i, c in enumerate(CUTS):
    note('drm', 9, sec2beat(c), .5, 49 if i in (0, 5, 7) else 53, 70 if i in (0, 5, 7) else 64)
note('drm', 9, 0, .5, 49, 66)

for name, ev in events.items():
    tr = mido.MidiTrack(); mid.tracks.append(tr)
    ev.sort(key=lambda x: (x[0], 0 if x[1].type != 'note_on' else 1))
    last = 0
    for t, msg in ev:
        tr.append(msg.copy(time=t - last)); last = t
tempo = mido.MidiTrack(); tempo.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(BPM), time=0)); mid.tracks.insert(0, tempo)
os.makedirs(OUT, exist_ok=True)
mid.save(f"{OUT}/music.mid")

# render each instrument group separately for mixing (mute others via separate MIDI files)
def render(keep, wav):
    m2 = mido.MidiFile(ticks_per_beat=TPB); m2.tracks.append(tempo)
    for name, tr in zip(events.keys(), mid.tracks[1:]):
        if name in keep: m2.tracks.append(tr)
    m2.save(f"{OUT}/tmp.mid")
    subprocess.run(["fluidsynth", "-ni", "-g", "0.6", "-r", "48000", "-R", "0", "-C", "0", "-F", wav, SF, f"{OUT}/tmp.mid"], check=True, capture_output=True)
    sr, x = wavfile.read(wav); x = x.astype(np.float64) / 32768.0
    n = int(48000 * (DUR + .2)); x = np.pad(x, ((0, max(0, n - len(x))), (0, 0)))[:n]
    return x
SR = 48000
drm = render({'drm'}, f"{OUT}/drm.wav"); bas = render({'bas'}, f"{OUT}/bas.wav")
mel = render({'mar', 'piz'}, f"{OUT}/mel.wav"); rho = render({'rho'}, f"{OUT}/rho.wav")
# kick-keyed ducking envelope for rhodes + melody (gentle sidechain)
env = np.ones(len(drm))
for bar in range(BARS):
    for o in (0, 2):
        s = int((bar * 4 + o) * 0.5 * SR)
        L = int(.22 * SR)
        if s < len(env): env[s:s + L] = np.minimum(env[s:s + L], 1 - .35 * np.exp(-np.linspace(0, 5, len(env[s:s + L]))))
rho *= env[:, None]; mel *= (0.5 + 0.5 * env)[:, None]
# EQ: high-pass melody/rhodes at 180 Hz, low-pass bass at 2.5 kHz, gentle air shelf on drums
hp = butter(2, 180, 'hp', fs=SR, output='sos'); lp = butter(2, 2500, 'lp', fs=SR, output='sos')
mel = sosfilt(hp, mel, axis=0); rho = sosfilt(hp, rho, axis=0); bas = sosfilt(lp, bas, axis=0)
mix = 1.0 * drm + 1.05 * bas + 0.95 * mel + 0.8 * rho
# room reverb send (synthetic stereo IR, 1.1 s decay, pre-delay 18 ms), on melody + rhodes only
rng = np.random.default_rng(23)
L = int(1.1 * SR); t = np.arange(L) / SR
ir = rng.standard_normal((L, 2)) * np.exp(-t * 5.5)[:, None]; ir[:int(.018 * SR)] = 0
ir = sosfilt(butter(2, [300, 6000], 'bp', fs=SR, output='sos'), ir, axis=0); ir /= np.abs(ir).sum(0).max() / 6
wet = np.stack([fftconvolve((mel + rho)[:, c], ir[:, c])[:len(mix)] for c in range(2)], 1)
mix = mix + 0.18 * wet
# soft bus compression (simple RMS follower)
rms = np.sqrt(np.convolve((mix ** 2).mean(1), np.ones(960) / 960, 'same')) + 1e-9
g = np.minimum(1, (rms / 0.12) ** (-0.35)); g = np.where(rms > 0.12, g, 1)
mix *= g[:, None]
mix = mix[:int(DUR * SR)]
fi, fo = int(.01 * SR), int(.8 * SR)
mix[:fi] *= np.linspace(0, 1, fi)[:, None]; mix[-fo:] *= (np.cos(np.linspace(0, np.pi, fo)) * .5 + .5)[:, None]
meter = pyln.Meter(SR); lufs = meter.integrated_loudness(mix)
mix = pyln.normalize.loudness(mix, lufs, -14.0)
# true-peak safety: 4x oversampled peak, soft-limit to -1 dBFS
from scipy.signal import resample_poly
tp = np.abs(resample_poly(mix, 4, 1, axis=0)).max()
lim = 10 ** (-1.2 / 20)
if tp > lim:
    mix = np.tanh(mix / lim * 0.9) * lim / np.tanh(0.9) if False else mix
    over = np.abs(mix) > lim * .85
    k = lim * .85
    mix = np.where(over, np.sign(mix) * (k + (lim - k) * np.tanh((np.abs(mix) - k) / (lim - k))), mix)
lufs2 = meter.integrated_loudness(mix); tp2 = 20 * np.log10(np.abs(resample_poly(mix, 4, 1, axis=0)).max())
print(f"LUFS {lufs2:.1f}  truepeak {tp2:.1f} dBFS  first {np.abs(mix[0]).max():.4f} last {np.abs(mix[-1]).max():.4f}")
wavfile.write(f"{OUT}/music.wav", SR, (mix * 32767).astype(np.int16))
