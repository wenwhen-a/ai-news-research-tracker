## Kandinsky S2V 1.0: Audio-Driven Avatar Video Generation
- **arXiv:** 2610.19290 · https://arxiv.org/abs/2610.19290
- **Submitted:** 2026-10-13
- **Authors:** Nikolay Semenov, Artem Riabinin, Sergey Bassenko, Anna Averchenkova, Julia Agafonova, Anastasia Aliaskina, Kirill Kozlov, Lev Novitskiy, Nikita Samsonov, Nikolai Gerasimenko, Denis Dimitrov
- **Qualifying affiliation(s):** Kandinsky Lab (Sber) — all authors; FLAG: borderline — Kandinsky Lab
- **Categories:** cs.CV
- **Open release:** code, model checkpoints, and a diffusers integration, released under the MIT license (per abstract); no specific repo URL found in the page text
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Kandinsky S2V 1.0 is an open family of speech-to-video models (a 2B "Lite" and a 21B "Pro" variant) that generate long-form 25 FPS video of a person speaking, driven by a reference image, a speech waveform, and a text prompt. Lip movement, facial expression, pose, and gestures are generated to follow the input speech. The models are trained on 1.17M single-speaker video clips with English and Russian captions.
**Purpose (≤3 sentences):** The goal is controllable, audio-driven human/avatar animation that stays consistent with speech over long video durations, rather than short clips.
**Breakthrough (≤3 sentences):** The authors report that in a human side-by-side evaluation, the Pro model performed comparably to or better than an open-source baseline and two commercial models, and was preferred specifically for lip sync. They also report distilled variants that need only 16 sampling steps and no classifier-free guidance, giving roughly a 5.4x end-to-end speedup.
**Tools & method (≤3 sentences):** Text and audio conditioning is handled by a Qwen2.5-Omni model, combined with a reference-aware visual memory for identity/appearance consistency; the models are trained on 1.17M single-speaker clips, and the release includes code, checkpoints, and a diffusers integration under the MIT license.
**Limitation (≤3 sentences):** The training data is limited to single-speaker clips captioned only in English and Russian, which may constrain generalization to other languages or multi-speaker scenes; the retrieved text does not state additional failure modes.

---

## Long-horizon Video Generation with Slot Memory Addressed By Region Tokens
- **arXiv:** 2610.19257 · https://arxiv.org/abs/2610.19257
- **Submitted:** 2026-10-13
- **Authors:** Eren Cetin, Julius Erbach, Vukasin Bozic, Hyojun Go, Zixiang Zhao, Nikolai Kalischek, Federico Tombari, Konrad Schindler, Dominik Narnhofer
- **Qualifying affiliation(s):** Google — Hyojun Go, Nikolai Kalischek, Federico Tombari (each listed with a joint "ETH Zurich / Google" affiliation note)
- **Categories:** cs.CV
- **Open release:** none found (no code repository or project page link located in the retrieved text)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper introduces SMART, a slot-based memory for long-horizon video generation that keeps constant storage size while still supporting accurate recall of content when a camera revisits a previously seen location. It avoids building an explicit 3D representation or a growing cache. Recall quality depends on inter-view geometry rather than how recently content was seen.
**Purpose (≤3 sentences):** The authors target a core tension in long video generation: memory must stay bounded so generation can continue indefinitely, but it must also recall distant, previously observed content accurately regardless of elapsed time, which neither reconstruction-based nor purely recurrent memories do well.
**Breakthrough (≤3 sentences):** The authors report that on long trajectories in Memory Maze and Minecraft, SMART achieves high-fidelity recall beyond the training horizon while maintaining constant memory size and per-step computational cost.
**Tools & method (≤3 sentences):** Memory writes are indexed by the observing camera and reads are queried by the rendering camera; each read also produces a confidence score that conditions a chunk-causal diffusion transformer, letting it selectively trust retrieved memory content versus falling back on its generative prior; evaluated in Memory Maze and Minecraft environments.
**Limitation (≤3 sentences):** The authors acknowledge that fixed slot capacity bounds the spatial extent the model can retain, so in large environments different regions must reuse the same slots and earlier content can be overwritten; they also note their experiments used relatively modest generator backbones, leaving scaling to larger video models as future work.

---

## Decoupled Drift-Diffusion World Models for Consistent Future Frame Prediction
- **arXiv:** 2610.19212 · https://arxiv.org/abs/2610.19212
- **Submitted:** 2026-10-13
- **Authors:** Anton Arapin, Aditya Singh, Yixin Wang, Jun Gao, Bernadette Bucher
- **Qualifying affiliation(s):** NVIDIA — Jun Gao (all five authors are also listed with University of Michigan)
- **Categories:** cs.CV
- **Open release:** project page at https://anton-arapin.github.io/d3wm-site/; the paper's AI-use statement mentions "polishing code for the release" but no code repository link was found yet
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** D3WM (Decoupled Drift-Diffusion World Model) predicts future video frames conditioned on action sequences by combining a deterministic transformer prediction with a diffusion model gated by a learned spatial uncertainty map. Predictable regions stay anchored to the deterministic prediction, while uncertain regions (e.g., disocclusions, dynamic textures) are generated by the diffusion process. The authors frame this as a variance-gated stochastic differential equation separating deterministic drift from stochastic diffusion.
**Purpose (≤3 sentences):** The goal is more consistent future-frame prediction in action-conditioned world models, avoiding both over-smoothed deterministic predictions and unnecessary stochastic variation in parts of a scene that are actually predictable.
**Breakthrough (≤3 sentences):** The authors report that D3WM shows improved results over competitive baselines across two distinct types of action spaces, and that the spatial location of stochastic changes is itself learnable rather than fixed.
**Tools & method (≤3 sentences):** A transformer trained with a Gaussian negative-log-likelihood objective outputs both a deterministic next-state prediction and a spatial aleatoric-uncertainty map; that map gates a conditional diffusion model; the method is evaluated on robotic tabletop manipulation and camera-motion prediction tasks using two reference input views.
**Limitation (≤3 sentences):** The authors note the model produces only a single frame per query, limiting assessment of intermediate states; it assumes scene changes are driven entirely by the input actions, not modeling independent predictable dynamics; and it currently takes only two reference views, with other view counts and modalities beyond RGB left as future work.

---

## Into the LidarVerse: A Real-Time Unified LiDAR World Model Across Tasks and Sensors
- **arXiv:** 2610.19201 · https://arxiv.org/abs/2610.19201
- **Submitted:** 2026-10-13
- **Authors:** Henry Che, Xuanchi Ren, Sanja Fidler, Shenlong Wang, Laura Leal-Taixé, Shengyu Huang
- **Qualifying affiliation(s):** NVIDIA — Henry Che, Laura Leal-Taixé, Shengyu Huang
- **Categories:** cs.CV, cs.RO
- **Open release:** project page at https://research.nvidia.com/labs/sil/projects/lidarverse; no separate code repository for LidarVerse itself was found (it uses NVIDIA's existing Cosmos-Drive-Dreams toolkit only as a preprocessing dependency)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** LidarVerse is a single conditional generative world model for simulating LiDAR sensor data, intended to combine the accuracy of per-scene reconstruction methods with the scalability of generative approaches. It conditions on past LiDAR frames, HD maps, and a spatial memory. Its tokenizer is designed to handle multiple beam counts (32-, 64-, and 128-beam sensors).
**Purpose (≤3 sentences):** The authors aim for a unified, real-time LiDAR world model that generalizes across driving-simulation tasks and sensor configurations, rather than requiring per-scene fitting (as reconstruction methods do) or sacrificing long-sequence consistency (as prior generative methods do).
**Breakthrough (≤3 sentences):** The authors report state-of-the-art results on most metrics across three evaluation protocols, that the model can be distilled into a faster autoregressive student running at about 11 FPS on a single H100 GPU, and that the tokenizer generalizes to an unseen scan pattern it was not trained on.
**Tools & method (≤3 sentences):** The model conditions on past LiDAR frames, HD maps, and a spatial memory to generate future LiDAR observations; it is distilled into an autoregressive student model for real-time inference; NVIDIA's Cosmos-Drive-Dreams toolkit is used for LiDAR-to-range-map preprocessing.
**Limitation (≤3 sentences):** The authors acknowledge LidarVerse models only a single spinning LiDAR, leaving solid-state sensors and multi-LiDAR rigs as future work; it depends on annotated object poses for dynamic resimulation, limiting use on unlabeled scenes; and it currently generates LiDAR only, not synchronized camera and LiDAR observations together.

---

## Imagining Goals with Geometric Horizon Models for Policy Generalization
- **arXiv:** 2610.19129 · https://arxiv.org/abs/2610.19129
- **Authors:** Daniel Lawson, Dhruv Sreenivas, Adriana Hugessen, Khimya Khetarpal, Glen Berseth
- **Submitted:** 2026-10-13
- **Qualifying affiliation(s):** Google DeepMind — Khimya Khetarpal (listed as "Equal Advising"; also affiliated with Mila and Université de Montréal); other authors are Mila-affiliated
- **Categories:** cs.LG, cs.AI
- **Open release:** project page at https://td-aug.github.io; no code repository link found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper addresses zero-shot goal generalization in goal-conditioned reinforcement learning, where a policy must handle unseen tasks by composing existing skills. It proposes TD-Aug, which samples from a geometric horizon model (GHM, also called a γ-model) — a generative model of the distribution of future states a policy can reach — to imagine novel goal outcomes reachable by stitching together known skills. These imagined outcomes are then used to train goal-conditioned behavioral-cloning policies.
**Purpose (≤3 sentences):** Generating new, longer-horizon experience with world/horizon models has been difficult, which limits how well policies generalize to goals not seen during training; TD-Aug aims to make this kind of imagined-goal data generation practical for stitching-style generalization.
**Breakthrough (≤3 sentences):** On OGBench stitching tasks, the authors report average success rising from 31% to 79% on state-based pointmaze-stitch tasks (e.g., pointmaze-giant-stitch from 0% to 54%), from 29% to 56% on visual-antmaze navigation, and from 13% to 52% on manipulation (cube/puzzle) stitching tasks, in each case comparing TD-Aug against a goal-conditioned flat behavioral-cloning baseline.
**Tools & method (≤3 sentences):** Geometric horizon models are trained via temporal-difference learning combined with flow matching (TD-Flows) and sampled in a small number of steps; GHM samples serve as augmented imagined goals for training goal-conditioned behavioral-cloning policies; evaluation uses the OGBench suite (state-based and visual maze navigation, and manipulation tasks).
**Limitation (≤3 sentences):** The authors note the MCHC training objective is a biased approximation of the target successor measure, with bias growing as the horizon parameter increases; their visual-setting variant (TD2-β) underperforms, which they attribute to bootstrapping in latent space; and they identify scaling TD-based GHM training stably to high-dimensional, partially observable robotics tasks as an open challenge.

---

## WorldMemBench: A Comprehensive Benchmark for Memory of Video World Models
- **arXiv:** 2610.19063 · https://arxiv.org/abs/2610.19063
- **Submitted:** 2026-10-13
- **Authors:** Nan Zhou, Jianxiong Gao, Qiuyu Wang, Wen Wang, Jiahao Wang, Yufeng Yuan, Shuaiting Li, Hao Ouyang, Yujun Shen, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen
- **Qualifying affiliation(s):** Ant Group — Nan Zhou, Jianxiong Gao, Qiuyu Wang, Jiahao Wang, Yufeng Yuan, Shuaiting Li, Hao Ouyang, Yujun Shen; FLAG: borderline — Ant Group
- **Categories:** cs.CV
- **Open release:** homepage https://zju-real.github.io/WorldMemBench/ · code https://github.com/ZJU-REAL/WorldMemBench · dataset https://huggingface.co/datasets/rescuerz/WorldMemBench
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** WorldMemBench is a benchmark testing whether video world models remember their own past, spanning 260 test cases. It covers static memory (retaining people, objects, environments) and dynamic memory (tracking how events unfold and how states persist), using camera departures and repeated revisits to probe recall.
**Purpose (≤3 sentences):** The authors argue that world memory is a critical capability to evaluate in video world models alongside visual fidelity and video duration, and built this benchmark because existing evaluation did not systematically test it.
**Breakthrough (≤3 sentences):** Evaluating nine video world models (including HY-WorldPlay, Matrix-Game 3, Matrix-Game 3.5, SANA-WM, YUME, LingBot-World, LingBot-World-v2, Evoke, and DreamX-World), the authors report that good static content retention does not guarantee reliable dynamic state tracking, and that memory reliability degrades over repeated revisits; human studies corroborated the automatic evaluation metrics.
**Tools & method (≤3 sentences):** Static content is checked against fixed reference images and dynamic events against expected state changes, combining appearance and geometry metrics with event-specific checks; video quality and camera-following accuracy are reported as supplementary measures; the benchmark, code, and dataset are publicly released.
**Limitation (≤3 sentences):** The paper's conclusion section does not state limitations directly and instead points to an appendix ("Limitation and Future Work") whose content was not available in the retrieved text; no further detail can be reported without guessing.

# Near-misses
- 2610.19425 · Evaluating Agentic Capabilities Before Post-Training: An End-to-End Approach · off-topic: this is a generic LLM-agent evaluation framework (ASAP) for software-engineering/deep-research coding-agent benchmarks tied to pretraining checkpoints — not about 3D, world models, character animation, or game engines despite the "agentic" framing.
- 2610.19120 · DoReMe: Dual optimization of Reconstruction and Motion estimation for self-navigating free-breathing abdominal MRI · off-topic: despite using "Gaussian Splatting," this is a medical-imaging (MRI motion correction) paper, with authors from University of Tuebingen and Siemens Healthineers.
- 2610.18991 · Contact-UAN: Unsupervised Actuator Networks as a Residual World Model for Humanoid Control · no industry co-author — all five authors list a single affiliation, Improbable AI Lab, MIT; the NVIDIA hint did not check out, and no qualifying company affiliation was found.
