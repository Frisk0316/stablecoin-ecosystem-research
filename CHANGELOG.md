# Changelog

## v0.3 slide script — 2026-05-15 (full speaker script)

Full speaker script for the 2026-06-27 reading-group session, expanded
from the v0.3 slide outline. Self-contained file at
`07_final_report/slide_script_v0_3.md`.

Content:

- 49 main slides + 3 appendix slides (52 slide entries total), grouped into
  9 sections (Part 0 Opening through Part 8 Closing plus Appendix).
- Each slide includes bilingual title, Chinese slide body (the text intended
  to appear on the rendered slide), bilingual speaker notes (English
  analytical content + Chinese delivery prompt), `CLAIM_XXX` source claim
  references, and `KF_XXX` key-figure references where applicable.
- Visual notes flagged for slides where a flow diagram or custom chart is
  recommended (Slides 14, 15, 17, 18, 38).
- Audience: academic-leaning reading-group members; rendered slides in
  Traditional Chinese; written documents in English.

Coverage statistics:

- 1,379 lines total
- 73 distinct `CLAIM_XXX` IDs cited (out of 106 claims in the table)
- 31 distinct `KF_XXX` IDs cited (out of 34 in `key_figures.csv`)
- MD032 lint clean (no heading-to-list adjacency)

Speaker checklist at end of file flags eight pre-session decisions: title
slide attribution, custom visual completeness, USDC reserve composition
data source, DAI/USDS and USDe flow diagrams (not yet in
`06_flow_diagrams/`), USDPT four-layer swim-lane Mermaid reuse, slide-cut
options for under-60-minute and over-90-minute sessions, and appendix
gating.

Remaining v0.4 candidates after this delivery: CLARITY Act stablecoin-
specific extraction, central-bank Taiwan synthesis, MiCA EMT
Articles 51 / 52 / 55, and (if obtainable) USDPT product layer plus
adjusted on-chain volume.

## v0.3 slide prep extended — 2026-05-15 (key figures + chapter 8 + comparison tables)

Three further slide-prep deliverables ahead of the speaker-script
expansion step.

- `07_final_report/key_figures.csv` (34 entries) extracts every
  slide-citable numerical figure from the claim base with the columns
  `figure_id, topic, figure, value, unit, as_of_date, source_id, claim_id,
  slide_relevance, notes`. Covers USDT reserve composition, GENIUS Act
  thresholds, MiCA ART/EMT thresholds, BoE backing splits and holding
  limits, NYDFS T+2, GUSD timely-redemption commitment, Ethena Reserve
  Fund size and multi-sig, sUSDe / BTC / ETH funding rate averages, Sky
  Savings Rate quotes, IMF event-study 18% / $300bn, ESMA CASP scrutiny
  thresholds, and project-state counters.
- `05_chapter_drafts/chapter_08_failure_cases.md` rewritten from a 23-line
  v0.1 skeleton to a 206-line v0.3 module. The risk taxonomy (8 categories)
  is now anchored to v0.3 claims; the specific case-study layer (Terra UST,
  Iron Finance, USDC SVB depeg, Tether reserve controversy, DAI Black
  Thursday) is explicitly marked as open and is **not** in the v0.3 source
  archive. v0.4 candidates are listed for prioritisation if the project is
  taken further.
- `07_final_report/comparison_table_slide_31.md` and
  `07_final_report/comparison_table_slide_32.md` export the chapter-4
  six-dimension cross-jurisdiction comparison table as two slide-ready
  tables (top half: eligible issuer / reserve composition / redemption
  right; bottom half: insolvency / holder yield / significant-token
  threshold), each with bilingual speaker notes and visual notes for the
  design step. Slide 32 also includes a combined six-row reference table
  for the case where a single-slide layout is preferred.

Slide outline updated:

- `07_final_report/slide_outline_v0_3.md` slides 44/45 reframed: failure
  cases now described as "risk taxonomy anchored to v0.3 evidence" and
  "lessons preserved as guardrails", with an explicit note that the
  case-study layer remains v0.4 open work.
- Markdown linting fix: blank lines inserted between every slide heading
  and its bullet list (MD032 compliance) across all 52 slide headings.

## v0.3 slide prep — 2026-05-15 (slide outline + flow diagram sync)

Prep deliverables for the upcoming Chinese-language slide deck for the
2026-06-27 reading-group session.

New artifact:

- `07_final_report/slide_outline_v0_3.md` — bilingual 49-slide + 3-appendix
  outline, with English / Chinese title pairs, one-line Chinese takeaways,
  and `CLAIM_XXX` source-claim references per slide. Structured in 8 parts
  (Opening, Issuer ecosystem, Reserves, Law and regulation, Central-bank
  framing, USDPT, On-chain data, Closing) plus appendix slides for claim
  map / disclaimer / source registry.

Flow diagram v0.3 sync pass:

- `06_flow_diagrams/tokenized_money_system_flow.md` redrawn to make the
  three product categories from chapter 1.3 visually explicit (fiat-backed,
  crypto / RWA-collateralised, synthetic-dollar) and to overlay the
  regulatory perimeter (GENIUS / MiCA EMT / BoE / NYDFS).
- `06_flow_diagrams/usdpt_settlement_flow.md` redrawn as a four-swim-lane
  hypothesis map (customer remittance UX, WU agent network, stablecoin
  issuance and on-chain transfer, reserve and bank / correspondent
  settlement) with solid arrows for v0.3-confirmed edges and dashed arrows
  for the speculative linkages that workflow documentation would need to
  confirm before any "replaces SWIFT / correspondent banking" framing can
  be supported.
- The other four flow diagrams (`correspondent_banking_flow.md`,
  `western_union_traditional_flow.md`, `reserve_asset_flow.md`,
  `stablecoin_issuance_redemption_flow.md`) reviewed and found accurate
  against the v0.3 claim base; not edited.

Tooling:

- New helper script `08_scripts/check_mermaid.py` runs a light structural
  check on all Mermaid blocks under `06_flow_diagrams/`. All six diagrams
  pass at the v0.3 cut-off.

## v0.3 wrap-up — 2026-05-15 (Claude Code chapter 1/9 and exec summary)

Final v0.3 narrative wrap-up ahead of slide-deck handoff. No new claims;
existing 106 claims rolled into finished prose at the report-frame
boundaries.

Updates:

- `07_final_report/executive_summary.md` rewritten from v0.1 to v0.3
  state, with headline findings anchored to the 106-claim base and an
  explicit limitations / unresolved-questions section. Replaces the
  stale v0.1 wording that flagged NYDFS / IMF / Fed as still
  outstanding.
- `05_chapter_drafts/chapter_01_stablecoins_as_onchain_dollar_system.md`
  expanded from a 13-line working thesis into a full introduction
  chapter covering framing, motivation (GENIUS Act enactment, MiCA in
  force, BoE 2025 consultation, USDPT announcement), the three
  product categories that must be kept separate, five recurring
  conflations the report guards against, a chapter-by-chapter roadmap,
  and a note on method and traceability.
- `05_chapter_drafts/chapter_09_conclusion.md` expanded from an 11-line
  draft-direction note into a structured conclusion with six
  high-confidence findings (each anchored to claim ranges), two
  conditional findings (USDPT, adjusted volume), five unresolved
  items, three framing points for the reading-group discussion, and
  suggested v0.4 directions.

User decisions captured for slide handoff:

- Audience: academic-leaning reading-group members.
- Slide count: unconstrained at this stage; trimming deferred.
- Language: bilingual delivery — English written documents
  (executive summary, chapter drafts) and Chinese slides. The
  English documents in this wrap-up are positioned as the
  authoritative narrative; the Chinese slides will derive from
  them in a subsequent step.

## v0.3 interim — 2026-05-14 (Claude Code protocol + comparison batch)

Phase 1d protocol extraction adding `CLAIM_098` to `CLAIM_106`:

- MakerDAO Multi-Collateral Dai (MCD) Protocol (`DAI_USDS_002`):
  governance-approved collateral / Maker Vault overcollateralisation
  (`CLAIM_098`); automated Collateral Auction / Reverse Collateral
  Auction liquidation with Protocol Surplus or MKR dilution backstop
  (`CLAIM_099`); Dai Savings Rate global parameter and Sky Savings Rate
  rebrand via sUSDS (`CLAIM_100`); Keepers / Oracles / Global Settlers
  external-actor surface area (`CLAIM_101`).
- Sky.money product page (`DAI_USDS_004`): post-MakerDAO Sky rebrand
  describing USDS / sUSDS / stUSDS / SKY plus 1:1 USDC↔USDS conversion
  and US-jurisdiction unavailability of yield modules (`CLAIM_102`).
- Ethena USDe documentation (`USDE_004`, `USDE_005`, `USDE_007`):
  synthetic-dollar delta-neutral hedging at 1:1 collateralisation
  (`CLAIM_103`); Off-Exchange Settlement custody mitigating but not
  eliminating exchange counterparty risk (`CLAIM_104`); monthly
  custodian attestations stating no backing assets reside directly on
  exchange partners (`CLAIM_105`); Reserve Fund composition, 4/10
  multi-sig control, Q4 2024 size $46.6m (`CLAIM_106`).

Chapter 4 cross-jurisdiction comparison table added: GENIUS Act vs MiCA
ART vs MiCA EMT vs BoE systemic vs NYDFS guidance along six dimensions
(eligible issuer, reserve composition, redemption right, insolvency /
wind-down, holder yield / interest, significant-token threshold), each
cell anchored to one or more CLAIM IDs.

Downstream artifacts updated:

- `02_source_digests/issuer_source_digest.md` DAI/USDS and USDe sections
  rewritten with `CLAIM_098`-`CLAIM_106`.
- `04_matrices/issuer_comparison_matrix.csv` DAI/USDS and USDe rows
  rewritten with protocol-mechanics, custody, attestation, and Reserve
  Fund cites.
- `05_chapter_drafts/chapter_02_issuer_comparison.md` extended with
  USDe peg-stability mechanics and DAI/USDS protocol-mechanics
  paragraphs.
- `05_chapter_drafts/chapter_03_reserve_assets_and_money_markets.md`
  extended with Paxos / GUSD / GENIUS / BoE reserve-composition rules
  plus a guardrail paragraph separating fiat-backed from
  crypto/RWA-collateralised and synthetic-dollar reserve channels.
- `05_chapter_drafts/chapter_04_law_and_regulation.md` cross-jurisdiction
  comparison table added; "Remaining work" section pruned to CLARITY +
  MiCA EMT page-level + foreign-issuer equivalence analysis.

Data-quality finding: `DAI_USDS_003` (registered as "Sky Protocol
technical whitepaper 2025") is actually about a Cardano Layer 2 data
availability solution and is unrelated to the Maker/Sky stablecoin
protocol — name collision. No claims were sourced from this file; the
registry row should be relabelled or removed in a future
data-management pass.

Remaining v0.3 backlog: CLARITY Act stablecoin-specific extraction,
central-bank Taiwan-specific synthesis, MiCA EMT Articles 51/52/55
page-level extraction, and v0.3 final report consolidation snapshot.
USDPT and adjusted-volume market data remain frozen per the v0.2 scope
decision.

## v0.3 interim — 2026-05-14 (Claude Code legal batch)

Phase 1c legal extraction adding `CLAIM_088` to `CLAIM_097`:

- BoE 2023 discussion paper (`BOE_003`): preferred 100% central bank
  deposit backing model with singleness-of-money framing (`CLAIM_088`);
  recovery and administration plan plus shortfall reserve on statutory
  trust for coinholders (`CLAIM_089`).
- BoE 2025 consultation (`BOE_004`): revised backing-asset rule of at
  least 40% unremunerated central bank deposits with up to 60% in
  short-term sterling-denominated UK government debt securities, plus
  step-up regime up to 95% UK gilts at launch (`CLAIM_090`); proposed
  £20,000 retail per-coin and £10 million business holding limits
  (`CLAIM_091`).
- ESMA CASP authorisation supervisory briefing (`ESMA_002`): no
  "low-risk" CASPs and elevated NCA scrutiny for CASPs above
  quantitative or structural thresholds (`CLAIM_092`).
- ESMA transfer services Guidelines under MiCA Article 82 (`ESMA_003`):
  pre-contractual disclosure obligations and TOFR Article 14
  Travel-Rule-equivalent compliance gating before transfer execution
  (`CLAIM_093`).
- MiCA Article 45 (`MICA_004`): specific additional obligations for
  significant ART issuers, including FRAND custody, liquidity management
  policy, and EBA RTS minimum 60% deposits in each referenced official
  currency (`CLAIM_094`).
- MiCA Article 46: ART recovery plan with liquidity fees, daily
  redemption caps, and suspension options plus competent-authority
  redemption-suspension power (`CLAIM_095`).
- MiCA Article 47: ART redemption (wind-down) plan with temporary
  administrator designation, triggered by competent-authority
  determination of issuer inability to fulfil obligations (`CLAIM_096`).
- MiCA Articles 56-58: significant-EMT regime, EBA classification,
  supervisory transfer to EBA, and six-monthly independent audit cadence
  for significant EMT issuers (`CLAIM_097`).

Downstream artifacts updated:

- `02_source_digests/law_source_digest.md` MiCA, BoE, and ESMA sections
  rewritten with the ten new claims.
- `04_matrices/law_regulation_comparison_matrix.csv` MiCA, BoE systemic
  regime, and ESMA rows rewritten.
- `05_chapter_drafts/chapter_04_law_and_regulation.md` extended with the
  significant-ART/EMT, recovery/redemption plan, BoE 2023/2025, and ESMA
  CASP/transfer service paragraphs.

Tooling note: significant-ART and recovery/redemption-plan articles in the
MiCA PDF have a multi-column layout that returns headings only via
pdfplumber. PyMuPDF (`fitz`) was added as a fallback extractor for those
sections; the package is installed in the user's local Python 3.12
environment but is not yet listed in any project requirements file.

Remaining v0.3 backlog: CLARITY Act stablecoin-specific extraction, DAI/USDS
protocol mechanics, USDe risk extraction, central-bank Taiwan-specific
synthesis, and the cross-jurisdiction comparison table at the close of
chapter 4. USDPT and adjusted-volume market data remain frozen per the v0.2
scope decision unless new primary sources arrive.

## v0.2 interim — 2026-05-14 (Claude Code continuation)

Phase 0 cleanup of codex output:

- Replaced `?` range separator with `-` inside `primary_sources` for PYUSD,
  USDP, RLUSD, USDPT rows of `04_matrices/issuer_comparison_matrix.csv`.
- Normalized Chinese-language `文件未揭露 [於 ...]` placeholders to English
  `Not disclosed in archived source [...]` across the issuer matrix.
- Added page-level anchors to `CLAIM_048` (Fed IFDP 1334, p. 2),
  `CLAIM_049` (IMF WP/26/74, p. 2), and `CLAIM_050` (IMF WP/26/52, p. 2),
  replacing bare `Abstract` cites.
- Disambiguated `FDD` vs `FDUSD` in `issuer_source_digest.md`: the
  contractual short-name `FDD` is preserved per the source URL
  `firstdigitallabs.com/legal/fdd-terms`, with an added gloss clarifying it
  refers to the FDUSD asset.

Phase 1a issuer-terms claims `CLAIM_072` to `CLAIM_081`:

- Paxos USD Stablecoin Agreement entity allocation (`CLAIM_072`),
  Customer-only direct purchase/redemption gating across PYUSD, USDP, USDG
  (`CLAIM_073`), no-holder-yield rule (`CLAIM_074`), permitted reserve
  composition for Paxos Trust / Paxos Digital / PIE (`CLAIM_075`), and
  all-holders scope of the Paxos freeze and upgrade right (`CLAIM_076`).
- Gemini Trust User Agreement Customer-only GUSD creation/redemption
  (`CLAIM_077`), three-account-type GUSD reserve structure (`CLAIM_078`),
  and one-Business-Day "Timely" GUSD redemption commitment (`CLAIM_079`).
- USDP transparency-page KPMG AICPA attestation framing (`CLAIM_080`) and
  formally discontinued separate monthly reserve composition report
  (`CLAIM_081`).

Phase 1b GENIUS Act statutory claims `CLAIM_082` to `CLAIM_087` (sourced
from Public Law 119-27, `GENIUS_006`):

- Sec. 3(a) issuer limitation (`CLAIM_082`), Sec. 3(b) 3-year transition
  and foreign issuer treatment (`CLAIM_083`), Sec. 4(1)(A) exhaustive
  reserve composition list (`CLAIM_084`), Sec. 4(1)(C)-(D) and 4(3)
  monthly disclosure and registered-public-accounting-firm examination
  (`CLAIM_085`), Sec. 4(11) holder yield/interest prohibition
  (`CLAIM_086`), and Sec. 11 customer-priority rule in insolvency
  (`CLAIM_087`).

Downstream artifacts updated:

- `02_source_digests/issuer_source_digest.md` PYUSD, USDG, GUSD, and USDP
  sections rewritten with new claim cites.
- `02_source_digests/law_source_digest.md` GENIUS Act section anchored to
  the six statutory claims.
- `04_matrices/issuer_comparison_matrix.csv` PYUSD, USDP, USDG, GUSD rows
  rewritten with the new claims.
- `04_matrices/law_regulation_comparison_matrix.csv` GENIUS Act row
  rewritten with the six statutory anchors.
- `05_chapter_drafts/chapter_02_issuer_comparison.md` and
  `05_chapter_drafts/chapter_04_law_and_regulation.md` updated with new
  claim cites.
- `00_project_management/unresolved_open_questions.md` refreshed: closed
  Paxos-family / GUSD / USDP gaps, deferred USDPT and adjusted-volume
  market data to v0.3 with rationale.

User scope choices for this pass: USDPT scraping deferred (freeze as
unresolved); adjusted volume / Artemis methodology / McKinsey frozen at
current evidence; mixed-language convention (English claim cites, optional
Chinese commentary in chapter narrative). v0.2 final consolidation,
chapter 06 USDPT rewrite, and final-report rewrite remain for v0.3.

## v0.1 — 2026-05-14

- Built first structured research delivery package.
- Added source registry and source manifest.
- Added issuer comparison matrix and master claim table draft.
- Added law, central-bank, payment-settlement and failure-case matrix drafts.
- Added chapter draft skeletons and final report v0.1.
- Added Mermaid flow diagrams.
- Added validation scripts and GitHub/Codex handoff specification.
