# Chapter 9 — Conclusion

This chapter synthesises what the v0.3 evidence base supports, what it
supports only conditionally, and what remains unresolved. The structure
follows the framing established in chapter 1 and is intended to be read
alongside the cross-jurisdiction comparison table at the end of chapter
4 and the unresolved-questions file at
`00_project_management/unresolved_open_questions.md`.

## 9.1 What the evidence supports

Six findings are now claim-table anchored at high confidence.

### 9.1.1 Stablecoins are a reconfiguration of dollar liquidity, not a replacement of it

Major fiat-backed stablecoins (USDC, USDT, PYUSD, USDP, USDG, RLUSD,
FDUSD, GUSD) are issued against bank deposits, short-dated Treasury
securities, repurchase agreements, government money-market fund
shares, and similar regulated dollar instruments
(`CLAIM_026`–`CLAIM_034`, `CLAIM_075`, `CLAIM_078`). The four
jurisdictions that have written statute or quasi-statute on the
question (GENIUS Act in the United States, MiCA in the European
Union, the BoE proposed regime in the United Kingdom, NYDFS guidance
in New York) all enumerate a reserve list that overlaps with this
set. The stablecoin liability is therefore a tokenised wrapper around
the regulated dollar money-market and banking system, not an
independent monetary instrument. Any final-report conclusion about
"stablecoins as competition to banks" should be reframed as a
question about how the wrapper changes deposit substitution,
funding costs, payment system access, and reserve-asset market
demand.

### 9.1.2 Direct holder redemption rights are narrower than product-page language

For every fiat-backed stablecoin examined, the legally enforceable
right to redeem with the issuer is gated by counterparty contracts
that require KYC/AML completion, jurisdictional eligibility, an
account in good standing, and explicit carve-outs for prohibited
persons, sanctioned activity, and issuer-discretionary suspension
(`CLAIM_058` USDC, `CLAIM_060`–`CLAIM_061` USDT, `CLAIM_062`–`CLAIM_064`
FDUSD, `CLAIM_068` USDG EU retail, `CLAIM_073` Paxos family
including PYUSD and USDP, `CLAIM_077` GUSD via Gemini Trust,
`CLAIM_065`–`CLAIM_066` USDe Mint Users only). "Redeemable at par"
on a product page is not equivalent to a right available to any
lawful holder. The chapter-4 cross-jurisdiction comparison table
shows that this is also the structure under MiCA Article 39 ART
permanent redemption (subject to recovery-plan suspensions),
GENIUS Act Sec. 11 customer-priority insolvency rule, and NYDFS
T+2 lawful-holder redemption.

### 9.1.3 Attestation is not audit

Every issuer-side assurance report in the v0.3 archive is an
engagement under AICPA examination standards or ISAE 3000 / 3000R
review/assurance standards, not a full financial-statement audit
(`CLAIM_001` FDUSD ISAE 3000 limited assurance framing,
`CLAIM_080` USDP KPMG AICPA attestation, GUSD monthly examination
under AICPA via `GUSD_006`, Circle / Tether / Ripple / Paxos
transparency engagements). This is now also the statutory
expectation under the GENIUS Act, which mandates monthly
examination of reserve composition by a registered public
accounting firm with CEO/CFO certification under criminal-penalty
exposure (`CLAIM_085`), and under MiCA, which mandates a six-month
independent audit cadence for significant EMT issuers
(`CLAIM_097`). The terminology distinction is load-bearing: an
attestation does not opine on the issuer's financial statements,
internal controls, or going-concern status, only on the specific
assertion within the engagement scope at the engagement date.

### 9.1.4 Four jurisdictions now provide overlapping but distinct statutory baselines

The chapter-4 comparison table demonstrates that the U.S.
(GENIUS Act), EU (MiCA ART and EMT), UK (BoE systemic regime),
and New York (NYDFS guidance) regimes converge on a core
structure — eligible issuer, enumerated reserve composition,
redemption right, holder-yield prohibition, and insolvency
priority — but diverge materially on:

- **The mix of cash vs short-dated Treasuries vs central bank
  deposits.** GENIUS Act allows the full HQLA list including
  93-day Treasuries, repurchase agreements, and government MMF
  shares (`CLAIM_084`); MiCA ART requires at least 60% deposits
  in each referenced official currency under the EBA RTS
  (`CLAIM_094`); BoE 2025 requires at least 40% unremunerated
  central bank deposits plus up to 60% UK government debt
  (`CLAIM_090`). Only the BoE regime mandates a central-bank-
  deposit floor.
- **Holding limits.** Only the BoE 2025 consultation imposes
  quantitative holding limits (£20,000 retail per-coin and
  £10 million per business, `CLAIM_091`). GENIUS, MiCA, and
  NYDFS impose no analogous quantitative cap.
- **Insolvency / wind-down model.** GENIUS Act provides a
  customer-priority statutory rule in any insolvency proceeding
  (`CLAIM_087`); MiCA requires every ART issuer to maintain a
  redemption (wind-down) plan with temporary administrator
  designation triggered by competent-authority determination of
  inability to fulfil obligations (`CLAIM_096`); BoE proposes a
  recovery and administration plan plus shortfall reserve on
  statutory trust for coinholders (`CLAIM_089`); NYDFS imposes a
  T+2 lawful-holder redemption default with monthly CPA
  examination (`CLAIM_038`, `CLAIM_040`).
- **Significant-token thresholds.** GENIUS Act has no formal
  significant-token tier; MiCA ART and EMT both have EBA-
  supervised significant-token tiers triggered by at least
  three of the Article 43(1) criteria (`CLAIM_094`, `CLAIM_097`);
  BoE recognition by HMT on Bank recommendation under FSMA 2023
  functions as a different style of "significance" trigger.

The implication for a final report is that "stablecoin regulation"
should not be treated as a single regime. Cross-border issuers must
navigate four separate baselines, and equivalence between them is
not given.

### 9.1.5 Central-bank views frame stablecoin growth as a conditional channel

Federal Reserve and IMF analysis does not treat stablecoins as a
deterministic threat to banks. The conditional channels identified
are: source of inflow into stablecoins, reserve composition,
remuneration model, and substitutability with bank deposits
(`CLAIM_044`–`CLAIM_050`). The Fed IFDP 1334 model concludes that a
two-tiered banking model can support stablecoin issuance and
traditional credit creation simultaneously, while a narrow-bank
model increases disintermediation but strengthens the peg
(`CLAIM_048`). The IMF Making Stablecoins Stable model identifies
a welfare tradeoff between run-risk reduction (safe-asset backing)
and issuer profitability / issuance incentives (`CLAIM_049`). The
IMF Stablecoins and the Future of Payments event study finds that
listed incumbent payment firms lost approximately 18% (~US\$300bn)
of market value on U.S. pro-stablecoin policy news, which is
market-expectation evidence and not realised payment adoption
(`CLAIM_050`). The final-report framing should keep
market-expectation evidence and realised adoption separate.

### 9.1.6 Crypto / RWA-collateralised and synthetic-dollar stablecoins are different in kind

DAI / USDS (MakerDAO / Sky Protocol) is generated by
overcollateralisation of governance-approved collateral into
smart-contract vaults, with peg stability maintained through
automated liquidation auctions and governance-token dilution as
the residual loss absorber (`CLAIM_098`–`CLAIM_101`). The Sky
rebrand adds a yield-bearing wrapper (sUSDS), a SKY-backed-lending
risk capital token (stUSDS), and a 1:1 USDC ↔ USDS conversion
route, with sUSDS, stUSDS, and Sky Ecosystem Rewards unavailable
to U.S. users (`CLAIM_102`).

USDe (Ethena Labs) operates at 1:1 collateralisation maintained by
short perpetual futures hedges of approximately the same notional
as the spot backing, with backing assets held in Off-Exchange
Settlement custody and never transferred to the centralised
derivatives exchanges that host the hedge (`CLAIM_103`–`CLAIM_104`).
Monthly custodian attestations state that no backing assets reside
directly on exchange partners (`CLAIM_105`). A Reserve Fund of
stablecoins plus a smaller ETH allocation, controlled by a 4/10
multi-sig with keys held by Ethena Labs contributors and sized at
US\$46.6 million as of Q4 2024, functions as additional margin of
safety for negative-funding-rate periods and as a bidder of last
resort (`CLAIM_106`).

Neither category satisfies the reserve-composition rules of the
GENIUS Act, MiCA ART, MiCA EMT, or the BoE regime; neither category
has a single corporate issuer authorised under any of them. The
final-report framing therefore must not aggregate DAI / USDS or
USDe with fiat-backed payment stablecoins when estimating
stablecoin-driven Treasury demand, bank deposit substitution, or
payment-system implications.

## 9.2 What the evidence supports only conditionally

Two findings are central to the policy discussion but supportable
only under explicit conditions at the v0.3 cut-off.

### 9.2.1 USDPT as a payment-system reconfiguration

The Western Union digital-asset network announcement, Anchorage
Digital Bank as expected issuer per its OCC comment letter, and
the Fireblocks infrastructure release together support that USDPT
is being developed as a U.S. dollar payment token on Solana
intended to bridge digital and fiat workflows
(`CLAIM_051`–`CLAIM_053`). Beyond that, no claim that USDPT
replaces SWIFT, correspondent banking, Fedwire, CHIPS, or Western
Union's consumer-facing remittance rails is supportable, because
the product terms, reserve report, contract addresses, and
end-to-end customer-to-customer settlement workflow are not yet
in the public record. The chapter-6 discussion is therefore
deliberately conditional. If the missing documents become
available in v0.4, the framing should move from "planned product"
to "working system" only along the four-layer separation set out
in chapter 6 (customer remittance UX, agent network, internal
and agent settlement, bank or correspondent settlement).

### 9.2.2 Stablecoin payment demand as distinct from on-chain transfer volume

Raw on-chain transfer volume, market capitalisation, and supply
growth are not direct measures of realised payment usage. The
adjusted-volume datasets that would address this (Visa Onchain
Analytics, Artemis methodology beyond `CLAIM_054`, McKinsey /
Artemis joint analysis) are not in the v0.3 archive. The
chapter-7 discussion therefore relies on DeFiLlama supply data
for stablecoin-by-chain composition (`CLAIM_054`-style level) and
on the qualitative IMF and Fed framing for payment-adoption
expectations. The final report should not infer realised
payment-adoption levels from any aggregate volume figure without a
methodology note explaining the adjustment.

## 9.3 What remains unresolved

The full unresolved set is in
`00_project_management/unresolved_open_questions.md`. Five items
are load-bearing for any final-report conclusion and should be
flagged explicitly.

1. **USDPT product layer.** As discussed in section 9.2.1.
2. **Adjusted on-chain payment volume.** As discussed in section 9.2.2.
3. **CLARITY Act stablecoin-specific provisions.** The CLARITY Act
   is registered in the archive but its stablecoin-relevant
   sections have not been isolated from its market-structure
   provisions. The chapter-4 GENIUS / MiCA / BoE / NYDFS
   comparison should not be inferred to cover the CLARITY Act
   without that extraction.
4. **Foreign-issuer equivalence.** The GENIUS Act conditions
   foreign-payment-stablecoin-issuer distribution in the U.S. on
   technological capability and commitment to comply with lawful
   orders and Section 18 reciprocal arrangements
   (`CLAIM_083`). The research has not yet evaluated whether the
   BoE 2025 backing-asset rule, MiCA ART, or MiCA EMT regimes
   would qualify as "substantially similar" for this purpose.
5. **Taiwan-specific synthesis.** Central-bank claims at
   `CLAIM_044`–`CLAIM_050` are general. NTD stablecoin proposals,
   FX monitoring, digital dollarisation, deposit substitution,
   and monetary sovereignty implications for Taiwan have not
   yet been drawn from existing CBC and TWFRC sources.

## 9.4 Implications for the reading-group discussion

Three framing points are worth surfacing for the 2026-06-27
session.

1. **The right question is not "are stablecoins safe?" but "for
   which holder, against which counterparty, under which
   jurisdiction's regime?"** A USDC holder with a Circle Mint
   account in good standing, a USDT verified customer, a Gemini
   Customer holding GUSD, and a holder of bridged USDC on a chain
   without a Circle Mint footprint are exposed to different rights
   even though all of them hold a "stablecoin". The chapter-2
   matrix is the working tool for keeping these differences
   visible.

2. **Reserve composition rules are converging, but on different
   speeds.** The GENIUS Act enumerated list, the MiCA ART
   significant-token EBA RTS deposit floor, the BoE 40% central
   bank deposit floor, and the NYDFS permitted-asset list overlap
   on short-dated Treasuries and high-quality bank deposits but
   diverge on remuneration and on the role of central bank money.
   The next 12-24 months of rulemaking under each regime will
   determine whether the convergence holds. The chapter-4 table
   is intended to be re-read as those rules settle.

3. **Crypto / RWA-collateralised and synthetic-dollar instruments
   are now non-trivial in scale but are not the focus of the new
   statutes.** DAI / USDS and USDe are explicitly outside the
   permitted-payment-stablecoin-issuer perimeter of the GENIUS
   Act, are not authorised ART or EMT issuers under MiCA, and
   are not within the BoE recognised-systemic-stablecoin
   perimeter. The implication is not that they are unregulated
   in any operational sense — they remain subject to AML/CFT,
   securities, derivatives, and consumer-protection regimes in
   the jurisdictions where their counterparties operate — but
   that the new payment-stablecoin statutes treat them as out of
   scope. The reading-group discussion may want to consider
   whether the regulatory perimeter as drawn matches the
   economic perimeter the instruments occupy.

## 9.5 Suggested directions for v0.4

Subject to user scope decisions, the highest-leverage v0.4 work is:

- **CLARITY Act stablecoin-specific extraction** to close one of
  the remaining U.S. federal gaps.
- **Central-bank Taiwan-specific synthesis** using only existing
  CBC and TWFRC sources to draw the implications most directly
  relevant to the reading group's domestic policy interest.
- **MiCA EMT Articles 51 / 52 / 55 page-level extraction** to
  match the depth now available on the ART side.
- **USDPT product-layer extraction**, conditional on primary
  product terms, reserve report, contract addresses, and a
  workflow document becoming available; otherwise USDPT remains
  frozen.
- **Adjusted on-chain payment volume**, conditional on a
  reproducible export from Visa Onchain Analytics, Artemis, or a
  comparable source becoming available; otherwise the chapter-7
  discussion stays at the qualitative level.
- **Data-quality cleanup**: relabel or remove
  `DAI_USDS_003` (registered as "Sky Protocol technical
  whitepaper 2025" but in fact a Cardano Layer 2 data
  availability paper unrelated to the Maker / Sky stablecoin
  protocol).

The v0.3 cut-off has 106 claims, 130 registered sources, and a
chapter set that is internally consistent with both validation
scripts passing. The next deliverable is either a v0.3 final
report consolidation, a slide deck for the reading-group
session, or a v0.4 extraction pass on the items above. The
choice among these is a user decision.
