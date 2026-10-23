**[A03] GSHeadRelight: Fast Relightability for 3D Gaussian Head Synthesis**
- **arXiv:** 2610.30619 · <https://arxiv.org/abs/2610.30619>
- **Submitted:** 2026-10-22
- **Authors:** Henglei Lv, Bailin Deng, Jianzhu Guo, Xiaoqiang Liu, Pengfei Wan, Di Zhang, Lin Gao
- **Qualifying affiliation(s):** Kuaishou Technology — Jianzhu Guo, Xiaoqiang Liu, Pengfei Wan, Di Zhang
- **Categories:** cs.CV
- **Open release:** none (no code/weights/demo link found on the abstract page)
- **Shipped counterpart:** none found

**Summary:** GSHeadRelight addresses relighting and novel-view synthesis of human head portraits — producing photorealistic results in real time, for subjects unseen during training — using generative 3D Gaussians combined with a lighting model based on neural radiance transfer that responds linearly to incident light.
**Purpose:** The authors target the difficulty of doing portrait relighting that is simultaneously photorealistic, real-time, and generalizable to new (unseen) subjects, a combination prior 3D-aware relighting methods have not achieved together.
**Breakthrough:** The authors report state-of-the-art relighting quality while training only on in-the-wild images (no studio/light-stage capture required), with rendering about 12 times faster than prior 3D-aware portrait relighting methods.
**Tools & method:** The method represents heads as generative 3D Gaussians with a linear neural radiance transfer lighting model, enabling both relighting and novel-view synthesis from a single framework.
**Limitation:** The paper's current abstract/metadata do not state specific failure cases (e.g., extreme lighting, accessories, or hair) beyond the reported speed and quality comparisons.
