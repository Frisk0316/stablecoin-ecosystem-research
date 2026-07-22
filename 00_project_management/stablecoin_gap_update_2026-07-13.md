# Stablecoin P0 Gap Update — 2026-07-13

This update records the latest official-source pass for USDPT, adjusted
stablecoin-transfer datasets and Taiwan's Virtual Asset Service Act. It is a
bounded evidence update, not permission to fill unpublished facts by
inference.

## Outcome summary

| Gap | Outcome on 2026-07-13 | Remaining boundary |
| --- | --- | --- |
| USDPT reserve attestation | **Closed for the 2026-05-31 point in time.** Deloitte & Touche LLP reported 1,500,372 redeemable USDPT, US$1,603,106 reserves and US$102,734 surplus. | The engagement is an AICPA attestation examination, not a financial-statement audit or an opinion on legal compliance, contracts or control effectiveness. |
| USDPT-specific terms and fees | **Still open.** ADB's general covered-stablecoin terms limit direct issue/redemption to ADB Clients. The general fee schedule has a USDtb row but no USDPT row. | No USDPT series supplement, retail terms, direct agent/retail redemption rights or USDPT fee row was located. |
| USDPT technical controls | **Partially closed at issuer-capability level.** ADB states that issuer-level controls can issue/redeem and, when required, freeze, block or burn. | Exact USDPT contract roles, key governance, implementation and external control-effectiveness testing remain unpublished. |
| USDPT agent/payment workflow | **Partially supported at a high level.** WU describes 24/7 treasury/agent settlement intended to reduce prefunding; Bybit supports selected-market fiat buy/sell. | Agent balance-sheet treatment, bank/clearing/reconciliation sequence, direct redemption and the full customer→agent→bank workflow remain unpublished. Several consumer features remain labelled “coming soon.” |
| Visa / Artemis / Cambridge data | **Method and current snapshots updated; the original “market-wide adjusted payment volume export” requirement cannot be closed.** | Visa and Cambridge measure adjusted transfers, not payments. Artemis' live headline is transfer volume; its payments estimate is sample/model based. No complete anonymous-downloadable market-wide payments dataset exists among these sources. |
| Taiwan Virtual Asset Service Act | **Legislative stage advanced:** the Act passed third reading on 2026-06-30. | As of 2026-07-13, official passed-bill and Presidential Gazette pages do not show promulgated text; it is not yet safe to say “promulgated,” “effective” or to state final subordinate rules. |

## USDPT reserve attestation

The official May report was issued by Deloitte & Touche LLP on 2026-06-26
and measures 2026-05-31 23:59:59 UTC:

| Item | Amount |
| --- | ---: |
| Redeemable USDPT | 1,500,372 |
| Reserve assets | US$1,603,106 |
| Reported surplus | US$102,734 |
| Cash | US$150,241 |
| Money-market-fund NAV | US$1,452,865 |
| Uninsured bank cash | US$0 |

The report identifies MMF CUSIP `09248U874` and says reserve assets were held
in segregated, unencumbered fiduciary trust accounts. The official Solana
address remains `HVWf8JmLoHs99Lw8Psf3fyqAtA4crWxCPkrmSdNjhNH3`.

Local archive:
`09_data_exports/gap_update_2026-07-13/USDPT_attestation_2026-05-31.pdf`.

Primary sources:

- <https://www.anchorage.com/platform/usdpt-reserve-attestations-anchorage-digital>
- <https://learn.anchorage.com/05.31.26_USDPT_Stablecoin_Attestation_Report_signed.pdf>
- <https://www.anchorage.com/anchorage-digital-bank-n-a-covered-stablecoin-terms>
- <https://www.anchorage.com/anchorage-digital-bank-n-a-covered-stablecoin-service-fee-schedule>
- <https://learn.anchorage.com/Anchorage%20Digital%27s%20Comment%20Letter%20on%20Treasury%27s%20NPRM%20for%20GENIUS%20Act%20-%20June%209%202026.pdf>

## Transfer-volume evidence and reproducibility

The snapshot is archived in
`09_data_exports/gap_update_2026-07-13/adjusted_transfer_snapshot_2026-07-13.csv`.

### Visa Onchain Analytics

Observed on 2026-07-13:

- last 12 months: US$100.1T total transfers, US$14.7T adjusted transfers,
  16.9B total transactions and 2.4B adjusted transactions;
- last 30 days: US$5.8T total and US$1.5T adjusted transfers;
- retail-sized adjusted transfers: US$6.7B and 134.9M transactions.

Visa's adjustment selects the largest stablecoin amount in a transaction and
removes specified high-frequency/high-value addresses, intra-exchange flows,
bots/MEV, internal transfers and high-volume unlabeled addresses. The adjusted
series still includes exchange, lending, mint/burn and ramp activity. Therefore
neither “adjusted” nor “under US$250” is evidence that a transfer was a
merchant payment or remittance. The live anonymous UI exposes chart/image
functions, but no documented anonymous raw CSV/API was found.

Sources: <https://visaonchainanalytics.com/> and
<https://visaonchainanalytics.com/transactions>.

### Artemis

The 2026-07-13 overview displayed US$315.6B supply, US$229.0B average daily
transfer volume, 64.3M average daily transactions and 4.5M active addresses.
Its documented adjusted methodology removes duplicate transfers, keeps the
largest transfer per transaction, and removes intra-exchange and MEV activity;
P2P is wallet/EOA activity. The current headline is **transfer volume**, not a
payments-only total. Free account access is quota-limited; anonymous bulk CSV
is not available. Artemis' 2025 payments study reported a February 2025
annualised US$72B run rate from a non-comprehensive firm sample and must not be
presented as a 2026 market total.

Sources:

- <https://www.artemis.ai/sectors/stablecoins/overview?granularity=daily>
- <https://www.artemis.ai/docs/snowflake-share/stablecoins>
- <https://about.artemis.ai/pricing>
- <https://research.artemis.xyz/p/what-are-stablecoins-used-for>

### Cambridge CCAF

The public JSON archived on 2026-07-13 yields, for the latest complete month
June 2026, US$2,531,847,084,155.8467 adjusted transfer value and 122,153,423
adjusted transfers. It covers BUSD, DAI, USDC on Ethereum/Tron and USDT on
Ethereum/Tron, excludes off-chain exchange activity, and is not a complete
market-wide payments series. July is partial and was not used. The endpoint is
public but undocumented, so it is reproducible today but not a guaranteed API
contract.

Local raw data:
`09_data_exports/gap_update_2026-07-13/Cambridge_CCAF_transactions_monthly_2026-07-13.json`.

Sources:

- <https://ccaf.io/cdmd/about>
- <https://api.ccaf.io/v1/dmd/transactions?project=dmd&interval=monthly>
- <https://www.jbs.cam.ac.uk/wp-content/uploads/2026/02/2026-ccaf-tokenised-money-use-cases-interoperability-and-regulation.pdf>

## Taiwan legislative status

The official Legislative Yuan passed-bills list and plenary record show that
the Virtual Asset Service Act passed third reading on 2026-06-30. As of
2026-07-13, the passed-bills list still has blank full-text/promulgated-text
cells for the Act, and the Presidential Gazette index through 2026-07-08 does
not list it. The FSC and CBC were still preparing the stablecoin issuance
licensing rules; comments about likely bank issuance or foreign-stablecoin
treatment are policy direction, not issued regulations.

Safe wording:

> Taiwan's Virtual Asset Service Act passed third reading on 2026-06-30. As
> of 2026-07-13, this research had not verified promulgation, effectiveness or
> final FSC/CBC stablecoin subordinate rules.

Primary sources:

- <https://lis.ly.gov.tw/lynewbillc/newbillkm>
- <https://ppg.ly.gov.tw/ppg/sittings/meetingLink?id=11-05-15%3B115%2F06%2F26%3B%E9%99%A2%E6%9C%83>
- <https://www.ly.gov.tw/Pages/Detail.aspx?nodeid=47503&pid=263679>
- <https://www.president.gov.tw/page/129?DeteailNo=4>
- <https://www.ly.gov.tw/Pages/Detail.aspx?nodeid=47221&pid=263810>

## Research rule carried forward

Do not convert absence of public documentation into an affirmative product
claim. Unpublished terms, exact controls, agent workflows and future
subordinate rules stay open with explicit boundaries.

