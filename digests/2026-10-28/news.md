### 第一部分：游戏前沿技术与 AI（深度报道，至少 5 条）

说明：本节经两个独立检索批次（Sonnet子代理分别覆盖西方大厂/平台、中国大厂/引擎/硬件）及编排者本人约11次补充检索（涵盖NVIDIA ACE、Inworld AI、游戏AI融资、反作弊AI、生成式素材工具、Unity Muse、Roblox Cube 3D、PlayStation Mockingbird、SAG-AFTRA/配音演员、GamesIndustry.biz等专项检索）后，过去7天内（2026-10-21至2026-10-28）符合"游戏+AI"交叉、具备充分事实/背景/结果素材、且未被此前简报报道过的深度新闻候选项为2条，低于5条的目标数量。中文信源检索（游戏陀螺、36氪、IT之家、触乐周报、腾讯/网易/米哈游/字节/阿里官方渠道）未发现任何未被`state/news_previous_items.json`覆盖的新候选——本周中文游戏+AI热点（米哈游GameScaling开源、叠纸机器人子公司、腾讯"鹅次元"内测、网易AI选照NPC、Steam Next Fest AI披露数据等）均已在此前14天内的简报中报道过。

## Epic宣布将修改EULA允许用Unreal Engine、MetaHuman产出内容训练AI，被曝"AI双重标准"引发行业哗然
* **日期：** 2026-10-27
* **来源链接：** https://www.gamedeveloper.com/programming/epic-is-updating-the-eula-to-allow-ai-training-on-outputs-from-unreal-engine-and-metahuman
* **核心事实（发生了什么）：**
  * Epic Games CEO Tim Sweeney在X上宣布，公司计划修改Unreal Engine与MetaHuman的用户协议（EULA），取消此前明确禁止使用其产出内容训练AI模型的条款
  * 该变动尚无确定生效时间，Epic也未就具体操作细节回应Game Developer的置评请求
  * Sweeney称此举是对此前报道（批评Epic和微软一边拥抱AI编码、一边打击玩家用AI复刻自家游戏）的回应，强调两者性质不同——Epic对Fortnite的法律行动基于版权与授权
  * Sweeney同时确认Epic的Fab素材市场仍将保留AI使用披露要求，理由是该市场属于B2B场景，客户需要了解内容来源以满足合同要求
* **背景与起因（为什么会发生）：**
  * 10月初，Sweeney要求Epic员工（包括Fortnite团队及与迪士尼合作的未公布漫威/星战射击游戏团队）转向"AI优先"开发模式，该迪士尼合作项目随后被曝延期，Epic此前已裁员超1000人
  * 10月以来，"AI vibe coding"浪潮催生大量AI辅助反编译/移植作品（如Fortnite、Minecraft、Call of Duty、Halo的浏览器/PC移植版），微软和Epic对此发出多份DMCA下架通知
  * 同期，未使用生成式AI的开源项目《Slay the Spire 2》（10月6日）、《Celeste》（10月14日）、《RimWorld》（10月12日）也被卷入GitHub DMCA下架记录
  * Epic确认其"AI优先"迪士尼/漫威项目将使用Anthropic的Claude开发；Unreal Engine此前的EULA明确禁止用引擎/MetaHuman产出内容训练AI，与新方向形成反差
* **结果与进展（已经产生了什么结果）：**
  * 截至报道发布，Epic尚未正式更新EULA文本，新规则细节和生效时间均未公布
  * 事件进一步引发关于游戏行业"AI双重标准"的争议：批评者指出大公司一边以版权为由打击威胁自身利益的AI使用，一边扩大AI在自身业务中的应用以获利
  * 该争议与Epic和Valve围绕Steam AI内容披露政策的公开争执相互交织，成为10月下旬游戏+AI领域的焦点话题之一

## Valve回应Steam"AI乱象"：不做工具"看门人"拒绝封杀AI游戏；Epic CEO斥Steam AI披露新规"可耻"且"政治化"
* **日期：** 2026-10-28
* **来源链接：** https://www.videogameschronicle.com/news/valve-has-a-significant-number-working-on-steams-visibility-dilemma-but-says-it-wont-gatekeep-games-made-with-ai/
* **核心事实（发生了什么）：**
  * 在韩国Steam Indie Connect活动问答环节，Valve Steam业务团队的Tom Giardino表示："我们不想成为告诉开发者该用或不该用哪些工具的看门人"
  * Marc Wilkinson承认Steam新品节现行机制（前两天随机展示、随后转为个性化推荐）确实存在"部分低质量游戏获得曝光"的代价，并称公司内部"相当多的人"在研究这一曝光难题
  * 针对开发者反映遭遇"不交钱就用AI克隆你的游戏"式勒索邮件的问题，Giardino表示Valve会调查个案，但认为勒索本质上属于执法机构的职责范围
  * Epic CEO Tim Sweeney在X发帖中，称Steam店铺页面要求披露AI内容使用的新规是"可耻的"、被迫做出的"政治表态"，称其会被"仇恨团体"用来攻击开发者，还会造成"实际经济损失"
* **背景与起因（为什么会发生）：**
  * Steam今年已取消对"代码中使用AI"的披露要求，但仍要求披露美术资产、配音、翻译等方面的生成式AI使用情况，披露文字以小字显示在商店页面内容提示旁
  * 此次问答源于10月以来开发者持续抱怨Steam新品节充斥"AI垃圾"游戏、以及遭遇AI克隆要挟勒索的报道
  * Sweeney的批评发生在Epic"AI优先"转型及Epic Games Store推出"AI随性编写"新版启动器的背景之下
  * Valve方面强调，自14年前Greenlight上线、以及后来Steam Direct推出时，就曾面临类似的"筛选游戏"呼声，公司一贯策略是突出优质内容而非直接过滤差质内容
* **结果与进展（已经产生了什么结果）：**
  * Valve未在此次问答中宣布任何新政策调整，重申"不做工具看门人"的一贯立场
  * Sweeney与Valve围绕AI披露政策的公开争执，加剧了Epic与Valve平台竞争的紧张关系，也凸显两大平台在AI内容透明度上的政策分歧仍将持续

### 第二部分：游戏与 AI 综合简讯（至少 20 条）

说明：排除所有与此前简报重复的候选项后，本节仅核实到1条符合条件的新简讯，远低于20条的目标数量；经两个子代理（合计超过200次检索/核实工具调用）及编排者本人额外约11次补充检索后未发现更多独立可核实的新候选，故未凑数。

## 《极限脱出》编剧内田哲也自曝新工作室项目遭取消，坦言若早用AI省成本或可避免腰斩
* **日期：** 2026-10-27
* **来源链接：** https://kotaku.com/zero-escape-writer-is-pro-ai-believes-his-new-studios-game-wouldnt-have-been-canceled-if-hed-used-it-to-cut-costs-2000749911
* **概要（三句话以内，仅客观事实）：** 《极限脱出》《弥留之国的爱丽丝》编剧内田哲也透露，他与Too Kyo Games关联新工作室Crash Keys的一款在制作的游戏项目已被发行商取消，他称此事是自己"职业生涯最糟糕的一天"。他在社媒上表示自己是"AI支持者"，认为如果当时能用AI压缩开发周期、降低成本，该项目或许不会被取消，并呼吁中型工作室应更主动拥抱AI以对抗小团队借助AI高效产出大作的竞争压力。

### 第三部分：24 小时游戏与投资快讯（目标至少 10 条；不限 AI 主题）

* **[索尼发布透明配色"Prism"系列PS5手柄与主机外壳]**（2026-10-28）— 索尼公布三款透明配色"Prism Collection"DualSense手柄及PS5主机外壳，11月10日开放预购，2027年2月4日正式发售。 https://www.videogameschronicle.com/news/sony-announces-new-prism-collection-of-transparent-ps5-dualsense-controllers-and-console-covers/
* **[Valve回应Steam"AI游戏泛滥"争议：不会因使用AI工具而设限，正研究提升优质游戏曝光度]**（2026-10-27）— Valve员工在韩国Steam Indie Connect活动上表示不会限制开发者使用何种工具，但承认Next Fest早期随机曝光机制会让劣质AI游戏获得曝光，已有相当数量人员在研究解决方案。 https://www.videogameschronicle.com/news/valve-has-a-significant-number-working-on-steams-visibility-dilemma-but-says-it-wont-gatekeep-games-made-with-ai/
* **[腾讯《FC ONLINE》《FC足球世界》紧急下架姆巴佩相关素材]**（2026-10-27）— 因姆巴佩涉及不当言论引发网友不满，腾讯旗下两款足球游戏宣布下架外部渠道相关球员素材，游戏内内容将通过后续更新调整。 https://finance.sina.com.cn/tob/2026-10-28/doc-iniwttsf9757142.shtml
* **[米哈游《崩坏：星穹铁道》测试包泄密案终审判决生效，泄密者被判赔100万元]**（2026-10-28）— 两名非法获取并破解《崩坏：星穹铁道》未公开测试版本内容的人员，被法院判令连带赔偿共100万元，判决已生效。 https://www.ithome.com/1/018/879.htm
* **[Pocketpair CEO：愿意就《幻兽帕鲁》登陆Switch 2展开洽谈]**（2026-10-27）— 尽管与任天堂的诉讼仍在进行，《幻兽帕鲁》开发商Pocketpair CEO表示公司愿意就游戏登陆Switch 2平台展开讨论，但目前尚无官方移植计划。 https://www.videogameschronicle.com/news/pocketpair-would-love-to-have-conversations-to-bring-palworld-to-switch-2-ceo-says/
* **[《Crossy Road》创作者出任雅达利移动游戏业务执行副总裁]**（2026-10-27）— Hipster Whale联合创始人、《Crossy Road》创作者Matt Hall被任命为雅达利移动游戏业务执行副总裁，负责统筹雅达利跨平台战略。 https://www.videogameschronicle.com/news/the-creator-of-crossy-road-is-now-ataris-executive-vice-president-of-mobile-games/
* **[《天国:拯救》开发商Warhorse Studios确认遭遇网络攻击]**（2026-10-27）— Embracer集团旗下Warhorse Studios确认公司系统和数据遭未经授权访问，CEO称这是一起"严重事件"，正与外部网络安全专家合作调查。 https://www.shacknews.com/article/151157/warhorse-studios-cyberattack
* **[SK海力士：内存短缺将持续至2030年，游戏主机与显卡涨价压力难解]**（2026-10-28）— SK海力士表示全球内存供应短缺态势预计持续至2030年，已与14家主要客户签订长期协议，消费级内存涨价已波及主机与显卡定价。 https://www.theregister.com/systems/2026/10/28/sk-hynix-says-memory-shortages-to-persist-until-2030/
* **[Rockstar英国员工将于《GTA6》发售前后就工会承认进行投票]**（2026-10-27）— 独立工人总工会宣布，Rockstar英国员工将于11月12日至26日就承认工会进行匿名网络投票，投票期覆盖11月19日《GTA6》正式发售，议题涵盖薪酬、加班及生成式AI使用政策。 https://www.engadget.com/gaming/rockstar-workers-in-uk-hold-union-vote-as-gta-6-release.html
* **[据报道《GTA6》PS5版下载容量约210GB，接近占满初代PS5三分之一存储空间]**（2026-10-28）— 据PlayStation商店数据追踪者披露，《GTA6》PS5版下载容量约为210GB，约为《荒野大镖客：救赎2》的两倍，该数字尚未获官方确认。 https://www.gamesradar.com/games/grand-theft-auto/gta-6-is-a-210gb-download-says-playstation-store-sleuth/
* **[《使命召唤：现代战争4》被曝使用韩国梨泰院踩踏事故真实新闻画面，遇难者家属要求删除]**（2026-10-28）— 玩家发现《现代战争4》开场动画中一段片段为2022年梨泰院踩踏事故真实新闻画面，韩国遇难者家属协会要求动视移除并道歉，动视回应称无意轻视该真实悲剧事件。 https://www.koreatimes.co.kr/southkorea/society/20261028/call-of-duty-game-under-fire-for-using-real-itaewon-crowd-crush-footage
* **[《黎明杀机》开发商：查克、针头怪、迈克尔·迈尔斯等下架联动角色仍"敞开大门"欢迎回归]**（2026-10-28）— Behaviour Interactive表示，此前因授权到期移除的查克、针头怪、迈克尔·迈尔斯等恐怖IP联动角色仍有"公开邀请"回归游戏的可能，具体时间未定。 https://www.videogameschronicle.com/news/dead-by-daylight-studio-says-removed-characters-like-chucky-pinhead-and-michael-myers-have-an-open-invitation-to-return/
