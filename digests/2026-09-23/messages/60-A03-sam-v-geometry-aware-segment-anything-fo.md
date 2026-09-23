**[A03] SAM-V: Geometry-Aware Segment Anything for Multi-View Instance Segmentation**
- **arXiv:** 2609.25490 · <https://arxiv.org/abs/2609.25490>
- **Submitted:** 2026-09-21
- **Authors:** Jiangshan Gong et al.
- **Qualifying affiliation(s):** Meta — affiliation listed on the paper (specific author not distinguished in the visible author block; primary team is University of Illinois Urbana-Champaign); FLAG: borderline — Meta co-authorship confirmed on the page but not cleanly attributed to a specific named author in the fetched content
- **Categories:** cs.CV, cs.LG
- **Open release:** code + weights — "Our code and pretrained models are available" at <https://github.com/gong208/SAM-V.git>
- **Shipped counterpart:** none found

**Summary:** SAM-V integrates a feed-forward geometry model (VGGT) into the Segment Anything (SAM) foundation model, training the combination end-to-end for consistent object segmentation across multiple camera views in a single forward pass.
**Purpose:** The paper targets consistent multi-view object segmentation for 3D perception and robotics applications, where evaluating views independently cannot guarantee they describe the same object instance across viewpoints.
**Breakthrough:** The authors report SAM-V achieves "5 points [improvement in] overall IoU and 12 points on frame-level recall" over baselines on ScanNet++ (IGGT benchmark), plus leading performance in zero-shot evaluation on ScanNet, as they state it.
**Tools & method:** SAM-V fuses frozen SAM (ViT-H) and VGGT encoders via a trainable MLP feature-fusion module and a cross-attention prompt-fusion module that combines camera tokens with local VGGT features; only the fusion modules and SAM's mask decoder are trained, with a combined focal, Dice, and IoU-prediction loss.
