# Chapter 7 - On-chain Data and Payment Demand

Working status: partially upgraded after deficiency-source recovery and v0.4
data-export work.
This chapter is **not** ready to support final quantitative conclusions
about realised payment demand. Adjusted-volume exports and methodology
reconciliation between data providers are still incomplete. The chapter's
contribution at v0.4 is therefore a **methodology guardrail, a data-source
map, and an off-chain remittance-cost benchmark**, not a payment-adoption
study.

## Core methodological position

Raw on-chain transfer volume is not the same as payment demand. The same
issuance, the same transfer, and the same dashboard row can reflect very
different economic activities:

- **Raw transfer volume** — every value-moving transaction on chain, including
  exchange deposits, internal CEX wallet sweeps, market-maker rebalancing,
  bridge transfers, and MEV-driven re-routing.
- **Adjusted transfer volume** — a provider-specific filtered series that
  attempts to exclude exchange-internal moves, bridge moves, MEV/arbitrage,
  and round-trips between addresses controlled by the same entity.
- **Exchange / liquidity movement** — transfers tied to centralised-exchange
  deposits, withdrawals, and inter-exchange flow.
- **DeFi activity** — protocol interactions on DEXs, lending, and money
  markets.
- **Bridge movement** — cross-chain canonical and wrapped transfers.
- **MEV / arbitrage** — high-frequency value movement that is structurally
  not payment.
- **Real-world payment demand** — consumer remittance, merchant settlement,
  business B2B settlement, treasury operations.

The final report must not collapse these categories. Treating any one
data-provider's "stablecoin volume" headline as evidence of payment adoption
is a category error this chapter is designed to prevent.

## The data-source landscape

Four major external providers and one off-chain benchmark are currently
registered in `01_sources/source_registry.csv`. The table below is a research
map, not a quality ranking:

| Provider | What it primarily measures | Adjusted-volume series? | Source IDs | Reproducible export here? |
| --- | --- | --- | --- | --- |
| DeFiLlama | Supply, market cap, chain distribution | No | `DEFILLAMA_001`, `DEFILLAMA_002` | Yes — `09_data_exports/stablecoin_supply/` |
| Visa Onchain Analytics | Stablecoin transactions and volume dashboards | Yes (methodology not yet extracted) | `VISA_001`, `VISA_002` | No — dynamic dashboard shells only |
| Cambridge Digital Money Dashboard | Cross-protocol digital-money activity | Methodology page archived | `CAMBRIDGE_001`, `CAMBRIDGE_002` | No |
| Artemis | Transfer volume, transactions, supply, addresses across 18+ chains with `None`, `ARTEMIS`, `P2P` filters | Yes (filter framework documented) | `ARTEMIS_001`, `ARTEMIS_003` | No |
| World Bank remittance cost indicator | Off-chain remittance-cost benchmark | N/A - off-chain benchmark | `WB_RPW_001`, `WB_RPW_002` | Yes - `09_data_exports/remittance_benchmark/` |
| McKinsey / Artemis joint piece | Adjusted-volume methodology essay | Yes | `MCKINSEY_ARTEMIS_001` | Status: `manual_needed` |

Two observations follow:

1. The only adjusted-volume series whose filter framework is documented at
   claim level is Artemis (`CLAIM_054`), which describes its `None`,
   `ARTEMIS`, and `P2P` filters. Visa's adjusted methodology is referenced
   on the dashboard but not yet extracted into a claim.
2. The reproducible exports currently in this repo are the DeFiLlama
   supply and chain-distribution layer (`CLAIM_055`) and the World Bank
   remittance-cost benchmark (`CLAIM_147`). The DeFiLlama layer is supply
   evidence, while the World Bank layer is off-chain cost context; neither is
   adjusted stablecoin payment-volume evidence.

## What each source can support

- **DeFiLlama** supports total supply, supply by issuer, and supply by chain.
  It does **not** support payment-demand conclusions; supply growth can come
  from CEX deposits, DeFi collateral migration, or speculative holding as
  easily as from payment use.
- **Visa Onchain Analytics** supports a methodology-anchored adjusted-volume
  framing once the dashboard methodology is extracted and the chart can be
  exported reproducibly. The Visa/Allium "Making sense of stablecoins"
  analysis behind the dashboard publishes a headline magnitude: applying a
  heuristic that removes inorganic data adjusts trailing-30-day transfer
  volume from about US$2.65 trillion to about US$265 billion, roughly a
  tenfold reduction (`CLAIM_157`). Use that figure as a published,
  order-of-magnitude illustration that raw transfer volume overstates organic
  activity; it is a trailing-window provider number, not a fixed-date metric
  or a reproducible local export, so until the dashboard methodology and a
  chart export are captured, treat the rest as dashboard provenance only.
- **Cambridge Digital Money Dashboard** supports cross-source triangulation
  once its methodology is extracted.
- **Artemis** supports filtered transfer-volume analysis at the chain and
  filter level (`CLAIM_054`), but the project does not yet have a
  reproducible Artemis export.
- **World Bank remittance cost benchmark** supports **off-chain** remittance
  cost context. The v0.4 export uses WDI API indicator `SI.RMT.COST.IB.ZS`
  and writes a 17,556-row country/region-year CSV plus a 104-row latest
  non-null benchmark file (`CLAIM_147`). Use it only as a cost comparator,
  never as direct stablecoin usage evidence.

## Reproducible exports currently shipped

The data-export layer now ships reproducible local workflows:

- `09_data_exports/scripts/build_defillama_exports.py`
- `09_data_exports/notebooks/stablecoin_market_data_workflow.ipynb`
- `09_data_exports/stablecoin_supply/defillama_stablecoin_supply_snapshot.csv`
- `09_data_exports/stablecoin_supply/defillama_stablecoin_chain_distribution.csv`
- `09_data_exports/scripts/build_worldbank_remittance_benchmark.py`
- `09_data_exports/remittance_benchmark/worldbank_si_rmt_cost_ib_zs_raw.json`
- `09_data_exports/remittance_benchmark/worldbank_remittance_cost_by_country_year.csv`
- `09_data_exports/remittance_benchmark/worldbank_remittance_cost_latest_by_country.csv`
- `09_data_exports/data_manifest.csv`

The DeFiLlama outputs are **supply and chain-distribution evidence only** and
should be cited together with `CLAIM_055`. The World Bank outputs are
**off-chain remittance-cost benchmark evidence only** and should be cited
together with `CLAIM_147`. The folder README (`09_data_exports/README.md`)
carries the standing warning not to use either export for stablecoin
payment-demand claims.

## Claims explicitly **not** supported in this build

The current evidence base does not support the following statements at any
confidence level above narrative speculation, and they must therefore stay
out of the final report unless adjusted-volume exports become available:

- "X percent of stablecoin transfers are real payments."
- "Stablecoins have replaced remittances in corridor Y."
- "Stablecoin payment volume exceeds Visa / Mastercard / Western Union
  volume in any settled comparable sense."
- "Onchain volume growth implies merchant adoption growth."

Each of these statements requires a paired (i) adjusted-volume methodology
that is cited and reproducible and (ii) a comparable off-chain benchmark
with matching definitions and time windows. The project now has an off-chain
World Bank cost benchmark, but still lacks the adjusted stablecoin
payment-volume side of the comparison.

## Open methodology questions

- Whether Visa's adjusted-volume filter is methodologically comparable to
  Artemis' `ARTEMIS` filter or to Cambridge's adjusted series, or whether
  each provider defines "real payments" differently.
- Whether stablecoin supply growth at the issuer or chain level correlates
  with any adjusted-volume series in a stable way.
- Whether bridged stablecoin supply is double-counted across chains, and
  whether DeFiLlama's chain-distribution series reflects supply or transit.
- Whether off-chain remittance benchmarks (World Bank RPW) and stablecoin
  corridor flows can be brought to a comparable unit (per-corridor USD
  volume by month) for any single corridor.

## Chapter limitations

- Four claims (`CLAIM_054`, `CLAIM_055`, `CLAIM_147`, `CLAIM_157`) anchor this
  chapter.
  Quantitative inference about stablecoin payment demand is still
  deliberately excluded.
- Visa Onchain Analytics, Cambridge, and Artemis dashboards are archived as
  shells; their adjusted-volume series are not reproducible from this repo.
- `MCKINSEY_ARTEMIS_001` is `manual_needed` and remains unfetched.
- World Bank remittance-cost benchmark data is now reproducibly exported, but
  stablecoin corridor-flow data is not. Corridor-level stablecoin-versus-RPW
  comparisons are therefore still not possible.
- AGENTS.md rule 5 is the load-bearing red line here: do not equate raw
  on-chain transfer volume with real payment volume.

## Next extraction tasks

- Obtain or export reproducible Visa adjusted-volume data along with
  methodology notes.
- Extract Cambridge methodology and identify whether its adjusted series
  is definition-compatible with Artemis or Visa.
- Resolve `MCKINSEY_ARTEMIS_001` to capture the McKinsey/Artemis adjusted
  methodology essay.
- Add a single common-definition table that records, for each provider,
  what counts as "payment" and what is excluded, so the report can compare
  series like-for-like rather than headline-to-headline.
- If corridor-level RPW pricing is needed beyond the WDI benchmark indicator,
  obtain or manually download the full RPW Excel dataset and document the
  transformation separately.
