**[A68] ForgeWM: Progressive Causal Training for Few-Step Action-Conditioned Video World Models**
- **arXiv:** 2608.14022 · https://arxiv.org/abs/2608.14022
- **Submitted:** 2026-08-14
- **Authors:** Xinye Li, Lingshuai Lin, Lei Wang, Liuzhou Zhang, Jialin Cui, Qingshan Li, Guanchu Wang, Qingbin Liu, Xi Chen, Jiang Bian, Wai Lam
- **Qualifying affiliation(s):** Tencent PCG — Lingshuai Lin, Qingbin Liu, Jiang Bian
- **Categories:** cs.CV, cs.AI
- **Open release:** none
- **Shipped counterpart:** none found

**Summary:** ForgeWM converts bidirectional action-conditioned video generators into few-step (1, 2 or 4 step) causal world models for low-latency game-native control through four-stage progressive training, with an optional post-hoc "replay" refinement pass.
**Purpose:** Interactive, game-like applications that need low-latency causal generation with reliable response to discrete and continuous controls.
**Breakthrough:** The authors report the best results on 6 of 7 quality and control metrics against Matrix-Game 2.0 and HY-WorldPlay (ForgeWM-2: LPIPS 0.6171, mouse accuracy 0.8268 at 50.31 FPS and 239.7 ms latency) and a 60.7% pooled preference for ForgeWM-4 in a 41-participant study.
**Tools & method:** 40,000 clips from GF-Minecraft (352x640) and 65,246 clips across seven games for cross-game evaluation; eight GPUs with bf16 and fully sharded data parallelism.
**Limitation:** The authors identify long-horizon drift with visible artefacts beyond a 77-frame window, motion over-response (1.45x flow-magnitude ratio on FPS games), and a metric-dependent effect where a later stage raises sharpness but not paired reconstruction fidelity.
