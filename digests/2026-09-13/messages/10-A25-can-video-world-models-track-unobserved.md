**[A25] Can Video World Models Track Unobserved World States?**
- **arXiv:** 2608.30692 · https://arxiv.org/abs/2608.30692
- **Submitted:** 2026-08-31
- **Authors:** Joonghyuk Shin, Yicong Hong, Jaesik Park, Xun Huang
- **Qualifying affiliation(s):** Roblox — Yicong Hong, Xun Huang (co-authors at Seoul National University)
- **Categories:** cs.CV
- **Open release:** demo (project page https://joonghyuk.com/stateful-vwm-web/)
- **Shipped counterpart:** none found

**Summary:** Studies whether video world models maintain a hidden, unobserved world state rather than only producing plausible frames, using an action-conditioned "Shell Game" task, a visual analogue of S5 permutation-group state tracking that decouples rendering from tracking the underlying state.
**Purpose:** To determine which architectures can track unobserved state over long horizons and isolate the mechanism behind success or failure.
**Breakthrough:** The authors report that plain Transformers and Mamba fail to extrapolate state tracking beyond training length, while linear attention with negative eigenvalues and test-time training with nonlinear fast weights succeed; they also report the negative-eigenvalue mechanism does not transfer to Memory Maze and Block World, where state must be corrected from observations.
**Tools & method:** The Shell Game benchmark plus Memory Maze and Block World, comparing Transformer, Mamba, linear-attention and test-time-training video architectures.
**Limitation:** The authors state a real world model "has to correct its state from observations, keep it fixed when an action fails, and keep it evolving even when no action arrives," and that some prediction problems "plausibly require NC¹-hard state tracking," which none of the tested architectures capture.
