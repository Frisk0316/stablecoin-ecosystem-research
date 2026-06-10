# Payment and Settlement Source Digest v0.3.3

## CPMI Correspondent Banking 2016
This source defines correspondent banking as a network of bank relationships that enables access to cross-border financial services and payments. It is important for distinguishing messaging, banking relationships, compliance/KYC costs, and actual settlement.

## CPMI Cross-Border Retail Payments 2018
This source establishes the baseline problem: cross-border retail payments are often slower, costlier, and less transparent than domestic payments. It also explains that many providers still rely on correspondent banks for clearing, settlement and FX.

## Fedwire PFMI disclosure
This source should be used to distinguish wholesale USD settlement infrastructure from SWIFT messaging and retail payment-service providers.

## Western Union and Anchorage materials
These sources now support a stronger but still bounded USDPT chapter.
Anchorage's comment letter page and PDF support the issuer/brand-partner
context (`CLAIM_023`). Western Union's 2025 announcement states that USDPT
would be built on Solana, issued by Anchorage Digital Bank, and paired with a
Digital Asset Network intended to bridge digital and fiat worlds
(`CLAIM_051`). Western Union's 2026 launch release states that USDPT launched
as a U.S. dollar-denominated payment stablecoin, fully backed by U.S. dollars,
issued by Anchorage Digital Bank N.A., and built on Solana (`CLAIM_052`).

The 2026-05-04 Western Union investor-relations launch release (`USDPT_007`)
now also supports three further architectural claims at primary-source level:
the **Digital Asset Network** is described as the component bridging licensed
virtual currency exchanges and custodians to Western Union's global payout and
liquidity infrastructure (`CLAIM_132`); **Treasury and Agent Settlement** is
named as a USDPT use case enabling near-instant 24/7 settlement between
Western Union and its global agents, which anchors USDPT evidence to the
internal-treasury and agent-reconciliation layer rather than to the retail
cash-out layer (`CLAIM_133`); and **Stable by Western Union** is announced as
a separate consumer-facing spend capability launching in 2026 in 40+
countries, which must be kept distinct from USDPT issuance and settlement
(`CLAIM_134`).

The Fireblocks partnership release supports operational-infrastructure context:
wallet, settlement, and financial-operations infrastructure; agent settlement
in USDPT; Dynamic embedded wallets; and TRES translation of onchain data into
SWIFT MT940/MT942 formats (`CLAIM_053`). This is secondary evidence and should
not be used as product terms.

The Western Union USDPT product page (`USDPT_005`) now closes several earlier
document gaps at product-page level. It states that USDPT is redeemable 1:1,
issued by Anchorage Digital Bank N.A. on Solana, and backed by equal USD
reserves including bank deposits, U.S. Treasury bills, and similar cash
equivalents (`CLAIM_140`). It also discloses the official Solana contract
address and no-government-guarantee / no-FDIC-insurance disclaimer
(`CLAIM_141`). Finally, it describes coming-soon exchange availability,
select-market cash-out through a virtual-currency-exchange app at Western
Union locations, a self-custody USDPT wallet plus Visa payment-card mobile app,
and select-market receipt of money transfers in USDPT (`CLAIM_142`).

Anchorage's stablecoin reserve-transparency page (`USDPT_010`) gives a
platform-level statement that ADB-issued stablecoins are redeemable 1:1 on
Anchorage's platform and that monthly reserve attestations are published, but
the USDPT entry itself is still marked "Coming soon" (`CLAIM_143`). This means
the reserve-report location is now identified, while the USDPT-specific reserve
report remains unavailable.

Anchorage's Covered Stablecoin Terms (`USDPT_011`) add a legal-rights boundary
for ADB-issued stablecoin series. The terms distinguish ADB Clients from
Non-Clients and state that direct ADB issuance and redemption are exclusive to
Clients (`CLAIM_150`). They also describe a Covered Stablecoin Reserve trust,
ADB as sole issuer and sole obligor, brand partners as service providers
rather than obligors, par value only for direct Client redemption with ADB, and
legal/regulatory freeze or restriction powers (`CLAIM_151`).

Bybit's 2026-06-04 joint press release with Western Union (`USDPT_012`) adds a
first concrete exchange-integration data point for the Digital Asset Network.
Bybit states it is the first major crypto exchange to integrate USDPT and to
join Western Union's global USDPT network, with users able to buy USDPT through
Bybit One-Click Buy and convert back to fiat at any time, launching in selected
Latin America markets (`CLAIM_155`). This is partner / exchange news, not USDPT
legal product terms or reserve documentation, but it moves the previously
coming-soon exchange-support feature (`CLAIM_142`) to a first live exchange and
gives the Digital Asset Network (`CLAIM_132`) one named, live counterparty.

Open points remain: USDPT-specific retail product/user terms, fee schedule,
USDPT reserve report, exact mint/burn or smart-contract controls, customer
eligibility and supported jurisdictions for Western Union / exchange-app flows,
operational agent cash-out workflow, and whether USDPT changes
customer-facing remittance rails or only back-end treasury settlement. The
product-page, ADB terms, and layer-3 anchors (`CLAIM_140` to `CLAIM_143`,
`CLAIM_150`, `CLAIM_151`, plus `CLAIM_132` to `CLAIM_134`) narrow those gaps
but do not remove the need for USDPT-specific workflow documentation.

Delivery status after the v0.3.3 cascade:

| Layer | Evidence status | Current wording |
| --- | --- | --- |
| Customer remittance UX | Partially supported as planned feature | WU product page says select-market customers will have the option to receive a money transfer in USDPT (`CLAIM_142`); sender flow, custody, fees, KYC and terms remain missing. |
| Agent network / last-mile payout | Partially supported only for customer exchange-app cash-out | WU product page says exchange customers in select markets will be able to cash out local fiat at WU locations (`CLAIM_142`); Bybit is now a first live exchange integration for buying USDPT and converting back to fiat in selected Latin America markets (`CLAIM_155`); neither establishes that agents hold or redeem USDPT on their own balance sheets. |
| Internal treasury / agent settlement | Strongest layer | WU IR release explicitly names Treasury and Agent Settlement (`CLAIM_133`) and the Digital Asset Network bridge to licensed VCEs and custodians (`CLAIM_132`); Fireblocks materials add operational infrastructure (`CLAIM_053`). |
| Reserve / bank / correspondent settlement | Partially supported at ADB terms level; still source-dependent for USDPT-specific workflow | WU product page names broad reserve categories (`CLAIM_140`), Anchorage identifies the USDPT report slot as coming soon (`CLAIM_143`), and ADB Covered Stablecoin Terms describe a reserve trust and ADB sole-obligor role for ADB-issued series (`CLAIM_151`); no USDPT reserve report or bank-settlement workflow yet. |

The live USDPT research queue is
`00_project_management/usdpt_product_terms_research_queue.md`. Use that queue
before strengthening any Chapter 6 conclusion.
