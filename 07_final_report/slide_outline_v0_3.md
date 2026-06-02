# Slide Outline v0.3 Clean Build (2026-05-15)

Purpose: clean Traditional Chinese slide outline for the 2026-06-27 reading
group. The expanded speaker script is
`07_final_report/slide_script_v0_3.md`.

## Part 0 - Opening

| Slide | Title | Takeaway | Claims |
| --- | --- | --- | --- |
| 1 | 穩定幣研究 | 穩定幣是美元資產、支付網絡與監理規則的鏈上重組。 | chapter 1.1 |
| 2 | 為什麼 2026 要談 | GENIUS、MiCA、BoE 與 USDPT 讓穩定幣從市場議題變成制度議題。 | CLAIM_082, CLAIM_069, CLAIM_090, CLAIM_051 |
| 3 | 範圍與方法 | 研究包以 registry -> digest -> claim -> matrix -> chapter -> slide 追溯。 | AGENTS.md, KF_032, KF_033 |
| 4 | 三種產品不能混在一起 | Fiat-backed、crypto/RWA-collateralised、synthetic-dollar 風險通道不同。 | CLAIM_026, CLAIM_098, CLAIM_103 |
| 5 | 五個研究護欄 | Attestation, redemption, volume, USDPT, MiCA ART/EMT 都要分清楚。 | chapter 1.4 |

## Part 1 - Issuer Ecosystem

| Slide | Title | Takeaway | Claims |
| --- | --- | --- | --- |
| 6 | 八個法幣擔保發行架構 | 同樣錨定美元，不代表同樣發行人、贖回權、凍結權與收益結構。 | CLAIM_026-035, CLAIM_058-081 |
| 7 | USDC：Circle Mint 門檻 | USDC 的直接贖回權由 Circle Mint 資格決定。 | CLAIM_026, CLAIM_027, CLAIM_058, CLAIM_059 |
| 8 | USDT：驗證客戶與非現金曝險 | USDT 有顯著 T-bill、gold、Bitcoin 曝險，直接贖回是 verified customer 權利。 | CLAIM_028, CLAIM_029, CLAIM_060, CLAIM_061 |
| 9 | Paxos 家族 | PYUSD、USDP、USDG 的 Paxos Customer gating 是共同模式。 | CLAIM_072-076 |
| 10 | USDP：獨立儲備組成報告已停止 | USDP 缺口應重分類為 issuer-discontinued separate report。 | CLAIM_080, CLAIM_081 |
| 11 | GUSD：Gemini Customer 權利 | GUSD 由 Gemini Customer pathway 與三類 reserve account 支撐。 | CLAIM_077, CLAIM_078, CLAIM_079 |
| 12 | RLUSD：紐約信託架構 | RLUSD reserve/custody evidence 強於直接贖回與 contract-control evidence。 | CLAIM_032, CLAIM_033, CLAIM_057 |
| 13 | FDUSD：FD121 帳戶門檻 | FDUSD/FDD 贖回由 FD121 Account、暫停限制與 U.S. person exclusion 形塑。 | CLAIM_062-064 |
| 14 | DAI、USDS：Maker 到 Sky | DAI/USDS 是 protocol-collateralised，不是 fiat-backed payment stablecoin。 | CLAIM_098-102 |
| 15 | USDe：synthetic dollar | USDe 依靠 spot backing、short perp hedge、OES custody 與 Reserve Fund。 | CLAIM_065-067, CLAIM_103-106 |
| 16 | 直接贖回權的共同模式 | 直接贖回多半需要 KYC、合格地區、帳戶良好與 issuer 未暫停。 | CLAIM_058, CLAIM_060, CLAIM_062, CLAIM_065, CLAIM_073, CLAIM_077 |

## Part 2 - Reserves and Dollar Money Markets

| Slide | Title | Takeaway | Claims |
| --- | --- | --- | --- |
| 17 | 儲備資產比較 | Fiat-backed stablecoins 連到 deposits、T-bills、repo、MMF 與 custody。 | CLAIM_026, CLAIM_028, CLAIM_075, CLAIM_078, CLAIM_084 |
| 18 | USDC vs USDT | 兩者都錨定美元，但儲備輪廓與披露架構不同。 | CLAIM_026-029 |
| 19 | T-bill 需求通道 | Stablecoin growth 可能影響短期安全資產需求，但不是機械結論。 | CLAIM_084, BIS_003, ECB_003 |
| 20 | DAI、USDe 不能併入同一模型 | Protocol / synthetic designs 不應併入 fiat-backed reserve channel。 | CLAIM_098, CLAIM_103, CLAIM_106 |
| 21 | 儲備收益的不對稱 | Issuer 可獲 reserve income，holder 多半不取得 reserve yield。 | CLAIM_059, CLAIM_066, CLAIM_071, CLAIM_074, CLAIM_086 |

## Part 3 - Law and Regulation

| Slide | Title | Takeaway | Claims |
| --- | --- | --- | --- |
| 22 | 四個監理基準 | GENIUS、MiCA、BoE、NYDFS 重疊但不相同。 | CLAIM_036-043, CLAIM_069-071, CLAIM_082-097, CLAIM_126-131 |
| 23 | GENIUS：發行人門檻 | GENIUS 先定義誰能發行、誰能在美國市場流通，以及 foreign issuer screen。 | CLAIM_082, CLAIM_083, CLAIM_126 |
| 24 | GENIUS：儲備資產清單 | GENIUS 列出 cash、93-day Treasuries、overnight repo、MMF 等儲備。 | CLAIM_084, CLAIM_085 |
| 25 | GENIUS：收益禁止與破產順位 | GENIUS 禁止 holder yield 並建立 customer priority。 | CLAIM_086, CLAIM_087 |
| 26 | MiCA：ART 與 EMT | ART 與 EMT 是兩套規則，reserve、redemption 與 interest rules 不同。 | CLAIM_042, CLAIM_043, CLAIM_069-071, CLAIM_127, CLAIM_128 |
| 27 | MiCA：重大代幣與復原計畫 | Significant-token layer 增加 EBA supervision、recovery、wind-down 與 non-euro derogation。 | CLAIM_094-097, CLAIM_129 |
| 28 | BoE：100% CBD 到 40/60 | BoE 從 100% central-bank deposits 轉向 40% CBD + 60% UK debt，並納入 cross-border use framing。 | CLAIM_088-090, CLAIM_130, CLAIM_131 |
| 29 | BoE：持有上限 | BoE proposed GBP 20,000 individual and GBP 10m business holding limits。 | CLAIM_091 |
| 30 | ESMA：CASP 與 transfer service | ESMA 展示 MiCA authorisation 與 transfer-service 監理實務。 | CLAIM_092, CLAIM_093 |
| 31 | 跨法域比較：發行人、儲備、贖回 | 比較各制度的 issuer、reserve、redemption 三個維度。 | chapter 4 table |
| 32 | 跨法域比較：破產、收益、重大門檻 | 比較 insolvency、holder yield、significant-token threshold。 | chapter 4 table |

## Part 4 - Central Bank and Policy Framing

| Slide | Title | Takeaway | Claims |
| --- | --- | --- | --- |
| 33 | Fed：條件式銀行通道 | Stablecoin 對銀行影響取決於需求來源、儲備配置與 backing model。 | CLAIM_044, CLAIM_047, CLAIM_048 |
| 34 | IMF：穩定化的代價 | Safe-asset backing 降低 run risk 但可能壓低 issuer profitability。 | CLAIM_049 |
| 35 | IMF：18% 與 US$300bn | 這是 payment firms 的市場預期反應，不是已實現 adoption。 | CLAIM_050 |
| 36 | 台灣場景綜整 | 台灣問題聚焦 NTD stablecoin、USD stablecoin、FX monitoring、dollarisation 與 M2/credit channel。 | CLAIM_112-118 |

## Part 5 - USDPT and Cross-Border Payments

| Slide | Title | Takeaway | Claims |
| --- | --- | --- | --- |
| 37 | USDPT 已有證據 | USDPT launch / issuer / chain / Fireblocks infrastructure 有初步證據。 | CLAIM_051-053 |
| 38 | 四層拆解 | USDPT 討論必須拆成 UX、agent network、on-chain transfer、bank settlement。 | chapter 6 |
| 39 | USDPT 尚未取得文件 | product terms、reserve report、contract addresses、workflow 都仍缺。 | unresolved_open_questions |
| 40 | USDPT 的安全說法 | 可說 digital-asset settlement layer，不可說 replaces SWIFT。 | chapter 6 |

## Part 6 - On-Chain Data

| Slide | Title | Takeaway | Claims |
| --- | --- | --- | --- |
| 41 | 轉帳量不是支付需求 | Raw transfer volume 需要調整，不能直接當 payment demand。 | chapter 7 |
| 42 | DeFiLlama 可以說什麼 | DeFiLlama 支撐 supply / chain distribution，不支撐 adjusted payment volume。 | CLAIM_054 |
| 43 | 還缺哪些 adjusted data | Visa、Artemis、Cambridge、McKinsey/Artemis、World Bank exports 仍缺。 | 09_data_exports README |

## Part 7 - Failure Cases

| Slide | Title | Takeaway | Claims |
| --- | --- | --- | --- |
| 44 | 風險分類 | v0.3 支撐 risk taxonomy，但不支撐完整 price/depeg timelines。 | CLAIM_069, CLAIM_075, CLAIM_084, CLAIM_090, CLAIM_094, CLAIM_098, CLAIM_103, CLAIM_106 |
| 45 | 事件教訓變成研究護欄 | Failure cases 強化 attestation、redemption、volume、USDPT、ART/EMT guardrails。 | CLAIM_107-111 |

## Part 8 - Closing

| Slide | Title | Takeaway | Claims |
| --- | --- | --- | --- |
| 46 | 證據可以支持什麼 | 高信心結論集中在 dollar liquidity、redemption gating、regulatory baselines。 | chapter 9.1 |
| 47 | 哪些結論仍是條件式 | USDPT 與 payment demand 都仍需要新 primary evidence。 | chapter 9.2 |
| 48 | 未解問題 | USDPT、adjusted volume、Taiwan enacted law、failure-case timelines、Maker Black Thursday。 | chapter 9.3 |
| 49 | 讀書會討論題 | 討論風險落點、法規目的與台灣的美元化問題。 | chapter 9.4 |

## Appendix

| Slide | Title | Takeaway | Claims |
| --- | --- | --- | --- |
| A1 | Claim 對照 | 每個大結論都可追到 claim table 和 source registry。 | PROJECT_METHODOLOGY_001 |
| A2 | 使用限制 | 非投資建議；USDPT inferred；attestation not audit；volume not demand。 | AGENTS.md |
| A3 | 資料庫狀態 | 131 claims validated, 137 source rows, no high-priority missing local files。 | README |
