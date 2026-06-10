# Changelog

## v0.4 targeted gap closure - 2026-06-05

Current project state:

- Claim table expanded to 154 claims (`CLAIM_001` to `CLAIM_154`).
- Source registry expanded to 148 rows.
- Fifteen new claims and seven new source rows were added; no new matrices were
  added, and the existing six matrices were extended.
- `validate_claim_table.py`, `check_missing_sources.py`, `check_mermaid.py`
  and `build_portal.py` passed at 153 claims before the final `CLAIM_154`
  USDC risk-factor addition. After `CLAIM_154`, static checks confirm the
  source row and cross-document references; Python validation / portal rerun
  is pending because the current execution session blocked additional Python
  runs.

Newly closed or narrowed v0.4 backlog items:

- **P0-1 USDPT product-page and ADB terms layer** (partially closed):
  added `CLAIM_140` to `CLAIM_143` and `CLAIM_150` to `CLAIM_151`.
  Western Union's product page now supports 1:1
  redeemability wording, broad reserve categories, the official Solana
  contract address, and planned / coming-soon exchange, cash-out, card and
  receive-in-USDPT features in select markets. Anchorage's reserve
  transparency page is registered as `USDPT_010`; it states ADB stablecoins
  are redeemable 1:1 on the Anchorage platform and marks the USDPT report
  slot as "Coming soon". Anchorage's Covered Stablecoin Terms are registered
  as `USDPT_011`; they bound Client vs Non-Client redemption rights, reserve
  trust, ADB sole-obligor status, brand-partner status and legal/control
  powers for ADB-issued series.
- **P0-3 Taiwan legislative timeline** (partially closed): added
  `CLAIM_144` to `CLAIM_146`. `TAIWAN_VASP_003` registers the official
  Executive Yuan 2026-04-02 approval / Legislative Yuan submission of the
  FSC draft VASP Act. `TAIWAN_VASP_004` registers 2026-06-03 news reporting
  that the Legislative Yuan Finance Committee first review passed.
  `TAIWAN_VASP_005` registers the official Legislative Yuan bill-detail
  docket for the Executive Yuan draft, including Finance Committee review
  entries through 2026-06-03 and gazette production pending for June entries.
- **P0-2 World Bank remittance-cost benchmark** (closed for off-chain
  benchmark context): added `WB_RPW_002`, `CLAIM_147`, and
  `09_data_exports/scripts/build_worldbank_remittance_benchmark.py`. The
  script exports World Bank WDI API indicator `SI.RMT.COST.IB.ZS` into a
  17,556-row country/region-year CSV and a 104-row latest non-null benchmark
  CSV. This closes the World Bank benchmark-export piece only; it does not
  close Visa / Artemis / Cambridge adjusted stablecoin volume.
- **P1-1 failure-case public hourly proxy timelines** (partially closed):
  added `CRYPTOCOMPARE_001`, `CLAIM_148`, `CLAIM_149`, and
  `09_data_exports/scripts/build_failure_case_price_timelines.py`. The
  script exports 749 public hourly OHLCV rows and a 5-row summary for
  selected windows. It provides usable coarse proxies for USDC/SVB, Terra
  USTC and Maker DAI, while Iron Finance remains unresolved because public
  IRON/TITAN rows are zero-only and exact tick-level or exchange-level
  timeline claims still require higher-quality data.
- **P2 USDT Q1 2026 reserve table** (closed for category-level extraction):
  added `CLAIM_152`, `CLAIM_153`, and
  `09_data_exports/scripts/build_usdt_q1_2026_reserve_breakdown.py`. The
  script exports the `USDT_002` reserve breakdown table into a 12-row CSV.
  This closes the full point-in-time reserve-category table; maturity ladder,
  custodian/counterparty split, collateral detail, redemption operations and
  smart-contract controls remain open.
- **P2 USDC risk-factor controls** (closed at risk-factor / policy layer):
  added `CLAIM_154` from `USDC_007`. Circle's archived risk-factor page now
  anchors address blocking, associated Circle-custodied USDC freezing,
  Blocked Address flow consequences, and extraordinary on-chain transfer
  blocking under Circle's blacklisting policy. Chain-specific contract-code
  extraction and Circle Mint eligibility mapping remain open.

Confirmed still-open backlog items at v0.4:

- **USDPT legal and operational terms**: partially narrowed by ADB
  covered-stablecoin terms, but USDPT-specific retail/user terms, fee
  schedule, reserve attestation, exact token-control implementation beyond
  the disclosed Solana address, agent balance-sheet treatment, end-to-end
  workflow, and bank/clearing route remain unresolved.
- **Adjusted on-chain payment volume**: still requires reproducible Visa /
  Artemis / Cambridge exports or paid/manual data access. World Bank now
  supplies off-chain cost benchmark context, not stablecoin adjusted-volume
  evidence.
- **Taiwan enacted statute / FSC sub-rules**: legislative-stage evidence is
  stronger, but final enacted text, final committee report / gazette text,
  official sub-rules, and detailed binding issuer obligations remain open.
- **Failure-case reproducible price / depeg timelines**: partially narrowed
  by public hourly proxies for USDC/SVB, Terra USTC and Maker DAI; still
  data-dependent for Iron Finance and exact trough/duration/recovery claims.

Cascaded updates:

- `00_project_management/unresolved_open_questions.md` and
  `00_project_management/usdpt_product_terms_research_queue.md` updated to
  distinguish newly supported product-page facts from unresolved legal /
  operational terms.
- `02_source_digests/payment_settlement_source_digest.md` and
  `02_source_digests/law_source_digest.md` updated with v0.4 evidence.
- `04_matrices/payment_settlement_matrix.csv`,
  `04_matrices/issuer_comparison_matrix.csv`,
  `04_matrices/law_regulation_comparison_matrix.csv`, and
  `04_matrices/central_bank_theme_matrix.csv` updated with the new claim
  cites and bounded conclusions.
- `05_chapter_drafts/chapter_04_law_and_regulation.md`,
  `05_chapter_drafts/chapter_05_central_bank_views.md`, and
  `05_chapter_drafts/chapter_06_usdpt_and_cross_border_payments.md` updated
  for the v0.4 source state.
- `README.md` snapshot counts, validation expectations, and live unresolved
  gap summary updated.
- `09_data_exports/README.md`, `09_data_exports/data_manifest.csv`, and the
  new `09_data_exports/remittance_benchmark/` exports added for World Bank
  remittance-cost benchmark integration.

## v0.3.3 evidence-base reinforcement - 2026-06-02

Current project state:

- Claim table expanded to 139 validated claims (`CLAIM_001` to `CLAIM_139`).
- Source registry expanded to 141 rows.
- Eight new claims and four new source rows from public primary or
  secondary materials. No new matrices added; the existing six matrices
  were extended.
- `validate_claim_table.py`, `check_missing_sources.py`,
  `check_mermaid.py` and `build_portal.py` all pass: 139 claims, 141
  sources, 6 matrices, 8 Mermaid diagrams structurally balanced, no
  archived rows missing local files, no high-priority sources needing
  attention.

Newly closed v0.3.3 backlog items:

- **P0-1 USDPT product layer** (partially closed): added `CLAIM_132`
  (Digital Asset Network bridges licensed virtual currency exchanges and
  custodians to Western Union's global payout and liquidity
  infrastructure), `CLAIM_133` (Treasury and Agent Settlement use case
  enables near-instant 24/7 settlement between Western Union and its
  global agents — the strongest layer-3 anchor now in the archive), and
  `CLAIM_134` (Stable by Western Union consumer-spend product launching
  in 2026 in 40+ countries — kept distinct from USDPT issuance). Source:
  `USDPT_007`, the 2026-05-04 Western Union investor-relations launch
  release already archived locally. Product terms, reserve report,
  contract addresses, and retail-redemption / agent-fiat-payout
  workflow remain unresolved.
- **P1-2 Maker / DAI Black Thursday** (closed at community / analyst
  confidence): added `CLAIM_135` (ETH -43% on 2020-03-12, gas spike >6x
  to approximately 80 Gwei with hourly peaks near 200 Gwei, Medianizer
  oracle lag of approximately US$36 versus spot — Glassnode chronology),
  `CLAIM_136` (1,462 of 3,994 collateral auctions closed at 100% discount,
  62,892.93 ETH and US$8.325 million liquidated for zero DAI bids, 5.67
  million DAI protocol undercollateralisation — Whiterabbit post-mortem),
  and `CLAIM_137` (Emergency Shutdown vetoed; lot size raised from 50 to
  500 ETH; auction duration extended; MKR Debt Auction 2020-03-19 —
  Glassnode chronology). Sources: `FAILURE_007` (Whiterabbit Medium
  community post-mortem) and `FAILURE_008` (Glassnode Insights). These
  are community and analyst, not Maker Foundation primary; the case
  study should remain medium-confidence.
- **P0-3 Taiwan legislative timeline** (partially closed): added
  `CLAIM_138` (FSC Chairman Peng Jin-lung 2025-12-03 public statement
  that Taiwan's first regulated stablecoin may launch in the latter half
  of 2026 at the earliest, plus a six-month post-publication buffer for
  subordinate regulations) and `CLAIM_139` (draft VASP Act submitted to
  the Executive Yuan in late June 2025 and still under executive review
  as of 2025-12; prior-approval, reserve, audit, disclosure, and
  foreign-issued-stablecoin-consent obligations; at least eight
  subordinate regulations in preparation). Sources: `TAIWAN_VASP_001`
  (Focus Taiwan / CNA English) and `TAIWAN_VASP_002` (Stellex Law
  commentary). Both are legislative-stage; enacted statutory text
  remains unresolved.

Confirmed still-open backlog items at v0.3.3:

- **P0-1 USDPT product terms, reserve, contract addresses, retail
  redemption, agent cash-out workflow**: source-dependent. Treasury and
  Agent Settlement is now anchored, but customer UX, agent last-mile,
  and bank / clearing settlement layers still lack primary terms.
- **P0-2 Adjusted on-chain payment volume**: data-workflow-dependent
  and paid-feed-dependent. Cambridge dashboard numerical export, Visa
  Onchain Analytics adjusted volume, Artemis reproducible adjusted
  series, World Bank Remittance Prices Worldwide integration, and the
  `MCKINSEY_ARTEMIS_001` manual archive are still required.
- **P0-3 Taiwan enacted statute / FSC sub-rules**: source-dependent.
  `TAIWAN_VASP_001` and `TAIWAN_VASP_002` are legislative-stage; enacted
  Yuan-passed statutory text or FSC sub-rules would be the next-tier
  source.
- **P1-1 Reproducible failure-case price / depeg timelines**:
  partially narrowed at v0.4. CryptoCompare public hourly proxies now cover
  USDC/SVB, Terra USTC and Maker DAI, but paid or exchange-level feeds are
  still required for exact duration/trough/recovery claims and for a usable
  Iron Finance IRON/TITAN chronology.
- **P1-2 Maker Foundation primary source for Black Thursday**:
  source-dependent. Current anchors are community and analyst;
  Foundation / governance forum upgrade would lift confidence from
  medium to high.
- **P1-3 Central-bank / IMF deeper page-level extraction**: continues to
  be conditional framing rather than blocker.
- **P2 issuer-specific gaps (USDC, USDT, Paxos family, RLUSD, GUSD,
  FDUSD, DAI/USDS, USDe, USDPT)**: each requires its own primary terms /
  contract / attestation source; not blockers for the current report.
- **P2-10 Foreign-issuer equivalence official Treasury determination**:
  awaits future Treasury determination, Section 18 reciprocal arrangement
  or Comptroller registration; not closeable by inference.

Cascaded updates:

- `02_source_digests/payment_settlement_source_digest.md`,
  `02_source_digests/failure_case_source_digest.md`,
  `02_source_digests/law_source_digest.md` updated with the new claim
  cites and v0.3.3 source rows.
- `04_matrices/payment_settlement_matrix.csv`,
  `04_matrices/failure_case_matrix.csv`,
  `04_matrices/law_regulation_comparison_matrix.csv`, and
  `04_matrices/central_bank_theme_matrix.csv` updated with the new
  claim cites; matrix count remains 6.
- `05_chapter_drafts/chapter_04_law_and_regulation.md`,
  `05_chapter_drafts/chapter_05_central_bank_views.md`,
  `05_chapter_drafts/chapter_06_usdpt_and_cross_border_payments.md`, and
  `05_chapter_drafts/chapter_08_failure_cases.md` updated with v0.3.3
  prose paragraphs and remaining-work pointers.
- `07_final_report/slide_outline_v0_3.md` slides 36, 37, 38, 39, 40,
  44, 45 and Appendix A3 updated with the new claim cites and v0.3.3
  count.
- `07_final_report/slide_script_v0_3.md` slides 36, 37, 38, 40, 44 and
  45 rewritten with v0.3.3 body, speaker notes and source-claim
  pointers.
- `07_final_report/key_figures.csv` updated: KF_032 and KF_033 refreshed
  to v0.3.3 counts; KF_035 to KF_040 added for Stable by Western Union
  country count, Black Thursday auction count / ETH / dollar / DAI
  figures, and the FSC Chair H2 2026 statement.
- `00_project_management/unresolved_open_questions.md` rewritten for the
  v0.3.3 state.
- `README.md` snapshot counts and "What Changed Since v0.1" updated.

## v0.3.2 foreign-issuer equivalence screen - 2026-05-26

Current project state:

- Claim table expanded to 131 validated claims (`CLAIM_001` to
  `CLAIM_131`); source registry remains 137 rows.
- Added `CLAIM_126` to `CLAIM_131` for GENIUS Section 18 foreign-issuer
  reciprocity, MiCA EMT issuer/no-interest/supervision details, and BoE 2025
  cross-border / robust-claim / par-redemption framing.
- Added `04_matrices/foreign_issuer_equivalence_matrix.csv`.
- Updated chapter 4 and the law digest with a bounded equivalence screen:
  BoE and MiCA are comparison cases, not automatically Treasury-recognised
  equivalent regimes.
- Removed foreign-issuer equivalence from the live unresolved backlog. It is
  now "screened, not adjudicated": a future Treasury determination or
  reciprocal-arrangement source would still be needed for an official
  equivalence claim.

## v0.3.1 evidence-base cleanup - 2026-05-25

Current project state:

- Claim table expanded to 125 validated claims (`CLAIM_001` to
  `CLAIM_125`) and source registry synchronized at 137 rows.
- Rebuilt `07_final_report/slide_script_v0_3.md` and
  `07_final_report/slide_outline_v0_3.md` after mojibake cleanup.
- Added DAI/USDS and USDe flow diagrams:
  `06_flow_diagrams/dai_usds_protocol_flow.md` and
  `06_flow_diagrams/usde_synthetic_dollar_flow.md`.
- Added Taiwan CBC synthesis claims (`CLAIM_112` to `CLAIM_118`) and updated
  the central-bank digest, matrix, chapter 5, and slide 36.
- Added CLARITY Act claims (`CLAIM_119` to `CLAIM_121`) and MiCA EMT
  Article 51/52/53/55 claims (`CLAIM_122` to `CLAIM_125`). Article 52 is
  white-paper liability; Article 53 is marketing communications.
- Updated USDPT and data-export documentation so unsupported workflow,
  redemption, contract-address, adjusted-volume, and SWIFT/correspondent-
  banking displacement claims remain explicit open questions.
- Active next items: USDPT product documentation, adjusted payment-volume
  exports, foreign-issuer equivalence, Taiwan enacted law/sub-rules,
  failure-case timelines, and selected issuer-detail extraction.

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
- 73 distinct `CLAIM_XXX` IDs cited (out of the 106 claims in the table at
  the 2026-05-15 snapshot; current v0.3.2 table has 131 claims)
- 31 distinct `KF_XXX` IDs cited (out of 34 in `key_figures.csv`)
- MD032 lint clean (no heading-to-list adjacency)

Speaker checklist at end of file flags eight pre-session decisions: title
slide attribution, custom visual completeness, USDC reserve composition
data source, DAI/USDS and USDe flow diagrams (not yet in
`06_flow_diagrams/`), USDPT four-layer swim-lane Mermaid reuse, slide-cut
options for under-60-minute and over-90-minute sessions, and appendix
gating.

Superseded by v0.3.1: CLARITY extraction, central-bank Taiwan synthesis,
and MiCA EMT Article 51/52/53/55 extraction are now closed. Remaining
forward candidates are USDPT product layer, adjusted on-chain volume,
foreign-issuer equivalence, Taiwan enacted law/sub-rules, and failure-case
timelines.

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
the then-existing 106 claims were rolled into finished prose at the
report-frame boundaries. Current v0.3.2 supersedes this with 131 claims.

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
protocol — name collision. **Resolved 2026-05-15**: relabelled to
`OTHER_CARDANO_SKY_001` (category `archive_reference`, priority `low`);
no claims were sourced from this file.

Superseded by v0.3.1: CLARITY, central-bank Taiwan synthesis, MiCA EMT
Article extraction, DAI/USDS, USDe, and report-frame cleanup are now closed.
USDPT and adjusted-volume market data remain open.

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

Superseded by v0.3.1: CLARITY extraction, DAI/USDS protocol mechanics, USDe
risk extraction, central-bank Taiwan synthesis, and the chapter-4 comparison
table are now closed. USDPT and adjusted-volume market data remain open
unless new primary sources arrive.

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
