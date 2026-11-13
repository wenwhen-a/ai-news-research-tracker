**[A09] BirdDreams: Joint Perspective and BEV Video Generation for a Plausible, Reactive Driving World Model**
- **arXiv:** 2611.14815 · <https://arxiv.org/abs/2611.14815>
- **Submitted:** 2026-11-10
- **Authors:** Junyoung Seo et al.
- **Qualifying affiliation(s):** NVIDIA — Jaewoo Seo, Laura Leal-Taixé (project page hosted at research.nvidia.com/labs/sil); Seungryong Kim is listed with KAIST
- **Categories:** cs.CV
- **Open release:** project page only (<https://research.nvidia.com/labs/sil/projects/birddreams/>); no explicit code/weights release stated in fetched text
- **Shipped counterpart:** none found

**Summary:** BirdDreams is an autoregressive driving world model that generates a perspective (camera-view) video and a schematic bird's-eye-view (BEV) video jointly, so scene layout is part of the prediction rather than inferred implicitly.
**Purpose:** Driving world models need to show plausible surrounding-vehicle motion and precise ego-trajectory control, but learning vehicle motion from perspective video alone is hard because motion is "entangled with appearance and vehicles can be occluded." The paper aims to disentangle layout from appearance by generating a BEV stream alongside the perspective stream.
**Breakthrough:** The authors report, without ego conditioning, a 21% reduction in minADE vs. their OmniDreams (Vanilla) backbone on PhysicalAI-AV and 37% on nuScenes; with ego conditioning, ADE reductions of 35% (PhysicalAI-AV) and 36% (nuScenes) vs. an OmniDreams (Plücker) baseline.
**Tools & method:** The model builds on a pretrained "OmniDreams" backbone (~4B parameters) with Diffusion Forcing (per-stream noise sampling) followed by "Resampling Forcing"; at inference it needs only a single camera image, no HD map or vehicle-state input, and ego control works by reprojecting the latest BEV frame along an input trajectory as a soft condition.
