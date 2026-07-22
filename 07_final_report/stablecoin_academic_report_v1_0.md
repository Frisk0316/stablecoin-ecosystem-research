# Stablecoins as an On-chain Extension of the Dollar System

Issuer Design, Reserve Assets, Regulation, Payment Infrastructure, and
Systemic Risk

Status: **canonical academic report — v1.1 evidence update** (current main version)

Last updated: 2026-07-13

This is the canonical version of the final report for the 2026-06-27 reading
group delivery. Earlier versions are preserved for historical reference at
`07_final_report/archive/v0_1/` (initial structured memo) and
`07_final_report/archive/v0_2/` (interim claim-backed build); v0.1 and v0.2
are superseded and should not be cited as the project's current findings.

This report is claim-backed. Major assertions are anchored to
`03_claim_tables/claim_table_master.csv`. Source metadata is tracked in
`01_sources/source_registry.csv`. The 2026-07-13 P0 update is summarised in
`00_project_management/stablecoin_gap_update_2026-07-13.md`.

## Abstract

Stablecoins are often described either as crypto-native money or as a
technological substitute for banks and payment systems. The evidence in this
project supports a different interpretation: stablecoins are better understood
as an on-chain extension and reconfiguration of the dollar system. Fiat-backed
payment stablecoins package bank deposits, Treasury bills, repo/reverse repo,
money-market funds, custodians, compliance controls, issuer contracts, and
blockchain transferability into tokenized claims (`CLAIM_026`, `CLAIM_027`,
`CLAIM_034`, `CLAIM_075`, `CLAIM_078`, `CLAIM_084`). Their core differences
are not captured by the shared claim of one-dollar price stability. The
important questions are who issues the token, who regulates the issuer, who can
redeem directly, what assets sit behind the liability, where the reserves are
held, who receives the reserve income, which controls can freeze or suspend
transfers, and what rights a holder has in stress (`CLAIM_058`, `CLAIM_060`,
`CLAIM_062`, `CLAIM_065`, `CLAIM_068`, `CLAIM_073`, `CLAIM_077`,
`CLAIM_086`, `CLAIM_087`, `CLAIM_154`). This report therefore treats stablecoins as a
legal, balance-sheet, market-infrastructure, and data problem rather than only
a cryptoasset taxonomy problem.

## Executive Summary

The central thesis is that stablecoins do not sit outside the dollar system.
They tokenize claims and protocols that rearrange dollar liquidity across
regulated issuers, reserve assets, banking relationships, custodians,
blockchain settlement environments, and compliance systems. For fiat-backed
payment stablecoins, the token is only the visible interface. The economic
structure is a bundle of off-chain reserve assets and contractual rights linked
to on-chain transferability (`CLAIM_026`, `CLAIM_027`, `CLAIM_075`,
`CLAIM_078`, `CLAIM_084`).

The second finding is that stablecoin categories must be separated before
policy or investment conclusions are drawn. USDC, USDT, PYUSD, USDP, USDG,
RLUSD, FDUSD, and GUSD are issuer-led fiat-backed or reserve-backed
instruments. DAI / USDS depends on governance-approved collateral, vaults,
oracles, auctions, keepers, and governance-token loss absorption (`CLAIM_098`
to `CLAIM_102`). USDe is a synthetic-dollar instrument whose stability depends
on delta-neutral hedging, collateral, off-exchange custody, exchange venues,
funding rates, and a reserve fund rather than a simple bank-deposit/Treasury
reserve model (`CLAIM_103` to `CLAIM_106`). Algorithmic stablecoins such as
Terra UST introduce a separate reflexivity problem (`CLAIM_107`).

The third finding is that redemption rights are narrower than broad 1:1
product language often suggests. Direct redemption commonly requires an
account relationship, customer onboarding, KYC/AML, jurisdictional eligibility,
or an account in good standing (`CLAIM_058`, `CLAIM_060`, `CLAIM_062`,
`CLAIM_065`, `CLAIM_068`, `CLAIM_073`, `CLAIM_077`). Secondary-market holders
may hold a token that trades near one dollar while lacking a direct redemption
right against the issuer.

The fourth finding is that regulation is converging around reserve,
redemption, disclosure, and no-holder-yield principles, but the regimes remain
different in issuer perimeter, reserve-asset lists, redemption treatment,
central-bank deposit requirements, holding limits, insolvency priority, and
significant-token rules (`CLAIM_036` to `CLAIM_043`, `CLAIM_069` to
`CLAIM_071`, `CLAIM_082` to `CLAIM_097`).

The fifth finding is methodological. Supply, market capitalization, and raw
on-chain transfer volume cannot be treated as payment demand. The project has
DeFiLlama supply and chain-distribution exports (`CLAIM_055`) and Artemis
schema evidence (`CLAIM_054`), but adjusted payment-flow conclusions require a
reproducible pipeline that separates transfers, exchange movements, DeFi
activity, self-churn, and genuine payment use.

The sixth finding is about stress. Stablecoins reveal their structure under
pressure. USDC's SVB episode highlights bank-deposit and operational-liquidity
risk (`CLAIM_108`, `CLAIM_109`). Tether / Bitfinex NYAG sources highlight
reserve-opacity and disclosure risk (`CLAIM_110`). Iron Finance and Terra
illustrate reflexive collapse channels (`CLAIM_107`, `CLAIM_111`). DAI / USDS
and USDe require stress analysis through collateral, oracle, auction, basis,
funding, exchange, and custodian channels (`CLAIM_098` to `CLAIM_106`).

## 1. Introduction

The research question is not whether stablecoins are "crypto" or "money" in
the abstract. The practical question is how stablecoins reorganize the existing
dollar system: which legal entities create claims, which assets back those
claims, which holders can redeem, which intermediaries hold reserves, how
compliance powers operate, how payment and settlement workflows change, and
which failure channels emerge in stress.

This framing matters because the dominant public narrative often makes two
opposite mistakes. One mistake treats stablecoins as a clean replacement for
banks, Treasuries, money-market funds, custodians, SWIFT, correspondent
banking, Fedwire, CHIPS, or regulators. The current evidence does not support
that conclusion. Fiat-backed stablecoins rely on many of those institutions
and assets (`CLAIM_026`, `CLAIM_027`, `CLAIM_075`, `CLAIM_078`,
`CLAIM_084`). The other mistake treats all stablecoins as interchangeable
because they target one dollar. The evidence also rejects that view: fiat
reserves, crypto/RWA collateral, algorithmic mechanisms, and synthetic-dollar
hedging create different legal and market exposures (`CLAIM_098` to
`CLAIM_107`).

The report's thesis is therefore precise: stablecoins are tokenized claims and
protocols that extend dollar liquidity onto blockchains while preserving, and
sometimes intensifying, dependence on off-chain balance sheets, regulation,
safe assets, custodians, and payment infrastructure. They are not merely an
external substitute for the dollar system; they are one way the dollar system
is being rebuilt at its edges.

## 2. Taxonomy Of Stablecoins

The first analytical requirement is taxonomy. A stablecoin's shared price
target does not determine its risk profile. The relevant categories are
fiat-backed payment stablecoins, crypto/RWA-collateralized stablecoins,
synthetic-dollar instruments, and algorithmic stablecoins.

Fiat-backed payment stablecoins are issuer liabilities or issuer-administered
tokens backed by cash, bank deposits, Treasury bills, repo/reverse repo,
government money-market funds, or similar assets. The evidence base supports
this structure for USDC, GUSD, Paxos-family stablecoins, RLUSD, and FDUSD
through issuer reports, terms, or reserve-related claims (`CLAIM_026`,
`CLAIM_027`, `CLAIM_034`, `CLAIM_075`, `CLAIM_078`, `CLAIM_010`). USDT shares
the broad reserve-backed framing but has additional asset-mix and disclosure
issues because its detailed Q1 2026 table includes Treasury bills, reverse
repos, cash/bank deposits, precious metals, Bitcoin, public equities, other
investments, and secured loans (`CLAIM_002`, `CLAIM_003`, `CLAIM_152`).

Crypto/RWA-collateralized stablecoins such as DAI / USDS require a different
model. Their stability comes from collateral, vaults, liquidation mechanisms,
governance, oracles, keepers, and governance-token loss absorption rather than
a conventional issuer reserve account alone (`CLAIM_098` to `CLAIM_102`).
This makes them sensitive to collateral liquidity, price feeds, auction
design, governance decisions, and market stress.

Synthetic-dollar instruments such as USDe should not be merged with
fiat-backed payment stablecoins. USDe evidence describes delta-neutral hedging,
off-exchange custody, custodian attestations, and a reserve fund
(`CLAIM_103` to `CLAIM_106`). The stability problem is therefore not simply
whether a custodian holds Treasury bills. It is also whether hedges perform,
funding rates remain favorable, collateral can be accessed, exchanges remain
functional, and custodial arrangements withstand stress.

Algorithmic stablecoins represent the strongest warning against price-target
taxonomy. SEC evidence describes Terra USD as an algorithmic stablecoin that
was marketed as maintaining its peg through interchangeability with LUNA and
that collapsed in May 2022 (`CLAIM_107`). The relevant failure channel is
reflexivity: the mechanism that is supposed to stabilize the token can
accelerate collapse when confidence breaks.

## 3. Issuer And Redemption Structure

The core distinction among fiat-backed stablecoins is not only reserve quality.
It is also who has a direct claim against the issuer. A token can circulate
widely on-chain while issuer redemption remains limited to approved customers,
registered users, or eligible residents.

USDC illustrates the distinction. Circle reserve claims support bank deposits,
deposits at systemically important institutions, overnight reverse Treasury
repo, short Treasury bills, and Circle Reserve Fund exposure (`CLAIM_026`,
`CLAIM_027`). But Circle terms also establish that direct redemption requires
a Circle Mint account in good standing, and transferred holders can redeem
directly only if they are eligible for and registered with Circle Mint
(`CLAIM_058`). USDC holders are not entitled to reserve interest or returns
(`CLAIM_059`). Circle's USDC risk factors also add the control layer: Circle
may block addresses, freeze associated Circle-custodied USDC, and block
on-chain transfers to and from an address in extraordinary circumstances under
its blacklisting policy (`CLAIM_154`).

USDT shows a different structure. Tether's Q1 2026 materials are an ISAE 3000R
assurance report limited to point-in-time financial figures and reserve
statements, not full financial statements (`CLAIM_002`). Tether terms state
that issuance/redemption with Tether requires verified-customer status and
define restrictions around prohibited persons and jurisdictions (`CLAIM_060`,
`CLAIM_061`). The detailed Q1 2026 reserve-table export from `USDT_002`
records total reserves/assets of US$191.768bn, including US$117.036bn U.S.
Treasury bills, US$19.335bn overnight reverse repos, US$4.746bn term reverse
repos, US$107.0m cash/bank deposits, US$19.838bn precious metals,
US$6.624bn Bitcoin, US$3.408bn public equities, US$4.843bn other investments,
and US$15.830bn secured loans (`CLAIM_152`). The same report describes
Tether International as an El Salvador S.A. de C.V., FinCEN MSB, and
authorised Stablecoin Issuer / Digital Assets Service Provider under El
Salvador law, and lists 13 approved blockchains with several discontinued or
scheduled-to-end redemption obligations (`CLAIM_153`).

Paxos-family stablecoins also require careful separation of product identity
and holder rights. Paxos terms identify the issuer allocation across USDP,
PYUSD, USDG, and BUSD (`CLAIM_072`), restrict direct purchase/redemption to
Paxos customers (`CLAIM_073`), state that stablecoins are not designed to
create holder returns (`CLAIM_074`), enumerate reserve categories
(`CLAIM_075`), and give Paxos freeze/upgrade powers across holders
(`CLAIM_076`). USDG EU retail redemption is separately gated by EU residence,
supported chain, EU bank account, and KYC/AML (`CLAIM_068`).

GUSD terms distinguish Gemini Customers from non-Customers. Only Gemini
Customers may exchange dollars and GUSD at Gemini, while non-Customer holders
do not thereby create obligations from Gemini (`CLAIM_077`). GUSD reserve
accounts and redemption timing are claim-backed (`CLAIM_078`, `CLAIM_079`).

FDUSD terms add another form of gatekeeping. The evidence requires eligible
FD121 Account status for selling FDD/FDUSD to FD121, permits suspension or
limitation of buying/selling under stress, and excludes U.S. persons from
account eligibility (`CLAIM_062` to `CLAIM_064`).

USDe makes the direct-holder distinction explicit in a different way. Ethena
terms distinguish Mint Users and Holding Users, deny Holding Users a direct
redemption right with Ethena BVI, exclude U.S. users from Mint User status,
and state that USDe itself does not generate holder yield (`CLAIM_065`,
`CLAIM_066`). This is a reminder that secondary-market transferability and
issuer redemption are separate legal and operational layers.

## 4. Reserve Assets And Money Market Linkages

Stablecoin reserves create a bridge between blockchain transferability and
off-chain money markets. Bank deposits, Treasury bills, repo/reverse repo,
government money-market funds, and custodial relationships are not background
details. They are the assets and institutions that make a fiat-backed
stablecoin credible.

USDC, GUSD, Paxos-family stablecoins, RLUSD, and FDUSD each have evidence of
cash, bank deposit, Treasury, MMF, repo, or similar reserve channels
(`CLAIM_026`, `CLAIM_034`, `CLAIM_075`, `CLAIM_078`, `CLAIM_032`,
`CLAIM_010`). This means fiat-backed stablecoins can increase demand for
short-term safe assets while also concentrating operational dependence on
reserve managers, custodians, and banking partners.

USDT's reserve profile is not identical to those issuer models. Tether
materials support point-in-time assurance and reserve-surplus claims
(`CLAIM_002`, `CLAIM_003`), and the detailed reserve-table extraction adds
U.S. Treasury bills, overnight and term reverse repos, cash/bank deposits,
precious metals, Bitcoin, public equities, other investments, and secured
loans (`CLAIM_152`). The asset mix therefore matters for both liquidity
analysis and disclosure analysis.

Reserve-income allocation is central. A fiat-backed stablecoin may be marketed
as stable for the holder, but reserve returns generally accrue to the issuer or
its affiliates rather than to token holders. Circle, Paxos, GENIUS Act, MiCA
ART, and USDe evidence all support no-holder-yield or no-interest treatment
for the token itself (`CLAIM_059`, `CLAIM_066`, `CLAIM_071`, `CLAIM_074`,
`CLAIM_086`).

The policy implication is that stablecoins can transmit Treasury yield, bank
deposit, and money-market conditions into crypto markets and payment
applications while keeping the income and liquidity-management decisions in
the issuer or protocol layer. This is why stablecoins should be analyzed as
money-market-linked infrastructure rather than only as crypto payment tokens.

## 5. Regulatory Comparison

Stablecoin regulation is converging around a common vocabulary: issuer
perimeter, reserve assets, redemption, disclosure, examination or attestation,
holder-yield restrictions, recovery planning, and insolvency treatment. But
the actual legal designs differ.

NYDFS guidance applies to DFS-regulated U.S. dollar-backed stablecoins and
supports full backing, lawful-holder redemption, permitted reserve assets, and
CPA examination or attestation requirements (`CLAIM_036` to `CLAIM_040`).
This is a supervisory model built around regulated issuers and reserve
standards.

MiCA separates e-money tokens and asset-referenced tokens. EMT claims support
issuer eligibility, at-par redemption, no-interest treatment, investment-of-
funds rules, white-paper / marketing / liability duties, and recovery /
redemption plans (`CLAIM_042`, `CLAIM_043`, `CLAIM_122` to `CLAIM_128`).
ART claims support reserve-of-assets, permanent redemption, and no-interest
rules (`CLAIM_069` to `CLAIM_071`). Significant-token obligations, recovery
plans, and redemption plans add another layer of oversight (`CLAIM_094` to
`CLAIM_097`, `CLAIM_129`).

The GENIUS Act claims cover permitted issuer eligibility, a three-year
distribution transition, foreign-issuer access conditions, permitted reserve
assets, monthly reserve composition publication, registered-public-accounting-
firm examination, CEO/CFO certification with criminal-penalty exposure, a
holder-yield prohibition, customer-priority treatment in insolvency, and the
foreign-issuer exception / reciprocity path under Section 18 (`CLAIM_082` to
`CLAIM_087`, `CLAIM_126`). The statute is therefore important not only
because it recognizes payment stablecoins, but because it defines the reserve
and issuer perimeter in which they can circulate.

The Bank of England materials show a different design. The 2023 model favored
full central-bank deposit backing for systemic payment stablecoins, while the
2025 consultation permits a 40% unremunerated Bank of England deposit floor
plus up to 60% short-term UK government debt, with holding limits for
individuals and businesses (`CLAIM_088` to `CLAIM_091`). The 2025
consultation also treats wide cross-border use as jointly regulated in the
UK and subject to the home authority's regime, while foregrounding robust
legal claim and always-at-par fiat redemption (`CLAIM_130`, `CLAIM_131`).
The UK model
therefore treats systemic stablecoins as closer to payment-system and monetary
stability infrastructure than as a purely private issuer product.

The comparative table implied by these regimes should focus on reserve,
redemption, disclosure, yield, insolvency, and systemic treatment. The same
word "stablecoin" can conceal large differences in whether the legal system is
protecting the issuer, the customer, the payment system, monetary sovereignty,
or the broader financial system.

The foreign-issuer equivalence screen is now bounded rather than open-ended.
GENIUS Section 18 makes foreign market access a Treasury comparability,
Comptroller registration, U.S. liquidity, sanctions/AML, and lawful-order
question (`CLAIM_083`, `CLAIM_126`). BoE systemic stablecoin rules and MiCA
EMT rules are useful comparison cases, but neither should be described as
automatically equivalent to GENIUS absent a Section 18 determination and
reciprocal-arrangement analysis.

## 6. Central Bank And International Institution Views

Central banks and international institutions mostly do not analyze
stablecoins as isolated crypto products. They analyze them as instruments that
can affect the singleness of money, bank deposits, safe-asset demand, credit
intermediation, capital flows, payment competition, and regulatory perimeter.

BIS work supplies the conceptual benchmark. Stablecoins are evaluated against
singleness, elasticity, and integrity, and the BIS evidence treats them as
falling short as a backbone for the monetary system under those tests
(`BIS_001` in the source registry). This framing is useful because it asks
whether a privately issued token can preserve the public-good features of
money at scale.

Fed materials support conditional banking-transmission claims. Stablecoins may
reduce, recycle, or restructure deposits depending on the source of demand,
the assets converted into stablecoins, and the reserve allocation chosen by
issuers (`CLAIM_046`). They may affect bank credit through deposit volume,
deposit composition, funding costs, and liquidity management (`CLAIM_047`).
Fed IFDP work also distinguishes a two-tier model from a narrow-bank model
(`CLAIM_048`).

IMF work supports the run-risk and safe-asset-backing trade-off as well as the
issuer incentive problem (`CLAIM_049`). IMF payment-sector event-study
evidence supports a market-expectation claim that pro-stablecoin policy news
reduced listed incumbent payment-firm value by about 18%, roughly US$300bn
(`CLAIM_050`). This should not be overstated as realized adoption; it is
evidence about market expectations around payment-sector competition.

Taiwan is now a bounded claim-backed synthesis area rather than an open
placeholder. CBC materials frame stablecoins as tokenized private-sector money
without legal-tender status, while preserving central-bank money as the anchor
for singleness and payment finality (`CLAIM_112`, `CLAIM_113`). CBC identifies
USD-stablecoin dollarisation and FX-management channels (`CLAIM_114`) and
frames potential NTD stablecoins as tokenized electronic-payment stored value
requiring 100% reserves, no-yield controls, disclosure, and FSC-CBC rulemaking
coordination (`CLAIM_115`, `CLAIM_118`). CBC also expects current domestic
payment, M2, bank-credit and monetary-policy effects to be limited under
current market conditions (`CLAIM_116`, `CLAIM_117`).

The legal layer remains legislative-stage rather than enacted law. The record
now supports a timeline from FSC public timing statements and draft-law
commentary (`CLAIM_138`, `CLAIM_139`) through Executive Yuan approval /
Legislative Yuan submission on 2026-04-02 (`CLAIM_144`), 2026-06-03
committee-stage news (`CLAIM_145`), and an official Legislative Yuan docket
showing Finance Committee review entries through 2026-06-03 with gazette
production pending (`CLAIM_146`). This does not establish final statutory
requirements or FSC sub-rules.

## 7. Stablecoins In Payment And Settlement

Stablecoins can improve some payment workflows, but the analysis must separate
messaging, correspondent banking, clearing, settlement, liquidity management,
FX, customer onboarding, and last-mile cash-out. SWIFT should not be described
as a funds-settlement system absent source evidence; it is best treated as a
messaging/network layer within the broader correspondent-banking environment.

The cross-border retail payment baseline matters. Stablecoins may reduce some
costs or frictions by enabling transferable token balances, faster internal
settlement between platform participants, or new treasury/agent workflows.
That does not prove replacement of correspondent banking, Fedwire, CHIPS, bank
accounts, or consumer-facing remittance channels.

Western Union's USDPT evidence is valuable but still bounded. Western Union's
announcement and launch materials state that USDPT is built on Solana, issued
by Anchorage Digital Bank or Anchorage Digital Bank N.A., fully backed by U.S.
dollars, and intended for real-world payment systems (`CLAIM_051`,
`CLAIM_052`). Fireblocks material adds wallet, settlement, agent-settlement,
treasury/operations, and MT940/MT942 reporting context (`CLAIM_053`). The
2026-05-04 Western Union investor-relations launch release adds a Digital
Asset Network, Treasury and Agent Settlement use case, and separate Stable by
Western Union consumer-spend layer (`CLAIM_132` to `CLAIM_134`). Western
Union's product page adds broad reserve categories, 1:1 redeemability wording,
the official Solana contract address, and planned / coming-soon select-market
exchange, cash-out, card and receive-in-USDPT features (`CLAIM_140` to
`CLAIM_142`). Anchorage's transparency page previously identified the USDPT
reserve report slot as "Coming soon" (`CLAIM_143`); Deloitte's subsequently
published 2026-05-31 examination reports 1,500,372 redeemable USDPT,
US$1,603,106 reserves and US$102,734 surplus (`CLAIM_158`, `CLAIM_159`).
Anchorage Digital Bank's Covered Stablecoin Terms add an ADB-level legal
boundary: ADB-issued series are issued and redeemed directly only to Clients,
Non-Clients are not ADB customers under the terms, the reserve is described as
a Covered Stablecoin Reserve trust, ADB is sole issuer and sole obligor, brand
partners are service providers rather than obligors, par value applies only to
direct Client redemption with ADB, and ADB reserves legal/regulatory freeze or
restriction powers (`CLAIM_150`, `CLAIM_151`).

The current defensible conclusion is that Western Union is attempting to use
USDPT and related infrastructure to build a regulated digital-asset settlement
layer. It is not yet defensible to claim that USDPT replaces SWIFT,
correspondent banking, Fedwire, CHIPS, Western Union's consumer front end, or
all traditional remittance rails. USDPT-specific retail/user terms, fee
schedule, exact contract/key control implementation, retail/agent eligible-
redeemer scope beyond ADB Client status, agent balance-sheet treatment, and
end-to-end workflow documents remain blockers. ADB's general fee schedule has
no USDPT row, and issuer-level freeze/block/burn capability does not disclose
the exact USDPT program implementation (`CLAIM_160`, `CLAIM_161`,
`CLAIM_170`).

## 8. On-Chain Data And Payment Demand

On-chain data is essential but easy to misread. Stablecoin supply, market
capitalization, chain distribution, and raw transfer volume are not equivalent
to payment demand.

Artemis documentation supports the existence of stablecoin transfer volume,
transaction, supply, and address-level schemas with filter categories
(`CLAIM_054`). DeFiLlama API snapshots support supply and chain-distribution
analysis (`CLAIM_055`). The repository now includes reproducible DeFiLlama
exports under `09_data_exports`, but those exports should be treated as supply
and chain-distribution evidence rather than adjusted payment-flow evidence.
The repository also now includes a reproducible World Bank remittance-cost
benchmark export using WDI API indicator `SI.RMT.COST.IB.ZS`, with 17,556
country/region-year rows and a 104-row latest non-null benchmark file
(`CLAIM_147`). That benchmark is useful for off-chain cost context, not for
measuring stablecoin payment adoption.

The 2026-07-13 source pass adds current but carefully bounded snapshots. Visa
displayed US$100.1 trillion total and US$14.7 trillion adjusted transfer volume
over the prior 12 months; its filters still leave exchange, lending, mint/burn
and ramp activity, so the metric is not payments-only (`CLAIM_162`,
`CLAIM_163`). Artemis displayed US$229.0 billion average daily transfer volume
but does not label that headline as payment volume, and its CSV/API access is
account/product gated (`CLAIM_164`, `CLAIM_165`). Cambridge's locally archived
public JSON yields US$2.531847 trillion and 122,153,423 adjusted transfers for
June 2026 across six token/chain series (`CLAIM_166`). These sources do not
collectively provide a complete, anonymously downloadable, market-wide
adjusted stablecoin payments dataset (`CLAIM_167`).

The methodological problem is that raw transfers can include exchange
deposits/withdrawals, internal treasury operations, bridge movements,
liquidity-pool activity, DeFi collateral movements, smart-contract churn,
wash-like transfers, self-transfers, and payments. A credible payment-demand
chapter must define filters, document data transformations, retain source
dates, and preserve enough intermediate outputs to be reproduced.

The current report can therefore make a negative methodological claim with
confidence: raw on-chain transfer volume should not be equated with real
economic payment volume. Strong positive payment-demand claims require a
separate adjusted-data workflow.

## 9. Failure Cases And Stress Scenarios

Failure cases are not a side chapter. They reveal which layer of the
stablecoin system is actually bearing risk. The same one-dollar promise can
fail through reserve access, redemption queues, disclosure failure,
algorithmic reflexivity, collateral auctions, oracle failure, basis/funding
stress, exchange failure, or custodian disruption.

Terra UST anchors the algorithmic failure channel. SEC evidence describes UST
as an algorithmic stablecoin marketed as maintaining its peg through
interchangeability with LUNA, and records its May 2022 collapse
(`CLAIM_107`). The lesson is not merely that one algorithm failed. It is that
reflexive stabilization mechanisms can become destabilizing when the market
starts redeeming into the asset whose price is also collapsing.

Iron Finance provides another reflexive run case. The post-mortem evidence
describes the June 2021 IRON/TITAN event as a bank run after liquidity removal
and selling, with IRON moving off peg and TITAN collapsing (`CLAIM_111`). The
confidence level is medium because the registered source is a mirror; the case
should be triangulated before supporting high-confidence prose.

USDC's SVB depeg anchors a different risk channel. Circle stated that
US$3.3bn of the USDC reserve, about 8% of total reserve, was held at Silicon
Valley Bank and became fully available when banks opened, after which the
depeg closed (`CLAIM_108`). Circle also stated that by March 15, 2023
substantially all minting and redemption backlogs were cleared (`CLAIM_109`).
This is not an algorithmic death spiral. It is a bank-deposit, reserve-access,
and operational-liquidity stress case.

Tether / Bitfinex NYAG evidence anchors reserve-opacity and disclosure risk.
NYAG stated that its investigation found false statements about tether backing
and transfers between Bitfinex and Tether to cover losses, and that the
settlement required ending New York activity and monetary relief
(`CLAIM_110`). This case should be used carefully: it supports historical
disclosure and reserve-opacity analysis, not unsupported claims about current
reserve composition beyond the source.

DAI / USDS requires a collateral, oracle, liquidation, and governance stress
framework. Current claims support vaults, auctions, keepers, oracles,
governance, and loss-absorption structure (`CLAIM_098` to `CLAIM_102`), but
Maker Black Thursday now has community / analyst event anchors for the ETH
price shock, gas spike, oracle lag, zero-bid auction losses, governance
response and 2020-03-19 MKR Debt Auction (`CLAIM_135` to `CLAIM_137`). A
Maker Foundation or governance-forum primary source would still upgrade the
case-study confidence.

The repository now also includes public hourly failure-case proxy timelines
from CryptoCompare (`CRYPTOCOMPARE_001`). These exports support coarse
event-window context for USDC/SVB, Terra USTC and Maker DAI (`CLAIM_148`,
`CLAIM_149`): for example, the selected windows show a USDC minimum hourly
close of 0.9022 on 2023-03-11T07:00:00Z, a USTC minimum hourly close of
0.08716 on 2022-05-13T10:00:00Z, and a Maker DAI maximum hourly high of
1.339 on 2020-03-12T10:00:00Z. These figures should not be treated as
tick-level or exchange-level troughs, and the public IRON/TITAN rows are
zero-only and unusable for Iron Finance timeline claims.

USDe requires a synthetic-dollar stress framework. The relevant risks are not
limited to reserve backing. Evidence points to hedging, off-exchange custody,
custodian attestations, and reserve-fund design (`CLAIM_103` to
`CLAIM_106`). Stress scenarios should examine negative funding, hedge
unwindability, collateral access, exchange failure, custodian failure, and the
reserve fund's limits.

## 10. Conclusion

Stablecoins are best understood as tokenized claims on, or protocols linked
to, off-chain balance sheets and market infrastructure. Their innovation is
not that they abolish the dollar system. Their innovation is that they make
dollar claims programmable, transferable, and composable while keeping the
underlying dependence on issuers, reserves, banks, custodians, law, and
market-liquidity conditions.

The policy implications follow from that structure. Regulators should focus on
issuer perimeter, reserve quality, redemption rights, insolvency priority,
holder-yield treatment, custody, disclosure, operational resilience, payment
system access, and stress behavior. Investors and researchers should avoid
comparing stablecoins only by market capitalization or one-dollar price
targets. The relevant comparison is structural: who issues, who can redeem,
where reserves sit, who earns the yield, who can freeze or suspend, which
regime applies, and what fails under stress.

For Taiwan, the reading-group agenda should distinguish domestic NTD
stablecoins from offshore USD stablecoin usage. The evidence now supports a
source-grounded CBC framing: USD stablecoins raise digital-dollarisation and
FX-monitoring concerns, while NTD stablecoins are closer to tokenized
electronic-payment stored value with reserve, disclosure, no-yield and
rulemaking constraints (`CLAIM_112`-`CLAIM_118`).
The Virtual Asset Service Act passed third reading on 2026-06-30. As of
2026-07-13, official sources had not yet verified promulgation or effectiveness,
and final FSC/CBC stablecoin subordinate rules had not been issued
(`CLAIM_168`, `CLAIM_169`).

The next research priorities are clear. First, complete USDPT-specific
retail/user terms and fee schedule, retail/agent eligible redeemer scope beyond
ADB Client status, exact token-control and workflow extraction. Second, obtain
a genuinely payments-classified market-wide dataset if a provider publishes
one; current Visa, Artemis and Cambridge series are transfer or sampled/model
evidence. Third, register Taiwan promulgated text and final subordinate rules
when official sources publish them.
Fourth, upgrade failure-case timelines from public hourly proxies to
higher-quality or paid feeds where exact duration, trough and recovery claims
are required, and obtain a usable Iron Finance IRON/TITAN chronology. Fifth,
complete additional USDe stress evidence. Sixth, maintain the evidence portal
so every major paragraph can be audited back to its claim and source.

## Appendix A - Issuer Comparison Matrix

The authoritative working table is
`04_matrices/issuer_comparison_matrix.csv`. It compares stablecoin type,
issuer, jurisdiction, reserves or collateral, redemption rights, direct
redeemer, assurance/reporting, holder yield, freeze/blacklist/pause powers,
bank-deposit dependency, Treasury/repo/MMF dependency, primary use, risks,
sources, and confidence.

For the current report, the most important issuer-comparison anchors are USDC
reserve and Circle Mint redemption claims (`CLAIM_026`, `CLAIM_027`,
`CLAIM_058`, `CLAIM_059`, `CLAIM_154`), Tether reserve and verified-customer redemption
claims (`CLAIM_002`, `CLAIM_003`, `CLAIM_028`, `CLAIM_029`, `CLAIM_060`,
`CLAIM_061`), Paxos-family terms (`CLAIM_072` to `CLAIM_076`), GUSD terms
(`CLAIM_077` to `CLAIM_079`), FDUSD terms (`CLAIM_062` to `CLAIM_064`), DAI /
USDS protocol structure (`CLAIM_098` to `CLAIM_102`), and USDe mechanics
(`CLAIM_103` to `CLAIM_106`).

## Appendix B - Regulation Matrix

The authoritative working table is
`04_matrices/law_regulation_comparison_matrix.csv`. It compares frameworks by
jurisdiction, scope, issuer/activity rules, research use, source IDs, and
confidence.

The current report relies on NYDFS claims (`CLAIM_036` to `CLAIM_040`), MiCA
EMT/ART and significant-token claims (`CLAIM_042`, `CLAIM_043`,
`CLAIM_069` to `CLAIM_071`, `CLAIM_094` to `CLAIM_097`), GENIUS Act claims
(`CLAIM_082` to `CLAIM_087`), and Bank of England systemic stablecoin claims
(`CLAIM_088` to `CLAIM_091`).

## Appendix C - Methodology

This project uses a traceability workflow: source registry, source digest,
claim table, comparison matrix, chapter draft, and final report. No major
conclusion should appear in the final report unless it can be traced to
`03_claim_tables/claim_table_master.csv` and
`01_sources/source_registry.csv`.

The claim table fields are `claim_id`, `claim`, `source_id`,
`page_or_section`, `evidence`, `confidence`, and `notes`. High confidence is
reserved for direct primary-source support or strongly verified official
materials. Medium confidence is used when the source is useful but needs
triangulation, page-level extraction, or context. Low confidence is used for
background or weakly anchored material.

Attestation, assurance, and reserve reports are not described as audits unless
the source itself uses that term. SWIFT is not described as a funds-settlement
system. Raw on-chain transfer volume is not equated with real payment volume.
Fiat-backed, crypto/RWA-collateralized, algorithmic, and synthetic-dollar
stablecoins are kept analytically separate.

## Appendix D - Claim Table Excerpt

The full claim table is `03_claim_tables/claim_table_master.csv`. The most
important claim groups for this report are:

| Claim Group | Research Use |
| --- | --- |
| `CLAIM_026`-`CLAIM_034` | Reserve and issuer evidence for major fiat-backed stablecoins |
| `CLAIM_036`-`CLAIM_043` | NYDFS and MiCA baseline rules |
| `CLAIM_046`-`CLAIM_050` | Fed and IMF views on banking, credit, run risk, and payment competition |
| `CLAIM_051`-`CLAIM_053` | Western Union USDPT launch and payment-settlement infrastructure |
| `CLAIM_054`-`CLAIM_055` | On-chain data and DeFiLlama supply/chain evidence |
| `CLAIM_058`-`CLAIM_079` | Issuer terms, redemption eligibility, yield, controls, and reserve terms |
| `CLAIM_082`-`CLAIM_097` | GENIUS Act, BoE, ESMA/EBA, and MiCA significant-token rules |
| `CLAIM_098`-`CLAIM_106` | DAI / USDS and USDe structure |
| `CLAIM_107`-`CLAIM_111` | Failure cases and stress evidence |
| `CLAIM_112`-`CLAIM_118` | Taiwan CBC synthesis |
| `CLAIM_119`-`CLAIM_121` | CLARITY Act stablecoin-specific market-structure provisions |
| `CLAIM_122`-`CLAIM_125` | MiCA EMT white-paper, liability, marketing, and recovery/redemption rules |
| `CLAIM_126`-`CLAIM_131` | GENIUS foreign-issuer screen, MiCA EMT eligibility/no-interest/supervision, and BoE cross-border equivalence screen |
| `CLAIM_132`-`CLAIM_134` | Western Union Digital Asset Network, Treasury and Agent Settlement, and Stable by WU layer separation |
| `CLAIM_135`-`CLAIM_137` | Maker / DAI Black Thursday community and analyst event anchors |
| `CLAIM_138`-`CLAIM_139` | Taiwan VASP Act legislative-stage timing and draft-law commentary |
| `CLAIM_140`-`CLAIM_143` | USDPT product-page reserve categories, official Solana address, customer-feature direction, and Anchorage report-slot status |
| `CLAIM_144`-`CLAIM_146` | Taiwan Executive Yuan / Legislative Yuan Finance Committee / official docket legislative-stage update |
| `CLAIM_147` | World Bank remittance-cost benchmark data export |
| `CLAIM_148`-`CLAIM_149` | CryptoCompare public hourly failure-case proxy timeline export and selected summary metrics |
| `CLAIM_150`-`CLAIM_151` | Anchorage Digital Bank covered-stablecoin Client / Non-Client, reserve-trust, sole-obligor, brand-partner and legal-control terms |
| `CLAIM_152`-`CLAIM_153` | USDT Q1 2026 detailed reserve-table extraction and Tether International entity/blockchain boundary |
| `CLAIM_154` | Circle USDC risk-factor address-blocking, freezing and blacklisting-policy controls |

## Appendix E - Source Registry

The full source registry is `01_sources/source_registry.csv`. It records
stable `source_id` values, category, publisher, title, asset, year, document
type, local path, URL, status, priority, hash, and notes. Raw PDFs and HTML
files are not assumed to be publishable; local archive paths and URLs are
tracked so the evidence trail can be reconstructed.
