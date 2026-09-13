# Part B — Primary sources per company

Check every line for the current window. `product:` lines are the customer-facing surfaces to inspect first (product pages, changelogs, cloud model catalogs, app-store notes). Lines prefixed `github:` are parsed by `scripts/github_releases.py` (format: `github: <org>/<repo>` or `github: <org>/*` for all public repos of an org, capped by the script). Blog/newsroom lines are searched and fetched manually. Add or remove lines to change coverage.

## Google / DeepMind
- product: Gemini app / Project Genie (https://deepmind.google/models/genie/ and Gemini app release notes), Google AI Studio & Vertex AI model catalog, Android XR / Android developer blog
- blog: https://deepmind.google/discover/blog/ (Genie, Veo, world-model posts)
- blog: https://research.google/blog/
- blog: https://developers.googleblog.com/
- github: google-deepmind/*

## Microsoft
- product: Azure AI Foundry model catalog, Xbox Game Studios / Muse announcements, Microsoft Flight Simulator & Halo engine posts
- blog: https://www.microsoft.com/en-us/research/blog/
- blog: https://developer.microsoft.com/en-us/games/blog/ (Xbox / Muse / game-dev tooling)
- github: microsoft/* (filter to graphics/3D/animation repos, e.g. TRELLIS, RenderFormer)

## Meta
- product: Meta Horizon / Quest release notes (https://www.meta.com/help/quest/), Meta AI app, Horizon Worlds creator updates, Ray-Ban/Hypernova features
- blog: https://ai.meta.com/blog/
- blog: https://www.meta.com/blog/ (Reality Labs, Horizon, avatars)
- github: facebookresearch/*

## NVIDIA
- product: DLSS / RTX Kit / ACE in shipped games (NVIDIA game-ready driver and GeForce news), Omniverse and Isaac Sim release notes, NVIDIA NIM catalog (https://build.nvidia.com/)
- blog: https://developer.nvidia.com/blog/ (Omniverse, Cosmos, Isaac, RTX Kit, DLSS, ACE)
- blog: https://blogs.nvidia.com/
- release notes: https://docs.nvidia.com/ (Omniverse Kit, Isaac Sim/Lab, Cosmos)
- github: NVIDIA/*, nv-tlabs/*, NVlabs/*, NVIDIA-Omniverse/*, nvidia-cosmos/*

## Amazon
- blog: https://www.amazon.science/blog
- blog: https://aws.amazon.com/blogs/gametech/

## Apple
- product: visionOS / RealityKit / Object Capture release notes, WWDC session pages, App Store release notes
- newsroom: https://www.apple.com/newsroom/
- research: https://machinelearning.apple.com/ (visionOS, RealityKit, Object Capture)
- github: apple/*

## Adobe
- product: Substance 3D release notes, Firefly web app and Creative Cloud app release notes (https://helpx.adobe.com/), Project Neo
- blog: https://research.adobe.com/news/ and https://blog.adobe.com/ (Substance 3D, Firefly 3D, Project releases)

## Intel / Qualcomm
- blog: https://www.intel.com/content/www/us/en/developer/ (graphics research, XeSS)
- blog: https://www.qualcomm.com/news (Snapdragon graphics, Unity/Unreal integrations)

## Tencent
- product: Hunyuan 3D Studio (https://3d.hunyuan.tencent.com/), Tencent Cloud model catalog, Yuanbao app, Tencent Games engine/tooling announcements (GDC/TGDC)
- hub: https://huggingface.co/tencent and https://huggingface.co/Tencent-Hunyuan (Hunyuan3D, HunyuanWorld, GameCraft, HY-Motion)
- blog: https://hunyuan.tencent.com/ and Tencent Games / TiMi / LightSpeed tech blogs
- github: Tencent/*, Tencent-Hunyuan/*

## ByteDance / TikTok
- product: Volcano Engine / BytePlus model catalog (Seed3D, Seedance, Seedream APIs), Dreamina / Jimeng / CapCut / Doubao app release notes, PICO developer blog
- hub: https://huggingface.co/ByteDance and https://huggingface.co/ByteDance-Seed
- blog: https://seed.bytedance.com/ (Seed, Seedance, DreamActor, PICO)
- github: bytedance/*, ByteDance-Seed/*

## miHoYo / HoYoverse
- product: in-game engine features documented in HoYoverse dev blogs and GDC/SIGGRAPH talks
- blog: https://www.hoyoverse.com/ (engine/tech posts), Anime tech talks (GDC/SIGGRAPH)
- github: mihoyo/* (rarely used)

## NetEase
- product: NetEase Games titles and Fuxi tools (e.g. in-game AI NPC / animation systems) documented on official pages
- blog: https://fuxi.163.com/ (Fuxi AI Lab), NetEase Games tech blog
- github: netease-youdao/*, fuxi-lab/* (if present)

## Alibaba
- product: Alibaba Cloud Model Studio (Bailian) catalog, Tongyi / Quark / Wan app updates, AMAP (Gaode) app features
- hub: https://huggingface.co/Wan-AI, https://huggingface.co/Qwen, https://huggingface.co/alibaba-damo-academy, https://huggingface.co/acvlab (AMAP), https://huggingface.co/GD-ML
- blog: https://www.alibabacloud.com/blog and https://damo.alibaba.com/
- github: Wan-Video/*, AMAP-ML/*, amap-cvlab/*, alibaba/*, QwenLM/*

## Baidu
- hub: https://huggingface.co/baidu ; blog: https://research.baidu.com/

## Kuaishou
- product: Kling app and Kling API changelog
- blog: https://klingai.com/ (Kling, 3D/video features)
- github: KwaiVGI/*

## Sony
- product: PlayStation / PS5 Pro (PSSR) features, mocopi, Sony AI product pages
- blog: https://ai.sony/ and https://www.sie.com/en/blog/ (PlayStation, Sony AI, SIE R&D)
- github: sony/*

## Ubisoft
- product: shipped Ubisoft titles with documented Anvil/Snowdrop features (e.g. NEO NPC), Ubisoft Connect updates
- blog: https://www.ubisoft.com/en-us/studio/laforge ; news: https://news.ubisoft.com/

## Electronic Arts
- product: shipped EA titles documenting new engine/ML features, EA SEED public tools
- blog: https://www.ea.com/seed and https://www.ea.com/news
- github: electronicarts/*

## Roblox
- product: Roblox Studio release notes and Creator Hub (Cube 3D, Texture/Mesh generation), Roblox app updates
- blog: https://corp.roblox.com/newsroom and https://devforum.roblox.com/c/updates/announcements (Cube 3D, Roblox AI)
- github: Roblox/*

## Unity
- product: Unity Editor release announcements, Unity AI / Muse, Unity Studio, Asset Store official packages
- blog: https://unity.com/blog ; release notes: https://unity.com/releases/editor/whats-new ; https://discussions.unity.com/c/announcements
- github: Unity-Technologies/*

## Epic Games
- product: Unreal Engine release notes, MetaHuman product blog (https://www.metahuman.com/news), Fab, UEFN release notes, Fortnite engine-feature posts
- blog: https://www.unrealengine.com/en-US/blog and https://www.unrealengine.com/en-US/news ; release notes: https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-5-release-notes ; Fab / MetaHuman announcements
- github: EpicGames/* (most repos require org membership; expect empty results)

## Borderline (keep + flag) and world-model-native startups (near-miss only unless added above)
- World Labs (Marble), Decart, Odyssey, Runway — list as one-line near-misses when notable; not tracked by default.
- JD (Joy Future Academy): https://github.com/jd-opensource
- Ant Group (Robbyant): https://github.com/ant-research
- StepFun, MiniMax, Huawei, Samsung, AMD (GPUOpen), Autodesk, Nintendo — check only if a Part A paper or a lead points there.

## Trade press (leads only, never the source)
GamesIndustry.biz, Game Developer, 80.lv, The Verge, VentureBeat, 36Kr/量子位 (Chinese labs), Hugging Face daily papers, alphaXiv.
