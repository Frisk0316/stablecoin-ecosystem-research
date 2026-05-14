# Agent Instructions

This repository is a stablecoin ecosystem research project.

## Non-negotiable research rules

1. Do not add a major conclusion to the final report unless it is backed by `03_claim_tables/claim_table_master.csv`.
2. Every claim must have a `source_id`, `page_or_section`, evidence summary, and confidence level.
3. Do not call an attestation or assurance report an audit unless the source explicitly says audit.
4. Do not describe SWIFT as a funds-settlement system. Treat it as a messaging/network layer unless a source says otherwise.
5. Do not equate raw on-chain transfer volume with real payment volume.
6. Distinguish fiat-backed, crypto/RWA-collateralized, algorithmic, and synthetic-dollar stablecoins.
7. Preserve open questions rather than guessing.
8. If a source is dynamic HTML, record access date or local saved copy.

## Workflow

- Update source registry first.
- Then update source digest.
- Then update claim table.
- Then update comparison matrix.
- Then update chapter drafts.
- Final report should only summarize verified claims.

## Branch naming

```
main        stable release only
dev         integration branch
feature/*   module-specific research branches
```

Recommended feature branches:

```
feature/issuer-page-level-extraction
feature/law-genius-mica-nydfs
feature/central-bank-imf-fed
feature/payment-usdpt-western-union
feature/onchain-data
feature/failure-cases
```

## Traceability requirement

No major conclusion should appear in the final report unless it is traceable to a claim in
`03_claim_tables/claim_table_master.csv` and a source in `01_sources/source_registry.csv`.
