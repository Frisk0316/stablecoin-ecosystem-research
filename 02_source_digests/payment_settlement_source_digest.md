# Payment and Settlement Source Digest v0.1

## CPMI Correspondent Banking 2016
This source defines correspondent banking as a network of bank relationships that enables access to cross-border financial services and payments. It is important for distinguishing messaging, banking relationships, compliance/KYC costs, and actual settlement.

## CPMI Cross-Border Retail Payments 2018
This source establishes the baseline problem: cross-border retail payments are often slower, costlier, and less transparent than domestic payments. It also explains that many providers still rely on correspondent banks for clearing, settlement and FX.

## Fedwire PFMI disclosure
This source should be used to distinguish wholesale USD settlement infrastructure from SWIFT messaging and retail payment-service providers.

## Western Union and Anchorage materials
These sources now support a stronger but still bounded USDPT/UDSPT chapter.
Anchorage's comment letter page and PDF support the issuer/brand-partner
context (`CLAIM_023`). Western Union's 2025 announcement states that USDPT
would be built on Solana, issued by Anchorage Digital Bank, and paired with a
Digital Asset Network intended to bridge digital and fiat worlds
(`CLAIM_051`). Western Union's 2026 launch release states that USDPT launched
as a U.S. dollar-denominated payment stablecoin, fully backed by U.S. dollars,
issued by Anchorage Digital Bank N.A., and built on Solana (`CLAIM_052`).

The Fireblocks partnership release supports operational-infrastructure context:
wallet, settlement, and financial-operations infrastructure; agent settlement
in USDPT; Dynamic embedded wallets; and TRES translation of onchain data into
SWIFT MT940/MT942 formats (`CLAIM_053`). This is secondary evidence and should
not be used as product terms.

Open points remain: direct holder redemption, reserve report, contract
addresses, customer eligibility, agent cash-out workflow, and whether USDPT
changes customer-facing remittance rails, back-end treasury settlement, or both.
