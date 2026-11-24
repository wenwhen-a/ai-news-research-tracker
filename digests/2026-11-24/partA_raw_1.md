# Part A — Papers (batch 1 of pre-screened IDs)
Window: last 30 days (2026-10-25 to 2026-11-24). Categories seen: cs.CV, cs.LG. Retrieval: direct verification of 10 pre-screened arXiv IDs (abs + HTML). Qualifying papers in this batch: 6 (2 flagged borderline).

---
## Lyris: Layout-Guided Long Video Generation with Persistent 3D Memory
- **arXiv:** 2611.31239 · https://arxiv.org/abs/2611.31239
- **Submitted:** 2026-11-23 (v1, 18:59:46 UTC)
- **Authors:** Chen Wang, Jiahui Huang, Riccardo de Lutio, Alex Trevithick, Bryan Chu, Jiawei Ren, Laura Leal-Taixé, Shengyu Huang, Lingjie Liu, Haithem Turki
- **Qualifying affiliation(s):** NVIDIA — Haithem Turki (paper's affiliation block also lists University of Pennsylvania for other authors; a footnote notes work partly done during an NVIDIA internship)
- **Categories:** cs.CV
- **Open release:** project page only — http://research.nvidia.com/labs/sil/projects/lyris (no code/weights link stated)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Lyris generates long, camera-controlled video walkthroughs from a single photo by pairing a persistent point-cloud memory of already-observed/generated regions with a 3D layout — one labeled 3D box per object — authored by a vision-language model for areas not yet seen.

**Purpose (≤3 sentences):** The paper targets drift and inconsistency in long video generation, specifically the problem of a walkthrough losing spatial coherence when it revisits a previously seen area.

**Breakthrough (≤3 sentences):** The authors report walkthroughs exceeding three minutes and 50 meters in length, and on minute-long round-trip evaluations across four datasets they report a 3.8x reduction in camera error and a 22% average improvement in consistency upon return.

**Tools & method (≤3 sentences):** The system combines a persistent 3D point-cloud memory for seen/generated content with a VLM-authored simplified 3D box layout for unseen regions, evaluated via round-trip consistency tests on four datasets.

**Limitation (≤3 sentences):** Not stated in the accessible abstract text (the full abstract exceeded the tool's quoting limit); no acknowledged limitation could be extracted.

---
## Analyzing and Improving FlowMap Distillation of Autoregressive Video Models
- **arXiv:** 2611.31164 · https://arxiv.org/abs/2611.31164
- **Submitted:** 2026-11-23 (v1, 18:24:33 UTC)
- **Authors:** Yong-Hyun Park, Guande He, Joon Hyeok Kim, Hansheng Chen, Kaifan Yu, Chaoqi Luo, Xun Huang, Jiatao Gu
- **Qualifying affiliation(s):** Roblox — Guande He, Xun Huang (per paper's affiliation block; a footnote also notes the lead author's work was partly done during a Roblox internship)
- **Categories:** cs.CV, cs.LG
- **Open release:** project page (preprint) — https://enkeejunior1.github.io/ar-video-flowmap/ (no code/weights link stated)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper analyzes why standalone FlowMap distillation underperforms for autoregressive (AR) video generation and proposes two guidance methods, anti-drifting guidance and motion-aware guidance, to fix it.

**Purpose (≤3 sentences):** Existing few-step AR video models rely on distribution-matching distillation (DMD), which the authors state reduces sample diversity and requires a large bidirectional teacher; they seek an effective pure-FlowMap-distillation alternative.

**Breakthrough (≤3 sentences):** Applied to π-Flow, MeanFlow, and consistency distillation with 1.3B AR teachers, the authors report that 4-step π-Flow students trained with their methods match DMD students distilled from 14B teachers on VBench, with reduced drift over 30-second rollouts.

**Tools & method (≤3 sentences):** Anti-drifting guidance uses an auxiliary model that mimics the student's drift as a negative-guidance branch so the AR teacher corrects drifted rollouts; motion-aware guidance locates motion patches and selectively applies skip-layer guidance.

**Limitation (≤3 sentences):** Not stated beyond the comparison baselines in the extracted abstract text; no explicit acknowledged limitation found.

---
## Head Anything: Correspondence-Guided Joint Generation of 3D Heads from Few Images
- **arXiv:** 2611.31143 · https://arxiv.org/abs/2611.31143
- **Submitted:** 2026-11-23 (v1, 18:14:49 UTC)
- **Authors:** Umut Kocasarı, Bartłomiej Baranowski, Richard Shaw, Eduardo Pérez-Pellitero, Matthias Nießner
- **Qualifying affiliation(s):** Huawei Noah's Ark Lab — Richard Shaw, Eduardo Pérez-Pellitero (also Technical University of Munich for other authors). FLAG: borderline (Huawei — not on the core list; kept per instructions)
- **Categories:** cs.CV
- **Open release:** code and models stated as "will be released" (not yet available); project page https://kocasariumut.github.io/HeadAnything/
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Head Anything jointly generates detailed 3D head meshes from several images of the same person showing different expressions and viewpoints, rather than processing each photo independently.

**Purpose (≤3 sentences):** Current image-to-3D head generators handle each input photo separately, so they must guess at head regions unseen in that single image even when other photos of the same person are available.

**Breakthrough (≤3 sentences):** On head scans, the authors report a 32% reduction in head Chamfer distance and a 47% reduction in cross-frame inconsistency relative to the best single-image baseline, along with improved face tracking.

**Tools & method (≤3 sentences):** The authors adapt a pretrained single-image 3D generator with lightweight adapters that restrict each 3D token to attend only to corresponding points in the other images; correspondences come from fitting a neural parametric head model to the generator's own outputs, requiring no ground truth at test time.

**Limitation (≤3 sentences):** Not stated in the available abstract text.

---
## WildAnySplat: Feed-Forward 3D Gaussian Splatting in the Wild
- **arXiv:** 2611.31023 · https://arxiv.org/abs/2611.31023
- **Submitted:** 2026-11-23 (v1, 17:05:01 UTC)
- **Authors:** Richard Shaw, Arthur Moreau, Athanasios Papaioannou, Thomas Tanay, Zhang Zhensong, Eduardo Pérez-Pellitero
- **Qualifying affiliation(s):** Huawei Noah's Ark Lab — all six authors. FLAG: borderline (Huawei — not on the core list; kept per instructions)
- **Categories:** cs.CV
- **Open release:** project page — https://wildanysplat.github.io/ (plus a supplementary-material link); no explicit code/weights release stated
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** WildAnySplat is a feed-forward 3D Gaussian Splatting method for novel-view synthesis from photos captured in uncontrolled, "in the wild" settings.

**Purpose (≤3 sentences):** Standard feed-forward Gaussian-splatting pipelines struggle with transient occlusions and lighting/appearance changes typical of casually captured photo sets.

**Breakthrough (≤3 sentences):** The authors report improved robustness to transient occlusions and lighting variation while keeping fast feed-forward inference, via a student-teacher training setup.

**Tools & method (≤3 sentences):** A teacher network sees clean images while a student sees real-world inputs, trained on real paired captures, synthetic augmentations, and pseudo-clean labels from optimization-based reconstructions; a transformer with DPT heads predicts camera pose, depth, and Gaussians, with per-view transient masks and a bilateral grid for appearance changes.

**Limitation (≤3 sentences):** Not stated in the available abstract text.

---
## CineAct: Interaction-State Agents for Playable, Branching Film Generation
- **arXiv:** 2611.30613 · https://arxiv.org/abs/2611.30613
- **Submitted:** 2026-11-23 (v1, 12:49:13 UTC)
- **Authors:** Junyan Lin, Jianqi Ma, Shujie Duan, Hanxin Zhu, Zhihao Hu, Jinming Liu, Shuai Li, Jun Zhang, Xin Jin, Chang Wen Chen, Weidong Zhang
- **Qualifying affiliation(s):** Tencent — listed in the paper's affiliation block for the author group containing Hanxin Zhu (also Hong Kong Polytechnic University, Xiamen University Malaysia, USTC in that group); exact per-author superscript mapping was not recoverable from the rendered HTML, but Tencent is explicitly one of the stated institutions for this paper's authors
- **Categories:** cs.CV
- **Open release:** none found (no project page, code, or demo link in abstract/comments)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** CineAct is a state-first agentic framework for playable, branching film generation, where language-model agents handle narrative/state reasoning while frozen pretrained image and video generators act purely as renderers.

**Purpose (≤3 sentences):** The authors note that open video generators (citing MiniMax-H3 as an example) produce only short clips of several to a dozen seconds per run, which the paper argues is insufficient for interactive, branching narrative experiences.

**Breakthrough (≤3 sentences):** The authors report gains in multi-step rollout consistency and branching success, measured on a new multi-space benchmark introduced in the paper covering two evaluation suites.

**Tools & method (≤3 sentences):** Interaction-state agents (LLM-based) drive narrative state and branching decisions; frozen image/video generators render the resulting visuals; a new multi-space benchmark is used for evaluation.

**Limitation (≤3 sentences):** Not stated in the available abstract text.

---
## 3AGameFactory-Motion: Agentic Rigging and Reliable Complex Motion Generation for Diverse 3D Assets
- **arXiv:** 2611.30013 · https://arxiv.org/abs/2611.30013
- **Submitted:** 2026-11-23 (v1, 04:16:51 UTC)
- **Authors:** Bohan Zeng, Kaixin Zhu, Yifan Yang, Dongge Yu, Zihao Wu, Yifan Dai, Zhou Liu, Junbo Niu, Xiaochen Ma, Shiran Ge, Zimo Meng, Junzhu Liang, Huanyao Zhang, Jinhang Liu, Tianqi Xiao, Jinhao Zhang, Tianyi Bai, Zhixiong Zeng, Penghao Zhao, Yuanbo Peng, Key Zhang, Wentao Zhang
- **Qualifying affiliation(s):** Tencent Hunyuan — listed in the paper's affiliation block for the author groups containing Huanyao Zhang / Jinhang Liu / Tianqi Xiao / Jinhao Zhang / Tianyi Bai / Zhixiong Zeng and Penghao Zhao / Yuanbo Peng / Key Zhang / Wentao Zhang (alongside Institute of Automation, Chinese Academy of Sciences); per-author superscript mapping was not recoverable from rendered HTML but Tencent Hunyuan is explicitly a stated institution for this paper
- **Categories:** cs.CV
- **Open release:** none found (benchmark DivDynBench introduced but no access link stated)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper introduces DivDynBench, a benchmark for rigging and motion generation across six morphology categories requiring multi-phase part coordination and explicit timing/angle/repetition/trajectory constraints, and proposes an Agentic Motion Framework for diverse 3D assets.

**Purpose (≤3 sentences):** The authors compare three paradigms for controllable motion generation on 3D assets — specialized motion generation, video generation followed by motion recovery, and direct agent-driven generation — to find a more reliable approach across varied morphologies.

**Breakthrough (≤3 sentences):** The authors report that their Agentic Motion Framework's compact parametric control lowers generation overhead and improves rigging reliability and motion-control accuracy relative to the compared paradigms.

**Tools & method (≤3 sentences):** An agent writes compact parametric skeleton and motion programs; a deterministic executor then performs rigging, kinematic solving, and geometric correction.

**Limitation (≤3 sentences):** Not stated in the available abstract text.

# Near-misses
- 2611.30666 · Zhengrong: World Models with Pole-Based Action-Response Factorization for Direct Visual Planning · affiliation does not qualify — the paper's only stated author affiliation is "Beijing Freedo Technology Co., Ltd." (not on the qualifying list and not comparable to the tracked top-tier labs); the pre-screen hint's "Google, NVIDIA" affiliations were not found — NVIDIA appears only as the A100 GPU used for latency benchmarks, not as an author affiliation.
- 2611.30472 · Target-Part Preference Optimization for Part-Aware 3D Generation · academic-only — authors are affiliated with UNSW Sydney, CSIRO, and NTU; no ByteDance or other qualifying industry affiliation appears anywhere in the paper.
- 2611.30022 · MOVER: Planning Beyond Motion · academic-only — authors are affiliated with University of Texas at Austin and ETH Zurich; no ByteDance or other qualifying industry affiliation appears anywhere in the paper.

Verification pass: all 10 pre-screened IDs were independently checked against both the arXiv abstract page (v1 date, title, authors, categories, withdrawal status) and the arXiv HTML page (author affiliations read directly from the paper, not from the pre-screen hints). One ID (2611.31184, "On-Policy Codec Distillation for Efficient All-in-One Video Generation") had a confirmed Adobe Research affiliation but was dropped as off-topic — a general conditioned-video-generation efficiency/distillation method, not clearly a 3D-generation, world-model, character-animation, or game-engine contribution — and is therefore not listed above per instructions for off-topic drops. Double-verification confirmed: all 6 included papers are v1, not withdrawn, on-topic, and carry at least one qualifying-company affiliation read from the paper's own HTML author/affiliation block.
