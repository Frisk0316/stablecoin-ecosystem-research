# Stablecoin Research Phase 3 Status

## Completed in this pass

- Added `NYDFS_001` as URL-only primary source for the June 8, 2022 NYDFS
  stablecoin guidance.
- Added `MICA_004` as URL-only primary source for Regulation (EU) 2023/1114
  through the official EUR-Lex identifier.
- Added 8 legal/regulatory claims (`CLAIM_036` to `CLAIM_043`):
  NYDFS scope, backing, redemption, reserve assets, attestations, MiCA scope,
  MiCA EMT par redemption, and MiCA EMT fund investment/safeguarding.
- Rebuilt `02_source_digests/law_source_digest.md` as a readable Phase 3
  working digest.
- Updated `04_matrices/law_regulation_comparison_matrix.csv` for NYDFS and
  MiCA.
- Rewrote `05_chapter_drafts/chapter_04_law_and_regulation.md` with
  traceable Phase 3 findings.
- Added `00_project_management/known_deficiencies_phase3.md`.

## Validation

- `validate_claim_table.py`: OK, 43 claims validated.
- `source_registry.csv`: parsed successfully as 85 rows.
- `law_regulation_comparison_matrix.csv`: parsed successfully as 9 rows and 8
  columns.
- `issuer_comparison_matrix.csv`: parsed successfully as 11 rows and 16
  columns.

## Current research position

The project now has two strengthened pillars: issuer evidence and regulatory
evidence. The final report should still not be treated as final because the
research remains incomplete for on-chain adjusted volume, USDPT / UDSPT, IMF /
Fed views, direct issuer terms, and normalized reserve composition.

## Recommended next steps

1. Save local archival copies of `NYDFS_001` and `MICA_004`.
2. Upgrade `check_missing_sources.py` so it distinguishes fully missing,
   URL-only registered, and locally archived sources.
3. Extract issuer terms for direct redemption and suspension rights.
4. Ingest market/on-chain datasets: Visa, DeFiLlama, Cambridge, Artemis.
5. Continue central-bank source expansion with IMF and Fed sources.
