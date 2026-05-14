# Chapter 2 - Issuer Comparison

Use `04_matrices/issuer_comparison_matrix.csv` as the main working table and
`03_claim_tables/claim_table_master.csv` as the traceability layer.

## Phase 2 extraction notes

The issuer comparison should separate three questions that are easy to blur:

1. What backs the token?
2. Who has a direct redemption right?
3. What kind of assurance, attestation, or report supports the reserve claim?

For USDC, Circle's transparency page now supports the reserve-category claim:
bank deposits, deposits at systemically important institutions, overnight
reverse Treasury repo, and sub-3-month Treasuries (`CLAIM_026`). Circle also
states USDC is redeemable 1:1 and backed by highly liquid cash and
cash-equivalent assets, with most reserve assets in the Circle Reserve Fund
(`CLAIM_027`). Circle terms now resolve the first layer of direct redeemer
scope: direct issuance/redemption requires a Circle Mint account in good
standing, and subsequent holders can redeem only if eligible for and registered
with Circle Mint (`CLAIM_058`). USDC holders are not entitled to reserve
interest or returns, and USDC itself does not generate holder yield
(`CLAIM_059`).

For USDT, the Q1 2026 reserve report remains the stronger source for assurance
scope and excess-reserve claims (`CLAIM_002`, `CLAIM_003`). Tether's May 1,
2026 release adds reserve-composition context: approximately US$141bn of
direct and indirect U.S. Treasury bill exposure, about US$20bn of physical
gold, and about US$7bn of Bitcoin (`CLAIM_028`, `CLAIM_029`). These reserve
composition items should be treated as medium-confidence issuer-release
claims until reconciled with the full report table.

Tether terms now narrow direct redemption. Users must be verified Tether
customers to cause tokens to be issued or redeemed, and the redemption right is
a personal contractual right (`CLAIM_060`). The same terms define prohibited
persons/jurisdictions, including U.S. persons except limited discretionary ECP
acceptance, Canadian/Singaporean persons, sanctioned persons, and prohibited
jurisdictions (`CLAIM_061`).

For the Paxos family (PYUSD, USDP, USDG), the unified Paxos USD Stablecoin
Agreement now resolves the issuer-entity, direct-redemption, holder-yield,
reserve-composition, and freeze-right questions at the contractual layer.
Paxos Trust Company, N.A. issues USDP, PYUSD, and BUSD (redemption-only);
Paxos Digital Singapore Pte. Ltd. and Paxos Issuance Europe Oy (PIE) jointly
issue USDG (`CLAIM_072`). Only Paxos Customers may purchase or redeem these
USD Stablecoins directly with Paxos; Non-Customer Token Holders defined in
the agreement have no direct purchase or redemption right (`CLAIM_073`).
Paxos USD Stablecoins are explicitly not designed to create returns, profits,
or other financial benefit for holders (`CLAIM_074`). Paxos Trust reserves
are restricted to FDIC-insured fiat deposits, U.S. government-guaranteed
debt instruments (direct or repurchase), and money-market funds composed of
such instruments; Paxos Digital and PIE follow analogous restrictions under
MAS and FIN-FSA frameworks (`CLAIM_075`). Paxos' freeze and upgrade right
applies aggregate-wise to all holders regardless of customer status,
extending the earlier USD Stablecoin freeze/seizure/forfeiture and
illegal/sanctioned-activity restriction claim (`CLAIM_056`, `CLAIM_076`).

For PYUSD specifically, the PayPal release continues to support Paxos
issuance and reserve basics (`CLAIM_004`) and PayPal's 70-market commerce
framing (`CLAIM_005`). PayPal crypto terms add the platform-eligibility
overlay and the PayPal Digital transition (`CLAIM_030`, `CLAIM_031`). The
relationship between PayPal Hub redemption and Paxos direct redemption is
better described as two layered redemption channels: PayPal Hub redemption
for retail US/territory users at the PayPal layer (`CLAIM_031`), and Paxos
direct redemption available only to Paxos Customers at the issuer layer
(`CLAIM_073`).

For USDP specifically, USDP attestation reports posted on or after
February 28, 2025 are by KPMG LLP under AICPA examination/attestation
standards (and are not financial statement audits); prior reports were by
WithumSmith+Brown, PC under the same AICPA framework (`CLAIM_080`). Paxos
also discloses on the USDP transparency page that it no longer proactively
provides a separate monthly USDP reserve composition report apart from the
KPMG attestation (`CLAIM_081`); this reclassifies the long-standing
"missing USDP reserve report" gap from "missing" to "discontinued by
issuer".

For USDG specifically, Paxos' EU redemption page continues to provide the
route-level retail criteria: EU residency, Ethereum/Solana USDG, an EU bank
account, and KYC/AML information (`CLAIM_068`).

For RLUSD, the attestation supports entity and NYDFS-derived reserve criteria
(`CLAIM_007`, `CLAIM_008`). The product page adds at-par redemption language,
reserve-asset categories, segregated reserve accounts, and BNY primary custody
information (`CLAIM_032`, `CLAIM_033`). Treat the product-page custody detail
as medium confidence until matched to reserve reports and terms.

For FDUSD, terms now support a direct-redeemer distinction. Holders may sell
FDD to FD121 only if eligible for and registered with a FD121 Account; holders
who are ineligible or not registered are not entitled to sell FDD to FD121
(`CLAIM_062`). FD121 may suspend, restrict, defer, or limit buying/selling in
reserve, liquidity, market-volatility, emergency, legal, or similar
circumstances (`CLAIM_063`). FD121 account terms also exclude U.S. individuals
or entities from account eligibility and permit termination for
misrepresentation (`CLAIM_064`).

For GUSD, the whitepaper and February 2026 reserve report support the core New
York trust company model (`CLAIM_011`, `CLAIM_012`). Gemini's product page
adds reserve-asset categories and platform-customer redemption language
(`CLAIM_034`, `CLAIM_035`). The Gemini Trust User Agreement now resolves the
platform-versus-lawful-holder question contractually: only Gemini Customers
may exchange U.S. dollars for Gemini Dollars or Gemini Dollars for U.S.
dollars at Gemini, and for non-Gemini-Customers, obtaining or using GUSD does
not create any relationship between the holder and Gemini and does not
subject Gemini to any obligation toward that holder (`CLAIM_077`). GUSD
reserves are held across three account categories — FDIC-insured bank
omnibus accounts, money market accounts holding MMFs invested in U.S.
government-issued or -guaranteed securities, and Treasury accounts holding
U.S. Treasury Obligations — managed to a 1:1 ratio with outstanding GUSD
(`CLAIM_078`). Gemini's contractual redemption commitment to Customer sell
Orders is "Timely", defined as no more than one full Business Day after the
Business Day on which Gemini receives the sell Order (`CLAIM_079`).

## Working comparison dimensions

- Issuer and legal entity
- Jurisdiction and regulator
- Reserve/collateral composition
- Direct redemption rights and eligible redeemers
- Assurance / attestation / reserve report status
- Yield or reward treatment
- Freeze, blacklist, and suspension powers
- Primary use case
- Key risk type

Important distinction: fiat-backed payment stablecoins,
crypto/RWA-collateralized stablecoins, and synthetic-dollar products should
not be treated as one risk class.

For USDe, this distinction is now claim-table backed. Ethena terms distinguish
whitelisted Mint Users from Holding Users: only Mint Users may create or redeem
directly with Ethena BVI, while Holding Users are not Ethena BVI customers and
do not have a direct redemption right (`CLAIM_065`). U.S. users are not
eligible to become Mint Users, and USDe itself does not generate interest or
return for holders (`CLAIM_066`). Ethena's overview frames USDe as a
delta-neutral synthetic dollar backed within the crypto ecosystem
(`CLAIM_067`).

The USDe peg-stability mechanism is now anchored at the mechanics level.
When a whitelisted Mint User deposits backing assets to mint USDe, Ethena
opens a corresponding short perpetual futures position on a derivatives
exchange of approximately the same notional value; this allows USDe to
operate at 1:1 collateralisation rather than the overcollateralisation
model used by DAI/USDS, because the price-change risk of the backing asset
is offset by an equal-and-opposite change in the value of the short hedge
(`CLAIM_103`). Backing assets are held in Off-Exchange Settlement
institutional-grade custody, and Ethena delegates but never transfers
custody of backing assets to centralised derivatives exchanges, mitigating
exchange-specific idiosyncratic counterparty risk while leaving off-exchange
custodian and derivatives-exchange operational risks intact (`CLAIM_104`).
Ethena publishes monthly custodian attestations validating existence,
control, and value of backing assets and explicitly states that none of
the backing assets reside directly on its exchange partners (`CLAIM_105`).
A separate Reserve Fund acts as an additional margin of safety to fund
periods of negative perpetual-funding-rate payments and as a bidder of
last resort for USDe; its composition is stablecoins (USDC, USDT) for
USD-margined contracts plus a smaller ETH allocation for ETH-margined
contracts, controlled by a 4/10 multi-sig with keys held by Ethena Labs
contributors and sized at US$46.6 million as of Q4 2024 (`CLAIM_106`).

For DAI/USDS the protocol mechanics now have direct claim support and the
asset should continue to be kept categorically separate from fiat-backed
payment stablecoins. The MakerDAO Multi-Collateral Dai (MCD) Protocol
generates Dai by allowing users to deposit governance-approved collateral
into Maker Vaults; every Dai in circulation is directly backed by excess
collateral, and MKR holders govern by voting on accepted collateral types
and risk parameters including Stability Fees and Liquidation Ratios
(`CLAIM_098`). Any Vault that falls below its Liquidation Ratio is
liquidated through automated Collateral Auctions; auction shortfalls are
covered by Protocol Surplus or MKR dilution, and surpluses return leftover
collateral to the Vault owner via a Reverse Collateral Auction
(`CLAIM_099`). The Dai Savings Rate (DSR) — implemented under the Sky
rebrand as the Sky Savings Rate paid through sUSDS — allows Dai/USDS
holders to earn savings by locking the stablecoin into the DSR/SSR
contract with no minimum and at-will withdrawal (`CLAIM_100`). The
protocol depends on three classes of external actors: Keepers, Oracles,
and Global Settlers / Emergency Oracles with unilateral Emergency Shutdown
authority (`CLAIM_101`). The Sky.money product page describes the
post-MakerDAO rebrand: USDS as the rebranded stablecoin, sUSDS as the
yield-bearing wrapper, stUSDS as SKY-backed-lending risk capital, SKY as
the governance token, and a 1:1 USDC ↔ USDS conversion route with zero
fees or slippage; sUSDS, stUSDS, and Sky Ecosystem Rewards are flagged as
"Currently unavailable in the US" (`CLAIM_102`).
