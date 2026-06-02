# Slide Script v0.3 Clean Build (2026-05-15)

Reading group date: 2026-06-27

Audience: academic-leaning reading-group members.

Language convention: slide body text is in Traditional Chinese; speaker notes
are bilingual, with English as the analytical backbone and Chinese as the
delivery cue.

Evidence convention: every slide points back to `CLAIM_XXX`, a chapter
section, or a project guardrail. Full citations live in
`03_claim_tables/claim_table_master.csv` and
`01_sources/source_registry.csv`.

# Part 0 - Opening

## Slide 1 - Title / 穩定幣研究

**Body**

> 穩定幣不是美元體系之外的替代品  
> 它是美元資產、支付網絡與監理規則的鏈上重組  
> 讀書會版本：2026-06-27  
> v0.3.2 evidence base: 131 claims, 137 sources

**Speaker notes**

This opening frames stablecoins as a reconfiguration of the dollar system,
not as a clean break from it. The point is not to ask whether stablecoins
are "real money" in the abstract, but to trace the institutions, assets,
contracts, and rules that make them work.

中文提示：先把聽眾帶進研究問題。今天不是介紹幣種清單，而是拆解穩定幣怎樣把美元資產、金融機構與鏈上轉帳包在一起。

**Source claims**: chapter 1.1, KF_032, KF_033

## Slide 2 - Why This Matters Now / 為什麼 2026 要談

**Body**

> 2026 的穩定幣議題同時發生在三條線上：  
> 1. 美國 GENIUS Act 進入聯邦法制  
> 2. 歐盟 MiCA ART / EMT 規則已運作  
> 3. BoE 系統性穩定幣規則從 100% CBD 轉向 40/60  
> 4. Western Union 宣布 USDPT 與 Digital Asset Network

**Speaker notes**

The reason this is timely is institutional convergence. Stablecoins have
moved from a crypto-market instrument into a statutory, central-bank, and
payment-infrastructure question.

中文提示：強調這不是市場熱點而已，而是法規、央行、支付公司同時動起來的時間點。

**Source claims**: CLAIM_082, CLAIM_069, CLAIM_090, CLAIM_051

## Slide 3 - Scope and Method / 範圍與方法

**Body**

> 本研究不是單篇 memo  
> 它是一組可追溯研究包：  
> registry -> digest -> claim table -> matrix -> chapter -> slide  
>  
> 截至 v0.3：  
> 131 筆 claim  
> 137 筆 source registry rows

**Speaker notes**

The claim table is the control layer. If a major conclusion cannot be traced
to a source and a claim ID, it should remain framed as open or conditional.

中文提示：讓聽眾知道，今天每個大結論都有可回查的 claim ID，不是只靠敘事推論。

**Source claims**: AGENTS.md rules, KF_032, KF_033

## Slide 4 - Three Product Categories / 三種產品不能混在一起

**Body**

> 1. Fiat-backed payment stablecoins  
> USDC, USDT, PYUSD, USDP, USDG, RLUSD, FDUSD, GUSD  
>  
> 2. Crypto / RWA-collateralised protocol stablecoins  
> DAI / USDS  
>  
> 3. Synthetic-dollar instruments  
> USDe / sUSDe

**Speaker notes**

The most common analytical mistake is aggregating all stablecoins into one
risk class. These three categories transmit risk through different balance
sheets, contracts, collateral channels, and governance systems.

中文提示：這張是全場的分類底盤。後面所有比較都要先問：我們談的是哪一類穩定幣？

**Source claims**: CLAIM_026, CLAIM_098, CLAIM_103

## Slide 5 - Five Guardrails / 五個研究護欄

**Body**

> 1. Attestation 不等於 audit  
> 2. Product page 不等於直接贖回權  
> 3. Raw volume 不等於 payment demand  
> 4. USDPT 不等於 SWIFT replacement  
> 5. MiCA ART 不等於 MiCA EMT

**Speaker notes**

These five distinctions prevent the deck from overstating the evidence. They
are not caveats at the margin; they are the method.

中文提示：把這張講成今天的「防誤讀清單」。後面每個章節都會回到這五點。

**Source claims**: chapter 1.4, AGENTS.md non-negotiable rules

# Part 1 - Issuer Ecosystem

## Slide 6 - Eight Fiat-Backed Issuers / 八個法幣擔保發行架構

**Body**

> 八個 fiat-backed payment stablecoins：  
> USDC, USDT, PYUSD, USDP, USDG, RLUSD, FDUSD, GUSD  
>  
> 共同點：以美元資產支撐  
> 差異點：發行實體、監理地、直接贖回資格、凍結權、收益處理

**Speaker notes**

The fiat-backed category looks uniform from the token holder's screen, but
the legal architecture differs substantially across issuers.

中文提示：提醒大家「同樣 1 美元價格」不代表「同樣法律權利」。

**Source claims**: CLAIM_026-035, CLAIM_058-068, CLAIM_072-081, KF_034

## Slide 7 - USDC and Circle Mint / USDC：Circle Mint 門檻

**Body**

> USDC reserve disclosures support cash, Treasury repo, T-bills and the Circle Reserve Fund  
> 直接贖回需要 Circle Mint account in good standing  
> 被轉讓取得 USDC 的持有人，不自動取得直接贖回資格  
> USDC 本身不給 holder yield

**Speaker notes**

USDC is useful for distinguishing product-page par language from direct
issuer redemption. The key institution is Circle Mint.

中文提示：不要只講「USDC 可 1:1 贖回」，要補上誰可以直接向 Circle 贖回。

**Source claims**: CLAIM_026, CLAIM_027, CLAIM_058, CLAIM_059

## Slide 8 - USDT and Non-Cash Exposures / USDT：驗證客戶與非現金曝險

**Body**

> Tether 2026-05-01 issuer release：  
> 約 US$141bn T-bill exposure  
> 約 US$20bn gold  
> 約 US$7bn Bitcoin  
>  
> 直接贖回是 verified customer 的個人契約權

**Speaker notes**

USDT cannot be modelled as pure cash-equivalent backing. The issuer release
contains material gold and Bitcoin exposures, and redemption is gated.

中文提示：這張的重點是，USDT 的儲備組合和 USDC 不一樣，贖回資格也不是開放給所有持有人。

**Source claims**: CLAIM_028, CLAIM_029, CLAIM_060, CLAIM_061
**Key figures**: KF_001, KF_002, KF_003

## Slide 9 - Paxos Family / Paxos 家族：一組條款管理三種幣

**Body**

> Paxos Trust：PYUSD / USDP  
> Paxos Digital + PIE：USDG  
>  
> 直接買回與贖回：Paxos Customer only  
> Non-Customer Token Holder 沒有直接向 Paxos 贖回的同等權利  
> Paxos 條款也涵蓋 no holder yield 與 freeze / upgrade scope

**Speaker notes**

The Paxos family is an example of a unified contract layer covering several
tokens. The holder's direct rights come through Paxos Customer status.

中文提示：把 PYUSD、USDP、USDG 放在一起看，因為它們有共同的 Paxos stablecoin agreement 層。

**Source claims**: CLAIM_072, CLAIM_073, CLAIM_074, CLAIM_075, CLAIM_076

## Slide 10 - USDP Reserve Report Status / USDP：獨立儲備組成報告已停止

**Body**

> 早期缺口：找不到 USDP monthly reserve composition report  
> v0.3 修正：issuer 已正式停止 separate monthly reserve composition report  
> 現有披露：KPMG LLP monthly AICPA attestation  
> 仍不可稱為 full financial-statement audit

**Speaker notes**

This slide is a good example of how a "missing source" can become a
substantive finding: the report is not merely absent; the issuer says the
separate report was discontinued.

中文提示：這裡不是說我們漏抓資料，而是 issuer 的披露形式已改變。

**Source claims**: CLAIM_080, CLAIM_081

## Slide 11 - GUSD and Gemini Customer Rights / GUSD：Gemini Customer 權利

**Body**

> GUSD creation / redemption is a Gemini Customer pathway  
> Reserve account structure：  
> 1. Omnibus Accounts  
> 2. Money Market Accounts  
> 3. Treasury Accounts  
>  
> Customer sell order 的 Timely redemption 約束：1 business day

**Speaker notes**

GUSD is especially helpful for separating a broader lawful-holder concept
from a platform-customer contract pathway.

中文提示：這張說明 NYDFS 架構不會自動消除 Gemini 條款中的 customer gating。

**Source claims**: CLAIM_077, CLAIM_078, CLAIM_079
**Key figures**: KF_017

## Slide 12 - RLUSD and NY Trust Structure / RLUSD：紐約信託架構

**Body**

> RLUSD is tied to Standard Custody / NYDFS trust-company framing  
> Product page supports reserve and custody statements  
> Ripple terms support suspension / termination consequences  
> 仍需補：直接贖回資格與 smart-contract level freeze powers

**Speaker notes**

RLUSD has stronger reserve and custody evidence than direct-redemption
evidence. That asymmetry should stay visible.

中文提示：這裡可以講得保守一點：有 reserve/custody 證據，但直接贖回與合約控制權還沒有完整閉合。

**Source claims**: CLAIM_032, CLAIM_033, CLAIM_057

## Slide 13 - FDUSD and FD121 / FDUSD：FD121 帳戶門檻

**Body**

> FDUSD terms use the contractual name FDD  
> Direct sale / redemption is gated through FD121 Account status  
> Terms include suspension / limitation mechanics  
> U.S. persons are excluded

**Speaker notes**

FDUSD is another example where redemption exists, but only inside a defined
account and eligibility perimeter.

中文提示：FDD 是條款中的名稱，不是另一個不同產品；這點要先說清楚。

**Source claims**: CLAIM_062, CLAIM_063, CLAIM_064

## Slide 14 - DAI / USDS Protocol Mechanics / DAI、USDS：Maker 到 Sky

**Body**

> DAI / USDS 不是 fiat-backed payment stablecoin  
> 核心機制：  
> Maker Vaults  
> overcollateralisation  
> liquidation auctions  
> MKR / SKY governance  
> DSR / Sky Savings Rate via sUSDS

**Speaker notes**

DAI / USDS belongs in the protocol-collateralised category. Its peg and
risk mechanics are not issuer-redemption mechanics.

中文提示：這張要阻止聽眾把 DAI/USDS 的「穩定」想成銀行存款加 T-bill 儲備。

**Source claims**: CLAIM_098, CLAIM_099, CLAIM_100, CLAIM_101, CLAIM_102
**Visual**: `06_flow_diagrams/dai_usds_protocol_flow.md`

## Slide 15 - USDe Synthetic Dollar / USDe：delta-neutral synthetic dollar

**Body**

> USDe 不是 fiat-backed payment stablecoin  
> 核心機制：  
> spot backing asset  
> short perpetual futures hedge  
> Off-Exchange Settlement custody  
> custodian attestations  
> Reserve Fund

**Speaker notes**

USDe is a synthetic-dollar design. The peg depends on hedge execution,
custody, funding rates, and reserve-fund governance rather than par
redemption from a regulated payment-stablecoin issuer.

中文提示：把 USDe 講成「現貨資產加空方永續合約」的結構，並提醒 sUSDe 才是收益包裝。

**Source claims**: CLAIM_065, CLAIM_066, CLAIM_067, CLAIM_103, CLAIM_104, CLAIM_105, CLAIM_106
**Visual**: `06_flow_diagrams/usde_synthetic_dollar_flow.md`
**Key figures**: KF_018, KF_019, KF_020, KF_021

## Slide 16 - Direct Redemption Gating / 直接贖回權的共同模式

**Body**

> 大多數「可贖回」都需要：  
> KYC / AML  
> 帳戶狀態良好  
> 合格司法管轄區  
> 不是 sanctioned / prohibited person  
> issuer 沒有暫停、凍結或限制

**Speaker notes**

The recurring pattern is that "redeemability" exists, but it is filtered
through account status and legal eligibility.

中文提示：這張把 issuer-by-issuer 的細節收束成一個共同模式。

**Source claims**: CLAIM_058, CLAIM_060, CLAIM_062, CLAIM_065, CLAIM_073, CLAIM_077

# Part 2 - Reserves and Dollar Money Markets

## Slide 17 - Reserve Composition / 儲備資產比較

**Body**

> Fiat-backed stablecoins 通常連到：  
> bank deposits  
> T-bills  
> repo / reverse repo  
> government MMF shares  
> custodians and trust accounts  
>  
> 但每個 issuer 的資產組合不同

**Speaker notes**

Reserve composition is the bridge between token supply and the dollar
money-market system.

中文提示：這張要講「鏈上美元」其實牽到鏈下短期安全資產。

**Source claims**: CLAIM_026, CLAIM_028, CLAIM_075, CLAIM_078, CLAIM_084

## Slide 18 - USDC vs USDT / 同樣美元包裝，不同儲備輪廓

**Body**

> USDC：cash, repo, short T-bills, Circle Reserve Fund  
> USDT：T-bills plus gold and Bitcoin exposures  
>  
> 不能把所有 fiat-backed stablecoin 都假設成同一個儲備模型

**Speaker notes**

Both tokens target the dollar, but the reserve composition and disclosure
architecture are different.

中文提示：用 USDC / USDT 做最直觀的對照。

**Source claims**: CLAIM_026, CLAIM_027, CLAIM_028, CLAIM_029

## Slide 19 - T-Bill Demand Channel / T-bill 需求通道

**Body**

> Stablecoin growth can increase demand for short-term safe assets  
> 但效果取決於：  
> reserve composition  
> issuer business model  
> banking-system offset  
> regulatory reserve lists

**Speaker notes**

The safe-asset channel is plausible but conditional. It should not be stated
as a mechanical one-dollar-for-one-dollar drain from bank deposits into
Treasuries.

中文提示：這裡要保持央行研究的語氣：有通道，但不是機械結論。

**Source claims**: CLAIM_084, BIS_003, ECB_003

## Slide 20 - Why DAI and USDe Do Not Aggregate / 為什麼 DAI、USDe 不能併入同一儲備模型

**Body**

> DAI / USDS：Vault collateral, liquidation, governance  
> USDe：spot asset, short perp hedge, reserve fund  
>  
> 這兩類不會以相同方式傳導到 T-bill demand 或 bank deposit substitution

**Speaker notes**

Aggregating protocol and synthetic-dollar designs with fiat-backed payment
stablecoins would distort the reserve-market analysis.

中文提示：這張是為了保護 chapter 3 的邏輯，不要把不同穩定機制加總成一個數字。

**Source claims**: CLAIM_098, CLAIM_103, CLAIM_106

## Slide 21 - Reserve Income Asymmetry / 儲備收益的不對稱

**Body**

> Issuers may earn reserve income  
> Holders usually do not receive reserve yield  
>  
> GENIUS, MiCA ART, Paxos terms, Circle terms, Ethena terms all reinforce this asymmetry in different ways

**Speaker notes**

Reserve income is central to the stablecoin business model. The legal and
contractual architecture often prevents that income from flowing to token
holders.

中文提示：這張可帶到利益結構：誰持有資產、誰拿收益、誰承擔流動性風險。

**Source claims**: CLAIM_059, CLAIM_066, CLAIM_071, CLAIM_074, CLAIM_086

# Part 3 - Law and Regulation

## Slide 22 - Jurisdiction Map / 四個監理基準

**Body**

> U.S. GENIUS Act  
> EU MiCA ART / EMT  
> UK BoE systemic stablecoin regime  
> New York NYDFS guidance  
>  
> 它們重疊，但不是同一套制度

**Speaker notes**

The legal chapter is not a single "regulation is coming" story. It is a
comparison of distinct baselines, plus a bounded foreign-issuer equivalence
screen.

中文提示：把這張當成法規章的地圖。

**Source claims**: CLAIM_036-043, CLAIM_069-071, CLAIM_082-097, CLAIM_126-131

## Slide 23 - GENIUS Act: Issuer Gate / GENIUS Act：發行人門檻

**Body**

> 只有 permitted payment stablecoin issuer 可以發行  
> 3-year transition gate affects DASP distribution  
> foreign issuer treatment depends on Treasury comparability, registration, U.S. liquidity, and reciprocal arrangements

**Speaker notes**

The GENIUS Act is not only about reserve assets. It defines who may issue
and how non-U.S. issuers may reach the U.S. market.

中文提示：先講 issuer gate，再講儲備資產，順序會比較清楚。

**Source claims**: CLAIM_082, CLAIM_083, CLAIM_126, KF_005, KF_007

## Slide 24 - GENIUS Act: Reserves / GENIUS Act：儲備資產清單

**Body**

> Permitted reserves include：  
> cash and insured deposits  
> Treasury bills / notes / bonds with max 93-day maturity  
> overnight repo / reverse repo  
> government MMF shares  
> central-bank reserves where allowed  
>  
> monthly disclosure and registered-public-accounting-firm examination

**Speaker notes**

This is the statutory reserve model. It is broad enough to include several
money-market instruments, not just bank deposits.

中文提示：把 93 天與 monthly examination 說出來，這是量化 anchor。

**Source claims**: CLAIM_084, CLAIM_085, KF_004, KF_006

## Slide 25 - GENIUS Act: Yield and Insolvency / GENIUS Act：收益禁止與破產順位

**Body**

> Issuer may not pay holder yield for holding, using, or retaining stablecoins  
> In insolvency, customer claims receive statutory priority  
>  
> 這讓穩定幣更像支付負債，而不是收益型存款產品

**Speaker notes**

The yield prohibition and insolvency priority help define the legal nature
of a payment stablecoin under the Act.

中文提示：這張可以連回「儲備收益不對稱」。

**Source claims**: CLAIM_086, CLAIM_087

## Slide 26 - MiCA ART vs EMT / MiCA：ART 與 EMT

**Body**

> ART：asset-referenced token  
> reserve of assets, permanent redemption, no interest  
>  
> EMT：e-money token  
> par-value redemption, no interest, 30% credit-institution deposit floor

**Speaker notes**

MiCA has two separate token regimes. Treating ART and EMT as one category
would lose important legal differences.

中文提示：這張只做清楚分類，不要把所有 MiCA stablecoin 都叫同一種。

**Source claims**: CLAIM_042, CLAIM_043, CLAIM_069, CLAIM_070, CLAIM_071, CLAIM_127, CLAIM_128, KF_009

## Slide 27 - MiCA Significant Tokens / MiCA：重大代幣與復原、贖回計畫

**Body**

> Significant ART：Article 45 additional obligations  
> recovery plan：liquidity fees, redemption caps, suspension options  
> redemption plan：wind-down and temporary administrator  
> Significant EMT：EBA transfer, six-month audit cadence, non-euro home-state derogation

**Speaker notes**

The significant-token layer creates an additional supervisory regime above
ordinary ART and EMT rules.

中文提示：用 recovery plan 和 redemption plan 說明 MiCA 不只管平常，也管壓力情境。

**Source claims**: CLAIM_094, CLAIM_095, CLAIM_096, CLAIM_097, CLAIM_129, KF_008, KF_010

## Slide 28 - BoE 2023 to 2025 / BoE：從 100% CBD 到 40/60

**Body**

> 2023：preferred 100% central bank deposit backing  
> 2025：at least 40% unremunerated CBD  
> up to 60% short-term UK government debt  
> launch step-up can allow up to 95% UK government debt
> cross-border use remains jointly UK-regulated and subject to home authority

**Speaker notes**

The BoE shift is important because it shows a central bank balancing
singleness-of-money concerns against operational and market structure. It is
also the closest non-U.S. comparison case for the foreign-issuer screen, but
not an automatic GENIUS equivalent.

中文提示：這張可以講 BoE 是最明顯把 central bank money 放進穩定幣儲備設計的案例。

**Source claims**: CLAIM_088, CLAIM_089, CLAIM_090, CLAIM_130, CLAIM_131, KF_011, KF_012, KF_013

## Slide 29 - BoE Holding Limits / BoE：持有上限

**Body**

> proposed limit：GBP 20,000 per individual per coin  
> proposed business limit：GBP 10 million  
>  
> 這是 UK regime 最特別的工具之一

**Speaker notes**

Holding limits are not common across the other regimes. They are a specific
BoE proposal for managing adoption speed and systemic risk.

中文提示：把它定位成 UK 特有工具，不要誤說成全球標準。

**Source claims**: CLAIM_091, KF_014, KF_015

## Slide 30 - ESMA Supervisory Practice / ESMA：CASP 與 transfer service

**Body**

> ESMA rejects a low-risk CASP assumption  
> elevated scrutiny triggers include：  
> 1M EU users  
> EUR 3bn balance sheet  
> 200,000 cross-border users  
>  
> Article 82 transfer-service guidelines connect MiCA to Travel Rule-style controls

**Speaker notes**

ESMA materials are useful because they show how MiCA supervision will look
in practice, not only in statutory text.

中文提示：這張把 MiCA 從條文拉到監理實務。

**Source claims**: CLAIM_092, CLAIM_093, KF_029, KF_030, KF_031

## Slide 31 - Cross-Jurisdiction Table 1 / 跨法域比較：發行人、儲備、贖回

**Body**

> 比較維度：  
> eligible issuer  
> reserve composition  
> redemption right  
>  
> GENIUS, MiCA ART, MiCA EMT, BoE, NYDFS 的共同點多，但細節不同

**Speaker notes**

Use the slide-ready table rather than narrating every cell. The table is
designed to show convergence and divergence at the same time.

中文提示：不要逐格朗讀，用三個維度點出差異。

**Source claims**: chapter 4 comparison table
**Visual**: `07_final_report/comparison_table_slide_31.md`

## Slide 32 - Cross-Jurisdiction Table 2 / 跨法域比較：破產、收益、重大門檻

**Body**

> 比較維度：  
> insolvency / wind-down  
> holder yield / interest  
> significant-token threshold  
>  
> holder yield 是少數高度一致的限制方向

**Speaker notes**

The second comparison table is useful for discussing the economic design of
stablecoins: who gets yield, who has priority, and when a token becomes
systemically supervised.

中文提示：把焦點放在「收益被壓住」與「重大代幣門檻不同」。

**Source claims**: chapter 4 comparison table
**Visual**: `07_final_report/comparison_table_slide_32.md`

# Part 4 - Central Bank and Policy Framing

## Slide 33 - Fed IFDP 1334 / Fed：條件式銀行通道

**Body**

> Fed models do not say stablecoins mechanically drain deposits  
> impact depends on：  
> source of demand  
> backing model  
> whether reserves recycle into banks  
> two-tier banking vs narrow-bank design

**Speaker notes**

The Fed frame is conditional. It avoids the simplistic claim that every
stablecoin dollar is a one-for-one loss to bank credit.

中文提示：這張要講「條件式」，不是單向恐慌敘事。

**Source claims**: CLAIM_044, CLAIM_047, CLAIM_048

## Slide 34 - IMF: Making Stablecoins Stable / IMF：穩定化的代價

**Body**

> Safe-asset backing can reduce run risk  
> but may reduce issuer profitability and issuance incentives  
>  
> policy design is a tradeoff between stability and business viability

**Speaker notes**

The IMF model clarifies that safer reserves are not free. The economics of
the issuer still matter.

中文提示：這張不要只講「安全資產比較安全」，要補上 issuer incentive 的代價。

**Source claims**: CLAIM_049

## Slide 35 - IMF Event Study / IMF：18% 與 US$300bn

**Body**

> U.S. pro-stablecoin policy news was associated with：  
> about 18% decline in listed incumbent payment-firm value  
> about US$300bn market value reduction  
>  
> this is market expectation, not realised adoption

**Speaker notes**

This is a powerful figure, but it must be interpreted carefully. It is not
evidence that stablecoins already replaced payment firms.

中文提示：數字很吸睛，但務必加上「市場預期，不是已實現支付採用」。

**Source claims**: CLAIM_050, KF_027, KF_028

## Slide 36 - Taiwan-Specific Synthesis / 台灣場景綜整

**Body**

> 台灣問題不是「要不要有穩定幣」而已  
> 更精準的問題是：  
> NTD stablecoin 如何分類  
> USD stablecoin 是否帶來數位美元化  
> 外匯監理如何看待鏈上美元流動  
> deposit token、CBDC、商業銀行貨幣如何分工

**Speaker notes**

The Taiwan synthesis is now backed by CBC claims. It should still be phrased
carefully: CBC does not treat stablecoins as removing central-bank money from
the system, but it does identify USD-stablecoin, FX, NTD-stablecoin reserve,
payment-system and monetary-transmission channels.

中文提示：這張現在可以當作台灣結論頁。重點是：美元穩定幣牽涉美元化與外匯監理，新台幣穩定幣更像電子支付儲值款項的代幣化。

**Source claims**: CLAIM_112, CLAIM_113, CLAIM_114, CLAIM_115, CLAIM_116, CLAIM_117, CLAIM_118

# Part 5 - USDPT and Cross-Border Payments

## Slide 37 - What Is Documented About USDPT / USDPT 已有證據

**Body**

> Western Union announced USDPT  
> expected issuer：Anchorage Digital Bank  
> chain：Solana  
> infrastructure：Fireblocks wallet / settlement / reporting stack  
>  
> evidence supports a planned digital-asset settlement layer

**Speaker notes**

USDPT is important, but the evidence base is narrow. We can document launch
framing and infrastructure partners, not the full operating architecture.

中文提示：先說有什麼，不要一開始就說缺什麼。

**Source claims**: CLAIM_051, CLAIM_052, CLAIM_053

## Slide 38 - Four-Layer Separation / 四層拆解

**Body**

> Layer 1：customer remittance UX  
> Layer 2：Western Union agent network  
> Layer 3：stablecoin issuance and on-chain transfer  
> Layer 4：reserve assets and bank / correspondent settlement  
>  
> Replacement claims must specify which layer is replaced

**Speaker notes**

The four-layer diagram prevents the phrase "USDPT replaces SWIFT" from
collapsing multiple systems into one claim.

中文提示：請直接展示 swim-lane 圖。任何替代論都必須先指出替代的是哪一層。

**Source claims**: chapter 6 framing, CLAIM_051-053
**Visual**: `06_flow_diagrams/usdpt_settlement_flow.md`

## Slide 39 - What Is Not Documented / USDPT 尚未取得文件

**Body**

> Not yet in the archive：  
> product terms  
> reserve report  
> contract addresses  
> direct redemption policy  
> customer-to-customer workflow  
> agent cash-out workflow

**Speaker notes**

The missing documents are exactly the ones needed to move from "planned
product" to "documented operating system."

中文提示：這不是悲觀，而是證據紀律。沒有 workflow 文件就不講替代 SWIFT。

**Source claims**: unresolved_open_questions.md, usdpt_product_terms_research_queue.md

## Slide 40 - Conditional USDPT Framing / USDPT 的安全說法

**Body**

> Safe wording：  
> Western Union is attempting to use USDPT and a Digital Asset Network  
> to build a regulated digital-asset settlement layer  
>  
> Unsafe wording：  
> USDPT replaces SWIFT / correspondent banking / Fedwire / CHIPS / WU retail rails

**Speaker notes**

This slide gives the exact language discipline for discussion and Q&A.

中文提示：這張是問答時的保護欄。聽眾問替代論時，就回到這裡。

**Source claims**: chapter 6, AGENTS.md guardrails

# Part 6 - On-Chain Data

## Slide 41 - Volume Is Not Payment Demand / 轉帳量不是支付需求

**Body**

> Raw transfer volume includes：  
> exchange flows  
> bridge flows  
> arbitrage  
> internal wallet movement  
> protocol flows  
>  
> payment demand needs adjusted methodology

**Speaker notes**

This is one of the central guardrails. Transfer volume is useful, but it is
not equivalent to real-world payment adoption.

中文提示：這張要講清楚「看起來很多」不等於「真的拿去付款」。

**Source claims**: AGENTS.md rule, chapter 7 framing

## Slide 42 - DeFiLlama Supply Data / DeFiLlama 可以說什麼

**Body**

> DeFiLlama exports support：  
> stablecoin supply snapshot  
> chain distribution  
> market structure context  
>  
> They do not support：  
> adjusted payment volume  
> merchant adoption  
> real-world remittance volume

**Speaker notes**

DeFiLlama data is useful for supply-side analysis, but it cannot answer the
payment-demand question by itself.

中文提示：這張把資料用途和不能用途分開。

**Source claims**: CLAIM_054, 09_data_exports README

## Slide 43 - Missing Adjusted Exports / 還缺哪些 adjusted data

**Body**

> Still missing：  
> Visa Onchain Analytics adjusted-volume export  
> Artemis reproducible export beyond methodology  
> Cambridge numerical export  
> McKinsey / Artemis local archive  
> World Bank remittance-cost benchmark export

**Speaker notes**

The chapter stays qualitative because the adjusted-volume exports are not
reproducible from the current archive.

中文提示：這張和 USDPT 缺口一樣，是 freeze 而不是 guess。

**Source claims**: chapter 7, 09_data_exports README

# Part 7 - Failure Cases

## Slide 44 - Risk Taxonomy / 風險分類

**Body**

> v0.3 can support a risk taxonomy：  
> reserve risk  
> redemption gate risk  
> collateral liquidation risk  
> liquidity stress risk  
> oracle / governance risk  
> basis and funding risk  
> regulatory and wind-down risk

**Speaker notes**

The taxonomy is claim-backed. Detailed case timelines are a v0.4 task unless
the project ingests a reproducible price and event-data workflow.

中文提示：這張不要講成完整歷史事件研究；它是風險分類。

**Source claims**: CLAIM_069, CLAIM_075, CLAIM_084, CLAIM_090, CLAIM_094, CLAIM_098, CLAIM_101, CLAIM_103, CLAIM_106

## Slide 45 - Lessons as Guardrails / 事件教訓變成研究護欄

**Body**

> Past failures reinforce the five guardrails：  
> attestation vs audit  
> direct right vs product page  
> volume vs payment demand  
> USDPT vs payment-rail replacement  
> ART vs EMT

**Speaker notes**

Failure cases are not just colourful anecdotes. They are why the report is
strict about terminology and evidence boundaries.

中文提示：把失敗案例拉回研究方法，不要變成故事時間。

**Source claims**: CLAIM_107-111, chapter 8

# Part 8 - Closing

## Slide 46 - What the Evidence Supports / 證據可以支持什麼

**Body**

> Stablecoins reconfigure dollar liquidity  
> direct redemption rights are narrower than marketing language  
> attestation is not audit  
> regulation is converging but not identical  
> central-bank channels are conditional  
> DAI / USDS and USDe are different in kind

**Speaker notes**

These are the high-confidence findings. They are the safest backbone for the
reading-group discussion.

中文提示：這張是主結論。

**Source claims**: chapter 9.1

## Slide 47 - What Is Conditional / 哪些結論仍是條件式

**Body**

> Conditional findings：  
> USDPT may become a settlement-layer reconfiguration  
> but primary product documents are missing  
>  
> Stablecoin payment adoption may grow  
> but adjusted-volume evidence is missing

**Speaker notes**

The report is strongest when it explicitly marks what is conditional.

中文提示：這張是誠實標籤，不是削弱研究。

**Source claims**: chapter 9.2

## Slide 48 - What Remains Unresolved / 未解問題

**Body**

> USDPT product layer  
> adjusted on-chain payment volume  
> Taiwan enacted law / sub-rules  
> failure-case price/depeg timelines  
> Maker Black Thursday primary sources

**Speaker notes**

The unresolved list is the v0.4 roadmap. None of these should be answered by
guessing.

中文提示：把這張當成後續研究 agenda。

**Source claims**: unresolved_open_questions.md, chapter 9.3

## Slide 49 - Discussion Questions / 讀書會討論題

**Body**

> 1. 穩定幣的主要風險在 holder、issuer、reserve asset 還是 payment rail？  
> 2. 法規是在保護持有人，還是在重塑誰能取得美元支付基礎設施？  
> 3. 台灣面對的是 NTD stablecoin 問題，還是 USD stablecoin 的數位美元化問題？

**Speaker notes**

These questions are designed to keep discussion tied to the evidence. They
also connect global regulation back to Taiwan-specific policy concerns.

中文提示：最後不要只收在技術面，要把討論拉回金融制度與台灣情境。

**Source claims**: chapter 9.4

# Appendix

## Slide A1 - Claim Map / Claim 對照

**Body**

> 所有主要結論都可追到：  
> `03_claim_tables/claim_table_master.csv`  
> `01_sources/source_registry.csv`  
>  
> Claim ID -> source ID -> local archive path -> evidence summary

**Speaker notes**

Use this if the audience asks where the evidence is. It also signals that the
deck is traceable.

中文提示：學術型聽眾通常會在意來源，這張可以放在備用頁。

**Source claims**: PROJECT_METHODOLOGY_001

## Slide A2 - Disclaimer / 使用限制

**Body**

> This is not investment advice  
> USDPT workflow is inferred, not production architecture  
> reserve figures are point-in-time disclosures  
> attestations are not audits  
> volume is not payment demand  
> fiat-backed, crypto/RWA, and synthetic-dollar products are separate categories

**Speaker notes**

This slide codifies the evidence boundaries for the session.

中文提示：如果正式上台，這張建議保留在 appendix 或開場備用。

**Source claims**: AGENTS.md non-negotiable rules

## Slide A3 - Source Registry / 資料庫狀態

**Body**

> v0.3.2 source registry：137 rows  
> claim table：131 validated claims  
> missing archived local files：none  
> high-priority rows needing attention：none  
> known unresolved items：USDPT documents, adjusted-volume exports, Taiwan enacted law, failure-case timelines

**Speaker notes**

This is the operational status slide. It distinguishes research gaps from
broken repository state.

中文提示：這張可以回答「資料庫完整嗎？」這類問題。

**Source claims**: README current snapshot, validation scripts

# Speaker Checklist Before 2026-06-27

1. Decide whether Slide 1 should include presenter affiliation and reading-group logo.
2. Render or redraw the Mermaid diagrams for Slides 14, 15, and 38.
3. Check whether the deck will use the 49-slide full path or a shorter 60-minute cut.
4. For under 60 minutes, cut Slides 12, 30, 36, 42, 43, 44, and 45 first.
5. Keep Slides 4, 5, 22, 31, 32, 38, 41, 46, and 48 in every version.
6. Do not update USDPT, adjusted-volume, Taiwan enacted-law, or failure-case slides from inference unless new claims are added first.
