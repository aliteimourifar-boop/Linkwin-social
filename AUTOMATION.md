# LinkWin daily Instagram run — RUNBOOK (Grok Bot pipeline, from 13 Nov 2026)

This is the end-to-end procedure for one daily run. **PLAYBOOK.md is the creative and editorial standard; this file is the
mechanics.** If they disagree on mechanics (paths, tools, commands), this file wins.

Account: Instagram @linkwinco · Windsor connector `instagram` · account id `17841478603045856`.
Repo: `aliteimourifar-boop/Linkwin-social` (public; raw URLs are what Instagram fetches).
Output per day: 4 feed posts (EN → FA → RU → AR), 1080×1350 JPEG, one topic adapted per language (not translated literally).
Stories (1080×1920, `render.py ... story`) are optional extras per PLAYBOOK.md.

## 0. Setup (once per box; skip if already done)
```bash
pip install --user --break-system-packages playwright pillow   # uses system Chrome, no browser download
# optional: system Vazirmatn as a fallback (templates load the woff2 from fonts/ anyway)
curl -sL -o /tmp/vaz.zip https://github.com/rastikerdar/vazirmatn/releases/download/v33.003/vazirmatn-v33.003.zip \
  && unzip -oq /tmp/vaz.zip 'fonts/ttf/*' -d /tmp/vaz && mkdir -p ~/.local/share/fonts && cp /tmp/vaz/fonts/ttf/*.ttf ~/.local/share/fonts/ && fc-cache -f
```
Clone / update (token is in env var `GITHUB_LINKWIN_TOKEN`, fine-grained, Contents read/write on this repo only).
**Never print the token, never put it in a remote URL, git config or any file.** Pass it per command:
```bash
gitw() { git -c http.extraHeader="Authorization: Basic $(printf 'x-access-token:%s' "$GITHUB_LINKWIN_TOKEN" | base64 -w0)" "$@"; }
[ -d /workspace/Linkwin-social ] || gitw clone https://github.com/aliteimourifar-boop/Linkwin-social.git /workspace/Linkwin-social
cd /workspace/Linkwin-social && gitw pull --ff-only
```
(`Authorization: Bearer` does not work for git-over-HTTPS; use the Basic `x-access-token` form above.)

## 1. Research (pick ONE topic)
1. Read `posted-log.md` (last 14 days) and `design-log.md`. Do not repeat a topic, headline or angle.
2. WebSearch/WebFetch, last ~48 h, credible sources only (government/official, Xinhua, Reuters, major business press,
   industry bodies such as Drewry, SMM, Mysteel). Rotate categories per PLAYBOOK.md (ferroalloys/metals are the flagship).
   If a site blocks WebFetch, `curl -sL -A "Mozilla/5.0"` the same public page.
3. Write down every figure/date with its source URL and publication date. **Nothing goes on an image or in a caption
   that is not in a source fetched today.** If nothing verifiable and useful turned up, do an evergreen how-to instead.

## 2. Write
- Per language: headline (≤10 words), ≤45 words of on-image text, caption (hook → bullets → why it matters → practical tip
  → CTA with linkwinco.com → source line → 4–6 hashtags ending `#LinkWinTrading`), ≤2,200 characters, no markdown.
- FA: natural Persian business prose, Persian digits, Solar Hijri dates (check: 9 Nov 2026 = 18 Aban 1405).
  AR: Western digits, wrap Latin/digits in `<bdi>` on images. RU: thin/no-break space before %, dd.mm.yyyy.
- Store captions in `posts/YYYY-MM-DD/posts.json` (`[{lang, image_url, caption}]`) and `posts/YYYY-MM-DD/captions.md`.

## 3. Design + render
1. Photo (preferred): search Wikimedia Commons via the API (no key needed), keep only commercial-use licences
   (CC0, CC BY, CC BY-SA, PD) with ≥2,400 px on the long side, avoid identifiable people:
   `https://commons.wikimedia.org/w/api.php?action=query&format=json&generator=search&gsrnamespace=6&gsrsearch=<terms>&prop=imageinfo&iiprop=url|size|extmetadata|mime&iiurlwidth=400`
   (send a User-Agent). Download the original, resize to ≤3000 px, save in `photos/`, add a line to `photos/CREDITS.md`,
   credit photographer + licence on the image and in the caption. Never use AI imagery for photos; if an AI background is
   ever unavoidable, it must contain no text, and all text is set in HTML.
2. Write `scripts/YYYY-MM-DD-<slug>.py` (creative brief + facts in the docstring, see `scripts/2026-11-13-apec-trucks.py`
   as the reference). It writes `templates/YYYY-MM-DD-<slug>-<lang>.html` and renders each one:
   ```bash
   python3 tools/render.py templates/<file>.html posts/YYYY-MM-DD/<file>.jpg feed     # 1080x1350
   ```
   `tools/render.py` waits for fonts and images, and reports (exit 2 unless `--no-strict`) any text element outside the
   canvas, horizontally clipped text, a web font that failed to load or a broken image.
   Fonts: `brand/fonts.css` (Playfair, Cormorant, Manrope, Oswald, IBM Plex Sans/Arabic, Space Grotesk, Noto Naskh/Kufi
   Arabic, Lalezar, **Vazirmatn**). Arabic-script faces have no Latin: stack a Latin face after them. RTL: `dir="rtl"` on `<html>`.
3. Logo — **default treatment "Seal signature + echo" (Ali, 13 Nov 2026: integrated, never pasted on; no white box/tab)**.
   Use `tools/linkwin_mark.py` in every day script:
   ```python
   sys.path.insert(0, os.path.join(ROOT, "tools")); from linkwin_mark import MARK_CSS, signature, echo
   # put MARK_CSS in the <style>, signature() on the layout grid (footer cell or masthead), and optionally
   # echo("right"|"left", bottom, inset) inside a position:relative; overflow:hidden panel/section
   ```
   - signature = official seal as a single-colour vector in seal red `#AC3E33` (`--lw-seal`), a hairline rule, and the
     official 链赢贸易 / LinkWin Trading wordmarks in the design's text tint (`--lw-ink`); seal height `--lw-sig-h` (≈60–70 px feed).
     On light designs set `--lw-ink` to the ink colour; the seal may also go tone-on-tone (e.g. paper tint) if red clashes.
   - echo = the same seal very large and faint (`--lw-echo-op` 4–7 %, `--lw-echo-size`), cropped by an edge, behind content.
   - RTL: `dir="rtl"` mirrors the signature automatically; pass `echo("left")` for FA/AR.
   - Vectors live in `brand/mark/` (`linkwin-seal.svg`, `linkwin-logo-full.svg`, `linkwin-wordmark-cn.svg`, `linkwin-wordmark-en.svg`),
     traced 1:1 from the official transparent files `brand/mark/source-*.png` (linkwinco.com/assets/img/seal-light.png,
     logo-full-light.png) by `tools/trace_logo.py`. Never redraw, distort or re-letter them; vary placement, size and tint only.
   - QC: crop the logo area at 100 % and check edges are crisp, the wordmark is legible, nothing sits on a box.

## 4. QC (all must pass before anything is published)
Open every JPEG with the Read tool (also a 100 % crop of the RTL text) and tick:
- [ ] Facts: every number/date/name on image and caption matches a source fetched today; source line present.
- [ ] Language: reads natively; no literal translation; FA digits/Solar Hijri; AR digits; RU typography.
- [ ] RTL: FA/AR right-aligned, letters joined, ZWNJ correct (e.g. می‌شود), Latin/digits in correct order, no letter-spacing.
- [ ] No clipping/overflow/fallback glyphs (`tools/render.py` printed OK).
- [ ] Logo: `linkwin_mark` signature (traced official mark), crisp at 100 % crop, wordmark legible, no box/tab, integrated in the grid.
- [ ] Design: differs from the last 3 days (tone, palette, layout, headline face, logo treatment) per design-log.md.
- [ ] Photo licence recorded in photos/CREDITS.md and credited.
- [ ] Caption ≤2,200 chars, 4–6 hashtags ending #LinkWinTrading, linkwinco.com included.
- [ ] JPEG, 1080×1350, < 8 MB.

## 5. Push + verify URLs
```bash
git add -A && git -c user.name="LinkWin Bot" -c user.email="noreply@linkwinco.com" commit -m "YYYY-MM-DD: <topic> (4 feed)"
gitw push origin main
for l in en fa ru ar; do u="https://raw.githubusercontent.com/aliteimourifar-boop/Linkwin-social/main/posts/YYYY-MM-DD/YYYY-MM-DD-<slug>-$l.jpg"
  curl -s -o /dev/null -w "$l %{http_code} %{content_type} %{size_download}\n" "$u"; done
```
Every URL must return `200 image/jpeg`. raw.githubusercontent.com can lag ~1–5 min after a push (CDN); retry, do not publish
until all four pass.

## 6. Publish (only when Ali has approved the run or has switched on unattended publishing)
Windsor MCP tool `execute_action`, one call per language, in order EN → FA → RU → AR:
```json
{"connector": "instagram", "account": "17841478603045856", "action": "create_image_post",
 "params": {"image_url": "<raw URL>", "caption": "<caption from posts.json>"}}
```
- Check each response for the new media id. If a call errors (permissions, Windsor plan/trial, Instagram rejection of
  the image), stop, do not retry in a loop, and report the exact error to Ali. A permissions error usually means reconnecting
  Instagram in Windsor.
- Windsor has no scheduling and no draft state: a successful call is live immediately.
- Verify: Windsor `get_data`, connector `instagram`, accounts `["17841478603045856"]`, fields
  `media_id, timestamp, media_product_type, media_permalink, media_caption`, `date_preset: last_7dT`; confirm 4 new FEED items.
- Optional Stories: `create_story` with `{"image_url": ...}` (no caption).

## 7. Log (so tomorrow does not repeat)
Append one line to `posted-log.md`:
`- YYYY-MM-DD · <topic with key facts> · <layout> · <sources with dates> · feed EN <id>, FA <id>, RU <id>, AR <id>`
and one line to `design-log.md` (format at its top; replace "DRAFT" with the media ids once published). Commit + push.

## 8. Weekly analytics (Mondays)
Windsor `get_data`, connector `instagram`, account `17841478603045856`, `date_preset: last_7dT`, fields such as
`media_id, timestamp, media_caption, media_reach, media_likes, media_saved, media_shares, media_comments` (post level) and
`reach, follower_count` (account level; follower growth only reports above 100 followers). Summarise best/worst post,
language and topic, and suggest one change. Save the summary to `analytics/YYYY-Www.md`.
