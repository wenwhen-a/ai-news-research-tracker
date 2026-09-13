---
name: research-paper-tracker
description: Two-part tracker for 3D, world models, character animation, and game engines from top industry labs (Google/DeepMind, Microsoft, Meta, NVIDIA, Apple, Adobe, Tencent, ByteDance, miHoYo, NetEase, Alibaba, Sony, Ubisoft, EA, Roblox, Unity, Epic, etc.). Part A covers arXiv papers from the last 30 days with at least one tracked-company author (academic-only papers excluded). Part B covers research that has become a real product (consumer app features, cloud APIs, engine releases, studio tools, shipped games) from the same companies over the last 90 days, verified from primary sources and linked to the underlying papers; open-weights drops are noted in Part A, not Part B. Use whenever the user asks to catch up on or get a digest of recent papers, what tracked companies have shipped or released, research-to-product or engineering progress in these areas, or for a scheduled tracking task. Both parts run by default. Five objective blocks per item, no hype, never fabricates.
---

# Research Paper & Product Tracker

> Self-contained: helper scripts live in `scripts/`, source lists and criteria in `references/`.

## Goal
Produce one digest with two sections:

- **Part A — Papers (last 30 days):** arXiv papers on **3D, world models, character animation, game engines** from **qualified teams** (below), five objective blocks each.
- **Part B — Research → Product (last 90 days):** **final products** — consumer apps/features (2C) or paid/enterprise services, cloud APIs, studio tools and engine features (2B) — in the same four areas from a **qualified company**, verified from a primary source, five objective blocks each, linked to underlying papers where traceable. Open-weights/code releases and research demos are **not** Part B items; they are noted on the paper's `Open release:` line in Part A.

Both parts run by default unless the user asks for one. Two co-equal priorities for both: **factual accuracy** (every paper, product, date, affiliation, and claim verified against the primary source) and **not missing qualifying items** (search broadly). Never fabricate or pad. Few or zero items is an acceptable result.

## Qualified companies (the affiliation gate, shared by both parts)
- **Big tech:** Google / DeepMind, Microsoft, Meta / FAIR / Reality Labs, Amazon, Apple, NVIDIA, Adobe, Intel, Qualcomm.
- **Top gaming & Chinese tech:** Tencent, ByteDance / TikTok, miHoYo / HoYoverse, NetEase, Alibaba, Baidu, Kuaishou, Sony, Ubisoft, Electronic Arts, Roblox, Unity, Epic Games.

Rules:
- The list is illustrative. Other clearly top-tier industry labs of comparable standing count. When unsure (e.g. JD.com, Ant Group, StepFun), **keep the item and add a one-line flag** for the user to judge rather than silently dropping or including.
- Part A: any one industry co-author is enough; the first author need not be from industry; a purely academic paper does **not** qualify.
- Part B: the company selling or operating the product must be a qualified company (or a clearly comparable one, flagged). Academic releases and third-party wrappers of a tracked model do not count.
- Affiliation/ownership must be **verified against the primary source** (paper author block; company blog/docs/release page), never inferred from a name or topic.

## Tools
- **Code execution** — `scripts/arxiv_fetch.py` (Part A candidates via arXiv API) and `scripts/github_releases.py` (Part B candidates via GitHub Releases API for tracked orgs). Both are stdlib-only and exit non-zero with a clear message if their host is blocked.
- **Web fetch** — verify every candidate against its primary source (arXiv abstract/HTML page; company blog, docs, release notes, model card).
- **Web search** — fallback retrieval when an API is blocked, and the main retrieval path for company blogs/newsrooms that have no API. Trade press is used only as a lead back to a primary source, never as the source itself.

## Part A — Papers (unchanged procedure, summarized)
1. **Plan.** Today (UTC), cutoff = today − 30 days. Categories: cs.GR, cs.CV, cs.LG, cs.AI, cs.RO.
2. **Fetch.** `python scripts/arxiv_fetch.py --as-of <today>` → `arxiv_candidates.json`. If the API host is blocked (it is in some sandboxes), fall back to the website: `arxiv.org/list/<cat>/recent`, `arxiv.org/list/<cat>/new`, the monthly listings `arxiv.org/list/<cat>/YYYY-MM`, targeted searches per topic phrase, and curated trackers (Hugging Face papers, alphaXiv, Awesome-World-Model lists) as **leads only**. State in the header which path was used and any coverage gap.
3. **Verify each candidate** by fetching its abstract page (and HTML/PDF first page for affiliations): (a) v1 submission date in window, (b) at least one qualifying author affiliation read from the paper, (c) genuinely on one of the four topics, (d) real arXiv record with matching title/authors. Drop anything that fails.
4. **Extract** only what the paper states: problem, method, contribution, tools/datasets/hardware, acknowledged limitations.
5. **Write** five blocks per paper (format below), newest first.
6. **Double-verify** every included paper before delivering; state that the pass was done.
7. **Empty case:** say so plainly; never lower the bar or widen the window. List near-misses dropped for lacking an industry author.

## Part B — Research → Product (new)
Read `references/product-criteria.md` (what counts as a product, status tiers, paper-linking rules) and `references/product-sources.md` (per-company product surfaces and primary sources) before starting. The bar is "a customer or developer can use it today": apps, app features, cloud APIs, engine releases, studio tools, plugins, shipped games with documented new tech.

1. **Plan.** Cutoff = today − 90 days. Load the previous run's `product_seen.json` if present (see step 6).
2. **Fetch candidates.**
   - `python scripts/github_releases.py --as-of <today> --days 90` → `github_release_candidates.json`. This is a **lead generator only**, useful for engine/SDK/plugin releases (Unity, NVIDIA SDKs, Roblox, EA); most hits will be research repos, which are Part A material, not Part B.
   - Walk `references/product-sources.md`: for each company, check its product pages, changelogs/release notes, cloud model catalogs, app-store notes and newsroom for items in the window on the four topics. Use trade press only to find primary links.
   - Also mine Part A: any paper whose abstract, project page, or company blog says the method "ships in", "is available in", "powers" a named product is a Part B lead.
3. **Verify each candidate** against a **primary source** (company blog/newsroom, official docs or release notes, official GitHub release, official model card). Confirm: (a) release date in window, (b) releasing org is a qualified company (flag borderline), (c) on-topic, not keyword-matched, (d) **status tier** per `product-criteria.md` — **Shipped**, **Public release**, or **Announced only**. Drop anything that cannot be verified from a primary source.
4. **Link to research.** Search for the underlying paper(s): the release page's citations, the company's research blog, arXiv search on the product/method name. Record the arXiv link if found; otherwise write "no traceable paper" — never guess a paper.
5. **Write** five blocks per item (format below), newest first. GA and Public-beta items go in the main list; Announced-only items go in a short trailing list (title · company · date · source), no blocks.
6. **Dedup across runs.** Items are keyed by primary-source URL. Anything present in `product_seen.json` from a prior run is marked **Previously reported** and collapsed to one line; new items are marked **New**. After delivering, write all keys (old + new) back to `product_seen.json` in the working/output directory.
7. **Cross-link.** Annotate Part A papers that already have a Part B counterpart ("→ shipped as …") and Part B items that cite a Part A paper ("← paper in Part A"). Fill each Part A paper's `Open release:` line (weights / code / demo / none) so open releases are still visible without polluting Part B.
8. **Double-verify** every included item (URL resolves to the stated primary source; date, company, tier, and every claim supported). State that the pass was done.
9. **Empty case:** if nothing qualifies in 90 days, say so; optionally list announced-only items and near-misses (academic releases, unverifiable claims).

## Objectivity rules (both parts)
- No unsupported adjectives ("novel", "powerful", "state-of-the-art", "game-changing") unless immediately grounded in a stated fact with a number, benchmark, or source.
- Attribute comparative and performance claims: "the authors report…", "NVIDIA states…". Company marketing claims are reported as claims, not facts.
- Prefer numbers, names, dates, platforms, prices, licenses over adjectives.
- Limitations: prefer those the source acknowledges; mark added scope limits as "(observed, not stated)".
- Preserve official names, arXiv IDs, and URLs exactly. If a detail can't be verified, omit it.

## Output format (plain Markdown, one digest)

```
# Part A — Papers
Window: last 30 days (<cutoff> to <today>). Categories: cs.GR, cs.CV, cs.LG, cs.AI, cs.RO. Retrieval: <API | website fallback>. Qualifying papers: <N> (<n flagged>).

---
## <Paper Title>
- **arXiv:** <id> · <abs_url>
- **Submitted:** <v1 date>
- **Authors:** <list>
- **Qualifying affiliation(s):** <company — author(s)>; flag if borderline
- **Categories:** <cats>
- **Open release:** weights | code | demo | none (with link)
- **Shipped counterpart:** <Part B item or "none found">

**Summary (≤3 sentences):** …
**Purpose (≤3 sentences):** …
**Breakthrough (≤3 sentences):** … (attributed)
**Tools & method (≤3 sentences):** …
**Limitation (≤3 sentences):** …

[near-misses line; verification statement]

# Part B — Research → Product
Window: last 90 days (<cutoff> to <today>). Qualifying products: <N> (<new> new, <prev> previously reported, <k> flagged). Announced-only: <m>. Open releases moved to Part A: <j>.

---
## <Product / feature / release name>
- **Company:** <name> (flag if borderline)
- **Status:** GA | Public beta/preview · **Released:** <date> · **New / Previously reported**
- **Surface:** <app / cloud API / engine / studio tool / shipped game>
- **Primary source:** <url>
- **Underlying research:** <arXiv link(s) + title> | "no traceable paper" (← Part A if applicable)
- **Availability:** <platforms, license, pricing tier, regions, beta/GA>

**What shipped (≤3 sentences):** …
**What research it translates (≤3 sentences):** …
**Practical significance (≤3 sentences):** … (claims attributed)
**Engineering details (≤3 sentences):** formats, integrations, engine versions, hardware
**Limitation / caveats (≤3 sentences):** …

### Announced only (not yet usable)
- <name> · <company> · <date> · <source>

[near-misses line; verification statement]
```

## Scheduled / delivered runs
If a destination is given (email, Slack, doc), send the same verified content in that channel's shape: title+link list up top for each part, then details. Persist `product_seen.json` alongside the output so the next run can mark items Previously reported.

## Helper scripts
- `scripts/arxiv_fetch.py` — see docstring. `python scripts/arxiv_fetch.py --as-of 2026-09-12 --days 30`.
- `scripts/github_releases.py` — see docstring. `python scripts/github_releases.py --as-of 2026-09-12 --days 90 --out github_release_candidates.json`. Repo list lives in `references/product-sources.md` (the `github:` lines); the script parses that file.
