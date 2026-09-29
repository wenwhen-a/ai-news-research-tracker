**[A13] TrackEverything: Long Horizon Dense Tracking via De-Duplicating 3D Scene Representations**
- **arXiv:** 2609.30222 · <https://arxiv.org/abs/2609.30222>
- **Submitted:** 2026-09-24
- **Authors:** Ayush Jain et al.
- **Qualifying affiliation(s):** Meta — Fan Zhang, Tanner Schmidt, Jakob Engel, Adam W. Harley
- **Categories:** cs.CV, cs.AI, cs.RO
- **Open release:** none confirmed (project page only: <https://trackeverything.github.io/;> no code/weights link stated)
- **Shipped counterpart:** none found

**Summary:** TrackEverything is a 3D point tracker that represents video as persistent 3D scene tracks in world coordinates so that tracking cost is decoupled from video length, letting it track all visible points across full videos rather than only sparse query points or short clips.
**Purpose:** Existing point trackers force a tradeoff: track sparse query points over long videos, or track dense points only in short clips, because dense long-horizon tracking is memory-prohibitive.
**Breakthrough:** The authors report their method is "the first 3D tracker capable of tracking all visible points across videos exceeding 1000 frames within 40 GB of GPU memory," outperforms open-source all-frame dense 3D trackers "by more than 20% APD" on short clips, and remains competitive with sparse trackers on long sequences despite tracking orders of magnitude more points.
**Tools & method:** The method combines voxelization-based de-duplication (merging co-located tracks at sliding-window boundaries), an endpoint-then-trajectory decomposition (endpoint refiner plus a trajectory refiner limited to dynamic points), and "3D WAFT," a 3D extension of warp-aligned feature transforms replacing costly 4D correlation volumes; it is trained on Kubric, PointOdyssey, and Dynamic Replica and evaluated on TAPVid-3D, PointOdyssey, and Dynamic Replica, using 8 L40S-46GB GPUs for training and a single L40S for inference.
