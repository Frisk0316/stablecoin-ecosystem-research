# Stablecoin Ecosystem Research

Current status: v1.0 academic draft / evidence portal build / v0.4 targeted gap closure

This repository is a reproducible research package for stablecoins, dollar
money markets, issuer balance sheets, regulation, central-bank views,
cross-border settlement, on-chain data, and failure cases. It is not just a
single memo: the source registry, source digests, claim table, matrices,
chapter drafts, and final report are meant to stay traceable to each other.

## Current Snapshot

Last synchronized: 2026-06-10

Source registry rows: **150**

Claim table rows: **157**

Category counts:

- archive_reference: 2
- central_bank: 23
- failure_case: 8
- issuer: 65
- law: 27
- market_data: 15
- payment_settlement: 7
- project_management: 3

Status counts:

- api_saved: 4
- download_script: 2
- downloaded: 67
- dynamic_html_saved: 6
- html_saved: 56
- manual_needed: 1
- url_only: 14

## What Changed Since v0.1

The old v0.1 README said that NYDFS, MiCA, Fed, IMF, on-chain sources, and
USDPT materials were missing. That is no longer accurate.

Recovered or partially extracted:

- NYDFS and MiCA official sources are registered and locally archived.
- Federal Reserve and IMF source sets are registered and partly extracted.
- Visa, DeFiLlama, Cambridge, and Artemis sources are registered; DeFiLlama
  API snapshots, Artemis methodology claims, and a reproducible World Bank
  remittance-cost benchmark export are available.
- USDPT / Western Union launch and infrastructure evidence is registered and
  claim-backed; product-page evidence now also supports USDPT's official
  Solana contract address, broad reserve categories, 1:1 redeemability
  wording, and coming-soon / select-market retail features.
- Issuer terms extraction now covers USDC, USDT, Paxos-family stablecoins,
  GUSD, RLUSD, FDUSD, and USDe.
- USDT Q1 2026 detailed reserve-table extraction is now exported from the
  local `USDT_002` PDF under `09_data_exports/issuer_details/`.
- Failure-case sources and first-pass claims now cover Terra UST, USDC/SVB,
  Tether/Bitfinex, Iron Finance, Maker Black Thursday, and public hourly
  proxy timelines for USDC/SVB, Terra USTC and Maker DAI.
- Taiwan CBC extraction now supports a claim-backed Taiwan-specific synthesis
  on NTD stablecoins, USD-stablecoin dollarisation, FX monitoring, M2/credit
  channels, and draft regulatory design.
- Taiwan VASP Act tracking now reaches Executive Yuan approval and
  Legislative Yuan submission on 2026-04-02, plus news-reported Finance
  Committee first review and an official Legislative Yuan bill-detail docket
  entry on 2026-06-03. It remains legislative-stage, not enacted-law
  analysis.
- CLARITY Act stablecoin-specific market-structure sections and MiCA EMT
  Articles 51, 52, 53, and 55 are now extracted; note that MiCA Article 52 is
  white-paper liability and Article 53 is marketing communications.
- Foreign-issuer equivalence analysis now has a dedicated GENIUS Section 18
  screen and comparison matrix at
  `04_matrices/foreign_issuer_equivalence_matrix.csv`. The conclusion is
  deliberately bounded: BoE and MiCA are comparison cases, not automatically
  Treasury-recognised equivalent regimes.
- A formal academic report draft now exists at
  `07_final_report/stablecoin_academic_report_v1_0.md`. **This is the canonical
  current report.** Earlier versions are preserved at
  `07_final_report/archive/v0_1/` and `07_final_report/archive/v0_2/` for
  historical reference only and should not be cited as current findings.
- A static Evidence Portal now exists at `10_evidence_portal/site/index.html`.
  It joins report paragraphs to `claim_id`, `source_id`, document metadata,
  page/section, evidence summary, confidence, matrix hits, and source links.

v0.4 (2026-06-05) targeted gap closure:

- USDPT product-page and ADB covered-stablecoin terms evidence added:
  `CLAIM_140` to `CLAIM_143` and `CLAIM_150` to `CLAIM_151` register
  Western Union's 1:1 redeemability wording, broad reserve categories,
  official Solana contract address, planned / coming-soon exchange, cash-out,
  card and receive-in-USDPT features in select markets, and Anchorage's
  reserve-transparency page showing the USDPT report slot as "Coming soon".
  ADB terms now bound Client vs Non-Client redemption rights, reserve trust,
  ADB sole-obligor status, brand-partner status, and legal/control powers for
  ADB-issued series. Remaining USDPT gaps are USDPT-specific retail/user
  terms, fee schedule, reserve attestation, exact token-control
  implementation, agent balance-sheet treatment, full operational workflow,
  and bank/clearing route.
- Taiwan legislative-stage evidence added: `CLAIM_144` to `CLAIM_146`
  register Executive Yuan approval / Legislative Yuan submission on
  2026-04-02, news-reported Finance Committee first review on
  2026-06-03, and the official Legislative Yuan bill-detail docket showing
  committee-review entries through 2026-06-03 with gazette production
  pending. Enacted text, FSC sub-rules, and official detailed rulemaking
  remain open.
- World Bank remittance-cost benchmark export added: `WB_RPW_002` and
  `CLAIM_147` register a reproducible WDI API pull for indicator
  `SI.RMT.COST.IB.ZS`, exported under `09_data_exports/remittance_benchmark/`.
  This closes the off-chain remittance-cost benchmark layer only; it does
  not close Visa / Artemis / Cambridge adjusted stablecoin payment-volume
  evidence.
- Failure-case public hourly proxy export added: `CRYPTOCOMPARE_001`,
  `CLAIM_148` and `CLAIM_149` register reproducible hourly OHLCV proxy
  timelines under `09_data_exports/failure_case_timelines/`. The export is
  usable as coarse public timeline context for USDC/SVB, Terra USTC and
  Maker DAI, but Iron Finance IRON/TITAN rows are zero-only and exact
  tick-level duration/trough/recovery claims still require higher-quality
  data.
- USDT Q1 2026 reserve-table extraction added: `CLAIM_152`, `CLAIM_153`,
  and `09_data_exports/scripts/build_usdt_q1_2026_reserve_breakdown.py`
  register a rebuildable export from `USDT_002`. This closes the detailed
  point-in-time reserve-category extraction gap; maturity ladder,
  custodian/counterparty split, collateral detail, fees/redemption operations,
  and smart-contract controls remain open.
- USDC risk-factor control extraction added: `CLAIM_154` anchors Circle's
  address-blocking, Circle-custodied USDC freeze, Blocked Address flow, and
  blacklisting-policy transfer-control language from `USDC_007`. Chain-specific
  contract-code extraction and Circle Mint eligibility mapping remain open.

v0.3.3 (2026-06-02) evidence-base reinforcement:

- USDPT product layer partially closed: `CLAIM_132` (Digital Asset
  Network bridge to licensed virtual currency exchanges and custodians),
  `CLAIM_133` (Treasury and Agent Settlement use case), and `CLAIM_134`
  (Stable by Western Union 40+ country consumer-spend pilot) anchored to
  the 2026-05-04 Western Union investor-relations launch release
  (`USDPT_007`). Product terms, reserve report, contract addresses and
  retail-redemption / agent-cash-out workflow remain missing.
- Maker / DAI Black Thursday closed at community / analyst confidence:
  `CLAIM_135` (ETH crash, gas spike, Medianizer oracle lag — Glassnode),
  `CLAIM_136` (1,462 / 3,994 zero-bid auctions, 62,892.93 ETH and
  US$8.325m extracted for zero DAI, 5.67M DAI protocol loss —
  Whiterabbit) and `CLAIM_137` (Emergency Shutdown vetoed, immediate
  auction parameter patches, 2020-03-19 MKR Debt Auction — Glassnode).
  Maker Foundation primary source would upgrade confidence.
- Taiwan VASP Act legislative-stage anchored: `CLAIM_138` (FSC Chair
  2025-12-03 public statement on H2 2026 earliest launch plus six-month
  buffer) and `CLAIM_139` (executive-review status of the draft VASP
  Act, prior-approval / consent / reserve / audit / disclosure
  obligations, eight subordinate regulations in preparation). Enacted
  statute or FSC sub-rules would upgrade to enacted-law analysis.

Still unresolved at v0.4:

- Adjusted on-chain payment-volume exports remain incomplete for Cambridge,
  Visa Onchain Analytics, Artemis adjusted series, and
  `MCKINSEY_ARTEMIS_001` manual archive. The World Bank remittance-cost
  benchmark export is now reproducible through `CLAIM_147`, but it is
  off-chain cost context rather than stablecoin adjusted-volume evidence.
- USDPT legal and operational gaps are partially narrowed by ADB
  covered-stablecoin terms, but USDPT-specific retail/user terms, fee
  schedule, reserve attestation, exact token-control implementation beyond
  the disclosed Solana address, agent balance-sheet treatment, full
  operational workflow, and bank/clearing settlement route remain missing
  despite the v0.3.3/v0.4 anchors above.
- Failure-case price / depeg timelines are only partially closed: public
  hourly proxies now exist for USDC/SVB, Terra USTC and Maker DAI through
  `CLAIM_148` and `CLAIM_149`, but Iron Finance remains unresolved and
  exact tick-level or exchange-level trough/duration/recovery claims still
  require paid or higher-quality historical feeds.
- Maker / DAI Black Thursday primary Maker Foundation source would
  upgrade `CLAIM_135` to `CLAIM_137` from medium-confidence community /
  analyst anchors.
- Enacted Taiwan VASP Act statutory text or FSC sub-rules remain open.
- Foreign-issuer equivalence remains screened, not adjudicated, pending
  a Treasury comparability determination.

## Research Rules

See `AGENTS.md`. The most important rule is:

> No major conclusion should appear in the final report unless it is traceable
> to `03_claim_tables/claim_table_master.csv` and
> `01_sources/source_registry.csv`.

Other guardrails:

- Do not call an attestation or assurance report an audit unless the source
  explicitly says audit.
- Do not describe SWIFT as a funds-settlement system.
- Do not equate raw on-chain transfer volume with real payment volume.
- Distinguish fiat-backed, crypto/RWA-collateralized, algorithmic, and
  synthetic-dollar stablecoins.
- Preserve open questions rather than guessing.

## How To Use This Repository

1. Start with `07_final_report/stablecoin_academic_report_v1_0.md` for the
   main academic draft.
2. Use `10_evidence_portal/site/index.html` to browse the claim-backed
   evidence portal.
3. Verify important conclusions through `03_claim_tables/claim_table_master.csv`.
4. Use `01_sources/source_registry.csv` to trace every source document.
5. Use `04_matrices/issuer_comparison_matrix.csv` and
   `04_matrices/law_regulation_comparison_matrix.csv` for structured
   comparison.
6. Use `00_project_management/unresolved_open_questions.md` for the live
   backlog. `00_project_management/consolidated_phase_deficiency_review.md`
   is a historical deficiency trail with a v0.3.1 superseding note.

## Evidence Portal

Rebuild from the repository root:

```powershell
& 'C:\Users\woody\AppData\Local\Programs\Python\Python312\python.exe' 10_evidence_portal\scripts\build_portal.py
```

Open:

```text
10_evidence_portal/site/index.html
```

## Validation

Run from the repository root:

```powershell
& 'C:\Users\woody\AppData\Local\Programs\Python\Python312\python.exe' 08_scripts\validate_claim_table.py
& 'C:\Users\woody\AppData\Local\Programs\Python\Python312\python.exe' 08_scripts\check_missing_sources.py
```

Current claim-table target after the `CLAIM_155`-`CLAIM_157` additions;
full Python validation rerun passed on 2026-06-10:

```text
OK: 157 claims validated.
```

`check_missing_sources.py` should report no missing archived local files and
no high-priority rows needing attention. It will list `MCKINSEY_ARTEMIS_001`
and the `FAILURE_001` to `FAILURE_005`, `FAILURE_007`, `FAILURE_008`,
`USDPT_010`, `USDPT_011`, and `TAIWAN_VASP_001` to `TAIWAN_VASP_005` `url_only`
sources as known no-local / non-blocking items. (`FAILURE_006`, `USDPT_012`,
and `VISA_ALLIUM_001` were archived to local HTML on 2026-06-11 and are now
`html_saved`.)

Current portal build target after the `CLAIM_155`-`CLAIM_157` additions;
portal rebuilt on 2026-06-10:

```text
Claims: 157 | Sources: 150 | Matrices: 6
```
