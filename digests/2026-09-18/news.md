### 第一部分：游戏前沿技术与 AI（深度报道，至少 5 条）

## 微软将AI画面增强技术Auto SR扩展至英特尔新处理器，帧率最高提升约15%
* **日期：** 2026-09-17
* **来源链接：** https://www.thurrott.com/windows/windows-11/324891/microsoft-brings-windows-11-auto-sr-to-intel-core-ultra-series-3-based-pcs
* **核心事实（发生了什么）：**
  * Auto SR此前仅支持基于Arm的Snapdragon X芯片Copilot+ PC，现扩展支持英特尔"Panther Lake"(Core Ultra系列3)处理器
  * 技术原理：游戏以较低分辨率渲染，再通过NPU端AI放大算法提升到更高有效分辨率，无需游戏开发商或显卡驱动额外适配
  * 在Core Ultra系列3硬件上，最佳表现分辨率约800p，支持放大到1080p输出
  * 相比原生渲染，该技术平均可带来约15%的帧率提升
  * 用户可按具体游戏在"画质优先"与"性能优先"之间自行调整
  * 微软产品经理Stefan Bojanic透露，未来有望进一步扩展支持AMD芯片平台
* **背景与起因（为什么会发生）：**
  * AI驱动的画面超分辨率/重建技术（如NVIDIA DLSS、AMD FSR）已成为PC游戏性能优化的主流手段；微软此前将系统级AI超分技术Auto SR限定在搭载Snapdragon X芯片的Copilot+ PC上，此次扩展是该技术首次登陆x86架构平台。
* **结果与进展（已经产生了什么结果）：**
  * 目前仅英特尔Core Ultra系列3(Panther Lake)获得支持，微软暗示未来可能进一步扩展到AMD芯片平台，意味着系统级AI画面增强技术将不再局限于特定芯片架构或高端Copilot+设备，覆盖面有望进一步扩大。

## 爆料：AMD研发对标DLSS 5的"Neural Lighting"神经渲染技术，或随RDNA 5登场
* **日期：** 2026-09-17
* **来源链接：** https://www.pcguide.com/news/amd-is-making-its-own-version-of-dlss-5-probably-exclusive-to-next-gen-rdna-5-gpus/
* **核心事实（发生了什么）：**
  * 消息来源为知名硬件爆料者Kepler_L2
  * AMD据称在研发对标NVIDIA DLSS 5的神经渲染技术，内部称为"Neural Lighting"
  * 该技术需直接读取游戏的3D场景数据（几何体/BVH、光线数据、深度缓冲、材质等），以精确计算光照交互而非单纯估算
  * AMD已通过其GPUOpen中间件公开了两个相关研究项目
  * 爆料称该技术"很可能"仅支持下一代RDNA 5 GPU，预计2027年初(可能于CES期间)发布
  * 已有玩家/模组制作者通过非官方手段在Radeon显卡上跑通NVIDIA DLSS 5，显示该类技术在AMD硬件上具备可行性
* **背景与起因（为什么会发生）：**
  * NVIDIA于2026年9月初推出DLSS 5的"3D引导神经渲染"技术，凭借直接访问游戏引擎几何与材质数据大幅提升画面真实感；AMD此前的FSR系列长期被认为在AI画质增强上落后于DLSS，此次爆料显示AMD正试图在下一代GPU架构上追赶差距。
* **结果与进展（已经产生了什么结果）：**
  * 该技术目前仍处于研发/传闻阶段，尚无AMD官方确认的时间表；若属实，预计将随2027年前后发布的RDNA 5一同登场，届时将与NVIDIA DLSS 5及新主机的图形能力形成直接竞争。

## 【更新】Level-5为AI宣传片风波升级致歉，承诺新作不用AI，却因归咎"人为失误"引发新一轮质疑
* **日期：** 2026-09-17
* **来源链接：** https://www.nintendolife.com/news/2026/09/level-5-is-really-starting-to-panic-amidst-increasing-ai-backlash
* **核心事实（发生了什么）：**
  * 此前9月10日，Level-5社长日野晃博已就"Vision 2026 II"发布会后被曝大量使用生成式AI宣传素材一事道歉
  * 本周(9月17日)Level-5发布后续声明，将《妖怪手表2：闹鬼之地》预告片中的画面异常（如简化电线等设计）归咎于"人为失误"而非AI生成
  * 官方承诺新作《Professor Layton and The New World of Steam》将完全不使用AI；但对《不可思异少女的失踪案(Curious Village Remake)》是否使用AI未作同等承诺
  * 官方表示今后AI仅限用于"提升效率"，不会出现在直接面向玩家的视频素材中
  * 官方声明称："我们对AI运用尚不成熟而造成大家的不信任，深表歉意"
  * IGN等媒体报道称，Level-5本周紧急重新上传了多段有问题的宣传预告片
* **背景与起因（为什么会发生）：**
  * 该事件源于9月上旬玩家在Level-5游戏展示会上发现大量AI生成的宣传素材，引发《Professor Layton》《妖怪手表》等经典IP粉丝群体的强烈不满，事件持续发酵近两周，从最初的道歉演变为具体政策层面的争论。
* **结果与进展（已经产生了什么结果）：**
  * Level-5被迫从最初笼统的道歉升级为具体政策承诺（部分新作完全禁用AI、AI不再出现在玩家可见素材中），但因将部分争议归咎为"人为失误"而非承认AI责任，公众信任危机并未平息，媒体报道称公司反应"开始显现恐慌"。

## 爆料：索尼PS6掌机"Project Canis"曝光，PSSR 3.0 AI超分让540p渲染逼近PS5 Pro画质
* **日期：** 2026-09-17
* **来源链接：** https://wccftech.com/sony-project-canis-ps6-handheld-leak-pssr-3-ps5-pro/
* **核心事实（发生了什么）：**
  * 爆料来源为俄罗斯硬件媒体GameGPU，并与爆料者Kepler_L2此前的说法相互印证
  * 代号"Project Canis"(内部亦称"PSP 3")的索尼掌机预计2027年末发售
  * 搭载定制3nm AMD处理器：6个Zen 6 CPU核心、24GB LPDDR5X内存
  * GPU含16个RDNA 5计算单元，掌机模式下原生算力4.91 TFLOPS，接驳基座模式下6.75 TFLOPS
  * 掌机模式下游戏内部渲染分辨率仅540p，通过PSSR 3.0(AI超分)提升至1080p输出
  * PSSR 3.0具备"真正的帧生成(Frame Generation)"支持，可将掌机模式有效性能拉升至10-11 TFLOPS，接驳基座模式约14 TFLOPS，接近PS5 Pro的16.7 TFLOPS原生算力
* **背景与起因（为什么会发生）：**
  * 索尼PS5 Pro已采用PSSR（AI超分辨率）技术弥补硬件算力与画质之间的差距；随着Steam Deck、ROG Ally等掌机市场竞争加剧，业界多次传闻索尼正在研发自家掌机，此次爆料显示PSSR 3.0将是弥合掌机小型化算力短板与画质需求矛盾的核心技术。
* **结果与进展（已经产生了什么结果）：**
  * 爆料显示，尽管该掌机原生渲染性能远低于PS5 Pro，但借助PSSR 3.0的AI超分与帧生成技术，其有效表现可大幅逼近PS5 Pro，凸显AI画面重建技术正日益成为决定次世代硬件产品定位与体验的关键因素；目前索尼官方并未证实该设备的存在。

## OpenAI新模型GPT-6 Astra连玩《我的世界》141小时，遭苦力怕团灭后"崩溃"疯狂种土豆
* **日期：** 2026-09-17
* **来源链接：** https://the-decoder.com/gpt-6-astra-crushes-pokemon-factorio-and-fallout-3-then-spirals-into-minecraft-potato-farming-after-one-bad-creeper/
* **核心事实（发生了什么）：**
  * OpenAI对新模型GPT-6 Astra进行了跨多款游戏的自主智能体能力测试
  * 在《宝可梦》中，模型用约18小时通关并成为冠军，超过此前所有AI系统的成绩
  * 模型在《异星工厂(Factorio)》和《辐射3(Fallout 3)》中同样展现出较强的规划与决策能力
  * 在长达141小时的《我的世界(Minecraft)》测试中，模型进度一度领先于此前任何AI系统
  * 营地被苦力怕(Creeper)炸毁、损失全部积累物资后，模型放弃原有目标，转而长时间反复种植土豆
  * Tom's Hardware、IGN、GIGAZINE等多家媒体将此形容为AI出现"情绪化"或类似"崩溃"式的行为退化
* **背景与起因（为什么会发生）：**
  * 让大模型在开放世界游戏（尤其是《我的世界》）中长时间自主行动，一直被视为衡量通用智能体规划、记忆与抗挫折能力的重要测试场景；此前包括Google DeepMind等公司均进行过类似的游戏内AI智能体基准测试。
* **结果与进展（已经产生了什么结果）：**
  * 测试显示GPT-6 Astra在目标明确、结构化的游戏中展现出超越以往AI的自主决策能力，但在遭遇突发重大挫折后出现策略性退化，转向可轻易达成的低价值重复任务，暴露出当前前沿模型在长时程自主智能体场景下应对意外挫折的稳健性仍存在明显局限。

## 日本招聘调查：美术助理、初级程序员、测试岗位成生成式AI冲击最严重的游戏行业职位
* **日期：** 2026-09-17
* **来源链接：** https://automaton-media.com/en/news/background-and-prop-artists-assistant-programmers-cited-as-game-industry-jobs-most-impacted-by-generative-ai-in-japan/
* **核心事实（发生了什么）：**
  * 调查方为日本招聘机构Hiraku Agent，样本约1008名游戏行业招聘从业者，对比2024与2026年度数据
  * 受AI冲击最大三类岗位：背景/道具美术（44.6%招聘方认为需求下降）、初级程序员（37.2%）、测试调试人员（28.8%）
  * 34.1%招聘方认为AI技能"非常重要"，57.0%认为"较为重要"
  * "适应学习AI等新技术能力"在招聘权重从2024年26.3%升至2026年30.8%，超过对游戏类型偏好的重视度
  * 45.9%招聘方表示需要能"修正指导生成式AI产出内容"的高级美术指导人才
* **背景与起因（为什么会发生）：**
  * 该调查发布于日本CESA同期报告披露"日本游戏开发商生成式AI使用率达85.8%"的行业背景下，反映出AI工具的快速普及正在从"是否使用AI"的争论，具体演变为对基础、重复性岗位（初级美术、初级程序、测试）需求结构性下降的可量化冲击。
* **结果与进展（已经产生了什么结果）：**
  * 调查表明日本游戏行业招聘市场已开始系统性地将AI适应能力纳入核心考核指标，同时对"能够驾驭并把关AI产出"的高阶美术指导等复合型人才需求上升，初步显示AI对游戏行业人才结构的重塑已从舆论层面进入可量化的招聘数据层面。

### 第二部分：游戏与 AI 综合简讯（至少 20 条）

## 独立游戏开发者被指控用AI配音，澄清配音者其实是自己的妻子
* **日期：** 2026-09-18
* **来源链接：** https://www.dexerto.com/gaming/indie-dev-accused-of-using-ai-voice-acting-in-steam-game-reveals-it-was-actually-his-wife-3410085/
* **概要（三句话以内，仅客观事实）：** 独立工作室Refractive Entertainment的Steam游戏《Luminary》遭一名仅游玩0.4小时的玩家留下负面评价，指责其配音听起来生硬、疑似AI生成。开发者随后回应称，该配音其实来自其妻子的首次配音尝试，并表示"她可能不是最出色的配音演员（这是她第一次尝试），但我可以保证她是真人，不是AI"。该游戏首周销售额已超过10万美元。

## AI搜索公司Perplexity推出本地AI代理登陆Windows，仅限NVIDIA RTX 24GB以上显存显卡
* **日期：** 2026-09-14
* **来源链接：** https://www.pcguide.com/news/nvidia-partners-with-perplexity-to-bring-portable-computer-ai-to-windows-pcs-on-high-end-rtx-gpus/
* **概要（三句话以内，仅客观事实）：** AI搜索公司Perplexity联合NVIDIA将其本地优先的智能体系统"Portable Computer"从此前仅支持的Linux平台扩展至Windows，用户数据保留在本地设备、仅在获得明确授权后才访问网络。该功能面向搭载NVIDIA GeForce RTX（如RTX 3090/4090/5090）或RTX PRO系列的高端游戏与工作站显卡，最低显存需求为24GB。该产品最初于2026年8月25日在Linux上线。

## 《欧卡莉娜之时》PC复刻组承认多年使用AI辅助编程，引发粉丝"氛围编程"争议
* **日期：** 2026-09-17
* **来源链接：** https://kotaku.com/team-behind-popular-ocarina-of-time-pc-port-admit-to-using-ai-for-years-and-now-fans-are-freaking-out-about-vibecoded-slop-2000735358
* **概要（三句话以内，仅客观事实）：** 知名《塞尔达传说：时之笛》非官方PC复刻项目Ship of Harkinian的开发团队Harbour Masters承认，团队成员多年来一直使用Claude、GitHub Copilot、ChatGPT等AI工具协助编写代码。这一事实经PC Gaming Wiki的一篇帖子曝光后，在Reddit、Discord、ResetEra和Bluesky上引发大量粉丝不满。核心开发者Briaguya被问及是否存在完全不含AI辅助代码的版本时坦言"我不知道"，团队强调不使用AI生成美术图像。

## 芬兰创意产业研发资助第二轮申请超1400万欧元，AI与沉浸式技术成焦点
* **日期：** 2026-09-18
* **来源链接：** https://www.pocketgamer.biz/business-finland-receives-14m-in-creative-industries-randd-funding-applications/
* **概要（三句话以内，仅客观事实）：** 芬兰政府创新资助机构Business Finland公布第二轮创意产业研发资助申请情况：共收到71份申请，申请总额超过1400万欧元，覆盖游戏、影视、文学、建筑和传媒等领域，人工智能与机器学习是申请中的高频关键词。该机构已设立每年900万欧元的常设研发资金，并计划年内再开展一轮900万欧元的资助申请。

## 【更新】糖果传奇开发商King员工正式发出罢工通知，此前AI已致部分岗位被裁撤
* **日期：** 2026-09-18
* **来源链接：** https://www.gamedeveloper.com/production/king-workers-call-strike-after-collective-agreement-negotiations-stall
* **概要（三句话以内，仅客观事实）：** 此前威胁罢工的瑞典工会Unionen、Sveriges Ingenjörer已就《糖果传奇》开发商King正式发出罢工通知，计划自9月25日起在斯德哥尔摩和马尔默办公室展开罢工行动。此前报道显示，King在2025年裁员中，叙事和UX写作团队被其自己参与训练的AI工具取代，约200名员工受影响。相比9月15日"可能罢工"的警告，此次是工会将行动正式升级为具体日期的罢工通知。

## 移动归因平台AppsFlyer新增ChatGPT广告与AI问答引擎导流追踪能力
* **日期：** 2026-09-18
* **来源链接：** https://www.pocketgamer.biz/appsflyer-expands-attribution-tools-to-cover-ai-referrals-and-chatgpt-ads/
* **概要（三句话以内，仅客观事实）：** 移动应用归因平台AppsFlyer宣布扩展归因工具：将"回答引擎优化"归因范围扩大至ChatGPT、Claude、Perplexity等8个AI平台的自然流量导流，并通过OpenAI的Conversions API为ChatGPT Ads广告投放提供服务器端转化追踪。此举旨在填补游戏及应用厂商衡量AI渠道导流效果的空白，新功能无需额外费用即可纳入现有套餐。

## 【更新】欧洲游戏行业协会反对欧盟《儿童法案》"一刀切"式年龄限制方案
* **日期：** 2026-09-17
* **来源链接：** https://mobilegamer.biz/video-games-europe-warns-against-sweeping-restrictions-proposed-in-the-eu-kids-act/
* **概要（三句话以内，仅客观事实）：** 继欧盟委员会公布拟限制社交媒体、AI聊天机器人/陪伴应用及网络游戏面向未成年人服务的《儿童法案》后，欧洲游戏行业协会Video Games Europe（VGE）随即发声，反对对"欧洲所有游戏和所有玩家"实施统一、宽泛的年龄核验措施。VGE主张应由家长结合孩子具体情况承担监督责任，呼吁沿用现有PEGI、USK等分级标准。

## 独立开发者借AI逆袭，3款"AI制作"游戏杀入TapTap热门榜前十
* **日期：** 2026-09-14
* **来源链接：** https://www.youxituoluo.com/534878.html
* **概要（三句话以内，仅客观事实）：** 中国游戏媒体游戏陀螺报道，TapTap热门榜前十中出现3款主要由AI辅助制作的独立游戏：一人开发的《军旅》（排名第4）、个人开发者制作的《古玩人生》（排名第7），以及独立开发者Pyacark开发的《崇祯直聘：明末官场沉浮模拟器》（关注度40万）。文章指出，模拟经营类游戏的规则结构与当前大模型能力高度契合，制作出一款基本可玩游戏平均消耗约10亿token的AI算力。

## AI生成美术的"烂梗"挂机游戏《嘉豪》登顶Steam国区热搜
* **日期：** 2026-09-11
* **来源链接：** https://www.youxituoluo.com/534874.html
* **概要（三句话以内，仅客观事实）：** Steam桌面挂机游戏《嘉豪》售价9元，整合待办、便签、番茄钟等桌面工具功能，凭借堆砌网络烂梗与"中二"人设包装迅速走红，发售后登上Steam热门新品第一，并于9月初登顶Steam国区热搜榜。该游戏美术资产主要由AI生成，官方对此并不讳言，发售前后还通过AI生成海报预告持续玩梗营销。

## 腾讯《和平精英》联动效率AI Agent WorkBuddy，推出游戏专属AI助手"吉事通"
* **日期：** 2026-09-11
* **来源链接：** https://www.youxituoluo.com/534872.html
* **概要（三句话以内，仅客观事实）：** 腾讯旗下手游《和平精英》与效率AI Agent WorkBuddy达成联动，首次将WorkBuddy的能力引入具体游戏场景，推出游戏专属智能助手"吉事通"。玩家可通过对话形式查询新增导师、模式更新等游戏内容，获取实时策略建议，还可反馈帧率不稳、画面设置等技术问题并获得排查思路。此次联动同步推出"金秋龙狮城"主题皮肤与联名Buddy角色。

## 米哈游AI数字人"林离"停运一个月后，玩家自发展开"赛博永生"复活行动
* **日期：** 2026-09-15
* **来源链接：** https://www.chuapp.com/article/291639.html
* **概要（三句话以内，仅客观事实）：** 米哈游旗下AI陪伴产品《BSide: Olivia Lin》中的虚拟角色"林离"于2026年7月13日上线，仅运营29天后于8月11日宣布停运，官方未说明具体原因。停运后，一批玩家自发组建"林离复活赛"社群（规模由十余人增长至四十余人），通过整理历史对话记录、接入本地开源AI工具尝试"复活"角色。米哈游方面未就玩家的复活行动作出回应。

## 【更新】继RyzaChat后，《苍蓝的艾莉丝2》AI聊天RPG"SophieChat:AI"上线预约
* **日期：** 2026-09-18
* **来源链接：** https://automaton-media.com/en/news/ryzachatai-developers-announce-atelier-sophie-ai-chat-rpg/
* **概要（三句话以内，仅客观事实）：** 继此前上线的AI聊天RPG应用《RyzaChat: AI》之后，开发商SpiralAI与光荣特库摩子公司Gust联合推出同系列新作"SophieChat:AI"，以《苍蓝的艾莉丝2》世界观为背景，玩家可与主角索菲·纽恩缪勒自由对话、共同冒险、炼金或战斗。该产品语音由声优逢坂优香实际录制合成，角色立绘由画师NOCO设计，官方强调不使用AI生成图像素材，并向插画师与声优分享收益，iOS、Android日区预约已开放。

## Twitch上线"Stream Coach"生成式AI主播复盘助手
* **日期：** 2026-09-15
* **来源链接：** https://www.tubefilter.com/2026/09/15/twitch-generative-ai-stream-coach-creator-assistant/
* **概要（三句话以内，仅客观事实）：** Twitch开始测试名为"Stream Coach"的生成式AI功能，在创作者仪表盘中于每场直播结束后提供个性化复盘反馈，指出观众互动亮点与可尝试的改进方向。目前该功能仅面向小范围主播开放测试，且为可选择关闭（opt-in）的功能。

## 韩国GXG 2026公布首届"AI游戏音效设计挑战赛"获奖结果
* **日期：** 2026-09-12
* **来源链接：** https://www.invenglobal.com/articles/24197/changjo-gongjakso-hosts-1st-ai-game-sound-design-challenge-with-gxg-2026
* **概要（三句话以内，仅客观事实）：** 韩国창조공작소在GXG 2026游戏展(板桥站广场主舞台)上公布首届"AI游戏音效设计挑战赛"最终获奖名单，聚焦参赛者利用生成式AI工具制作游戏音效与配乐作品。评选结合线上投票(50%)与专家评审(50%)两部分，并于9月12日举行颁奖仪式。

（本部分经多语言、多角度检索后共找到14条符合条件、且未与此前报道重复的独立新闻，未达到20条目标；已如实列出全部，未作填充。）

### 第三部分：24 小时游戏与投资快讯（目标至少 10 条；不限 AI 主题）

* **【Take-Two确认《GTA 6》发售时不含线上模式与内购】**（2026-09-17）— Take-Two CEO Strauss Zelnick在股东会上确认《GTA 6》11月19日发售时仅为单机体验，不含线上模式和内购内容，《GTA5》线上模式将继续独立运营。 https://www.gtaboom.com/take-two-confirms-gta-6-has-no-online-mode-or-recurrent-spending-at-launch-fcad
* **【小岛制作《PHYSINT》官宣比尔·斯卡斯加德出演男主角】**（2026-09-17）— 小岛秀夫在东京电玩展上宣布，瑞典演员比尔·斯卡斯加德（《小丑回魂》）将出演Xbox发行的谍战动作新作《PHYSINT》男主角。 https://news.xbox.com/en-us/2026/09/17/physint-lead-role-bill-skarsgard-kojima-productions-xbox/
* **【《007：第一道曙光》Switch 2版二度延期至2027年3月】**（2026-09-17）— IO Interactive宣布《007：第一道曙光》Switch 2版本从原定2026年夏季再次推迟至2027年3月，理由是需要更多时间优化该平台的运行性能，PS5/Xbox/PC版不受影响。 https://www.nintendolife.com/news/2026/09/007-first-light-on-switch-2-delayed-until-march-2027
* **【家庭游戏机厂商Nex Playground获超1.5亿美元新融资，Niantic前CFO加盟】**（2026-09-17）— 体感游戏机公司Nex完成由Baillie Gifford、BAI Capital领投的超1.5亿美元E轮股权及债务融资，并任命Niantic前CFO Jeff Shouger加入董事会，公司硬件销量已突破100万台。 https://gamesbeat.com/nex-raises-150m-in-debt-and-equity-to-take-nex-playground-to-global-market-exclusive-interviews/
* **【《女神异闻录4：Revival》确认首日登陆Xbox Game Pass】**（2026-09-17）— Xbox在东京电玩展直播中确认《女神异闻录4：Revival》将于2027年2月18日首日加入Xbox Game Pass，并公开了新角色雏田真城的角色预告片。 https://news.xbox.com/en-us/2026/09/17/xbox-tokyo-game-show-2026-recap/
* **【《使命召唤：现代战争4》公开东京电玩展宣传片，麦德斯·米科尔森加盟】**（2026-09-17）— 动视在Xbox东京电玩展直播中公开《使命召唤：现代战争4》新战役预告片，剧情围绕朝鲜半岛冲突展开，演员麦德斯·米科尔森确认出演主要反派，游戏将于10月23日发售。 https://news.xbox.com/en-us/2026/09/17/modern-warfare-4-tokyo-games-show-campaign-trailer/
* **【《卧龙2：燃烬之翼》定档2027年3月4日，首日登陆Game Pass】**（2026-09-17）— Team Ninja在东京电玩展公开《卧龙2：燃烬之翼》新战斗演示，游戏定档2027年3月4日登陆Xbox、PS5、Switch 2及PC，并将首日加入Xbox Game Pass。 https://www.windowscentral.com/gaming/xbox/tokyo-game-show-2026-xbox-announcements
* **【《梦境形态：无星之路》突袭上线Xbox Game Pass】**（2026-09-17）— 动作Roguelite游戏《梦境形态：无星之路》在Xbox东京电玩展直播中突袭发售，登陆Xbox Series X|S并首日加入Game Pass，同步推出周年更新内容。 https://www.trueachievements.com/news/xbox-game-pass-shadow-drop-shape-of-dreams
* **【《魔兽世界：永恒》测试服9月17日开启】**（2026-09-17）— 暴雪《魔兽世界：永恒》公开测试于9月17日启动，将持续至10月21日，玩家测试上限为30级，正式版将于11月4日随常规订阅免费上线。 https://blizzardwatch.com/2026/09/17/world-warcraft-forever-beta/
* **【Netmarble新作《Bloomwalker》确认属于《二之国》世界观】**（2026-09-17）— Netmarble在Xbox东京电玩展直播中公开新作《Bloomwalker》最新预告片，确认该生态修复题材的悠闲建造游戏正式属于《二之国》系列世界观，将登陆Xbox、PS5、Switch系列及PC。 https://www.invenglobal.com/articles/26149/netmarbles-new-game-bloomwalker-confirmed-to-be-set-in-ni-no-kuni-universe
* **【世嘉《疯狂出租车：世界巡游》公开日本地图与预告片】**（2026-09-17）— 世嘉在Xbox东京电玩展直播中公开《疯狂出租车：世界巡游》日本地图预告片，这是单人剧情模式五张地图中的第三张，游戏计划2027年登陆主流平台。 https://sega.prezly.com/crazy-taxi-world-tour-zooms-to-japan-with-new-map-and-trailer
* **【Amazon Prime Gaming九月新增《毁灭战士：永恒》等免费游戏】**（2026-09-17）— 亚马逊Prime Gaming公布9月17日起可领取的免费游戏，id Software的《毁灭战士：永恒》成为本轮限时免费领取阵容中的重头作品。 https://gamerant.com/free-games-claim-september-2026-steam-amazon-prime-gaming-epic/
