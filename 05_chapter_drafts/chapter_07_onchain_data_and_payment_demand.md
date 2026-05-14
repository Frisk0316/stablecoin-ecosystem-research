# Chapter 7 - On-chain Data and Payment Demand

Working status: partially upgraded after deficiency-source recovery. This
chapter is still not ready for final quantitative conclusions because adjusted
exports and methodology reconciliation are incomplete.

## Core Principle

Raw transfer volume, adjusted transfer volume, exchange/liquidity movement,
DeFi activity, bridge movement, MEV/arbitrage, and real-world payment demand
must be separated. The report should not treat stablecoin supply or raw
on-chain transfers as direct evidence of consumer or merchant payment usage.

## Sources Now Registered

- Visa Onchain Analytics dashboard shells are archived and can support
  dashboard provenance and methodology follow-up, but not yet a reproducible
  export.
- DeFiLlama API snapshots are archived and support supply/market-cap style
  analysis; they are not adjusted payment-volume evidence by themselves
  (`CLAIM_055`).
- Cambridge Digital Money Dashboard pages are archived for triangulation, but
  still need extraction.
- Artemis report/docs are archived. Artemis' Snowflake schema supports
  stablecoin transfer volume, transactions, supply, and address-level metrics
  across more than 18 chains, with filters such as `None`, `ARTEMIS`, and
  `P2P` (`CLAIM_054`).
- McKinsey/Artemis material remains a manual-needed item because the page could
  not be fully archived through the command-line fetch route.

## Current Interpretation

The available evidence can support a data-source map and a methodology warning.
It cannot yet support precise claims such as "X% of stablecoin activity is real
payments" or "stablecoins have replaced remittances" unless those claims are
paired with a specific adjusted-volume methodology and export.

## Next Extraction Tasks

- Obtain or export reproducible Visa adjusted-volume data.
- Normalize DeFiLlama supply by issuer, chain, and date, then separate supply
  from transaction demand.
- Extract Cambridge and Artemis methodology notes and identify whether their
  definitions are comparable.
- Add World Bank remittance data only as an off-chain benchmark, not as direct
  stablecoin usage evidence.
