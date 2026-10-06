**[A11] Lollypop: Camera-to-Motion-Capture Calibration Verification with a Reference Target**
- **arXiv:** 2610.04785 · <https://arxiv.org/abs/2610.04785>
- **Submitted:** 2026-10-03
- **Authors:** Tianyi Liu, Kevin Harris, Mihika Dave, Kun He
- **Qualifying affiliation(s):** Meta — Tianyi Liu, Kevin Harris, Mihika Dave, Kun He (all four authors, Meta, Redmond, WA, USA)
- **Categories:** cs.CV
- **Open release:** none confirmed
- **Shipped counterpart:** none found

**Summary:** The paper introduces Lollypop, a fiducial-mocap reference target that independently verifies camera-to-motion-capture (mocap) calibration.
**Purpose:** The authors state that camera-to-mocap calibration is essential for using mocap as ground truth in robotics, AR/VR, and other computer vision tasks, but that calibration can drift after deployment while existing residual checks and visual inspection provide only limited independent verification.
**Breakthrough:** The authors report that their target achieves sub-pixel nominal accuracy, demonstrates measurable sensitivity to controlled extrinsic perturbations, and detects increasing error during a representative handling/drift scenario — providing an independent check beyond standard calibration residuals.
**Tools & method:** The verification procedure compares ArUco-detected fiducial corners (via 2D homography-warped canonical center) against a mocap-derived centroid projected through the full mocap-pose/camera-extrinsic/intrinsic transformation chain, reporting both 2D pixel-space and 3D metric-space error.
**Limitation:** The paper has no dedicated limitations section, but the authors note in their conclusion that "future work includes multi-point or non-coplanar reference targets and stronger depth observability," implying the current single coplanar target has limited depth-error sensitivity.
