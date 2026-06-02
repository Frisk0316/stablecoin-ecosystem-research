# DAI / USDS Protocol Flow

Updated 2026-05-25: added for the v0.3 clean slide script. This diagram keeps
DAI / USDS outside the fiat-backed payment-stablecoin issuer model and shows
the protocol-collateralised stability path supported by `CLAIM_098` to
`CLAIM_102`.

```mermaid
flowchart TD
    User["User / Vault owner"] --> Vault["Maker Vault<br/>governance-approved collateral"]
    Vault --> Mint["DAI / USDS minted as debt"]
    Mint --> Use["On-chain use / savings modules"]

    Governance["MKR / SKY governance"] --> CollateralList["Collateral types<br/>risk parameters"]
    CollateralList --> Vault
    Governance --> DSR["DSR / Sky Savings Rate<br/>via sUSDS"]
    Use --> DSR

    Oracle["Oracles"] --> Price["Collateral price feeds"]
    Price --> Health["Vault health check"]
    Vault --> Health
    Health -->|"below Liquidation Ratio"| Auction["Collateral Auction"]
    Auction -->|"enough Dai raised"| Surplus["Debt repaid<br/>excess collateral returned"]
    Auction -->|"shortfall"| Backstop["Protocol Surplus / MKR dilution backstop"]

    Emergency["Global Settlers / Emergency Oracles"] -. "emergency shutdown authority" .-> Shutdown["Emergency Shutdown"]

    classDef protocol stroke:#315a9a,stroke-width:2px
    classDef risk stroke:#a66b00,stroke-width:2px,stroke-dasharray:5
    class Vault,Mint,Use,Governance,CollateralList,DSR,Oracle,Price protocol
    class Health,Auction,Surplus,Backstop,Emergency,Shutdown risk
```

## Notes

- The diagram supports Slide 14 in `07_final_report/slide_script_v0_3.md`.
- It should not be read as a fiat-backed redemption flow. The user-facing
  stability mechanism is overcollateralisation, liquidation, governance risk
  parameters, and external actors, not direct issuer redemption.
- `CLAIM_102` covers the Sky rebrand layer: USDS, sUSDS, stUSDS, SKY, and
  the product-page USDC-to-USDS conversion route.

