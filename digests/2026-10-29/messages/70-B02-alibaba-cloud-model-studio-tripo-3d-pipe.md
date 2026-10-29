**[B02] Alibaba Cloud Model Studio — Tripo 3D pipeline tools (Segmentation, SmartSegmentation, MeshCompletion, Retopology, ConvertFormat, RigCheck, AutoRig, AnimationRetarget, ImageToSplat, Texture)**
- **Company:** Alibaba Cloud (Model Studio) — **flagged:** the underlying models are built by Tripo/VAST, which is not itself a tracked company; Alibaba operates and sells access to them via its own cloud catalog, which is the basis for inclusion
- **Status:** GA (listed in Model Studio's self-serve "newly released models" catalog; no invite/whitelist marker found on the page) · **Released:** 2026-10-27 · **New**
- **Surface:** cloud API (Alibaba Cloud Model Studio / Bailian Open API)
- **Primary source:** <https://help.aliyun.com/zh/model-studio/newly-released-models>
- **Underlying research:** arXiv 2504.12451, "One Model to Rig Them All: Diverse Skeleton Rigging with UniRig" — the catalog's own description of Tripo-AutoRig cites "the UniRig algorithm"; no traceable paper found for the other nine tools
- **Availability:** Open API, China North 2 (Beijing) region; Tripo's base generation models (Tripo-P1.0, Tripo-H3.1) have been on this catalog since 2026-04-27, but these ten part/rig/animation pipeline tools are newly listed as of 2026-10-27

**What shipped:** Alibaba's Model Studio catalog added ten new Tripo-branded 3D-pipeline tools on 2026-10-27 — mesh segmentation (standard and semantically-controlled), mesh completion, retopology, format conversion, rig-compatibility checking, automatic rigging, animation retargeting (against 100 preset animations), image-to-Gaussian-splat conversion, and automatic PBR texturing — extending Tripo's existing base 3D-generation models into a fuller generate-to-animate pipeline.
