# QC: Thai Narak Story, DINNER slot, Wed 2026-11-18 (Asia/Shanghai)
File: story-2026-11-18-dinner.jpg, made by dinner.py (`/workspace/tn-venv/bin/python dinner.py story-2026-11-18-dinner.jpg`)

## Concept
Weekly plan Wed 18, slot 2: #1 Signature Grilled Pork Neck 招牌炭烧猪颈肉, macro char close-up, "Dinner is open" angle.
Layout: **split-axis editorial**. The headline group sits top-left, a full-width macro of the charred slices fills the centre, and the hours line (bottom-right) plus a gold-foil signature (bottom-left) share one baseline row.
- Differs from today's lunch Story, which was centred with the label, headline, dish and hours all stacked on the centre axis.
- Differs from yesterday's evening Story, which had the neon-sign photo at the top and all text bottom-left.
- Differs from yesterday's Reel, which used the whole portrait shot (galangal, sauce bowl and orchid). This frame is a tight 315×286 px source crop of the slices only: no sauce bowl, orchid or galangal, and the tray is mostly burned out.

## Exact text on image
1. SIGNATURE GRILLED PORK NECK (Montserrat 500, tracked, gold)
2. Dinner is / *open.* (Cormorant Garamond Light 300 roman; Regular 400 italic, gold)
3. 招牌炭烧猪颈肉 (Noto Serif CJK SC)
4. DINNER  17:00–22:00 (Montserrat 500, tracked, cream)
5. 晚市 17:00–22:00 (Noto Serif CJK SC, muted cream)
6. Logo signature: traced official `word` lockup (THAI NARAK + flower + THAI RESTAURANT) in gold foil, 58 px tall, uniform scale only

## Facts
- The dish name matches the verified menu item 9: Signature Grilled Pork Neck / 招牌炭烧猪颈肉 (brand-kit.md).
- Dinner hours are 17:00–22:00. 10:00 does not appear anywhere.
- The image states no price, ingredient, award or claim.

## PRC compliance
- PASS. Nothing political. No maps, flags or national symbols. No religious or royal imagery (the orchid and dancer are not in frame).
- PASS. No superlatives (最好/第一/best/No.1 etc.).
- PASS. No AI imagery: it is the real dish photo only.

## Asset
`assets/food/signature-grilled-pork-neck_portrait_453x536.jpg` (= thainarak.com menu-dish3.jpg, md5 d6149785…). It is the only real photo of this dish.
- Crop box (8,214,323,500), uniform scale ×3.43 to 1080×981, placed at y 580–1561. No stretch.

## Grade and retouch
- Hue mask burns the bamboo tray and pineapple by 55%. The pale stone is burned by 55%. The banana leaf is pulled to deep olive.
- Radial macro falloff, with shallow depth of field: sharp band through the slices, Gaussian 7 px toward the top and bottom.
- grade(): exposure 0.82, contrast 0.42, saturation 0.92, warm 1.7, lift 6.
- Ember lift on the char highlights, plus a saturation boost on the meat.
- Warm ember glow in the charcoal ground (#131215). Smoothstep feather on all four sides, so there is no hard edge. Vignette, grain 5.5.

## Design-system checks
- One hero, three text groups (headline group, hours, signature).
- No boxes, borders or collage. The logo is integrated as gold foil, not a pasted square.
- Palette: gold #DEB150, cream #F0E6D4, muted #C8BCA8. No pure white.
- Thumbnail at 216×384: the headline and the slices read clearly.
- Self-critique, round 1 (v1): the tray was too bright and yellow, and the crop read like the Reel.
- Self-critique, round 2 (v2–v4): an RGB tray mask failed. The HSV mask then left the garlic topping olive, so I added a component-size filter. The meat was pale pink, so I warmed and saturated it.
- Self-critique, round 3 (v5–v6): moved to a tighter macro crop and lengthened the bottom feather, so the bottom no longer looks like an oval cut-out.
- Known limit: the source is 453×536, so at 1:1 the slices look soft. Grain and the depth-of-field band hide this at phone size. A new high-resolution photo of this dish from Ali would help future posts.

## CJK render
- fontTools cmap check (NotoSerifCJK-Regular.ttc index 2) on 招牌炭烧猪颈肉晚市17:00–22:00: all glyphs present.
- Visual crops of the top group and the bottom row show no tofu boxes.

## Specs and text y-range
- 1080×1920 JPEG, RGB, quality 94, 4:4:4, 9:16.
- Text bounding boxes (asserted in script, 250 ≤ y ≤ 1570):

| Element | Box (x0, y0, x1, y1) |
|---|---|
| label | 96,306–588,322 |
| h1 | 91,378–495,449 |
| h2 | 91,503–294,588 |
| cn | 96,599–362,638 |
| hours | 654,1494–984,1512 |
| cnhours | 749,1528–984,1558 |
| sig | 96,1499–204,1558 |

- Overall text y-range: 306–1558. The top 250 px and bottom 350 px (y > 1570) are clear.
