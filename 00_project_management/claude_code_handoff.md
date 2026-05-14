# Claude Code Handoff - Stablecoin Research v0.3 Phase

Last updated: 2026-05-14 (v0.3 protocol + comparison batch closed)

Purpose: this is the working handoff for the remaining v0.3 work after the
legal batch closed. v0.2 closed Phase 0 cleanup, Phase 1a Paxos-family /
Gemini Dollar direct redemption, and Phase 1b GENIUS Act statutory anchors.
v0.3 legal batch then closed BoE 2023/2025, ESMA CASP/transfer services, and
MiCA significant-ART/EMT plus recovery/redemption plans. Remaining v0.3
work focuses on DAI/USDS, USDe risk, CLARITY Act, central-bank Taiwan
synthesis, and final-report consolidation.

## Current State (v0.3 protocol + comparison batch close)

The source registry remains the current archived source set, and the claim
table now runs through `CLAIM_106`. Chapter 4 has a cross-jurisdiction
comparison table covering GENIUS / MiCA ART / MiCA EMT / BoE / NYDFS.

Validated status:

- `08_scripts/validate_claim_table.py`: `OK: 106 claims validated.`
- `08_scripts/check_missing_sources.py`: no missing archived local files and
  no high-priority rows needing attention.
- Remaining deficient source: `MCKINSEY_ARTEMIS_001` is still
  `manual_needed` (deferred per user decision; revisit only if a local copy
  is obtained).
- Tooling note: PyMuPDF (`fitz`) is now used as a fallback PDF extractor for
  multi-column legal PDFs where pdfplumber returns only headings; installed
  in the user's local Python 3.12 environment.

Important current files:

- `01_sources/source_registry.csv`
- `03_claim_tables/claim_table_master.csv`
- `04_matrices/issuer_comparison_matrix.csv`
- `04_matrices/law_regulation_comparison_matrix.csv`
- `04_matrices/central_bank_theme_matrix.csv`
- `04_matrices/payment_settlement_matrix.csv`
- `02_source_digests/issuer_source_digest.md`
- `02_source_digests/law_source_digest.md`
- `02_source_digests/central_bank_source_digest.md`
- `02_source_digests/market_data_source_digest.md`
- `02_source_digests/payment_settlement_source_digest.md`
- `00_project_management/consolidated_phase_deficiency_review.md`
- `00_project_management/unresolved_open_questions.md`

## Claims Added Since Deficiency Recovery

`CLAIM_044` to `CLAIM_057`:

- Federal Reserve and IMF stablecoin banking/payment claims.
- USDPT/WU/Anchorage/Fireblocks launch and infrastructure claims.
- Artemis/DeFiLlama methodology and data-source claims.
- Paxos and Ripple restriction/freeze/suspension claims.

`CLAIM_058` to `CLAIM_071`:

- USDC Circle Mint direct redemption scope and no holder reserve-yield claim.
- USDT verified-customer redemption and prohibited-person claims.
- FDUSD/FD121 direct sale/redemption gating and suspension/limitation claims.
- USDe Mint User vs Holding User, U.S. user ineligibility, no USDe holder
  yield, and synthetic-dollar framing.
- USDG EU retail redemption criteria.
- MiCA ART Article 36 reserve, Article 39 redemption, and Article 40
  no-interest provisions.

`CLAIM_072` to `CLAIM_087` (v0.2 interim):

- Paxos USD Stablecoin Agreement entity allocation, Customer-only direct
  redemption gating for PYUSD/USDP/USDG, no-holder-yield rule, permitted
  reserve composition, and all-holders freeze/upgrade scope.
- Gemini Trust User Agreement Customer-only GUSD creation/redemption,
  three-account-type GUSD reserve structure, and one-Business-Day "Timely"
  redemption commitment.
- USDP transparency-page KPMG AICPA attestation framing and formally
  discontinued separate monthly reserve composition report.
- GENIUS Act Public Law 119-27 statutory anchors: issuer limitation,
  3-year transition + foreign issuer gating, exhaustive reserve
  composition list, monthly disclosure + registered-public-accounting-firm
  examination, holder yield prohibition, and customer-priority insolvency
  rule.

`CLAIM_088` to `CLAIM_097` (v0.3 legal batch):

- BoE 2023 discussion paper preferred 100% central bank deposit backing
  model with singleness-of-money framing and the recovery/administration
  plan plus statutory-trust shortfall reserve construct.
- BoE 2025 consultation revised 40% CBD + 60% UK short-dated government
  debt backing rule plus step-up regime, and £20,000 retail / £10 million
  business holding limits.
- ESMA CASP authorisation supervisory briefing (no low-risk CASPs;
  elevated-scrutiny thresholds) and ESMA Article 82 transfer-service
  guidelines with TOFR Article 14 gating.
- MiCA Article 45 significant-ART additional obligations (FRAND custody,
  liquidity management, 60% deposit floor), Article 46 ART recovery plan,
  Article 47 ART redemption (wind-down) plan, and Articles 56-58
  significant-EMT regime with six-monthly audits.

`CLAIM_098` to `CLAIM_106` (v0.3 protocol + comparison batch):

- MakerDAO MCD Protocol core mechanics: governance-approved collateral /
  Maker Vault overcollateralisation, Collateral Auction / Reverse
  Collateral Auction liquidation, Dai Savings Rate (now Sky Savings Rate
  via sUSDS), and Keepers / Oracles / Global Settlers external-actor
  surface.
- Sky.money rebrand mapping: USDS / sUSDS / stUSDS / SKY plus 1:1
  USDC↔USDS conversion and US-jurisdiction unavailability of yield
  modules.
- Ethena USDe peg mechanics: synthetic-dollar delta-neutral hedging at
  1:1 collateralisation; Off-Exchange Settlement custody mitigating but
  not eliminating exchange counterparty risk; monthly custodian
  attestations stating no backing assets reside directly on exchange
  partners; Reserve Fund composition, 4/10 multi-sig control, Q4 2024
  size $46.6m.
- Chapter 4 cross-jurisdiction comparison table covering GENIUS Act,
  MiCA ART, MiCA EMT, BoE systemic, and NYDFS guidance along six
  dimensions (eligible issuer, reserve composition, redemption right,
  insolvency/wind-down, holder yield/interest, significant-token
  threshold).

## Research Guardrails

- Final report conclusions must be backed by
  `03_claim_tables/claim_table_master.csv`.
- Do not equate raw stablecoin transfer volume, market cap, or supply with
  real payment demand.
- Do not call reserve attestations "audits" unless the source itself supports
  that term for the relevant engagement.
- Separate fiat-backed payment stablecoins, crypto/RWA-collateralized protocol
  stablecoins, and synthetic-dollar products.
- Separate broad product-page redemption language from legally gated direct
  redemption rights.
- Do not claim USDPT replaces SWIFT, correspondent banking, Fedwire, CHIPS, or
  Western Union's customer-facing remittance rails without workflow documents.
- Treat MiCA EMT and ART rules separately.

## Recommended Next Tasks (remaining v0.3)

The Phase 0 cleanup, Phase 1a (Paxos / Gemini), Phase 1b (GENIUS Act),
the Phase 1c legal batch (BoE 2023/2025, ESMA CASP/transfer services,
MiCA significant-ART/EMT and recovery/redemption plans), and the Phase 1d
protocol + comparison batch (DAI/USDS, USDe, chapter-4 comparison table)
are all closed. Claim table runs to `CLAIM_106`. The following items
remain on the v0.3 list.

### 1. CLARITY Act (Stablecoin-Specific Sections)

Targets:

- Isolate any stablecoin-specific provisions from the broader
  market-structure text.
- Do not infer stablecoin conclusions from general market-structure
  provisions.

### 2. Central-Bank Taiwan Synthesis

Files:

- `02_source_digests/central_bank_source_digest.md`
- `04_matrices/central_bank_theme_matrix.csv`
- `05_chapter_drafts/chapter_05_central_bank_views.md`

Targets:

- Extend the Fed/IMF context in `CLAIM_044`-`CLAIM_050` into
  Taiwan-specific implications using existing CBC and TWFRC sources only
  (do not introduce new sources).
- Themes: NTD stablecoin, FX monitoring, digital dollarisation, deposit
  substitution, monetary sovereignty.
- Keep bank-disintermediation claims conditional, not mechanical.

### 3. MiCA EMT Articles 51 / 52 / 55

Targets:

- Page-level extraction of MiCA EMT white paper rules (Article 51),
  marketing communications rules (Article 52), and additional issuer
  obligations (Article 55).
- Treat as supplementary to existing EMT claims (`CLAIM_042`, `CLAIM_043`,
  `CLAIM_097`).

### 4. v0.3 Final Report Consolidation

Targets:

- Snapshot `07_final_report/stablecoin_ecosystem_research_report_v0_3.md`
  once body chapters stabilise.
- Refresh `executive_summary.md` to reflect the closed claim set
  (`CLAIM_001` to `CLAIM_106`) and the cross-jurisdiction comparison
  table.

### 5. Data-Quality Cleanup

Targets:

- `DAI_USDS_003` ("Sky Protocol technical whitepaper 2025") is in fact
  about a Cardano Layer 2 data availability solution and is unrelated to
  the Maker/Sky stablecoin protocol. The registry row should be
  relabelled (e.g. as `OTHER_CARDANO_SKY_001`) or removed.

### 6. Deferred for v0.3 Unless New Sources Arrive

These were deferred in v0.2 per user scope decision and should not be
reopened without a new primary source:

- USDPT product terms, reserve reports, contract addresses, and end-to-end
  settlement workflow.
- Visa Onchain Analytics adjusted-volume export.
- Artemis methodology beyond `CLAIM_054`.
- McKinsey `MCKINSEY_ARTEMIS_001` manual download.

If you obtain a primary source for any of these, register it first, then
extract claims and update the relevant chapter draft. Do not infer
USDPT/SWIFT/correspondent-banking-replacement claims without workflow
documents.

Add new claims only when the evidence is clear and source-backed.

## Suggested Validation Commands

Run from repo root:

```powershell
& 'C:\Users\woody\AppData\Local\Programs\Python\Python312\python.exe' 08_scripts\validate_claim_table.py
& 'C:\Users\woody\AppData\Local\Programs\Python\Python312\python.exe' 08_scripts\check_missing_sources.py
```

Optional status check:

```powershell
git -c safe.directory='C:/財金所/2026 鏈上數據讀書會/06.27 穩定幣研究/stablecoin-ecosystem-research' status --short
```

## Expected Next Deliverable (v0.3)

The v0.2 interim delivery has closed the issuer-matrix cleanup, Paxos-family
direct redemption, Gemini Dollar customer-only rights, USDP reserve-report
status, and the GENIUS Act statutory anchors. The next useful deliverable
(v0.3) is:

- BoE / ESMA / MiCA significant-token / CLARITY page-level law extraction.
- DAI/USDS protocol-mechanics extraction and USDe risk extraction.
- Central-bank Taiwan-specific synthesis derived from existing CBC/TWFRC
  sources, without new external fetches.
- v0.3 final report consolidation snapshot
  (`07_final_report/stablecoin_ecosystem_research_report_v0_3.md`) once the
  body chapters are stable.
- Validation commands passing (`validate_claim_table.py`,
  `check_missing_sources.py`).
