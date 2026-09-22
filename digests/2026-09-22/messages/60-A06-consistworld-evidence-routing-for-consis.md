**[A06] ConsistWorld: Evidence Routing for Consistent Multi-Agent World Models**
- **arXiv:** 2609.22641 · <https://arxiv.org/abs/2609.22641>
- **Submitted:** 2026-09-18
- **Authors:** Qianxun Xu et al.
- **Qualifying affiliation(s):** StepFun — Xianfang Zeng, Xinyao Liao, Wei Cheng, Gang Yu (Qianxun Xu also lists StepFun alongside Westlake University and UCLA); FLAG: borderline
- **Categories:** cs.CV
- **Open release:** code (<https://github.com/CeciliaTheBirb/ConsistWorld),> weights (<https://huggingface.co/CeciliaXu00/ConsistWorld),> eval data (<https://huggingface.co/datasets/CeciliaXu00/multicam_no_person)>
- **Shipped counterpart:** none found

**Summary:** ConsistWorld is a multi-agent video world model that generates camera-controlled video streams of a static scene from a single shared source image, with multiple independently steered "agents" (viewpoints) exploring the same world.
**Purpose:** Existing autoregressive video world models handle a single observer well, but extending them to several independently-controlled cameras raises the problem of keeping revisited or jointly-explored regions of the world visually consistent across agents and over long time horizons.
**Breakthrough:** The authors report that "Pose Conditioned Memory Retrieval" (selecting relevant historical observations via camera-geometry overlap rather than keeping full history active) and "Visibility-Gated Peer Sharing" (a gate that suppresses peer information over already-committed regions while preserving it for new content) together substantially reduce inconsistency.
**Tools & method:** Training proceeds in two stages: first on MultiCamVideo (3,400 Unreal Engine-rendered scenes with ten cameras, 81 frames at 240x416), then on 1,000 Infinigen scenes with eight synchronized cameras (141 frames).
