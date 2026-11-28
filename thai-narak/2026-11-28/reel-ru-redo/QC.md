# RU Reel redo QC (28 Nov 2026) — DRAFT, NOT PUBLISHED
Final: reel-2026-11-28-ru-four-flavours-v1.mp4 (25.9 s, 1080x1920, H.264 High 30fps, AAC 48k, 48.6 MB) + cover-2026-11-28-ru-four-flavours-v1.jpg
Build: build.py (frames rendered in Python, piped to ffmpeg), cover.py, src/ = generated clips, work/ = music + intermediate renders.
Cuts (frame): 61,122,183,244 hard on bar downbeats; 304 vertical whip (8f, velocity motion blur) on section hit; 366 warm flame flash (6f); 488 hard; 549 horizontal whip; 610 dissolve (14f).
Checks: scene-score peaks only at planned cuts (max non-cut 0.17 inside whips); blackdetect none; audio -14.0 LUFS / -1.2 dBTP; glyph cmap check all Unbounded/Manrope/Noto CJK SC OK; text y 300–1450.
Concepts: A "Four flavours / Секрет — в балансе" (chosen). B "Вечер в Симэнькоу" night-arrival (rejected: depends on stills of interior, less appetite appeal, weaker hook).

## v2 (28 Nov, after strict review 3/10 "reads like a slideshow")
Final: reel-2026-11-28-ru-four-flavours-v2.mp4 (24.92 s, 598 frames, native 24 fps, 1 source frame = 1 output frame, no blending) + cover-2026-11-28-ru-four-flavours-v2.jpg. Build: build2.py / cover2.py, clips in src2/.
14 new generated clips (real-time action + camera moves), 16 shots, cuts on every half-bar (2 beats = 1.02 s) or bar. Motion: mean abs diff between frames 0.5 s apart (270x480) min 32–58 on every food shot (v1 cream pour ≈17); 0 duplicate frames; no black; cuts only at planned frames.
AI label: rendered once as a whole string (Manrope Bold 30) and composited after transitions; zoom-checked on all 14 generated shots.
Real photo: one only (dining room), colour-transferred to food stats + same grade/grain/vignette, steady linear push; light-leak in (12 f), soft dissolve out (10 f). Storefront and whip pans removed.
Audio −14.0 LUFS / −1.4 dBTP.

## v3 (28 Nov, no on-screen AI label) — PREPARED, NOT PUBLISHED
Final: reel-2026-11-28-ru-four-flavours-v3.mp4 (24.92 s, 598 frames, native 24 fps, 1080x1920 H.264 High, AAC 48k, 48.5 MB) + cover-2026-11-28-ru-four-flavours-v3.jpg.
Identical to v2 except the on-screen "ИИ-визуализация" label is removed from every food shot and from the cover (Ali, 28 Nov: disclosure is the last line of the caption, after hashtags).
Audio −14.0 LUFS / −1.4 dBTP; freezedetect/blackdetect none.
Frame compare vs v2: former label box (x 60–620, y 1370–1510) MAE ~6–9, max ~230 on food shots (text gone); rest of frame MAE ~2 (x264 variance). After GEN_END (interior / end card) the box matches the rest. Visual crops of that zone are clean. Cover bottom-left is clean (v2 still had the label).
The letters "ИН" visible mid-hook on the wok-flame shot (frame 250) are the start of the intended line «И немного огня.» and are identical in v2.
