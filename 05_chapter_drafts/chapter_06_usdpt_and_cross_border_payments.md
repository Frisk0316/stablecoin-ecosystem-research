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

Current evidence is strongest at layer 3 (internal treasury and agent
settlement) and weakest at layers 1, 2, and 4 (customer UX, agent last-mile,
and bank/clearing settlement). The chapter's claims must respect that
asymmetry.

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

What this set supports: product existence, issuer identity, chain choice,
USD-backing framing, and a back-office infrastructure partnership at layer 3.
What it does **not** support: direct retail redemption rights, agent-layer
cash-out semantics, replacement of any specific wholesale rail, or any
quantitative claim about corridor pricing or settlement time.

## USDPT in the issuer-comparison frame

Where the issuer-comparison matrix (chapter 2 / `04_matrices/issuer_comparison_matrix.csv`)
catalogues USDC, USDT, PYUSD, USDG, RLUSD, GUSD, FDUSD, DAI/USDS, and USDe along
dimensions of reserve composition, regulatory regime, direct redemption rights,
freeze powers, and yield, USDPT currently occupies an evidence-poor cell on
every dimension except product existence, issuer identity, and the high-level
USD-backing assertion. The reserve composition, redemption rights, freeze
mechanics, holder yield position, and contractual customer scope are **not
documented** at primary-source level. Comparisons between USDPT and other
stablecoins in this project should therefore be made by *what we know about
the other stablecoin*, with the USDPT side held conditional until product
terms become available.

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
infrastructure layer of the Fireblocks partnership. The customer UX (layer 1),
agent last-mile (layer 2), and bank/clearing settlement (layer 4) are not yet
documented from primary sources, and the comparative analytical work in
chapter 6 should therefore not claim displacement of those layers.

## Documentation gaps and the live research queue

The complete primary-document gap list — product terms, reserve attestation,
direct redemption policy, contract addresses, chain/network support,
end-to-end customer workflow, agent settlement workflow — lives in
`00_project_management/usdpt_product_terms_research_queue.md`. The intake
workflow there (sections 60–71) defines how to promote a found source into
registry → digest → claim → matrix → chapter. Until that queue closes, the
chapter's USDPT statements must remain at digest level for layers 1, 2, and 4.

## Safe wording (do not exceed)

The project's standing wording for USDPT-related conclusions is:

> Western Union is attempting to use USDPT and a Digital Asset Network to
> build a regulated digital-asset settlement layer that may affect back-end
> treasury, wallet, agent-settlement, or reporting workflows, but the archive
> does not yet prove displacement of SWIFT, correspondent banking, wholesale
> settlement systems, or consumer-facing remittance rails.

Do not upgrade this wording without a primary product or workflow document
supporting the exact statement being added.

## Chapter limitations

- Only four USDPT-related claims are formally anchored (`CLAIM_023`,
  `CLAIM_051`, `CLAIM_052`, `CLAIM_053`). All cover product
  announcement / launch / infrastructure framing; none cover product terms,
  reserve composition, redemption rights, or end-to-end customer workflow.
- Western Union and Anchorage product documentation (terms, reserve report,
  contract addresses, agent workflow) is not yet archived.
- No corridor-level pricing, settlement-time, or volume data has been
  extracted; chapter 7's data-landscape limitations apply to any quantitative
  USDPT inference.
- The four-layer frame above is a structural device, not a claim. It is used
  to organise gaps, not to license inference between layers.

## Open Questions

- Obtain USDPT product terms, reserve reports, contract addresses, direct
  redemption rights, and user/agent workflow documentation.
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
