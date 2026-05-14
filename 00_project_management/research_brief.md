# 穩定幣生態研究：GPT 研究任務包

> 用途：本 Markdown 檔可直接交給 GPT / Deep Research / Claude / NotebookLM 作為研究指令。  
> 研究主題：穩定幣生態、美元貨幣市場、USDPT、SWIFT / correspondent banking、GENIUS Act、央行觀點與發行商比較。

---

## 0. 研究目標

本研究不是單純比較「哪一顆穩定幣比較安全」，而是要從 **美元貨幣體系、穩定幣發行商資產負債表、跨境支付結算、法規監理、央行觀點、鏈上數據** 等層面，建立完整的穩定幣生態研究框架。

核心問題如下：

1. 穩定幣如何把美元國債、回購市場、貨幣市場基金、銀行存款包裝成鏈上美元負債？
2. USDC、USDT、PYUSD、USDPT、RLUSD、FDUSD、GUSD、DAI / USDS、USDe 等穩定幣在儲備資產、贖回權、監理架構、風險上有何差異？
3. Western Union 的 USDPT 想改變傳統跨境支付 / SWIFT / correspondent banking 的哪一段？
4. GENIUS Act、CLARITY Act、NYDFS、MiCA、BoE 等法規如何重新分配穩定幣利益結構？
5. BIS、FSB、IMF、Fed、ECB、台灣央行等機構如何看待穩定幣對金融穩定、貨幣政策、銀行中介、數位美元化與短債市場的影響？
6. 穩定幣的鏈上數據與真實世界支付場景如何連接？

---

## 1. 資料整理原則

### 1.1 文件優先順序

研究時請依照以下優先順序引用資料：

1. **法案 / 監理原始文件**  
   例如 GENIUS Act、CLARITY Act、NYDFS Guidance、MiCA / EBA、BoE consultation。

2. **央行 / 國際監理機構文件**  
   例如 BIS、FSB、IMF、Federal Reserve、ECB、台灣央行。

3. **發行商官方文件**  
   例如 Circle、Tether、Paxos、Ripple、First Digital、Gemini、MakerDAO / Sky、Ethena、Western Union、Anchorage。

4. **支付與清算系統官方文件**  
   例如 SWIFT、BIS CPMI、Fedwire、CHIPS、World Bank remittance cost data。

5. **鏈上資料 / 市場資料 dashboard**  
   例如 Visa Onchain Analytics、DeFiLlama、Cambridge Digital Money Dashboard、Artemis。

6. **新聞、Podcast、二手文章**  
   只作為輔助，不作為主要證據。Blocktrend EP316 可放在台灣應用場景觀察，不應作為官方監理來源。

---

### 1.2 HTML / 403 處理原則

若 `.html` 網頁遇到 403、動態頁面無法下載、或抓下來只有原始碼，請不要硬抓。

請改成 `source_registry.csv` 中的 link-only 紀錄：

```csv
id,category,publisher,title,url,status,notes
NYDFS_001,law,NYDFS,Guidance on USD-backed Stablecoins,https://...,link_only,HTML; fetch when needed or manually save PDF
```

原則如下：

- PDF / Excel / 法案 / 財報 / 準備金報告：優先下載。
- HTML 官方頁 / Transparency landing page / Dashboard：先保留官方連結。
- 只有在 AI 無法 fetch 或研究需要固定版本時，才用瀏覽器 `Ctrl + P` → 另存 PDF。

---

## 2. 建議資料夾結構

```text
stablecoin_research_docs/
├── 01_issuer_primary_docs/
│   ├── circle_usdc/
│   ├── tether_usdt/
│   ├── paxos_pyusd_usdp_usdg/
│   ├── ripple_rlusd/
│   ├── first_digital_fdusd/
│   ├── gemini_gusd/
│   ├── maker_sky_dai_usds/
│   ├── ethena_usde/
│   └── western_union_usdpt/
│
├── 02_laws_and_regulation/
│   ├── us_genius_act/
│   ├── us_clarity_act/
│   ├── nydfs/
│   ├── mica_eu/
│   ├── uk_boe_fca/
│   └── hong_kong_singapore_japan/
│
├── 03_central_bank_and_academic/
│   ├── bis/
│   ├── fsb/
│   ├── imf/
│   ├── federal_reserve/
│   ├── ecb/
│   ├── taiwan_cbc/
│   └── other_central_banks/
│
├── 04_payment_and_settlement/
│   ├── swift/
│   ├── fedwire_chips/
│   ├── correspondent_banking/
│   └── remittance_costs/
│
├── 05_market_and_onchain_data/
│   ├── visa_onchain_analytics/
│   ├── defillama/
│   ├── cambridge_digital_money_dashboard/
│   └── artemis/
│
├── 06_failure_cases/
│   ├── terra_ust/
│   ├── iron_finance/
│   └── other_depeg_cases/
│
├── 07_research_outputs/
│   ├── 01_source_digest.md
│   ├── 02_claim_table.csv
│   ├── 03_comparison_matrix.csv
│   ├── 04_open_questions.md
│   └── 05_chapter_drafts/
│
└── source_registry.csv
```

---

## 3. Source Registry 格式

請建立 `source_registry.csv`，每份文件都要登錄。

```csv
id,category,publisher,title,asset,year,document_type,local_path,url,status,priority,notes
USDC_001,issuer,Circle,USDC Reserve Report,USDC,2026,reserve_report,01_issuer_primary_docs/circle_usdc/xxx.pdf,https://...,downloaded,high,latest monthly reserve report
BIS_001,central_bank,BIS,Stablecoins and International Monetary System,Stablecoins,2026,research_paper,03_central_bank_and_academic/bis/xxx.pdf,https://...,downloaded,high,core BIS source
GENIUS_001,law,GovInfo,GENIUS Act,Stablecoin,2026,law,02_laws_and_regulation/us_genius_act/xxx.pdf,https://...,downloaded,high,primary law text
```

### 欄位說明

| 欄位 | 說明 |
|---|---|
| id | 自訂文件 ID，例如 USDC_001、BIS_001 |
| category | issuer / law / central_bank / payment_settlement / market_data / failure_case |
| publisher | 發布者，例如 Circle、BIS、FSB、GovInfo |
| title | 文件標題 |
| asset | 對應資產，例如 USDC、USDT、USDPT、Stablecoins |
| year | 文件年份 |
| document_type | reserve_report / whitepaper / law / research_paper / annual_report / transparency_page |
| local_path | 本地檔案路徑 |
| url | 官方來源 URL |
| status | downloaded / link_only / failed_download / manual_pdf |
| priority | high / medium / low |
| notes | 補充說明 |

---

## 4. 第一批研究：穩定幣發行商比較

### 4.1 請上傳的文件

優先上傳：

```text
Circle / USDC:
- USDC reserve report
- Circle annual report / 10-K
- USDC terms
- MiCA USDC whitepaper

Tether / USDT:
- Tether whitepaper
- Tether reserve reports
- Tether Relevant Information Document
- Tether transparency page

Paxos / PYUSD / USDP / USDG:
- PYUSD transparency
- USDP transparency
- USDG whitepaper
- Paxos terms

Ripple / RLUSD:
- RLUSD product page
- RLUSD transparency / attestation

First Digital / FDUSD:
- FDUSD transparency
- FDUSD reserve account report
- FDUSD attestation

Gemini / GUSD:
- GUSD whitepaper
- GUSD reserve reports
- Gemini 10-K

MakerDAO / Sky / DAI / USDS:
- DAI original whitepaper
- Maker MCD whitepaper
- Sky technical whitepaper

Ethena / USDe:
- USDe overview
- How USDe works
- Custodian attestations
- Reserve fund
- Audits

Western Union / USDPT:
- Western Union USDPT product page
- Western Union USDPT launch press release
- Western Union annual report / 10-K
- Western Union Investor Day
- Anchorage USDPT partnership announcement
- Anchorage OCC GENIUS Act comment letter
```

### 4.2 給 GPT 的任務指令

```text
請根據我上傳的 issuer 文件，為每個穩定幣整理一張比較表。

請整理以下欄位：

1. 穩定幣名稱
2. 發行主體
3. 監理管轄
4. 發行方式
5. 儲備資產類型
6. 是否 1:1 贖回
7. 誰有直接贖回權
8. 準備金報告頻率
9. attestation / audit 機構
10. 是否支付利息
11. 是否可凍結 / 黑名單 / 暫停贖回
12. 是否依賴銀行存款
13. 是否依賴美國短債 / repo / MMF
14. 主要用途
15. 主要風險
16. 文件來源與頁碼

請只根據文件內容回答；如果文件沒有說明，請標示「文件未揭露」。
請不要用猜測補齊缺漏欄位。
```

### 4.3 預期產出

```text
07_research_outputs/
├── issuer_source_digest.md
├── issuer_comparison_matrix.csv
├── issuer_claim_table.csv
└── issuer_open_questions.md
```

---

## 5. 第二批研究：法規與監理框架

### 5.1 請上傳的文件

```text
美國:
- GENIUS Act
- CLARITY Act
- CLARITY Act House Report
- OCC GENIUS Act NPRM
- FinCEN / Treasury GENIUS Act related documents
- NYDFS Guidance on USD-backed Stablecoins

歐盟:
- MiCA / EBA ART and EMT documents
- EBA reporting ITS
- EBA PSD2 and MiCA interplay opinion
- ESMA MiCA overview

英國:
- Bank of England systemic stablecoin consultation
- BoE financial stability report
- BoE FPC record
```

### 5.2 給 GPT 的任務指令

```text
請只根據我上傳的法規與監理文件，整理 payment stablecoin / digital asset market structure 的法規架構。

請分別整理：

A. GENIUS Act
1. payment stablecoin 的定義
2. permitted payment stablecoin issuer 的資格
3. reserve asset 限制
4. redemption rule
5. disclosure / monthly reporting
6. audit / attestation requirement
7. interest / yield restriction
8. rehypothecation restriction
9. bankruptcy priority
10. foreign issuer rule
11. AML / sanctions / BSA requirement
12. 對銀行、非銀行發行商、州監理的影響

B. CLARITY Act
1. digital commodity 的定義
2. SEC / CFTC 分工
3. stablecoin 是否被排除在 securities 定義之外
4. 交易所、broker、dealer、custodian 的新規則
5. 對 permitted payment stablecoin transaction 的處理
6. 對 DeFi / self-custody / blockchain developer 的影響

C. NYDFS / MiCA / BoE
1. reserve requirement
2. redemption requirement
3. custody / safeguarding
4. disclosure / reporting
5. systemic stablecoin treatment
6. 與美國 GENIUS Act 的差異

請用表格比較不同監理框架，並保留每一個結論的來源與頁碼。
```

### 5.3 預期產出

```text
07_research_outputs/
├── law_source_digest.md
├── law_comparison_matrix.csv
├── genius_act_claim_table.csv
├── clarity_act_claim_table.csv
└── law_open_questions.md
```

---

## 6. 第三批研究：央行與國際機構觀點

### 6.1 請上傳的文件

```text
BIS:
- BIS Annual Economic Report 2025 Chapter III
- BIS Papers No.170: Stablecoins and international monetary system
- BIS Working Paper No.1270: Stablecoins and safe asset prices

FSB:
- FSB Global Stablecoin Recommendations
- FSB 2025 Thematic Review
- FSB / IOSCO implementation progress report

IMF:
- Understanding Stablecoins
- Stablecoins and the Future of Payments
- Stablecoin Shocks
- Making Stablecoins Stable

Federal Reserve:
- Stablecoins in 2025
- Banks in the Age of Stablecoins

ECB:
- Stablecoins and monetary sovereignty
- ECB Financial Stability Review
- ECB working papers on stablecoins

台灣央行:
- 穩定幣、存款代幣與 CBDC 相關文件
- 美元穩定幣與新台幣穩定幣相關文件
```

### 6.2 給 GPT 的任務指令

```text
請整理央行與國際機構對穩定幣的共同觀點與分歧。

請依照以下主題整理：

1. 穩定幣是否能改善支付效率？
2. 穩定幣是否會造成金融穩定風險？
3. 穩定幣是否可能引發擠兌？
4. 穩定幣如何影響銀行存款與金融中介？
5. 穩定幣如何影響貨幣政策傳導？
6. 美元穩定幣是否會造成數位美元化？
7. 穩定幣是否會增加對美國短債 / safe assets 的需求？
8. 穩定幣如何影響跨境資本流動？
9. 穩定幣與 CBDC / tokenized deposits 的關係是什麼？
10. 央行建議的監理原則是什麼？

請將每個主題分成：
- 主要共識
- 不同機構的差異
- 支持該結論的文件來源
- 對 USDC / USDT / USDPT / USDe / DAI 等不同穩定幣的含義
```

### 6.3 預期產出

```text
07_research_outputs/
├── central_bank_source_digest.md
├── central_bank_theme_matrix.csv
├── central_bank_claim_table.csv
└── central_bank_open_questions.md
```

---

## 7. 第四批研究：USDPT、SWIFT 與跨境結算

### 7.1 請上傳的文件

```text
Western Union / USDPT:
- Western Union USDPT product page
- Western Union USDPT launch press release
- Western Union annual report / 10-K
- Western Union Investor Day
- Anchorage USDPT partnership announcement
- Anchorage USDPT launch announcement
- Anchorage OCC GENIUS Act comment letter

SWIFT / Correspondent Banking:
- BIS CPMI Correspondent Banking
- BIS CPMI Cross-border Retail Payments
- SWIFT PMPG Cover Payments Guideline
- SWIFT Spotlight on Speed
- Fedwire Funds PFMI Disclosure
- CHIPS overview
- World Bank Remittance Prices Worldwide
```

### 7.2 給 GPT 的任務指令

```text
請研究 Western Union USDPT 是否可能改變跨境匯款結算模式。

請依照以下架構回答：

1. Western Union 傳統匯款模式
   - 前台收付款流程
   - agent network
   - settlement assets
   - settlement obligations
   - agent receivables / payables
   - 為何前台可以很快，但後台資金結算仍可能較慢

2. 傳統 SWIFT / correspondent banking 流程
   - SWIFT 是訊息網路，不是資金結算系統
   - MT103 / pacs.008
   - MT202 COV / pacs.009 COV
   - cover payment
   - nostro / vostro
   - correspondent bank / respondent bank
   - Fedwire / CHIPS / local clearing
   - 最後一哩入帳

3. USDPT 的產品設計
   - 發行主體
   - 使用鏈
   - 儲備資產
   - 1:1 贖回
   - exchange support
   - Digital Asset Network
   - Stable by Western Union
   - treasury and agent settlement

4. USDPT 可能取代的環節
   - agent settlement
   - prefunding
   - nostro / vostro liquidity
   - 批次對帳
   - 銀行營業時間限制
   - 部分交易所出金流程

5. USDPT 不能取代的環節
   - KYC / AML / sanctions screening
   - local fiat cash-out
   - 銀行帳戶與當地清算
   - 使用者保護與爭議處理
   - 法規核准
   - 穩定幣發行商儲備與贖回風險

6. 利益結構
   - Western Union
   - Anchorage
   - Solana
   - 交易所
   - 託管商
   - agent
   - 使用者
   - 傳統 correspondent bank

7. 風險
   - 儲備風險
   - 贖回風險
   - 鏈上風險
   - 私鑰與託管風險
   - 監理風險
   - last-mile cash-out 風險
   - 交易所與流動性風險

請畫出兩個流程：
A. 傳統 SWIFT / correspondent banking 跨境支付流程
B. USDPT-based Western Union settlement flow

請明確標示：USDPT 取代的是 SWIFT 訊息層、銀行清算層、還是 Western Union 內部 agent settlement layer。
```

### 7.3 預期產出

```text
07_research_outputs/
├── usdpt_source_digest.md
├── swift_settlement_flow.md
├── usdpt_settlement_flow.md
├── usdpt_vs_swift_comparison_matrix.csv
└── usdpt_open_questions.md
```

---

## 8. 第五批研究：鏈上數據與市場資料

### 8.1 資料來源

```text
- Visa Onchain Analytics
- DeFiLlama Stablecoins
- Cambridge Digital Money Dashboard
- Artemis stablecoin data
- World Bank Remittance Prices Worldwide
```

### 8.2 給 GPT 的任務指令

```text
請根據可取得的鏈上與市場資料，建立穩定幣市場分析框架。

請整理：

1. 穩定幣總供給
2. 各穩定幣市占
3. 各鏈分布
4. 交易量
5. 轉帳量
6. 活躍地址
7. exchange flow / DeFi flow / payment flow 的區別
8. stablecoin velocity
9. peg deviation
10. 與傳統匯款成本或跨境支付資料的連結

請注意：
- dashboard 資料會變動，請標示資料抓取日期。
- 不要把交易所內部 wash volume 或智能合約重複轉帳直接當成真實支付需求。
- 請區分 adjusted transfer volume 與 raw transfer volume。
```

### 8.3 預期產出

```text
07_research_outputs/
├── onchain_data_source_map.md
├── stablecoin_market_metrics.csv
├── data_limitations.md
└── market_data_open_questions.md
```

---

## 9. 第六批研究：失敗案例與風險事件

### 9.1 建議補充案例

```text
- Terra UST
- Iron Finance
- Basis Cash
- USDC 2023 SVB depeg
- USDT historical reserve controversy
- DAI / USDS collateral risk episodes
- algorithmic stablecoin failures
```

### 9.2 給 GPT 的任務指令

```text
請整理穩定幣失敗案例，並分析失敗原因。

請針對每個案例整理：

1. 穩定幣類型
2. 穩定機制
3. 儲備資產或抵押品
4. 觸發事件
5. depeg 過程
6. 是否發生擠兌
7. 是否有流動性危機
8. 是否有治理或風控失敗
9. 監理後果
10. 對今日 USDC / USDT / USDPT / USDe / DAI 的啟示

請特別區分：
- fiat-backed stablecoin
- overcollateralized crypto-backed stablecoin
- algorithmic stablecoin
- synthetic dollar
- tokenized money market fund
```

---

## 10. 必須產出的中間文件

大量文件研究不要直接產出總報告。請先建立以下中間文件。

### 10.1 Source Digest

每份文件 200–500 字摘要。

```markdown
# Source Digest

## GENIUS_001 - GENIUS Act
- Publisher:
- Year:
- Document type:
- Main topic:
- Key claims:
- Useful sections:
- Relevance to research:
- Limitations:
```

### 10.2 Claim Table

每個重要主張都要有來源。

```csv
claim_id,claim,source_id,page_or_section,evidence,confidence,notes
CLAIM_001,GENIUS Act restricts reserve assets to cash/T-bills/repo/MMF,GENIUS_001,Sec X,"...",high,"Need exact section check"
```

### 10.3 Comparison Matrix

用來比較穩定幣、法規、央行觀點。

```csv
object,dimension,value,source_id,notes
USDC,reserve_assets,cash and short-term US Treasuries via reserve fund,USDC_001,Check latest report
USDT,reserve_assets,T-bills repo bitcoin gold loans etc,USDT_001,Depends on latest attestation
GENIUS,reserve_rule,1:1 permitted reserves,GENIUS_001,Need section citation
```

### 10.4 Open Questions

```markdown
# Open Questions

## USDPT
1. 是否已有完整 whitepaper？
2. 是否公開智能合約地址？
3. 是否已公布 reserve attestation？
4. 誰可以直接 redeem USDPT？
5. Western Union agents 是否直接持有 USDPT，還是只在後台 settlement 使用？

## USDT
1. 最新 reserve report 是否為完整 audit 或 limited assurance？
2. 其他投資與 secured loans 的比例如何變動？
```

---

## 11. 最終研究報告建議架構

```markdown
# 穩定幣生態與美元結算體系研究報告

## Executive Summary

## Chapter 1: 穩定幣不是獨立於美元體系，而是美元市場的鏈上封裝

## Chapter 2: 各類穩定幣的發行模式與資產負債表
- USDC
- USDT
- PYUSD
- USDPT
- RLUSD
- FDUSD
- GUSD
- DAI / USDS
- USDe

## Chapter 3: 美元貨幣市場與穩定幣儲備資產
- 銀行存款
- T-bills
- Repo
- MMF
- Fed reserve
- ON RRP
- SRF
- 一級交易商
- 託管銀行

## Chapter 4: 法規重塑穩定幣利益結構
- GENIUS Act
- CLARITY Act
- NYDFS
- MiCA
- BoE framework

## Chapter 5: 央行與國際機構如何看穩定幣
- 金融穩定
- 銀行中介
- 貨幣政策
- 數位美元化
- safe asset demand

## Chapter 6: USDPT 與 Western Union 跨境支付轉型
- 傳統 SWIFT / correspondent banking
- Western Union agent settlement
- USDPT 的可替代環節
- USDPT 的不可替代環節

## Chapter 7: 鏈上數據與真實支付需求
- supply
- transfer volume
- adjusted volume
- velocity
- chain distribution
- payment vs trading demand

## Chapter 8: 穩定幣風險與失敗案例
- depeg
- run risk
- reserve opacity
- collateral risk
- algorithmic failure
- synthetic dollar risk

## Chapter 9: 結論：穩定幣是美元金融體系的延伸，而不是替代美元
```

---

## 12. 給 GPT 的總控 Prompt

可以直接複製這段給 GPT：

```text
你是一位金融市場、貨幣市場、支付清算、穩定幣監理與鏈上數據研究員。

我會上傳一批穩定幣相關文件，包括：
1. 各穩定幣發行商文件
2. 法案與監理文件
3. 央行與國際機構研究
4. SWIFT / correspondent banking / Fedwire / CHIPS 文件
5. 鏈上與市場資料來源

請遵守以下規則：

1. 先建立 source map，不要直接寫結論。
2. 每份文件先做 source digest。
3. 所有重要主張都要進 claim table。
4. 沒有文件支持的內容請標示「目前文件未證實」。
5. 不要把新聞或二手文章當成主要證據。
6. 如果不同文件說法不同，請明確標示矛盾。
7. 如果文件過舊，請提醒可能已不適用。
8. HTML / dashboard 資料若是動態頁，請標示 access date。
9. 請區分 fiat-backed stablecoin、crypto-backed stablecoin、algorithmic stablecoin、synthetic dollar、tokenized MMF。
10. 最後才產出章節草稿與總報告。

第一階段任務：
請先根據我上傳的 source_registry.csv 與文件，建立：
1. source map
2. high-priority reading list
3. 每份文件的 200–500 字摘要
4. claim table 草稿
5. open questions list

請不要在第一階段直接寫完整研究報告。
```

---

## 13. 最重要的研究原則

> 大量文件研究不是一次問 GPT「幫我研究」，而是先建立 source map，再建立 source digest，再建立 claim table，最後才寫報告。

穩定幣研究尤其要避免以下錯誤：

1. 把 SWIFT 誤認為資金結算系統。
2. 把 stablecoin reserve attestation 誤認為完整 audit。
3. 把鏈上交易量誤認為真實支付量。
4. 把 USDT / USDC / USDe / DAI 視為同一類風險。
5. 把 GENIUS Act 的合規穩定幣視為完全無風險。
6. 忽略持有人是否有直接贖回權。
7. 忽略穩定幣收益到底歸誰。
8. 忽略銀行、貨幣基金、託管銀行、一級交易商在底層美元市場的角色。
