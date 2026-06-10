# Unresolved Open Questions

Last updated: 2026-06-05 (v0.4 targeted gap closure)

Purpose: this file is the live research backlog. It preserves questions that
must not be guessed in the final report, slides, evidence portal, or matrices.
If an item is answered, first register the source in
`01_sources/source_registry.csv`, then add claim rows in
`03_claim_tables/claim_table_master.csv`, then update the relevant digest,
matrix, chapter, slide, and this file.

Current baseline:

- Claim table: 154 claims (`CLAIM_001` to `CLAIM_154`). Full Python
  validation passed at 153 claims earlier on 2026-06-05; after `CLAIM_154`,
  static source / reference checks passed and Python validation rerun is
  pending.
- Source registry: 148 rows.
- Matrices: 6 CSV files under `04_matrices/`.
- Evidence portal build source:
  `07_final_report/stablecoin_academic_report_v1_0.md`.
- Known no-local / deficient rows:
  `MCKINSEY_ARTEMIS_001` (`manual_needed`); `FAILURE_001` to `FAILURE_008`
  (`url_only`); `USDPT_010`, `USDPT_011`, and `TAIWAN_VASP_001` to
  `TAIWAN_VASP_005` (`url_only`).

Validation baseline:

```powershell
& 'C:\Users\woody\AppData\Local\Programs\Python\Python312\python.exe' 08_scripts\validate_claim_table.py
& 'C:\Users\woody\AppData\Local\Programs\Python\Python312\python.exe' 08_scripts\check_missing_sources.py
& 'C:\Users\woody\AppData\Local\Programs\Python\Python312\python.exe' 08_scripts\check_mermaid.py
& 'C:\Users\woody\AppData\Local\Programs\Python\Python312\python.exe' 10_evidence_portal\scripts\build_portal.py
```

Expected current results after rerun:

- `validate_claim_table.py`: `OK: 154 claims validated.`
- `check_missing_sources.py`: no missing archived local files and no
  high-priority rows needing attention.
- `check_mermaid.py`: all 8 diagrams structurally pass.
- `build_portal.py`: `Claims: 154 | Sources: 148 | Matrices: 6`.

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
| USDPT layer-3 architecture (Treasury and Agent Settlement; Digital Asset Network; Stable by WU consumer-spend layer) | `CLAIM_132` to `CLAIM_134` (via `USDPT_007` WU IR launch release) | Layer-3 architecture is anchored; product terms, reserve report, retail redemption and complete agent fiat cash-out workflow remain open under P0-1 below. |
| USDPT product-page reserve categories, official Solana address, coming-soon retail features, and ADB covered-stablecoin terms | `CLAIM_140` to `CLAIM_143`; `CLAIM_150`, `CLAIM_151` (via `USDPT_005` WU product page, `USDPT_010` Anchorage reserve-transparency page, and `USDPT_011` ADB Covered Stablecoin Terms) | Official Solana contract address, product-page features, ADB Client / Non-Client redemption boundary, reserve-trust framing, ADB sole-obligor role, brand-partner status and legal/control powers are anchored; USDPT-specific retail terms, fee schedule, attestation, exact token-control implementation and operational workflow remain open. |
| Maker / DAI Black Thursday case-study (community / analyst confidence) | `CLAIM_135` to `CLAIM_137` (via `FAILURE_007` Whiterabbit; `FAILURE_008` Glassnode) | Case study is closed at community / analyst level. A Maker Foundation primary source would upgrade confidence; public hourly DAI proxy is now available under P1-1, but exact duration/trough/recovery still require higher-quality data. |
| Taiwan VASP Act legislative-stage framing | `CLAIM_138`, `CLAIM_139`, `CLAIM_144`, `CLAIM_145`, `CLAIM_146` | Legislative-stage now runs through Executive Yuan approval/submission to Legislative Yuan (2026-04-02), Finance Committee first-review news (2026-06-03), and the official Legislative Yuan bill-detail docket showing committee-review entries through 2026-06-03 with gazette production pending. Enacted statutory text / FSC sub-rules remain under P0-3 below. |
| World Bank remittance-cost benchmark export | `CLAIM_147`; `WB_RPW_002`; `09_data_exports/remittance_benchmark/` | Reproducible off-chain remittance-cost benchmark is now available. It does not close Visa / Artemis / Cambridge adjusted stablecoin payment-volume evidence. |
| Failure-case public hourly proxy timelines | `CLAIM_148`, `CLAIM_149`; `CRYPTOCOMPARE_001`; `09_data_exports/failure_case_timelines/` | Reproducible public hourly proxy timelines are now available for USDC/SVB, Terra USTC and Maker DAI. Iron Finance remains unresolved because public IRON/TITAN rows are zero-only, and exact tick-level duration/trough/recovery still require higher-quality data. |
| USDT Q1 2026 detailed reserve-table extraction | `CLAIM_152`; `USDT_002`; `09_data_exports/issuer_details/usdt_q1_2026_reserve_breakdown.csv` | Full point-in-time reserve-category amounts are now extracted and rebuildable. Maturity ladder, custodian/counterparty split, collateral composition and smart-contract controls remain open. |
| USDC risk-factor address blocking / freeze / blacklisting-policy controls | `CLAIM_154`; `USDC_007` | Risk-factor / policy-control language is now anchored. Circle Mint eligibility, region-specific terms and chain-specific contract-code details remain open. |

## Priority Legend

- **P0**: Blocks a major conclusion in the current report or slides.
- **P1**: Important for stronger report quality, but current cautious wording
  is defensible.
- **P2**: Useful depth / appendix / later version material.
- **P3**: Housekeeping or low-risk enhancement.

## P0 Active Gaps

### P0-1. USDPT Product Layer And Workflow

Status: partially closed at v0.4. Layer 3 is anchored; the official Solana
contract-address gap is closed; coming-soon/select-market customer cash-out
and receive-in-USDPT direction is now supported at product-page level. Legal
terms, fee schedule, USDPT-specific attestation, exact token-control
implementation and full workflow remain source-dependent; ADB covered-
stablecoin terms now partially bound Client / Non-Client redemption rights,
reserve-trust structure, issuer-obligor role and legal/control powers.

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
- `CLAIM_132` (v0.3.3): WU 2026-05-04 IR launch release describes Digital
  Asset Network as the component bridging licensed virtual currency
  exchanges and custodians to WU's payout and liquidity infrastructure.
- `CLAIM_133` (v0.3.3): same release names Treasury and Agent Settlement
  as a USDPT use case enabling near-instant 24/7 settlement between WU and
  its global agents. Strongest layer-3 anchor in the archive.
- `CLAIM_134` (v0.3.3): Stable by Western Union announced as a separate
  consumer-spend product launching in 2026 in 40+ countries; kept
  distinct from USDPT issuance and settlement.
- `CLAIM_140` (v0.4, `USDPT_005` Western Union product page): USDPT is
  described as redeemable 1:1, issued by Anchorage Digital Bank N.A. on
  Solana, and backed by equal USD reserves including bank deposits, U.S.
  Treasuries, and similar cash equivalents.
- `CLAIM_141` (v0.4, `USDPT_005`): the product page discloses the official
  Solana contract address and states that no government or FDIC insurance
  applies.
- `CLAIM_142` (v0.4, `USDPT_005`): Western Union describes planned or
  coming-soon exchange support, cash-out at Western Union locations through
  a virtual-currency-exchange app in select markets, a self-custody wallet
  and Visa card app in select markets, and money-transfer receipt in USDPT
  in select markets.
- `CLAIM_143` (v0.4, `USDPT_010` Anchorage reserve-transparency page):
  Anchorage states that ADB stablecoins are redeemable 1:1 on its platform
  and that monthly reserve attestations are published, while the USDPT
  report slot is still marked "Coming soon."
- `CLAIM_150` (v0.4, `USDPT_011` ADB Covered Stablecoin Terms): ADB terms
  apply to ADB-issued payment-stablecoin series, distinguish Clients from
  Non-Clients, and limit direct ADB issuance/redemption to Clients.
- `CLAIM_151` (v0.4, `USDPT_011`): ADB terms describe a Covered Stablecoin
  Reserve trust, ADB sole issuer / sole obligor status, brand partners as
  service providers rather than obligors, par value only for direct Client
  redemption with ADB, and legal/regulatory freeze or restriction powers.
- Dedicated queue:
  `00_project_management/usdpt_product_terms_research_queue.md`.

What is still missing:

- USDPT-specific product terms / user terms, fee schedule, and retail risk
  disclosure.
- Anchorage Digital Bank USDPT-specific series supplement, if any.
- USDPT-specific reserve report, attestation, or detailed reserve composition
  disclosure beyond product-page reserve categories and ADB general reserve
  trust terms.
- Token metadata and exact mint / burn / freeze-control implementation beyond
  the disclosed official Solana contract address and ADB general legal-control
  powers.
- Direct retail / agent redemption policy and eligible redeemer scope beyond
  ADB Client / Non-Client boundary.
- End-to-end customer-to-customer or customer-to-agent workflow.
- Stable by Western Union product terms, eligible jurisdictions list, and
  the operational relationship between Stable by WU and USDPT.
- Whether Western Union agents hold, redeem, or settle USDPT on their own
  balance sheets. Product-page evidence only supports planned / coming-soon
  customer cash-out at WU locations through exchange-app rails in select
  markets.
- Actual settlement route between USDPT on-chain transfer and bank,
  correspondent, Fedwire, CHIPS, or local payout rails.

Do not claim:

- USDPT replaces SWIFT.
- USDPT replaces correspondent banking.
- USDPT replaces Fedwire or CHIPS.
- Western Union agents themselves hold, redeem, or cash out USDPT.
- Any holder can redeem USDPT 1:1; current ADB terms limit direct ADB
  redemption to Clients.
- USDPT reserve composition is equivalent to USDC / Paxos / GENIUS reserves.
- USDPT is a fully operational production remittance architecture beyond what
  WU / Anchorage / Fireblocks materials state.
- The disclosed Solana address proves circulating supply, mint / burn
  controls, freeze controls, sanctions controls, or reserve adequacy.
- Coming-soon / select-market customer features are already live globally.

Safe current wording (v0.4):

> Western Union has launched USDPT issued by Anchorage Digital Bank N.A.
> on Solana as a regulated digital-asset settlement layer for Treasury
> and Agent Settlement. The product page now supports 1:1 redeemability
> wording, broad reserve categories, an official Solana contract address,
> and planned / coming-soon exchange, cash-out, card and receive-in-USDPT
> customer features in select markets. ADB covered-stablecoin terms now bound
> direct ADB redemption to Clients, distinguish Non-Clients, describe a
> reserve trust and ADB sole-obligor role, and reserve legal/control powers.
> The public archive still does not support USDPT-specific retail/user terms,
> a USDPT-specific attestation report, exact mint / burn / freeze-control
> implementation, agent balance-sheet treatment, full operational workflow,
> or SWIFT / correspondent-banking replacement claims.

Resolution criteria:

1. Add new primary source(s) as `USDPT_###` or `ANCHORAGE_###`.
2. Add claim rows for USDPT-specific retail/user terms, fee schedule,
   USDPT-specific reserve report, retail/agent eligible redeemer scope beyond
   ADB Client status, exact token-control metadata, workflow, and agent /
   treasury role.
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

Status: partially narrowed at v0.4. The World Bank off-chain remittance-cost
benchmark export is now reproducible from the World Bank API (`CLAIM_147`),
but this does not close the adjusted stablecoin payment-volume gap. Visa
Onchain Analytics adjusted-volume export, Artemis Pro adjusted-volume export,
Cambridge Digital Money Dashboard numerical export, and McKinsey/Artemis
report still require subscriptions, manual licensed acquisition, or a
reproducible export.

Current supported evidence:

- `CLAIM_054`: Artemis documentation supports a schema for stablecoin
  transfer volume, transactions, supply, addresses, and filter categories
  such as `None`, `ARTEMIS`, and `P2P`.
- `CLAIM_055`: DeFiLlama API snapshots support stablecoin supply and
  chain-distribution analysis, not adjusted payment-volume evidence.
- `09_data_exports/` includes reproducible DeFiLlama exports for supply /
  chain distribution.
- `CLAIM_147`: World Bank API indicator `SI.RMT.COST.IB.ZS` is now exported
  reproducibly under `09_data_exports/remittance_benchmark/`, with 17,556
  country/region-year rows and a 104-row latest non-null benchmark file.
  This is off-chain remittance-cost benchmark context, not stablecoin
  adjusted-volume evidence.

What is still missing:

- Reproducible Visa Onchain Analytics adjusted-volume export.
- Reproducible Artemis adjusted-volume export beyond the existing schema /
  methodology claim.
- Cambridge Digital Money Dashboard numerical export.
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

> The project can support supply, chain-distribution and off-chain remittance
> cost benchmark context, and it can explain why raw transfer volume overstates
> payment demand. It cannot yet estimate realised stablecoin payment volume
> without reproducible adjusted exports and methodology reconciliation.

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

Status: legislative-stage anchored through v0.4; enacted statute and FSC
sub-rules remain unresolved and source-dependent.

Current supported evidence:

- `CLAIM_112` to `CLAIM_118` support CBC policy framing for:
  private tokenised money, central-bank-money anchor, USD-stablecoin
  digital-dollarisation / FX-management risk, NTD-stablecoin stored-value
  framing, 100% reserve design, no-yield treatment, disclosure, asset
  segregation, audit/assurance, and FSC-CBC consultation.
- `CLAIM_138` (v0.3.3, `TAIWAN_VASP_001` Focus Taiwan / CNA English): FSC
  Chairman Peng Jin-lung 2025-12-03 publicly stated that Taiwan's first
  regulated stablecoin may launch in H2 2026 at the earliest and that a
  six-month buffer applies after subordinate regulations are published.
- `CLAIM_139` (v0.3.3, `TAIWAN_VASP_002` Stellex Law commentary): draft
  Virtual Asset Service Provider (VASP) Act was submitted to the
  Executive Yuan in late June 2025 and remained under executive review
  as of 2025-12; draft requires domestic stablecoin issuance to obtain
  prior approval from the competent authority, requires foreign-issued
  stablecoins to obtain consent before trading on Taiwan VASP platforms,
  imposes reserve / audit / disclosure obligations, and is accompanied
  by at least eight subordinate regulations in preparation.
- `CLAIM_144` (v0.4, `TAIWAN_VASP_003` Executive Yuan): the Executive
  Yuan approved the FSC draft VASP Act on 2026-04-02 and submitted it to
  the Legislative Yuan; the official release says the draft covers VASPs
  and stablecoin issuers and includes financial-soundness, segregated
  custody, and unfair-trading safeguards.
- `CLAIM_145` (v0.4, `TAIWAN_VASP_004` UDN / Economic Daily News):
  news coverage reports that the Legislative Yuan Finance Committee first
  review of the VASP draft passed on 2026-06-03, including licensing,
  full reserve segregation, and fraud / manipulation penalties. Treat as
  committee-stage news until an official Legislative Yuan record or
  enacted text is registered.
- `CLAIM_146` (v0.4, `TAIWAN_VASP_005` Legislative Yuan): the official
  bill-detail page for the Executive Yuan draft lists the case as referred
  for review, assigned to the Finance Committee, and records committee
  review entries on 2026-05-07, 2026-06-01, and 2026-06-03 with gazette
  production pending for the June entries.

What is still missing:

- Enacted Taiwan VASP Act statutory text from the Legislative Yuan /
  Presidential Office gazette, once passed.
- Final Legislative Yuan committee report / gazette text for the 2026-06-03
  committee stage, once produced.
- Final FSC sub-rules, licensing forms, consultation documents, or
  official explanatory notes.
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

Safe current wording (v0.4):

> CBC materials support a Taiwan policy synthesis. The draft VASP Act is
> claim-backed at legislative-stage only: FSC Chair Peng Jin-lung
> publicly stated on 2025-12-03 that the first regulated stablecoin may
> launch in H2 2026 at the earliest; the Executive Yuan approved the FSC
> draft and submitted it to the Legislative Yuan on 2026-04-02; 2026-06-03
> news reports say the Legislative Yuan Finance Committee first review
> passed; and the official Legislative Yuan bill-detail page records
> committee-review entries through 2026-06-03 with gazette production
> pending. Taiwan statutory conclusions should still wait for enacted text
> or official FSC/CBC sub-rules.

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

Status: partially narrowed at v0.4. CoinGecko now returns 401 without an API
key for tested historical range requests, but CryptoCompare's public
`histohour` endpoint produced a reproducible hourly proxy export for selected
USDC/SVB 2023, Terra USTC 2022, and Maker DAI Black Thursday 2020 windows
(`CLAIM_148`, `CLAIM_149`). Iron Finance remains unresolved at price-timeline
level because the public CryptoCompare IRON/TITAN rows are zero-only and
CoinPaprika historical OHLCV returned HTTP 402 in spot tests.

Current supported evidence:

- `CLAIM_107`: SEC description of Terra UST as algorithmic stablecoin and
  May 2022 collapse.
- `CLAIM_108`, `CLAIM_109`: Circle's USDC/SVB depeg and backlog-clearing
  statements.
- `CLAIM_110`: NYAG Tether / Bitfinex investigation and settlement.
- `CLAIM_111`: Iron Finance post-mortem characterising the IRON/TITAN event
  as a bank run.
- Current `FAILURE_001` to `FAILURE_006` rows are `url_only`.
- `CLAIM_148`: `09_data_exports/failure_case_timelines/` now includes a
  reproducible CryptoCompare public hourly OHLCV proxy export: 749 hourly rows
  and a 5-row summary table. USDC, USTC and DAI are usable public hourly
  proxies; IRON/TITAN are zero-only and not usable as Iron Finance price
  timelines.
- `CLAIM_149`: the public hourly proxy provides coarse USDC/SVB, Terra USTC,
  and Maker DAI event-window metrics. Use as public hourly context only, not
  exact depeg duration / tick-level trough evidence.

What is still missing:

- Usable Iron Finance IRON/TITAN price series from a non-zero historical data
  source.
- Higher-quality paid or exchange-level historical data for exact depeg
  duration, tick-level trough, recovery time, and liquidity path.
- Provider methodology comparison between CryptoCompare public OHLCV and
  paid feeds such as Kaiko, Coin Metrics, Amberdata or CryptoCompare Pro.
- Local archive for the currently `url_only` failure sources if strict local
  reproducibility is desired.

Do not claim:

- Exact depeg duration, tick-level trough, recovery time, or liquidity path
  from the CryptoCompare public hourly proxy alone.
- Iron Finance price timeline from the zero-only IRON/TITAN public proxy rows.
- Terra / Iron / USDC / Tether cases are mechanically equivalent.
- Current reserve condition from historical failure-case sources.

Safe current wording:

> Failure-case sources support qualitative risk channels, and the project now
> has public hourly proxy timelines for USDC/SVB, Terra USTC and Maker DAI.
> Exact depeg duration, tick-level trough/recovery, and Iron Finance price
> timeline claims still require a better historical data source.

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

### P1-2. Maker / DAI Black Thursday Maker Foundation Primary Source

Status: case study closed at v0.3.3 at community / analyst confidence;
Maker Foundation primary source still missing and source-dependent.

Current supported evidence:

- `CLAIM_098` to `CLAIM_102` support Maker / Sky core mechanics: vaults,
  collateralisation, auctions, DSR / Sky Savings Rate, Keepers, Oracles,
  Global Settlers, and USDS / sUSDS / stUSDS mapping at product-page level.
- `CLAIM_135` (v0.3.3, `FAILURE_008` Glassnode): ETH -43% on 2020-03-12
  ($194 → $111), gas spike >6x to ~80 Gwei with hourly peaks ~200 Gwei,
  Medianizer oracle showed ~$166 versus spot ~$130.
- `CLAIM_136` (v0.3.3, `FAILURE_007` Whiterabbit): 1,462 of 3,994
  collateral auctions (~36.6%) closed at 100% discount; 62,892.93 ETH and
  US$8.325 million liquidated for zero DAI bids; 5.67 million DAI of
  protocol undercollateralisation.
- `CLAIM_137` (v0.3.3, `FAILURE_008` Glassnode): community vetoed
  Emergency Shutdown; max lot size raised 50 → 500 ETH; auction duration
  extended; MKR Debt Auction commenced 2020-03-19 to recapitalise.

What is still missing:

- A MakerDAO Foundation / governance forum / official post-mortem source
  for Black Thursday. The legacy `blog.makerdao.com` URL has been
  redirected to `sky.money` and the original Foundation post is no
  longer published at the original location.
- Maker Foundation public statement on final post-event MKR dilution,
  recapitalisation outcome, or claims-process settlement.
- Page-level mapping of the legacy 2020 MakerDAO Maker Vault / Cat /
  Flopper / Vow architecture to the current Sky LSE / Spark architecture.

Do not claim:

- A Maker Foundation primary post-mortem exists in the local archive.
- Current Sky risk is identical to 2020 Maker risk; pair the case with
  current Sky governance circuit breakers and collateral mix.
- Black Thursday auction figures should be upgraded to high confidence
  while only community and analyst sources are anchored.

Safe current wording:

> MakerDAO Black Thursday 2020-03-12 is claim-backed in this repository
> via Whiterabbit and Glassnode community / analyst sources at medium
> confidence. A Maker Foundation primary source would upgrade the case
> study but is not currently archived.

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
- `CLAIM_152`: Q1 2026 reserve-table extraction from `USDT_002`, with total
  reserves/assets and category-level amounts for Treasury bills, repos,
  cash/bank deposits, precious metals, Bitcoin, public equities, other
  investments and secured loans.
- `CLAIM_153`: Tether International entity / El Salvador regulatory framing,
  13 approved blockchains at the reporting date, and discontinued redemption
  obligations for legacy networks/tokens.

Open questions:

- Maturity ladder, custodian/counterparty split, liquidity-stress details, and
  loan collateral composition behind the extracted Q1 2026 reserve categories.
- Redemption fee, minimum, timing, operational delay, and bank-transfer
  mechanics.
- Smart-contract freeze / blacklist / pause powers.
- Separation among USDT, Tether International / El Salvador registration, and
  any future GENIUS-compliant USAT structure beyond the Q1 2026 report note.

Do not claim:

- USDT is a pure cash equivalent.
- Any holder can redeem directly with Tether.
- Current smart-contract control powers without source-backed extraction.

Resolution criteria:

- Add claims from contract documentation and any official USAT / Tether
  International materials that address smart-contract controls, fees,
  redemption operations, custodian/counterparty detail or USAT/USDT
  separation.
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

- Product name and ticker stability: primary rows mostly use USDPT, but
  `USDPT_001` retains a UDSPT spelling in the Anchorage comment-letter
  archive and should be treated as source spelling rather than silently
  normalised.
- Issuer legal entity is now anchored as Anchorage Digital Bank N.A.; any
  co-branding / program-manager structure still needs product terms.
- Reserve trust, USDPT-specific reserve report, and attestation cadence.
- Token metadata and mint / burn controls beyond the disclosed official
  Solana contract address.
- Direct redemption rights and eligible redeemers beyond broad 1:1
  redeemability statements.
- Freeze / blacklist / suspension / sanctions controls.
- Holder yield / reserve-yield treatment.

Do not claim:

- USDPT can be compared issuer-by-issuer with USDC, USDT, Paxos, GUSD,
  FDUSD, RLUSD on redemption or reserve composition until product terms and
  reserve reports exist. The product page narrows the gap but does not close
  issuer-comparison parity.

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
- `FAILURE_001` to `FAILURE_008`: `url_only`.
- `USDPT_010`: `url_only`, medium-priority Anchorage transparency page;
  no USDPT-specific report is available yet.
- `USDPT_011`: `url_only`, medium-priority Anchorage Covered Stablecoin
  Terms page; not a USDPT-specific fee schedule or reserve report.
- `TAIWAN_VASP_001` to `TAIWAN_VASP_005`: `url_only`, legislative-stage
  Taiwan sources. `TAIWAN_VASP_003` is official Executive Yuan;
  `TAIWAN_VASP_004` is committee-stage news; `TAIWAN_VASP_005` is the
  official Legislative Yuan bill-detail docket, with June committee gazette
  text still pending.

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
