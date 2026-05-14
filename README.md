# Stablecoin Ecosystem Research — Delivery v0.1

This is the first structured delivery package for the stablecoin ecosystem research project. It is designed as a reproducible research package rather than a single narrative report.

## Delivery date

2026-05-14

## What is included

- Source registry built from the uploaded archive and previous uploads.
- First issuer comparison matrix covering USDC, USDT, PYUSD, USDP, USDG, RLUSD, FDUSD, GUSD, DAI/USDS, USDe, and USDPT/UDSPT.
- Draft claim table with source-backed claims.
- Draft source digests.
- Draft legal, central-bank, and payment-settlement matrices.
- Draft chapter outlines and report v0.1.
- Mermaid flow diagrams for future HTML/report rendering.
- Validation scripts for claim tables and source registry.
- GitHub/Codex handoff instructions.

## Source coverage snapshot

Total source registry rows: **85**

Category counts:

- archive_reference: 1
- central_bank: 14
- issuer: 46
- law: 16
- payment_settlement: 6
- project_management: 2

Status counts:

- download_script: 2
- downloaded: 55
- html_saved: 25
- url_only: 3

## Important limitations of v0.1

This is not the final research report. It is the first structured research delivery. Several parts are intentionally marked as pending:

- NYDFS stablecoin guidance original source still needs final external fetch or manual download.
- IMF and Federal Reserve stablecoin sources are not yet included in the archive.
- On-chain data sources such as Visa, DeFiLlama, Cambridge, and Artemis are not yet ingested.
- USDPT/UDSPT documentation is still mostly inferred from Western Union / Anchorage materials; product terms, reserve report, and redemption mechanics remain open questions.
- Some issuer terms pages require page-level extraction in Phase 2.

## How to use this package

1. Start with `07_final_report/stablecoin_ecosystem_research_report_v0_1.md`.
2. Verify claims through `03_claim_tables/claim_table_master.csv`.
3. Use `04_matrices/issuer_comparison_matrix.csv` as the main issuer comparison database.
4. Use `01_sources/source_registry.csv` to trace every source document.
5. Use `GITHUB_REPO_CODEX_SPEC.md` if converting this package into a GitHub repository.
