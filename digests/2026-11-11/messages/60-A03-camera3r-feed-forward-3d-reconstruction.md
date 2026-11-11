**[A03] Camera3R: Feed-Forward 3D Reconstruction from Heterogeneous Camera Models**
- **arXiv:** 2611.13453 · <https://arxiv.org/abs/2611.13453>
- **Submitted:** 2026-11-10
- **Authors:** Ruxiao Duan, Yunwen Zhou, Erin Hong, Dongxu Zhao, Eric Turner, Federico Tombari, Alex Wong
- **Qualifying affiliation(s):** Google — Yunwen Zhou, Erin Hong, Dongxu Zhao, Eric Turner, Federico Tombari (affiliation block lists "@google.com"; Ruxiao Duan and Alex Wong are dual-affiliated with Yale University)
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** Camera3R is a low-rank adaptation (LoRA) framework that extends feed-forward 3D reconstruction networks pretrained on perspective images to other camera models (fisheye, panoramic) without full retraining.
**Purpose:** Most feed-forward 3D reconstruction networks are trained only on perspective images and fail on fisheye or panoramic cameras; the authors adapt pretrained perspective models to heterogeneous camera geometries cheaply.
**Breakthrough:** Applied to the π³ baseline, the authors report relative rotation accuracy rising from 0.540 to 0.990 on the fisheye ADT benchmark and from 0.076 to 0.978 on the panoramic Stanford2D3DS benchmark, while adding ~0.5% extra parameters, training in under a day, and leaving perspective-image performance unchanged.
**Tools & method:** The framework uses synthetic cross-camera distortion augmentation with separate LoRA experts per camera category, trained on ScanNet++, ASE, KITTI360, Matterport3D, Gibson, TartanAirV2, and PanoCity, using 8 NVIDIA RTX 6000 Blackwell (48GB) GPUs.
**Limitation:** The authors state the method assumes each input image belongs to one of a predefined set of camera categories, so a new camera model requires training an additional LoRA expert; they also note the synthetic cross-camera distortion augmentation may not fully capture real lens- and sensor-specific effects.
