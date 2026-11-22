# QC — 2026-11-22 (unattended run, Grok Bot)

## Carousel "Crane Column" — China opens two new trade-deal talks in one day (order RU → AR → FA → EN; first ≠ EN of 21 Nov)
- [x] Facts vs sources fetched 22 Nov: MOFCOM press office 20 Nov 2026 16:17 (China–Singapore MoU to launch FTA 4.0 upgrade negotiations; built on China–ASEAN FTA, RCEP, China–Singapore FTA + upgrade protocol; government procurement and digital-related trade rules; FTA signed Oct 2008, upgraded Nov 2018 and Dec 2023); MOFCOM 20 Nov 2026 16:16 (China–Indonesia MoU to launch CEPA negotiations on the basis of China–ASEAN FTA and RCEP, wider coverage and higher level); Media Indonesia/Antara 12 Nov 2026 (Indonesia targets completion in early 2029). Tip line (ACFTA/RCEP preferences with certificate of origin) is general, uncontroversial practice. Source line on every slide and in caption.
- [x] Dates: 22 Nov 2026 = 1 Azar 1405 (FA mast); 20 Nov = 29 Aban 1405; 12 Nov = 21 Aban 1405; RU dd.mm.yyyy.
- [x] Language: RU/AR/FA/EN written natively; FA Persian digits + ZWNJ (موافقت‌نامهٔ، آسه‌آن، توافق‌های); AR Western digits in <bdi>; RU no-break space in "Китай — АСЕАН".
- [x] RTL: FA/AR dir=rtl, right-aligned, photo column + signature mirrored, letters joined (100 % crop of FA plates checked), Latin tokens (4.0, CEPA, RCEP, Media Indonesia/Antara) isolated, no letter-spacing on Arabic script.
- [x] Rendering: tools/render.py OK on all 4 (no overflow/clipping, fonts and image loaded). First draft had CEPA token touching text + broken bidi in FA source line: fixed (token 80 px in 212 px cell; sources on separate lines). All 4 re-inspected.
- [x] Logo: linkwin_mark signature (seal red + crane-green wordmarks) at the footer end of the text column, 4.5 % green echo cropped behind the lower column; no box/tab; crisp at 100 %.
- [x] Design differs from 21 Nov (mid gunmetal, Playfair, masthead signature, specimen cut-out) and 20 Nov (mist photo band, Space Grotesk): light porcelain sand, vertical photo-column split, Cormorant Garamond / Noto Kufi Arabic, footer-end signature.
- [x] Photo: Pasir Panjang Container Terminal, Singapore · Jacklee · CC BY-SA 3.0 (Wikimedia Commons), photos/CREDITS.md; credited on slides + caption. Not used in the last 21 days.
- [x] Files: 4 × JPEG 1080×1350, 255–292 KB (< 8 MB).
- [x] Caption: 2,046 chars (≤ 2,200); sections RU 468 / AR 454 / FA 449 / EN 450 in slide order; 5 hashtags ending #LinkWinTrading; linkwinco.com included.
- [x] PRC compliance RU: neutral, positive commercial news from MOFCOM; no politics, leaders, sovereignty, sanctions/trade-war framing; no flags or maps. PASS
- [x] PRC compliance AR: same content, neutral; no religious/political references. PASS
- [x] PRC compliance FA: same content, neutral commercial wording. PASS
- [x] PRC compliance EN: same content, neutral; no leaders named, no hostile framing. PASS
- [x] Image compliance: port cranes photo only, no flags, no maps, no people.

## Reel "Blueprint Box" — 20ft, 40ft or 40ft High Cube? Key numbers (EN, 24.0 s)
- [x] Facts vs Hapag-Lloyd container spec pages (20' / 40' / 40' HC Standard, fetched 22 Nov): inside L 5,900 / 12,032 / 12,032 mm; W 2,352 / 2,352 / 2,350; H 2,395 / 2,395 / 2,700; capacity 33.2 / 67.7 / 76.3 m³; tare 2,350 / 3,750 / 3,900 kg; max gross 30,480 / 32,500 / 32,500 kg; max payload 28,130 / 28,750 / 28,600 kg. Labels truncated to 2 decimals (2.39 m, 12.03 m); bar values rounded to 0.1 t. "Typical values; boxes vary by manufacturer" on end card + caption.
- [x] Frames inspected at 0, 0.5, 1, 3, 4.5, 6.5, 8.2, 10, 13, 16, 17.6, 19, 20, 21, 22.5, 23.9 s + 100 % crops (20' drawing + counters, end-card logo): hook text on frame 0, smooth box draw/morph, ghost outline, counters land on exact values, no clipping.
- [x] Safe zones: text y 300–1590; text x ≤ 952 (height label moved inside to x ≤ 947); top 220 / bottom 320 clear.
- [x] Photos: Yangshan Port · Reb42 · CC BY 3.0; Yangshan Port · Gmbsfd · CC BY-SA 4.0 (Wikimedia Commons), photos/CREDITS.md, credited on frame + caption.
- [x] Music: original synthesized score (scripts/2026-11-22-reel-audio.py), cyclic tail; −18.0 LUFS integrated, true peak −5.1 dBFS; loop sample jump 0.004 (no click); video fades to blueprint 23.55–24 s and hook photo fades in 0–0.35 s, so loop is blueprint→blueprint.
- [x] Files: reel H.264 yuv420p 1080×1920, 30 fps, 24.0 s, AAC 48 kHz, 4.7 MB, faststart; story re-encode H.264 yuv420p ~3.6 Mbps (5M target/6M max), AAC 44.1 kHz 128k, faststart (moov at byte 36), 10.9 MB; cover JPEG 1080×1920 (frame at 1.0 s).
- [x] Caption 1,073 chars, 6 hashtags ending #LinkWinTrading, linkwinco.com, source + photo + music credits.
- [x] PRC compliance (video + caption): neutral logistics education; Chinese port (Yangshan) shown positively; no maps, flags, politics, religion, people. PASS
