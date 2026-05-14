# Issuer Source Digest - Phase 1 Draft

> 本文件是第一輪正式研究輸出，目的在於建立可追溯的 issuer source digest。頁碼與段落在下一輪會逐一精修。

## USDC / Circle

目前資料包含 Circle 年報、Form 10-K、USDC March 2026 reserve report、USDC terms、MiCA USDC whitepaper 與 transparency page。第一輪可先用於建立 USDC 的準備金、條款、MiCA 合規與公司風險揭露脈絡；下一步需精抽誰能直接 redeem、可否凍結、reserve fund 結構、銀行與短債暴露。

## USDT / Tether

Tether 文件包含 whitepaper、Relevant Information Document、Q1 2026 reserve report、transparency reports page。Q1 2026 BDO report 為 ISAE 3000R reasonable assurance，限定於 2026-03-31 單一時間點；財務資料不是完整財務報表。核心研究用途是比較 USDT 的儲備資產廣度、超額準備、secured loans/other investments 與 GENIUS 型狹義 permitted reserve 模式的差異。

## PYUSD / PayPal-Paxos

PYUSD 文件包含 PayPal crypto terms、PayPal 70 markets release、Paxos product page 與 transparency reports page。PayPal release 指出 PYUSD 由 Paxos Trust Company, N.A. 發行，儲備由美元存款、美國公債與現金等價物支持，並於 70 markets 擴張。研究重點是 PayPal 平台型穩定幣如何把穩定幣帶進既有支付網路，以及 rewards 是否形成 GENIUS 利息限制的比較議題。

## USDG / Paxos Digital Singapore

USDG 文件包含 about page、EU whitepaper、transparency reports page 與 2024 whitepaper。Whitepaper 指出 USDG 由 Paxos Digital Singapore Pte. Ltd. 發行，受 MAS 審慎監理，並可向 Paxos 1:1 贖回美元。研究重點是 MAS single-currency stablecoin 框架、DBS reserve custody、企業級 global dollar network 以及與 PYUSD/USDP 的多司法轄區比較。

## USDP / Pax Dollar

USDP 文件目前主要是 product page 與 transparency reports page，缺少具體月份 reserve report PDF。可先標記為 Paxos 發行、fully reserved/dollar-backed 產品，但 reserve composition、auditor、redemption details 需等外部或後續補件。

## RLUSD / Ripple

RLUSD 文件包含 product page、transparency page 與 March 2026 attestation report。Attestation 顯示發行主體是 Standard Custody & Trust Company, LLC，為 Ripple Labs Inc. 子公司且是 New York limited purpose trust company；reserve criteria 取自 NYDFS 2022 guidance。此來源適合與 GUSD / USDC / PYUSD 的 NYDFS/美國合規模式對照。

## FDUSD / First Digital

FDUSD 文件包含 ISAE 3000 attestation report 與 reserve accounts report。AOGB 報告是 limited assurance；Reserve accounts report 顯示 FD121 (BVI) Limited、跨鏈供給與 reserve accounts 形式，包含美元與美國短債等資產。研究重點是 offshore issuer + Hong Kong trust/custodian 結構，與美國 NYDFS/OCC/MAS 模式不同。

## GUSD / Gemini

GUSD 文件包含 Gemini filing、product page、Jan/Feb 2026 reserve reports 與 whitepaper。Whitepaper 將 GUSD 定義為 New York trust company issued、1:1 USD-pegged ERC20 token；Feb 2026 reserve report 則按 NYDFS guidance 檢查 reserves。研究重點是較早期 regulated stablecoin model、NY trust company、reserve attestation 與平台 redemption。

## DAI / USDS / Maker-Sky

Maker/Sky 文件包含 DAI original whitepaper、Multi-Collateral DAI whitepaper、Sky money product page 與 Sky Protocol technical whitepaper。它們不應與 fiat-backed stablecoins 放在同一風險類別；研究重點是 overcollateralized crypto-backed / RWA collateral / governance / oracle / liquidation / savings mechanisms。

## USDe / Ethena

Ethena 文件包含 USDe overview、How USDe works、reserve fund、custodian attestations、audits 與 LlamaRisk PoR page。USDe 應作為 synthetic dollar 類別研究，核心風險不是單純 T-bill reserve，而是 basis/funding/custodian/exchange/hedging 與 liquidity unwind risk。

## USDPT / Western Union-Anchorage

USDPT 文件包含 Western Union annual report/proxy、Investor Day、Anchorage OCC comment letter、Fedwire PFMI 與 remittance data。Anchorage comment letter 提到 ADB 期待與 Western Union 發行 UDSPT；但 zip 中尚未見完整 USDPT product page、launch release、whitepaper 或 reserve attestation。因此目前只能研究「可能設計」與「Western Union 結算場景」，不能斷言實際產品細節。
