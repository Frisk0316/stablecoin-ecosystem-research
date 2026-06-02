# Stablecoin Ecosystem Research Report v0.2

Status: claim-backed report build

Last updated: 2026-05-15

This v0.2 report upgrades the original v0.1 memo into chapter form. It does
not rewrite the research database. It summarizes the current claim table
(`03_claim_tables/claim_table_master.csv`) and preserves open questions where
the archive is still incomplete.

## Executive Summary

Stablecoins are best understood as an on-chain reconfiguration of dollar
liquidity, not as a clean replacement for banks, Treasuries, money-market
funds, custodians, payment networks, or regulators. The evidence base now
supports four broad conclusions.

First, fiat-backed payment stablecoins package bank deposits, Treasury bills,
repo/reverse repo, government money-market funds, custodians, and regulated
issuer contracts into transferable token liabilities (`CLAIM_026`,
`CLAIM_027`, `CLAIM_028`, `CLAIM_034`, `CLAIM_075`, `CLAIM_078`,
`CLAIM_084`). Second, direct redemption rights are narrower than product-page
language: they usually require customer onboarding, jurisdictional eligibility,
KYC/AML, and an account in good standing (`CLAIM_058`, `CLAIM_060`,
`CLAIM_062`, `CLAIM_065`, `CLAIM_068`, `CLAIM_073`, `CLAIM_077`). Third,
regulatory regimes are converging around reserve, redemption, disclosure, and
no-interest principles, but they diverge sharply in issuer perimeter, central
bank deposit requirements, holding limits, insolvency treatment, and
significant-token rules (`CLAIM_036` to `CLAIM_043`, `CLAIM_069` to
`CLAIM_071`, `CLAIM_082` to `CLAIM_097`). Fourth, failure cases show that
stablecoin risk is revealed under stress: reserve access, redemption
operations, reserve opacity, algorithmic feedback loops, collateral auctions,
and basis/funding dynamics fail in different ways (`CLAIM_107` to
`CLAIM_111`).

Two conclusions remain conditional. USDPT is best framed as Western Union's
attempt to build a digital-asset settlement layer, not as proven replacement
of SWIFT, correspondent banking, Fedwire, CHIPS, or the consumer remittance
front end (`CLAIM_051` to `CLAIM_053`). On-chain transfer volume and supply
data cannot yet support strong payment-demand conclusions because adjusted
exports and reproducible data pipelines remain incomplete (`CLAIM_054`,
`CLAIM_055`).

## Chapter 1 - Stablecoins As On-Chain Dollar Infrastructure

The report distinguishes four categories: fiat-backed payment stablecoins,
crypto/RWA-collateralized protocol stablecoins, algorithmic stablecoins, and
synthetic-dollar instruments. This distinction is not cosmetic. USDC, USDT,
PYUSD, USDP, USDG, RLUSD, FDUSD, and GUSD are issuer liabilities backed by
fiat or near-fiat reserve assets. DAI / USDS relies on governance-approved
collateral, vaults, auctions, keepers, oracles, and governance-token
loss-absorption (`CLAIM_098` to `CLAIM_102`). USDe relies on delta-neutral
hedging, off-exchange custody, and a reserve fund rather than a bank-deposit /
Treasury reserve model (`CLAIM_103` to `CLAIM_106`).

This framing prevents three recurring errors: treating all stablecoins as the
same risk class, treating product-page redemption language as contractual
holder rights, and treating raw on-chain activity as real payment demand.

## Chapter 2 - Issuer Comparison

The issuer comparison matrix is the main working table. The claim table now
supports a more precise issuer-by-issuer view.

USDC reserve disclosures support bank deposits, deposits at systemically
important institutions, overnight reverse Treasury repo, sub-3-month
Treasuries, and Circle Reserve Fund exposure (`CLAIM_026`, `CLAIM_027`).
Circle terms establish that direct redemption requires a Circle Mint account
in good standing; transferred holders can redeem directly only if eligible for
and registered with Circle Mint (`CLAIM_058`). USDC holders are not entitled
to reserve interest or returns (`CLAIM_059`).

USDT has a different risk profile. Tether's Q1 2026 reserve materials support
point-in-time assurance and reserve-surplus claims (`CLAIM_002`,
`CLAIM_003`), while issuer-release evidence adds Treasury, gold, and Bitcoin
reserve composition context (`CLAIM_028`, `CLAIM_029`). Tether terms require
verified-customer status for direct issuance/redemption and define prohibited
persons and jurisdictions (`CLAIM_060`, `CLAIM_061`).

Paxos-family stablecoins now have much stronger terms evidence. Paxos terms
identify the issuer allocation across USDP, PYUSD, USDG, and BUSD
(`CLAIM_072`), restrict direct purchase/redemption to Paxos customers
(`CLAIM_073`), state that stablecoins are not designed to create holder
returns (`CLAIM_074`), enumerate reserve categories (`CLAIM_075`), and give
Paxos freeze/upgrade powers across holders (`CLAIM_076`). USDG EU retail
redemption is separately gated by EU residence, supported chain, EU bank
account, and KYC/AML (`CLAIM_068`).

GUSD terms distinguish Gemini Customers from non-Customers: only Gemini
Customers may exchange dollars and GUSD at Gemini, while non-Customer holders
do not thereby create obligations from Gemini (`CLAIM_077`). GUSD reserve
accounts and redemption timing are also claim-backed (`CLAIM_078`,
`CLAIM_079`).

FDUSD terms require eligible FD121 Account status for selling FDD/FDUSD to
FD121, allow suspension or limitation of buying/selling under stress, and
exclude U.S. persons from account eligibility (`CLAIM_062` to `CLAIM_064`).

USDe should not be grouped with fiat-backed payment stablecoins. Ethena terms
distinguish Mint Users and Holding Users, deny Holding Users a direct
redemption right with Ethena BVI, exclude U.S. users from Mint User status,
and state that USDe itself does not generate holder yield (`CLAIM_065`,
`CLAIM_066`). Product-mechanics claims then describe delta-neutral hedging,
off-exchange custody, custodian attestations, and the reserve fund
(`CLAIM_103` to `CLAIM_106`).

## Chapter 3 - Reserve Assets And Dollar Money Markets

Stablecoin reserves connect tokens to bank funding, Treasury bill demand,
repo/reverse repo markets, government MMFs, custodians, and issuer profitability.
The key distinction is not whether a stablecoin says it is "backed", but what
kind of reserve assets sit behind the liability and who receives reserve
income.

USDC, GUSD, Paxos-family stablecoins, RLUSD, and FDUSD all have evidence of
cash, bank deposit, Treasury, MMF, repo, or similar reserve channels
(`CLAIM_026`, `CLAIM_034`, `CLAIM_075`, `CLAIM_078`, `CLAIM_032`,
`CLAIM_010`). USDT includes large Treasury exposure, but also gold and Bitcoin
exposure in issuer-release evidence (`CLAIM_028`, `CLAIM_029`). USDe's backing
and reserve fund are structurally different from a fiat reserve: the risk
channel runs through collateral, hedges, custodians, exchanges, funding rates,
and governance (`CLAIM_103` to `CLAIM_106`).

Reserve-income allocation matters. Circle, Paxos, GENIUS Act, MiCA ART, and
USDe evidence all support a no-holder-yield or no-interest framing for the
token itself (`CLAIM_059`, `CLAIM_066`, `CLAIM_071`, `CLAIM_074`,
`CLAIM_086`).

## Chapter 4 - Law And Regulation

The U.S., EU, UK, and NYDFS regimes are not interchangeable. NYDFS guidance
applies to DFS-regulated U.S. dollar-backed stablecoins and supports full
backing, lawful-holder redemption, permitted reserve assets, and CPA
examination/attestation requirements (`CLAIM_036` to `CLAIM_040`).

MiCA separates EMT and ART regimes. EMTs have at-par redemption and
investment-of-funds rules (`CLAIM_042`, `CLAIM_043`). ARTs have reserve of
assets, permanent redemption, and no-interest rules (`CLAIM_069` to
`CLAIM_071`). Significant-token obligations, recovery plans, and redemption
plans add another layer (`CLAIM_094` to `CLAIM_097`).

GENIUS Act claims now cover permitted issuer eligibility, a three-year
distribution transition and foreign-issuer access conditions, permitted
reserve assets, monthly disclosures and examinations, no holder yield, and
customer-priority insolvency treatment (`CLAIM_082` to `CLAIM_087`). The Bank
of England materials show a different model: 2023 favored full central bank
deposit backing, while the 2025 consultation allows a 40% unremunerated Bank
of England deposit floor plus up to 60% short-term UK government debt, with
holding limits for individuals and businesses (`CLAIM_088` to `CLAIM_091`).

## Chapter 5 - Central-Bank And International Institution Views

Fed and IMF materials are no longer missing. The Fed source set supports
conditional banking-transmission claims: stablecoins may reduce, recycle, or
restructure deposits depending on demand source, converted assets, and reserve
allocation (`CLAIM_046`), and may affect bank credit through deposit volume,
composition, funding costs, and liquidity management (`CLAIM_047`). Fed IFDP
work distinguishes a two-tier model from a narrow-bank model (`CLAIM_048`).

IMF work supports the run-risk / safe-asset backing trade-off and the issuer
incentive problem (`CLAIM_049`). IMF payment-sector event-study evidence
supports a market-expectation claim that pro-stablecoin policy news reduced
listed incumbent payment-firm value by about 18%, roughly US$300bn
(`CLAIM_050`). This is not direct realized payment adoption.

Taiwan-specific implications remain open and should be synthesized only from
CBC/Taiwan sources, not inferred from U.S. or EU documents alone.

## Chapter 6 - USDPT And Cross-Border Payments

USDPT evidence supports product existence, issuer/chain framing, and
infrastructure partnerships. Western Union's announcement and launch materials
state that USDPT is built on Solana, issued by Anchorage Digital Bank or
Anchorage Digital Bank N.A., fully backed by U.S. dollars, and intended for
real-world payment systems (`CLAIM_051`, `CLAIM_052`). Fireblocks material
adds wallet, settlement, agent-settlement, treasury/operations, and MT940/MT942
reporting context (`CLAIM_053`).

This does not prove replacement of SWIFT, correspondent banking, Fedwire,
CHIPS, or Western Union's consumer-facing remittance rails. The safest current
claim is that Western Union is attempting to build a regulated digital-asset
settlement layer. Product terms, reserve report, contract addresses, direct
redemption mechanics, and end-to-end workflow documents remain blockers.

## Chapter 7 - On-Chain Data And Payment Demand

The market-data module is no longer empty, but it remains methodologically
limited. Artemis documentation supports the existence of stablecoin transfer
volume, transaction, supply, and address-level schemas with filter categories
(`CLAIM_054`). DeFiLlama API snapshots support supply and chain-distribution
analysis, not adjusted payment-volume evidence (`CLAIM_055`).

The report must not equate raw transfer volume, supply, or market cap with
real payment demand. A reproducible data pipeline is required before Chapter 7
can make quantitative payment-demand claims.

## Chapter 8 - Failure Cases

Failure cases now support the risk taxonomy. Terra UST anchors algorithmic
death-spiral risk (`CLAIM_107`). USDC/SVB anchors fiat-backed bank-deposit and
operational-liquidity risk (`CLAIM_108`, `CLAIM_109`). Tether / Bitfinex NYAG
sources anchor reserve-opacity and disclosure risk (`CLAIM_110`). Iron
Finance anchors a medium-confidence reflexive bank-run case (`CLAIM_111`).

Maker / DAI Black Thursday remains a priority open case because it would
strengthen the crypto-collateral / oracle / liquidation-auction risk channel.

## Chapter 9 - Conclusion

The current evidence supports a disciplined formulation: stablecoins are not
outside the dollar system. They are tokenized claims and protocols that
rearrange the legal, operational, and market plumbing of dollar liquidity. The
main policy questions are therefore about issuer perimeter, reserve quality,
redemption rights, insolvency priority, holder yield, payment-system access,
data transparency, and stress behavior.

The remaining work is not cosmetic. Adjusted data exports are needed for
payment-demand conclusions; USDPT product documents are needed for
settlement-displacement claims; and additional failure-case sources are needed
for a full risk-history chapter.
