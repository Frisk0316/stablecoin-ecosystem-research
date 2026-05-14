# Chapter 8 — Failure Cases and Risk Taxonomy

## v0.3 status note

This chapter is a deliberately open module at the v0.3 cut-off. The
**risk taxonomy** below is now anchored to claim-table evidence drawn
from issuer terms, attestation regimes, central-bank papers, and the
statutory regimes covered in chapters 4 and 5. The **specific case
studies** (Terra UST, Iron Finance, USDC SVB depeg, USDT historical
reserve controversy, DAI / USDS collateral-stress episodes,
synthetic-dollar peg breaks) remain source-light: the failure-case
matrix at `04_matrices/failure_case_matrix.csv` records each case
as "not included" or "external source needed". A v0.4 pass would
need to register dedicated event-analysis sources before
case-by-case prose can be drafted.

The implication for the reading-group deck is that the chapter
supports the **taxonomy slide** (Slide 44 in the v0.3 outline) and
the **guardrails slide** (Slide 45), but does not yet support
case-by-case slides. If detailed case studies are wanted for the
session, the reading-group hosts should either (a) commission a
focused v0.4 pass on three or four cases, or (b) present cases
from outside this research package with their own citations
clearly distinguished.

## 8.1 Risk taxonomy — anchored to v0.3 evidence

Eight risk categories are sustained throughout the report. Each
category below cites the v0.3 claim entries that establish the
mechanism, even where no specific historical episode is yet
documented in this archive.

### 8.1.1 Reserve and custody risk

The risk that the reserve assets backing a stablecoin lose value,
become inaccessible, or are encumbered, and that the issuer cannot
satisfy redemption requests at par. The reserve composition rules
under GENIUS Act Sec. 4(1)(A) (`CLAIM_084`), MiCA Article 36
(`CLAIM_069`), MiCA Article 54 (`CLAIM_043`), the BoE 2025
backing-asset rule (`CLAIM_090`), and the Paxos USD Stablecoin
Agreement (`CLAIM_075`) are designed precisely to address this
risk through enumerated permitted assets, maturity caps, and
segregation requirements. USDT's published exposure to physical
gold and Bitcoin (`CLAIM_029`) places it in a different
reserve-risk class from USDC, even though both are described as
"fiat-backed".

### 8.1.2 Redemption risk

The risk that the legally enforceable right to redeem with the
issuer is narrower than product-page language implies. v0.3
extractions consistently show direct redemption gated by customer
status (`CLAIM_058` USDC, `CLAIM_060`-`CLAIM_061` USDT,
`CLAIM_062`-`CLAIM_064` FDUSD, `CLAIM_065`-`CLAIM_066` USDe,
`CLAIM_073` Paxos family, `CLAIM_077` GUSD). MiCA Article 46
permits competent authorities to suspend redemption under the
recovery plan (`CLAIM_095`); BoE 2023 proposes either prohibiting
redemption fees or capping them at cost (`CLAIM_089`). The NYDFS
T+2 lawful-holder default (`CLAIM_038`) is the most generous
written redemption right in the v0.3 archive.

### 8.1.3 Bank-deposit risk

The risk that bank deposits backing the stablecoin become
unavailable through bank failure, regulatory action, or operational
disruption. This is the canonical channel illustrated by the
March 2023 USDC depeg episode, which is not yet source-anchored
in this archive. The Paxos USD Stablecoin Agreement (`CLAIM_075`)
expressly permits FDIC-insured deposit holdings in excess of FDIC
limits where Paxos believes funds must remain liquid, surfacing
the uninsured-deposit channel within the permitted reserve list.
GENIUS Act Sec. 4(1)(A)(ii) allows demand deposits at insured
depository institutions subject to safety-and-soundness limits
established by the FDIC and NCUA (`CLAIM_084`).

### 8.1.4 Market liquidity risk

The risk that secondary-market liquidity for the stablecoin
diverges from the par-value redemption commitment, particularly
under stress. MiCA Article 45 imposes a liquidity management
policy and stress-test cadence on significant ART issuers
(`CLAIM_094`); MiCA Article 46 recovery plans allow daily
redemption caps and redemption suspension (`CLAIM_095`); BoE 2023
proposes a shortfall reserve on statutory trust to mitigate
shortfall-induced run risk (`CLAIM_089`).

### 8.1.5 Oracle and collateral risk

The risk that oracle price feeds, governance-set risk parameters,
or collateral-quality changes produce liquidation cascades or
peg failures in crypto / RWA-collateralised stablecoins. The
MakerDAO MCD Protocol's reliance on three classes of external
actors — Keepers, Oracles, and Global Settlers (`CLAIM_101`) —
makes this a structural rather than incidental risk for
DAI / USDS. Automated Collateral Auctions with MKR (now SKY)
dilution as the residual loss absorber (`CLAIM_099`) is the
specific mechanism through which the risk is socialised.

### 8.1.6 Governance risk

The risk that governance decisions — collateral approvals,
Stability Fees, Liquidation Ratios, Emergency Shutdown triggers,
multi-sig key compromise — produce outcomes adverse to holders.
For DAI / USDS this is the MKR / SKY voting layer
(`CLAIM_098`, `CLAIM_101`). For USDe this is the 4-of-10 Reserve
Fund multi-sig with keys held by Ethena Labs contributors
(`CLAIM_106`). The BoE 2023 recovery-and-administration-plan
requirement (`CLAIM_089`) and MiCA Article 47 redemption plan
with temporary administrator designation (`CLAIM_096`) are
attempts to embed governance failure into a statutory wind-down
mechanism.

### 8.1.7 Basis and funding-rate risk

Specific to synthetic-dollar instruments. USDe's peg is
maintained by short perpetual hedges of approximately the same
notional as backing assets (`CLAIM_103`); the protocol earns
funding-rate revenue when funding is positive (BTC ~11% / ETH
~12.6% average in 2024 per Ethena documentation), but the
Reserve Fund is sized to fund periods of negative funding and
to act as bidder of last resort (`CLAIM_106`). The risk is that
a sustained negative-funding regime or a derivatives-exchange
disruption simultaneously reduces revenue and impairs the
hedge.

### 8.1.8 Regulatory risk

The risk that statutes, supervisory expectations, or
enforcement actions change the conditions under which an
issuer may operate or under which holders may redeem. v0.3
captures four such regimes (GENIUS Act, MiCA ART, MiCA EMT,
BoE systemic, NYDFS) that all impose distinct ongoing
obligations and significance triggers. The GENIUS Act 3-year
distribution transition (`CLAIM_083`) is the most immediate
forward-looking regulatory risk for non-permitted-issuer
tokens distributed to U.S. persons; the BoE 2025 holding
limits (`CLAIM_091`) are an example of a quantitative
regulatory cap with no GENIUS or MiCA analogue.

## 8.2 Failure-case matrix — current status

See `04_matrices/failure_case_matrix.csv` for the live status
of each candidate case. At v0.3, all five rows (Terra UST, Iron
Finance, USDC SVB depeg, USDT reserve controversy, DAI / USDS
collateral episodes) carry `current_source_coverage` of "not
included" or "partially covered", and `action_needed` of
"external source needed". This is the principal v0.3 limitation
in this chapter.

## 8.3 How failure cases have shaped this report's guardrails

The five non-negotiable rules in `AGENTS.md` map directly onto
historical failure modes:

- "Do not equate raw on-chain transfer volume with real payment
  volume" responds to the long-running misuse of supply and
  transfer figures to imply payment adoption.
- "Do not call an attestation an audit" responds to the
  transparency-reporting controversies that surrounded several
  early stablecoin issuers.
- "Do not describe SWIFT as a funds-settlement system" responds
  to the recurring misframing of SWIFT in cross-border
  remittance commentary.
- "Distinguish fiat-backed, crypto / RWA-collateralised,
  algorithmic, and synthetic-dollar stablecoins" responds
  directly to the 2022 Terra UST collapse and to the analytical
  errors that aggregated fundamentally different instruments.
- "Preserve open questions rather than guessing" responds to the
  general pattern in which industry narratives outrun the
  available primary evidence.

This is the v0.3 chapter-8 contribution: not a case-by-case
analysis, but a taxonomy of risks anchored to the rest of the
research, and an explicit acknowledgement that the case-study
layer is open work.

## 8.4 v0.4 candidates

Suggested case studies for v0.4 prioritisation, if the project
is taken further:

1. **March 2023 USDC SVB depeg** — supports section 8.1.3
   (bank-deposit risk) and the Paxos / USDC reserve-channel
   discussion in chapter 3. Primary sources: Circle public
   statements, SVB FDIC receivership documents, secondary-market
   price data.
2. **2022 Terra UST collapse** — supports section 8.1.4 (market
   liquidity) and the chapter-1 three-category guardrail.
   Primary sources: Terraform Labs filings, SEC complaints,
   Anchor Protocol documentation.
3. **Tether 2017-2021 reserve disclosure controversy** —
   supports section 8.1.1 (reserve and custody) and the
   attestation-versus-audit guardrail. Primary sources: NYAG
   settlement (2021), CFTC settlement (2021), Tether
   transparency timeline.
4. **DAI March 2020 "Black Thursday" auction failure** —
   supports section 8.1.5 (oracle and collateral). Primary
   sources: Maker post-mortem, on-chain auction data.
5. **A documented synthetic-dollar negative-funding episode** —
   supports section 8.1.7 (basis and funding); requires a
   public Ethena Reserve Fund drawdown event or a comparable
   episode.

The reading-group session can either treat these as known
external case studies presented from outside this package or
defer them to a v0.4 extraction pass.
