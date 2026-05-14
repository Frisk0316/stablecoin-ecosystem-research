# Issuer Source Digest - Phase 2/Deficiency Follow-up Draft

This digest summarizes issuer evidence that is already represented in
`03_claim_tables/claim_table_master.csv`. It is a working research digest, not
the final narrative report.

## Traceability updates

- Corrected source IDs in the claim table for USDT reserve report claims
  (`USDT_002`), PayPal PYUSD release claims (`PYUSD_003`), GUSD whitepaper
  claims (`GUSD_004`), and GUSD reserve-report claims (`GUSD_001`).
- Added `USDT_006` for Tether's official May 1, 2026 Q1 reserve-buffer news
  release. It now has a local HTML archive in the deficiency download package.
- Added claims `CLAIM_026` to `CLAIM_035` covering USDC reserves, Tether Q1
  reserve composition, PayPal crypto-hub eligibility, RLUSD product-page
  reserve statements, and GUSD product-page reserve/redemption statements.
- Added deficiency-source follow-up claims `CLAIM_051` to `CLAIM_053` for
  USDPT/UDSPT launch and infrastructure evidence, plus `CLAIM_056` and
  `CLAIM_057` for Paxos and Ripple restriction/freeze-style issuer terms.
- Added next-phase issuer-terms claims `CLAIM_058` to `CLAIM_068` covering
  USDC, USDT, FDUSD, USDe, and USDG direct redemption eligibility, user
  restrictions, suspension powers, and token-holder yield limitations.
- Added Paxos-family and Gemini Dollar terms claims `CLAIM_072` to `CLAIM_081`
  covering Paxos USD Stablecoin entity allocation, Customer-only direct
  purchase/redemption gating for USDP/PYUSD/USDG, the no-holder-yield rule for
  the Paxos family, the permitted reserve composition for Paxos Trust / Paxos
  Digital / PIE, the all-holders scope of the Paxos freeze/upgrade right,
  Gemini Customer-only GUSD creation/redemption, the three-account-type GUSD
  reserve structure, the one-Business-Day redemption-timing definition for
  GUSD, the KPMG AICPA attestation framing for USDP, and the issuer-announced
  discontinuation of the USDP monthly reserve composition report.

## USDC / Circle

Circle's transparency page supports two near-term research points. First, USDC
reserve categories include bank deposits, deposits at systemically important
institutions, overnight reverse Treasury repo, and sub-3-month Treasuries
(`CLAIM_026`). Second, Circle states that USDC is redeemable 1:1 for U.S.
dollars and backed 100% by highly liquid cash and cash-equivalent assets, with
the majority of the reserve in the Circle Reserve Fund (`CLAIM_027`).

Circle terms now narrow the direct redemption scope. USDC may be issued and
redeemed directly with Circle only through a Circle Mint account in good
standing, and transferred holders receive a redemption right only if they are
eligible for and register a Circle Mint account (`CLAIM_058`). Circle terms
also state that holders are not entitled to interest or returns earned on USDC
reserves, and USDC itself does not generate interest or return for holders
(`CLAIM_059`).

Remaining open question: Circle Mint eligibility and any region-specific terms
should still be mapped before making a universal direct-redeemer statement.

## USDT / Tether

The Q1 2026 reserve report should be described as an ISAE 3000R assurance
report limited to point-in-time financial figures, not as a full financial
statement audit (`CLAIM_002`). The same report supports the reserve surplus
claim of approximately US$8.232bn as of March 31, 2026 (`CLAIM_003`).

Tether's official May 1, 2026 release adds a higher-level reserve composition
snapshot: approximately US$141bn of direct and indirect U.S. Treasury bill
exposure (`CLAIM_028`), plus about US$20bn of physical gold and about US$7bn
of Bitcoin (`CLAIM_029`). These are issuer-release claims and should be used
with medium confidence unless confirmed against the detailed reserve report.

Tether terms now support direct redemption eligibility constraints. A user must
be a verified Tether customer to cause Tether Tokens to be issued or redeemed
by Tether, and the purchase/redemption right is a personal contractual right
(`CLAIM_060`). The terms also define Prohibited Persons to include U.S. Persons
except certain Eligible Contract Participants accepted by Tether in its
discretion, Canadian Persons, Singaporean Persons, sanctioned persons, and
persons in prohibited jurisdictions (`CLAIM_061`).

Open question: extract the full Q1 2026 reserve table from `USDT_002`,
including repo, secured loans, precious metals, Bitcoin, other investments,
public equities, and any maturity or custodian detail. Smart-contract-level
freeze/blacklist controls still need separate extraction.

## PYUSD / PayPal-Paxos

PayPal's release supports the issuer/basic-reserve claim: PYUSD is issued by
Paxos Trust Company, N.A. and backed by U.S. dollar deposits, U.S. Treasuries,
and similar cash equivalents (`CLAIM_004`). It also frames PYUSD availability
across 70 markets as faster/lower-cost global commerce infrastructure
(`CLAIM_005`).

PayPal crypto terms add two platform-level constraints. The terms state that
PayPal cryptocurrency services would transition from PayPal, Inc. to PayPal
Digital, Inc. on or after April 20, 2026 pending regulatory approval
(`CLAIM_030`). The same terms limit Consumer Cryptocurrencies Hub access to
U.S. or U.S. territory residents aged at least 18, and Business
Cryptocurrencies Hub access to businesses organized in, operating in, or
resident in the U.S. or its territories (`CLAIM_031`).

Paxos stablecoin terms now resolve the direct-redemption-rights question for
PYUSD at the contractual layer. The unified Paxos USD Stablecoin Agreement
identifies Paxos Trust Company, N.A. as the issuer of USDP, PYUSD, and BUSD
(redemption-only), and Paxos Digital Singapore and PIE as joint issuers of
USDG (`CLAIM_072`). Under that agreement, only Paxos Customers (registered,
verified Account holders) may purchase or redeem USD Stablecoins, including
PYUSD, directly with Paxos; Non-Customer Token Holders are defined in the
agreement but have no direct purchase or redemption right with Paxos
(`CLAIM_073`). The terms further state that Paxos USD Stablecoins are not
designed to create returns, profits, increases in value, or other financial
benefit for Customer or Non-Customer Token Holders (`CLAIM_074`).

Paxos Trust reserves backing PYUSD are restricted to three forms: fiat
currency in FDIC-insured bank accounts, direct or repo investments in U.S.
government-guaranteed debt instruments and money-market funds composed of
such instruments, and FDIC-insured deposits in excess of FDIC limits where
liquidity demands (`CLAIM_075`). The Paxos freeze and upgrade right is
explicitly aggregate and applies to all holders regardless of customer status,
extending the earlier restriction claim (`CLAIM_056`) with all-holders scope
(`CLAIM_076`).

Open questions: PayPal-platform-level eligibility and PayPal Digital
transition mechanics (`CLAIM_030`, `CLAIM_031`) remain orthogonal to Paxos
direct redemption; the relationship between PayPal Hub redemption and Paxos
direct redemption for end users still needs explicit mapping.

## USDG / Paxos Digital Singapore

USDG is issued by Paxos Digital Singapore Pte. Ltd., subject to MAS oversight,
and described as redeemable 1:1 for USD from Paxos (`CLAIM_006`). The USDG
whitepaper also supports an issuer claim that USDG can settle in minutes on
Ethereum or approved networks compared with potential days for fiat movements
(`CLAIM_024`).

The Paxos USD Stablecoin Agreement now resolves the issuer-and-direct-rights
layer for USDG. USDG is jointly issued by Paxos Digital Singapore Pte. Ltd.
and Paxos Issuance Europe Oy (PIE); Paxos Digital operates under a MAS Major
Payment Institution licence and PIE under a Finnish FIN-FSA Electronic Money
Institution licence (`CLAIM_072`). USD Stablecoins, including USDG, are
purchasable or redeemable directly with Paxos only by Paxos Customers; USDG
itself is not money or legal tender, except to the extent USDG constitutes
"money" under MiCA and the Second Electronic Money Directive (Paxos terms
Section 3.1.1, supporting `CLAIM_073`). Paxos USD Stablecoins are not designed
to create holder yield or returns (`CLAIM_074`), and the reserves at Paxos
Digital and PIE are restricted to bank-held fiat (with MAS-licensed or
A-/equivalent custodians for Paxos Digital, and credit institutions for PIE)
or U.S. government-guaranteed debt instruments and money-market funds composed
of such instruments (`CLAIM_075`). The all-holders freeze/upgrade right
(`CLAIM_076`) applies to USDG holders as well as Customers.

The EU redemption page continues to support the route-specific retail claim:
retail USDG redemptions through Paxos require EU residence, USDG on Ethereum
or Solana, an EU-based bank account, and KYC/AML information (`CLAIM_068`).
Remaining open question: non-EU institutional and direct-Paxos-Customer USDG
workflows beyond the EU retail route, and any USDG-specific reserve report
distinct from the unified USD Stablecoin reserves disclosure.

## RLUSD / Ripple

The March 2026 attestation supports the entity and regulatory framing:
Standard Custody & Trust Company, LLC is a New York limited purpose trust
company and Ripple Labs subsidiary (`CLAIM_007`), and the reserve criteria are
derived from NYDFS 2022 guidance (`CLAIM_008`).

The product page adds issuer-level reserve and custody detail: RLUSD is
supported one-to-one by U.S. dollar deposits, U.S. Treasuries, and cash
equivalents, and can be redeemed at par (`CLAIM_032`). It also states that
reserves are held in segregated accounts at depository institutions and
securities custodians, and that BNY was selected in July 2025 for primary
custody (`CLAIM_033`).

Open question: do not call reserve attestations "audits" unless the source
itself specifically supports that term for the relevant engagement. Product
terms now support a restrictions claim: Ripple may suspend or terminate access
to RLUSD-related services for prohibited uses/businesses, with possible loss of
ability to redeem RLUSD with Ripple (`CLAIM_057`). Direct redeemer eligibility
and any contract-level freeze/blacklist mechanism still need separate
extraction.

## FDUSD / First Digital

FDUSD's March 2026 attestation is a limited assurance engagement under ISAE
3000 Revised, not reasonable assurance (`CLAIM_009`). The reserve accounts
report identifies FD121 (BVI) Limited, multi-chain FDUSD supply, and reserve
accounts at least equal to outstanding supply (`CLAIM_010`).

FDUSD terms now support direct-rights and suspension claims. The First Digital
terms (`FDUSD_003`, URL path `/legal/fdd-terms`) use the contractual short-name
`FDD` for the FDUSD token; the two names refer to the same asset and are used
interchangeably below to match the source. Holders may sell FDD to FD121 only
if they are eligible for and register a FD121 Account; holders who are not
eligible or do not register are not entitled to sell FDD to FD121
(`CLAIM_062`). FD121 may cancel, suspend, restrict, defer, or limit
buying and selling in specified reserve, liquidity, market-volatility,
exchange-disruption, emergency, legal, or similar circumstances (`CLAIM_063`).
The FD121 account agreement also excludes U.S. individuals/entities from
account eligibility and allows termination if representations become untrue or
misleading (`CLAIM_064`).

Remaining open question: the legal relationship among the BVI issuer, Hong
Kong trust/custody arrangements, and reserve-account banks still needs
source-by-source mapping.

## GUSD / Gemini

The GUSD whitepaper supports the basic product mechanics: GUSD is a New York
trust company-issued, 1:1 USD-pegged ERC-20 token created and redeemed on the
Gemini platform (`CLAIM_011`). The February 2026 reserve report supports
monthly compliance with NYDFS stablecoin guidance and full reserve backing
(`CLAIM_012`).

Gemini's product page adds reserve-composition and platform-redemption
details. Each GUSD corresponds to U.S. dollars held as deposits at
FDIC-insured banks, money market funds invested only in U.S. Treasury
obligations, or U.S. Treasury obligations (`CLAIM_034`). Gemini also states
that Gemini customers can redeem 1 GUSD for US$1 on Gemini at any time
(`CLAIM_035`).

The Gemini Trust User Agreement (`GUSD_006`) now resolves the
platform-versus-lawful-holder distinction at the contractual layer. Only
Gemini Customers may exchange U.S. dollars for Gemini Dollars or Gemini
Dollars for U.S. dollars at Gemini; for non-Gemini-Customers, obtaining or
using GUSD does not create any relationship between the holder and Gemini and
does not subject Gemini to any obligations toward that holder (`CLAIM_077`).
GUSD reserves are explicitly held across three account categories: Gemini
Dollar Omnibus Accounts at FDIC-insured banks, Gemini Dollar Money Market
Accounts holding MMFs invested in U.S.-government-issued or -guaranteed
securities, and Gemini Dollar Treasury Accounts holding U.S. Treasury
Obligations; Gemini manages the reserve to a 1:1 ratio with outstanding GUSD
(`CLAIM_078`). The same agreement defines Gemini's redemption-timing
commitment to Customer sell Orders as "Timely", meaning no more than one full
Business Day after the Business Day on which Gemini receives the sell Order
(`CLAIM_079`).

The Gemini Dollar section is framed as an examination/attestation regime: a
registered independent public accounting firm examines and attests under
AICPA standards, on a monthly basis, whether reserve assets equal or exceed
outstanding GUSD; this is consistent with the broader research guardrail that
such reports should not be called full audits.

## USDP / Pax Dollar

The Paxos USD Stablecoin Agreement now covers USDP at the contractual layer.
USDP is issued by Paxos Trust Company, N.A. (`CLAIM_072`); only Paxos
Customers may purchase or redeem USDP directly with Paxos and Non-Customer
Token Holders have no direct redemption right (`CLAIM_073`); USDP is not
designed to create holder yield or returns (`CLAIM_074`); USDP reserves are
restricted to FDIC-insured fiat deposits, U.S.-government-guaranteed debt
instruments (direct or repo), and money-market funds composed of such
instruments (`CLAIM_075`); and the Paxos freeze/upgrade right applies to all
USDP holders regardless of customer status (`CLAIM_076`).

The USDP transparency page resolves the long-standing absence of a USDP
monthly reserve composition report in two ways. First, USDP attestations
posted on or after February 28, 2025 are issued by KPMG LLP under AICPA
attestation standards and are examinations/attestations, not financial
statement audits; prior reports were issued by WithumSmith+Brown, PC under the
same AICPA framework (`CLAIM_080`). Second, the same page states that Paxos
no longer proactively provides monthly reserve composition reports for USDP
separately from these attestation reports (`CLAIM_081`). The earlier
deficiency item "USDP monthly reserve report PDF is absent" should therefore
be reclassified from "missing" to "discontinued by issuer" in the unresolved
questions list.

## DAI / USDS / Maker-Sky

DAI/USDS should not be grouped with fiat-backed payment stablecoins. It is a
crypto/RWA-collateralised protocol stablecoin system with governance, oracle,
liquidation, and collateral-module risks now anchored in the claim table.

The MakerDAO Multi-Collateral Dai (MCD) Protocol generates Dai by allowing
users to deposit governance-approved collateral assets into Maker Vaults;
every Dai in circulation is directly backed by excess collateral, and MKR
holders vote on the set of accepted collateral types and risk parameters
including Stability Fees and Liquidation Ratios (`CLAIM_098`). When a
Vault falls below its governance-set Liquidation Ratio it is automatically
liquidated through Collateral Auctions; auction shortfalls are converted
into Protocol Surplus or covered by MKR dilution, while auction surpluses
return leftover collateral to the Vault owner via a Reverse Collateral
Auction (`CLAIM_099`). The Dai Savings Rate (DSR) is a global parameter
allowing any Dai holder to earn savings by locking Dai into the DSR
contract with no minimum and at-will withdrawal; this savings module is now
implemented under the Sky rebrand as the Sky Savings Rate paid through
sUSDS (`CLAIM_100`). The protocol depends on three classes of external
actors: Keepers (incentivised market actors), Oracles (governance-permitted
price feeds), and Global Settlers / Emergency Oracles with unilateral
Emergency Shutdown authority (`CLAIM_101`).

The Sky.money product page (Sky Protocol's post-MakerDAO rebrand) describes
USDS as the rebranded stablecoin, sUSDS as the yield-bearing wrapper
accruing the Sky Savings Rate, stUSDS as SKY-backed-lending risk capital,
and SKY as the governance token; it advertises 1:1 USDC ↔ USDS conversion
in both directions with zero fees or slippage (a PSM-style fiat-backed
on-ramp/off-ramp). The sUSDS, stUSDS, and Sky Ecosystem Rewards entry
points are flagged as "Currently unavailable in the US" (`CLAIM_102`).

Source-quality note: `DAI_USDS_003` (registered as "Sky Protocol technical
whitepaper 2025") is in fact a Cardano Layer 2 data-availability paper that
shares the "Sky" name but is unrelated to the MakerDAO/Sky stablecoin
protocol. It is a name collision and has not been used to support any
claim; the registry row should be flagged for relabelling or removal.

Open question (v0.4 candidate): the RWA Vaults inventory, Peg Stability
Module contract-level mechanics, and the precise relationship between
USDS, sUSDS, stUSDS and the legacy DAI token are not yet extracted at
contract or governance-vote level; the chapter-2 narrative should remain
descriptive on the rebrand until that mapping is anchored to source.

## USDe / Ethena

USDe should be treated as a synthetic-dollar / derivatives-backed stable asset,
not a fiat-backed payment stablecoin. Ethena terms distinguish Mint Users from
Holding Users: only whitelisted Mint Users that complete KYC/AML and onboarding
may create or redeem USDe directly with Ethena BVI; Holding Users are not
Ethena BVI customers and do not have a direct redemption right (`CLAIM_065`).
Users in the United States are not eligible to become Mint Users, and USDe
itself does not generate interest or return for holders (`CLAIM_066`). The
Ethena overview describes USDe as a delta-neutral synthetic dollar backed
within the crypto ecosystem, with whitelisted direct mint/redeem access and
external liquidity-pool acquisition for other users (`CLAIM_067`).

USDe risk extraction is now claim-table anchored. Ethena's USDe is a
synthetic-dollar stablecoin whose peg is maintained by delta-neutral
hedging: when a whitelisted Mint User deposits backing assets, Ethena
opens a corresponding short perpetual futures position on a derivatives
exchange of approximately the same notional value, allowing USDe to
operate at 1:1 collateralisation (not overcollateralisation) because the
price-change risk of the backing asset is offset by the short hedge
(`CLAIM_103`). Backing assets are held in Off-Exchange Settlement
institutional-grade custody and Ethena delegates but never transfers
custody to centralised derivatives exchanges; this Off-Exchange Custody
arrangement mitigates exchange-specific idiosyncratic counterparty risk
but does not eliminate off-exchange custodian default risk or
derivatives-exchange operational disruption risk affecting hedge execution
(`CLAIM_104`). Ethena publishes monthly custodian attestations validating
existence, control, and value of USDe backing assets and explicitly states
that none of the backing assets reside directly on its exchange partners
(`CLAIM_105`). The USDe Reserve Fund acts as an additional margin of
safety to fund periods of negative perpetual-funding-rate payments and as
a bidder of last resort for USDe in open markets; its composition is
stablecoins (USDC, USDT) for USD-margined contracts plus a smaller ETH
allocation for ETH-margined contracts; it is controlled by a 4/10
multi-sig with keys held by Ethena Labs contributors, capitalised from
protocol revenue and private placement investors, with a stated size of
US$46.6 million as of Q4 2024 (`CLAIM_106`).

Remaining open question: live exchange-by-exchange exposure breakdown,
basis trade scenario analysis, and the relationship between sUSDe APY
(19% average in 2024 per Ethena documentation) and the sustainability of
funding-rate revenue under sustained negative-funding regimes. USDe must
also continue to be kept separate from sUSDe in narrative — only sUSDe is
the reward-accruing token.

## USDPT / UDSPT / Western Union-Anchorage

The current evidence is now stronger for product existence and launch framing,
but still incomplete for legal terms and operational workflow. Anchorage's
comment letter states that Anchorage Digital Bank issues USAT, USDGO, and
USDtb, and expects to begin issuing UDSPT with Western Union as brand partner
(`CLAIM_023`). Western Union's October 28, 2025 announcement states that USDPT
would be built on Solana, issued by Anchorage Digital Bank, and supported by a
Digital Asset Network (`CLAIM_051`). Western Union's March 31, 2026 launch
release states that USDPT is a USD-denominated payment stablecoin, fully backed
by U.S. dollars, issued by Anchorage Digital Bank N.A., and built on Solana
(`CLAIM_052`). Fireblocks also describes infrastructure roles for agent
settlement, wallet infrastructure, compliance tooling, and MT940/MT942
translation (`CLAIM_053`).

Product terms, reserve reports, contract addresses, direct redemption rights,
and end-to-end settlement workflow documents are still missing.

Open question: do not infer that Western Union agents will directly handle
stablecoin retail cash-out or that USDPT replaces correspondent banking until
product documentation supports the actual workflow.
