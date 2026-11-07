# LinkWin Instagram — Daily Playbook

This file is the standing brief for the daily LinkWin Instagram run. Follow it every day.
Owner: Ali Teimourifar, Founder & CEO, LinkWin Trading (Hong Kong HQ + Guangzhou). Account: **@linkwinco**.

## Goal
Make @linkwinco look like a knowledgeable, trustworthy, internationally connected trading partner.
People should follow because every post teaches them something useful (trade news, market intelligence,
practical how-tos), and then think "LinkWin could help me with this". Informative and commercially relevant,
subtly persuasive, never pushy advertising.

## What to publish each day
Per day: **4 feed posts + 4 Stories** — one each in **English, Persian (Farsi), Russian, Arabic**, in that order.
- Feed: 1080×1350 JPEG (4:5). Story: 1080×1920 JPEG (9:16), same design, safe zones top/bottom.
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
- Check `posted-log.md` and **do not repeat** a topic, headline, angle or layout type from the last 14 days. Vary formats
  (stat grid, rate board, checklist, timeline, map/route, myth vs fact, step-by-step guide, comparison).
- Quality beats schedule: if nothing verifiable and valuable is found, publish an evergreen educational guide instead of thin news.

## Brand & design
- Use `brand/brand.css` (fonts bundled in `fonts/`, colour tokens, header, tip card, footer, story mode).
- Colours: ink #12161D, paper #F4EEE4, seal red #AC3E33 / #D0604F, gold #C8A96A.
- **Logo: always `brand/linkwin-logo-original-cropped.png`, unaltered, on the white plate in the top-left header.**
  Never redraw, recolour, crop into, distort or replace it.
- Premium agency look: clear hierarchy, generous spacing, mobile-readable (body text ≥ 20px), no overcrowding.
- Photos: prefer authentic high-resolution photos (ports, ships, factories, warehouses, commodities) from Unsplash/Pexels/Wikimedia
  **if those sites are reachable from the workspace**; never AI-looking imagery. If they are blocked, use the typographic/data design.
- Footer on every image: one-line LinkWin service hook + source line + `linkwinco.com`.
- **Look at every rendered image before publishing** (Read the JPEG). Fix any clipping, overflow, RTL misalignment or font fallback.

## Captions
Structure: hook → key facts (bullets) → why it matters → practical tip → natural CTA (contact LinkWin / linkwinco.com) → source line → 4–6 targeted hashtags ending with #LinkWinTrading.
No markdown, no AI-typical phrasing, max 2,200 characters.

## Technical workflow
1. Repo: `aliteimourifar-boop/linkwin-social` (attach with push access, clone to /home/claude/linkwin-social).
2. Write `scripts/YYYY-MM-DD-<slug>.py` that writes `templates/<slug>-<lang>.html` and renders with
   `python3 render.py <template> posts/<slug>-<lang>.jpg feed` and `... posts/<slug>-<lang>-story.jpg story`
   (see `scripts/2026-11-07-freight.py` as the reference implementation).
3. Commit and push (`git -c user.name="LinkWin Bot" -c user.email="noreply@anthropic.com" commit ...`).
4. Confirm each public URL returns 200:
   `https://raw.githubusercontent.com/aliteimourifar-boop/Linkwin-social/main/posts/<file>.jpg`
5. Publish with Windsor.ai for Social Media, connector `instagram`, account `17841478603045856`:
   `create_image_post` (image_url + caption) ×4, then `create_story` (image_url) ×4. EN → FA → RU → AR.
6. Append a line to `posted-log.md` (date · topic · format · sources · media ids), commit, push.
7. If publishing fails (e.g. Windsor plan/trial ended, Instagram error), do not retry endlessly: report the exact error to Ali.
