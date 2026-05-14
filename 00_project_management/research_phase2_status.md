# Stablecoin Research Phase 2 Status

## Completed in this pass

- Corrected semantically wrong `source_id` references in the master claim
  table for USDT, PYUSD, and GUSD.
- Added one official URL-only source: `USDT_006`, Tether's May 1, 2026 Q1
  reserve-buffer release.
- Added 10 issuer claims (`CLAIM_026` to `CLAIM_035`) covering USDC reserve
  categories, Tether Q1 reserve composition, PayPal crypto-hub eligibility,
  RLUSD product-page reserve/custody statements, and GUSD reserve/redemption
  product-page statements.
- Rebuilt the issuer digest into a readable Phase 2 working draft.
- Updated the issuer comparison matrix for USDC, USDT, PYUSD, RLUSD, and GUSD.
- Updated chapter drafts 2 and 3 with traceable Phase 2 findings.
- Rebuilt open questions to reflect what is now partially answered and what
  remains missing.

## Validation

- `validate_claim_table.py`: OK, 35 claims validated.
- `issuer_comparison_matrix.csv`: parsed successfully as 11 rows with 16
  columns.
- `source_registry.csv`: parsed successfully as 83 rows.

## Current research position

Issuer evidence extraction has started. The strongest immediate outputs are
now the claim table, issuer source digest, and issuer comparison matrix. The
final report should not yet be rewritten, because several high-impact
questions remain unresolved: NYDFS original guidance, Paxos/PayPal direct
redemption rights, USDT detailed reserve table extraction, USDP monthly report,
USDPT product documents, and on-chain adjusted-volume data.

## Recommended next steps

1. Extract NYDFS stablecoin guidance and update law / issuer matrices.
2. Extract direct redemption and suspension terms for USDC, USDT, PYUSD, USDG,
   RLUSD, GUSD, and FDUSD.
3. Extract the full Tether Q1 2026 reserve table from `USDT_002`.
4. Fetch or manually add the USDP monthly reserve report.
5. Ingest Visa and DeFiLlama stablecoin data with clear caveats against using
   raw transfer volume as payment volume.
