# QC — Thai Narak Reel 2026-11-25 (Russian edition, Spice Market Colour) — NOT PUBLISHED
Files: reel-2026-11-25-ru-spice-market-v1.mp4, cover-2026-11-25-ru-spice-market-v1.jpg, story-teaser-2026-11-25-ru-spice-market-v1.jpg (build.py / cover.py / cutout.py in this folder)

## Concepts (critiqued)
- A "Thai, unexpected" (CHOSEN): three question hooks, one saturated field per dish (turmeric / chili / lemongrass), cut-out dish, on-beat snaps, colour-stripe wipes, cream end card. Strength: the Russian hook is a curiosity question, each dish is shown big and clean, the pacing is varied. Weakness: sources are small (365–900 px), so dishes are cut out at ≤1.2x snap zoom instead of full-bleed.
- B "Вкус Таиланда: from herbs to bowl" (REJECTED): ingredient still-lifes into plated dishes. No usable high-res ingredient photos, it would repeat the used-up 11-17..22 set, and the hook is generic.

## PRC check
No politics, maps, flags (the small "THAI NARAK" pick-flag on the Massaman is cropped out of the cut-out), national/government symbols, regions, religion, royalty, dates/news. No superlatives (no «лучший», «№1», «самый»), no nationality/language address. The only figure is the restaurant's own neon dancer logo (brand sign). No prices, deals or awards claimed.

## Facts
Address 荔湾区中山七路48号西门口广场137-1、139铺; Metro Line 1 Ximenkou, ~420 m; hours 11:00–15:00 и 17:00–22:00 (website 10:00 NOT used). Dish names from the website: Thai Durian Spring Rolls 泰式榴莲春卷; Massaman Curry Chicken 马沙曼咖喱面包鸡 (pastry bowl); Coconut Goji Shrimp Soup 椰奶枸杞虾汤. No ingredient/spice/price/recipe claims beyond names. Thai SELECT Classic is mentioned only in the caption.

## Russian language critique
- Hook «Дуриан… / в спринг-ролле?»: natural, a spoken-style question; «спринг-ролл» is the usual Russian term.
- «Карри — / в слоёной булочке?»: the photo shows a layered pastry, so «слоёная булочка» is accurate (more natural than «хлебная чаша»). Chose «булочке» over «пирожке» (a pirozhok is stuffed, not a vessel).
- «Годжи — / в кокосовом супе?»: «годжи» is indeclinable, the case after «в» is correct (prepositional: в супе).
- «Тайская кухня, / которая удивляет.»: warm, no superlative.
- «Заходите попробовать.»: warm, plain invitation. Dash and ёлочки used: «Симэнькоу». ё in «слоёной». Station name transliterated per Russian norm: 西门口 = Симэнькоу.
- Dish labels: «ТАЙСКИЕ СПРИНГ-РОЛЛЫ С ДУРИАНОМ», «КУРИЦА В КАРРИ МАССАМАН», «КОКОСОВЫЙ СУП С КРЕВЕТКАМИ И ГОДЖИ»: verified-name based, grammatical (instrumental after «с»).
- Chinese text kept to dish names, 蕉媚泰国餐厅 · 西门口, and the address on the end card.
- No machine-translation patterns; no addressing viewers by nationality.
- Limitation: reviewed as a copy-editor, not by a human native speaker; Ali/another native reader should give it a final skim.

## Design
Direction 3 Spice Market Colour (not in the last 3: Full-bleed Photo Hero, Rattan & Wood, Daylight Editorial). Fields #E3A21A / #C8341F / #B8C25A, cream end card #F4EDE1; NO charcoal/black base. Cormorant Garamond (roman + gold/chili italic emphasis), Montserrat caps labels, Noto Serif CJK SC. Logo: traced vector foil `full` on the end card (uniform scale only) plus tone-on-tone embossed `flower` ornament on every field and embossed `word` signature on cover/story. No collage, no PiP, no boxes. Grade: saturated, bright, warm. Cut-outs via GrabCut then colour-boosted; soft contact shadows. Goji top edge feathered (source crop cut the shrimp).
Transitions: curved colour-stripe wipes on bar lines (right, right, up, diagonal) — no crossfades.
Variety vs 11-17 reels (charcoal/gold, dissolves, seal): bright saturated per-dish fields, cream end card, upbeat nu-disco.

## Music
House 02 / Lily J (Mixkit Free License) — nudisco-house-123bpm-house-02.mp3, start 23.46 s (kick/downbeat located by low-band onset analysis; bar line at 23.476 s), clip 25.366 s, fade-out 2.5 s, via prep_music.sh. Measured on the final MP4: I = -13.8 LUFS, TP = -2.3 dBTP (LRA 0.7). First library use (previous reels used legacy synth, so no rotation conflict). Scene cuts every 1.951 s bar (3+3+3+2+2 bars). No voiceover (no verifiably native-quality Russian voice available).

## Glyphs
fontTools cmap check: all Cyrillic / digits / punctuation in Cormorant Garamond (roman+italic) and Montserrat, all hanzi in Noto Serif CJK SC: 0 missing. Visual crops of full-res frames and cover/story inspected: no tofu (a tofu caught in the Story first draft, Chinese set in Montserrat, was fixed by using the CJK font).

## Text safe zone
Reel text spans y≈262–1330 (interior scene up to ≈1430); cover key content centre 4:5 (y 285–1635); story text y≈268–1450.

## Frames inspected
Every 1 s (25 frames, 9×3 sheet), 8 wipe frames and full-res crops of the hook, label, end card, cut-outs, cover and story. Known cosmetic notes: slight notch on the durian plate rim (left) and on the Massaman's lower-right edge near the flowers; goji top fade; source photos small, upscaled ≤1.9x (soft at 100%).

## Specs (ffprobe)
H.264 High, yuv420p, 1080x1920, 30 fps, faststart, ~2.9 Mb/s; AAC-LC 48 kHz stereo ~277 kb/s; duration 25.37 s (video 25.30 s), 10.1 MB; cover JPG 1080x1920; story JPG 1080x1920.
