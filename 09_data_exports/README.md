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

These outputs are based on local archived DeFiLlama JSON snapshots
(`DEFILLAMA_001`, `DEFILLAMA_002`). They support supply and chain-distribution
analysis only. They do not support adjusted payment-volume conclusions.

`data_manifest.csv` intentionally lists only reproducible outputs that exist
in this repository. Missing dashboards or manual-download items are tracked
below and in `00_project_management/unresolved_open_questions.md`; they should
not be added to the manifest until a local, rebuildable output exists.

Still missing:

- Visa Onchain Analytics adjusted-volume export.
- Artemis reproducible export beyond methodology documentation.
- Cambridge Digital Money Dashboard numerical export.
- World Bank remittance-cost benchmark export.
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
```

## Guardrail

Do not use these files to claim real-world payment demand. DeFiLlama supply
data is useful for market structure, issuer scale, and chain distribution, but
not for adjusted payment activity.
