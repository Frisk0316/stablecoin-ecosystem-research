# Chapter 6 - USDPT and Cross-border Payments

Working thesis: USDPT should be analysed as a potential change to payment and
settlement architecture, not simply as a generic stablecoin. Evidence supports
that Western Union is attempting to build a USDPT-based digital-asset
settlement layer; it does not yet support claims that USDPT displaces SWIFT,
correspondent banking, Fedwire/CHIPS, or Western Union's own consumer-facing
remittance rails. This chapter retains a conditional framing throughout, in
keeping with the safe wording defined in
`00_project_management/usdpt_product_terms_research_queue.md`.

## Why USDPT is treated separately

USDPT is the only registered stablecoin in this project that is positioned by
its sponsor as **payment infrastructure first** rather than as a reserve-asset
or DeFi-liquidity instrument. That positioning is what justifies a dedicated
chapter. It does not, on its own, justify any conclusion about substitution of
existing rails. The four-layer analytical frame below is the structural device
used to keep evidence and inference separated.

## Four-layer analytical frame

USDPT is organised across four payment layers. Treat the evidence on each
layer separately:

1. **Customer remittance user experience** — sender and receiver flows, KYC,
   pricing, FX disclosure, cash-in / cash-out endpoints.
2. **Agent network and last-mile fiat payout** — Western Union's existing
   agent footprint and whether agents touch USDPT at any point.
3. **Internal treasury and agent settlement** — Western Union's back-office
   liquidity, agent-network reconciliation, and the wallet/custody layer.
4. **Bank, correspondent, Fedwire/CHIPS, and local clearing settlement** —
   the wholesale and clearing rails that connect Western Union (or any
   issuer) into the broader payment system.

Current evidence remains strongest at layer 3 (internal treasury and agent
settlement) — anchored explicitly at primary-source level via the WU
2026-05-04 IR launch release (`CLAIM_132`, `CLAIM_133`) and the Fireblocks
partnership materials (`CLAIM_053`). The Western Union product page now
partially strengthens layer 1 and layer 2 by describing coming-soon,
select-market cash-out at Western Union locations through virtual-currency
exchange apps, a Visa card mobile app tied to a self-custody USDPT wallet,
and money transfers received in USDPT (`CLAIM_142`). That is product-page
direction, not full user terms. Layer 4 (reserve-bank / correspondent /
clearing settlement) remains the weakest layer: broad reserve categories and
the official Solana contract address are now disclosed (`CLAIM_140`,
`CLAIM_141`), and ADB covered-stablecoin terms now provide a reserve-trust /
sole-obligor and Client-redemption boundary (`CLAIM_150`, `CLAIM_151`), but no
USDPT-specific reserve report, fee schedule, mint/burn control document, or
bank-settlement workflow is in the archive.

## Evidence currently anchored at claim level

- Anchorage's OCC comment letter supplies background: Anchorage Digital Bank
  described itself as issuer of USAT, USDGO, and USDtb, and said it expected
  to begin issuing USDPT with Western Union as brand partner (`CLAIM_023`).
- Western Union's October 28, 2025 announcement states that USDPT would be
  built on Solana, issued by Anchorage Digital Bank, and connected to a
  Digital Asset Network (`CLAIM_051`).
- Western Union's March 31, 2026 launch release states that USDPT is a
  USD-denominated payment stablecoin, fully backed by U.S. dollars, issued by
  Anchorage Digital Bank N.A., and built on Solana (`CLAIM_052`).
- Fireblocks' infrastructure material adds operational clues: agent
  settlement, wallet infrastructure, compliance tooling, TRES accounting
  support, and MT940/MT942 message translation are presented as part of the
  USDPT ecosystem (`CLAIM_053`).
- The 2026-05-04 Western Union investor-relations launch release
  (`USDPT_007`) adds three further anchors. The Digital Asset Network is
  described as the component bridging licensed virtual currency exchanges
  and custodians to Western Union's global payout and liquidity
  infrastructure (`CLAIM_132`). Treasury and Agent Settlement is named as a
  USDPT use case enabling near-instant 24/7 settlement between Western
  Union and its global agents, which is the strongest layer-3 (internal
  treasury / agent-reconciliation) anchor now in the archive
  (`CLAIM_133`). Stable by Western Union is announced as a separate
  consumer-facing spend capability launching in 2026 in 40+ countries, and
  must be kept distinct from USDPT issuance and settlement (`CLAIM_134`).
- Western Union's USDPT product page (`USDPT_005`) states that USDPT is
  redeemable 1:1, issued by Anchorage Digital Bank N.A. on Solana, and
  backed by equal USD reserves including bank deposits, U.S. Treasury bills,
  and similar cash equivalents (`CLAIM_140`). The same page discloses the
  official Solana contract address and no-government-guarantee /
  no-FDIC-insurance disclaimer (`CLAIM_141`), and lists coming-soon exchange,
  cash-out, Visa card app, and receive-in-USDPT product features
  (`CLAIM_142`).
- Anchorage's reserve-transparency page (`USDPT_010`) identifies USDPT as a
  Western Union U.S. dollar-denominated stablecoin issued by Anchorage
  Digital Bank, but marks USDPT reports as "Coming soon" (`CLAIM_143`).
- Anchorage Digital Bank's Covered Stablecoin Terms (`USDPT_011`) apply to
  ADB-issued payment-stablecoin series, distinguish Clients from Non-Clients,
  and limit direct ADB issuance/redemption to Clients (`CLAIM_150`). They also
  describe a Covered Stablecoin Reserve trust, ADB sole issuer / sole obligor
  status, brand partners as service providers rather than obligors, par value
  only for direct Client redemption with ADB, and legal/regulatory freeze or
  restriction powers (`CLAIM_151`).

What this set supports: product existence, issuer identity, chain choice,
USD-backing framing, official Solana address disclosure, product-page reserve
categories, coming-soon/select-market exchange/cash-out/receive-in-USDPT
features, a back-office infrastructure partnership at layer 3, and an
explicit Treasury and Agent Settlement use case at layer 3 with a separate
consumer-spend product layer (Stable by Western Union) at layer 1. The ADB
terms also support a Client / Non-Client redemption-right boundary, reserve
trust framing, sole-obligor role, brand-partner limit, and legal/control-risk
language for ADB-issued stablecoin series. What this set does **not** support:
live global cash-out availability, direct retail USDPT redemption rights for
WU users / exchange users / agents unless they are ADB Clients, agent
balance-sheet treatment of USDPT, replacement of any specific wholesale rail,
the existence of a USDPT-specific reserve report, exact mint/burn or blacklist
implementation details, or any quantitative claim about corridor pricing or
settlement time.

## USDPT in the issuer-comparison frame

Where the issuer-comparison matrix (chapter 2 / `04_matrices/issuer_comparison_matrix.csv`)
catalogues USDC, USDT, PYUSD, USDG, RLUSD, GUSD, FDUSD, DAI/USDS, and USDe along
dimensions of reserve composition, regulatory regime, direct redemption rights,
freeze powers, and yield, USDPT has now moved out of the most evidence-poor
state on chain/address and high-level reserve categories: the product page
discloses Solana, a specific official Solana contract address, and broad
reserve categories (`CLAIM_140`, `CLAIM_141`). It remains evidence-poor on
attested reserve composition, retail/agent eligibility beyond the ADB Client
boundary, exact freeze / blacklist / pause implementation, holder yield
treatment, USDPT-specific customer terms, and operational workflow. Comparisons
between USDPT and other stablecoins in this project should therefore
distinguish *product-page assertions* and *ADB covered-stablecoin terms* from
*USDPT-specific user terms and attested reserve reports*.

## How USDPT relates to existing rails (required distinctions)

The literature regularly conflates three distinct components of cross-border
payments. Keep them separated:

- **SWIFT** is primarily a financial messaging network. It does not move
  funds itself; payments move via correspondent-bank account relationships.
- **Correspondent banking** provides relationships, accounts, KYC and
  compliance, liquidity management, and settlement pathways. CPMI 2016
  (BIS_004) is the canonical reference for the model and its frictions.
- **Fedwire and CHIPS** provide wholesale USD settlement and clearing inside
  the United States; they are domestic settlement layers, not cross-border
  ones.
- **Western Union's agent network** is a consumer-facing remittance system
  with corridor-specific pricing, cash-in/cash-out endpoints, and an
  agent-reconciliation back office. It is operationally distinct from the
  bank-to-bank rails above.

USDPT, on the evidence currently archived, intersects most directly with the
back-office and agent-reconciliation layer (layer 3 above) and the wallet/
infrastructure layer of the Fireblocks partnership. The product page now gives
a planned layer-1 / layer-2 direction: select-market cash-out at WU locations
through exchange apps, select-market Visa card app use, and select-market
receipt of money transfers in USDPT. Those are not enough to claim that WU's
existing consumer-remittance rails, agents' balance sheets, or correspondent
banking routes have been displaced. The bank/clearing settlement layer
(layer 4) remains undocumented beyond reserve-category, issuer, and ADB
covered-stablecoin terms statements.

## Documentation gaps and the live research queue

The complete remaining primary-document gap list -- USDPT-specific product
terms, fee schedule, reserve attestation, retail/agent redemption policy beyond
the ADB Client boundary, chain/network support beyond the disclosed Solana
address, exact mint/burn controls, end-to-end customer workflow, and agent
settlement workflow -- lives in
`00_project_management/usdpt_product_terms_research_queue.md`. The intake
workflow there (sections 60–71) defines how to promote a found source into
registry → digest → claim → matrix → chapter. Until that queue closes, the
chapter's USDPT statements must remain at digest level for layers 1, 2, and 4.

## Safe wording (do not exceed)

The project's standing wording for USDPT-related conclusions is:

> Western Union is attempting to use USDPT and a Digital Asset Network to
> build a regulated digital-asset settlement layer that may affect back-end
> treasury, wallet, agent-settlement, exchange cash-out, or reporting
> workflows. Western Union's product page also points to coming-soon,
> select-market consumer-facing USDPT features, and ADB's covered-stablecoin
> terms bound direct ADB redemption to Clients while reserving legal/control
> powers, but the archive does not yet prove displacement of SWIFT,
> correspondent banking, wholesale settlement systems, or Western Union's
> existing consumer-facing remittance rails.

Do not upgrade this wording without a primary product or workflow document
supporting the exact statement being added.

## Chapter limitations

- Thirteen USDPT-related claims are now formally anchored (`CLAIM_023`,
  `CLAIM_051`, `CLAIM_052`, `CLAIM_053`, `CLAIM_132`, `CLAIM_133`,
  `CLAIM_134`, `CLAIM_140`, `CLAIM_141`, `CLAIM_142`, `CLAIM_143`,
  `CLAIM_150`, `CLAIM_151`). They
  cover issuer / chain / fully-USD-backed framing,
  Fireblocks operational context, the Digital Asset Network bridge to
  licensed VCEs and custodians, the Treasury and Agent Settlement use
  case, Stable by Western Union as a separate consumer-spend product,
  official Solana contract-address disclosure, broad product-page reserve
  categories, coming-soon exchange/cash-out/card/receive features, and the
  Anchorage reserve-report slot, plus ADB covered-stablecoin Client /
  Non-Client, reserve-trust, sole-obligor, brand-partner and legal-control
  terms.
  None of them cover USDPT-specific retail terms, attested reserve
  composition, exact mint/burn implementation, retail/agent eligible-redeemer
  scope beyond ADB Client status, or complete end-to-end customer workflow.
- Western Union retail legal/product documentation, USDPT reserve reports,
  USDPT-specific fee/user disclosures, and agent workflow are not yet archived.
- No corridor-level pricing, settlement-time, or volume data has been
  extracted; chapter 7's data-landscape limitations apply to any quantitative
  USDPT inference.
- The four-layer frame above is a structural device, not a claim. It is used
  to organise gaps, not to license inference between layers.

## Open Questions

- Obtain USDPT-specific product/user terms, fee schedule, reserve reports,
  direct retail/agent redemption rights beyond the ADB Client boundary,
  mint/burn and exact smart-contract freeze controls, supported network list
  beyond the disclosed Solana address, and user/agent workflow documentation.
- Determine whether Western Union agents handle retail stablecoin cash-out,
  only fiat endpoints, or only internal/agent settlement.
- Map the relationship between Fireblocks' MT940/MT942 reporting layer and
  the upstream bank/clearing settlement.
- Map any regulatory filings beyond the Anchorage OCC comment letter
  (state-level, OCC, FinCEN, foreign jurisdictions) once available.

The live product-document queue is
`00_project_management/usdpt_product_terms_research_queue.md`. Do not upgrade
the chapter from "digital asset settlement layer" to "replacement of
traditional cross-border payment rails" unless that queue is closed with
primary-source evidence.
