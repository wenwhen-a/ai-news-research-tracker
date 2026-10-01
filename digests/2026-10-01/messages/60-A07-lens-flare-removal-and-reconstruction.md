**[A07] Lens Flare Removal and Reconstruction**
- **arXiv:** 2609.39527 · <https://arxiv.org/abs/2609.39527>
- **Submitted:** 2026-09-30
- **Authors:** Tarun Yenamandra et al.
- **Qualifying affiliation(s):** Meta — Jonathon Luiten (Meta Reality Labs, New York) and Nathan Matsuda (Meta Reality Labs Research, Redmond); Tarun Yenamandra's work was done during a Meta Reality Labs Research internship, with primary affiliation TU Munich (MCML)
- **Categories:** cs.CV; cs.GR
- **Open release:** demo — project page at <https://lensflare-3dgs.pages.dev> (per the arXiv Comments field: "20 pages, 14 figures. Project page: [this https URL]"); no GitHub code link found
- **Shipped counterpart:** none found

**Summary:** Lens flares are camera artifacts that degrade downstream applications such as 3D scene reconstruction, and existing removal methods handle small flares but struggle with large, full-frame reflective flares; consistent flare representation across multiple viewpoints had not previously been explored.
**Purpose:** The authors want to both remove large reflective lens flares from individual images and model flares explicitly in 3D so they can be edited, removed, or transferred consistently across views and scenes during multi-view/Gaussian-splatting reconstruction.
**Breakthrough:** The authors report PSNR of 26.68 dB on the Flare7K++ benchmark and 27.06 dB on their new VFX benchmark, stated to outperform prior methods, while their flare removal model trains in about 20 hours versus more than 4 days for baselines.
**Tools & method:** The removal model is a Difix3D+ diffusion model fine-tuned with LoRA on a combined dataset of real large reflective flares (1,866 images from 90 ActionVFX visual-effects clips) and procedurally generated flares, plus the clean Flickr24K dataset.
