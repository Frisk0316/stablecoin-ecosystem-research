# USDe Synthetic-Dollar Flow

Updated 2026-05-25: added for the v0.3 clean slide script. This diagram shows
USDe as a synthetic-dollar structure rather than a fiat-backed payment
stablecoin. It is anchored to `CLAIM_103` to `CLAIM_106`.

```mermaid
flowchart TD
    MintUser["Whitelisted Mint User"] --> Backing["Backing asset<br/>spot collateral"]
    Backing --> OES["Off-Exchange Settlement custody"]
    OES --> USDe["USDe minted<br/>1:1 collateralisation"]

    Backing --> Hedge["Short perpetual futures hedge<br/>similar notional"]
    Hedge --> Exchange["Derivatives exchange venue"]
    Exchange -. "funding / realised P&L settlement" .-> OES

    USDe --> Holder["Holding User"]
    USDe --> sUSDe["sUSDe reward-accruing wrapper"]

    Custodian["Monthly custodian attestations"] --> OES
    ReserveFund["Reserve Fund<br/>USDC + USDT + smaller ETH allocation"] --> Support["Negative funding support<br/>bidder of last resort"]
    Support --> USDe
    Governance["4 of 10 multi-sig<br/>Ethena contributors"] --> ReserveFund

    classDef core stroke:#2f6f5e,stroke-width:2px
    classDef risk stroke:#8a4f16,stroke-width:2px,stroke-dasharray:5
    class MintUser,Backing,OES,USDe,Holder,sUSDe,Custodian core
    class Hedge,Exchange,ReserveFund,Support,Governance risk
```

## Notes

- The diagram supports Slide 15 in `07_final_report/slide_script_v0_3.md`.
- It separates USDe from sUSDe. USDe is the synthetic-dollar token; sUSDe is
  the reward-accruing wrapper.
- Off-Exchange Settlement custody mitigates exchange-specific counterparty
  risk but does not eliminate funding-rate, exchange-operational, custodian,
  or governance risk.

