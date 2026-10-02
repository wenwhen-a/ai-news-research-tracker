### 第一部分：游戏前沿技术与 AI（深度报道，至少 5 条）

## Krafton发布PUBG Ally技术报告:55页论文揭示AI队友的训练过程与真实玩家反馈
* **日期：** 2026-09-29
* **来源链接：** http://www.invenglobal.com/articles/26592/built-a-teammate-got-a-chat-partner-kraftons-first-scorecard-for-pubg-ally
* **核心事实（发生了什么）：**
  * Krafton在arXiv上发布了一份长达55页的技术报告,详细披露了由NVIDIA ACE驱动的AI队友'PUBG Ally'的开发过程
  * 训练数据采集自韩国一家网吧连续28天的实测,1,046名拥有10小时以上PUBG经验的成年玩家参与,累计进行38,956场对局,期间测试了六个迭代版本的端侧模型
  * 覆盖17种语言、141个国家的live service调研显示,整体净推荐值(NPS)为+25.1个百分点;但细分维度中,战斗技巧评分仅2.58/5(各项指标中最低),情景判断2.88/5,反应速度2.93/5,指令执行2.99/5
  * 玩家认知调查显示:50%的玩家将Ally视为'工具',31.5%视为'伙伴',仅18.5%认为它达到了Krafton最初设想的'队友'定位;51%的玩家认为其最大优点是'提供情报/战术建议',28%认为是'聊天对象'
  * 技术架构完全在端侧(用户PC本地)运行语言模型、语音识别与语音合成;云端API每场对局成本为3.70-7.10美元,端侧成本为0美元;端侧响应速度为1.6秒,云端为3.4秒
  * 推荐运行配置为8GB显存,量化后的模型仅占用1.6-2.1GB显存
* **背景与起因（为什么会发生）：**
  * PUBG Ally是Krafton与NVIDIA ACE合作开发的'可共同游玩角色'(Co-Playable Character,CPC),区别于传统NPC,能够在语音交流中自主推理、保持记忆并与玩家协同作战。该项目此前已经历多轮公开测试,包括2026年6月17日至7月1日面向全球玩家开放的两周公测。此次发布的技术报告是Krafton首次完整公开该项目的量化评估数据与开发细节,契合公司整体转向'AI优先'战略的方向。
* **结果与进展（已经产生了什么结果）：**
  * 报告显示NPS从测试初期约+8个百分点提升至后期约+36个百分点,说明持续迭代确实改善了玩家体验;但实测数据也暴露出Ally在'并肩作战'的战斗表现上仍弱于其作为'情报伙伴'的表现,与团队最初设想存在落差。Krafton表示下一步计划开发全双工(full-duplex)语音模型以提升交流自然度,并将相关设计原则延伸应用到旗下机器人子公司Ludo Robotics的Ludi 0.1机器人项目中。

## 索尼推出QSSR技术,让标准版PS5也能获得AI超分辨率画质提升
* **日期：** 2026-10-01
* **来源链接：** https://blog.playstation.com/2026/10/01/ai-upscaling-is-coming-to-ps5/
* **核心事实（发生了什么）：**
  * 索尼正式发布Quick Spectral Super Resolution(QSSR),为标准版PS5(非Pro版本)主机带来全新AI超分辨率升级技术
  * QSSR源自索尼与AMD联合研发的Project Amethyst计划,技术血统可追溯至此前仅限PS5 Pro使用的PlayStation Spectral Super Resolution(PSSR)
  * 该技术采用精简版神经网络架构,并针对标准版PS5的算力进行了手动调优,可逐像素分析画面并提升细节表现与时间稳定性
  * 首批支持QSSR的游戏为《Marvel's Wolverine》与《Ghost of Yōtei》,两者已于10月1日通过补丁加入QSSR作为可选画质选项
  * Insomniac Games表示QSSR'为画面带来更多像素级清晰度与稳定性,凸显出更多细节';Sucker Punch Productions表示QSSR'能够精细还原角色与场景细节,实现了PS5此前从未有过的时间稳定性'
  * 索尼将PSSR称为PS5 Pro上的'黄金标准',QSSR则是让标准版PS5用户获得接近效果的折中方案
* **背景与起因（为什么会发生）：**
  * PS5 Pro此前凭借专用硬件独占PSSR AI超分辨率技术,标准版PS5用户长期缺乏对等的画质优化手段,这也是PS5 Pro相较标准版的核心卖点之一。随着索尼与AMD在Project Amethyst计划下的持续合作,双方得以将神经网络模型进一步精简压缩,使其能够在算力较弱的标准版PS5硬件上实时运行,从而部分弥合两款主机间的画质差距。
* **结果与进展（已经产生了什么结果）：**
  * 《Marvel's Wolverine》在城市等细节密集场景中获得'极佳'的画质提升,而原本画质表现已经较好的《Ghost of Yōtei》提升幅度相对有限。索尼表示将把QSSR作为标准功能开放给PlayStation第一方与第三方开发者用于未来新作,预计后续会有更多游戏陆续加入支持列表。

## 开发者用Claude AI五天打造《辐射》同人游戏,遭Bethesda发函下架
* **日期：** 2026-10-02
* **来源链接：** https://frvr.com/blog/bethesda-quickly-kills-ugly-ai-generated-fallout-new-york-game-as-ai-slop-bros-continue-to-forget-how-copyright-works
* **核心事实（发生了什么）：**
  * 开发者Chris First在社交媒体上称,他指挥Anthropic的Claude Opus 5.5模型及'一支AI智能体团队',在约5天内完成了一款浏览器端、完全由AI生成的3D《辐射》同人游戏'Fallout: New York'(域名Fallout.nyc)
  * 该游戏包含任务系统、对话树、VATS战斗系统与可用的Pip-Boy界面;建筑、武器、角色面部与音效等全部资产均由代码生成,未使用任何现成贴图或音频文件
  * 游戏存在大量技术问题,包括动画错误、角色手部模型异常('mutated player fists')、角色升级时游戏死锁等
  * 该项目在X(Twitter)上获得350万次浏览后,Bethesda母公司ZeniMax以涉及'受版权保护内容'及商标侵权为由,向Fallout.nyc域名发出DMCA停止函
  * ZeniMax表示必须'监控并执行针对未经授权侵权使用的维权行动',以保护自身知识产权
  * Chris First随后在社交媒体回应称'西装革履的人介入了,乐趣到此为止',并反问Bethesda'不如你们自己做一款辐射游戏,我就不用做了'
* **背景与起因（为什么会发生）：**
  * 该项目是近期'vibe coding'(氛围编程,即通过向AI描述需求、由AI自动生成代码与资产的开发方式)热潮中的代表性案例,反映出生成式AI工具已能在数天内独立产出具备基本可玩性的3D游戏原型,也再度凸显了同人创作与版权方之间长期存在的法律张力。
* **结果与进展（已经产生了什么结果）：**
  * Fallout.nyc网站已被下线,开发者原定的开源发布计划也随之放弃。多数玩家对下架结果表示支持,部分评论调侃称'没想到这些搞AI废物的人,反倒让人站到了版权执法这一边'。

（本窗口内经过严格去重与验证后，仅找到 3 条达到第一部分深度报道标准的独立新项目；过去一周游戏+AI 深度报道角度的其他重大事件已被此前每日简报覆盖，三个检索子代理及两轮补充检索均未能找到更多合格新项目。）

### 第二部分：游戏与 AI 综合简讯（至少 20 条）

## NVIDIA专利曝光:AI聊天助手可帮助开发者诊断GPU性能问题
* **日期：** 2026-09-25
* **来源链接：** https://www.eteknix.com/nvidia-patents-ai-chat-assistant-to-help-developers-optimize-gpu-performance/
* **概要（三句话以内，仅客观事实）：** NVIDIA注册了一项专利,描述一款连接大语言模型(LLM)与性能分析工具的AI聊天助手,能自动读取GPU性能报告、用Python等脚本提取数据、定位性能瓶颈并用通俗语言向开发者解释问题所在。相比此前面向普通玩家、提供画质设置建议的Project G-Assist,该专利面向开发者,旨在帮助缺乏专职优化团队的中小型工作室更高效诊断GPU性能问题,但不会自动修改代码,仅作为辅助决策的'副驾驶'。

## 索尼专利:AI控制器辅助系统可为残障玩家自动补全操作输入
* **日期：** 2026-09-30
* **来源链接：** https://www.retrohandhelds.gg/sonys-ai-powered-controller-assistant-could-help-disabled-players-if-it-ever-ships/
* **概要（三句话以内，仅客观事实）：** 索尼递交了一项专利(申请提交于9月17日),描述一套利用AI实时监测玩家动作并据此生成对应手柄输入的系统,可学习玩家个人动作模式、适配特定手柄,用于弥补手部可及范围不足、摇杆漂移或因残障无法完成完整按键动作等问题。系统支持本地或云端两种处理方式,并计划在多人游戏中加入屏幕提示以标明辅助功能启用状态,避免被误判为'开挂'。报道指出索尼历史上不少专利最终未能落地为实际产品,该技术目前仍停留在专利阶段。

## 第三方工具Borderless Gaming实现'类DLSS 5'效果,让老款NVIDIA显卡也能体验神经渲染
* **日期：** 2026-09-30
* **来源链接：** https://wccftech.com/borderless-gaming-nvidia-dlss-5-quantized-unsupported-gpus/
* **概要（三句话以内，仅客观事实）：** 第三方工具Borderless Gaming开发者Andrew Sampson推出一套独立于NVIDIA官方软件运行的'DLSS 5风格'神经渲染实现,通过在合成器层级截取游戏画面并经GPU效果管线处理,无需替换游戏DLL或修改游戏文件。该实现对神经网络模型进行量化精简,使其能在官方DLSS 5仅支持的RTX 50系列之外的老款显卡(如RTX 3090)上运行,约可达30帧/秒,但开发者强调这只是'受DLSS 5启发'的效果,并非NVIDIA官方的3D引导神经渲染技术。

## 韩国应用商店ONE Store全面开放'AI游戏'专区,接受所有开发者提交
* **日期：** 2026-09-28
* **来源链接：** http://www.invenglobal.com/articles/26558/one-store-fully-opens-ai-game-registration
* **概要（三句话以内，仅客观事实）：** 韩国移动应用分发平台ONE Store宣布全面开放此前于8月小范围测试的'AI Games'专区,接受所有开发者通过其ONEconsole开发者中心提交作品,包括通过AI对话、无需编程经验开发的游戏,并优先推荐无需安装的HTML5网页游戏。ONE Store CEO Henry Chang表示公司将'积极拥抱'AI游戏快速涌入市场的趋势,该专区将于10月初调整至应用底部菜单栏以提升可见度,并计划在韩国本土站稳后逐步向全球扩展。

## '氛围编程'(Vibe Coding)催生独立游戏抄袭潮,开发者担忧创意被AI快速复刻
* **日期：** 2026-09-28
* **来源链接：** https://www.msn.com/en-xl/gaming/general/indie-games-flooded-by-ai-generated-imitations-via-vibe-coding/ar-AA2d6vQc
* **概要（三句话以内，仅客观事实）：** 据Chosun Ilbo报道,越来越多业余开发者利用AI'氛围编程'(vibe coding,即通过向AI描述需求自动生成代码)工具,在原创者完成作品前就迅速复制其尚处开发阶段的独立游戏创意;瑞典独立开发者Freya Holmér今年3月分享的一个Tetris新玩法创意,随后就被他人用AI工具复刻。有开发者表示'只要在网上发点什么,就会开始焦虑',担忧成果被迅速抄袭,这股趋势也与近期热议的'用AI把《我的世界》玩法塞进《艾尔登法环》'等混搭复刻现象相呼应。

## Bake3D 推出 AI 工作流,可将图片或文字提示一键转化为带骨骼绑定与动画的 3D 角色
* **日期：** 2026-09-29
* **来源链接：** https://news.marketersmedia.com/bake3d-introduces-ai-workflow-for-creating-rigged-and-animated-3d-characters/89204608
* **概要（三句话以内，仅客观事实）：** AI 3D 工具公司 Bake3D Inc.(由 Marcus Garcia 领导)发布基于浏览器的工作流,可将图片、渲染图、照片或文字提示自动转化为贴图完整、骨骼绑定并带动画的 3D 资产,涵盖建模隐藏面、构建骨骼结构、分配蒙皮权重及生成动作等此前需人工完成的步骤。该工具不仅支持人形角色,还能处理动物、带翼生物、载具、机械及混合设计等多种形态,并可导出为 GLB 或 FBX 格式,兼容 Unreal Engine 5、Unity、Blender 和 Godot 等主流引擎,同时提供 API 及 Model Context Protocol 工具供 AI 助手调用。创始人 Garcia 表示,其定位是为原型、预可视化和过场动画提供"可供检查、动画化并继续打磨"的起点,而非最终成品级资产。

## GamesIndustry.biz:多名从业者反映 AI 工具并未节省时间,反而为游戏公司带来更多工作量
* **日期：** 2026-10-02
* **来源链接：** https://www.gamesindustry.biz/quite-often-its-given-me-more-to-do-why-ai-might-be-creating-more-work-for-games-companies-rather-than-saving-time
* **概要（三句话以内，仅客观事实）：** 游戏行业媒体 GamesIndustry.biz 发表报道称,在其近期活动(围绕 GamesIndustry.biz HR Summit 2026 的讨论)中,多名游戏行业从业者反映生成式 AI 工具带来的效率提升被额外产生的工作量所抵消,标题引用的受访者原话为"很多时候它反而给了我更多事情要做"(Quite often it's given me more to do)。报道探讨了 AI 工具在游戏公司实际应用中,承诺的"节省时间"效果与一线从业者真实体验之间存在落差的现象。

## 米哈游创始人刘伟:目标2-3年内进入国产大模型第一梯队,未来三年AI投入上限1000亿元
* **日期：** 2026-09-28
* **来源链接：** https://m.thepaper.cn/detail/34164101
* **概要（三句话以内，仅客观事实）：** 9月28日,米哈游创始人兼总裁刘伟在2027校园招聘宣讲会上海交通大学专场上表示,希望米哈游在2到3年内成为国产大模型团队中举足轻重的一员。他重申此前表态,公司未来三年在AI领域的投入上限为1000亿元人民币,目标是通过AI实现游戏体验的"千人千面"个性化。

## 《全面战争:战锤3》人气模组作者为反制AI未授权转载自毁模组
* **日期：** 2026-10-02
* **来源链接：** https://news.17173.com/content/10022026/190653502.shtml
* **概要（三句话以内，仅客观事实）：** 《全面战争:战锤3》知名模组"SFO: Grimhammer III"作者Venris于10月2日宣布,因该模组被他人利用AI制作未授权衍生版本并大量转载,已故意破坏模组使其无法在未授权转载版本中正常运行。作者称该模组凝聚近十年心血,若情况持续将考虑把模组设为私密,社区内多数玩家对此表示支持。

## 美国求职平台Handshake联合OpenAI推出"AI技能工作室",首期挑战为用AI开发多人游戏
* **日期：** 2026-10-02
* **来源链接：** https://www.sohu.com/a/1083361789_121124337
* **概要（三句话以内，仅客观事实）：** 大学生求职平台Handshake与OpenAI合作推出项目式学习项目"AI Skills Studio",首期挑战要求学生零代码基础、仅依靠ChatGPT独立构建一款可运行的多人游戏。学生需与ChatGPT协作完成需求定义、开发、测试与迭代,成品将以可分享房间码形式发布,并作为求职作品集供雇主查看。

## 《战争机器:E日》出现民间AI俄语配音,质量被指接近真人配音演员
* **日期：** 2026-10-02
* **来源链接：** https://ixbt.games/en/news/2026/10/02/pokazali-geimplei-gears-of-war-e-day-s-russkoi-ozvuckoi-ii-lokalizaciia-napominaet-rabotu-akterov-dubliaza.html
* **概要（三句话以内，仅客观事实）：** 俄罗斯神经网络配音项目MDRevoice于10月2日发布了新上线游戏《战争机器:E日》的非官方AI俄语配音演示,相关试玩片段已在其YouTube频道公开,报道称配音质量"接近真人配音演员的水准"。此前该项目也曾为《控制:共鸣》制作过俄语AI配音。

（本窗口内经过严格去重与验证后，仅找到 11 条合格简讯；过去一周的游戏+AI 新闻已被第一部分深度报道及此前每日简报大量覆盖，三个检索子代理及两轮补充检索均未能找到更多合格新项目，未进行任何凑数。）

### 第三部分：24 小时游戏与投资快讯（目标至少 10 条；不限 AI 主题）

* **[Bungie联合创始人Jason Jones创立跨媒体工作室Stone Kite]**（2026-10-01）— Bungie联合创始人、《光环》(Halo)与《命运》(Destiny)缔造者Jason Jones与作家Margaret Stohl共同创立全新跨媒体工作室Stone Kite,致力于打造跨游戏、漫画、影视等多种媒介的原创世界观,Stohl将出任公司CEO。 https://www.ign.com/articles/jason-jones-co-creator-of-halo-and-destiny-and-co-founder-of-bungie-announces-new-studio
* **[AppLovin就Ad Quality SDK对Unity提起法律诉讼]**（2026-10-01）— AppLovin对Unity提起法律诉讼并寻求临时禁令,指控Unity的Ad Quality SDK收集其广告业务数据(含创意素材、用户、设备、收入及互动信息)并用于训练竞争模型;Unity回应称Ad Quality只是用于防止不当广告的免费小工具,反指AppLovin自家Ad Review工具更具侵入性。 https://www.pocketgamer.biz/applovin-takes-legal-action-against-unity-over-ad-quality-sdk/
* **[网易游戏Club与EBANX合作拓展拉美本地化支付]**（2026-10-01）— 网易游戏Club与支付公司EBANX达成合作,将在拉美五国推出Pix、SPEI、PagoEfectivo、Mercado Pago等本地化支付方式,该战略预计今年将为相关游戏业务带来84亿美元收入,其中巴西市场预计贡献38亿美元。 https://www.pocketgamer.biz/netease-games-club-partners-with-ebanx-projecting-84bn-in-latam-revenue-this-year/
* **[HoYoLAND 2026线下嘉年华在韩国开幕]**（2026-10-02）— HoYoverse旗下线下粉丝活动HoYoLAND 2026于10月2日至5日在韩国一山KINTEX展览中心举行,《原神》《崩坏:星穹铁道》《绝区零》《崩坏3》《未定事件簿》等旗下游戏IP同台展出。 https://www.invenglobal.com/articles/25379/hoyoland-2026-to-be-held-at-kintex-on-october-2
* **[迪士尼总裁回应收购Epic Games传闻:目前没有计划]**（2026-10-02）— 迪士尼总裁兼首席创意官Dana Walden在接受彭博社采访时回应此前有关迪士尼可能收购Epic Games的传闻,表示公司"目前"并未与Epic Games进行收购谈判,但确认双方对现有合作关系满意,并计划在未来两年推进更多合作项目;此前迪士尼已于2024年向Epic Games投资15亿美元。 https://gameworldobserver.com/2026/10/02/disney-is-not-planning-to-purchase-epic-games-at-least-not-at-the-moment
* **[《真·三国无双》制作人谈不愿制作更多重制版]**（2026-10-02）— 《真·三国无双》制作人Tomohiko Sho表示,鉴于自己已年过五十、不确定还能制作多少款游戏,相比重制版他更希望投入新作或系列续作的开发。 https://www.videogameschronicle.com/news/dynasty-warriors-producer-says-hed-rather-not-make-more-remasters-because-he-doesnt-know-how-many-more-games-he-has-left/

（过去 24 小时内经核实的合格快讯共 6 条，低于 10 条的目标但高于下限要求；该目标为软性目标而非硬性下限。）
