**[A01] GestureFAR: Streaming Co-Speech Gesture Generation with Flow Autoregression**
- **arXiv:** 2609.21576 · <https://arxiv.org/abs/2609.21576>
- **Submitted:** 2026-09-18
- **Authors:** Pinxin Liu, Haiyang Liu, Jiahao Luo, Junhua Huang, Chunhao Zou, Luchuan Song
- **Qualifying affiliation(s):** Meta — one author (exact name-to-affiliation mapping not resolvable from the rendered HTML; the paper lists five institutions — University of Rochester, University of Tokyo, UC Santa Cruz, UCLA, Meta — against six authors without a clear footnote pairing in the fetched content)
- **Categories:** cs.CV, cs.GR, cs.HC
- **Open release:** demo — <https://andypinxinliu.github.io/GestureFAR> (project page; no code/GitHub link found)
- **Shipped counterpart:** none found

**Summary:** GestureFAR is a streaming co-speech gesture generation system that produces body motion for conversational agents in real time, using continuous (not discretized) motion latents to avoid the "representation ceiling" the authors say discrete tokenization imposes.
**Purpose:** The authors state that streaming gesture generation must be strictly causal — using only past motion and currently available speech — while prior discrete-token systems trade away motion expressiveness for streamability.
**Breakthrough:** On the BEAT2 benchmark (speaker-22 split), the authors report their one-step distilled student model reaches FGD 3.08 versus 4.57 for LiveGesture and 8.06 for MIBURI (ground truth FGD is 0.703); on Audio2PhotoReal they report FGD 2.08, best among compared methods.
**Tools & method:** The tokenizer is a 1D causal VAE (128-dim latent, stride 4); the transformer is 8 layers (hidden size 384, 6 attention heads) with a lightweight MLP flow head (6.51M parameters).
**Limitation:** The authors do not provide a formal limitations section in the fetched content.
