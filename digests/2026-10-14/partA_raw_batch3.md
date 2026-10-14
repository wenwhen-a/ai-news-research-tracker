## ProWorld: Multi-View World Model with Proprioceptive Feedback for Closed-Loop Policy Evaluation
- **arXiv:** 2610.15294 · https://arxiv.org/abs/2610.15294
- **Submitted:** 2026-10-11
- **Authors:** Zijun Wang, Tianyi Yan, Haokun Lin, Panwen Hu, Bohang He, Siyu Ren, Xiaoyu Guo, Weijia Liufu, Shuoshuo Xue, Fengjiao Chen, Zipeng Ye, Xuezhi Cao, Zutao Jiang, Hanhui Li, Xiaodan Liang
- **Qualifying affiliation(s):** Meituan — Xiaoyu Guo (footnote: "Work done during an internship at Meituan"); FLAG: borderline (Meituan is not on the explicit qualified list; other co-authors are Sun Yat-sen University / University of Macau / MBZUAI / South China University of Technology)
- **Categories:** cs.RO
- **Open release:** demo/project page — https://zijunwa.github.io/proworld/ (no code repo link found on the abs page)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** ProWorld is an action-conditioned world model that jointly predicts multi-view video and robot proprioceptive state, feeding both back to a frozen policy to serve as a closed-loop test environment for robot manipulation policies. It uses a shared transformer for joint video-state flow prediction and a "Shared-Time View Encoding" that keeps multiple camera views synchronized while distinguishing them. Training is augmented with failed-interaction data collected in high-fidelity simulation to suppress hallucinated successes (e.g., a missed grasp rendered as a successful lift).

**Purpose (≤3 sentences):** Repeated physical trials to evaluate robot policies are costly, so the authors ask whether a generative world model can substitute for real robots while still tracking real success/failure rates. The model must supply the camera views and proprioceptive state the policy needs for its next action, and must not overestimate policy capability by failing to represent failed actions.

**Breakthrough (≤3 sentences):** The authors report ProWorld achieves "the highest overall TriWorldBench score among the compared methods," and across three policies and four local manipulation tasks attains a Pearson correlation of 0.95 and Spearman correlation of 0.94 between generated-environment and real-robot success rates (their claim).

**Tools & method (≤3 sentences):** A shared transformer jointly generates multi-view video and robot state; Shared-Time View Encoding preserves temporal synchronization across camera views; training data is augmented with failure trajectories gathered in high-fidelity simulation to reduce "interaction hallucinations."

**Limitation (≤3 sentences):** The abstract itself does not enumerate limitations beyond the stated goal of reducing — not eliminating — hallucinated successes; no explicit failure-mode or compute-cost discussion was found in the fetched text.

## CAST: Real-Time Motion Capture for Any Skeleton Topology
- **arXiv:** 2610.14856 · https://arxiv.org/abs/2610.14856
- **Submitted:** 2026-10-10
- **Authors:** Pu Pang, Zhongfei Qing, Ling-Hao Chen, Songnan Li, Hua Huang, Bo Hu
- **Qualifying affiliation(s):** Tencent — Zhongfei Qing, Songnan Li, Bo Hu (marked "Project leader")
- **Categories:** cs.CV
- **Open release:** code — https://github.com/fankewen/CAST
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** CAST recovers motion from monocular video and retargets it onto a target skeleton whose topology differs from the filmed subject's, addressing joint-rotation errors that previously propagated down the kinematic hierarchy. It pairs a learned local-rotation predictor with a geometric correction module (GRACE) guided by predicted global bone directions, applying reliability-gated corrections in parent-to-child order. A causal variant, CAST-B, is designed for real-time use.

**Purpose (≤3 sentences):** Cross-topology motion capture — mapping a performance captured on one body/skeleton onto an arbitrary target skeleton — remains error-prone because small joint-rotation mistakes compound along the skeletal hierarchy. The authors want a framework that generalizes to unseen target skeleton topologies without per-character retraining of rotation estimation.

**Breakthrough (≤3 sentences):** An "observability analysis" formally characterizes which rotational degrees of freedom outgoing bone directions can and cannot constrain, which motivates GRACE's reliability-gated parent-to-child correction. The authors report improved motion recovery across target topologies, including unseen ones, under a new "TopoCap" evaluation protocol plus a curated cross-skeleton Mixamo benchmark and a user preference study; CAST-B (causal) runs at over 51 FPS on a single NVIDIA A100 GPU, including image encoding and motion prediction (their claim).

**Tools & method (≤3 sentences):** The motion predictor and GRACE correction module are trained jointly with motion-derived supervision on top of a frozen image encoder (DINOv3 features mentioned in the appendix); GRACE applies rank-based geometric correction only to the rotation components that outgoing bone directions can observably constrain, leaving the rest to the learned predictor.

**Limitation (≤3 sentences):** The authors state GRACE can only correct rotational components constrained by outgoing bone directions — leaf joints and collinear bone chains leave axial twist undetermined, which they illustrate as visible head-orientation ("twist") errors even when joint positions are accurate. They also note CAST assumes fixed parent-local bone offsets and represents motion only via joint rotations, so animations involving bone translation relative to parents fall outside the model's representation.

## Demiurge: Forging Navigable 4D Worlds via Autoregressive Video Rerendering
- **arXiv:** 2610.14685 · https://arxiv.org/abs/2610.14685
- **Submitted:** 2026-10-10
- **Authors:** Hanxin Zhu, Jianqi Ma, Cong Wang, Zhihao Hu, Junyao Gao, Tianyu He, Junyan Lin, Jiayin Xiao, Jiateng Shou, Sen Liang, Weidong Zhang, Zhibo Chen, Jun Zhang
- **Qualifying affiliation(s):** Tencent — Zhihao Hu, Weidong Zhang; Microsoft — Tianyu He (other authors: USTC, CASIA, Tongji University, PolyU)
- **Categories:** cs.CV
- **Open release:** code/demo — project page https://hanxinzhu-lab.github.io/demiurge_project_page/ linking to GitHub repo https://github.com/HanxinZhu-lab/Demiurge
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Demiurge is an autoregressive video-rerendering pipeline for generating navigable 4D worlds from a single input video, built around a dynamic 4D point-cloud memory cache that enforces consistency across different camera trajectories. It chains four components: an appearance video-diffusion model conditioned on the 4D memory, a memory-consistent video depth-completion model, memory-aware dual-stream warping, and a geometry-aware video refinement stage. Outputs can be optimized directly into 3D Gaussian Splatting representations.

**Purpose (≤3 sentences):** Existing novel-view video synthesis methods process each camera trajectory independently, so they lack the cross-trajectory consistency needed to build a single coherent, navigable 4D world (useful for world modeling, embodied intelligence, and robotic simulation, per the authors). Demiurge targets this cross-trajectory consistency gap directly.

**Breakthrough (≤3 sentences):** The authors claim state-of-the-art performance and three capabilities: coherent spatiotemporal lattice construction over dense multi-view trajectories, large-parallax rerendering under challenging camera motion including 180-degree rotations with no input-view overlap, and geometry-faithful outputs that optimize into high-quality 3D Gaussian Splatting with "minimal artifacts" (their claim).

**Tools & method (≤3 sentences):** A dynamic 4D point-cloud memory cache is updated autoregressively as new trajectories are rendered; a video depth-completion model aligns newly generated depth with cached geometry to resolve scale ambiguity, and dual-stream warping supplies visual/occlusion guidance for the diffusion model before a geometry-aware refinement pass sharpens perceptual quality.

**Limitation (≤3 sentences):** The authors state inference latency is the primary limitation: the sequentially coupled modules (appearance generation, depth completion, optional refinement, memory update) cannot run in parallel, so the full pipeline takes "approximately five minutes to generate one target-trajectory video," ruling out interactive use as-is. They propose an asynchronous cloud-edge fast/slow-path split and a more compact 4D memory representation as future work, since the current point-cloud memory accumulates redundant points and rising storage/retrieval cost as more trajectories are added.

## Remembering What Matters for Long-Horizon Robotic World Models
- **arXiv:** 2610.14583 · https://arxiv.org/abs/2610.14583
- **Submitted:** 2026-10-10
- **Authors:** Hao Wu, Tianyu Shao, Shengju Qian, Yizhou Zhao, Fan Zhang, Penghao Zhao, Weiyan Wang, Yufei Huang, Fan Xu, Kun Wang, Xin Wang, Ming-Hsuan Yang, Yuxuan Liang
- **Qualifying affiliation(s):** Tencent — Penghao Zhao, Weiyan Wang, Yufei Huang (other authors: HKUST(GZ), North China Electric Power University, LIGHTSPEED, Carnegie Mellon University, CUHK, USTC, Nanyang Technological University, UC Merced)
- **Categories:** cs.RO (primary), cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper studies why autoregressive robot-video world models using discrete visual tokens degrade over long rollout horizons, arguing that keeping the entire generated history actually hurts because persistent scene context, recent visual-action states, and stale history compete for the model's attention. They propose ReCAP (Receding Context with Anchor Preservation), a training-free method that keeps only an initial scene "anchor" plus a sliding window of recent visual-action blocks, evicting older history, while leaving pretrained models frozen. ReCAP is evaluated on RT-1, BridgeV2, LIBERO-90, and CALVIN.

**Purpose (≤3 sentences):** Long-horizon rollouts are central to using video world models for robot policy evaluation and planning, but naively keeping full generation history is both computationally expensive and, the authors argue, actively degrades prediction quality. They aim to identify and preserve only the context that matters.

**Breakthrough (≤3 sentences):** ReCAP improves visual fidelity, action-conditioned consistency, and robot-structure preservation versus full-context decoding across all four benchmarks (their claim); on BridgeV2 it reduces LPIPS by 63.3%, and across the four benchmarks LPIPS at horizon H=64 degrades far less than Full Context (e.g., Full Context LPIPS rises from 0.204→0.237 on RT-1, 0.106→0.154 on CALVIN, 0.166→0.183 on LIBERO-90). At H=64 it also cuts logical KV cache footprint by 73.3% and p50 latency by 6.51%, and an attention analysis shows Full Context spends 71.5% of attention on stale history on CALVIN C06 versus ReCAP shifting 70.4% of attention to recent states.

**Tools & method (≤3 sentences):** ReCAP is training-free and model-agnostic: it keeps a fixed initial "scene anchor" (to retain persistent scene information) plus a receding window of the most recent visual-action blocks, discarding intermediate history rather than retraining or fine-tuning the underlying discrete-token world model.

**Limitation (≤3 sentences):** The authors acknowledge their results are "consistent with" a memory-role-conflict hypothesis but do not isolate it from confounding context-length and position-handling effects, since reinserting tokens also changes context length. In their VLM-based evaluation protocol specifically, they note sparse-frame sampling can miss transient errors, judges share evidence/rubrics so errors may be correlated (12 positive differences are not independent replications), and the scores measure visible plausibility/instruction compatibility rather than verified physics or real-robot task success.

# Near-misses
- 2610.15280 · GeoBridge: Evolving Transferable Decoder Topologies for Geometric Vision · on-topic (3D/geometric vision: depth estimation, Gaussian-splatting novel-view synthesis on RealEstate10K, open-vocabulary segmentation on LERF) and within the submission window (2026-10-11), but no HTML version exists (https://arxiv.org/html/2610.15280 returns 404) so the author/affiliation block could not be verified; the pre-screen's "Google" hit could not be confirmed. Only 3 listed authors (Rui Wang, Haoyu Zhang, Ran Cheng), which looks academic (Ran Cheng is associated with an evolutionary-computation lab) rather than an industry team, but this is not independently confirmed — affiliation unverifiable per the no-PDF-fallback rule.
