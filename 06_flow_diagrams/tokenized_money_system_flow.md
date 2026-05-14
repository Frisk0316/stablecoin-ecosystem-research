# Tokenized Money System Flow

Updated 2026-05-15 (v0.3): redrawn to reflect the three product categories
the report sustains throughout (chapter 1.3) and the regulatory perimeter
under GENIUS Act, MiCA, BoE, and NYDFS.

```mermaid
flowchart TD
    subgraph CB["Central-bank money layer"]
        Reserves[Central bank reserves]
        CBDC["CBDC / wholesale tokenised central-bank money"]
    end

    subgraph Bank["Commercial-bank money layer"]
        Deposits[Commercial bank deposits]
        DepTokens[Deposit tokens]
    end

    subgraph FiatBacked["Fiat-backed payment stablecoins (in regulatory perimeter)"]
        F1["USDC / USDT / PYUSD / USDP /<br/>USDG / RLUSD / FDUSD / GUSD"]
        F2["Regulated under one or more of:<br/>GENIUS Act (CLAIM_082-087)<br/>MiCA EMT (CLAIM_042-043, CLAIM_097)<br/>BoE systemic (CLAIM_088-091)<br/>NYDFS (CLAIM_036-040)"]
    end

    subgraph CryptoColl["Crypto / RWA-collateralised stablecoins (outside payment-stablecoin perimeter)"]
        C1["DAI / USDS<br/>Maker / Sky Protocol"]
        C2["Over-collateralisation via Maker Vaults<br/>(CLAIM_098-102)"]
    end

    subgraph Synthetic["Synthetic-dollar instruments (outside payment-stablecoin perimeter)"]
        S1["USDe / Ethena Labs"]
        S2["1:1 collateralised + delta-neutral perp hedge<br/>off-exchange custody<br/>(CLAIM_103-106)"]
    end

    Reserves --> Deposits
    Reserves --> CBDC
    Deposits --> DepTokens

    Deposits -. reserve channel: bank deposits + T-bills + repo + MMF .-> F1
    Reserves -. BoE 40-95%% proposed CBD backing .-> F1

    DepTokens --> Use[Tokenised payments / DeFi / settlement use cases]
    CBDC --> Use
    F1 --> Use
    C1 --> Use
    S1 --> Use
```

## Notes

- The diagram preserves the three product categories established in
  chapter 1.3. They share the on-chain transfer layer but enter the money
  system through different channels.
- Fiat-backed payment stablecoins are the only category fully inside the
  GENIUS Act / MiCA EMT / BoE systemic regime / NYDFS perimeter as written
  at the v0.3 cut-off.
- DAI / USDS and USDe are shown explicitly outside the payment-stablecoin
  perimeter. They remain subject to other applicable regimes (AML/CFT,
  securities, derivatives, consumer protection), which are not drawn here.
- BoE's proposed 40-95% central-bank-deposit backing channel is dashed to
  emphasise that it is a consultation rule, not yet enacted (`CLAIM_090`).
- The diagram does not attempt to scale the boxes by market size; supply
  and volume data should be sourced from chapter 7, not from this diagram.
