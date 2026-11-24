# QC — 2026-11-24 (scheduled run, Grok Bot)

## Carousel "Print Registration" — China Single Window prints customs forms pre-stamped (order EN → AR → FA → RU; first EN ≠ FA of 23 Nov)
- [x] Facts vs sources fetched 24 Nov 2026: China E-Port Data Center notice 11 Nov 2026 (singlewindow.hn.cn; Anhui Single Window via 10100.com): one-click print gains "affix customs declaration seal" option from 20:00 11 Nov; covers check sheet, inspection/release notice, import goods permitted-removal notice, paperless release notice, agency declaration agreement; pilot Qingdao + Hangzhou districts. Notice 23 Nov 2026 (The Paper; Fujian Single Window fjdport.gov.cn): from 20:00 23 Nov adds Beijing, Tianjin, Dalian, Shanghai, Nanjing, Ningbo, Xiamen, Jinan, Guangzhou, Shenzhen, Huangpu (11) → 13 districts. Hebei E-Port operation guide: seal created with legal-representative card, bound to operator card; replaces print → manual stamp → scan; only documents where the logged-in company is the declaring unit. All on-image numbers (13, 2, 11, dates) match.
- [x] Dates: 24 Nov 2026 = 3 Azar 1405 (FA mast); 11 Nov = 20 Aban 1405; 23 Nov = 2 Azar 1405; RU dd.mm.yyyy; AR Western digits.
- [x] Language: EN/AR/FA/RU written natively; FA Persian digits + ZWNJ (برگه‌های، می‌شوند، یک‌بار، اطلاعیه‌های، می‌نشیند); RU «ёлочки» quotes, Cyrillic in Unbounded/Golos (fonts loaded); AR digits isolated in <bdi>.
- [x] RTL: FA/AR dir=rtl, right-aligned, process arrow points left (reading direction), chips grid flows right-to-left, legend and footer mirrored; strikethrough legible on Arabic script.
- [x] Rendering: tools/render.py OK on all 4 (no overflow/clipping, fonts loaded); all 4 inspected + FA 100 % crop of footer/tip.
- [x] Logo: linkwin_mark signature (seal red + black wordmarks) at footer end with linkwinco.com; 3 % echo behind right edge of chip grid, no box/tab; crisp.
- [x] Design differs from 21–23 Nov: light press-white (vs graphite/sand/gunmetal), new archetype (crop-mark proof page + struck process row + numeral + chip index), new type Unbounded + Golos Text / Noto Kufi + Vazirmatn (FA) / Noto Naskh + IBM Plex Sans Arabic (AR), process cyan palette; no photo (graphic).
- [x] Files: 4 × JPEG 1080×1350, 160–210 KB.
- [x] Caption: see count below (≤ 2,200); sections EN/AR/FA/RU in slide order (~430–480 each), language codes (no flags), 5 hashtags ending #LinkWinTrading, linkwinco.com.
- [x] PRC compliance EN: official China E-Port Data Center trade-facilitation notice, positive and neutral; no politics, leaders, sovereignty, sanctions or trade-war framing; no maps/flags. PASS
- [x] PRC compliance AR: same content, neutral; "الصين" only in commercial context. PASS
- [x] PRC compliance FA: same content, neutral; no politics. PASS
- [x] PRC compliance RU: same content, neutral; no politics. PASS
- [x] Not self-promotion; topic new vs posted-log (customs digitalisation; recent: trains, deal talks, ferrochrome, ports).

## Reel "Glass Ledger" — Letter of credit, in 5 steps (EN, 26.7 s)
- [x] Facts: ICC UCP 600 (library.iccwbo.org rules text + UCP 600 PDF, fetched 24 Nov 2026): Art. 5 "Banks deal with documents and not with goods…"; Art. 14(b) max five banking days following presentation, per bank; Art. 14(c) original transport documents presented not later than 21 calendar days after shipment, and not later than expiry (worded "by default within 21 days of shipment"). Steps 1/2/5 are the standard documentary-credit flow; tip (inspection certificate as a required document) is general practice, worded as advice.
- [x] Distinctness vs last 7 (17–23 Nov): art direction glassmorphism depth over defocused night cityscapes (new); layout centred glass cards + 2×2 tilted 3D flow stage (new); palette night #070B14 / emerald #3FE0B0 / violet #8C7BFF / frost #F4F6FB (new); fonts Syne + DM Sans (new); animation damped springs in z-depth, per-word focus pull, stroke-draw glowing paths with glass tokens, orbiting 3D camera, countdown ring, light sweeps (new); transitions zoom-through, rack focus, camera orbit, iris, venetian blinds, pull-back (new); music neo-classical cinematic, piano/strings/cello/celesta/timpani, 90 BPM, D minor (vs nu-jazz 120 BPM and synth beds); length 26.7 s, 10 bars (vs 23–24 s).
- [x] Music: original, sample-based (FluidSynth + FluidR3_GM, MIT); no third-party recording → no Content-ID risk. Cuts on bar lines (every 2.667 s).
- [x] Frames: 12 frames extracted across every scene (hook, zoom-through, title, steps 1–5 incl. countdown ring, iris into twist, blinds into tip, end card) and compared with the 21/22/23 Nov reels (ivory route ruler, blueprint line box, cobalt Swiss kinetic): reads as a different film, not a variation. First render: step lines resolved too late (~1 s) and twist/tip backgrounds looked flat → re-timed word reveals (done by ~0.7 s into each bar) and lifted the Zhujiang photo (less blur, brighter); re-rendered.
- [x] Text rendering: Syne/DM Sans loaded (no font errors); no clipping (twist headline reduced to 88 px after the first preview clipped "documents."); safe zones checked by script: all text y 250–1600, x 72–940 except intentional transient motion (zoom-through, tip slide-in).
- [x] Logo: linkwin_mark signature tone-on-tone frost white on the end-card glass next to linkwinco.com; crisp at 100 % crop; no badge/box.
- [x] Audio: −14.0 LUFS integrated, true peak −2.1 dBFS, no clipping; 10 ms fade-in, 1.2 s cosine fade-out, first/last samples 0 → no click at loop; visuals fade the end card to the night background in the last 0.5 s.
- [x] Files: reel MP4 H.264 High yuv420p 1080×1920 30 fps (rendered 60 fps, 2-frame blend motion blur), AAC 48 kHz, 26.67 s, 9.0 MB, +faststart; story MP4 H.264 yuv420p ~5 Mbps, AAC 44.1 kHz 128 kbps, +faststart, 16.4 MB; cover JPEG 1080×1920 (hook frame).
- [x] Caption EN 1,108 chars; facts match UCP 600; credits for photos and music; 5 hashtags ending #LinkWinTrading; linkwinco.com.
- [x] PRC compliance EN (reel): neutral ICC trade-finance education; Chinese city photos (Pudong, Zhujiang New Town) without people, politics, maps or flags. PASS

## Publishing
- Raw URLs pinned to commit SHAs (raw.githubusercontent.com branch URL served a stale RU slide for >5 min after a wording fix; SHA URLs verified 200 + byte-identical to local files before each call).
- Carousel 18127525240711350 · Reel 17917494858501425 · Story (video) 18136239892707498
