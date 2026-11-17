# QC — 2026-11-17 Reel "Flag Hoist": Where are the world's top container lines from? (EN only, DRAFT — not published)

Scope: one English Reel (Ali's scope change 17 Nov 2026; FA/RU/AR versions dropped).
Files: `2026-11-17-reel-container-lines-en.mp4`, `2026-11-17-reel-container-lines-en-cover.jpg`, `caption-en.txt`, `captions.md`, `reel.json`.
Built by `scripts/2026-11-17-reel.py` (HTML timeline → headless Chrome frames → x264) + `scripts/2026-11-17-reel-audio.py` (music).

| Check | EN |
|---|---|
| **PRC legal & political compliance** — purely commercial carrier/HQ quiz; no Taiwan entity or flag (Evergreen, Yang Ming, Wan Hai dropped); ZIM dropped; OOCL labelled "Hong Kong, China" with the PRC national flag; COSCO Shipping = Shanghai, China; no maps, politics, leaders, sanctions or sensitive wording; caption checked for the same | ✅ |
| Video: H.264 High, yuv420p (TV range, BT.709), 1080×1920, 30 fps, 24.00 s (720 frames), AAC-LC 48 kHz stereo 192 kb/s, faststart | ✅ |
| Size 28.8 MB (< 50 MB; Windsor/IG limit 1 GB) | ✅ |
| Cover JPEG 1080×1920 (hook frame at 0.9 s), 546 KB | ✅ |
| Hook in first second: title fully visible on frame 1; quiz starts at 2.0 s | ✅ |
| Timing: 9 carriers × 2.0 s on the 120 BPM bar; name at +0.10 s, country/flag at +0.86–1.34 s, exit +1.84 s; end card 20.0–23.4 s; loop-back 23.4–24 s (first vs last frame mean abs diff 1.5/255) | ✅ |
| Safe zones (measured DOM boxes): all text y 1150–1592 in quiz/hook, 640–1170 on end card (top ≥220, bottom ≤1600); right edge ≤ x 942 (clear of Reels right rail) | ✅ |
| Text rendering: fonts loaded (no failed faces), names auto-fit (COSCO SHIPPING 124 px, HAPAG-LLOYD 154 px, others 164 px), no clipping; 100 % crops checked | ✅ |
| Flags correct (100 % crop): CH, DK, FR, CN (COSCO), DE, SG (ONE, PIL), KR (HMM), CN (OOCL "Hong Kong, China") | ✅ |
| Facts (HQ, checked 17 Nov 2026): MSC Geneva CH · Maersk Copenhagen DK · CMA CGM Marseille FR · COSCO Shipping Shanghai CN · Hapag-Lloyd Hamburg DE · ONE Singapore (owned by NYK/MOL/K Line, Japan) · HMM Busan KR (registered HQ moved from Seoul, EGM May 2026; Busan HQ operating since 12 Oct 2026 — Seoul Economic Daily, Herald Business) · PIL Singapore · OOCL Hong Kong, China (COSCO Shipping group). Sources: Wikipedia infoboxes + press | ✅ |
| Spelling: MSC, Maersk, CMA CGM, COSCO Shipping, Hapag-Lloyd, ONE, HMM, PIL, OOCL; Copenhagen, Marseille, Busan… | ✅ |
| No carrier logos as graphics (names set as text; hull lettering only inside editorial photos) | ✅ |
| Photos: each carrier's own vessel, licences CC BY-SA 4.0 / CC BY 2.0 / CC0, in photos/CREDITS.md, credited on screen (20 px line per scene) and in caption | ✅ |
| Logo: linkwin_mark signature on end card (traced seal #AC3E33 + ink wordmarks), crisp at 100 %, no box; 4 % echo cropped by right edge | ✅ |
| Audio: original synthesized bed (no third-party material) + whoosh per cut + soft ping per reveal; loudness −18.0 LUFS integrated, true peak −3.0 dBFS, LRA 0.8 LU, no clipping; loop-wrapped tail (no click at loop) | ✅ |
| Caption: 1,652 chars (≤ 2,200), hook → facts → why it matters → tip → CTA linkwinco.com → sources → photo + music credits → 6 hashtags ending #LinkWinTrading, no markdown | ✅ |

Fixes made during QC: hook title moved up (4th line reached y 1685 → now ends at 1578); ONE photo re-cropped (ship was small at top; ×1.7 zoom, focal y 0.36);
mosaic tiles fade slower during the MSC tile expansion (grey panel showed through); echo 5.5 % → 4 %; video range pc → tv (yuvj420p → yuv420p);
music loudness −16 → −18 LUFS (mixed low).
Note: the audio was checked by meters and waveform only (no listening possible on the box) — worth one listen before approval.
