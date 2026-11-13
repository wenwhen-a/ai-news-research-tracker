**[A06] VibePrevisBench: Evaluating Agentic Coding for 4D Scene Generation in Blender**
- **arXiv:** 2611.15789 · <https://arxiv.org/abs/2611.15789>
- **Submitted:** 2026-11-11
- **Authors:** Yuzhe Chen et al.
- **Qualifying affiliation(s):** Kuaishou (Kling AI) — paper lists "Kling AI" as one of five author affiliations, with Yuzhe Chen's work explicitly "conducted during the author's internship at Kling AI." FLAG: borderline — the HTML extraction could not cleanly map every author to a numbered affiliation (no visible superscripts), so the full author↔institution mapping beyond Yuzhe Chen's internship footnote is inferred, not directly confirmed from the text.
- **Categories:** cs.CV (primary), cs.AI
- **Open release:** project page (vibeprevisbench.github.io); tasks/media/ground truth/scorer stated to be "frozen with checksums" for reproducibility "from the release" — no explicit code/data repo link found in fetched text
- **Shipped counterpart:** none found (the paper cites Kuaishou's "Kling 4.0" and "Seedance 2.5" only as existing third-party video generation models used downstream of the Blender proxy video, not as something this paper ships into)

**Summary:** The paper introduces VibePrevisBench, a 242-task benchmark that asks coding agents to turn a text/photo/video brief into an executable 4D scene in Blender and render a proxy ("previs") video.
**Purpose:** Proxy-conditioned video generation pipelines depend on getting the underlying 4D scene right, but no existing benchmark checks both the generated proxy video and the longer, multi-shot scene logic behind it.
**Breakthrough:** The authors report top overall scores of 77.7 (GPT-6 Astra), 76.1 (GPT-6.1 Sol), 75.0 (Gemini 4 Argon), and 74.1 (Opus 5.5), with the best-of-all-agents overall score only 80.6 and just 35 of 242 tasks reaching a 90+ Scene Check score for any agent.
