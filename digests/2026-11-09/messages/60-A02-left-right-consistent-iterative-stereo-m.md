**[A02] Left-Right-Consistent Iterative Stereo Matching via Cross-Injection**
- **arXiv:** 2611.09458 · <https://arxiv.org/abs/2611.09458>
- **Submitted:** 2026-11-06
- **Authors:** Manuel Knott, Diogo Luvizon, Daniel Scharstein, Elias Vansteenkiste
- **Qualifying affiliation(s):** Meta — all four authors listed under Meta Reality Labs
- **Categories:** cs.CV
- **Open release:** code (<https://github.com/facebookresearch/stereo_crossinjection>); S2M2 checkpoints at <https://github.com/junhong-3dv/s2m2> (models used for the Middlebury SOTA numbers are not released, per the paper)
- **Shipped counterpart:** none found

**Summary:** The paper proposes cross-injection (CI), a lightweight add-on for iterative refinement-based stereo-matching models that produces mutually consistent left- and right-view disparity maps from a single pass, rather than two independent passes that often disagree.
**Purpose:** Applications such as per-eye AR/VR rendering, novel view synthesis, and two-view depth fusion need both left and right disparity maps that agree with each other.
**Breakthrough:** The authors report CI "more than halves" left-right disagreement on the Booster benchmark for FoundationStereo, across five evaluation benchmarks (Middlebury, ETH3D, KITTI-12, KITTI-15, Booster) not seen during training.
**Tools & method:** FoundationStereo fine-tuning used a subset of the FoundationStereo Dataset, SceneFlow, FallingThings, Virtual KITTI 2, and Sintel (bf16, effective batch 128, 32 H100 GPUs, 50k steps); S2M2 fine-tuning used a similar mix with DrivingStereo instead of Sintel (fp32, effective batch 128 on 32 GPUs, 4,000 optimizer updates).
**Limitation:** CI assumes a RAFT-style iterative refinement stage and does not apply to single-shot cost-volume regressors, per the authors.
