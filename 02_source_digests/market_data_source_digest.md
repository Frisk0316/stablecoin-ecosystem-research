# Market and On-chain Data Source Digest v0.2

The deficiency-source pass moved this module from empty placeholder to partial
source coverage. The project now has archived sources for Visa, DeFiLlama,
Cambridge CCAF, and Artemis, but the evidence is still uneven.

## Available Sources

- `VISA_001` and `VISA_002`: dynamic dashboard shells for Visa Onchain
  Analytics and its transactions page. These should not yet be treated as
  quantitative exports.
- `DEFILLAMA_001` and `DEFILLAMA_002`: local JSON API snapshots for stablecoin
  supply/price and stablecoin chain distribution. These support supply and
  chain-distribution analysis, not payment-volume conclusions (`CLAIM_055`).
- `CAMBRIDGE_001` and `CAMBRIDGE_002`: Cambridge Digital Money Dashboard shell
  and about/methodology page.
- `ARTEMIS_001` and `ARTEMIS_003`: Artemis stablecoin payments report and
  stablecoin metrics documentation. The docs describe transfer volume,
  transactions, supply, and address-level data across chains with None,
  ARTEMIS, and P2P filters (`CLAIM_054`).
- `MCKINSEY_ARTEMIS_001`: still manual-needed because command-line fetch
  timed out, although the page was reachable in a browser/web view.

## Interpretation Guardrail

The final report must still not equate raw transfer volume, supply, dashboard
activity, or chain distribution with real payment demand. Current local data is
enough to start supply/chain and methodology work, but final payment-demand
claims still require adjusted-volume exports, dashboard screenshots, or a
reproducible data pull with access dates.

## Data Exports

The v0.2 data-export pass adds a reproducible local workflow under
`09_data_exports/`. The script
`09_data_exports/scripts/build_defillama_exports.py` converts archived
DeFiLlama JSON snapshots into:

- `09_data_exports/stablecoin_supply/defillama_stablecoin_supply_snapshot.csv`
- `09_data_exports/stablecoin_supply/defillama_stablecoin_chain_distribution.csv`
- `09_data_exports/data_manifest.csv`

These outputs remain supply and chain-distribution evidence only. They should
be cited together with `CLAIM_055` and the data-manifest limitations, not as
payment-volume evidence.
