# QC — 2026-11-21 (unattended run, Grok Bot)

## Carousel "Specimen Readout" — Ferrochrome slips below cost, chrome ore holds (order EN → FA → RU → AR; first ≠ RU of 20 Nov)
- [x] Facts: every figure checked against SMM "Weak Demand Drags Ferrochrome Lower; Chrome Ore Prices Stabilize" (news.metal.com, 20 Nov 2026 17:14 GMT+8, fetched 21 Nov): HC FeCr Inner Mongolia 7,200–7,400 yuan/50-base t; East China 7,650–7,700, −125 w/w; below cost/negative margins; SA 40–42% fines Tianjin 49–49.5 yuan/mt-degree, +0.5; port stocks declined; miners' offers firm; Oct HC FeCr imports 150,000 t, +5.11% m/m; next tender expected −200 yuan. Source line on every slide and in caption.
- [x] Dates: 21 Nov 2026 = 30 Aban 1405 (FA), source date 20 Nov = 29 Aban 1405; RU dd.mm.yyyy.
- [x] Language: EN/FA/RU/AR written natively; FA Persian digits + ZWNJ (تمام‌شده، می‌فروشند، ارزان‌تر); AR Western digits in <bdi dir=ltr> (CSS isolate), "+" removed from AR 5.11% to avoid bidi ambiguity; RU no-break spaces in thousands.
- [x] RTL: FA/AR right-aligned, joined letters, mirrored layout (specimen and signature on the left), no letter-spacing on Arabic script.
- [x] Rendering: tools/render.py OK on all 4 (no overflow, no clipped text, fonts loaded, images loaded). Visually inspected all 4 + AR 100 % crop of panels.
- [x] Logo: linkwin_mark signature (silver seal tone-on-tone + chrome-white wordmarks) in the masthead, 3.5 % echo cropped at bottom start corner; no box/tab.
- [x] Design differs from 20 Nov (light mist photo band, Space Grotesk, footer signature): mid gunmetal, specimen cut-out, Playfair/Noto Naskh, masthead signature.
- [x] Photo: chromite with serpentine, Darla Sondrol, CC0 (Wikimedia Commons), background removed; recorded in photos/CREDITS.md; credited on slides + caption.
- [x] Files: 4 × JPEG 1080×1350, 0.33–0.38 MB (< 8 MB).
- [x] Caption: 1,899 chars (≤ 2,200); sections EN 434 / FA ~425 / RU ~443 / AR ~412 in slide order; text labels instead of flag emojis; 5 hashtags ending #LinkWinTrading; linkwinco.com included.
- [x] PRC compliance EN: commercial price report, neutral; "Inner Mongolia" as a Chinese producing region; no politics/maps/flags. PASS
- [x] PRC compliance FA: same content, neutral commercial wording; no flags/maps/politics. PASS
- [x] PRC compliance RU: same content, neutral; no sanctions/trade-war framing. PASS
- [x] PRC compliance AR: same content, neutral; no religious or political references. PASS
- [x] Image compliance: mineral specimen photo only, no map, no flag, no people.

## Reel "Route Ruler" — FOB vs CIF vs DDP (EN, 24.0 s)
- [x] Facts vs ICC Incoterms® 2020 (iccwbo.org, fetched 21 Nov): FOB delivery/risk on board at port of shipment, buyer pays main carriage; CIF seller pays carriage + minimum insurance (ICC (C) default) to destination port, risk passes on board at shipment; DDP seller delivers cleared for import, duties paid, ready for unloading (buyer unloads); FOB/CIF are sea rules, FCA/CIP for containers handed over at a terminal.
- [x] Frames inspected at 0, 1, 2.6, 4, 6.9, 8, 10.5, 12, 13, 16.5, 17.6, 19, 20.5, 22.5, 23.9 s + 100 % crops (CIF ruler, end-card logo): hook text on frame 0, smooth bar fills, risk pin drops, no clipping.
- [x] Safe zones: all text y 250–1583 and x ≤ 938 (top 220 / bottom 320 / right buttons clear).
- [x] Photos: existing Commons files (Yangshan · Bruno Corpet CC BY-SA 3.0; COSCO Shipping Himalayas · Hummelhummel CC BY-SA 4.0; Shennan East Road · Dinkun Chen CC BY-SA 4.0; Ningbo-Zhoushan · Nbfreeh CC BY-SA 4.0), credited on frame and in caption.
- [x] Music: original synthesized score (scripts/2026-11-21-reel-audio.py), cyclic tail; loudness ≈ −18 LUFS, true peak −5.5 dBFS; loop sample jump 0.02 (no click); video fades to ivory at 23.55–24 s.
- [x] Files: reel H.264 yuv420p 1080×1920, 30 fps, 24.0 s, AAC 48 kHz, 15.0 MB, faststart; story re-encode H.264 yuv420p ~4.1 Mbps (5M target), AAC 44.1 kHz 128k, faststart, 12.2 MB; cover JPEG 1080×1920.
- [x] Caption 1,286 chars, 6 hashtags ending #LinkWinTrading, linkwinco.com, source + photo + music credits.
- [x] PRC compliance (video + caption): neutral trade education; no maps, flags, politics, religion; Chinese ports shown positively. PASS
