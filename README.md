# Stablecoin Ecosystem Research

Current status: v1.0 academic draft / evidence portal build / v0.3.2 extraction base

This repository is a reproducible research package for stablecoins, dollar
money markets, issuer balance sheets, regulation, central-bank views,
cross-border settlement, on-chain data, and failure cases. It is not just a
single memo: the source registry, source digests, claim table, matrices,
chapter drafts, and final report are meant to stay traceable to each other.

## Current Snapshot

Last synchronized: 2026-05-26

Source registry rows: **137**

Claim table rows: **131**

Category counts:

- archive_reference: 2
- central_bank: 23
- failure_case: 6
- issuer: 62
- law: 22
- market_data: 13
- payment_settlement: 6
- project_management: 3

Status counts:

- api_saved: 2
- download_script: 2
- downloaded: 67
- dynamic_html_saved: 6
- html_saved: 53
- manual_needed: 1
- url_only: 6

## What Changed Since v0.1

The old v0.1 README said that NYDFS, MiCA, Fed, IMF, on-chain sources, and
USDPT materials were missing. That is no longer accurate.

Recovered or partially extracted:

- NYDFS and MiCA official sources are registered and locally archived.
- Federal Reserve and IMF source sets are registered and partly extracted.
- Visa, DeFiLlama, Cambridge, and Artemis sources are registered; DeFiLlama
  API snapshots and Artemis methodology claims are available.
- USDPT / Western Union launch and infrastructure evidence is registered and
  claim-backed.
- Issuer terms extraction now covers USDC, USDT, Paxos-family stablecoins,
  GUSD, RLUSD, FDUSD, and USDe.
- Failure-case sources and first-pass claims now cover Terra UST, USDC/SVB,
  Tether/Bitfinex, and Iron Finance.
- Taiwan CBC extraction now supports a claim-backed Taiwan-specific synthesis
  on NTD stablecoins, USD-stablecoin dollarisation, FX monitoring, M2/credit
  channels, and draft regulatory design.
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

Still unresolved:

- Adjusted on-chain payment-volume exports remain incomplete.
- `MCKINSEY_ARTEMIS_001` remains `manual_needed`.
- USDPT product terms, reserve report, contract addresses, direct redemption
  mechanics, and end-to-end workflow documents remain missing.
- Maker / DAI Black Thursday still needs a primary event source.
- Adjusted failure-case price/depeg timelines remain open.
- Enacted Taiwan stablecoin statutory text remains open if those sources
  become available.

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

Expected current claim-table result:

```text
OK: 131 claims validated.
```

`check_missing_sources.py` should report no missing archived local files and
no high-priority rows needing attention. It will list `MCKINSEY_ARTEMIS_001`
and failure-case URL-only sources as known unresolved / non-local items.
