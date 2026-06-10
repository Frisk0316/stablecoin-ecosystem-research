# USDPT Product Terms / Reserve / Redemption Research Queue

Last updated: 2026-06-10

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
- `CLAIM_140`: Western Union's product page states USDPT is redeemable 1:1,
  issued by Anchorage Digital Bank N.A. on Solana, and backed by equal USD
  reserves including bank deposits, U.S. Treasury bills and similar cash
  equivalents.
- `CLAIM_141`: Western Union's product page discloses the official Solana
  contract address and the no-government-guarantee / no-FDIC-insurance
  disclaimer.
- `CLAIM_142`: Western Union's product page lists coming-soon exchange,
  cash-out, Visa card app, and receive-in-USDPT features with select-market
  caveats.
- `CLAIM_143`: Anchorage's reserve-transparency page identifies USDPT and
  marks USDPT reports as "Coming soon".
- `CLAIM_150`: Anchorage Digital Bank's Covered Stablecoin Terms apply to
  ADB-issued payment-stablecoin series and distinguish Clients from
  Non-Clients; ADB issues and redeems Covered Stablecoins exclusively to and
  from Clients.
- `CLAIM_151`: The same terms describe a one-dollar par value, Covered
  Stablecoin Reserve trust structure, ADB as sole issuer and sole obligor,
  brand partners as service providers rather than obligors, par value only
  for direct Client redemption with ADB, and legal/regulatory freeze or
  restriction powers.
- `CLAIM_155` (2026-06-04, `USDPT_012`): Bybit is the first major crypto
  exchange to integrate USDPT and join Western Union's global USDPT network;
  users can buy USDPT via Bybit One-Click Buy and convert back to fiat in
  selected Latin America markets. First live exchange counterparty for the
  Digital Asset Network; still exchange/partner news, not USDPT-specific
  product terms, fee schedule, or reserve report.

## Evidence Status Table

| Question | Current status | Supported by | Delivery note |
| --- | --- | --- | --- |
| Product exists / was announced | Supported | `CLAIM_051`, `CLAIM_052` | Safe to describe USDPT as announced/launched in WU materials. |
| Expected issuer | Supported | `CLAIM_051`, `CLAIM_052` | Safe to identify Anchorage Digital Bank N.A. as issuer in launch materials. |
| Chain / network | Supported | `CLAIM_051`, `CLAIM_052` | Safe to state Solana, subject to future supported-network updates. |
| Broad USD backing language | Supported at issuer-release and product-page level | `CLAIM_052`, `CLAIM_140` | Safe wording: WU says USDPT is backed by equal USD reserves including bank deposits, U.S. Treasury bills and similar cash equivalents; do not treat this as an attested reserve composition. |
| Fireblocks / Dynamic / TRES infrastructure | Supported as infrastructure context | `CLAIM_053` | Safe to describe wallet, settlement, reporting and agent-settlement tooling. |
| Official Solana contract address | Supported | `CLAIM_141` | Safe to cite the disclosed Solana address; do not infer mint/burn controls or circulating supply without chain analysis. |
| Exchange / cash-out / receive-in-USDPT product direction | Supported as coming-soon / select-market product-page wording | `CLAIM_142` | Safe to describe planned features; do not state live availability, eligible jurisdictions, fees, KYC flow, or agent obligations without terms. |
| Product terms / user terms | Partially supported at ADB covered-stablecoin terms level; USDPT-specific retail/WU terms still missing | `CLAIM_150`, `CLAIM_151` | ADB terms bound Client vs Non-Client rights and reserve/control framework for ADB-issued series; do not infer WU app terms, exchange-app terms, fees, jurisdiction eligibility, or retail customer workflow. |
| Reserve report / attestation | Location identified, report not yet available | `CLAIM_143` | Anchorage reserve page says reports are published monthly for ADB stablecoins but USDPT is "Coming soon"; do not compare USDPT reserve composition to USDC/USDT/Paxos reports yet. |
| Direct redemption eligibility | Partially bounded at ADB terms level | `CLAIM_140`, `CLAIM_143`, `CLAIM_150` | WU says redeemable 1:1 and Anchorage says ADB stablecoins are redeemable on its platform; ADB terms say issuance/redemption is exclusively for Clients and Non-Clients are not ADB customers. Do not state that any retail holder, WU user, exchange user, or agent can redeem directly unless they are an ADB Client under applicable terms. |
| Reserve trust / issuer-obligor structure | Supported at ADB covered-stablecoin terms level | `CLAIM_151` | Safe to state that ADB terms describe a Covered Stablecoin Reserve trust and ADB sole issuer/sole obligor role for ADB-issued series; still not a USDPT-specific reserve attestation. |
| Legal/control powers | Partially supported at ADB terms level | `CLAIM_151` | Safe to note ADB terms reserve legal/regulatory freeze, block, seize or restriction powers; do not infer exact smart-contract roles, mint/burn admin keys, blacklist function implementation, or Solana-program controls. |
| Customer-to-customer workflow | Partially supported as planned feature | `CLAIM_142` | WU product page says select-market customers will have the option to receive transfers in USDPT; user terms, sender flow, fees, KYC, custody and settlement details remain missing. |
| Agent cash-out / agent USDPT holding | Partially supported only for customer exchange-app cash-out at WU locations | `CLAIM_142` | Product page supports a planned cash-out path for exchange customers in select markets; it does not say WU agents hold, redeem, or settle USDPT on their own balance sheets. |
| SWIFT / correspondent / Fedwire / CHIPS displacement | Not supported and not inferable | none | Only discuss possible back-office settlement-layer experimentation. |

## Missing Primary Documents

High-priority:

- USDPT-specific product terms / user terms, fee schedule, and retail risk
  disclosure.
- Anchorage Digital Bank USDPT-specific series supplement, if any.
- USDPT reserve report or attestation.
- USDPT direct redemption policy and eligible redeemer scope beyond the ADB
  Client / Non-Client boundary.
- Supported chain/network list beyond the disclosed Solana contract address.
- End-to-end customer-to-customer workflow document, including sender/receiver
  eligibility, custody model, fees, FX disclosure, and KYC/AML flow.
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
- "USDPT cash-out is live in all Western Union locations."
- "The disclosed Solana contract address proves current circulating supply or
  mint/burn controls."

unless primary product or workflow documents support the exact statement.

Current safe wording:

> Western Union is attempting to use USDPT and a Digital Asset Network to build
> a regulated digital-asset settlement layer. The product page now supports
> broad reserve categories, 1:1 redeemability wording, an official Solana
> contract address, and planned / coming-soon select-market exchange, cash-out,
> card and receive-in-USDPT features. ADB's covered-stablecoin terms partially
> bound Client vs Non-Client redemption rights, reserve-trust structure,
> issuer/obligor role, brand-partner status and legal/control powers, but the
> archive does not yet prove USDPT-specific fee/user terms, USDPT-specific
> attestation, exact token-control implementation, agent balance-sheet
> treatment, displacement of SWIFT / correspondent banking / wholesale
> settlement systems, or full consumer-facing remittance workflow.

If a future primary document supports only one layer of the four-layer frame,
upgrade only that layer. For example, a mint / burn / freeze-control
disclosure would support token-control analysis, but would still not support
agent balance-sheet treatment or correspondent-banking displacement.

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
