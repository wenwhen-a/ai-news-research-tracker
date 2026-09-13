**[A45] ReWorld: An Interactive World Model with Long-Horizon Memory**
- **arXiv:** 2608.23565 · https://arxiv.org/abs/2608.23565
- **Submitted:** 2026-08-24
- **Authors:** Zhifei Chen, Luozhou Wang, Guibao Shen, Dongyu Yan, Shuai Yang, Tianshuo Xu, Yihua Du, Wei Wang, Tianyi Gui, Lianghua Huang, Yingcong Chen
- **Qualifying affiliation(s):** Alibaba (ATH) — Zhifei Chen (also HKUST(GZ)), Guibao Shen, Wei Wang, Tianyi Gui, Lianghua Huang
- **Categories:** cs.AI
- **Open release:** demo (project page https://zhifeichen097.github.io/ReWorld/)
- **Shipped counterpart:** none found

**Summary:** ReWorld separates short-horizon control from long-horizon memory during training and bounds both at inference: most attention heads use short windows while a few global heads attend over full history, with a fixed 12-chunk pose-indexed landmark cache to regenerate starting views in minute-long sequences.
**Purpose:** To resolve the tension the authors describe as "control wants a short horizon, memory wants an unbounded one," while streaming in real time.
**Breakthrough:** The authors report the best rotation error (11.95 degrees) among seven compared methods and the highest mean VBench score (0.850) across seven video-quality dimensions.
**Tools & method:** A metric-scale-aligned data engine of 220,724 clips from eight sources (Unreal-rendered fly-throughs, roaming across 79 games, RealEstate10K, DL3DV and others); distribution-matching distillation confined to a LoRA adapter for four-step sampling at 704x1280.
**Limitation:** The authors state "memory is still keyed on camera pose alone; extending consolidation to dynamic scenes and richer, non-navigational interaction is the natural next step."
