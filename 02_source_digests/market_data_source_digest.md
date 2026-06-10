# Market and On-chain Data Source Digest v0.2

The deficiency-source pass moved this module from empty placeholder to partial
source coverage. The project now has archived sources for Visa, DeFiLlama,
Cambridge CCAF, and Artemis, plus reproducible World Bank remittance-cost
benchmark and CryptoCompare failure-case timeline exports, but the evidence is
still uneven.

## Available Sources

- `VISA_001` and `VISA_002`: dynamic dashboard shells for Visa Onchain
  Analytics and its transactions page. These should not yet be treated as
  quantitative exports.
- `VISA_ALLIUM_001`: Allium/Visa "Making sense of stablecoins" article behind
  the dashboard. It publishes a headline adjustment ratio - trailing-30-day
  stablecoin transfer volume of ~US$2.65T raw vs ~US$265B adjusted after a
  heuristic that removes inorganic data, roughly a tenfold reduction
  (`CLAIM_157`). Use as a published, order-of-magnitude illustration of the
  raw-vs-adjusted gap, not as a fixed-date metric or reproducible export; the
  full per-filter thresholds and numbers stay on the dynamic dashboard.
- `DEFILLAMA_001` and `DEFILLAMA_002`: local JSON API snapshots for stablecoin
  supply/price and stablecoin chain distribution. These support supply and
  chain-distribution analysis, not payment-volume conclusions (`CLAIM_055`).
- `CAMBRIDGE_001` and `CAMBRIDGE_002`: Cambridge Digital Money Dashboard shell
  and about/methodology page.
- `ARTEMIS_001` and `ARTEMIS_003`: Artemis stablecoin payments report and
  stablecoin metrics documentation. The docs describe transfer volume,
  transactions, supply, and address-level data across chains with None,
  ARTEMIS, and P2P filters (`CLAIM_054`).
- `WB_RPW_002`: World Bank WDI API indicator `SI.RMT.COST.IB.ZS`, cached as
  raw JSON and exported to CSV under `09_data_exports/remittance_benchmark/`.
  This supports off-chain remittance-cost benchmark context only
  (`CLAIM_147`).
- `CRYPTOCOMPARE_001`: CryptoCompare public `histohour` API cache for selected
  failure-case windows, exported under `09_data_exports/failure_case_timelines/`.
  This supports coarse public hourly proxy timelines for USDC/SVB, Terra USTC
  and Maker DAI, while the IRON/TITAN rows are zero-only and not usable as Iron
  Finance price timelines (`CLAIM_148`, `CLAIM_149`).
- `MCKINSEY_ARTEMIS_001`: still manual-needed because command-line fetch
  timed out, although the page was reachable in a browser/web view.

## Interpretation Guardrail

The final report must still not equate raw transfer volume, supply, dashboard
activity, or chain distribution with real payment demand. The Visa/Allium
~US$2.65T-to-~US$265B adjustment (`CLAIM_157`) is now usable as a published
order-of-magnitude illustration that raw transfer volume overstates organic
activity, but it is a trailing-window provider figure, not a reproducible local
export. Current local data is enough to start supply/chain, off-chain
remittance-cost benchmark, failure-case proxy-timeline and methodology work,
but final stablecoin payment-demand claims still require adjusted-volume
exports, dashboard screenshots, or a reproducible data pull with access dates.

## Data Exports

The data-export layer adds reproducible local workflows under
`09_data_exports/`. The script
`09_data_exports/scripts/build_defillama_exports.py` converts archived
DeFiLlama JSON snapshots into:

- `09_data_exports/stablecoin_supply/defillama_stablecoin_supply_snapshot.csv`
- `09_data_exports/stablecoin_supply/defillama_stablecoin_chain_distribution.csv`

The script `09_data_exports/scripts/build_worldbank_remittance_benchmark.py`
downloads the World Bank API indicator and writes:

- `09_data_exports/remittance_benchmark/worldbank_si_rmt_cost_ib_zs_raw.json`
- `09_data_exports/remittance_benchmark/worldbank_remittance_cost_by_country_year.csv`
- `09_data_exports/remittance_benchmark/worldbank_remittance_cost_latest_by_country.csv`
- `09_data_exports/scripts/build_failure_case_price_timelines.py`
- `09_data_exports/failure_case_timelines/cryptocompare_failure_case_histohour_raw.json`
- `09_data_exports/failure_case_timelines/cryptocompare_failure_case_hourly_prices.csv`
- `09_data_exports/failure_case_timelines/cryptocompare_failure_case_summary.csv`
- `09_data_exports/data_manifest.csv`

The DeFiLlama outputs remain supply and chain-distribution evidence only. The
World Bank outputs are off-chain remittance-cost benchmark evidence only.
CryptoCompare outputs are public hourly proxy failure-case evidence only. Cite
them together with `CLAIM_055`, `CLAIM_147`, `CLAIM_148`, `CLAIM_149`, and the
data-manifest limitations, not as payment-volume evidence.
