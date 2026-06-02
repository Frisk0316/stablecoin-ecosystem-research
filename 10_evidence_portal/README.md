# Stablecoin Evidence Portal

This folder contains a zero-dependency static evidence portal for the stablecoin
research project.

The portal is generated from the repository's research database:

- `03_claim_tables/claim_table_master.csv`
- `01_sources/source_registry.csv`
- `04_matrices/*.csv`
- `07_final_report/stablecoin_academic_report_v1_0.md`

It is designed to answer one question quickly:

> Where does this sentence come from?

For every report paragraph that cites `CLAIM_###`, the generated site displays:

- the paragraph conclusion,
- corresponding `claim_id`,
- `source_id`,
- original source title,
- page or section,
- evidence summary,
- confidence,
- related matrix rows when detected,
- source URL or local archive link when available.

## Build

From the repository root:

```powershell
& 'C:\Users\woody\AppData\Local\Programs\Python\Python312\python.exe' 10_evidence_portal\scripts\build_portal.py
```

Output is written to:

```text
10_evidence_portal/site/
```

Open:

```text
10_evidence_portal/site/index.html
```

## Pages

- `index.html` - Executive Summary
- `issuer-comparison.html`
- `regulation.html`
- `central-bank-views.html`
- `payment-settlement.html`
- `onchain-data.html`
- `failure-cases.html`
- `source-registry.html`
- `claim-explorer.html`
- `methodology.html`

The generator also creates topic drill-down pages for the requested research
tree, including USDC, USDT, Paxos-family stablecoins, RLUSD, FDUSD, GUSD,
DAI/USDS, USDe, GENIUS Act, MiCA, NYDFS, BoE, ESMA/EBA, BIS, ECB, Fed, IMF,
FSB, Taiwan CBC, correspondent banking, Fedwire, Western Union, USDPT,
DeFiLlama, Visa/Artemis, Cambridge, Terra, Iron Finance, USDC/SVB,
USDT/NYAG, DAI/USDS stress, and USDe stress.

## Notes

This is intentionally a static-first implementation. It can later be migrated
to Astro, Starlight, Docusaurus, or Next.js without changing the underlying
research database.
