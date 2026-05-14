# Slide Outline — v0.3 (2026-05-15)

讀書會：2026-06-27 穩定幣研究 / Stablecoin Ecosystem Research

對象（audience）: 學術導向讀書會成員 — academic-leaning reading-group members.
語言（language）: 投影片以中文呈現 / slides delivered in Traditional Chinese; based on
the English narrative documents (`executive_summary.md`, chapter 1, chapter 9).
張數（slide count）: 目前約 49 張，視時間可再砍。

## How to read this outline

每張 slide 包含四欄資訊：

- **Slide #** — sequential number.
- **EN title / 中文標題** — bilingual slide title; the Chinese title is what
  appears on the rendered slide, the English title is for cross-reference to
  the chapter drafts.
- **Takeaway（中文）** — 投影片要讓聽眾帶走的那一句話（≤30 字）。
- **Source claims** — `CLAIM_XXX` IDs that anchor the slide content; speaker
  notes should cite these in long form.

Speaker notes language: bilingual is OK; recommended pattern is English
analytical statement (≤2 sentences) followed by Chinese delivery prompt.

# Part 0 — Opening（開場：5 張）

## Slide 1

- **EN title / 中文標題**: Title / 標題頁
- **Takeaway**: 穩定幣不是另一種貨幣，是把美元工具上鏈包裝的負債。
- **Source claims**: framing — chapter 1.1

## Slide 2

- **EN title / 中文標題**: Why this matters now / 為什麼在 2026 談這件事
- **Takeaway**: GENIUS Act 已立法、MiCA 已全面適用、BoE 2025 諮詢、Western Union USDPT 宣布，四件事同年發生。
- **Source claims**: CLAIM_082, CLAIM_069, CLAIM_090, CLAIM_051

## Slide 3

- **EN title / 中文標題**: Scope & method / 研究範圍與方法
- **Takeaway**: 106 條 source-backed claim、130 個 archived source、registry → digest → claim → matrix → chapter 五層 traceability。
- **Source claims**: AGENTS.md 工作流；chapter 1.6

## Slide 4

- **EN title / 中文標題**: Three product categories / 三類穩定幣不能混為一談
- **Takeaway**: Fiat-backed / Crypto-RWA-collateralised / Synthetic-dollar 三類風險通道完全不同。
- **Source claims**: CLAIM_026 USDC, CLAIM_098 DAI/USDS, CLAIM_103 USDe

## Slide 5

- **EN title / 中文標題**: Five guardrails / 五條本研究刻意守住的分界
- **Takeaway**: Attestation ≠ Audit；Product page ≠ Direct right；Volume ≠ Payment demand；USDPT ≠ SWIFT 取代；ART ≠ EMT。
- **Source claims**: chapter 1.4 全段

# Part 1 — Issuer ecosystem（發行者：10 張）

## Slide 6

- **EN title / 中文標題**: Eight fiat-backed issuers at a glance / 八家法幣支撐型發行者全覽
- **Takeaway**: USDC、USDT、PYUSD、USDP、USDG、RLUSD、FDUSD、GUSD 各自在不同司法管轄下被監管。
- **Source claims**: CLAIM_001-035, CLAIM_058-068, CLAIM_072-081
- **Visual**: issuer matrix 重新排版為投影片表格

## Slide 7

- **EN title / 中文標題**: USDC — Circle Mint gating / USDC：Circle Mint 帳戶閘門
- **Takeaway**: 「Redeemable at par」不等於人人能贖；直接贖回限 Circle Mint 帳戶持有人。
- **Source claims**: CLAIM_026, CLAIM_027, CLAIM_058, CLAIM_059

## Slide 8

- **EN title / 中文標題**: USDT — verified customer + non-cash exposures / USDT：驗證客戶限定＋非現金部位
- **Takeaway**: 約 141bn T-bill ＋ 20bn 黃金 ＋ 7bn BTC，不應以純 cash equivalent 模型分析。
- **Source claims**: CLAIM_028, CLAIM_029, CLAIM_060, CLAIM_061

## Slide 9

- **EN title / 中文標題**: Paxos family — unified terms govern PYUSD / USDP / USDG / Paxos 體系：三幣同一條款
- **Takeaway**: Paxos Trust 發行 PYUSD/USDP；Paxos Digital + PIE 共同發行 USDG；只有 Paxos Customer 能直接贖回。
- **Source claims**: CLAIM_072, CLAIM_073, CLAIM_074, CLAIM_075, CLAIM_076

## Slide 10

- **EN title / 中文標題**: USDP — discontinued separate reserve report / USDP：月度儲備組成報告已停發
- **Takeaway**: KPMG AICPA attestation 月度仍出，但 separate reserve composition report 已被發行人主動停發。
- **Source claims**: CLAIM_080, CLAIM_081

## Slide 11

- **EN title / 中文標題**: GUSD — Gemini Customer only + three reserve accounts / GUSD：限 Gemini 客戶＋三類儲備帳戶
- **Takeaway**: 非 Gemini 客戶持有 GUSD 與 Gemini 之間「不存在任何關係」；贖回承諾為 T+1 Business Day。
- **Source claims**: CLAIM_077, CLAIM_078, CLAIM_079

## Slide 12

- **EN title / 中文標題**: RLUSD — Standard Custody NY trust / RLUSD：紐約信託發行
- **Takeaway**: NYDFS 監理的 New York limited purpose trust company 發行；BNY 為主託管。
- **Source claims**: CLAIM_007, CLAIM_008, CLAIM_032, CLAIM_033, CLAIM_057

## Slide 13

- **EN title / 中文標題**: FDUSD — FDD/FDUSD via FD121 (BVI) / FDUSD：FDD 條款下的 BVI 發行架構
- **Takeaway**: 直接 sell to FD121 需 FD121 Account；條款排除美國個人 / 機構。
- **Source claims**: CLAIM_009, CLAIM_010, CLAIM_062, CLAIM_063, CLAIM_064

## Slide 14

- **EN title / 中文標題**: DAI / USDS — Maker → Sky rebrand / DAI/USDS：MakerDAO 轉 Sky Protocol
- **Takeaway**: 超額抵押 + Vault + Liquidation Auction + Emergency Shutdown；sUSDS 為 yield wrapper；美國不可用。
- **Source claims**: CLAIM_098, CLAIM_099, CLAIM_100, CLAIM_101, CLAIM_102
- **Visual**: 建議新增 Vault → Liquidation Auction → Surplus 流程圖

## Slide 15

- **EN title / 中文標題**: USDe — synthetic dollar via delta-neutral hedge / USDe：合成美元、Delta-中性對沖
- **Takeaway**: 1:1（非超額）抵押；現貨在 Off-Exchange Custody、空頭 perp 在交易所；月度 custodian attestation 聲明 backing assets 不在交易所。
- **Source claims**: CLAIM_065, CLAIM_066, CLAIM_067, CLAIM_103, CLAIM_104, CLAIM_105, CLAIM_106
- **Visual**: 建議新增 spot + short perp 對沖示意圖

## Slide 16

- **EN title / 中文標題**: Direct redemption gating — the recurring pattern / 直接贖回閘門：一個重複出現的模式
- **Takeaway**: USDC / USDT / FDUSD / Paxos 家族 / GUSD / USDe 都以「客戶身分 + KYC + 適格管轄」當贖回門檻，無人例外。
- **Source claims**: CLAIM_058, CLAIM_060, CLAIM_062, CLAIM_065, CLAIM_073, CLAIM_077

# Part 2 — Reserves & dollar money markets（儲備與美元貨幣市場：5 張）

## Slide 17

- **EN title / 中文標題**: Reserve composition matrix / 儲備組成對照
- **Takeaway**: 各發行者揭露的儲備類別重疊但不一致；T-bills 是最大公因數。
- **Source claims**: CLAIM_026, CLAIM_028, CLAIM_034, CLAIM_075, CLAIM_078
- **Visual**: 跨發行者儲備類別熱力表（slide-ready）

## Slide 18

- **EN title / 中文標題**: USDC vs USDT — same wrapper, different backing / USDC vs USDT：同樣的包裝、不同的底層
- **Takeaway**: USDC 主要為 cash + 短 T-bills + Circle Reserve Fund；USDT 含 gold 與 BTC，不能視為純現金替代。
- **Source claims**: CLAIM_026, CLAIM_027, CLAIM_028, CLAIM_029
- **Visual**: 兩個圓餅圖並列

## Slide 19

- **EN title / 中文標題**: T-bill demand channel / 對短期國債需求的傳遞通道
- **Takeaway**: Fiat-backed 規模成長 → 對 ≤93 天 T-bill / overnight repo / govt MMF shares 的需求；BIS / ECB 已建模此通道。
- **Source claims**: CLAIM_026, CLAIM_028, CLAIM_075, CLAIM_084；BIS WP1270, ECB WP3174

## Slide 20

- **EN title / 中文標題**: Why crypto/RWA and synthetic stablecoins do not aggregate / 為什麼 DAI/USDS 與 USDe 不能與 fiat-backed 加總
- **Takeaway**: DAI/USDS 透過 RWA Vault 與 PSM；USDe 透過 perp hedge；兩者進入美元貨幣市場的通道與規模都不同。
- **Source claims**: CLAIM_098, CLAIM_103, CLAIM_106；chapter 3 guardrail 段

## Slide 21

- **EN title / 中文標題**: Reserve income asymmetry / 儲備收益歸誰
- **Takeaway**: 發行者收儲備收益、持有人合約上明文沒有 yield 權利；GENIUS / MiCA 均統一禁止 holder yield。
- **Source claims**: CLAIM_059, CLAIM_066, CLAIM_071, CLAIM_074, CLAIM_086

# Part 3 — Law & regulation（法律與監管：11 張）

## Slide 22

- **EN title / 中文標題**: Four jurisdictions on one map / 四司法管轄一覽
- **Takeaway**: GENIUS（美國聯邦）、MiCA ART + EMT（歐盟）、BoE 系統性穩定幣（英國）、NYDFS（紐約州）：架構相近、細節差異實質。
- **Source claims**: CLAIM_082-087, CLAIM_069-071, CLAIM_088-091, CLAIM_036-040

## Slide 23

- **EN title / 中文標題**: GENIUS Act — eligible issuer & transition / GENIUS Act：適格發行者與三年過渡
- **Takeaway**: 非 permitted issuer 不得在美國發行；3 年後 DASP 不得分銷非適格發行者所發；外國發行者須具備守 lawful order 能力。
- **Source claims**: CLAIM_082, CLAIM_083

## Slide 24

- **EN title / 中文標題**: GENIUS Act — reserve composition rule / GENIUS Act：儲備組成規則
- **Takeaway**: 列舉式 HQLA 清單；T-bill 上限 93 天到期；repo / reverse repo 隔夜；MMF 僅得投資前述底層；月度披露 + 註冊會計師檢視 + CEO/CFO 刑責認證。
- **Source claims**: CLAIM_084, CLAIM_085

## Slide 25

- **EN title / 中文標題**: GENIUS Act — yield prohibition & insolvency priority / GENIUS Act：禁付收益＋客戶破產優先
- **Takeaway**: 任何 issuer 不得單純因 holding/use/retention 而給予 holder 利息或收益；破產時客戶對其持有 stablecoin 之債權優先於非客戶。
- **Source claims**: CLAIM_086, CLAIM_087

## Slide 26

- **EN title / 中文標題**: MiCA ART vs EMT / MiCA：ART 與 EMT 是兩套規則
- **Takeaway**: ART Article 36/39/40：reserve segregation、permanent redemption、no interest；EMT Article 49/54：at-par redemption、30% 同幣別存款。
- **Source claims**: CLAIM_042, CLAIM_043, CLAIM_069, CLAIM_070, CLAIM_071

## Slide 27

- **EN title / 中文標題**: MiCA significant-token + recovery / redemption plans / MiCA significant-token 與復原 / 贖回計畫
- **Takeaway**: EBA 監管 significant ART/EMT；ART 須備 recovery plan（含暫停贖回選項）+ redemption plan（含臨時管理人）；significant EMT 半年 audit。
- **Source claims**: CLAIM_094, CLAIM_095, CLAIM_096, CLAIM_097

## Slide 28

- **EN title / 中文標題**: BoE 2023 → 2025 evolution / BoE：從 100% 央行存款到 40/60 split
- **Takeaway**: 2023 偏好 100% 央行存款；2025 改為至少 40% 央行存款（不付息）＋ 最多 60% 短期英國公債；step-up 規定發行初期可達 95% 公債。
- **Source claims**: CLAIM_088, CLAIM_089, CLAIM_090

## Slide 29

- **EN title / 中文標題**: BoE holding limits — a UK-only feature / BoE 持有上限：英國獨有設計
- **Takeaway**: 個人 £20,000 / per-coin、企業 £10 million；零售商與服務於零售客戶之中介可申請豁免；GENIUS 與 MiCA 皆無此類量化上限。
- **Source claims**: CLAIM_091

## Slide 30

- **EN title / 中文標題**: ESMA supervisory practice / ESMA：實務監管預期
- **Takeaway**: 「沒有低風險 CASP」；加重審查門檻（1M EU 用戶 / €3B BS / 跨境用戶 / 複雜集團 / 關鍵職能外包）；Article 82 transfer service 須符 TOFR Article 14。
- **Source claims**: CLAIM_092, CLAIM_093

## Slide 31

- **EN title / 中文標題**: Cross-jurisdiction comparison (1/2) — issuer / reserve / redemption / 跨管轄比較（上）
- **Takeaway**: 五制度（GENIUS、MiCA ART、MiCA EMT、BoE、NYDFS）在「適格發行者」、「儲備組成」、「贖回權」三維上的並列對比。
- **Source claims**: chapter 4 末比較表上半
- **Visual**: 三欄表格直接搬到投影片

## Slide 32

- **EN title / 中文標題**: Cross-jurisdiction comparison (2/2) — insolvency / yield / significance / 跨管轄比較（下）
- **Takeaway**: 五制度在「破產 / 清算」、「持有人收益」、「significant-token 門檻」三維上的並列對比。
- **Source claims**: chapter 4 末比較表下半
- **Visual**: 三欄表格直接搬到投影片

# Part 4 — Central-bank & policy framing（央行與政策框架：4 張）

## Slide 33

- **EN title / 中文標題**: Fed IFDP 1334 — a conditional channel / Fed IFDP 1334：取決於模型的傳遞通道
- **Takeaway**: 衝擊取決於資金來源與儲備組成；two-tiered banking 可共存，narrow bank 模型則加深 disintermediation 但強化 peg。
- **Source claims**: CLAIM_044, CLAIM_047, CLAIM_048

## Slide 34

- **EN title / 中文標題**: IMF — Making Stablecoins Stable / IMF：穩定幣穩定化的取捨
- **Takeaway**: 無監管均衡為次優；安全資產支撐能降低 run 風險但壓縮發行誘因；需替代營收機制。
- **Source claims**: CLAIM_049

## Slide 35

- **EN title / 中文標題**: IMF — 18% / $300bn event study / IMF：18% / $300bn 事件研究
- **Takeaway**: 美國有利穩定幣法案訊息使既有上市支付公司市值縮水 18%（~$300bn）；屬市場預期證據，不是已實現的支付採用。
- **Source claims**: CLAIM_050

## Slide 36

- **EN title / 中文標題**: Taiwan-specific synthesis — open / 台灣場景綜整：尚未做
- **Takeaway**: NTD 穩定幣、FX 監控、digital dollarisation、deposit substitution、貨幣主權——已具備 Fed / IMF 框架，但本研究尚未取既有 CBC / TWFRC 來源做台灣綜整。
- **Source claims**: unresolved_open_questions.md / chapter 9.3 第 5 點

# Part 5 — USDPT and cross-border（USDPT 與跨境支付：4 張）

## Slide 37

- **EN title / 中文標題**: What is documented about USDPT / USDPT：目前已有的證據
- **Takeaway**: Western Union 宣布、Anchorage Digital Bank 為發行人（依其 OCC 評論信）、Fireblocks 提供 wallet / settlement 基礎設施。
- **Source claims**: CLAIM_051, CLAIM_052, CLAIM_053

## Slide 38

- **EN title / 中文標題**: Four-layer separation / 四層分離框架
- **Takeaway**: 必須分（a）消費者匯款 UX、（b）WU 代理網絡、（c）內部 / 代理結算、（d）銀行 / correspondent 結算，不可一概以「USDPT 取代 SWIFT」概括。
- **Source claims**: chapter 6 framing；AGENTS.md guardrail
- **Visual**: 既有 usdpt_settlement_flow.md（建議重畫為四層 swim-lane）

## Slide 39

- **EN title / 中文標題**: What is NOT documented (frozen) / 尚未取得（且決定 freeze）
- **Takeaway**: Product terms、reserve report、合約地址、end-to-end workflow 都不在公開檔案中；v0.3 決定 freeze、不啟動 scraping。
- **Source claims**: chapter 9.2.1；unresolved_open_questions.md

## Slide 40

- **EN title / 中文標題**: Why conditional framing matters / 為何必須條件式敘事
- **Takeaway**: 在沒有 workflow 文件之前，「USDPT 取代 SWIFT / correspondent banking / Fedwire / CHIPS / WU 零售匯款管道」皆無法支撐；本研究刻意保留 conditional 語氣。
- **Source claims**: AGENTS.md non-negotiable rule #4；chapter 6 framing

# Part 6 — On-chain data（鏈上數據：3 張）

## Slide 41

- **EN title / 中文標題**: Volume ≠ payment demand / 轉帳量不等於支付需求
- **Takeaway**: 鏈上 transfer volume 包含交易所流動、橋接、套利、協議內部流動；不能直接視為實際支付需求。
- **Source claims**: AGENTS.md non-negotiable rule #5；chapter 7 framing

## Slide 42

- **EN title / 中文標題**: What DeFiLlama supply data can and cannot say / DeFiLlama 供給資料的可用範圍
- **Takeaway**: 供給快照可分析鏈別 / 發行者分布；不可代用為支付規模或實際使用率。
- **Source claims**: CLAIM_054（Artemis methodology basis）；market_data_source_digest

## Slide 43

- **EN title / 中文標題**: What is missing / 缺什麼
- **Takeaway**: Visa Onchain Analytics adjusted-volume export、Artemis methodology 超出 CLAIM_054 的部分、McKinsey-Artemis 聯合分析皆未取得；v0.3 freeze。
- **Source claims**: unresolved_open_questions.md v0.2 deferrals

# Part 7 — Failure cases（失敗案例：2 張，視時間可省）

注意：v0.3 對失敗案例的「分類」已 anchored 到既有 claim；但「個案研究」（Terra UST、Iron Finance、USDC SVB depeg、Tether 歷史儲備爭議、DAI 黑色星期四）在 v0.3 不在 source archive 內。投影片若要含個案，需由報告人自行引用，或 commission v0.4 extraction。

## Slide 44

- **EN title / 中文標題**: Risk taxonomy anchored to v0.3 evidence / v0.3 evidence 已支撐的風險分類
- **Takeaway**: 八類風險（reserve / 贖回 / 銀行存款 / 市場流動性 / oracle / governance / basis / 監管）已對應到既有 claim，可說「我們知道風險存在於哪些通道」。
- **Source claims**: chapter 8.1 全段；CLAIM_069, CLAIM_075, CLAIM_084, CLAIM_090, CLAIM_094, CLAIM_098, CLAIM_101, CLAIM_103, CLAIM_106

## Slide 45

- **EN title / 中文標題**: Lessons preserved as guardrails / 失敗案例如何形塑研究 guardrail
- **Takeaway**: 過去事件直接落地為本研究的五條 guardrail（attestation / direct right / volume / USDPT / ART vs EMT）；個案層尚為 v0.4 open work。
- **Source claims**: AGENTS.md non-negotiable rules；chapter 8.3 / 8.4

# Part 8 — Closing（收尾：4 張）

## Slide 46

- **EN title / 中文標題**: What the evidence supports / 證據可支撐什麼
- **Takeaway**: 六條高信心 finding：reconfiguration、redemption gating、attestation ≠ audit、四司法管轄分歧、央行條件式通道、三類產品不可加總。
- **Source claims**: chapter 9.1 全段

## Slide 47

- **EN title / 中文標題**: What is conditional / 條件式可言
- **Takeaway**: USDPT 為 planned product、payment volume 為定性而非數量級結論。
- **Source claims**: chapter 9.2

## Slide 48

- **EN title / 中文標題**: What remains unresolved / 五項仍未解
- **Takeaway**: USDPT 產品層、adjusted volume、CLARITY、跨境等價認定、台灣綜整。
- **Source claims**: chapter 9.3

## Slide 49

- **EN title / 中文標題**: Reading-group framing questions / 留給讀書會的三個問題
- **Takeaway**: (1) 「對哪個持有人、對哪個 counterparty、在哪個司法管轄」才是真正的問題；(2) 儲備規則正在收斂、但速度不一；(3) 監管範圍與經濟範圍是否對齊。
- **Source claims**: chapter 9.4 三點

# Appendix slides（附錄，視聽眾時間決定是否放）

## Slide A1

- **EN title / 中文標題**: Claim map / 引用對照表
- **Takeaway**: 投影片內的來源簡稱對應到 CLAIM_XXX 與 source_id 的完整查證路徑。
- **Source claims**: 全部 106 條，附表

## Slide A2

- **EN title / 中文標題**: Disclaimer / 免責與範圍
- **Takeaway**: 本研究不構成投資建議；USDPT workflow 為 inferred；儲備數字為點時間 attestation；volume ≠ payment demand。
- **Source claims**: AGENTS.md non-negotiable rules

## Slide A3

- **EN title / 中文標題**: Source registry / 來源登錄
- **Takeaway**: 130 個 archived source 與其在 stablecoin-ecosystem-research/01_sources/source_registry.csv 的對應。
- **Source claims**: 全 registry

# Notes for the next expansion step

When expanding this outline into a full speaker-script document
(`slide_script_v0_3.md` in a future pass), recommended convention:

- Keep slide titles bilingual but consolidate the in-slide body in
  Traditional Chinese.
- For each numerical figure (USDT $141bn T-bill, BoE £20,000 limit, USDe
  Reserve Fund $46.6m, IMF 18% / $300bn), add a footnote line below the
  bullet with the `CLAIM_XXX` ID and the as-of date.
- For each diagram referenced (`Visual:` line above), decide whether to
  reuse the Mermaid source from `06_flow_diagrams/`, redraw in
  Keynote/PowerPoint shapes, or attach as a rendered image. Three of the
  six Mermaid diagrams need refresh before reuse — see the v0.3 sync note
  in this file's companion review.
- Slide 4 (three product categories) and Slides 22 / 31 / 32
  (jurisdictional comparison) are the load-bearing comparative visuals. If
  total slide count is later cut, prioritise keeping these four.
