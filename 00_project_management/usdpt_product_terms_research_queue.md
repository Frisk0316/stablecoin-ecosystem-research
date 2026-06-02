# USDPT Product Terms / Reserve / Redemption Research Queue

Last updated: 2026-05-25

Purpose: USDPT is valuable for the Western Union cross-border settlement
chapter, but current evidence supports only a bounded claim: Western Union is
attempting to build a USDPT-based digital asset settlement layer. The archive
does not yet support a strong claim that USDPT replaces SWIFT, correspondent
banking, Fedwire, CHIPS, or Western Union's consumer-facing remittance rails.

## Current Claim Support

- `CLAIM_051`: Western Union announced USDPT would be built on Solana, issued
  by Anchorage Digital Bank, and linked to a Digital Asset Network.
- `CLAIM_052`: Western Union announced USDPT launched as a fully USD-backed
  payment stablecoin issued by Anchorage Digital Bank N.A. and built on Solana.
- `CLAIM_053`: Fireblocks describes wallet, settlement, agent-settlement,
  financial-operations, and MT940/MT942 reporting infrastructure.

## Evidence Status Table

| Question | Current status | Supported by | Delivery note |
| --- | --- | --- | --- |
| Product exists / was announced | Supported | `CLAIM_051`, `CLAIM_052` | Safe to describe USDPT as announced/launched in WU materials. |
| Expected issuer | Supported | `CLAIM_051`, `CLAIM_052` | Safe to identify Anchorage Digital Bank N.A. as issuer in launch materials. |
| Chain / network | Supported | `CLAIM_051`, `CLAIM_052` | Safe to state Solana, subject to future supported-network updates. |
| Broad USD backing language | Supported only at issuer-release level | `CLAIM_052` | Safe wording: WU says fully backed by U.S. dollars; do not specify asset mix. |
| Fireblocks / Dynamic / TRES infrastructure | Supported as infrastructure context | `CLAIM_053` | Safe to describe wallet, settlement, reporting and agent-settlement tooling. |
| Product terms / user terms | Unsupported | none | Do not infer customer rights or direct holder protections. |
| Reserve report / attestation | Unsupported | none | Do not compare USDPT reserve composition to USDC/USDT/Paxos reports. |
| Contract addresses | Unsupported | none | Do not present on-chain verification or circulating-supply analysis. |
| Direct redemption eligibility | Unsupported | none | Do not state that any holder, retail WU user, or agent can redeem directly. |
| Customer-to-customer workflow | Unsupported | none | Treat customer remittance UX as existing WU rails, not a documented USDPT flow. |
| Agent cash-out / agent USDPT holding | Unsupported | none | Do not say WU agents handle, hold, redeem, or cash out USDPT. |
| SWIFT / correspondent / Fedwire / CHIPS displacement | Not supported and not inferable | none | Only discuss possible back-office settlement-layer experimentation. |

## Missing Primary Documents

High-priority:

- USDPT product terms / user terms.
- Anchorage Digital Bank USDPT issuance terms.
- USDPT reserve report or attestation.
- USDPT direct redemption policy and eligible redeemer scope.
- Contract addresses and supported chain/network list.
- End-to-end customer-to-customer workflow document.
- Agent settlement workflow: whether agents hold USDPT, settle in USDPT, or
  only receive fiat with USDPT used in a back-office treasury layer.

Medium-priority:

- Exchange or liquidity-provider support documentation.
- Custodian / wallet / compliance-provider technical docs.
- Customer disclosure or risk-factor page.
- Any regulator-facing filing beyond the Anchorage comment letter.

## Required Evidence Before Strong Claims

Do not write:

- "USDPT replaces SWIFT."
- "USDPT replaces correspondent banking."
- "USDPT replaces Fedwire or CHIPS."
- "Western Union agents cash out USDPT directly."
- "USDPT gives any holder direct 1:1 redemption."

unless primary product or workflow documents support the exact statement.

Current safe wording:

> Western Union is attempting to use USDPT and a Digital Asset Network to build
> a regulated digital-asset settlement layer that may affect back-end treasury,
> wallet, agent-settlement, or reporting workflows, but the archive does not
> yet prove displacement of SWIFT, correspondent banking, wholesale settlement
> systems, or consumer-facing remittance rails.

If a future primary document supports only one layer of the four-layer frame,
upgrade only that layer. For example, a contract-address disclosure would
support on-chain issuance analysis, but would still not support agent cash-out
or correspondent-banking displacement.

## Intake Workflow

When a missing USDPT source is found:

1. Add it to `01_sources/source_registry.csv` with a stable `USDPT_###` ID.
2. Add a source digest paragraph in
   `02_source_digests/payment_settlement_source_digest.md`.
3. Add claim-table rows only for explicit product, reserve, redemption, or
   workflow statements.
4. Update `04_matrices/payment_settlement_matrix.csv`.
5. Update `05_chapter_drafts/chapter_06_usdpt_and_cross_border_payments.md`.
6. Update this queue and `00_project_management/unresolved_open_questions.md`.

## Four-Layer Analysis Frame

Keep the USDPT chapter organized by layer:

1. Customer remittance user experience.
2. Western Union agent network and last-mile fiat payout.
3. Western Union internal treasury / agent settlement.
4. Bank, correspondent, Fedwire, CHIPS, and local clearing settlement.

Current evidence is strongest for layer 3 and weakest for layers 1, 2, and 4.
