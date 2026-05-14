# Unresolved Open Questions

Last updated: 2026-05-14 (v0.2 interim refresh)

This file preserves questions that should not be guessed in the final report.
If a question is answered, add the supporting claim IDs and source IDs before
removing it. v0.2 interim pass closed the Paxos-family direct redemption
(PYUSD/USDP/USDG), GUSD platform-versus-lawful-holder distinction, USDP
monthly reserve report status, and the six GENIUS Act statutory anchors;
USDPT and adjusted-volume market-data items are deliberately deferred to
v0.3 per user decision.

## v0.2 deferrals (frozen for this pass, not unresolved-pending-research)

These items have been deliberately deferred for v0.2 and are not active
research questions during this pass:

1. USDPT product terms, reserve report, contract addresses, and end-to-end
   four-layer settlement workflow remain absent from primary documentation.
   No further extraction or scraping in v0.2 per scope decision; chapter 6
   conclusions must remain conditional. Move to v0.3 when WU/Anchorage
   publish primary product documentation.
2. Visa Onchain Analytics adjusted-volume export, Artemis methodology
   beyond `CLAIM_054`, and McKinsey/Artemis `MCKINSEY_ARTEMIS_001`
   (manual_needed) are frozen at current evidence; chapter 7 retains the
   "raw on-chain volume ≠ payment volume" guardrail. Move to v0.3 only if
   the corresponding reproducible exports become available.

## v0.3 backlog (next pass)

- BoE systemic stablecoin regime page-level extraction from `BOE_003` and
  `BOE_004`.
- ESMA MiCA / CASP guidance page-level extraction from `ESMA_002` and
  `ESMA_003`.
- MiCA significant-ART and significant-EMT obligations, and ART
  recovery/redemption plan provisions.
- CLARITY Act stablecoin-relevant sections (if any) isolated from
  market-structure provisions.
- Federal Reserve / IMF Taiwan-specific synthesis beyond `CLAIM_044` to
  `CLAIM_050` page-level anchors.
- DAI/USDS protocol mechanics: RWA collateral, PSM, savings/yield,
  governance, oracle, liquidation, legal/custody.
- USDe risk extraction: custodian attestations, exchange exposure,
  basis/funding risk, reserve fund composition, liquidity unwind.

## External source gaps

1. NYDFS Guidance on the Issuance of U.S. Dollar-Backed Stablecoins is now
   registered as `NYDFS_001`, locally archived, and partially extracted. The
   remaining task is page-level citation cleanup before final publication.
2. MiCA Regulation (EU) 2023/1114 is now registered as `MICA_004` and locally
   archived as an official PDF. Direct EUR-Lex HTML fetch remains blocked by an
   anti-bot challenge, so final citations should use the archived PDF unless a
   clean HTML export is later obtained.
3. IMF and Federal Reserve stablecoin sources are now registered and partially
   extracted into `CLAIM_044` to `CLAIM_050`. Remaining work is page-level
   extraction and Taiwan-specific synthesis.
4. On-chain market dashboards are partially ingested: Visa dashboard shells,
   DeFiLlama APIs, Cambridge pages, and Artemis report/docs are archived.
   Adjusted exports and methodology reconciliation are still needed to separate
   payment activity from raw transfer volume.
5. USDPT / UDSPT launch/product evidence is now partially captured
   (`CLAIM_051` to `CLAIM_053`). Missing items remain product terms, reserve
   report, contract addresses, direct redemption terms, and end-to-end workflow
   documentation.
6. McKinsey/Artemis material remains a manual-needed item because command-line
   archival timed out or failed.

## Issuer-specific questions

### USDC

- Circle transparency evidence now supports reserve categories and the broad
  1:1 redemption statement (`CLAIM_026`, `CLAIM_027`). Circle terms now
  establish that direct redemption requires a Circle Mint account in good
  standing, and transferred holders can redeem only if eligible for and
  registered with Circle Mint (`CLAIM_058`). Remaining question: map Circle
  Mint eligibility and any region-specific limits.
- Circle terms now state holders are not entitled to reserve interest/returns
  and USDC itself does not generate holder yield (`CLAIM_059`).
- Circle Reserve Fund documentation should be extracted to separate direct
  Treasuries, repo, MMF shares, and bank deposits.

### USDT

- Tether's May 1, 2026 release supports approximate Treasury bill, gold, and
  Bitcoin figures (`CLAIM_028`, `CLAIM_029`), but the full Q1 2026 reserve
  table in `USDT_002` still needs extraction.
- Tether terms now establish that direct issuance/redemption requires verified
  customer status and that redemption is a personal contractual right
  (`CLAIM_060`). Remaining question: extract exact fee/minimum timing and any
  operational delays.
- Tether terms define prohibited persons/jurisdictions, including U.S. persons
  except limited discretionary Eligible Contract Participant acceptance,
  Canadian/Singaporean persons, sanctioned persons, and prohibited
  jurisdictions (`CLAIM_061`).
- Tether International / El Salvador registration and any GENIUS-compliant
  USAT structure should be separated from USDT before making U.S. regulatory
  claims.

### PYUSD / USDP / USDG

- Paxos USD Stablecoin Agreement now resolves entity allocation,
  direct-redemption gating, no-holder-yield, reserve composition, and
  all-holders freeze/upgrade scope for the Paxos family (`CLAIM_072` to
  `CLAIM_076`); these subsume the earlier general restriction claim
  (`CLAIM_056`).
- PYUSD: PayPal Hub eligibility (`CLAIM_031`) and Paxos direct redemption
  (`CLAIM_073`) are now described as two layered channels in chapter 2.
  Remaining question: end-to-end mapping between PayPal Digital transition
  (`CLAIM_030`) and Paxos Customer onboarding when a retail PayPal user
  attempts direct Paxos redemption.
- USDP: monthly reserve composition reports have been formally discontinued
  by the issuer (`CLAIM_081`); USDP attestations are issued monthly by KPMG
  LLP under AICPA examination/attestation standards (`CLAIM_080`).
  Reclassify the earlier "USDP monthly reserve report PDF is absent" gap
  from "missing" to "discontinued by issuer".
- USDG: EU retail USDG redemption route conditions (`CLAIM_068`) and unified
  Paxos Customer-only direct redemption (`CLAIM_073`) are captured.
  Remaining question: non-EU institutional and direct-Paxos-Customer USDG
  workflows beyond the EU retail route, plus any USDG-specific reserve
  report distinct from the unified Paxos disclosure.

### RLUSD / GUSD

- RLUSD product-page reserve and custody statements are now captured
  (`CLAIM_032`, `CLAIM_033`), and Ripple user terms now support prohibited-use
  and suspension/termination consequences (`CLAIM_057`). Direct redeemer
  eligibility and any contract-level freeze/blacklist powers still need
  separate extraction (carry to v0.3).
- GUSD: Gemini Trust User Agreement now resolves the platform-versus-
  lawful-holder distinction at the contractual layer (`CLAIM_077`),
  enumerates the three-account-type reserve structure (`CLAIM_078`), and
  defines the one-Business-Day "Timely" redemption commitment for Customer
  sell Orders (`CLAIM_079`). Remaining question: smart-contract-level
  freeze/blacklist specifics and the interaction between NYDFS guidance
  obligations and Gemini's contractual customer-only redemption gating.

### FDUSD

- FDUSD terms now support claim-level extraction for redemption/sale rights,
  eligible redeemers, FD121 Account gating, suspension/limitation mechanics,
  and U.S. person exclusion (`CLAIM_062`, `CLAIM_063`, `CLAIM_064`).
  Remaining question: map the relationship among FD121 (BVI) Limited, Hong
  Kong trust/custody arrangements, and reserve-account banks.

### DAI / USDS

- MCD core mechanics (overcollateralised Maker Vaults, governance, Stability
  Fee and Liquidation Ratio risk parameters), liquidation auctions
  (Collateral Auction + Reverse Collateral Auction + Protocol Surplus / MKR
  dilution backstop), Dai Savings Rate / Sky Savings Rate via sUSDS, and
  the three external-actor classes (Keepers, Oracles, Global Settlers /
  Emergency Oracles) are now anchored at `CLAIM_098`-`CLAIM_101`.
- Sky.money rebrand mapping (USDS / sUSDS / stUSDS / SKY plus 1:1 USDC↔USDS
  conversion and US-jurisdiction unavailability of yield modules) is
  anchored at `CLAIM_102`.
- Keep DAI/USDS categorised as crypto/RWA-collateralised protocol
  stablecoins, not fiat-backed payment stablecoins.
- Remaining open question: RWA Vaults inventory, Peg Stability Module
  contract-level mechanics, and the precise relationship between USDS,
  sUSDS, stUSDS and the legacy DAI token are not yet extracted at
  contract or governance-vote level.
- Data-quality finding: `DAI_USDS_003` (registered as "Sky Protocol
  technical whitepaper 2025") is in fact a Cardano Layer 2 data
  availability paper unrelated to the Maker/Sky stablecoin protocol — it
  has not been used to support any claim and the registry row should be
  relabelled or removed in v0.4.

### USDe

- Distinguish USDe from sUSDe before discussing yield.
- Ethena terms now establish the Mint User / Holding User distinction,
  direct redemption gating, U.S. Mint User ineligibility, and no USDe
  holder yield (`CLAIM_065`, `CLAIM_066`). Ethena overview supports the
  synthetic-dollar and delta-neutral framing (`CLAIM_067`).
- v0.3 protocol-mechanics extraction now anchors the peg-stability layer.
  Delta-neutral hedging at 1:1 collateralisation via short perpetual
  futures positions of approximately the same notional as the backing
  asset (`CLAIM_103`); Off-Exchange Settlement custody mitigating but not
  eliminating exchange-specific counterparty risk (`CLAIM_104`); monthly
  custodian attestations validating existence/control/value of backing
  assets and stating none reside directly on exchange partners
  (`CLAIM_105`); Reserve Fund composition (USDC + USDT + smaller ETH
  allocation), 4/10 multi-sig control, and Q4 2024 size US$46.6m
  (`CLAIM_106`).
- Remaining open question: live exchange-by-exchange exposure breakdown,
  basis trade scenario analysis, and sustainability of sUSDe APY (19%
  average in 2024) under sustained negative-funding regimes.

### USDPT / UDSPT

- Confirm whether the product name is USDPT or UDSPT in primary launch
  documents.
- Confirm reserve trust, reserve report, contract addresses, and redemption
  terms. Issuer and launch framing now have primary-source support
  (`CLAIM_051`, `CLAIM_052`).
- Do not assume Western Union agents handle retail stablecoin cash-out unless
  product documentation supports it.
- Do not frame USDPT as replacing SWIFT or correspondent banking until the
  actual settlement workflow is documented.
