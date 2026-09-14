**[B01] Wan3.0-Video / Wan3.0-Video-Prime (万相3.0)**
- **Company:** Alibaba (Tongyi Wanxiang / Bailian)
- **Status:** GA · **Released:** 2026-08-06 (wan3.0-video), 2026-08-20 (wan3.0-video-prime) · **New**
- **Surface:** Cloud API (Alibaba Cloud Model Studio / Bailian model catalog)
- **Primary source:** https://help.aliyun.com/zh/model-studio/newly-released-models
- **Underlying research:** arXiv:2503.20314, "Wan: Open and Advanced Large-Scale Video Generative Models" (Team Wan / Alibaba Tongyi Lab — foundational technical report for the Wan model family; no separate Wan3.0-specific paper found) — https://arxiv.org/abs/2503.20314
- **Availability:** Listed as production model IDs `wan3.0-video` and `wan3.0-video-prime` (fast/turbo variant) in Alibaba Cloud Model Studio's model catalog, China-North-2 (Beijing) region table; billed API access, not open-weights.

**What shipped:** Alibaba's Bailian model catalog added Wan3.0-Video, described as an "all-in-one" video generation model unifying reference-generation, editing, replication (复刻) and character-driving (驱动) into one model, with four-modality full reference input and up to 30-second video generation.
**What research it translates:** The Wan series originates from Alibaba Tongyi Lab's diffusion-transformer video foundation models described in the March 2025 "Wan" technical report (arXiv:2503.20314); Wan3.0 is a further, undocumented-in-public-paper iteration of that lineage that the vendor's own catalog entry credits with the "驱动" (character-driving/motion-transfer) capability previously associated with the separate Wan-Animate model line.
**Practical significance:** Alibaba's catalog copy states the model provides "生产级角色一致性保持" (production-grade character consistency) and "音画真实" (realistic audio-video sync), positioning it as a production tool rather than a demo.
