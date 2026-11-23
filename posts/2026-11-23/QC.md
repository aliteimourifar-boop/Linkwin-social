# QC — 2026-11-23 (scheduled run, Grok Bot)

## Carousel "Two-Way Board" — China–Europe trains now run full both ways (order FA → EN → AR → RU; first FA ≠ RU of 22 Nov)
- [x] Facts vs sources fetched 23 Nov: Xinhua 11 Nov 2026 (english.news.cn, NDRC official at press conference): Jan–Oct 2026 18,661 trains (+14.6% y/y), 1.865 million TEU (+11.2%); return 9,360 vs outbound 9,301; loaded-container ratio 100% for 50 consecutive months as of October; trans-Caspian line daily. Xinhua 20 Nov 2026: Wuhan's 500th China–Europe train of 2026 departed 20 Nov for Moscow. Tip (compare rail with sea/air quotes) is general advice. Source line on every slide and in caption.
- [x] Dates: 23 Nov 2026 = 2 Azar 1405 (FA mast); 11 Nov = 20 Aban 1405; 20 Nov = 29 Aban 1405; RU dd.mm.yyyy; AR Western digits.
- [x] Language: FA/EN/AR/RU written natively; FA Persian digits + ZWNJ (می‌کنند، شین‌هوا، ژنگ‌ژو، ویکی‌مدیا); RU no-break spaces in 9 301 / 18 661 / 14,6 %, grammar "18 661 поезд"; AR plus signs replaced with "بزيادة" to avoid bidi flips (first draft showed "11.2%+").
- [x] RTL: FA/AR dir=rtl, right-aligned, arrows mirrored (outbound points in reading direction), split-flap numbers isolated LTR, sources on separate lines (fixed a broken date wrap in AR).
- [x] Rendering: tools/render.py OK on all 4 (no overflow/clipping, fonts and image loaded); all 4 inspected. Photo credit moved from sky (low legibility) to footer; board echo seal removed (read as clutter).
- [x] Logo: linkwin_mark signature, tone-on-tone chalk seal + chalk wordmarks at the footer end next to linkwinco.com; no box/tab; crisp.
- [x] Design differs from 20–22 Nov: dark warm graphite (vs sand/gunmetal/mist), split-flap departure board archetype, Inter + IBM Plex Mono / Vazirmatn / IBM Plex Sans Arabic (no Cormorant/Playfair/Space Grotesk/Noto Kufi), signal mint + ice blue.
- [x] Photo: CR Express train near Putian, Zhengzhou · Windmemories · CC BY-SA 4.0 (Wikimedia Commons), photos/CREDITS.md; credited on slides + caption.
- [x] Files: 4 × JPEG 1080×1350, ~340–365 KB.
- [x] Caption: 2,102 chars (≤ 2,200); sections FA 461 / EN ~470 / AR 458 / RU 466 in slide order, language codes (no flags); 5 hashtags ending #LinkWinTrading; linkwinco.com.
- [x] PRC compliance FA: positive, neutral logistics news from Xinhua/NDRC; no politics, leaders, sovereignty, sanctions/trade-war framing. PASS
- [x] PRC compliance EN: same, neutral commercial wording. PASS
- [x] PRC compliance AR: same, no religious/political references. PASS
- [x] PRC compliance RU: same, neutral. PASS
- [x] Image compliance: Chinese CR Express train in Zhengzhou, no maps, no flags, no identifiable people.

## Reel "Swiss Kinetic" — Can you read this code? 7202.41, decoded (EN, 23.0 s)
- [x] Facts vs WCO "What is the Harmonized System (HS)?" (fetched 23 Nov): >5,000 commodity groups, six-digit code, >200 countries and economies, >98% of merchandise in international trade; WCO HS Nomenclature 2022 Chapter 72 PDF (fetched 23 Nov): 72 iron and steel; 72.02 ferro-alloys; 7202.11 FeMn >2% C; 7202.21 FeSi >55% Si; 7202.30 ferro-silico-manganese; 7202.41 FeCr >4% C. "Codes go national after six digits" is general customs practice (HS is the basis of national tariffs).
- [x] Frames inspected from the encoded mp4 at 0, 1, 4, 6.5, 9, 9.2 (100 %), 11.5, 12.5–12.9 (transition), 14.9, 15.2, 17.5, 19.6, 21.8, 21.9 (100 % end card + logo): hook text on frame 0, code complete by 0.7 s, no clipping; safe-zone check script: all text within y 250–1590, x 72–940.
- [x] Distinctness vs last 3 reels (20/21/22 Nov frames compared side by side): cobalt Swiss grid with oversized numerals vs darkroom/ivory/blueprint; Inter Tight + IBM Plex Mono vs Oswald/Manrope/Playfair/Space Grotesk; lime cursor, column shutter, circle polarity flip, barn-door, count-ups, typed line vs red-edged wipes/Ken Burns photo windows/line morph; 23 s vs 24 s; sample-based nu-jazz groove vs synthesized beds. End line rewritten ("Right code. Right duty.") after spotting it echoed 21 Nov's "Agree the term. Then the price.". PASS
- [x] Photos: Ferrosilicon / Ferrochrome · FocalPoint · CC BY-SA 4.0 (Wikimedia Commons), duotone (noted as modified), photos/CREDITS.md, credited on frame + caption. Real photos, no AI imagery.
- [x] Music: original, sample-based (FluidSynth + FluidR3_GM SoundFont, MIT), marimba / pizzicato / finger bass / Rhodes / kit, 120 BPM, cuts on beats; −14.0 LUFS integrated, true peak −1.0 dBFS; 10 ms fade-in, 0.8 s fade-out to silence; video fades to plain cobalt 22.4–23 s and opens on cobalt, so the loop has no jump/click. No Content ID risk (no third-party recordings).
- [x] Files: reel H.264 yuv420p 1080×1920, 30 fps, 23.0 s, AAC 48 kHz 192k, ~3.9 MB, faststart; story re-encode H.264 yuv420p (5M target/6M max), AAC 44.1 kHz 128k, faststart, ~8.2 MB; cover JPEG 1080×1920 (frame 1.1 s).
- [x] Caption ~1,030 chars, 6 hashtags ending #LinkWinTrading, linkwinco.com, source + photo + music credits.
- [x] PRC compliance (video + caption): neutral customs-classification education; no maps, flags, politics, religion, people. PASS
