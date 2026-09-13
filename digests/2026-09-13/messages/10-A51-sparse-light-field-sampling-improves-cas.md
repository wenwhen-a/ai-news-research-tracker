**[A51] Sparse Light Field Sampling Improves Casual 3D and 4D Reconstruction**
- **arXiv:** 2608.20602 · https://arxiv.org/abs/2608.20602
- **Submitted:** 2026-08-20
- **Authors:** Shamus Li, Ruiming Cao, Laura Waller, Kristina Monakhova, Sara Fridovich-Keil
- **Qualifying affiliation(s):** Adobe — Ruiming Cao
- **Categories:** eess.IV, cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary:** Studies why novel-view-synthesis pipelines use monocular input even though consumer devices carry several synchronised cameras, analysing sensor-limited and exposure-limited multi-camera capture for 3D and 4D reconstruction.
**Purpose:** To show that existing multi-camera hardware (phones, headsets, plenoptic cameras) improves single-shot, few-shot and casual-video reconstruction without new sensors.
**Breakthrough:** On synthetic NeRF-Blender data at one exposure the authors report 24.78 PSNR for light-field capture and 26.39 for a multiplexed setup versus 16.25 monocular; on dynamic real scenes, multi-view reaches 31.71 PSNR (iPhone) and 34.48 (stereo) versus 24.51 and 29.17 monocular.
**Tools & method:** Custom datasets from an iPhone 15 Pro (3 cameras), Apple Vision Pro (stereo) and a Lytro Illum (81 sub-views), plus a physical multiplexed light-field prototype; evaluated with 3DGS and 4DGS.
**Limitation:** The authors state benefits "diminish for distant content in large, unbounded scenes where disparity is minimal at more distant depths."
