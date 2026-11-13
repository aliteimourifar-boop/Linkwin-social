# LinkWin Instagram — Daily Playbook

This file is the standing brief for the daily LinkWin Instagram run. Follow it every day.
Owner: Ali Teimourifar, Founder & CEO, LinkWin Trading (Hong Kong HQ + Guangzhou). Account: **@linkwinco**.

## Goal
Make @linkwinco look like a knowledgeable, trustworthy, internationally connected trading partner.
People should follow because every post teaches them something useful (trade news, market intelligence,
practical how-tos), and then think "LinkWin could help me with this". Informative and commercially relevant,
subtly persuasive, never pushy advertising.

The visual presentation must be exceptional. **Work as the Creative Director and Senior Designer of a premium
international agency. Every day is a new creative project, not yesterday's template with new text.**
(Ali's standing instruction of 8 Nov 2026. It is permanent and applies to every run and all four languages.)

## What to publish each day
Per day: **4 feed posts + 4 Stories**, one each in **English, Persian (Farsi), Russian, Arabic**, in that order.
- Feed: 1080×1350 JPEG (4:5). Story: 1080×1920 JPEG (9:16). Keep text and logo out of the top 200 px and bottom 250 px of Stories.
- Each language is a fully adapted version (headline, on-image text, caption, CTA), not a word-for-word translation.
  Persian especially must read naturally, like a native business writer. Persian uses Persian digits (۰–۹) and Solar Hijri dates;
  Arabic uses Western digits and correct number–noun agreement; Russian uses a narrow space as the thousands separator.

## Topic selection (research first, every day)
Rotate across: global trade news · import/export opportunities · sourcing & supply chain · shipping/freight/logistics ·
commodity prices · **ferroalloys, metals, minerals** (LinkWin's flagship line) · customs rules, tariffs, trade agreements ·
China manufacturing · emerging markets · practical how-to guides (Hong Kong & Guangzhou business, payments, inspections, Incoterms…).
- Use credible sources: government/official sites, international organisations, Xinhua/Reuters/major business press, industry bodies (e.g. Drewry).
- **Verify every figure, date and claim against a source fetched today. Never invent statistics, news or opportunities.**
  Time-sensitive facts must be current (this week). Credit the source on the image and in the caption.
- Check `posted-log.md` and **do not repeat** a topic, headline or angle from the last 14 days.
- Quality beats schedule: if nothing verifiable and valuable is found, publish an evergreen educational guide instead of thin news.

---

## Creative direction (mandatory, every day)

### Step 1 — Review the feed before designing
1. Read `design-log.md` (the record of every visual concept used).
2. Look at the last 3 days of feed images in `posts/` with the Read tool (EN versions are enough), and list recent posts with
   Windsor `get_data` (connector `instagram`, fields `media_id, timestamp, media_product_type, media_permalink`, `date_preset: last_7dT`).
3. Write down what they share: background tone, palette, photography, layout, typography, headline placement, graphic elements, logo treatment.
4. Deliberately choose a different direction.

### Step 2 — Write today's creative brief (before any code)
Put it at the top of the day's script as a docstring, and copy the short form into `design-log.md`:
- **Concept name** (e.g. "Harbour at dawn", "Steel ledger", "Customs desk still life").
- **Idea**: one sentence on how the visual expresses the topic and the feeling we want (urgency, confidence, calm expertise…).
- **Background tone**: photo / light / mid / dark. **Palette**: 3–4 hex values chosen for this topic.
- **Composition**: e.g. full-bleed photo with lower-third headline, split screen, magazine cover, oversized numeral, minimal poster,
  editorial column layout, single elegant chart, product still life, map/route line art…
- **Type pairing** from `brand/fonts.css` (Latin/Cyrillic face + Arabic-script face), and why.
- **Imagery**: which photo (file + credit) or which illustration approach.
- **Logo treatment** (see below).
- **RTL plan**: how the Persian and Arabic versions mirror or re-balance the composition.

### Step 3 — Variety rules (hard rules)
- Never repeat on consecutive days: background tone, dominant palette, layout archetype, headline typeface, or logo treatment.
- Never reuse a concept name or the same overall look within 14 days. Check `design-log.md`.
- Mix the feed: roughly one photographic post in every two days when photos are available; light/bright designs at least twice a week;
  dark dramatic designs only when the topic calls for drama, and never two days running.
- Avoid making every post a report, spreadsheet, timeline or dashboard. Use a chart only when one picture of the data is the story,
  and then make it a single elegant chart, not a table of numbers.
- **The "Dark Ink" template (dark navy + red accents + white logo box + Inter + stat/rate/timeline cards), used 6–8 Nov 2026, is retired.**
  `brand/brand.css` and `scripts/2026-11-0*.py` remain only as examples of the technical workflow, not of the look.

### Step 4 — Less text on the image
- Headline ≤ 10 words. Total on-image text (excluding footer) ≈ 45 words or less for feed, a little more allowed for Stories.
- One key number or idea per image. Details, bullets and context go in the caption.
- Body text never below 20 px; generous margins (≥ 64 px); clear hierarchy.

### Photography
- Prefer authentic, high-resolution, professionally composed photographs directly relevant to the topic: container ships and ports,
  steel and metal processing, ferroalloy lumps and ingots, mines and minerals, factories and machinery, warehouses, freight, trade venues.
- The photo should be the hero (full-bleed or a large panel), not a small decoration. Use gradients/scrims so text stays readable.
- Only photos licensed for commercial use (Unsplash License, Pexels License, CC0, or CC BY / CC BY-SA with credit) or photos LinkWin owns.
  Never AI-generated imagery, never watermarked or low-resolution stock, never photos of identifiable public figures.
- **Photo library:** licensed photos live in `photos/`, with one entry per file in `photos/CREDITS.md` (file, subject, photographer,
  source URL, licence). Pick from there first; never reuse the same photo within 21 days (check `design-log.md`).
- **Network note:** as of 8 Nov 2026 this workspace cannot reach Unsplash, Pexels, Wikimedia, Openverse or Pixabay (blocked by the
  network policy, HTTP 403). Do not try to route around the block. If those hosts become reachable, download suitable photos, save them
  into `photos/` with a `CREDITS.md` entry, and commit them. If no suitable photo is available, choose a strong non-photographic concept
  (premium typographic poster, editorial magazine layout, refined line illustration or map drawn in SVG, material textures such as
  brushed steel or paper made with CSS) rather than falling back to the old dark template.

### Colour
LinkWin's identity is carried by the logo, the seal red (#AC3E33) used sparingly, and the quality of typography, not by one fixed palette.
Choose a palette per topic, for example: deep navy + silver (shipping) · white + steel grey (industry) · warm bronze/copper metallics
(metals, ferroalloys) · blue + white (logistics, international business) · natural industrial tones (manufacturing photos) ·
charcoal + subtle gold (premium business) · clean neutrals (education) · one bold, sophisticated accent for major market news.

### Typography
`brand/fonts.css` (load next to or instead of `brand/brand.css`) provides, all OFL-licensed:
- Latin + Cyrillic: Playfair Display (editorial serif), Cormorant Garamond (luxury serif), Manrope (modern sans), Oswald (condensed industrial),
  IBM Plex Sans (corporate). Space Grotesk is Latin only (EN). Inter (via brand.css) is also available.
- Arabic script (Persian + Arabic): Noto Naskh Arabic (editorial), Noto Kufi Arabic (geometric display), IBM Plex Sans Arabic (corporate),
  Lalezar (bold poster, one weight), Vazirmatn (via brand.css).
- Arabic-script faces have no Latin glyphs: always stack a Latin face after them for digits/URLs,
  e.g. `font-family:'Noto Naskh Arabic','Playfair Display',serif`.
- Pick type to suit the concept; vary the headline face day to day. Never use letter-spacing on Arabic script.

### LinkWin logo (non-negotiable rules)
> **Update 13 Nov 2026 (Ali): the logo must be a subtle, naturally integrated highlight, never a copy-pasted image on a box or tab.
> The default is now the "Seal signature + echo" treatment from `tools/linkwin_mark.py` (official mark traced 1:1 to a single-colour
> vector in `brand/mark/`, see AUTOMATION.md › 3). This supersedes the rules below where they conflict (single-colour/tone-on-tone
> use of the official shapes is allowed; paper tabs and pasted logo boxes are retired).**
- Always use the original file `brand/linkwin-logo-original-cropped.png`. Never redraw, redesign, recolour, distort, crop into,
  outline, reinterpret or replace it, and never use a monogram or text-only substitute.
- The full-colour original must appear at least once per image at a legible size (≥ 80 px tall on feed).
- What may change is its **presentation**: scale, placement, transparency, lighting, shadow, the surface it sits on.
- The logo file is RGB on an off-white field (no transparency). To integrate it without a pasted white box:
  - **A. Printed seal**: on light paper, light photos or light panels, use `mix-blend-mode:multiply; filter:brightness(1.015)`
    (the 1.5% white-point lift only makes the off-white field disappear; it is the one permitted tonal adjustment).
  - **B. Seal tab**: on dark or busy photos, set it on a small paper-coloured tab that hangs from an edge or sits in the composition,
    logo multiplied onto the tab, soft light/shadow; never a stark white rectangle in a corner.
  - **C. Watermark + signature**: a large, very faint (≤ 10% opacity, multiply) watermark of the original logo as a background element,
    plus a small full-colour signature with linkwinco.com.
  - Other ideas (a subtle glow behind the tab, the logo as part of an editorial masthead, a lit plate within a photo) are welcome if
    they keep the logo's shape, colours and proportions exactly.
  See `brand/samples/logo-treatments.jpg` (template: `templates/_logo-treatments.html`).
- Do not place the logo in the same position with the same treatment two days running.

### Footer
Every image carries, somewhere tasteful: a one-line LinkWin service hook, the source line, and `linkwinco.com`.
Its style follows the day's concept (it does not have to be the old two-column footer).

### Four languages, four polished designs
- Same concept for all four, but each version is designed for its language: re-balance line breaks, sizes and spacing
  for text length; mirror composition for RTL where it helps (text block, photo focal point, logo side).
- Persian and Arabic: `dir="rtl"`, right-aligned, Arabic-script typeface, comfortable line height (≈1.6), no letter-spacing.
- Never ship a version where translated text simply replaced English in an unchanged layout and looks cramped or unbalanced.

### Step 5 — Final creative quality check (all 8 images, before publishing)
Read every rendered JPEG with the Read tool and answer honestly:
1. Does it look clearly different from the last few posts?
2. Would it stop someone scrolling?
3. Does it look like the work of a premium international design agency?
4. Is a relevant, authentic photograph used where appropriate (or is there a strong reason not to)?
5. Is the logo elegantly integrated, not pasted on, and exactly the original?
6. Is the typography beautiful, balanced and readable, with no clipping, overflow, fallback glyphs or wrong RTL alignment?
7. Does it communicate the subject immediately?
8. Are all four language versions equally professional?
If any answer is no, fix it before publishing. Also check overflow programmatically (no element past the canvas or into Story safe zones).

Avoid: Canva-style templates, dark backgrounds with red boxes by default, too many charts or statistics, too much text,
cheap effects (heavy glows, bevels, lens flares), random decorative shapes, generic AI-looking corporate illustration, incorrect logo use.

---

## Captions
Structure: hook → key facts (bullets) → why it matters → practical tip → natural CTA (contact LinkWin / linkwinco.com) → source line → 4–6 targeted hashtags ending with #LinkWinTrading.
No markdown, no AI-typical phrasing, max 2,200 characters.

## Technical workflow
> **From 13 Nov 2026 the mechanics live in `AUTOMATION.md` (Grok Bot pipeline: tools/render.py, posts/YYYY-MM-DD/, Windsor execute_action). Follow that file; the list below is kept for history.**

1. Repo: `aliteimourifar-boop/Linkwin-social` (attach with push access, clone to /home/claude/linkwin-social).
2. Write `scripts/YYYY-MM-DD-<slug>.py` (creative brief in the docstring) that writes `templates/<slug>-<lang>.html` and renders with
   `python3 render.py <template> posts/<slug>-<lang>.jpg feed` and `... posts/<slug>-<lang>-story.jpg story`.
   Write fresh HTML/CSS for each day's concept. Templates live in `templates/`, so asset paths are `../brand/…`, `../fonts/…`, `../photos/…`.
   `render.py` adds `class="story"` to `<html>` for the Story render; style `html.story` for the 9:16 layout.
3. Commit and push (`git -c user.name="LinkWin Bot" -c user.email="noreply@anthropic.com" commit ...`).
4. Confirm each public URL returns 200:
   `https://raw.githubusercontent.com/aliteimourifar-boop/Linkwin-social/main/posts/<file>.jpg`
5. Publish with Windsor.ai for Social Media, connector `instagram`, account `17841478603045856`:
   `create_image_post` (image_url + caption) ×4, then `create_story` (image_url) ×4. EN → FA → RU → AR.
6. Append a line to `posted-log.md` (date · topic · format · sources · media ids) and a line to `design-log.md`; commit, push.
7. If publishing fails (e.g. Windsor plan/trial ended, Instagram error), do not retry endlessly: report the exact error to Ali.
