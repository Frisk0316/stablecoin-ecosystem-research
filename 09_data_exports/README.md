# Data Exports

This folder holds reproducible data exports used by Chapter 7. Dashboard HTML
is not enough for quantitative claims; every output here should record the
source ID, input path, transformation method, limitations, and output path.

## Current Status

Available now:

- `stablecoin_supply/defillama_stablecoin_supply_snapshot.csv`
- `stablecoin_supply/defillama_stablecoin_chain_distribution.csv`
- `data_manifest.csv`
- `notebooks/stablecoin_market_data_workflow.ipynb`
- `scripts/build_defillama_exports.py`
- `remittance_benchmark/worldbank_remittance_cost_by_country_year.csv`
- `remittance_benchmark/worldbank_remittance_cost_latest_by_country.csv`
- `remittance_benchmark/worldbank_si_rmt_cost_ib_zs_raw.json`
- `failure_case_timelines/cryptocompare_failure_case_hourly_prices.csv`
- `failure_case_timelines/cryptocompare_failure_case_summary.csv`
- `failure_case_timelines/cryptocompare_failure_case_histohour_raw.json`
- `issuer_details/usdt_q1_2026_reserve_breakdown.csv`
- `scripts/build_worldbank_remittance_benchmark.py`
- `scripts/build_failure_case_price_timelines.py`
- `scripts/build_usdt_q1_2026_reserve_breakdown.py`

These outputs are based on local archived DeFiLlama JSON snapshots
(`DEFILLAMA_001`, `DEFILLAMA_002`). They support supply and chain-distribution
analysis only. They do not support adjusted payment-volume conclusions.

The World Bank outputs are based on WDI API indicator `SI.RMT.COST.IB.ZS`
(`WB_RPW_002`). They support off-chain remittance-cost benchmark context:
the full CSV has 17,556 country/region-year rows and the latest non-null CSV
has 104 rows. They do not support stablecoin adjusted payment-volume,
merchant-adoption or remittance-displacement conclusions.

The CryptoCompare outputs are public hourly OHLCV proxy timelines for selected
failure windows (`CRYPTOCOMPARE_001`). They provide 749 hourly rows and a
5-row summary table. USDC/SVB, Terra USTC and Maker DAI have usable public
hourly proxy rows; IRON and TITAN are zero-only in the public API output and
should not be used as Iron Finance price timelines.

The USDT issuer-detail output is a local PDF extraction from `USDT_002`. It
exports the Q1 2026 "Assets at 31 March 2026" reserve breakdown table into a
12-row CSV with amount and share-of-total-assets fields. It is point-in-time
reserve composition evidence only, not a financial-statement audit or live
reserve monitor.

`data_manifest.csv` intentionally lists only reproducible outputs that exist
in this repository. Missing dashboards or manual-download items are tracked
below and in `00_project_management/unresolved_open_questions.md`; they should
not be added to the manifest until a local, rebuildable output exists.

Still missing:

- Visa Onchain Analytics adjusted-volume export.
- Artemis reproducible export beyond methodology documentation.
- Cambridge Digital Money Dashboard numerical export.
- McKinsey/Artemis article local archive (`MCKINSEY_ARTEMIS_001`).

Current interpretation:

- Available DeFiLlama exports support market-structure, issuer-scale and
  chain-distribution discussion.
- They do not support adjusted transfer volume, merchant payment adoption,
  remittance displacement, or stablecoin-versus-card-network comparisons.
- Any future adjusted-volume export must ship with the input file, method,
  provider filter definition, limitations, and comparable off-chain benchmark
  notes before it is used in chapter 7.

## Rebuild

Run from repository root:

```powershell
& 'C:\Users\woody\AppData\Local\Programs\Python\Python312\python.exe' 09_data_exports\scripts\build_defillama_exports.py
& 'C:\Users\woody\AppData\Local\Programs\Python\Python312\python.exe' 09_data_exports\scripts\build_worldbank_remittance_benchmark.py
& 'C:\Users\woody\AppData\Local\Programs\Python\Python312\python.exe' 09_data_exports\scripts\build_failure_case_price_timelines.py
& 'C:\Users\woody\AppData\Local\Programs\Python\Python312\python.exe' 09_data_exports\scripts\build_usdt_q1_2026_reserve_breakdown.py
```

## Guardrail

Do not use these files to claim real-world payment demand. DeFiLlama supply
data is useful for market structure, issuer scale, and chain distribution.
World Bank remittance-cost data is useful as an off-chain cost benchmark.
CryptoCompare failure-case timelines are useful as coarse public hourly proxy
data. None of these exports is adjusted stablecoin payment activity, and the
CryptoCompare failure outputs are not paid tick-level or exchange-level data.
The USDT issuer-detail export is useful for reserve-composition comparison
only; it should not be described as an audit or as evidence of reserve
composition at any time other than 2026-03-31 23:59 UTC.
