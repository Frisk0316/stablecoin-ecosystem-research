# Failure Case Source Digest v0.3.3

This module has moved from placeholder to first-pass source coverage. It is
still not a full failure-case history. The current purpose is to anchor the
risk taxonomy in a small set of official, issuer, analyst or community
sources and to prevent the final report from treating stablecoin risk as
only a normal-times operating question.

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
- `FAILURE_006` - Iron Finance post-mortem (canonical issuer Medium post,
  reachable again 2026-06-10; row repointed from the earlier mirror URL). This
  supports a medium-confidence description of the IRON/TITAN bank-run mechanics
  (`CLAIM_111`) and now also the protocol's own event timeline (`CLAIM_156`):
  on 16 June ~10:00 UTC TITAN fell ~US$65 to ~US$30 in two hours and recovered
  to ~US$52 within one hour while IRON briefly went off peg; a second ~15:00
  UTC sell-off triggered panic redemption, a spot-below-TWAP feedback loop, and
  the collapse toward zero into 17 June. This is the issuer narrative, not
  independent OHLCV; a local archive and a non-zero price series would still be
  needed for tick-level claims.
- `FAILURE_007` - Whiterabbit Medium post-mortem of MakerDAO Black Thursday
  2020-03-12. Supports the canonical numerical anchor for the cascade:
  1,462 of 3,994 collateral auctions closed at 100% discount, approximately
  62,892.93 ETH and US$8.325 million liquidated for zero DAI, and 5.67 million
  DAI of protocol undercollateralisation (`CLAIM_136`). Community
  post-mortem, not Maker Foundation primary.
- `FAILURE_008` - Glassnode Insights chronology of MakerDAO Black Thursday.
  Supports the ETH price decline, gas spike, and oracle-lag mechanics
  (`CLAIM_135`) and the governance response including Emergency-Shutdown
  veto, immediate auction parameter patches, and the 2020-03-19 MKR Debt
  Auction (`CLAIM_137`). Analyst chronology, not Maker Foundation primary.
- `CRYPTOCOMPARE_001` - CryptoCompare public `histohour` API cache for
  selected failure-case windows, exported under
  `09_data_exports/failure_case_timelines/`. It supports reproducible public
  hourly proxy timelines for USDC/SVB, Terra USTC and Maker DAI, while the
  public IRON/TITAN rows are zero-only and should not be treated as a usable
  Iron Finance price timeline (`CLAIM_148`, `CLAIM_149`).

## Interpretation

The failure cases now support five distinct risk channels:

- Algorithmic / reflexive death spiral: Terra UST (`CLAIM_107`) and Iron
  Finance (`CLAIM_111`, with the issuer event timeline in `CLAIM_156`).
- Fiat-backed bank-deposit and custody concentration risk: USDC/SVB
  (`CLAIM_108`, `CLAIM_109`).
- Reserve-opacity and disclosure risk: Tether / Bitfinex NYAG settlement
  (`CLAIM_110`).
- Crypto-collateral liquidation, oracle and auction-design risk: MakerDAO
  Black Thursday (`CLAIM_135`, `CLAIM_136`, `CLAIM_137`). The case is now
  anchored to two non-Maker-Foundation sources (Whiterabbit community
  post-mortem, Glassnode analyst chronology) and should be presented as a
  community / analyst-anchored case study, paired with current Maker / Sky
  protocol architecture (`CLAIM_098` to `CLAIM_102`) so the case is not read
  as describing current risk.
- Synthetic-dollar basis and funding risk: USDe mechanics in
  `CLAIM_103` to `CLAIM_106` cover the risk channel; no historical USDe
  failure episode is registered.
- Public hourly proxy price stress: `CLAIM_148` and `CLAIM_149` add a
  reproducible CryptoCompare export for selected event windows. This can be
  used for coarse timeline context for USDC/SVB, Terra USTC and Maker DAI,
  but not for tick-level duration, exchange-level troughs or a usable Iron
  Finance chronology.

## Remaining Work

- Register a Maker Foundation / governance forum primary source for Black
  Thursday if one is added to the archive; current anchors are community /
  analyst, which is sufficient for the case-study layer but should be upgraded
  if a primary source becomes available. Concrete retrieval target confirmed
  2026-06-10: the official `blog.makerdao.com` market-collapse post now 301
  redirects to `sky.money`, but the MakerDAO governance-forum post-mortem
  (published 2020-04-29, authored by "MakerMan") remains the best primary
  candidate and should be pulled via the Wayback Machine.
- Higher-quality market-price / depeg timelines remain open for exact
  duration, exchange-level trough and recovery-time claims. The public
  CryptoCompare export now covers USDC/SVB, Terra USTC and Maker DAI at
  hourly-proxy level, but Iron Finance market-price data remains blocked
  because public IRON/TITAN rows are zero-only. The Iron Finance event timeline
  is now captured qualitatively from the issuer post-mortem (`CLAIM_156`), but
  Kaiko, Coin Metrics, Amberdata or a paid CryptoCompare feed would still be
  needed for precise, independent trough/recovery timeline claims.
- Extract `FAILURE_005` settlement PDF sections before using detailed legal
  settlement language.
- `FAILURE_006` local HTML archived 2026-06-11 (`html_saved`); keep at medium
  confidence because it is the issuer's own narrative, not independent OHLCV.
