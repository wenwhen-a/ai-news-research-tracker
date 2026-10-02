# News sources — tiers and deny list

Used by the daily news digest. `scripts/dedup_and_filter.py` reads the **Deny** section and drops any candidate
whose URL host matches (subdomains included). The other tiers guide searching and sourcing:

- **Tier 1 — Official channels.** Cite these whenever the story has one. An item about a company's own product,
  release, earnings, acquisition or policy must link the company's page when it exists; trade press may be
  listed as a second link for context.
- **Tier 2 — Trade press with strong editing.** Acceptable as the sole source when no official page exists.
- **Leads only.** Any outlet not listed here may be used to *find* a story, but the posted link must come from
  Tier 1 or Tier 2 (or, failing both, a mainstream outlet with a visible publication date). Never post
  aggregator or redirect links (Google News, MSN, Newswav, Flipboard, Yahoo syndication): open them and cite
  the original article.
- **Concentration cap.** At most 3 items per outlet per section per day.

Reviewed monthly: on the last day of each month the routine posts a source report (usage per outlet,
denied drops, verification failures) with recommendations to add or drop sources, and this file is updated by
the maintainer afterwards.

## Tier 1 — Official channels (prefer)
- Unity: unity.com (blog, releases, news)
- Epic Games: unrealengine.com, dev.epicgames.com, forums.unrealengine.com (announcements)
- Roblox: about.roblox.com (newsroom), devforum.roblox.com (release notes), create.roblox.com
- NVIDIA: nvidia.com (GeForce news), developer.nvidia.com (blog), blogs.nvidia.com, nvidianews.nvidia.com
- AMD: gpuopen.com, newsroom.amd.com, amd.com
- Intel: intel.com (newsroom), game.intel.com
- Qualcomm: qualcomm.com (OnQ blog, news)
- Microsoft / Xbox: news.xbox.com, news.microsoft.com, blogs.microsoft.com, devblogs.microsoft.com
- Sony: blog.playstation.com, sonyinteractive.com, sony.com (newsroom), ai.sony
- Nintendo: nintendo.com (news), nintendo.co.jp
- Valve / Steam: store.steampowered.com (news), steamcommunity.com (official announcements)
- Google: blog.google, deepmind.google, developers.googleblog.com
- Meta: ai.meta.com, developers.meta.com, about.fb.com
- Apple: apple.com (newsroom), developer.apple.com
- Adobe: blog.adobe.com, news.adobe.com, helpx.adobe.com (release notes)
- Tencent: tencent.com, hunyuan.tencent.com, gp.qq.com, game.qq.com, cloud.tencent.com
- NetEase: h.163.com, game.163.com, neteasegames.com, fuxi.163.com
- miHoYo / HoYoverse: hoyoverse.com, hoyolab.com, mihoyo.com
- ByteDance: seed.bytedance.com, volcengine.com, bytepluses.com, jimeng.jianying.com
- Alibaba: alibabacloud.com, help.aliyun.com, tongyi.aliyun.com, alibabagroup.com
- Kuaishou: klingai.com, ir.kuaishou.com
- Baidu: qianfan.cloud.baidu.com, baidu.com (newsroom)
- Electronic Arts: ea.com, news.ea.com
- Ubisoft: news.ubisoft.com, ubisoft.com
- Take-Two / 2K / Rockstar: take2games.com, 2k.com, rockstargames.com
- Activision Blizzard: news.blizzard.com, activision.com
- Krafton: krafton.com
- Nexon: nexon.com, company.nexon.com
- NCSoft: ncsoft.com
- Square Enix: square-enix.com, square-enix-games.com
- Sega: sega.com, sega.co.jp, sega.prezly.com
- Capcom: capcom.co.jp, capcom.com
- Bandai Namco: bandainamcoent.com, bandainamco.co.jp
- Konami: konami.com
- Embracer: embracer.com
- CD Projekt: cdprojekt.com
- SAG-AFTRA: sagaftra.org (AI and labor statements)
- Company IR / filings: sec.gov, hkexnews.hk, and each company's investor-relations site (earnings, M&A)

## Tier 2 — Trade press with strong editing (acceptable as sole source)
- GamesIndustry.biz: gamesindustry.biz
- Game Developer: gamedeveloper.com
- Video Games Chronicle: videogameschronicle.com
- PocketGamer.biz: pocketgamer.biz
- MobileGamer.biz: mobilegamer.biz
- Eurogamer: eurogamer.net
- Rock Paper Shotgun: rockpapershotgun.com
- PC Gamer: pcgamer.com
- IGN: ign.com
- GameSpot: gamespot.com
- Gematsu: gematsu.com
- Kotaku: kotaku.com
- The Verge: theverge.com
- Reuters: reuters.com
- Bloomberg: bloomberg.com
- 80 Level: 80.lv
- GameFromScratch: gamefromscratch.com
- Tom's Hardware: tomshardware.com
- TechPowerUp: techpowerup.com
- Famitsu: famitsu.com
- 4Gamer: 4gamer.net
- Inven Global: invenglobal.com
- 游戏陀螺: youxituoluo.com
- 36氪: 36kr.com, eu.36kr.com
- IT之家: ithome.com
- 触乐: chuapp.com
- TechNode: technode.com
- 澎湃新闻: thepaper.cn
- The Decoder: the-decoder.com
- VentureBeat / GamesBeat: venturebeat.com, gamesbeat.com
- TechCrunch: techcrunch.com
- Crunchbase News: news.crunchbase.com

## Deny (dropped automatically by the filter)
# Aggregators and redirects — cite the original article instead
news.google.com
msn.com
newswav.com
flipboard.com
news.yahoo.com
# Crypto, penny-stock and press-release reprint sites
cryptonomist.ch
timesofcasino.com
panews.io
biggo.com
pulse2.com
marketersmedia.com
programminginsider.com
ad-hoc-news.de
# Low-editorial-standard rewrite sites
ts2.tech
tech-insider.org
gadgetreview.com
techtimes.com
windowsreport.com
exputer.com
aroged.com
gtaboom.com
# Vendor press-release feeds presented as news
simulationdaily.com
aithority.com
unite.ai
# Rumor-heavy; may be used as a lead but never as the posted source
insider-gaming.com
dexerto.com
