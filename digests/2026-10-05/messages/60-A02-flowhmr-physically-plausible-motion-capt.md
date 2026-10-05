**[A02] FlowHMR: Physically Plausible Motion Capture from Video**
- **arXiv:** 2610.03691 · <https://arxiv.org/abs/2610.03691>
- **Submitted:** 2026-10-02
- **Authors:** Zhanke Wang, Chengfeng Zhao, Qing Shuai, Jingzhong Lin, Heng Li, Zeyu Ling, Yuxin Wen, Jing Li, Di Kang, Chunchao Guo, Linchao Bao
- **Qualifying affiliation(s):** Tencent — Zhanke Wang, Chengfeng Zhao, Qing Shuai, Yuxin Wen, Jing Li, Di Kang, Chunchao Guo, Linchao Bao (joint Peking University / HKUST / Tencent affiliations)
- **Categories:** cs.CV
- **Open release:** code (<https://github.com/flowhmr/flowhmr>); demo/project page (<https://flowhmr.github.io/>)
- **Shipped counterpart:** none found

**Summary:** FlowHMR reframes monocular video human motion capture as a video-conditioned motion generation task, using flow matching to produce physically plausible 3D human motion from single-camera video.
**Purpose:** Prior direct-regression HMR methods suffer from depth ambiguity and tend to collapse toward an averaged, physically implausible solution, with no guarantee the recovered motion is dynamically trackable.
**Breakthrough:** The authors report a two-stage pipeline: a pretrained flow-matching model generates diverse motion candidates from video, then Group Relative Policy Optimization (GRPO) refines them with dual rewards for video fidelity and physics-simulation trackability.
**Tools & method:** The method combines flow matching for motion generation with reinforcement learning (GRPO) using video-alignment and physics-tracking reward signals; evaluation uses the newly introduced Wild-4K dataset of ~4K internet videos.
**Limitation:** The paper frames its contribution relative to prior regression-based methods' depth ambiguity and mode-collapse issues; no further limitations beyond this framing were stated in the available abstract/HTML content.
