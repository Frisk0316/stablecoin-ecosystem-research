# Central Bank and International Institution Source Digest v0.3

## BIS
BIS sources provide the strongest conceptual scaffolding for the project. The 2025 Annual Economic Report chapter evaluates stablecoins against singleness, elasticity, and integrity. BIS Papers No. 170 develops the international monetary-system and digital dollarisation angle. BIS Working Paper No. 1270 supports the safe-asset-price channel by analysing stablecoin flows and short-term Treasury yields.

## ECB
ECB sources focus on financial stability, monetary sovereignty, safe-asset channels, bank disintermediation, and monetary-policy transmission. ECB WP 3174 is central for the global safe asset channel, while ECB WP 3199 is central for deposit substitution and bank-lending transmission.

## FSB
FSB sources provide the global regulatory baseline and implementation-gap analysis. The 2023 recommendations are the normative framework; the 2025 thematic review documents slow, fragmented, and uneven implementation across jurisdictions.

## Taiwan CBC
CBC sources now support a Taiwan-specific claim set (`CLAIM_112` to
`CLAIM_118`).

`CBC_003` frames fiat-backed stablecoins as tokenized private-sector money:
they lack legal-tender status, still depend on central-bank money as anchor,
and are not expected to materially affect CBC seigniorage power on that basis
(`CLAIM_112`). `CBC_002` extends this into a two-tier tokenized-money
architecture: deposit tokens and stablecoins may become private tokenized
money, but central-bank money remains the cross-system settlement asset needed
for singleness of money and payment finality (`CLAIM_113`).

`CBC_004` supplies the strongest Taiwan policy synthesis. For USD
stablecoins, CBC identifies a digital-dollarisation and FX-management channel:
broad USD-stablecoin use can strengthen the dollar's role in trade and
payments, complicate traditional capital-management tools, weaken local
currency functions in vulnerable economies, and pressure FX reserves and
financial stability (`CLAIM_114`). For New Taiwan dollar stablecoins, CBC
frames the product as similar to tokenized electronic-payment stored value and
indicates that issuers should maintain 100% reserve assets, including CBC
reserve deposits for larger issuance and other high-quality liquid assets
(`CLAIM_115`). CBC also expects current domestic payment impact to be limited
because Taiwan already has complete, diverse, low-cost and real-time payment
rails and few NTD-denominated virtual assets (`CLAIM_116`). On monetary
statistics and transmission, CBC expects NTD stablecoin issuance to mainly
reallocate funds inside the monetary system, leaving M2 broadly unchanged and
having limited impact on bank credit creation or monetary-policy transmission
(`CLAIM_117`). CBC's regulatory description records the draft virtual-asset
service law direction: issuance permission, issuer qualification, asset
segregation, reserve management, audit/assurance, no interest/yield, disclosure,
and FSC-CBC consultation / joint sub-rules (`CLAIM_118`).

## Federal Reserve
The deficiency-source pass added a Federal Reserve source set. `FED_002`
supports market-development and financial-stability claims: stablecoins grew
about 50% in market capitalization during 2025, and the Fed highlights complex
intermediation chains, vertical integration, and retail wallet partnerships as
emerging vulnerabilities (`CLAIM_044`, `CLAIM_045`). `FED_004` supports the
banking-transmission discussion: stablecoins can reduce, recycle, or
restructure bank deposits depending on demand source, converted assets, and
issuer reserve allocation (`CLAIM_046`), and may affect bank credit through
deposit-volume, composition, funding-cost, and liquidity-management channels
(`CLAIM_047`). `FED_001` provides the earlier two-tier-versus-narrow-bank
framework (`CLAIM_048`).

## IMF
The IMF source gap is no longer empty. Four IMF files are now registered:
`IMF_001` to `IMF_004`. Current claim-table extraction covers two high-value
claims. `IMF_001` models the reserve-backing/run-risk tradeoff and the issuer
incentive problem (`CLAIM_049`). `IMF_003` uses market reaction evidence to
show that policy support for stablecoin payments affected incumbent
payment-firm valuations, consistent with expected payment-sector competition
(`CLAIM_050`). `IMF_002` and `IMF_004` still need page-level extraction.

## Remaining Work
The central-bank module is no longer blocked by missing IMF/Fed files, but it
still needs a normalized extraction pass for `IMF_002`, `IMF_004`, the Fed
accessible figure appendix, and any quantitative claims imported into the final
report. BIS, ECB, and FSB themes remain digest-level until they are promoted
to formal `CLAIM_XXX` rows. Taiwan CBC is no longer an unextracted gap for the
core reading-group synthesis, although enacted Taiwan statutory text should be
registered separately if it becomes available.
