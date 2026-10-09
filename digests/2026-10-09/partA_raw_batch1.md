Part A verification batch — leads matched by company-name regex, independently verified. 12 arXiv ids checked. Qualifying: 6. Near-misses: 6.

---

## DreamTrue: Action-Faithful Robot World Model with Counterfactual Post-Training
- **arXiv:** 2610.12468 · https://arxiv.org/abs/2610.12468
- **Submitted:** 2026-10-08 (v1)
- **Authors:** Junyan Li, Ruizhi Li, Yu Liu, Xiangshuo Liu, Mingchao Sun, Hongyu Pan, Mu Xu, Lue Fan, Zhaoxiang Zhang
- **Qualifying affiliation(s):** Alibaba Group / Amap — Yu Liu, Mingchao Sun, Hongyu Pan, Mu Xu (per HTML author block). Other authors are at NLPR, Institute of Automation, Chinese Academy of Sciences (CASIA).
- **Categories:** cs.RO (primary), cs.CV
- **Open release:** project page only, no code/weights stated — https://brave-eai.github.io/DreamTrue
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** DreamTrue is a multi-view, cross-embodiment robot world model trained to predict videos that follow given actions and stay physically plausible. It targets two problems in robot video datasets: imprecise action-to-video calibration and sparse coverage of failed interactions, which biases predictions toward success.

**Purpose (≤3 sentences):** The authors aim to improve action-faithfulness and physical plausibility of robot world-model video prediction across different robot embodiments and camera views.

**Breakthrough (≤3 sentences):** The authors report state-of-the-art action following on the AgiBot benchmark and say their counterfactual post-training cuts the human-assessed interaction defect rate from 48.12% to 6.25%. They state the model ranked first in the world model track of the AgiBot World Challenge 2026.

**Tools & method (≤3 sentences):** Action trajectories are rendered as image-space conditions with offline geometric calibration to align them with target videos; counterfactual post-training perturbs recorded trajectories to cover a wider range of actions and contact configurations. A human-annotated dataset of robot/object/interaction defects trains an embodied video reward model whose scores guide reinforcement-learning post-training.

**Limitation (≤3 sentences):** The abstract does not state explicit limitations; evaluation is reported on the AgiBot dataset/challenge only, so generalization beyond that benchmark is not characterized in the abstract (observed, not stated).

---

## What 30,000 Hours of Ego-centric Video Does Not Teach
- **arXiv:** 2610.12464 · https://arxiv.org/abs/2610.12464
- **Submitted:** 2026-10-08 (v1)
- **Authors:** Jiahua Dong, Anurag Bagchi, Yash Jangir, Muhammad Zubair Irshad, Sergey Zakharov, Martial Hebert, Homanga Bharadhwaj, Yu-Xiong Wang, Vitor Campagnolo Guizilini, Pavel Tokmakov
- **Qualifying affiliation(s):** Toyota Research Institute (TRI) — listed as an affiliation for multiple co-authors in the HTML author block (per-author superscript mapping did not render, so the exact subset of the 10 authors is not individually resolvable from the HTML, but TRI is unambiguously one of the paper's stated affiliations, distinct from the academic ones). **Flag: TRI is not on the explicit tracked-company list; keeping as a comparable top-tier industrial research lab, for user judgment.** Academic co-affiliations: UIUC, CMU, Johns Hopkins.
- **Categories:** cs.CV
- **Open release:** not stated in the abstract or abs page (a project-style URL appears garbled in extraction; not independently confirmed, so omitted)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper studies how far scaling ego-centric human video (30,000 hours, 1,000+ scene types, 14,000+ contributors) can push video world models as an alternative to physics-based simulators. It evaluates agent and object-interaction fidelity directly on an out-of-distribution benchmark rather than relying on downstream proxy metrics.

**Purpose (≤3 sentences):** The authors want to know whether scaling data alone closes the gap between video world models and physics simulators, and where it does not.

**Breakthrough (≤3 sentences):** The authors report a 100x increase in training data improves both agent and object fidelity, but unevenly: agent modeling becomes strong while object fidelity stays much lower and improves slowly. They report that careful visual-conditioning design can saturate agent fidelity with a fraction of the data, letting object fidelity be measured and its saturation point located separately; a new supervision scheme that shifts capacity toward object dynamics improves object fidelity, "though a substantial gap remains" (authors' statement).

**Tools & method (≤3 sentences):** The study trains on a 30,000-hour ego-centric video dataset and evaluates on a dedicated out-of-distribution benchmark; findings are also reported to transfer to downstream humanoid modeling.

**Limitation (≤3 sentences):** The authors state that a substantial object-fidelity gap remains even after their supervision change, and conclude that closing it depends on training methods, not data volume alone.

---

## LeWAM: A JEPA World Action Model with Diffusion-Steering-Based MPC
- **arXiv:** 2610.12407 · https://arxiv.org/abs/2610.12407
- **Submitted:** 2026-10-08 (v1)
- **Authors:** Shashank Hegde, Alexander Popov, Elie Aljalbout, Nikolai Smolyanskiy
- **Qualifying affiliation(s):** NVIDIA — all four authors (sole affiliation listed in HTML author block)
- **Categories:** cs.RO (primary), cs.AI, cs.CV
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** LeWAM is a bidirectional transformer that performs forward dynamics, backward dynamics, inverse dynamics, and policy prediction on a shared, decoder-free JEPA latent, trained end-to-end across all four modes. It is framed as a "world action model" (WAM) that predicts both actions and future observations.

**Purpose (≤3 sentences):** The authors aim to replace the noisy, redundant reconstruction-based representations typically used by world action models with a cleaner JEPA latent, and to improve planning by not sampling raw actions directly.

**Breakthrough (≤3 sentences):** The authors report that linear probes read robot and object state from LeWAM's latent better than from a forward-only JEPA world model, while the latent still ignores visual distractors as well as that forward-only model (and better than a reconstruction-based WAM). They report that closed-loop evaluations of LeWAM match a flow-matching policy trained on the same encoder at matched size while also providing a world model, and that planning in the policy head's noise space (rather than sampling raw actions) improves closed-loop MPC performance.

**Tools & method (≤3 sentences):** The core method is a JEPA-based latent trained jointly for forward, backward, and inverse dynamics plus policy prediction, combined with diffusion-steering-based model predictive control (MPC).

**Limitation (≤3 sentences):** The abstract states that sampling raw actions during MPC planning "lets MPC exploit dynamics-model inaccuracies," which is the specific failure mode their noise-space planning is designed to avoid; no other limitations are stated in the abstract.

---

## SpaceFlow: Locally Controllable 3D Generation
- **arXiv:** 2610.12399 · https://arxiv.org/abs/2610.12399
- **Submitted:** 2026-10-08 (v1)
- **Authors:** Neil De La Fuente, Joan Lafuente, Mukhammadali Sayfiddinov, Felicia Scharitzer, Marc Pollefeys, Ata Çelen, Sayan Deb Sarkar, Elisabetta Fedele
- **Qualifying affiliation(s):** Microsoft — listed as one of the paper's three institutional affiliations (alongside ETH Zürich and Stanford University) in the HTML author block. **Flag: the specific author(s) at Microsoft could not be resolved because the author→affiliation superscript markers failed to render in the arXiv HTML (a LaTeX macro/rendering artifact, confirmed by inspecting the raw HTML); Microsoft is listed identically to the two confirmed academic affiliations, so this is not a "Google Scholar"-style false positive, but the per-author mapping is unverified.**
- **Categories:** cs.CV (primary), cs.AI, cs.GR
- **Open release:** project page only, no code/weights stated — http://SpaceFlow3D.github.io
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** SpaceFlow is a training-free pipeline for locally controllable 3D generation from text and a set of geometric primitives, where each primitive acts as a per-part proxy with its own control strength. It addresses the lack of per-region control in current 3D generation methods, which the authors say typically use one global geometric-adherence strength and cannot localize appearance.

**Purpose (≤3 sentences):** The authors want users to specify, per object part, whether generation should strictly follow an input shape or allow generative completion, and to localize appearance cues (text/image) to specific parts without cross-part leakage.

**Breakthrough (≤3 sentences):** The authors report that regional geometry metrics show SpaceFlow preserves specified geometry in high-control regions while allowing plausible shape variation in low-control regions. They report state-of-the-art prompt faithfulness and color/material accuracy when evaluating text-conditioned appearance on fixed geometry, and say a user study found the fidelity/freedom balance "competitive" in overall quality.

**Tools & method (≤3 sentences):** Structure generation enforces per-primitive spatial constraints inside the generative flow process; for appearance, the generated structure is segmented and matched back to the primitives so each part is conditioned only on its assigned text/image cue.

**Limitation (≤3 sentences):** The abstract does not state explicit limitations; the authors' own supplementary table of contents lists a dedicated "Limitations" appendix section, but its content was not read for this verification pass (observed, not stated).

---

## LiteNWM: Efficient Latent World Models for Onboard Visual Navigation in the Wild
- **arXiv:** 2610.12368 · https://arxiv.org/abs/2610.12368
- **Submitted:** 2026-10-08 (v1)
- **Authors:** Linkai Liu, Yuntian Zhang, Zhenshan Bing, Chen Chen, Lingjuan Lyu, Shangguang Wang, Mengwei Xu, Dongqi Cai
- **Qualifying affiliation(s):** Sony AI — Chen Chen, Lingjuan Lyu. Other co-authors are at Nanjing University, Imperial College London, and Beijing University of Posts and Telecommunications.
- **Categories:** cs.RO
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** LiteNWM is a latent navigation world model for visual robot navigation that shares visual encoding across candidate trajectories and predicts their action-conditioned future representations at multiple time horizons, with a learned scorer choosing among them. It targets the cost of generative world models that must render full visual rollouts to evaluate many candidate trajectories.

**Purpose (≤3 sentences):** The authors want navigation policies that get the foresight benefit of world-model rollouts (evaluating likely future outcomes) without the computational cost of rendering a full visual rollout per candidate.

**Breakthrough (≤3 sentences):** The authors report LiteNWM reduces macro-averaged trajectory error by 17.56% relative to NoMaD+NWM-XL on offline benchmarks (RECON, SCAND, SACSoN), with a 128.00-fold end-to-end speedup on an RTX 5090. They report the same evaluator transfers from the NoMaD proposer to MBRA without retraining (reducing MBRA's error by 16.2%), and that in real-robot tests in unseen indoor/outdoor environments it raised navigation success from 43.3% to 83.3% relative to NoMaD.

**Tools & method (≤3 sentences):** The method shares a visual encoder across candidate trajectories, predicts action-conditioned future latent representations at several horizons, and uses a learned scorer for trajectory selection; it is evaluated offline on RECON/SCAND/SACSoN and on a physical robot, with speed measured on an RTX 5090 GPU.

**Limitation (≤3 sentences):** The abstract does not state explicit limitations.

---

## Controllable Exaggeration for Generative Motion Models via Training-Time Adaptation and Inference-Time Guidance
- **arXiv:** 2610.12316 · https://arxiv.org/abs/2610.12316
- **Submitted:** 2026-10-08 (v1)
- **Authors:** Amirhossein Zamani, Arianna Rampini, Bruno Roy
- **Qualifying affiliation(s):** Autodesk Research — all three authors are jointly listed under Autodesk Research, Mila (Quebec AI Institute), and Concordia University in the HTML author block (per-author institution not individually distinguished); acknowledgments separately state the work was "supported by Autodesk Research and the Autodesk AI Lab." **Flag: Autodesk is not on the explicit tracked-company list; keeping as a comparable top-tier industry lab for character-animation tooling (comparable to Adobe), for user judgment.**
- **Categories:** cs.CV
- **Open release:** project page (demo/visual results), no code/weights stated — https://ahhhz975.github.io/ControllableMotionExaggeration/
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper addresses the Exaggeration principle of traditional animation — largely absent from recent physically-plausible motion generative models — and proposes a two-stage framework to add it to existing text-to-motion pipelines. Stage one fine-tunes pretrained text-to-motion models on a curated exaggeration dataset; stage two adds an inference-time guidance signal, with no extra training, built on a mathematical formulation of exaggeration using dynamic movement primitives (DMPs).

**Purpose (≤3 sentences):** The authors want motion generative pipelines to produce character motion that is not only physically plausible but also expressive and engaging in the way professional animators design motion, specifically via the exaggeration principle.

**Breakthrough (≤3 sentences):** The authors report that, against three strong motion-generation baseline models, their methods generate "more exaggerated and expressive motions while preserving neutral reference motion intent and physical plausibility" (authors' claim, qualitative and quantitative evaluation).

**Tools & method (≤3 sentences):** Training-time: supervised fine-tuning of pretrained text-to-motion models on a curated exaggeration dataset. Inference-time: a DMP-based mathematical exaggeration signal used as guidance for existing diffusion and flow-matching text-to-motion models, without additional training.

**Limitation (≤3 sentences):** The abstract does not state explicit limitations.

---

# Near-misses
- 2610.12459 · WorldGuide: Goal-Directed Video World Model for Procedural Task Execution · academic-only — sole affiliation is Mohamed bin Zayed University of Artificial Intelligence (MBZUAI); no industry co-author found in the HTML author block. (On-topic as a video world model; dropped only on the affiliation gate.)
- 2610.12440 · Generative Neural Retargeting for Human-to-Robot Dexterous Manipulation · off-topic — Meta Reality Labs Research is a genuine co-affiliation (alongside UC Davis, UNC Chapel Hill, UC Berkeley, MIT, CMU; paper notes "work done at Meta"), but the paper is a human-to-robot motion-retargeting/control method (flow-matching trajectory sampling for dexterous manipulation), not a 3D-generation, world-model, character-animation, or game-engine paper.
- 2610.12382 · WorldAlign: Decoupled 4D Reward for World-Consistent Video Generation · affiliation unverifiable — arXiv HTML page returns HTTP 404 for both the current and v1 versions (confirmed independently via curl), so author affiliations could not be read from the HTML per the stated procedure; not guessed from the PDF or abstract text, even though author names suggest possible industry ties.
- 2610.12299 · Multi-Agent Egocentric World Model with Fine-Grained Embodied Interaction (ME-World) · academic-only — sole affiliation is KAIST AI; no industry co-author found in the HTML author block. (On-topic as a multi-agent egocentric world model; dropped only on the affiliation gate.)
- 2610.12156 · Connected Self Forcing: Beyond Local Learning in Video Autoregression · off-topic — XPeng is a genuine co-affiliation (project lead and several co-authors at XPeng; others at CUHK and Tsinghua), but the paper is a generic long-video autoregressive-generation/exposure-bias training technique with no action-conditioning or embodied/world-model framing stated in the abstract.
- 2610.12104 · VINCIE-NExT: Unlocking Video Editing from Images via In-Context Modeling · off-topic — ByteDance Seed is a genuine co-affiliation (alongside National University of Singapore and University of Science and Technology of China), but the paper is a general instruction-based video-editing framework, not 3D, a world model, character animation, or a game engine.

Verification pass: each of the 12 ids was checked against its arXiv abstract page (v1 date, title, authors, categories, no withdrawal notice) and, where available, its arXiv HTML page (author affiliations read from the rendered author block or raw HTML source, not inferred from the PDF). All quoted figures above were taken verbatim from the papers' own abstracts; no numbers were invented. 6 of 12 leads qualify; 6 are recorded as near-misses with reasons above, accounting for all 12 ids. Two flags raised for user judgment: Toyota Research Institute (2610.12464) and Autodesk Research (2610.12316) are not on the explicit tracked-company list but are kept as comparable top-tier industry labs; Microsoft's specific co-author on 2610.12399 could not be pinned down due to a broken HTML affiliation-rendering macro (confirmed by inspecting raw HTML), though Microsoft is unambiguously one of the paper's three listed institutional affiliations.
