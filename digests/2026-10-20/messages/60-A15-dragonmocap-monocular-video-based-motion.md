**[A15] DragonMoCap: Monocular Video-based Motion Capture for Diverse Dragon Topologies**
- **arXiv:** 2610.25437 · <https://arxiv.org/abs/2610.25437>
- **Submitted:** 2026-10-18
- **Authors:** Zhongfei Qing et al.
- **Qualifying affiliation(s):** Tencent — Zhongfei Qing, Xiaoxiang Zhao, Yifan Wu, Wei Zeng, Bo Hu, Songnan Li
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** DragonMoCap is a monocular video motion-capture framework for dragon-type game/film characters, whose production rigs vary widely in joint count (20–60+) and naming, breaking fixed-template regressors.
**Purpose:** The authors target the lack of parametric models and high-quality data for non-human (dragon) character mocap, which currently forces manual keyframing in animation production, covering three common topologies: winged quadrupeds, wingless quadrupeds, and winged bipeds (wyverns).
**Breakthrough:** The authors report DragonMoCap beats HMR-style baselines SMPLest-X and OSX on seen rigs (MPJPE 9.46cm vs 10.57cm for SMPLest-X, ~10.5% lower) and generalizes to 77 held-out unseen rigs (MPJPE 12.11cm vs 14.62–15.32cm for ablated variants), with 78.3% top-1 / 94.6% top-5 retrieval accuracy for bone-role matching in a leave-one-rig-out test.
**Tools & method:** Training uses an internal dataset of UE5-rendered, professionally animated dragon clips (88 training rigs / 77 held-out rigs, ~1.2M frames total after SLERP augmentation), with a frozen DINOv2 ViT-L/14 image encoder and frozen CLIP text encoder feeding a transformer decoder that predicts root translation and per-joint 6D rotations.
**Limitation:** The paper has no dedicated limitations section, but the conclusion calls the image encoder's appearance coverage "the main remaining bottleneck," mitigated by generative appearance augmentation to reduce overfitting to limited visual diversity in the internal dataset.
