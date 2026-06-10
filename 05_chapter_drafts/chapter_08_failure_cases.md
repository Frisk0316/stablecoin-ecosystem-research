# Chapter 8 - Failure Cases and Risk Taxonomy

## 8.1 Status

This chapter is now a first-pass failure-case module rather than a pure
placeholder. It is still not a full historical case-study chapter. The goal at
this stage is to connect the report's risk taxonomy to a small set of
source-backed stress episodes and to show why normal-times stablecoin mechanics
are not enough.

Current case anchors:

- Terra UST / LUNA collapse (`CLAIM_107`)
- USDC / Silicon Valley Bank depeg (`CLAIM_108`, `CLAIM_109`)
- Tether / Bitfinex reserve-disclosure controversy (`CLAIM_110`)
- Iron Finance IRON/TITAN collapse (`CLAIM_111`, medium confidence)
- MakerDAO Black Thursday 2020-03-12 cascade (`CLAIM_135`, `CLAIM_136`,
  `CLAIM_137`, medium confidence — community and analyst sources, not
  Maker Foundation primary)
- Public hourly proxy timelines for USDC/SVB, Terra USTC and Maker DAI
  (`CLAIM_148`, `CLAIM_149`; `CRYPTOCOMPARE_001`)

The v0.4 failure-case data layer is deliberately bounded. CryptoCompare
public `histohour` exports provide a reproducible hourly OHLCV proxy for
selected event windows: USDC/SVB reaches a minimum hourly close of 0.9022
at 2023-03-11T07:00:00Z, Terra USTC reaches a minimum hourly close of
0.08716 at 2022-05-13T10:00:00Z, and the Maker DAI Black Thursday window
shows a maximum hourly high of 1.339 at 2020-03-12T10:00:00Z
(`CLAIM_149`). These figures are coarse public proxies, not tick-level or
exchange-level troughs, and the public IRON/TITAN rows are zero-only and
unusable for Iron Finance timeline claims (`CLAIM_148`).

## 8.2 Risk Taxonomy

### Reserve And Custody Risk

The risk that reserve assets lose value, become inaccessible, or are
encumbered, leaving the issuer unable to meet redemption demand. This is the
risk channel illustrated by the USDC / SVB episode: Circle stated that
US$3.3bn of USDC reserve deposits, approximately 8% of the total reserve, were
at Silicon Valley Bank during the March 2023 depeg period (`CLAIM_108`).

### Redemption And Operational Liquidity Risk

The risk that the contractual redemption process is narrower or slower than a
product-page "redeemable at par" statement implies. Circle's post-depeg update
that it had cleared substantially all minting and redemption backlogs
(`CLAIM_109`) belongs in this category: the stress was not only asset backing,
but also operational conversion between tokens and dollars.

### Reserve Opacity And Disclosure Risk

The risk that market participants cannot verify the issuer's reserve backing
or are misled by disclosures. NYAG's 2021 Tether / Bitfinex press release
states that its investigation found false statements about tether backing and
transfers between the companies to cover Bitfinex losses (`CLAIM_110`). This
supports the report's attestation-versus-audit guardrail.

### Algorithmic And Reflexive Stability Risk

The risk that the mechanism intended to maintain the peg becomes part of the
failure loop. The SEC described UST as an algorithmic stablecoin marketed as
maintaining its peg through interchangeability with LUNA, and identified the
Terra ecosystem collapse as occurring in May 2022 (`CLAIM_107`). Iron
Finance's post-mortem describes a related reflexive dynamic: liquidity
withdrawal and selling pushed IRON off peg and collapsed TITAN (`CLAIM_111`).
The post-mortem also gives the protocol's own event timeline (`CLAIM_156`): on
16 June 2021 around 10:00 UTC TITAN fell from about US$65 to about US$30 within
two hours and recovered to about US$52 within one hour; a second sell-off
around 15:00 UTC triggered panic IRON redemption and a spot-below-TWAP feedback
loop that collapsed TITAN toward zero into 17 June. This is the issuer
narrative, not independent tick-level price data.

### Crypto-Collateral, Oracle, And Auction Risk

DAI / USDS is covered in the issuer taxonomy as a crypto/RWA-collateralized
protocol stablecoin, and the v0.3.3 update adds MakerDAO Black Thursday
2020-03-12 as a case study anchored to community and analyst sources. The
ETH price fell approximately 43% from US$194 to US$111 within a single
trading day; Ethereum network gas prices spiked over 6x to approximately
80 Gwei with hourly peaks near 200 Gwei; and the Medianizer price oracle
lagged the market so the on-chain ETH price showed approximately US$166
while spot was near US$130, triggering mass undercollateralisation of
MakerDAO collateralised debt positions (`CLAIM_135`). Because keeper
scripts could not keep pace with congested gas, 1,462 of 3,994 collateral
auctions (approximately 36.6%) closed at a 100% discount; approximately
62,892.93 ETH and a cumulative US$8.325 million were liquidated for zero
DAI bids, and MakerDAO was left with an estimated 5.67 million DAI of
undercollateralised loss (`CLAIM_136`). In the days that followed the
community vetoed an Emergency Shutdown in favour of less drastic
measures, raised the maximum auction lot size from 50 ETH to 500 ETH and
extended auction duration, and on 2020-03-19 commenced an MKR Debt
Auction that minted new MKR for DAI to recapitalise the system
(`CLAIM_137`). Pair the case with the current Maker / Sky liquidation
architecture (`CLAIM_098` to `CLAIM_101`) so the historical event is not
read as a description of current risk: present-day Sky has additional
governance circuit-breakers and a different collateral mix that the 2020
architecture did not include.

The Black Thursday anchors are community (Whiterabbit) and analyst
(Glassnode) sources, not Maker Foundation primary; treat the case as
medium-confidence and flag the source quality explicitly in any slide or
report use.

### Synthetic-Dollar Basis And Funding Risk

USDe is not a fiat-backed payment stablecoin. Its risk channel is tied to
delta-neutral hedging, off-exchange custody, funding-rate dynamics, and reserve
fund governance (`CLAIM_103` to `CLAIM_106`). No historical USDe failure case
is registered in the current archive, so this chapter should discuss the
mechanism rather than imply a realized failure episode.

## 8.3 What Failure Cases Add To The Report

The failure-case layer sharpens five report guardrails:

- Stablecoin type matters. Terra UST and Iron Finance are not comparable to
  USDC or GUSD simply because all are called stablecoins.
- Direct redemption rights matter. A holder's ability to exit at par depends
  on customer status, jurisdiction, KYC/AML, and issuer terms.
- Reserve assets matter under stress. Bank deposits, Treasury bills, repo,
  MMF shares, crypto collateral, and derivative hedges fail in different ways.
- Attestation is not audit. Historical reserve-disclosure controversies make
  the assurance distinction central rather than cosmetic.
- On-chain liquidity is not the same as payment demand or par redemption.

## 8.4 Chapter limitations

The failure-case layer at v0.3 is a first-pass module, not a complete
incident catalogue. The following limitations apply:

- **Coverage is selective.** Terra UST, USDC/SVB, Tether/Bitfinex, Iron
  Finance, and DAI are covered (`CLAIM_107`–`CLAIM_111`); MakerDAO Black
  Thursday is now covered at community / analyst confidence
  (`CLAIM_135`–`CLAIM_137`). Other notable incidents — the broader 2022
  algorithmic-stablecoin cascade outside Terra, and exchange-driven depegs
  — are not yet extracted.
- **Some sources are URLs only.** `FAILURE_001`–`FAILURE_006` includes
  several `url_only` entries (Iron Finance post-mortem mirror,
  Tether/Bitfinex settlement PDF, Circle press releases). Page-level
  extraction is incomplete; treat the corresponding claims at the framing
  level rather than as quotable evidence.
- **Public hourly timelines are partial proxies.** `CRYPTOCOMPARE_001`
  provides reproducible hourly proxy data for USDC/SVB, Terra USTC and
  Maker DAI (`CLAIM_148`, `CLAIM_149`). It does not support exact
  tick-level depeg duration, exchange-level troughs or a usable Iron Finance
  IRON/TITAN timeline.
- **The Iron Finance source is issuer-narrative.** `FAILURE_006` was repointed
  on 2026-06-10 from the earlier mirror to the canonical issuer Medium
  post-mortem, which now also supports the event timeline (`CLAIM_156`). Treat
  as medium confidence: it is the protocol's own narrative, not independent
  tick-level OHLCV, and no local archive is saved yet.
- **No regulator-action-vs-economic-loss separation.** The chapter currently
  treats regulatory settlements and economic losses jointly per case;
  cross-case comparison of legal action versus market impact is open.

For the full backlog see
`00_project_management/unresolved_open_questions.md`.

## 8.5 Remaining Work

- Upgrade the Maker / DAI Black Thursday anchors from community / analyst
  (`FAILURE_007`, `FAILURE_008`) to a Maker Foundation or governance-forum
  primary source if one is added to the archive.
- Extract `FAILURE_005` settlement PDF sections before writing detailed
  Tether settlement language.
- Upgrade the public hourly CryptoCompare proxy into paid or exchange-level
  price/depeg timelines when Kaiko, Coin Metrics, Amberdata or similar data
  becomes available; exact duration/trough/recovery claims should wait for
  that higher-quality data. Iron Finance now has the issuer post-mortem
  timeline (`CLAIM_156`), but independent tick-level OHLCV remains the main
  missing piece because the public CryptoCompare IRON/TITAN export is zero-only.
- Save a local archive of the canonical Iron Finance post-mortem and
  triangulate it with an independent price series before treating the Iron
  Finance timeline as high confidence.
