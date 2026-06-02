# Unresolved Open Questions

Last updated: 2026-05-26 (v0.3.2 comprehensive backlog refresh)

Purpose: this file is the live research backlog. It preserves questions that
must not be guessed in the final report, slides, evidence portal, or matrices.
If an item is answered, first register the source in
`01_sources/source_registry.csv`, then add claim rows in
`03_claim_tables/claim_table_master.csv`, then update the relevant digest,
matrix, chapter, slide, and this file.

Current baseline:

- Claim table: 131 validated claims (`CLAIM_001` to `CLAIM_131`).
- Source registry: 137 rows.
- Matrices: 6 CSV files under `04_matrices/`.
- Evidence portal build source:
  `07_final_report/stablecoin_academic_report_v1_0.md`.
- Known no-local / deficient rows:
  `MCKINSEY_ARTEMIS_001` (`manual_needed`) and `FAILURE_001` to
  `FAILURE_006` (`url_only`).

Validation baseline:

```powershell
& 'C:\Users\woody\AppData\Local\Programs\Python\Python312\python.exe' 08_scripts\validate_claim_table.py
& 'C:\Users\woody\AppData\Local\Programs\Python\Python312\python.exe' 08_scripts\check_missing_sources.py
& 'C:\Users\woody\AppData\Local\Programs\Python\Python312\python.exe' 08_scripts\check_mermaid.py
& 'C:\Users\woody\AppData\Local\Programs\Python\Python312\python.exe' 10_evidence_portal\scripts\build_portal.py
```

Expected current results:

- `validate_claim_table.py`: `OK: 131 claims validated.`
- `check_missing_sources.py`: no missing archived local files and no
  high-priority rows needing attention.
- `check_mermaid.py`: all 8 diagrams structurally pass.
- `build_portal.py`: 131 claims, 137 sources, 6 matrices.

## Closed Since Earlier Backlogs

These should not be reopened unless a new source creates a materially new
question.

| Item | Closed by | Current boundary |
| --- | --- | --- |
| Taiwan CBC policy synthesis | `CLAIM_112` to `CLAIM_118` | CBC policy framing is supported; enacted law / sub-rules remain separate. |
| CLARITY stablecoin-specific extraction | `CLAIM_119` to `CLAIM_121` | CLARITY is market-structure / intermediary treatment, not a reserve or issuer regime. |
| MiCA EMT Articles 51, 52, 53, 55 | `CLAIM_122` to `CLAIM_125` | Article 52 is white-paper liability; Article 53 is marketing communications. |
| DAI/USDS and USDe core mechanics | `CLAIM_098` to `CLAIM_106` | Contract-level RWA/PSM and stress analysis remain open. |
| GENIUS / BoE / MiCA foreign-issuer equivalence screen | `CLAIM_126` to `CLAIM_131`; `04_matrices/foreign_issuer_equivalence_matrix.csv` | Screened, not adjudicated. No official Treasury comparability determination is claimed. |
| USDP monthly reserve report missing status | `CLAIM_080`, `CLAIM_081` | Reclassified from missing to issuer-discontinued; do not keep asking for a discontinued standalone USDP report unless Paxos resumes publication. |
| Paxos-family direct redemption gating | `CLAIM_072` to `CLAIM_076` | Remaining PYUSD/PayPal question is operational mapping, not basic Paxos Customer-only gating. |
| Gemini GUSD customer-only redemption and timing | `CLAIM_077` to `CLAIM_079` | Remaining GUSD question is smart-contract control and NYDFS-lawful-holder interaction. |

## Priority Legend

- **P0**: Blocks a major conclusion in the current report or slides.
- **P1**: Important for stronger report quality, but current cautious wording
  is defensible.
- **P2**: Useful depth / appendix / later version material.
- **P3**: Housekeeping or low-risk enhancement.

## P0 Active Gaps

### P0-1. USDPT Product Layer And Workflow

Status: unresolved; source-dependent.

Current supported evidence:

- `CLAIM_023`: Anchorage comment letter says Anchorage Digital Bank issues
  USAT, USDGO and USDtb, and expects to begin issuing USDPT with Western
  Union as brand partner.
- `CLAIM_051`: Western Union announced USDPT as a U.S. Dollar Payment Token
  built on Solana and issued by Anchorage Digital Bank, alongside a Digital
  Asset Network.
- `CLAIM_052`: Western Union launch materials describe USDPT as a
  USD-denominated payment stablecoin, fully backed by U.S. dollars, issued by
  Anchorage Digital Bank N.A., and built on Solana for real-world payment
  systems.
- `CLAIM_053`: Fireblocks / Dynamic / TRES materials support wallet,
  settlement, agent-settlement, financial-operations, and MT940/MT942
  reporting infrastructure claims.
- Dedicated queue:
  `00_project_management/usdpt_product_terms_research_queue.md`.

What is still missing:

- USDPT product terms / user terms.
- Anchorage Digital Bank USDPT issuance agreement or program terms.
- USDPT reserve report, attestation, reserve trust agreement, or reserve
  composition disclosure.
- Contract addresses on Solana and any official token metadata.
- Direct redemption policy and eligible redeemer scope.
- End-to-end customer-to-customer or customer-to-agent workflow.
- Whether Western Union agents hold, cash out, receive, or settle in USDPT.
- Whether USDPT is used only in back-office treasury / liquidity management.
- Actual settlement route between USDPT on-chain transfer and bank,
  correspondent, Fedwire, CHIPS, or local payout rails.

Do not claim:

- USDPT replaces SWIFT.
- USDPT replaces correspondent banking.
- USDPT replaces Fedwire or CHIPS.
- Western Union agents directly cash out USDPT.
- Any holder can redeem USDPT 1:1.
- USDPT reserve composition is equivalent to USDC / Paxos / GENIUS reserves.
- USDPT is a fully operational production remittance architecture beyond what
  WU / Anchorage / Fireblocks materials state.

Safe current wording:

> Western Union is attempting to use USDPT and a Digital Asset Network to
> build a regulated digital-asset settlement layer, but the public archive
> does not yet support direct holder redemption, reserve composition,
> contract-address, agent cash-out, or SWIFT / correspondent-banking
> replacement claims.

Resolution criteria:

1. Add new primary source(s) as `USDPT_###` or `ANCHORAGE_###`.
2. Add claim rows for reserve structure, redemption scope, contract address,
   workflow, and agent / treasury role.
3. Update:
   - `00_project_management/usdpt_product_terms_research_queue.md`
   - `02_source_digests/payment_settlement_source_digest.md`
   - `02_source_digests/issuer_source_digest.md`
   - `04_matrices/payment_settlement_matrix.csv`
   - `04_matrices/issuer_comparison_matrix.csv`
   - `05_chapter_drafts/chapter_06_usdpt_and_cross_border_payments.md`
   - `07_final_report/slide_script_v0_3.md` slides 37 to 40
   - `07_final_report/slide_outline_v0_3.md`
   - evidence portal

### P0-2. Adjusted Payment-Volume Evidence

Status: unresolved; data-workflow-dependent.

Current supported evidence:

- `CLAIM_054`: Artemis documentation supports a schema for stablecoin
  transfer volume, transactions, supply, addresses, and filter categories
  such as `None`, `ARTEMIS`, and `P2P`.
- `CLAIM_055`: DeFiLlama API snapshots support stablecoin supply and
  chain-distribution analysis, not adjusted payment-volume evidence.
- `09_data_exports/` includes reproducible DeFiLlama exports for supply /
  chain distribution.

What is still missing:

- Reproducible Visa Onchain Analytics adjusted-volume export.
- Reproducible Artemis adjusted-volume export beyond the existing schema /
  methodology claim.
- Cambridge Digital Money Dashboard numerical export.
- World Bank remittance price benchmark export integration.
- `MCKINSEY_ARTEMIS_001` local archive or equivalent primary / licensed copy.
- A documented transformation notebook or script that separates raw transfer
  volume from adjusted payment-like flows.

Do not claim:

- Raw on-chain transfer volume equals payment demand.
- Stablecoin supply equals payment adoption.
- DeFiLlama supply or chain distribution is payment-volume evidence.
- Visa, Artemis, Cambridge, DeFiLlama, and World Bank series are comparable
  without methodology reconciliation.
- USDPT or any issuer has measurable adoption based only on supply or raw
  volume.

Safe current wording:

> The project can support supply and chain-distribution analysis, and it can
> explain why raw transfer volume overstates payment demand. It cannot yet
> estimate realised stablecoin payment volume without reproducible adjusted
> exports and methodology reconciliation.

Resolution criteria:

1. Add raw export files under `09_data_exports/` with source date,
   collection method, and transformation notes.
2. Add or update scripts/notebooks that can be rerun locally.
3. Register new source rows or data artifacts if needed.
4. Add claim rows only for reproducible, source-backed metrics.
5. Update:
   - `09_data_exports/README.md`
   - `02_source_digests/market_data_source_digest.md`
   - `05_chapter_drafts/chapter_07_onchain_data_and_payment_demand.md`
   - `07_final_report/slide_script_v0_3.md` slides 41 to 43
   - `07_final_report/key_figures.csv` if numerical figures are added
   - evidence portal

### P0-3. Taiwan Enacted Law And Sub-Rules

Status: unresolved; source-dependent.

Current supported evidence:

- `CLAIM_112` to `CLAIM_118` support CBC policy framing for:
  private tokenised money, central-bank-money anchor, USD-stablecoin
  digital-dollarisation / FX-management risk, NTD-stablecoin stored-value
  framing, 100% reserve design, no-yield treatment, disclosure, asset
  segregation, audit/assurance, and FSC-CBC consultation.

What is still missing:

- Enacted Taiwan stablecoin statute, if enacted.
- FSC sub-rules, licensing forms, consultation documents, or official
  explanatory notes.
- CBC / FSC joint reserve-management rules.
- Issuer qualification details, reserve custody requirements, disclosure
  templates, audit/assurance cadence, redemption timing, and enforcement
  powers under binding law.
- Treatment of offshore USD stablecoins offered to Taiwan users.

Do not claim:

- Taiwan has enacted a final stablecoin law unless official enacted text is
  registered and extracted.
- CBC policy papers are binding legal rules.
- NTD stablecoins are approved products.
- Taiwan's rules are equivalent to GENIUS, MiCA, BoE, or NYDFS.

Safe current wording:

> CBC materials support a Taiwan policy synthesis, not a final enacted-law
> analysis. Taiwan statutory conclusions should wait for enacted text or
> official FSC/CBC sub-rules.

Resolution criteria:

1. Register official Taiwan legal source(s), preferably from FSC, CBC,
   Executive Yuan, Legislative Yuan, or official gazette.
2. Add claim rows for enacted legal obligations.
3. Keep legal claims separate from `CLAIM_112` to `CLAIM_118` policy
   framing.
4. Update:
   - `02_source_digests/law_source_digest.md`
   - `02_source_digests/central_bank_source_digest.md`
   - `04_matrices/law_regulation_comparison_matrix.csv`
   - `04_matrices/central_bank_theme_matrix.csv`
   - `05_chapter_drafts/chapter_04_law_and_regulation.md`
   - `05_chapter_drafts/chapter_05_central_bank_views.md`
   - Taiwan slides in `07_final_report/slide_script_v0_3.md`
   - evidence portal

## P1 Active Gaps

### P1-1. Failure-Case Price / Depeg Timelines

Status: unresolved; data-workflow-dependent.

Current supported evidence:

- `CLAIM_107`: SEC description of Terra UST as algorithmic stablecoin and
  May 2022 collapse.
- `CLAIM_108`, `CLAIM_109`: Circle's USDC/SVB depeg and backlog-clearing
  statements.
- `CLAIM_110`: NYAG Tether / Bitfinex investigation and settlement.
- `CLAIM_111`: Iron Finance post-mortem characterising the IRON/TITAN event
  as a bank run.
- Current `FAILURE_001` to `FAILURE_006` rows are `url_only`.

What is still missing:

- Reproducible price / peg time series for Terra UST, USDC/SVB, Iron
  Finance, and any additional cases.
- Source selection for price data (CoinGecko, Kaiko, Chainlink, DeFiLlama,
  exchange candles, issuer data, or other reproducible datasets).
- Time-zone-normalised event windows.
- Rules for selecting intraday vs daily frequency.
- Data-cleaning notebook or script and exported CSVs.
- Local archive for the currently `url_only` failure sources if strict local
  reproducibility is desired.

Do not claim:

- Exact depeg duration, trough, recovery time, or liquidity path without a
  reproducible data series.
- Terra / Iron / USDC / Tether cases are mechanically equivalent.
- Current reserve condition from historical failure-case sources.

Safe current wording:

> Failure-case sources support qualitative risk channels, but not yet
> reproducible price/depeg timelines.

Resolution criteria:

1. Choose a price-data source and document why.
2. Save raw data under `09_data_exports/` or a new failure-case data folder.
3. Add a rerunnable script/notebook.
4. Add claim rows for any numerical timeline claims.
5. Update:
   - `02_source_digests/failure_case_source_digest.md`
   - `04_matrices/failure_case_matrix.csv`
   - `05_chapter_drafts/chapter_08_failure_cases.md`
   - `07_final_report/key_figures.csv`
   - slides 44 to 45
   - evidence portal

### P1-2. Maker / DAI Black Thursday

Status: unresolved; primary-event-source-dependent.

Current supported evidence:

- `CLAIM_098` to `CLAIM_102` support Maker / Sky core mechanics: vaults,
  collateralisation, auctions, DSR / Sky Savings Rate, Keepers, Oracles,
  Global Settlers, and USDS / sUSDS / stUSDS mapping at product-page level.
- `04_matrices/failure_case_matrix.csv` explicitly marks Maker Black Thursday
  as pending.

What is still missing:

- Primary MakerDAO / Maker Foundation / governance / forum / post-mortem
  source for Black Thursday.
- Event timeline, oracle / gas / auction / keeper failure mechanics.
- Quantitative losses, zero-bid auctions, collateral shortfall, MKR dilution,
  or governance response claims from primary sources.
- Relationship between legacy MakerDAO event mechanics and current Sky /
  USDS architecture.

Do not claim:

- Exact Black Thursday losses, zero-bid amounts, auction failures, or MKR
  dilution outcomes without a registered primary source.
- Current Sky risk is identical to 2020 Maker risk.

Safe current wording:

> Maker / Sky mechanics are claim-backed, but Black Thursday is not yet a
> claim-backed case study in this repository.

Resolution criteria:

1. Register primary event source(s) as `FAILURE_###` or `DAI_USDS_###`.
2. Add claim rows for event mechanics and consequences.
3. Update:
   - `02_source_digests/failure_case_source_digest.md`
   - `04_matrices/failure_case_matrix.csv`
   - `05_chapter_drafts/chapter_08_failure_cases.md`
   - DAI / USDS sections in chapter 2 if current-risk framing changes
   - slides 44 to 45
   - evidence portal

### P1-3. Central-Bank / International-Body Extraction Depth

Status: partially supported; not a current report blocker.

Current supported evidence:

- Fed and IMF source sets are locally registered.
- `CLAIM_044` to `CLAIM_050` support the current central-bank and IMF
  synthesis.
- Taiwan CBC synthesis is claim-backed at `CLAIM_112` to `CLAIM_118`.

What is still missing:

- Normalised extraction pass for `IMF_002`, `IMF_004`, and selected Fed /
  BIS / ECB / FSB sources beyond the currently cited claim set.
- Cleanup of stale `IMF pending` / `Federal Reserve pending` style rows in
  `04_matrices/central_bank_theme_matrix.csv` if a future matrix refresh is
  performed.
- More granular page-level mapping for capital-flow, safe-asset-demand,
  monetary-policy-transmission, and dollarisation channels.

Do not claim:

- A central-bank consensus beyond the cited claims.
- Taiwan statutory conclusions from CBC policy sources.
- Quantitative monetary-policy or bank-credit effects beyond sourced claims.

Safe current wording:

> Central-bank sources support the current conditional framing, but a deeper
> page-level extraction pass would strengthen the appendix and matrix layer.

Resolution criteria:

1. Extract additional claims only where page-level evidence is clear.
2. Update:
   - `02_source_digests/central_bank_source_digest.md`
   - `04_matrices/central_bank_theme_matrix.csv`
   - `05_chapter_drafts/chapter_05_central_bank_views.md`
   - slides 33 to 36 if new claims alter framing
   - evidence portal

## P2 Issuer-Specific Gaps

### P2-1. USDC

Current supported evidence:

- `CLAIM_026`, `CLAIM_027`: reserve categories and 1:1 backing / redemption
  statement.
- `CLAIM_058`: direct redemption requires a Circle Mint account in good
  standing.
- `CLAIM_059`: no entitlement to reserve interest / returns.

Open questions:

- Circle Mint eligibility and region-specific limits.
- Circle Reserve Fund breakdown across direct Treasuries, repo, MMF shares,
  and bank deposits beyond current high-level reserve categories.

Do not claim:

- Any holder can redeem directly with Circle.
- Circle Reserve Fund component weights unless extracted from a primary
  source.

Resolution criteria:

- Add claims from Circle Mint terms, Circle Reserve Fund documents, or
  official transparency filings.
- Update issuer digest, issuer matrix, chapter 2, chapter 3, and reserve
  slides.

### P2-2. USDT

Current supported evidence:

- `CLAIM_002`, `CLAIM_003`: Q1 2026 reserve report / report nature.
- `CLAIM_028`, `CLAIM_029`: May 2026 issuer release on Treasury exposure,
  gold, and Bitcoin.
- `CLAIM_060`, `CLAIM_061`: verified-customer redemption and prohibited
  persons / jurisdictions.

Open questions:

- Full Q1 2026 reserve table in `USDT_002`, including exact categories,
  maturity / liquidity notes, secured loans, other investments, and issuer
  distinctions.
- Redemption fee, minimum, timing, operational delay, and bank-transfer
  mechanics.
- Smart-contract freeze / blacklist / pause powers.
- Separation among USDT, Tether International / El Salvador registration,
  and any future GENIUS-compliant USAT structure.

Do not claim:

- USDT is a pure cash equivalent.
- Any holder can redeem directly with Tether.
- Current smart-contract control powers without source-backed extraction.

Resolution criteria:

- Add claims from `USDT_002`, `USDT_007`, contract documentation, and any
  official USAT / Tether International materials.
- Update issuer digest, issuer matrix, chapter 2, chapter 3, and slides 8,
  19, and reserve-risk sections.

### P2-3. PYUSD / USDP / USDG

Current supported evidence:

- `CLAIM_030`, `CLAIM_031`: PayPal crypto terms / PayPal Hub eligibility.
- `CLAIM_068`: EU USDG retail redemption route.
- `CLAIM_072` to `CLAIM_076`: Paxos entity allocation, Customer-only direct
  redemption, no-holder-yield, reserve restrictions, and freeze / upgrade
  powers.
- `CLAIM_080`, `CLAIM_081`: USDP attestation and discontinued standalone
  monthly reserve composition reports.

Open questions:

- PYUSD: operational relationship between PayPal retail user flows and Paxos
  Customer onboarding if a PayPal user attempts direct Paxos redemption.
- USDG: non-EU institutional and direct-Paxos-Customer workflows.
- USDG: whether any USDG-specific reserve report exists apart from the
  unified Paxos disclosure.

Do not claim:

- PayPal retail users automatically have direct Paxos redemption rights.
- USDP monthly reserve report is missing; current evidence says separate
  reports were discontinued.
- USDG non-EU workflow without source-backed terms.

Resolution criteria:

- Add claims from PayPal / Paxos operational terms or USDG-specific reserve
  documentation.
- Update issuer digest, issuer matrix, chapter 2, and slides 9 to 10.

### P2-4. RLUSD

Current supported evidence:

- `CLAIM_007`, `CLAIM_008`: RLUSD issuer and NYDFS-style reserve criteria.
- `CLAIM_032`, `CLAIM_033`: reserve and custody product-page statements.
- `CLAIM_057`: Ripple user terms support prohibited-use and suspension /
  termination consequences.

Open questions:

- Direct redeemer eligibility and whether all holders, customers, or only
  approved users can redeem directly.
- Contract-level freeze / blacklist / pause powers.
- Relationship among Ripple, Standard Custody & Trust Company, reserve
  accounts, and distributors if direct redemption is intermediated.

Do not claim:

- Any RLUSD holder can redeem directly.
- RLUSD smart-contract controls without source-backed extraction.

Resolution criteria:

- Add claims from RLUSD terms, technical documentation, smart-contract docs,
  or Standard Custody materials.
- Update issuer digest, issuer matrix, chapter 2, and NYDFS comparison text.

### P2-5. GUSD

Current supported evidence:

- `CLAIM_011`, `CLAIM_012`: GUSD product / reserve-report basics.
- `CLAIM_034`, `CLAIM_035`: product-page reserve and platform redemption.
- `CLAIM_077` to `CLAIM_079`: Gemini Customer-only creation/redemption,
  reserve account categories, and one-Business-Day "Timely" sell-order
  redemption commitment.
- `CLAIM_036` to `CLAIM_040`: NYDFS lawful-holder guidance.

Open questions:

- Smart-contract-level freeze / blacklist / pause specifics.
- How NYDFS lawful-holder redemption obligations interact with Gemini's
  customer-only contractual redemption channel.
- Dedicated claim for reserve interest accruing to Gemini if used in
  conclusion-level prose.

Do not claim:

- Non-customers have a contractual redemption relationship with Gemini.
- NYDFS lawful-holder guidance automatically overrides Gemini customer-only
  platform terms without legal analysis.
- GUSD smart-contract controls without technical source extraction.

Resolution criteria:

- Add claims from GUSD smart-contract docs, Gemini technical terms, NYDFS
  source analysis, or Gemini legal disclosures.
- Update issuer digest, issuer matrix, chapter 2, chapter 4, and slides 11
  and 30 if relevant.

### P2-6. FDUSD

Current supported evidence:

- `CLAIM_009`, `CLAIM_010`: FDUSD attestation / reserve account report.
- `CLAIM_062` to `CLAIM_064`: redemption / sale rights, FD121 Account
  gating, suspension / limitation mechanics, and U.S. person exclusion.

Open questions:

- Relationship among FD121 (BVI) Limited, Hong Kong trust / custody
  arrangements, and reserve-account banks.
- Whether there are entity-specific obligations for FDUSD on each supported
  chain.
- Smart-contract control terms if not already embedded in product terms.

Do not claim:

- U.S. individuals are eligible FD121 Account holders.
- FDUSD trust / custody structure beyond extracted source language.

Resolution criteria:

- Add claims from FD121 / First Digital trust, custody, reserve-bank, or
  token-contract documentation.
- Update issuer digest, issuer matrix, chapter 2, and reserve chapter.

### P2-7. DAI / USDS

Current supported evidence:

- `CLAIM_098` to `CLAIM_102`: Maker / Sky vault mechanics, liquidation
  auctions, DSR / Sky Savings Rate, external actors, and Sky rebrand /
  product mapping.

Open questions:

- RWA Vault inventory and current off-chain collateral / legal-wrapper
  structure.
- Peg Stability Module contract-level mechanics.
- Exact contract / governance relationship among legacy DAI, USDS, sUSDS,
  stUSDS, and SKY.
- Governance-vote history for major rebrand and conversion mechanics.
- Relationship between Maker legacy architecture and current Sky protocol
  risk allocation.

Do not claim:

- DAI / USDS is fiat-backed in the same sense as USDC / Paxos / GUSD.
- sUSDS or stUSDS yield is guaranteed.
- RWA custody / legal structure without source-backed extraction.

Resolution criteria:

- Add claims from Maker / Sky official docs, governance votes, contract docs,
  RWA reports, and PSM documentation.
- Update issuer digest, issuer matrix, chapter 2, chapter 3, DAI/USDS flow
  diagram if needed, and slides 14 and 44.

### P2-8. USDe

Current supported evidence:

- `CLAIM_065`, `CLAIM_066`: Mint User / Holding User distinction, U.S. Mint
  User ineligibility, and no USDe holder yield.
- `CLAIM_067`: synthetic-dollar framing.
- `CLAIM_103` to `CLAIM_106`: delta-neutral hedging, Off-Exchange Settlement
  custody, custodian attestations, and Reserve Fund composition / control.

Open questions:

- Live exchange-by-exchange exposure breakdown.
- Basis / funding scenario analysis and negative-funding stress.
- sUSDe APY sustainability under sustained adverse funding conditions.
- Liquidity unwind mechanics if derivatives exchange, OES custodian, or
  stablecoin collateral channels are impaired.
- Current Reserve Fund size and governance if changed from the extracted
  snapshot.

Do not claim:

- USDe is fiat-backed.
- sUSDe yield is guaranteed or risk-free.
- Off-Exchange Settlement eliminates exchange risk; evidence supports
  mitigation, not elimination.

Resolution criteria:

- Add claims from Ethena risk reports, exchange-exposure disclosures,
  custodian/OES documentation, funding-rate stress models, or reserve fund
  updates.
- Update issuer digest, issuer matrix, chapter 2, chapter 8, USDe flow
  diagram if needed, and slides 15 and 44.

### P2-9. USDPT Issuer-Specific Details

This overlaps with P0-1 but is retained here so issuer-comparison work does
not miss USDPT.

Open questions:

- Product name and ticker stability: confirm whether all primary documents
  use USDPT consistently.
- Issuer legal entity and any co-branding / program-manager structure.
- Reserve trust, reserve report, and attestation cadence.
- Contract addresses and mint / burn controls.
- Direct redemption rights and eligible redeemers.
- Freeze / blacklist / suspension / sanctions controls.
- Holder yield / reserve-yield treatment.

Do not claim:

- USDPT can be compared issuer-by-issuer with USDC, USDT, Paxos, GUSD,
  FDUSD, RLUSD on redemption or reserve composition until product terms and
  reserve reports exist.

Resolution criteria:

- Same as P0-1, plus update `04_matrices/issuer_comparison_matrix.csv`.

## P2 Legal / Regulatory Follow-Ups

### P2-10. Foreign-Issuer Equivalence: Future Official Determinations

Status: screened, not adjudicated.

Current supported evidence:

- `CLAIM_126`: GENIUS Section 18 statutory screen.
- `CLAIM_127` to `CLAIM_129`: MiCA EMT issuer eligibility, no-interest rule,
  and significant-EMT supervision / non-euro derogation.
- `CLAIM_130`, `CLAIM_131`: BoE cross-border and robust-claim / par
  redemption framing.
- `04_matrices/foreign_issuer_equivalence_matrix.csv`.

What remains open only if new sources appear:

- Treasury comparability determination for any foreign jurisdiction.
- Section 18 reciprocal arrangement.
- Comptroller registration of a foreign payment stablecoin issuer.
- U.S.-customer liquidity reserve treatment for a foreign issuer.
- Official finding that BoE, MiCA EMT, MiCA ART, or another regime is
  comparable to GENIUS.

Do not claim:

- BoE is substantially similar to GENIUS.
- MiCA EMT is equivalent to GENIUS.
- MiCA ART is a payment-stablecoin equivalent regime.
- CLARITY supplies foreign-issuer equivalence.

Safe current wording:

> BoE and MiCA are comparison cases for GENIUS Section 18, but the project
> does not make an official Treasury comparability determination.

Resolution criteria:

- Register Treasury / OCC / Federal Register / foreign regulator source.
- Add claim rows and update `foreign_issuer_equivalence_matrix.csv`.

## P3 Operational / Source Hygiene

### P3-1. Manual / URL-Only Source Rows

Current state:

- `MCKINSEY_ARTEMIS_001`: `manual_needed`.
- `FAILURE_001` to `FAILURE_006`: `url_only`.

Action if local copies are obtained:

1. Save the file or HTML under an appropriate archive folder.
2. Update `01_sources/source_registry.csv` status and `local_path`.
3. Update `01_sources/source_manifest.csv` if the project keeps the manifest
   synchronized.
4. Add claims only if extraction adds new evidence beyond the existing claim
   table.
5. Rerun `check_missing_sources.py`.

### P3-2. Evidence Portal Synchronization

Any claim-table or source-registry change must be followed by:

```powershell
& 'C:\Users\woody\AppData\Local\Programs\Python\Python312\python.exe' 10_evidence_portal\scripts\build_portal.py
```

If a new matrix is added under `04_matrices/`, the portal should report the
increased matrix count.

### P3-3. Stale Historical Deficiency Files

Historical files such as `known_deficiencies_phase3.md`,
`research_phase3_status.md`, and `consolidated_phase_deficiency_review.md`
retain older deficiency snapshots. They should not be treated as the live
backlog unless a v0.3.2 superseding note is missing.

Current live sources of truth:

- This file for unresolved research.
- `00_project_management/claude_code_handoff.md` for handoff state.
- `README.md` for current counts and validation expectations.
- `03_claim_tables/claim_table_master.csv` for evidence claims.
- `01_sources/source_registry.csv` for source availability.

## Universal Rules For Closing Any Item

1. Do not close an item from inference alone.
2. Do not cite product pages for contractual rights unless the product page
   itself states the legal right clearly.
3. Do not call attestations audits unless the source uses audit language for
   the relevant engagement.
4. Do not convert a policy paper into binding law.
5. Do not equate raw on-chain volume with payment demand.
6. Do not treat "customer", "lawful holder", "verified user", "Mint User",
   and "token holder" as interchangeable.
7. Do not treat a comparative legal screen as an official equivalence ruling.
8. Every closed item needs:
   - source registration,
   - claim-table row(s),
   - digest / matrix / chapter update,
   - slide update if presentation-facing,
   - evidence portal rebuild,
   - validation rerun.
