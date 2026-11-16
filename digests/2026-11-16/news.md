### 第一部分：游戏前沿技术与 AI（深度报道，至少 5 条）

## 百度文心发布 ERNIE 5.5 Flash Preview：专项训练支持游戏开发，适配 Unity、Unreal、Godot 等引擎
* **日期：** 2026-11-11
* **来源链接：** https://www.xinhuanet.com/tech/20261111/183aa161e70b4942b622e10b5e3da605/c.html （另见：https://tech.ifeng.com/c/8xxwDIS2DX4）
* **核心事实（发生了什么）：**
  * 11 月 11 日发布，为此前 11 月 5 日开源的 ERNIE 5.5 Flash Base 基座模型之后的首个后训练（post-trained）版本。
  * 总参数 2800 亿，单 Token 激活 140 亿参数，支持最长 100 万 Token 上下文，官方称生成速度超 200 tokens/秒。
  * 官方称模型针对游戏开发做了专项训练，适配 Unreal Engine、Unity、Godot、Cocos 等主流开发工具，可依据用户创意完成游戏设计、功能制作和场景搭建。
  * 3D 建模能力经过针对 Blender、CAD 等专业软件的专项训练，可从文本推断形状、比例与空间关系并进行程序化建模。
  * 模型 API 已在百度智能云千帆平台开放调用，模型权重计划 11 月 25 日前向全球开源社区发布。
* **背景与起因（为什么会发生）：**
  * 该版本基于百度 11 月 5 日刚开源的 ERNIE 5.5 Flash Base 基座模型构建，是文心 5.5 系列的首个后训练版本。
  * 官方将其定位为中间版本，说明可能存在因训练不充分导致的能力缺陷，将在后续正式版中优化。
* **结果与进展（已经产生了什么结果）：**
  * 模型 API 已可在千帆平台实际调用，为开发者提供了游戏原型生成等场景的接入入口。
  * 权重开源计划（11 月 25 日前）将使该模型的游戏开发与 3D 建模能力接受全球开发者社区的进一步验证。

注：经过对西方/全球及中文games+AI信源的广泛搜索（两路独立调研累计超过 200 次网页检索/核实），第一部分本期仅找到 1 条符合"深度报道"标准、且未与此前 14 天内已发布内容构成同一事件的游戏+AI 前沿新闻；其余候选均系此前简报已覆盖的同一事件（如 NVIDIA DLSS 5 系列、腾讯"鹅次元"、Epic Unreal 5.9 等），或缺乏可引用的一级/二级信源。未进行任何捏造或凑数。

### 第二部分：游戏与 AI 综合简讯（至少 20 条）

## 腾讯总办发文号召"AI 时代再创业"，提及游戏团队与混元模型协同设计
* **日期：** 2026-11-16
* **来源链接：** https://www.ithome.com/1/027/509.htm
* **概要（三句话以内，仅客观事实）：** 腾讯文化团队 11 月 16 日发布内部信《总办号召AI时代再创业，"心态归零"》，源自公司 28 周年 LinkTime 高管对谈，号召各业务单元围绕 AI 重构、加大投入、推行扁平化组织并打破内部壁垒。信中提到游戏、金融、安全等团队已将各自业务能力与混元（Hy）模型进行协同设计（Co-Design），并借此提升了混元模型的能力。腾讯强调组织调整并非 50% 裁员，而是约一半人力转向新业务方向。

## 字节跳动火山引擎全面开放 Seedance 2.5 4K 视频生成模型 API
* **日期：** 2026-11-16
* **来源链接：** https://www.ithome.com/1/027/736.htm
* **概要（三句话以内，仅客观事实）：** 字节跳动旗下火山引擎 11 月 16 日宣布，此前 10 月 23 日发布的 Seedance 2.5 4K 视频生成模型 API 服务正式面向开发者与企业全面开放调用。该模型支持 480P 草稿模式用于预览分镜与运镜，确认后生成 4K 最终版本，并支持 10-bit 色深。官方称其在还原人物表情、细微动作，以及保持参考素材画质与清晰度方面做了针对性优化，主要面向影视与视频内容生产场景。

## 腾讯混元发布 Hy4 flash：单任务成本降至 Hy4 约 5%，已接入元宝、企业微信等场景
* **日期：** 2026-11-16
* **来源链接：** https://www.ithome.com/1/027/630.htm
* **概要（三句话以内，仅客观事实）：** 腾讯混元 11 月 16 日发布 Hy4 flash 模型，总参数 2240 亿（含 640 亿 Engram 参数），单 Token 激活 120 亿参数，支持多模态输入与 100 万 Token 上下文。官方称其在 WorkBuddy WorkIndex 基准上单任务成本约为 Hy4 preview 的 1/13、Hy4 的 1/20，解码速度超 150 tokens/秒。该模型已上线腾讯云 TokenHub、WorkBuddy、元宝、企业微信、QQ、ima 等产品，后续将接入 OpenRouter 并计划开源。

## 腾讯混元发布 Hy Realtime 实时语音大模型，支持点歌演唱与工具调用
* **日期：** 2026-11-13
* **来源链接：** https://www.ithome.com/1/026/825.htm
* **概要（三句话以内，仅客观事实）：** 腾讯混元 11 月 13 日发布实时语音模型 Hy Realtime，已接入元宝语音通话及腾讯客服场景，腾讯云 API 即将开放。该模型可根据对话上下文自主判断是否需要联网搜索，并与腾讯音乐天琴/灵音 AI 团队联合开发了按歌手、专辑、年代等条件点歌演唱的能力，官方称其音质、发音、韵律与情感表达较上一代有所提升。

## 触乐：中国小游戏市场上半年收入增长 35%，但买量成本飙升抵消 AI 降本效果
* **日期：** 2026-11-14
* **来源链接：** http://www.chuapp.com/article/291756.html
* **概要（三句话以内，仅客观事实）：** 触乐 11 月 14 日发布的行业周报提到，中国小游戏市场 2026 年上半年收入同比增长超过 35%，但部分品类买量成本同期上涨超过 400%，创意素材生命周期缩短至约 5 天。报道指出，AI 带来的研发降本效果无法抵消买量成本上涨，利润被持续压缩。

## 美股保险分销商元保跨界游戏，曝光自研 AI 乙女向游戏《星河与你》
* **日期：** 2026-11-16
* **来源链接：** https://www.youxituoluo.com/535060.html
* **概要（三句话以内，仅客观事实）：** 据游戏陀螺报道，年营收约 43 亿元、主营保险分销业务的美股上市公司元保（Yuanbao）正式曝光其自研 AI 乙女向游戏《星河与你》，并已在多个平台开启测试招募。报道未进一步披露该游戏具体的 AI 功能细节及测试时间表。

注：经过对西方/全球及中文 games+AI 信源的广泛搜索，第二部分本期仅找到 6 条符合标准、且未与此前 14 天内已发布内容构成同一事件的游戏+AI 简讯；主因是此前一次简报（2026-11-15）已对过去 7 天窗口内绝大多数 NVIDIA、Sony、Epic、Unity、腾讯、网易、米哈游等信源的重大新闻做了覆盖，本期窗口与前一期重叠度极高。未进行任何捏造或凑数。

### 第三部分：24 小时游戏与投资快讯（目标至少 10 条；不限 AI 主题）
* **【Xbox 高管澄清 Project Helix 定位："是能玩 PC 游戏的主机，而非能玩主机游戏的 PC"】**（2026-11-16）— Xbox 高管公开澄清其代号 Project Helix 的新设备定位，强调该设备本质是一台可运行 PC 游戏的主机，而非可运行主机游戏的 PC。 https://www.videogameschronicle.com/news/xbox-says-project-helix-is-a-console-that-can-play-pc-games-not-a-pc-that-can-play-console-games/
* **【《夺宝奇兵：大环》主创谈开发历程：做一款"少用枪"的 MachineGames 作品很难】**（2026-11-16）— 该游戏设计师在采访中谈到，制作一款减少枪械战斗比重的 MachineGames 作品在工作室内部颇具挑战。 https://www.videogameschronicle.com/news/indiana-jones-and-the-great-circle-designer-says-it-was-very-tough-to-make-a-machinegames-title-that-didnt-focus-on-guns/
* **【2027 年格莱美最佳游戏配乐提名公布，《007：首次曝光》《金刚狼》等入围】**（2026-11-16）— 2027 年格莱美奖最佳游戏配乐类别提名名单公布，入围作品包括《007：首次曝光》与《金刚狼》等游戏原声。 https://www.videogameschronicle.com/news/this-years-video-game-soundtrack-grammy-nominations-include-bond-star-wars-and-wolverine/
* **【Unity 推出"Fellowship"扶持计划，每年为 10 支独立团队提供 5 万美元无偿资助】**（2026-11-16）— Unity 宣布推出名为 Fellowship 的扶持计划，每年将为 10 支独立游戏团队提供每队 5 万美元的无偿资助。 https://www.pocketgamer.biz/unity-launches-50000-fellowship-for-indie-game-studios/
* **【ASGC 统计：2022 年以来全球至少 170 家游戏工作室关闭，92% 集中在北美与欧洲】**（2026-11-16）— 行业组织 ASGC 发布统计数据，显示 2022 年以来全球至少有 170 家游戏工作室关闭，其中 92% 位于北美与欧洲地区。 https://www.pocketgamer.biz/asgc-tracks-170-game-studio-closures-since-2022-with-92-in-north-america-and-europe/
* **【Xbox 重组仍在持续：《黑色行动》系列 20 年老将编剧遭裁员】**（2026-11-16）— Treyarch 工作室一名在《使命召唤：黑色行动》系列任职近 20 年的编剧在 Xbox 持续重组中被裁员。 https://kotaku.com/activision-treyarch-layoffs-call-of-duty-zombies-craig-houston-2000757439
* **【据报道：黄仁勋被曝正探索重返 NVIDIA CEO 职位，团队设"作战室"游说董事会】**（2026-11-16）— 据报道，NVIDIA 创始人黄仁勋正在探索重返公司 CEO 职位的可能性，其团队设立"作战室"以游说董事会。 https://kotaku.com/jesen-huang-reportedly-goes-from-calling-himself-a-piece-of-sht-to-exploring-a-return-to-nvidia-2000757422
* **【万代南梦宫披露自研引擎 SOL-AVES 细节：渲染速度"对格斗游戏至关重要"】**（2026-11-16）— 万代南梦宫披露其自研游戏引擎 SOL-AVES 的技术细节，并表示渲染速度对格斗类游戏体验至关重要。 https://kotaku.com/bandai-namco-game-engine-sol-aves-tekken-fighting-games-2000757390
* **【网易《哈利波特：魔法觉醒》官宣停服，12 月 21 日停充值，明年 3 月关服】**（2026-11-16）— 网易公告旗下手游《哈利波特：魔法觉醒》将停止运营，12 月 21 日起停止充值，2027 年 3 月正式关服。 https://www.ithome.com/1/027/738.htm
* **【加拿大 9 岁男孩充值约 2.8 万加元遭 Roblox 拒绝退款】**（2026-11-16）— 一名加拿大 9 岁男孩在 Roblox 平台充值约 2.8 万加元后申请退款被拒，相关报道引发关注。 https://www.ithome.com/1/027/812.htm
* **【广东省首届电竞粤超总决赛定档 11 月 28-29 日深圳南山举行】**（2026-11-16）— 广东省首届电竞"粤超"联赛总决赛确定于 11 月 28 日至 29 日在深圳南山区举行。 https://www.youxituoluo.com/535054.html
* **【Nexon 母公司 NXC 将回购并注销约 2900 亿韩元股份】**（2026-11-15）— Nexon 母公司 NXC 宣布将回购并注销约 2900 亿韩元（约 2.05 亿美元）的股东权益。 https://www.invenglobal.com/articles/28633/nxc-to-buy-back-and-cancel-290-billion-won-worth-of-shareholder-equity
* **【Krafton 同时聘任前韩国企划财政部官员与三星法务高管】**（2026-11-16）— Krafton 宣布同时聘任一名韩国企划财政部前官员与一名三星法务高管加入公司。 https://www.invenglobal.com/articles/28645/krafton-hires-former-moef-senior-official-and-samsung-legal-executive
