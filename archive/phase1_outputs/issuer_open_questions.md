# Open Questions - Phase 1

## A. 文件缺口

1. NYDFS Guidance on the Issuance of U.S. Dollar-Backed Stablecoins：目前只有 RLUSD / GUSD reserve reports 引用 NYDFS Letter，但獨立原文資料夾仍是空的。
2. IMF stablecoin papers：03_central_bank_and_academic/imf 是空資料夾，需最後 external fetch 或手動下載。
3. Federal Reserve stablecoin papers / speeches：03_central_bank_and_academic/fed 是空資料夾。
4. On-chain market dashboards：05_market_and_onchain_data 是空資料夾，需補 Visa / DeFiLlama / Cambridge / Artemis export 或連結。
5. USDPT-specific primary docs：目前只有 Western Union / Anchorage / payment rail 背景資料，缺 USDPT product page、launch press release、whitepaper、reserve report、contract addresses、redemption terms。

## B. Issuer-specific open questions

### USDC
- Circle Mint / redemption policy 是否清楚區分 retail holders 與 eligible business account holders？
- USDC reserve fund 的法律結構、託管銀行與 BlackRock fund documentation 是否需要補？
- MiCA USDC whitepaper 與美國 USDC terms 是否有 redemption rights 差異？

### USDT
- Tether Terms of Service 中誰可以直接 redeem？最低贖回額、費用、地區限制為何？
- Q1 2026 reserve report 中 T-bills、repo、secured loans、bitcoin、gold、other investments 的精確比例需要表格化。
- Tether International / El Salvador registration 與 GENIUS-compliant USAT 的差異需建立對照。

### PYUSD / USDP / USDG
- Paxos 各穩定幣的 issuer entity 是否分別為 Paxos Trust Company, N.A.、Paxos Digital Singapore Pte. Ltd. 等？
- PYUSD rewards 是否構成「穩定幣持有人收益」問題，如何與 GENIUS Act 禁止支付利息比較？
- USDP 缺具體月份 reserve report PDF，需要補。

### RLUSD / GUSD
- NYDFS guidance 原文需要補齊，因 RLUSD/GUSD reserve reports 直接引用它。
- Product pages 是否揭露 freeze / blacklist / redemption suspension 權限？

### FDUSD
- FDUSD 的持有人直接 redemption rights 與 issuer terms 尚未補齊。
- Hong Kong trust / BVI issuer / multi-jurisdiction bank accounts 的法律保護程度需精查。

### DAI / USDS
- Sky / Maker 的 RWA collateral、PSM、savings yield、governance controls 需要分開建表。
- DAI/USDS 是否應與 payment stablecoins 同表，或獨立 crypto-backed / protocol stablecoin 表？

### USDe
- USDe 與 sUSDe 的權利、收益與風險要嚴格區分。
- Custodian attestations、exchange exposures、basis trade unwind risk 需建立單獨風險矩陣。

### USDPT
- USDPT 實際 token 名稱是 USDPT 還是 UDSPT？Anchorage comment letter 使用 UDSPT。
- 是否已有 reserve trust / attestation / redemption terms？
- Western Union agents 是否會直接持有 stablecoin，還是只作為後台 treasury settlement asset？
- USDPT 取代的是 agent settlement / prefunding / nostro liquidity 的哪一層，而不是 SWIFT 訊息層或中央銀行清算層。
