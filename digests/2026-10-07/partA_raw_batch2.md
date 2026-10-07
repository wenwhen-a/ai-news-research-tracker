## DistScene: Object-to-Scene Distillation for 3D Scene Generation
- **arXiv:** 2610.06960 · https://arxiv.org/abs/2610.06960
- **Submitted:** 2026-10-03 (Sat, 3 Oct 2026 16:21:52 UTC)
- **Authors:** Kunming Luo, Hongyu Yan, Ken Deng, Chengcheng Zhou, Tianyu Liu, Haipeng Li, Haibin Huang, Xuelong Li, Ping Tan
- **Qualifying affiliation(s):** TeleAI / China Telecom — Chengcheng Zhou, Haibin Huang, Xuelong Li (Kunming Luo via internship); other authors: HKUST. **FLAG: borderline** — TeleAI/China Telecom is not on the tracker's explicit company list and its standing relative to tracked gaming/3D industry labs is unclear, so this is kept per the tracker's guidance for unsure industry labs rather than dropped.
- **Categories:** cs.CV
- **Open release:** none (project page lists code/checkpoint/dataset as "coming soon"; a HuggingFace preview-assets page exists: https://huggingface.co/coolbeam/DistScene-preview-assets)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** DistScene generates compositional 3D scenes from a single image by jointly producing separate environment and object components in a unified coordinate system, then refining objects and distilling object-level generative priors into the scene.
**Purpose (≤3 sentences):** It targets single-image 3D scene generation that preserves spatial coherence between objects and their environment alongside the fidelity of individual objects, which the authors say existing scene-level methods have not addressed well.
**Breakthrough (≤3 sentences):** The authors report improved spatial coherence over existing approaches on indoor (MIDI-test, Gen3DSR-test) and outdoor (UrbanScene3D) benchmarks, with additional qualitative evaluation on ScanNet.
**Tools & method (≤3 sentences):** Scene-Frame Generation jointly produces environment and object components, Object-Centric Refinement locally enhances each object with scene awareness, and Object-to-Scene Distillation transfers knowledge from pretrained object-generation models into the scene pipeline.
**Limitation (≤3 sentences):** The authors note indoor training assets generally omit ceilings (since reliable fully-enclosed empty rooms are hard to obtain from pretrained 3D object generators), which can yield open-top reconstructions of closed interiors, and that outdoor scenes lose fine geometric detail and may contain holes because a limited number of scene-frame voxels must cover a wide area, compounded by a smaller outdoor training set due to compute constraints.

---

# Near-misses
- 2610.06910 · GAMEGO: Training Game-Dev Agents with Synthetic Trajectories Anchored in Real-World Assets · off-topic despite a genuine Baidu affiliation (Jingyao Li, Zhengfan Wu, Jing Liu): this is a generic LLM coding-agent training/benchmark paper (synthetic-trajectory data generation and PRD construction for browser-game code synthesis), not a research contribution to 3D, world models, character animation, or game-engine technology itself.

**Verification note:** All leads were checked against their arXiv abstract page (title, authors, v1 date, categories, withdrawal status) and the arXiv HTML full text. Fourteen papers from this batch's original 15 leads were dropped entirely from this file (not near-missed) because a concurrent run already verified and reported them on 2026-10-06 (FLEX-WAM, CleanMDM, CreativeFlow, Lollypop, Neuroll, Sparse-View 4DGS, CurveCodec 2, SUAVE, SCCM) or already screened/decided them as near-misses that day (Universal Test-Time Training, Mobile-4DGS, LoCoSplat, the Lagrangian 3DGS-SPH solid-mechanics paper) — this session's local clone of `state/papers_seen.json` was stale at screening time; it was refreshed via `git merge origin/main` before this file was finalized, and only the genuinely new id (not in the refreshed `papers_seen.json`) is listed above.
