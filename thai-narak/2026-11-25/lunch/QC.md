# QC · Thai Narak Story 2026-11-25 LUNCH
File: story-2026-11-25-lunch.jpg (1080x1920 JPEG, q94) · script lunch.py
Art direction: 1 Daylight Editorial — "botanical plate" still life: real lemongrass + root props from the top-left of
S/owner-photos/food-garlic-bread.png (source crop x0–1150, y0–1150 of 3000x2250; bread + newspaper excluded/inpainted
away and dissolved into the page), dark stone re-toned (screen + white balance) to warm cream-sand so the props sit
on the same sand page they dissolve into; props bleed off top/left edges, upper-left two-thirds; centred bottom-heavy
type stack. No boxes, borders or collage. No AI imagery.
Text (3 groups): "Lemongrass:" (Cormorant Garamond Light, #3A2A1E) / "bruise, don’t chop." (Cormorant italic, gold foil)
· 香茅先拍裂，香气才出来 (Noto Serif CJK SC) · LUNCH 11:00–15:00 午市 (Montserrat 500 tracked + Noto Sans CJK).
Logo: traced `word` lockup, gold foil, 50 px, centred under the stack (signature).
Text bboxes (y): h1 1149–1250, h2 1267–1368, cn 1389–1434, hours 1486–1507, logo 1518–1569 → all within 250–1570 (asserted).
PRC: no politics/maps/flags/national or govt symbols/religion/royalty/dates/news/superlatives. OK.
Facts: general Thai cooking tip (bruising lemongrass releases aroma), not a recipe/house claim; lunch 11:00–15:00. No prices, emoji, dishes, awards. OK.
CJK: cmap check all glyphs present; visual crop read, no tofu. OK.
Self-critique: differs from last 3 (11-24 lunch full-bleed + lower-right stack; 11-24 dinner shopfront/wood route line;
11-23 dinner chili-red poll) and from 11-23 lunch linen page (left headline top / photo off right). Revision 1: page
colour was peach → white-balanced to cream-sand; straight apostrophe → ’; highlight shoulder for roots.
Notes: root highlights slightly soft/bright after re-tone; small soft inpainted area right of the upper root (reads as dissolve).

## v2 (CD revision) · story-2026-11-25-lunch-v2.jpg (1080x1920 JPEG q94) · lunch.py now renders v2
Why: v1 rejected (root hero vs "Lemongrass" headline; blown root highlights; inpaint smudge; 50px logo; dead bottom).
Photo: ONLY green lemongrass blades from top-left of S/owner-photos/food-garlic-bread.png (src x0–1600, y0–420; HSV green
key + leaf-highlight fill, guard polygon well above roots, area filter). Zero root / newspaper pixels. Tiny stone slivers
between overlapping blades re-filled from neighbouring leaf colour (Telea), 1.2px feathered edge -> no dark stone halo.
Lightly brightened (x1.22+14), natural colour, soft warm drop shadow.
Composition: cream-sand page #EFE6D6 with subtle paper tooth; main blade sweep diagonally across upper third (photo's own
crop edge on canvas top, bundle runs off top/right, tips toward left); smaller 180° counter-sweep off the bottom-right edge;
type is the hero, centred mid-frame. Differs from 11-23 lunch (linen, off-right print, left top headline) and from v1.
Text: "Lemongrass:" Cormorant Garamond Light 168px #3A2A1E · "bruise, don’t chop." Cormorant italic 140px gold foil ·
香茅先拍裂，香气才出来 Noto Serif CJK SC 54px · gold hairline · LUNCH 11:00–15:00 午市 Montserrat 500 26px tracked + Noto Sans CJK.
Logo: traced `word` lockup, gold foil, 92px tall (169x92, proportional), centred under the stack.
Text bboxes (y): h1 776–927, h2 933–1074, cn 1111–1169, hours 1237–1262, logo 1390–1482 -> all within 250–1570 (asserted).
CJK: Noto CJK glyphs, visual crop read, no tofu. No boxes/borders/collage, no black. AI imagery: none.

## v3 (2026-11-25 touch-up) — blade notches
- CD note: jagged rectangular cream notches along blades (stone between overlapping blades keyed out).
- Fix: 71px elliptical closing + hole fill of bundle silhouette (within guard polygon); sealed seams filled with
  adjacent-blade leaf colour (normalised convolution from eroded blade interiors) darkened 8–28% as inter-blade shadow,
  2.5px feathered blend; outer alpha feather 1.6px. Type, layout, colours, logo unchanged (rows 500–1500 identical to v2 within JPEG noise).
- Checked full frame + top/bottom close-ups: no notches, no dark stone halo. Output story-2026-11-25-lunch-v3.jpg 1080x1920.
