# LinkWin Instagram (@linkwinco) - handoff for the next operator

Written 28 Nov 2026 at Ali's request ("summarize everything ... so another AI can take over exactly where you left off").
Read this first, then AUTOMATION.md (mechanics), PLAYBOOK.md (creative/editorial standard), OVERRIDES.md (one-off dated instructions),
and the three logs: posted-log.md (every post, topic, slide order, sources, media ids), design-log.md, video-log.md.

## Account and stack
- Instagram @linkwinco, LinkWin Trading Co., Ltd., https://linkwinco.com. Instagram account id 17841478603045856.
- Publishing: Windsor.ai connector `instagram`, actions create_carousel_post, create_video_post, create_story. Count a post as live only when a media id comes back; never retry a failed call before checking it didn't go live.
- Hosting: this public repo; Instagram fetches the raw.githubusercontent.com URLs. Write access uses a fine-grained GitHub token (Contents read/write, this repo only, expires 11 Feb 2027). Never commit or print the token.
- Rendering: Python + Playwright/Pillow templates, ffmpeg for video, fonts in fonts/ (Vazirmatn etc.), logo mark via tools/linkwin_mark.py. Per-day scripts in scripts/<date>-*.py.

## Schedule
- Daily, content live around 9:00 PM Asia/Shanghai (the job starts about 8:15-8:30 PM).
- Mondays also: pull 7- and 30-day Instagram analytics via Windsor, write analytics/<year>-W<nn>.md, apply learnings to the week.
- If posted-log.md already has today's date, skip. Missed days are logged as SKIPPED and not backfilled.

## Current daily format (Ali, 17 Nov 2026, effective 18 Nov)
1. ONE carousel: the day's news topic in four languages, one 1080x1350 slide each for EN, FA, RU, AR (+ optional sources/CTA slide). First-slide language is random each day and must differ from yesterday's. One combined caption <= 2200 chars: a native section per language in slide order (~400-480 chars each), then shared hashtags, CTA, linkwinco.com. FA/AR fully RTL-correct.
2. ONE short English Reel, ~15-30 s, 1080x1920: educational trade / shipping / sourcing / commodities / China-development format (quiz, X vs Y, key numbers, how-it-works). Published with share_to_feed true.
3. The same video as a Story (use the lower-bitrate *-story.mp4 encode; full bitrate failed as a Story).

## Ali's standing instructions (all still in force)
- HARD RULE (15 Nov): everything must comply strictly with PRC law and policy. Nothing anti-China, hostile or politically sensitive: no sovereignty/maps issues, no hostile sanctions or trade-war framing, no politics, leaders, religion, military. Strictly commercial and neutral; prefer Xinhua, MOFCOM, GACC, China Daily and recognised trade press. When in doubt, drop the topic. QC.md has a compliance line per language.
- No invented facts: every figure on an image or caption must come from a source fetched that day, logged with URL and date.
- Logo (13 Nov): the LinkWin mark is a subtle, elegant, integrated highlight in each design, never a pasted logo or badge.
- Topics: mix trade, ferroalloys/metals (flagship), logistics, sourcing and education; not self-promotion. Don't repeat a topic or angle from the last 14 days.
- Real imagery only (17-18 Nov): real, dated, licensed photos/footage, credited (photos/CREDITS.md); never AI-generated or fake visuals. Ali approved publishing Reels that pass QC without asking him first.
- Video creative direction (22-23 Nov): every video must have its own identity. Differ from the last 7 videos on art direction, layout, palette, fonts, animation, transitions, music and structure; write the renderer fresh each day; premium easing/motion; mood-matched professional music (license-clear track or produced original, about -14 LUFS, no click at loop point). Compare frames against the previous 3 videos and redesign if it reads as a variation. Log each in video-log.md.
- Caption labels sections EN/FA/RU/AR rather than flag emojis.
- Never change account settings, delete/edit existing posts, buy anything or grant permissions.
- Daily report to Ali: carousel topic + first-slide language, video subject + art direction + music style, the three media ids, any problem.

## Recent history (details and media ids in posted-log.md)
- 6-16 Nov: old format (4 single-language feed posts + 4 image Stories). Topics: Canton Fair record, freight rates, export-control dates, chrome ore stocks, HK exports, China Oct trade, tariff truce, Shenzhen APEC truck limits, RMB clearing in Indonesia, silicomanganese/Yunnan, CIIE record.
- 17 Nov: container-lines quiz Reel (Ali loved it).
- 18-19 Nov: skipped (usage/billing outage).
- 20 Nov: ports milestones carousel + China then-vs-now Reel (real 1976-1991 archive photos vs today).
- 21 Nov: ferrochrome below cost carousel + FOB/CIF/DDP Reel.
- 22 Nov: China trade-deal talks carousel + 20ft/40ft/40HC container Reel.
- 23 Nov: China-Europe trains carousel + HS code 7202.41 Reel ("Swiss Kinetic").
- 24 Nov: Single Window auto-stamp carousel + letter of credit Reel ("Glass Ledger").
- 25-26 Nov: skipped (weekly usage limit reached).
- 27 Nov: one-off override, China-Iran trade carousel (China Customs Jan-Sep 2026, US$3.33 bn) + PERSIAN Reel and Story ("Saffron Route"). Left out the y/y drop, the Bandar Abbas sea route and payment channels under the PRC rule.
- From 28 Nov: back to English Reels (the override in OVERRIDES.md applied to 27 Nov only).

## Known issues / watch-outs
- The shared weekly usage limit has stopped runs twice (18-19 and 25-26 Nov). It resets Fridays around 6:24 PM Shanghai time.
- Analytics (W47/W48 notes): some engagement figures look inorganic (e.g. ~990 likes/620 saves on 113 views; +726 followers on 18 Nov with no post). Organic reach is small (often <40 views). Practical how-it-works Reels outperform news; English gets most reach; Persian got relatively strong engagement.
- Windsor may need reconnecting; GitHub token expires 11 Feb 2027.
