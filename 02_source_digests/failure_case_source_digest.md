# Failure Case Source Digest v0.2

This module has moved from placeholder to first-pass source coverage. It is
still not a full failure-case history. The current purpose is to anchor the
risk taxonomy in a small set of official or issuer sources and to prevent the
final report from treating stablecoin risk as only a normal-times operating
question.

## Registered Sources

- `FAILURE_001` - SEC Terraform Labs / Terra USD press release. This supports
  the Terra UST algorithmic-stablecoin classification and the May 2022 collapse
  anchor (`CLAIM_107`).
- `FAILURE_002` and `FAILURE_003` - Circle statements during and after the
  March 2023 USDC/SVB depeg. These support the US$3.3bn SVB exposure, roughly
  8% reserve share, and operational backlog-clearance claims (`CLAIM_108`,
  `CLAIM_109`).
- `FAILURE_004` and `FAILURE_005` - NYAG Tether / Bitfinex settlement sources.
  The press release supports the reserve-disclosure controversy claim
  (`CLAIM_110`); the settlement PDF should be extracted if the report needs
  page-level legal settlement language.
- `FAILURE_006` - Iron Finance post-mortem mirror. This supports a
  medium-confidence description of the IRON/TITAN bank-run mechanics
  (`CLAIM_111`). The original Medium/local archive should still be recovered
  before this becomes a high-confidence case study.

## Interpretation

The failure cases now support four distinct risk channels:

- Algorithmic / reflexive death spiral: Terra UST (`CLAIM_107`) and Iron
  Finance (`CLAIM_111`).
- Fiat-backed bank-deposit and custody concentration risk: USDC/SVB
  (`CLAIM_108`, `CLAIM_109`).
- Reserve-opacity and disclosure risk: Tether / Bitfinex NYAG settlement
  (`CLAIM_110`).
- Crypto-collateral liquidation and oracle/auction risk: still pending for
  Maker / DAI Black Thursday.

## Remaining Work

- Recover or register a primary MakerDAO / Maker Foundation source for Black
  Thursday.
- Add market-price timelines only if the project creates reproducible data
  exports for depeg depth/duration.
- Extract `FAILURE_005` settlement PDF sections before using detailed legal
  settlement language.
- Treat `FAILURE_006` as medium confidence until the original source is
  archived.
