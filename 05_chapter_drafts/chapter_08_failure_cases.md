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

Maker / DAI Black Thursday remains an open case-study target because a primary
event post-mortem source has not yet been registered.

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

### Crypto-Collateral, Oracle, And Auction Risk

This remains the least complete case-study area. DAI / USDS is already covered
in the issuer taxonomy as a crypto/RWA-collateralized protocol stablecoin, but
the project still needs a primary event source for Maker / DAI Black Thursday
before drafting a concrete failure case.

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
  Finance, and DAI are covered (`CLAIM_107`–`CLAIM_111`). Other notable
  incidents — Maker / DAI Black Thursday, the broader 2022 algorithmic-
  stablecoin cascade outside Terra, and exchange-driven depegs — are not yet
  extracted at primary-source level.
- **Some sources are URLs only.** `FAILURE_001`–`FAILURE_006` includes
  several `url_only` entries (Iron Finance post-mortem mirror,
  Tether/Bitfinex settlement PDF, Circle press releases). Page-level
  extraction is incomplete; treat the corresponding claims at the framing
  level rather than as quotable evidence.
- **No reproducible price/depeg timelines.** Quantitative depeg-duration and
  recovery-time claims are deferred until the data-export workflow described
  in chapter 7 produces a reproducible price series.
- **The Iron Finance source is a mirror.** `CLAIM_111` cites a mirror of the
  original Medium post-mortem; treat as medium confidence until a more
  reliable archive is located.
- **No regulator-action-vs-economic-loss separation.** The chapter currently
  treats regulatory settlements and economic losses jointly per case;
  cross-case comparison of legal action versus market impact is open.

For the full backlog see
`00_project_management/unresolved_open_questions.md`.

## 8.5 Remaining Work

- Register and extract a primary Maker / DAI Black Thursday event source.
- Extract `FAILURE_005` settlement PDF sections before writing detailed
  Tether settlement language.
- Add reproducible price/depeg timelines only after the data export workflow is
  in place.
- Recover the original Iron Finance post-mortem or triangulate it with a more
  reliable source before treating `CLAIM_111` as high confidence.
