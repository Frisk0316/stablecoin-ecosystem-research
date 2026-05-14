# Chapter 1 — Stablecoins as an On-chain Extension of the Dollar System

## 1.1 Framing

This chapter sets out the analytical frame for the rest of the report. The
core claim is that **major fiat-backed stablecoins are not separate from the
dollar system**. They wrap bank deposits, Treasury bills, repurchase
agreements, money market fund shares, regulated custodians, and other
participants in the dollar money-market and banking system into
blockchain-transferable claims. A stablecoin issued by a chartered trust
company against U.S. Treasury bills and reverse repurchase agreements is
not a competing form of money in the sense that gold or a foreign currency
might be; it is a different ledger representation of the same underlying
dollar instruments.

This framing has three immediate consequences for the rest of the report.
First, the policy questions stablecoins raise are not new in kind. They
are the long-standing questions about narrow banking, payment-system
access, lender-of-last-resort coverage, money-market-fund regulation,
deposit insurance, custody, and capital adequacy, posed in a different
technical wrapper. The Bank for International Settlements and the
International Monetary Fund have framed the questions in exactly these
terms, focusing on singleness of money, elasticity of supply, integrity
of payments, financial stability, bank disintermediation, monetary
sovereignty, and short-term safe-asset market effects.

Second, the differences among stablecoin designs matter as much as the
common framing. A protocol-issued, collateral-backed stablecoin operating
through smart-contract vaults is not the same instrument as a
trust-issued, T-bill-backed stablecoin operating through a Federal
Reserve-regulated custodian, and neither is the same instrument as a
synthetic-dollar token whose peg is maintained by short perpetual
positions on centralised derivatives exchanges. Aggregating these into a
single "stablecoin" risk class — as some market-aggregator headlines do —
obscures the very channels through which each one transmits or fails to
transmit to the rest of the dollar system. The report therefore preserves
three product categories throughout (Section 1.3).

Third, the framing exposes a recurring confusion between product-page
language ("redeemable at par", "fully backed", "audited monthly") and
the legal and operational terms that actually condition holder rights.
Product pages describe the model; counterparty contracts and
attestation engagements describe the rights. The two routinely diverge.
The research is structured to keep them visibly separate (Section 1.4).

## 1.2 Why this question now

Three contemporaneous developments motivate the report's 2026 horizon.

First, the U.S. has, for the first time, enacted a federal payment
stablecoin statute (the Guiding and Establishing National Innovation for
U.S. Stablecoins Act, "GENIUS Act", Public Law 119-27), with a 3-year
distribution transition gate and an enumerated reserve composition list
(`CLAIM_082` through `CLAIM_087`). Implementation rulemaking by the OCC,
Treasury, and FinCEN is in progress.

Second, the European Union's Markets in Crypto-Assets Regulation
((EU) 2023/1114, "MiCA") is now in full force, separating
asset-referenced tokens (ARTs) from e-money tokens (EMTs) and adding
significant-token tiers supervised by the European Banking Authority,
with recovery and redemption plans now mandatory for all ART issuers
(`CLAIM_069` through `CLAIM_071`, `CLAIM_094` through `CLAIM_097`).

Third, the Bank of England has moved its proposed regime for systemic
sterling-denominated stablecoins from a 2023 discussion paper that
preferred 100% central bank deposit backing to a 2025 consultation
that revises the rule to at least 40% unremunerated central bank
deposits plus up to 60% short-term UK government debt, with a step-up
regime allowing up to 95% UK gilts at launch and quantitative holding
limits of £20,000 retail per coin and £10 million per business
(`CLAIM_088` through `CLAIM_091`). The U.S., EU, and UK regimes now
provide three distinct but overlapping statutory baselines that should
be compared at the article level rather than the headline level. The
chapter-4 cross-jurisdiction table assembles this comparison.

In parallel, a planned Western Union payment-stablecoin product
(USDPT, expected to be issued by Anchorage Digital Bank) was
announced in 2026 and is being positioned as part of a "Digital
Asset Network" connecting digital and fiat worlds. The research
treats USDPT as a deliberately conditional case: launch and
infrastructure evidence is documented, but product terms, reserve
report, contract addresses, and an end-to-end settlement workflow
are not yet in the archive. The chapter on USDPT (chapter 6)
therefore frames USDPT as a planned product rather than a working
system.

## 1.3 Three product categories that must be kept separate

The report sustains a three-way categorical distinction throughout the
issuer matrix, the chapter drafts, and the cross-jurisdiction
comparison table.

### 1.3.1 Fiat-backed payment stablecoins

Issued by a corporate or trust entity against bank deposits, short-dated
Treasury securities, repurchase agreements, government money-market
fund shares, and similar high-quality liquid assets. The set includes
USDC, USDT, PYUSD, USDP, USDG, RLUSD, FDUSD, and GUSD. Reserve
composition is disclosed under attestation rather than audit;
redemption rights are gated by counterparty contracts; product-page
language frequently overstates the scope of redemption available to
non-customer holders. The report's chapter 2 is organised around this
category.

### 1.3.2 Crypto / RWA-collateralised protocol stablecoins

Generated by user-deposited collateral into governance-controlled
smart-contract vaults, with peg stability maintained through
overcollateralisation, automated liquidation auctions, and
governance-token-backed dilution as the residual loss absorber. The
canonical instance is DAI (now USDS under the MakerDAO-to-Sky
Protocol rebrand), with MKR (now SKY) as the governance and
loss-absorbing token. There is no single corporate issuer authorised
under any of GENIUS, MiCA, NYDFS, or the BoE regime; the protocol is
not a permitted payment stablecoin under U.S. federal law as
enacted, and direct user-facing fiat redemption is not available
from the protocol itself. The chapter 2 discussion of DAI / USDS,
and the chapter 3 discussion of reserve channels, accordingly do
not place DAI / USDS in the same dollar money-market transmission
channel as fiat-backed stablecoins.

### 1.3.3 Synthetic-dollar instruments

Maintained at 1:1 collateralisation by delta-neutral hedging of
backing assets via short perpetual futures positions on centralised
derivatives exchanges, with the spot leg held in Off-Exchange
Settlement custody and never transferred to the exchange. The
canonical instance is USDe (Ethena Labs), with sUSDe as the
separate reward-accruing wrapper. USDe is not a fiat-backed
payment stablecoin and would not satisfy the GENIUS Act reserve
composition rule, the MiCA ART reserve-of-assets requirement, or
the BoE backing-asset rule on its own terms. Its risk profile
includes funding-rate reversal, off-exchange custodian default,
derivatives-exchange operational disruption, and governance / key
management of the Reserve Fund, none of which appear in the
fiat-backed category. Chapter 2 keeps USDe and sUSDe separate
throughout.

## 1.4 Distinctions that the report tries hard not to blur

Five recurring conflations appear in popular and industry writing on
stablecoins. The report flags each as a guardrail, preserved through
the chapter drafts, the claim table, and the source digests.

1. **Attestation versus audit.** A monthly attestation under AICPA
   or ISAE 3000 / 3000R standards on whether reserves equal or
   exceed liabilities is not a financial-statement audit. Several
   issuers issue both, but the attestation engagement is a separate
   product. Calling an attestation an "audit" inflates the assurance
   it provides. Where source language uses "audit", the report
   reproduces it; where source language uses "examination",
   "attestation", or "review", the report preserves the source
   language.
2. **Product-page redemption versus direct contractual right.**
   "Redeemable at par" on a product page is not the same as a
   legally enforceable right against the issuer. The right typically
   requires customer onboarding, KYC/AML completion, jurisdictional
   eligibility, and an account in good standing, with explicit
   carve-outs for prohibited persons, sanctioned activity, and
   issuer-discretionary suspension. The chapter-2 issuer-by-issuer
   discussion separates the two layers throughout.
3. **Raw on-chain transfer volume versus realised payment demand.**
   Transfer volume, market capitalisation, and supply growth are not
   direct measures of payment usage. They include exchange flows,
   bridge flows, arbitrage flows, and protocol-internal flows.
   Adjusted-volume datasets from Visa Onchain Analytics, Artemis,
   and similar aggregators attempt to subtract these categories, but
   the methodologies are not interchangeable and the underlying
   exports are not in this project's archive at v0.3.
4. **USDPT as a working remittance system versus USDPT as a
   planned product.** Without product terms, a reserve report, on-chain
   contract addresses, and an end-to-end customer-to-customer
   settlement workflow, no claim about USDPT replacing SWIFT,
   correspondent banking, Fedwire, CHIPS, or Western Union's
   consumer-facing remittance rails is supportable. The chapter-6
   discussion is therefore conditional.
5. **MiCA ART and MiCA EMT.** The two title-III and title-IV
   regimes have separate reserve, redemption, holder-yield, and
   significant-token rules; they apply to different products
   (asset-referenced tokens and e-money tokens) and to different
   types of issuer (authorised ART issuers under MiCA versus
   credit institutions or electronic money institutions under
   Article 48). The report keeps the two regimes separate at the
   claim, matrix, and chapter levels.

## 1.5 Roadmap

The remaining chapters develop the framing as follows.

- **Chapter 2 — Issuer comparison.** Issuer-by-issuer evidence
  on reserves, direct redemption rights, attestation regime,
  holder yield, freeze and blacklist powers, and primary use
  case across the three product categories. The issuer
  comparison matrix is the working table; the claim table is the
  traceability layer.
- **Chapter 3 — Reserve assets and dollar money markets.** The
  channels by which fiat-backed stablecoins are connected to
  short-term safe-asset markets, bank deposit funding, and
  money-market fund infrastructure. Crypto / RWA-collateralised
  and synthetic-dollar reserve channels are treated separately
  and are not aggregated with the fiat-backed channel.
- **Chapter 4 — Law and regulation.** GENIUS Act statutory
  anchors, NYDFS guidance, MiCA ART, MiCA EMT, significant-token
  regimes, recovery and redemption plans, BoE 2023 / 2025
  systemic stablecoin proposals, and ESMA supervisory practice
  under MiCA. The chapter ends with a cross-jurisdiction
  comparison table along six dimensions.
- **Chapter 5 — Central-bank views.** Federal Reserve, IMF,
  BIS, and ECB framing of stablecoin transmission to banking,
  payments, monetary policy, and safe-asset markets. Taiwan-
  specific implications are flagged as an open synthesis.
- **Chapter 6 — USDPT and cross-border payments.** Conditional
  treatment of the planned Western Union digital-asset network,
  with explicit separation between (a) consumer remittance UX,
  (b) the Western Union agent network, (c) internal and agent
  settlement, and (d) bank or correspondent settlement.
- **Chapter 7 — On-chain data and payment demand.** The
  difference between transfer volume and realised payment
  demand, the limitations of currently available
  adjusted-volume datasets, and what supply / chain-distribution
  data can and cannot say about stablecoin payment usage.
- **Chapter 8 — Failure cases.** Past depeg events, freezes,
  withdrawals, and operational disruptions used as risk
  reference points.
- **Chapter 9 — Conclusion.** Synthesis of what is supportable,
  what is conditional, and what remains unresolved at the v0.3
  cut-off.

## 1.6 Note on method and traceability

Every substantive claim in the chapter drafts and in the executive
summary is anchored to a row in `03_claim_tables/claim_table_master.csv`,
which records the `source_id`, `page_or_section`, an evidence
quotation, a confidence label, and methodology notes. The source
registry at `01_sources/source_registry.csv` records the primary
document for each `source_id`, including the local archive path. The
research relies on primary sources where possible: issuer terms,
attestation reports, statutory texts, central-bank discussion
papers, and supervisory guidance. Secondary sources (press releases,
explainer pages, dashboards) are used only where flagged in the
relevant claim's `confidence` and `notes` fields.

Where a question cannot be answered from the archive, the open
question is preserved in
`00_project_management/unresolved_open_questions.md` rather than
guessed. The v0.3 cut-off has 106 claims, 130 registered sources,
and a known set of frozen items (USDPT product terms, adjusted on-
chain volume, McKinsey / Artemis manual download) which are
explicitly carried as deferred for v0.4.
