# Executive Summary

Version: v0.3.2 evidence-base cleanup
Last updated: 2026-05-26

This document summarises the stablecoin ecosystem research project that
underpins the 2026-06-27 reading-group session. It is designed as a
one-page orientation before reading the chapter drafts and claim table.
Every substantive finding is anchored to one or more `CLAIM_XXX` entries
in `03_claim_tables/claim_table_master.csv`, which in turn cites a source
registered in `01_sources/source_registry.csv`.

## Scope

The project treats stablecoins as a structural question rather than a market
question. The unit of analysis is the system of issuers, reserves,
custodians, derivatives counterparties, payment-system participants, and
legal regimes through which a stablecoin liability is created, held,
transferred, redeemed, or wound down.

The project separates three product categories:

1. Fiat-backed payment stablecoins issued against bank deposits, short-dated
   Treasuries, Treasury repo, government money-market fund shares, and
   similar high-quality liquid assets.
2. Crypto / RWA-collateralised protocol stablecoins generated through
   governance-controlled smart-contract vaults and overcollateralised
   liquidation mechanics.
3. Synthetic-dollar stablecoins maintained through delta-neutral derivatives
   hedging and off-exchange custody of backing assets.

USDPT is treated separately. The archive supports the launch announcement,
issuer identity, Solana deployment, infrastructure partners, product-page
reserve categories, the official Solana contract address, and planned /
coming-soon select-market exchange, cash-out, card and receive-in-USDPT
features. Anchorage Digital Bank covered-stablecoin terms now partially
bound direct ADB redemption to Clients, distinguish Non-Clients, describe a
reserve trust and ADB sole-obligor role, and reserve legal/control powers. It
does not yet support USDPT-specific retail/user terms, fee schedule, a
USDPT-specific reserve attestation, exact token-control implementation, agent
balance-sheet treatment, or a full customer / agent / bank-settlement
workflow.

## Headline Findings

1. **Fiat-backed stablecoins are tokenised wrappers around dollar
   money-market and banking-system instruments.** USDC reserve evidence
   supports bank deposits, overnight reverse Treasury repo, sub-three-month
   Treasuries, and the Circle Reserve Fund (`CLAIM_026`, `CLAIM_027`). USDT
   evidence now includes the Q1 2026 reserve table, with Treasury bills,
   reverse repos, cash/bank deposits, precious metals, Bitcoin, public
   equities, other investments, and secured loans, so USDT should not be
   modelled as a pure cash equivalent (`CLAIM_152`). Paxos-family stablecoins
   and Gemini Dollar have more tightly specified reserve categories in their
   governing documentation (`CLAIM_075`, `CLAIM_078`).

2. **Direct redemption is contractual and gated.** USDC direct redemption
   requires a Circle Mint account in good standing (`CLAIM_058`), and Circle
   risk factors identify address-blocking, freezing and blacklisting-policy
   controls (`CLAIM_154`); USDT
   requires verified-customer status and excludes prohibited persons and
   jurisdictions (`CLAIM_060`, `CLAIM_061`); FDUSD requires an FD121 Account
   and excludes U.S. individuals (`CLAIM_062`, `CLAIM_064`); Paxos limits
   direct purchase and redemption of PYUSD, USDP, and USDG to Paxos Customers
   (`CLAIM_073`); Gemini restricts GUSD creation and redemption to Gemini
   Customers while expressly disclaiming a relationship with non-customers
   who obtain or use GUSD (`CLAIM_077`). USDe direct issuance and redemption
   are limited to whitelisted Mint Users (`CLAIM_065`, `CLAIM_066`).

3. **Reserve attestations are not financial-statement audits.** The research
   keeps CPA examinations, assurance reports, and statutory audit language
   separate. GENIUS requires monthly reserve disclosure with examination by
   a registered public accounting firm and CEO/CFO certification
   (`CLAIM_085`). MiCA adds monthly reserve disclosure and, for significant
   EMT issuers, a six-month audit cadence (`CLAIM_097`).

4. **The legal baseline is now multi-layered rather than single-statute.**
   GENIUS restricts issuance to permitted payment stablecoin issuers,
   defines permitted reserves, bans holder yield paid solely for holding,
   using, or retaining the stablecoin, and creates customer priority in
   issuer insolvency (`CLAIM_082`, `CLAIM_084` to `CLAIM_087`). MiCA keeps
   ART and EMT regimes separate, with ART reserve/redemption/no-interest
   obligations and EMT par redemption and disclosure duties
   (`CLAIM_069` to `CLAIM_071`, `CLAIM_094` to `CLAIM_097`,
   `CLAIM_122` to `CLAIM_129`). The BoE 2025 consultation proposes a
   sterling systemic-stablecoin regime with central-bank-deposit and gilt
   backing plus holding limits and cross-border home-authority treatment
   (`CLAIM_090`, `CLAIM_091`, `CLAIM_130`, `CLAIM_131`). NYDFS guidance
   remains central for GUSD and RLUSD (`CLAIM_036` to `CLAIM_040`).
   CLARITY is treated as a market-structure bill that defines permitted
   payment stablecoins and excludes them from several securities-law
   definitions while preserving specified SEC anti-fraud and market-
   integrity authority (`CLAIM_119` to `CLAIM_121`). GENIUS Section 18 now
   anchors the foreign-issuer screen: no foreign regime is treated as
   automatically equivalent; BoE and MiCA are comparison cases requiring a
   Treasury comparability determination, Comptroller registration, U.S.
   liquidity-reserve treatment, and lawful-order capability (`CLAIM_126`).

5. **Central-bank and IMF work frames stablecoin growth as a conditional
   transmission channel.** Federal Reserve and IMF sources emphasise that
   banking-system effects depend on inflow sources, reserve composition,
   and whether stablecoin issuers operate like two-tier money intermediaries
   or narrow banks (`CLAIM_048`, `CLAIM_049`). Payment-incumbent event-study
   evidence is treated as market-expectation evidence, not proof of realised
   stablecoin payment adoption (`CLAIM_050`). Taiwan CBC sources now support
   a bounded local synthesis: stablecoins are private tokenised money rather
   than legal tender, central-bank money remains the settlement anchor,
   USD stablecoins can create digital-dollarisation and FX-management risks,
   and an NTD stablecoin would likely be treated as a tightly reserved
   tokenised stored-value instrument with limited current monetary-policy
   effect (`CLAIM_112` to `CLAIM_118`).

6. **DAI/USDS and USDe should not be merged into fiat-backed payment
   stablecoin analysis.** Maker / Sky creates Dai or USDS through
   overcollateralised vaults, governance-approved collateral, liquidation
   auctions, and a protocol-surplus or MKR/SKY dilution backstop
   (`CLAIM_098`, `CLAIM_099`). USDe relies on delta-neutral short perpetual
   futures positions and off-exchange custody, with monthly custodian
   attestations and a separate Reserve Fund (`CLAIM_103` to `CLAIM_106`).

## Limitations And Open Questions

The research is not a complete final publication. The active open items are:

- USDPT-specific retail/user terms, fee schedule, USDPT-specific reserve
  attestation, exact token-control implementation beyond the disclosed Solana
  address, direct retail/agent redemption scope beyond ADB Client status,
  agent balance-sheet treatment, and end-to-end settlement workflow.
- Visa adjusted on-chain payment-volume export, Artemis reproducible export,
  Cambridge numerical export, and McKinsey / Artemis
  `MCKINSEY_ARTEMIS_001`. World Bank remittance-cost benchmark context is now
  reproducibly exported, but it is not adjusted stablecoin payment volume.
- Taiwan enacted statutory text and sub-rules if the draft VASP / stablecoin
  regime is later enacted or officially supplemented.
- Maker / DAI Black Thursday primary-source extraction, a usable Iron
  Finance price timeline, and higher-quality failure-case price/depeg data
  for exact duration/trough/recovery claims. Public hourly proxy timelines
  for USDC/SVB, Terra USTC and Maker DAI are now available.

## Method Commitments

- Attestation reports are not called audits unless the source supports that
  term for the relevant engagement.
- SWIFT is treated as a messaging layer, not a funds-settlement system.
- Raw on-chain transfer volume is not equated with realised payment demand.
- Fiat-backed payment stablecoins, protocol stablecoins, and synthetic-dollar
  instruments remain separate categories.
- MiCA ART and MiCA EMT rules remain separate.
- Unsupported questions stay open rather than being filled by inference.

The v0.4 claim table contains 154 entries (`CLAIM_001` through
`CLAIM_154`). The source registry contains 148 rows. Full Python validation
and portal build passed at 153 claims before the final `CLAIM_154` USDC
risk-factor addition; post-154 static checks confirm the `USDC_007` source row
and cross-document references, while Python validation / portal rerun is
pending in the current execution session.

## How To Read This Package

1. Start with `05_chapter_drafts/chapter_01_stablecoins_as_onchain_dollar_system.md`
   and `05_chapter_drafts/chapter_09_conclusion.md`.
2. Use `05_chapter_drafts/chapter_02_issuer_comparison.md` for issuer-level
   evidence and `05_chapter_drafts/chapter_04_law_and_regulation.md` for
   the cross-jurisdiction comparison.
3. Treat `03_claim_tables/claim_table_master.csv` as the traceability layer
   for every material assertion.
4. Use `07_final_report/slide_script_v0_3.md` and
   `07_final_report/slide_outline_v0_3.md` as the presentation package.
