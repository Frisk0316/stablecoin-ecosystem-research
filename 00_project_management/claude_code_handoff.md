# Claude Code Handoff - Stablecoin Research v0.3.2

Last updated: 2026-05-26

Purpose: working handoff for the stablecoin ecosystem research package after
the v0.3.2 evidence-base cleanup. This file supersedes older handoffs that
listed CLARITY, Taiwan CBC synthesis, MiCA EMT Article extraction, DAI/USDS,
USDe mechanics, or foreign-issuer equivalence as open v0.3 work.

## Current State

- Source registry: 137 rows.
- Claim table: 131 validated claims, `CLAIM_001` through `CLAIM_131`.
- Flow diagrams: 8 Mermaid diagrams.
- Main presentation package:
  - `07_final_report/slide_script_v0_3.md`
  - `07_final_report/slide_outline_v0_3.md`
- Evidence portal source:
  - `10_evidence_portal/`

Expected validation from repo root:

```powershell
& 'C:\Users\woody\AppData\Local\Programs\Python\Python312\python.exe' 08_scripts\validate_claim_table.py
& 'C:\Users\woody\AppData\Local\Programs\Python\Python312\python.exe' 08_scripts\check_missing_sources.py
& 'C:\Users\woody\AppData\Local\Programs\Python\Python312\python.exe' 08_scripts\check_mermaid.py
```

`MCKINSEY_ARTEMIS_001` remains the main manual-needed source. Several
failure-case sources are intentionally `url_only`; they do not currently
block missing-file validation.

## Closed In v0.3.2

### Foreign-Issuer Equivalence Screen

Added `CLAIM_126` to `CLAIM_131`:

- GENIUS Section 18 foreign-issuer exception and reciprocity path:
  Treasury comparability, Comptroller registration, U.S. customer-liquidity
  reserves unless reciprocal arrangement permits otherwise, sanctions /
  money-laundering-concern screening.
- MiCA Article 48 EMT issuer eligibility and Article 50 EMT no-interest rule.
- MiCA Article 56 non-euro significant-EMT home-state derogation.
- BoE 2025 cross-border use framing, HMT recognition, Bank/FCA joint
  regulation, robust legal claim and always-at-par fiat redemption.

Added:

- `04_matrices/foreign_issuer_equivalence_matrix.csv`

Updated:

- `02_source_digests/law_source_digest.md`
- `04_matrices/law_regulation_comparison_matrix.csv`
- `05_chapter_drafts/chapter_04_law_and_regulation.md`
- final-report summary, slide outline/script, and live unresolved backlog

Bounded conclusion: BoE and MiCA are comparison cases for GENIUS Section 18,
not automatically equivalent regimes. Do not state that any foreign regime has
Treasury-recognised comparability unless a future source supports it.

## Closed In v0.3.1

### Slide / Diagram Cleanup

- Rebuilt `07_final_report/slide_script_v0_3.md` from mojibake into a clean
  bilingual presentation script.
- Rebuilt `07_final_report/slide_outline_v0_3.md`.
- Added:
  - `06_flow_diagrams/dai_usds_protocol_flow.md`
  - `06_flow_diagrams/usde_synthetic_dollar_flow.md`

### Taiwan CBC Synthesis

Added `CLAIM_112` to `CLAIM_118` from archived CBC sources:

- Stablecoins as tokenised private-sector money, not legal tender.
- Central-bank money remains the anchor for singleness and final settlement.
- USD stablecoins as a digital-dollarisation and FX-management risk channel.
- NTD stablecoin as tokenised stored value with 100% reserves and CBC/FSC
  consultation.
- Limited current domestic payment, M2, credit, and monetary-policy impact
  under CBC's current framing.
- Draft Taiwan VASP/stablecoin requirements: issuance permission, issuer
  qualification, reserve management, asset segregation, audit/assurance,
  no interest/yield, and disclosure.

Updated:

- `02_source_digests/central_bank_source_digest.md`
- `04_matrices/central_bank_theme_matrix.csv`
- `05_chapter_drafts/chapter_05_central_bank_views.md`
- Slide 36 in the final-report package

### CLARITY / MiCA EMT Extraction

Added `CLAIM_119` to `CLAIM_121` from the CLARITY Act PDF:

- Definition of permitted payment stablecoin.
- Exclusion of permitted payment stablecoins / digital commodities from
  several securities-law definitions.
- SEC anti-fraud, anti-manipulation, insider-trading, and related
  market-structure authority in specified contexts.

Added `CLAIM_122` to `CLAIM_125` from official MiCA text:

- Article 51: EMT white paper content and form.
- Article 52: liability for white-paper information.
- Article 53: marketing communications.
- Article 55: recovery and redemption plans.

Updated:

- `02_source_digests/law_source_digest.md`
- `04_matrices/law_regulation_comparison_matrix.csv`
- `05_chapter_drafts/chapter_04_law_and_regulation.md`

### USDPT / Data Export Cleanup

- `00_project_management/usdpt_product_terms_research_queue.md` now separates
  supported, unsupported, and not-inferable USDPT assertions.
- `02_source_digests/payment_settlement_source_digest.md` now keeps USDPT
  customer UX, agent network, internal treasury, and reserve-bank settlement
  as separate evidentiary layers.
- `09_data_exports/README.md` now clarifies that the manifest lists only
  reproducible existing exports and that DeFiLlama supports supply / chain
  distribution, not payment adoption.

## Current Guardrails

- Do not equate raw stablecoin transfer volume, market cap, or supply with
  realised payment demand.
- Do not call reserve attestations audits unless the source uses that term
  for the relevant engagement.
- Separate fiat-backed payment stablecoins, crypto/RWA-collateralised
  protocol stablecoins, and synthetic-dollar products.
- Separate MiCA ART and MiCA EMT rules.
- Treat CLARITY as market-structure legislation unless a stablecoin-specific
  provision is directly cited.
- Do not claim USDPT replaces SWIFT, correspondent banking, Fedwire, CHIPS,
  or Western Union's customer-facing remittance rails without primary
  workflow documentation.

## Remaining Priority Work

1. USDPT primary documentation: USDPT-specific retail/user terms, fee
   schedule, reserve report, supported chain/network details beyond the
   disclosed Solana address, retail/agent direct redemption eligibility beyond
   ADB Client status, exact token-control implementation, and
   customer-to-customer settlement workflow. ADB Covered Stablecoin Terms are
   now registered as `USDPT_011` / `CLAIM_150` / `CLAIM_151`.
2. Adjusted payment-volume exports: Visa adjusted volume, Artemis
   reproducible methodology, Cambridge numerical export, and McKinsey /
   Artemis local archive. The World Bank off-chain remittance-cost benchmark
   export is now available, but it is not adjusted stablecoin payment volume.
3. Taiwan enacted legal text and sub-rules if official statutory or FSC/CBC
   materials become available after the CBC policy papers.
4. Failure-case data workflows: Iron Finance still lacks a usable price
   timeline, exact trough/duration/recovery claims still require higher-quality
   data, and Maker / DAI Black Thursday primary event extraction remains open.
   Public hourly proxy timelines are now available for USDC/SVB, Terra USTC
   and Maker DAI.
5. Remaining issuer details: USDT full reserve table, Circle Reserve Fund
   breakdown, RLUSD/GUSD smart-contract control terms, FDUSD entity/custody
   map, Maker RWA/PSM mechanics, and USDe exchange-exposure scenarios.

## Suggested Finalisation Commands

Run from repo root:

```powershell
& 'C:\Users\woody\AppData\Local\Programs\Python\Python312\python.exe' 08_scripts\validate_claim_table.py
& 'C:\Users\woody\AppData\Local\Programs\Python\Python312\python.exe' 08_scripts\check_missing_sources.py
& 'C:\Users\woody\AppData\Local\Programs\Python\Python312\python.exe' 08_scripts\check_mermaid.py
& 'C:\Users\woody\AppData\Local\Programs\Python\Python312\python.exe' 10_evidence_portal\scripts\build_portal.py
```

Optional status check:

```powershell
git -c safe.directory='C:/財金所/2026 鏈上數據讀書會/06.27 穩定幣研究/stablecoin-ecosystem-research' status --short
```
