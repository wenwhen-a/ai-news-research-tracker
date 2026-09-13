# Part B — What counts as "research translated into product"

Part B tracks **final products a customer or business can actually use**: consumer apps and app features (2C), or paid/enterprise services, cloud APIs, studio tools and engine features (2B). Examples of the right kind of item: ByteDance Seed3D 2.0 exposed as a Volcano Engine API; Google's Project Genie inside the Gemini app; MetaHuman Animator markerless capture shipping in Unreal Engine 5.8; Tencent Hunyuan 3D Studio; Adobe Substance 3D / Firefly 3D features; NVIDIA ACE or DLSS in shipped games; Roblox's Cube 3D generation inside Roblox Studio.

## Explicitly NOT Part B
- Open-weights or open-source code drops, Hugging Face model cards, research demos, paper project pages, Gradio/Space demos, and "technical previews" with no product surface. These are research artifacts. Record them in **Part A** on the paper's `Open release:` line (weights / code / demo / none) and do not list them in Part B.
- A model announced only on a research page (e.g. seed.bytedance.com, deepmind.google/research) with no app, API, or product it is available in.
- Third-party wrappers of a tracked company's model (aggregator sites, resellers). Only the company's own product surfaces count.

## Status tiers (label every item with exactly one)
| Tier | Definition | Goes in |
|---|---|---|
| **GA** | Generally available to customers or developers today, paid or free: an app feature, product, engine version, cloud API/service, SDK, plugin or studio tool. No invitation or waitlist. | Main list |
| **Public beta / preview** | Usable today by anyone who opts in (open beta, preview toggle, "labs" feature, self-serve API preview). Region- or plan-gated is still fine; invitation-only is not. | Main list |
| **Announced only** | Keynote demo, "coming later this year", waitlist, private/enterprise-invite beta, or press reports of an unreleased product. | Trailing list, one line each |

Test: can a customer or developer use it today without asking the company for access? Yes → GA or Public beta. No → Announced only.

## Product surfaces to look for (per company)
- Consumer apps: Gemini app / Project Genie (Google); Dreamina, Jimeng, Doubao, CapCut, PICO (ByteDance); Horizon, Quest, Meta AI (Meta); Roblox app/Studio; PlayStation (Sony); Kling app (Kuaishou); Yuanbao / Hunyuan 3D site (Tencent); Tongyi / Quark / Wan apps (Alibaba).
- Cloud & API: Vertex AI / AI Studio (Google), Azure AI Foundry (Microsoft), Volcano Engine / BytePlus (ByteDance), Alibaba Cloud Model Studio (Alibaba), Tencent Cloud (Tencent), Baidu Qianfan, NVIDIA NIM / Omniverse Cloud / DGX Cloud, AWS Bedrock (Amazon), Apple developer frameworks (RealityKit, Object Capture).
- Creator & developer tools: Unreal Engine, MetaHuman, Fab, UEFN (Epic); Unity Editor, Unity Muse/AI, Unity Studio (Unity); Substance 3D, Firefly, Photoshop/Premiere 3D features (Adobe); Omniverse, Isaac Sim, ACE, DLSS, RTX Kit (NVIDIA); Hunyuan 3D Studio (Tencent); Roblox Studio Cube; EA Frostbite / SEED tooling; Ubisoft engines and La Forge tools; Sony mocopi / SIE tools; miHoYo / NetEase in-game engine features and dev tools.
- Games and shipped titles: a tracked company's own game that ships a new engine/AI feature (e.g. neural rendering, ML animation) counts as GA if the game is released and the company documents the feature.

## Company gate
Same tracked list as SKILL.md; subsidiaries count under the parent. Borderline organizations (JD, Ant Group, StepFun, MiniMax, Huawei, Samsung, AMD, Autodesk, Nintendo) → keep and flag. World-model-native startups (World Labs, Decart, Odyssey, Runway) are **not** tracked by default — include them only if the user has added them to the tracked list; otherwise list as a one-line near-miss when notable.

## Primary sources only
Acceptable: the product's own page, pricing page, changelog / release notes, official blog or newsroom post, cloud console model catalog page, app-store release notes, official docs, official conference session page. Trade press, tweets, aggregator "AI news" sites and reseller model catalogs are leads only. No primary source → drop (or near-miss with "unverified").

## Linking to research
1. Check the product page / docs / blog for citations or "based on our research" links.
2. Search the company research blog and arXiv for the model or method name.
3. Record arXiv ID + title; if several, list the one or two the company names first.
4. Otherwise write **"no traceable paper"**. Never infer from topic similarity.

## Dedup across runs
Key = canonical primary-source URL. `product_seen.json`: `{ "<url>": {"name", "company", "tier", "first_seen", "release_date"} }`. Load before the run, mark matches **Previously reported** (one line), write all keys back after. A tier change (Announced → GA) or a new version is a **New** item.

## Objectivity for product items
- Availability facts (platforms, plans, price, regions, GA vs beta) verbatim from the source.
- Performance and quality claims are the company's claims: "ByteDance states…", "Epic reports…".
- "Practical significance" means concrete: who can use it, on what surface, at what cost, replacing which workflow — as the source states it.
