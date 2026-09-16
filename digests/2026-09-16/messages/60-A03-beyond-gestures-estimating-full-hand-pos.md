**[A03] Beyond Gestures: Estimating Full Hand Pose and Contact Forces from Wrist-Worn Pressure Sensor Array**
- **arXiv:** 2609.16518 · <https://arxiv.org/abs/2609.16518>
- **Submitted:** 2026-09-15 (v1)
- **Authors:** Svetoslav Kolev, Lingni Ma, Michael Goesele, Renzo De Nardi, Jakob Engel, Richard Newcombe
- **Qualifying affiliation(s):** Meta Reality Labs Research — all authors
- **Categories:** cs.HC; cs.RO
- **Open release:** none
- **Shipped counterpart:** none found

**Summary:** The paper presents a wrist-worn device using flexible capacitive sensor arrays (no electrical skin contact required) paired with a recurrent neural network to recover continuous full-hand pose and distributed contact force.
**Purpose:** The authors aim to complement camera-based hand tracking (e.g. egocentric cameras) with a wearable that also reports contact force and keeps working when the hand is occluded from view.
**Breakthrough:** The authors report the pressure signatures from muscle contraction and tendon displacement at the wrist correlate with hand movement and interaction forces; measured performance is 4.6° mean finger-joint MAE for isolated motion and per-finger contact-force estimation at R²=0.57 across users, improving to R²=0.75 when conditioned on external pose information.
**Tools & method:** A recurrent neural network is trained on synchronized data from a wrist-worn flexible capacitive pressure-sensor array, optical motion-capture, and tactile gloves, across isolated finger motions and everyday object-manipulation tasks with four users.
**Limitation:** The authors state that intrinsic hand muscles are largely invisible from forearm sensors, limiting observability of thumb motion; cross-user generalization could not be established due to small cohort size and mixed hardware; and tactile-glove ground truth does not cover lateral, dorsal, and webbing surfaces, and per-taxel force accuracy is bounded by the reference system.
