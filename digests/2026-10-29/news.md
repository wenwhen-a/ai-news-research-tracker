### 第一部分：游戏前沿技术与 AI（深度报道，至少 5 条）

## Epic Games副总裁称AI编程工具已消除Unreal Engine十年未解的「非确定性cooking错误」
* **日期：** 2026-10-28
* **来源链接：** https://www.gamedeveloper.com/programming/unreal-engine-will-be-developed-with-ai-code-confirms-epic
* **核心事实（发生了什么）：**
  * Epic Games开发副总裁(Executive Vice President of Development)Marcus Wassmer在接受播客This Week in Video Games采访时首次详细披露公司如何用AI开发自家引擎与软件,此前Epic未就此公开细节。
  * Wassmer表示Epic「确定在使用AI来开发Unreal Engine的代码与功能」,目前大部分相关开发集中在Fortnite、UEFN(Unreal Editor for Fortnite)及UE6的开发分支(dev stream)中进行。
  * 他表示Claude、Codex等AI编程工具已经消除了Epic团队尝试修复了十年之久的「非确定性cooking错误」(non-deterministic cooking bugs,即引擎打包资源阶段出现的不稳定、难复现的报错)。
  * Wassmer还提到AI工具被用于自动监测Fortnite在PC端的稳定性,标记导致问题的特定驱动与硬件组合。
  * 他提到Epic此前曾披露用「vibe coding」方式重写了Epic Games Launcher,新版本运行明显更快;这一开发方式目前已被用于不止商店这一个产品线,工程师不再手写大部分代码,但仍把控代码的范围与方向。
  * 针对外界对生成式AI可能拉低游戏品质的担忧(相关调查显示开发者对此担忧上升),Wassmer回应称Epic「更担心行动太慢的风险,而不是AI怀疑论」。
* **背景与起因（为什么会发生）：**
  * 此次表态是Epic近期「AI优先」(AI-first)战略的最新延伸:此前有报道称Epic旗下与迪士尼合作的项目已转向「AI优先」开发模式,且Epic正在更新Unreal Engine与MetaHuman的用户协议(EULA),以允许用这些工具产生的内容训练AI模型。Wassmer的采访是Epic首次就「如何用AI开发自家引擎」给出具体细节,此前相关动向多为外部报道或政策变更,未有高管正面披露内部工作流。
* **结果与进展（已经产生了什么结果）：**
  * 采访披露后,引擎开发社区关注Epic计划在类似「5.9」版本中推出的改动——据Wassmer描述,这类更新规模相对适度,将聚焦具体系统,并包含AI辅助产生的变更;Epic强调AI工具的作用目前集中在提升引擎稳定性(「让引擎在我们开发、精简过程中保持更稳定」),而非完全自动化整个开发流程。

## 3D模型网站Open3DLab指控Roblox旗下AI爬虫未经许可抓取145GB数据(含成人内容),Roblox确认已关停该爬虫
* **日期：** 2026-10-28
* **来源链接：** https://www.gamedeveloper.com/business/roblox-confirms-no-adult-content-used-in-ai-training-after-scraping-open3dlab-data
* **核心事实（发生了什么）：**
  * 3D素材分享站Open3DLab(其用户包括大量使用Valve Source Filmmaker制作模型的创作者)管理员「Salaryman」披露,该站及其关联的多个成人内容站点遭到一个关联Roblox的AI爬虫未经授权抓取数据。
  * 据Open3DLab统计,该爬虫几乎遍历了三个托管站点上的所有项目,从712个项目中下载了1,027个文件,总量约145.5GB,其中约117.4GB来自成人内容站点;被抓取项目中,345个为成人内容、423个仅获非商业使用授权。
  * Open3DLab表示爬虫无视其robots.txt协议及服务条款(均明确禁止抓取),该站10月18日首次发现并封锁了该爬虫并致信其创建者,爬虫10月19日恢复抓取并规避了站方的拦截措施。
  * Open3DLab称已通过爬虫的User-Agent信息,将其创建者认定为Roblox一名研究员,该研究员为Roblox生成式3D基础模型Cube的论文共同作者,据此判断抓取数据用于AI模型训练。
  * Roblox发言人回应称,该AI agent「未能按预期运行」,已被关停下线,且「收集的数据未被用于任何用途,包括训练任何AI模型」;公司表示将加强对此类agent构建与审核流程的安全保障。
* **背景与起因（为什么会发生）：**
  * Salaryman在披露中特别指出,若含成人内容的训练数据流入Roblox的生成式工具,可能经由这些工具触及未成年用户,并提出对基于其他公司知识产权数据训练模型的担忧。相关报道还提及,Roblox当前正面临美国多个州就儿童安全问题提起的诉讼,这使得此次事件对该公司更为敏感。
* **结果与进展（已经产生了什么结果）：**
  * 目前该事件停留在Open3DLab指控与Roblox官方声明「已关停agent、数据未用于训练」的阶段,尚无第三方独立核实抓取数据的具体用途或范围;Roblox表示将强化内部AI agent的构建与审核安全机制,但未公布具体整改措施或时间表。

## Valve在Steam Indie Connect活动上回应AI「仿制游戏」勒索与「AI垃圾内容」担忧,拒绝为AI工具设门槛
* **日期：** 2026-10-27
* **来源链接：** https://www.invenglobal.com/articles/27761/valve-responds-directly-to-developers-fearful-of-ai-slop-and-game-cloning
* **核心事实（发生了什么）：**
  * 2026年10月27日,Valve与釜山独立游戏节(BIC)组委会、韩国内容振兴院(KOCCA)在韩国共同举办「Steam Indie Connect」开发者交流活动。
  * Valve Steam商务团队成员Tom Giardino与Marc Wilkinson出席问答环节,回应韩国开发者的提问。
  * 多名开发者反映近期收到勒索邮件,威胁「如果不付款,将用AI克隆你的游戏并抢先发布」;Giardino称这是他首次听说此类具体案例,认为敲诈勒索更多属于执法范畴,但Valve愿意调查开发者举报的案例并提供帮助。
  * 关于AI工具使用,Giardino明确表示:「我们不想充当看门人,去告诉开发者应该或不应该使用哪些工具」,是否使用AI由开发者自行决定。
  * 关于「仿制游戏」问题,Valve建议开发者持续更新、构建社区与独特风格,而非依赖容易被复制的单一机制,认为正版应当成为「最好的版本」。
  * Wilkinson承认Steam Next Fest前两天采用随机曝光机制以保证公平,但这意味着「部分低质量游戏会被曝光」,Valve「完全意识到」这一问题,且有「相当多的人」正在研究解决方案(次日VGC报道确认了这一说法)。
  * Giardino回顾称,开发者在14年前Steam Greenlight上线、以及后来Steam Direct上线时都曾要求设置过滤器,但Valve的目标始终是让优质游戏浮现而非过滤劣质游戏,并称「我们不认为自己是完美的,还有很大改进空间」。
* **背景与起因（为什么会发生）：**
  * 此次活动是在Steam平台AI生成内容游戏数量快速增长(据统计,一年内披露使用生成式AI的Steam游戏数量增长近800%,达近8000款)、以及自2026年9月末以来多名独立开发者收到AI克隆勒索邮件的背景下举行的;Valve此前已在今年早些时候修改Steam的AI披露政策,收窄披露范围至玩家可感知的AI生成内容,豁免了幕后使用的开发工具。
* **结果与进展（已经产生了什么结果）：**
  * Valve未在此次活动上宣布任何新的AI工具审查机制或仿制游戏检测机制;次日(10月28日)Video Games Chronicle援引Inven Global详细报道了此次活动内容,进一步扩大了Valve表态的媒体关注度,并间接引发Epic Games CEO Tim Sweeney在随后几日对Steam AI披露政策的公开批评。

## 微软与Epic Games对AI「反编译」移植版游戏发起大量DMCA投诉,Tim Sweeney回应「AI是窃取」指控
* **日期：** 2026-10-27
* **来源链接：** https://kotaku.com/now-that-the-shoe-is-on-the-other-foot-microsoft-and-epic-games-suddenly-agree-that-ai-is-theft-2000749316
* **核心事实（发生了什么）：**
  * 借助AI编程工具(文章提及Anthropic的Claude Opus 5.5),反编译与「重新编译」游戏变得更快更便宜,大量AI「vibe coded」的浏览器移植版与PC重制版在网络上泛滥,催生大量DMCA删除通知;包括《Slay the Spire 2》《Celeste》《RimWorld》等并未使用生成式AI的独立游戏,其代码也在未获开发者同意的情况下被开源并出现在GitHub的DMCA记录中。
  * Epic Games于10月10日对一个AI「vibe coded」的浏览器版《堡垒之夜》移植版发起DMCA投诉;据一名用户反映,Epic还举报了大量展示该移植版的帖子。
  * 微软在过去一个月内对《我的世界》《使命召唤》《光环》的浏览器移植版发起多次DMCA投诉,文章统计至少有6个《使命召唤》移植版因此被下架。
  * Epic的服务条款禁止用户将其内容用作生成式AI的训练输入。
  * 文章指出讽刺之处:Epic于10月14日发布的新版Epic Games Store启动器被批评为大量使用AI「vibe coding」构建;据彭博社10月12日报道,Epic与迪士尼合作、「AI优先」开发的漫威/星球大战射击游戏将使用Anthropic的Claude开发,而Anthropic在2025年曾因使用BitTorrent来源数据训练模型支付15亿美元赔偿(但未被要求重新训练模型)。
  * 微软每年向AI数据中心投入约800亿美元;动视暴雪已承认在《黑色行动6》与《黑色行动7》中使用AI生成美术素材。
  * Xbox CEO Asha Sharma在10月13日的Xbox Labs公告中表示微软「致力于成为知识产权的负责任管理者」;文章援引微软一名产品经理2026年曾建议用《哈利·波特》原著训练大语言模型(该建议后被撤回)作为反例,并引用《纽约时报》诉微软与OpenAI版权案证据披露中微软员工Brent Hecht将大规模抓取训练数据形容为「令人震惊的盗窃」的内部言论。
* **背景与起因（为什么会发生）：**
  * 争议源于AI编程/反编译工具近期的快速进步,使独立开发者几乎无力对抗拥有法律资源的大公司对其开源代码提起的DMCA投诉,而大公司自身的AI产品训练数据来源(如经抓取盗版网站数据训练的图像与语言模型)也面临类似指控,形成被舆论称为「双重标准」的局面。
* **结果与进展（已经产生了什么结果）：**
  * Epic CEO Tim Sweeney于10月27日在X上回应称文章「混淆了多个不同问题」,强调Epic不允许未经授权使用《堡垒之夜》IP;他确认Epic的最终用户许可协议目前限制用Unreal Engine与MetaHuman的输出训练AI模型,并表示公司正着手从条款中移除这一限制。他还就Anthropic的法律灰色地带作出说明,称法院认定Anthropic因torrent下载盗版内容承担侵权责任,但训练行为本身被判定属合理使用,其他法院对AI输出是否侵权的判断则取决于其与原作品的相似度;Kotaku表示已通过Epic公关团队联系Sweeney寻求进一步评论。

## Epic CEO Tim Sweeney炮轰Steam的AI披露要求「令人憎恶」,称是一种「政治表态」
* **日期：** 2026-10-26
* **来源链接：** https://kotaku.com/epic-steam-valve-tim-sweeney-gen-ai-declaration-political-abhorrent-2000749706
* **核心事实（发生了什么）：**
  * 10月23日,Tim Sweeney在X上发帖称Steam强制开发者披露AI使用情况,是在「强迫开发者写一份政治声明」,并称这种做法「令人憎恶」(abhorrent)。
  * Sweeney表示Valve此举存在「实际的经济代价」,认为AI披露标签可能被用来发起针对开发者的抵制运动,从而损害其收入。
  * 对于有人指出Epic旗下的资产商店Fab同样要求披露AI使用情况,Sweeney回应称Fab是「一个企业对企业的市场」,买家需要知道内容来源,这与Steam面向普通消费者的政策「不同」。
  * 据报道,Steam的AI披露政策今年已有所放宽:目前不再要求披露代码中使用的AI,仅要求披露用于资产制作、配音、翻译等用途的生成式AI;披露信息以小字显示在商店页面下方,与内容警告并列。
  * 开发者Matt Workman发帖称「2026年还要求AI披露的前提本身就很荒谬」,认为这让Valve和Steam很难看,Sweeney对此回复表示赞同。
* **背景与起因（为什么会发生）：**
  * 此番言论发生在Valve于10月27日Steam Indie Connect活动上为其AI工具「不设门槛」政策进行辩护的前后,显示出Epic与Valve在生成式AI商店政策上的公开分歧,也延续了此前Epic被曝「AI优先」转型、以及微软与Epic因AI反编译移植版发起DMCA投诉引发「双重标准」质疑的背景。
* **结果与进展（已经产生了什么结果）：**
  * 报道中Valve并未对Sweeney的言论作出直接公开回应;部分评论者(包括Kotaku作者)认为Sweeney的批评带有政治色彩,实质是对AI使用本身的道德反对,并指出Epic Games Store长期以来难以与Steam竞争。

## Epic Games公布「2026 Epic AI MegaJam」游戏创作大赛,联合Anthropic、OpenAI、谷歌等共6.5万美元奖金
* **日期：** 2026-10-22
* **来源链接：** https://www.invenglobal.com/articles/27578/epic-games-announces-2026-epic-ai-megajam-with-up-to-50000-in-grants
* **核心事实（发生了什么）：**
  * 2026年10月22日,Unreal Engine官方X账号以「Vibe your way to 50K」为口号宣布2026 Epic AI MegaJam,详情同步发布于Unreal Engine官网及itch.io报名页。
  * 比赛为期四天(11月12日至15日),参赛者需使用Unreal Engine或Unreal Editor for Fortnite(UEFN)制作可玩游戏。
  * 每支队伍最多5名人类成员,外加「无限数量」的AI代理;参赛者可使用从资产生成到编程代理的任意AI工具,官方明确AI使用为可选而非强制。
  * 主奖项分三类:Unreal Engine最佳整体作品、UEFN最佳整体作品、最佳学生项目,各类别第一名7500美元、第二名5000美元、第三名2500美元。
  * 表现突出的Unreal Engine与UEFN作品可获最高5万美元「开发延续资助」,用于赛后继续开发。
  * 修饰奖项包括最佳团队(5000美元),以及最佳个人开发者作品、最佳视觉效果、最佳移动游戏、最佳展示AI工具使用的开发日志、最佳使用LLM驱动角色的UEFN叙事游戏(各2500美元)。
  * 活动支持线上参与、本地开发者社区参与,以及旧金山Digital Jungle线下场地(11月14日至15日);Epic表示Anthropic、谷歌、Meshy、OpenAI及SpaceXSI等公司团队将一同参赛,部分AI合作伙伴将为参赛者提供工具使用额度。
  * 线下名额将于11月1日太平洋时间7点开放报名,名额有限;开幕直播定于11月11日在Twitch、YouTube、X同步进行并公布主题。
* **背景与起因（为什么会发生）：**
  * 此次比赛是在Epic Games今年持续推进「AI优先」开发战略的背景下举办的:据此前报道,Epic CEO Tim Sweeney于10月12日宣布公司将重新分配人力以加速采用AI开发,并于10月14日发布了由AI「vibe coding」构建的新版Epic Games Store启动器(称启动速度比Steam快46%);Epic此前已在Unreal Engine 5.8中引入实验性插件允许接入大语言模型,并计划在Unreal Engine 6中集成Claude、Gemini等模型。
* **结果与进展（已经产生了什么结果）：**
  * 公告发布后,部分媒体与玩家对比赛的AI门槛提出批评,Rock Paper Shotgun将其形容为「奖励无人问津的AI vibe-coded slop游戏的现金」;截至发稿,线下场地报名尚未开放(定于11月1日开始),完整赛程与结果将在11月15日赛事结束后揭晓。

### 第二部分：游戏与 AI 综合简讯（至少 20 条）

说明：本周经两批独立检索子代理（分别覆盖西方大厂/平台、中国大厂/引擎/硬件）及编排者本人约20次补充检索（涵盖Unity、Xbox Copilot、游戏AI融资、反作弊AI、DeepMind、Meta Horizon、Krafton、ByteDance Seed、PlayStation、SAG-AFTRA、网易伏羲、快手可灵、完美世界、三七互娱等方向）后，去除与此前七天内已报道事件重复或属同一事件后续报道的条目（8条），本部分仅有 3 条经核实的全新「游戏+AI」简讯，低于20条目标——这是经过充分检索后的真实结果，未进行任何编造或凑数。

## 米哈游密集投资两家AI芯片公司，同期退出所持脑机接口公司股权
* **日期：** 2026-10-29
* **来源链接：** https://www.21jingji.com/article/20261029/herald/dd3031fa7cbaed3404c731e3b8014cc2.html
* **概要（三句话以内，仅客观事实）：** 据21世纪经济报道，米哈游10月19日跟投存算协同芯片公司铭芯启睿超4亿元A轮融资，随后又参与神经拟态低功耗芯片公司九天睿芯融资；同日，米哈游完成工商变更，退出此前持股49%的脑机接口公司零唯一思。报道指出，目前没有公开证据显示这些芯片已接入米哈游的模型或游戏业务，刘伟此前提出的“三年最多投入1000亿元”为投入上限而非已发生支出。

## NVIDIA为《Phantom Blade Zero》带来DLSS 4.5光线重构技术,并为多款游戏推出DLSS更新
* **日期：** 2026-10-28
* **来源链接：** https://www.nvidia.com/en-us/geforce/news/phantom-blade-zero-path-tracing-dlss-4-5-ray-reconstruction/
* **概要（三句话以内，仅客观事实）：** NVIDIA于10月28日宣布,由S-GAME开发的动作游戏《Phantom Blade Zero》上线即支持DLSS 4.5、光线追踪与路径追踪,启用路径追踪后自动开启DLSS光线重构(用单一神经网络模型取代传统手调降噪器)并支持最高6倍动态多帧生成,NVIDIA称2560×1440分辨率下RTX 50系列显卡平均帧率提升达7.8倍;同一公告中,《地铁2033:重制版》《地铁:最后的曙光:重制版》《黎明行者之血》《杀戮空间3》等游戏也同步获得DLSS 4.5相关更新。

## 据报道AI编程工具助推PS5主机破解热潮,黑客通过漏洞赏金计划获5万美元披露虚拟化层漏洞
* **日期：** 2026-10-26
* **来源链接：** https://kotaku.com/ai-has-triggered-a-ps5-homebrew-gold-rush-but-its-also-the-reason-gta-6-cant-be-pirated-at-release-2000749776
* **概要（三句话以内，仅客观事实）：** Kotaku 10月26日报道称,随着索尼停止生产PS5实体光盘媒介,借助AI编程工具的PS5自制软件(homebrew)热潮兴起,黑客「2tonejordy」通过HackerOne向索尼披露了一个PS5虚拟化层(hypervisor)漏洞并获5万美元赏金;因披露时间早于《GTA 6》11月19日发行日期,文章称该漏洞不会被用于在《GTA 6》首发当天实现盗版,索尼未就此发表官方声明。

### 第三部分：24 小时游戏与投资快讯（目标至少 10 条；不限 AI 主题）

* **[FromSoftware《The Duskbloods》延期至2027年发售]**（2026-10-29）— FromSoftware与任天堂合作开发的Switch 2平台独占游戏《The Duskbloods》被官方宣布延期至2027年发售，具体延期原因暂未披露。 https://www.videogameschronicle.com/news/fromsoftwares-switch-2-exclusive-the-duskbloods-has-been-delayed-to-2027/
* **[《GTA6》官方原声专辑由Justice创作，12月11日发行，CD与黑胶现已开放预购]**（2026-10-29）— Rockstar Games宣布《GTA6》官方配乐专辑由法国电子乐组合Justice创作，将于12月11日发行，CD与黑胶唱片预购已同步开放。 https://www.videogameschronicle.com/news/the-official-grand-theft-auto-6-musical-score-by-justice-is-released-in-december-cd-and-vinyl-pre-orders-available-now/
* **[《魔兽世界：永恒》加入手柄支持，被视为暴雪布局Xbox Helix跨平台战略第一步]**（2026-10-29）— 暴雪为《魔兽世界：永恒》（World of Warcraft Forever）加入控制器支持，报道认为这是暴雪为后续Xbox Helix跨平台布局所做的第一步准备。 https://www.videogameschronicle.com/news/world-of-warcraft-forever-controller-support-is-the-first-step-to-playing-anywhere-as-blizzard-prepares-for-xbox-helix/
* **[《南方公园》最新一集插入《GTA6》独家游戏画面]**（2026-10-29）— 动画《南方公园》最新播出集数中插入一段《GTA6》独家游戏画面，作为该作发售前的跨界营销联动之一。 https://www.videogameschronicle.com/news/the-latest-episode-of-south-park-features-exclusive-gta-6-footage-where-a-man-is-hit-in-the-head-with-dog-poo/
* **[韩国对谷歌、苹果开出约4760万美元罚单，指应用内支付政策违规]**（2026-10-29）— 据PocketGamer.biz报道，韩国监管机构对谷歌和苹果合计处以约4760万美元罚款，要求两家公司允许应用内第三方支付链接并修改应用审核流程，该政策将影响包括游戏类应用在内的所有App。 https://www.pocketgamer.biz/south-korea-fines-google-and-apple-476m-over-app-payments/
* **[谷歌Play公布非洲独立游戏基金入选名单，10家工作室获百万美元扶持]**（2026-10-29）— 谷歌Play公布「非洲独立游戏基金」（Indie Games Fund）入选的10家非洲独立游戏工作室名单，总扶持金额达100万美元，用于支持当地团队的游戏开发与业务增长。 https://www.pocketgamer.biz/google-play-selects-10-african-studios-for-1m-indie-games-fund/
* **[11月PS Plus Essential会免游戏公布，《死亡岛2》《古墓丽影IV-VI重制合集》在列]**（2026-10-28）— 索尼公布11月PS Plus Essential档期三款免费游戏，其中包括《死亡岛2》与《古墓丽影IV-VI重制合集》。 https://www.videogameschronicle.com/news/novembers-three-free-ps-plus-essential-monthly-games-include-dead-island-2-and-tomb-raider-4-6-remastered/
* **[《WWE 2K26》最终季票内容上线，新增地震者、台风等四名摔跤手]**（2026-10-28）— 2K公布《WWE 2K26》Ringside Pass最终批内容已上线，新增包括Earthquake、Typhoon等四名经典摔跤手角色。 https://www.videogameschronicle.com/news/wwe-2k26s-final-ringside-pass-launches-today-adding-four-more-wrestlers-including-earthquake-and-typhoon/
* **[约旦独立工作室Dimensions Games Studio运营四年后宣布关闭]**（2026-10-28）— 据PocketGamer.biz报道，约旦游戏工作室Dimensions Games Studio在成立四年后宣布停止运营，为中东地区近期又一家关闭的游戏开发商。 https://www.pocketgamer.biz/jordan-based-dimensions-games-studio-closes-after-four-years/
* **[Unity与投资机构PvX合作，为游戏开发者推出资金扶持计划]**（2026-10-28）— Unity宣布与投资机构PvX Partners合作推出开发者扶持计划，符合条件的开发者可获得Unity Ads广告额度等资金与资源支持。 https://www.pocketgamer.biz/unity-partners-with-pvx-to-offer-funding-for-game-developers/
* **[微软公布最新财季Xbox内容与服务收入同比下滑2%]**（2026-10-28）— 微软公布截至9月的最新财季（2027财年第一财季）业绩，其中Xbox内容与服务业务收入同比下降2%。 https://gamesbeat.com/xbox-content-and-services-revenue-decreased-2-in-september-quarter/
* **[雅虎游戏业务负责人在公司重组裁员中离职]**（2026-10-28）— 据GamesBeat报道，雅虎（Yahoo）游戏业务负责人已在公司近期的架构调整与裁员中离职。 https://gamesbeat.com/yahoos-head-of-games-exits-amid-restructuring-and-layoffs/
* **[Relic公布《英雄连3》剧情DLC「Operation Torch」（火炬行动）]**（2026-10-28）— 开发商Relic Entertainment公布《英雄连3》（Company of Heroes 3）新剧情DLC「Operation Torch」相关内容。 https://gamesbeat.com/relic-unveils-company-of-heroes-3-operation-torch-campaign-dlc/
* **[据报道黑客在GitHub发布伪装PS5模拟器，植入窃取密码的恶意软件]**（2026-10-28）— 据Engadget报道，有黑客在GitHub上传伪装成PS5模拟器的项目，实际捆绑可窃取用户密码等信息的恶意软件，提醒玩家谨慎下载来源不明的模拟器工具。 https://www.engadget.com/2299912/fake-ps5-emulators-on-github-are-spreading-password-stealing-malware/
* **[儿童体感游戏公司Nex Playground与英国NSPCC儿童保护机构达成合作]**（2026-10-28）— 体感游戏硬件公司Nex Playground宣布与英国防止虐待儿童协会（NSPCC）建立合作伙伴关系，共同推进儿童游戏安全相关工作。 https://gamesbeat.com/nex-playground-announces-new-partnership-with-nspcc/
