# Slide Script — v0.3 (2026-05-15)

讀書會：2026-06-27 穩定幣研究 / Stablecoin Ecosystem Research

## How to read this script

Each slide entry contains:

- **Slide N — Title** in bilingual form (English / 中文).
- **Body** — exact Chinese text intended for the rendered slide. Bullets are
  kept short (≤15 characters where possible) to fit slide formatting.
- **Speaker notes** — analytical content in English (2-3 sentences) followed
  by a Chinese delivery prompt for the speaker. The English sentences are
  the load-bearing analytical content; the Chinese prompt is one possible
  way to deliver them.
- **Source claims** — `CLAIM_XXX` references that anchor the slide content.
  Full citations are in `03_claim_tables/claim_table_master.csv`.
- **Visual** — visual asset notes where applicable.

Source authoritative documents:

- `07_final_report/executive_summary.md`
- `07_final_report/key_figures.csv`
- `07_final_report/comparison_table_slide_31.md`
- `07_final_report/comparison_table_slide_32.md`
- `05_chapter_drafts/chapter_01_stablecoins_as_onchain_dollar_system.md`
- `05_chapter_drafts/chapter_09_conclusion.md`
- `06_flow_diagrams/*.md`

# Part 0 — Opening（開場：5 張）

## Slide 1 — Title / 標題頁

**Body（投影片內容）**

> 穩定幣作為美元體系的鏈上延伸
>
> Stablecoins as an On-chain Extension of the Dollar System
>
> 2026-06-27 鏈上數據讀書會
>
> 報告人：[姓名] ｜ 研究版本：v0.3

**Speaker notes**

This is a research-grounded reading-group session, not a market briefing.
The entire deck is backed by 106 claim entries traceable to 130 archived
primary sources. The framing rejects the popular "stablecoins replace banks"
narrative in favour of treating stablecoins as a tokenised wrapper around
existing dollar money-market and banking-system instruments.

中文 delivery prompt: 開場可說「今天不是談價格，是談制度。穩定幣不是另一種貨幣，而是把美元工具上鏈包裝的負債。後面所有結論都建立在 106 條 source-backed claim 上。」

**Source claims**: 整體研究框架；chapter 1.1

## Slide 2 — Why this matters now / 為什麼在 2026 談這件事

**Body**

> 四件事同年發生
>
> 1. **GENIUS Act** 立法（Public Law 119-27）：美國聯邦首次有 payment stablecoin 法
> 2. **MiCA** 全面適用：ART / EMT 分離、significant-token、recovery / redemption plan 全到位
> 3. **BoE 2025 諮詢**：100% 央行存款 → 40/60 split + step-up；提出 £20,000 / £10m 持有上限
> 4. **Western Union USDPT** 宣布：Anchorage Digital Bank 預期發行、Solana 鏈、Fireblocks 基礎設施

**Speaker notes**

These four developments are not just contemporaneous; they create the
analytical baseline for the rest of the deck. The US, EU, UK now all have
written rules, and a major remittance incumbent is moving onto a stablecoin
rail. The deck reads them at the article level rather than at the headline
level.

中文 delivery prompt: 強調「四件事都在 2026 之前或之中發生」，因此本研究的時機是制度面確立後的第一輪整理。

**Source claims**: CLAIM_082 (GENIUS), CLAIM_069 (MiCA ART), CLAIM_090 (BoE), CLAIM_051 (USDPT 宣布)

## Slide 3 — Scope & method / 研究範圍與方法

**Body**

> - **單位分析**：發行者 → 儲備 → 託管 → 衍生品對手方 → 支付參與者 → 法律體系
> - **資料規模**：106 條 source-backed claim ｜ 130 個 archived source
> - **可追溯性**：registry → digest → claim → matrix → chapter（五層）
> - **守則**：每一句結論都對應 claim_table_master.csv 的一列

**Speaker notes**

The methodology is the deck's strongest defence. Every numerical claim has
a `CLAIM_XXX` ID, a `source_id`, a `page_or_section` reference, a quotation
of the operative evidence, and a confidence label. Where evidence is
missing, the open question is preserved rather than guessed.

中文 delivery prompt: 提醒「本研究刻意把『沒有證據的問題』留下而不猜測」，這是與一般市場 narrative 最大的差別。

**Source claims**: AGENTS.md 工作流；chapter 1.6；KF_032、KF_033

## Slide 4 — Three product categories / 三類穩定幣不能混為一談

**Body**

> 把所有穩定幣加總，等於忽略它們進入美元體系的不同通道。
>
> | 類別 | 代表 | 穩定機制 |
> | --- | --- | --- |
> | Fiat-backed payment stablecoin | USDC、USDT、PYUSD、USDP、USDG、RLUSD、FDUSD、GUSD | 法幣存款＋短期國債＋repo＋政府 MMF |
> | Crypto / RWA-collateralised | DAI / USDS（Maker / Sky） | 超額抵押 + 自動清算 + 治理代幣稀釋 |
> | Synthetic-dollar | USDe（Ethena） | 1:1 抵押 + 空頭 perp 對沖 + 場外託管 |

**Speaker notes**

Three categories, three different ways into the dollar system, three
different risk profiles. Aggregating them — as some market headlines do —
obscures the very channels through which each transmits or fails to
transmit. This is the load-bearing categorical distinction of the deck.

中文 delivery prompt: 強調「三類進入美元體系的通道完全不同；風險不同、監管定位也不同」。請聽眾把這張投影片當成整場的索引。

**Source claims**: CLAIM_026 (USDC fiat-backed), CLAIM_098 (DAI/USDS), CLAIM_103 (USDe)

## Slide 5 — Five guardrails / 五條本研究刻意守住的分界

**Body**

> 本研究全程堅守以下五條分界，避免常見論述失誤：
>
> 1. **Attestation ≠ Audit**：月度 attestation 不是財務報表 audit
> 2. **Product page ≠ Direct right**：「Redeemable at par」不等於人人有贖回權
> 3. **Volume ≠ Payment demand**：鏈上轉帳量不等於實際支付需求
> 4. **USDPT ≠ SWIFT 取代**：無 workflow 文件即不可宣稱替代既有支付網絡
> 5. **ART ≠ EMT**：MiCA 兩套規則必須分開處理

**Speaker notes**

Each of these maps onto a specific historical failure mode in
stablecoin discourse. The attestation-versus-audit confusion shaped early
transparency controversies; the volume-versus-payment confusion is still
widely repeated; the USDPT-versus-SWIFT confusion is the current temptation
the report explicitly guards against.

中文 delivery prompt: 用「五條分界」當作後面所有判斷的基石。後面任何 slide 若聽眾有疑慮，回到這五條應該都能回答。

**Source claims**: AGENTS.md non-negotiable rules; chapter 1.4

# Part 1 — Issuer ecosystem（發行者：11 張）

## Slide 6 — Eight fiat-backed issuers at a glance / 八家法幣支撐型發行者全覽

**Body**

> | 發行者 | 主要司法管轄 | 直接贖回對象 | 主儲備類別 |
> | --- | --- | --- | --- |
> | USDC / Circle | US（OCC、NYDFS、MiCA EMT） | Circle Mint account | 銀行存款＋反向回購＋短 T-bill |
> | USDT / Tether | El Salvador 註冊 | 驗證客戶 | T-bill 為主＋黃金＋BTC |
> | PYUSD / Paxos Trust | US OCC | Paxos Customer | FDIC 存款＋T-bill＋repo＋MMF |
> | USDP / Paxos Trust | US OCC | Paxos Customer | FDIC 存款＋T-bill＋repo＋MMF |
> | USDG / Paxos Digital + PIE | MAS / FIN-FSA | Paxos Customer | 銀行存款＋T-bill＋MMF |
> | RLUSD / Standard Custody | NYDFS | 文件未確定 | 美元存款＋T-bill＋現金等價 |
> | FDUSD / FD121 (BVI) | BVI + HK | FD121 Account（排除美國人） | 美元＋定存＋T-bill |
> | GUSD / Gemini Trust | NYDFS | Gemini Customer | FDIC 存款＋MMF＋T-bill |

**Speaker notes**

This is the "one slide if you only remember one" map. Across all eight,
the right to redeem with the issuer is gated by some form of customer
status. The reserve composition list overlaps but is not identical.

中文 delivery prompt: 提醒「八家發行人雖然在 product page 上都寫『1:1』，但實際贖回對象差很多」。

**Source claims**: CLAIM_001-035, CLAIM_058-068, CLAIM_072-081

**Visual**: 直接搬 issuer matrix 重新排版；可考慮用三段顏色（OCC / NYDFS / 其他）區分監管

## Slide 7 — USDC — Circle Mint gating / USDC：Circle Mint 帳戶閘門

**Body**

> - **儲備類別**：銀行存款、systemically important institutions 存款、隔夜反向 Treasury repo、≤3 月 T-bill、Circle Reserve Fund（CLAIM_026 / 027）
> - **直接贖回**：須持有 Circle Mint account in good standing；轉手持有人需註冊 Circle Mint 才可贖回（CLAIM_058）
> - **持有人收益**：條款明定持有人對儲備收益無權利；USDC 本身不付 yield（CLAIM_059）

**Speaker notes**

USDC is the canonical "fiat-backed, regulated, multi-jurisdiction"
stablecoin. The combination of reserve transparency and Circle Mint gating
makes it the natural reference point against which other issuers are
compared. The "redemption only via Circle Mint" gate is often missing from
product-page summaries.

中文 delivery prompt: 用「USDC = 標準參照組」帶過。重點在 Circle Mint gating 不是 product page 上明顯陳述的事。

**Source claims**: CLAIM_026, CLAIM_027, CLAIM_058, CLAIM_059

## Slide 8 — USDT — verified customer + non-cash exposures / USDT：驗證客戶限定 + 非現金部位

**Body**

> - **儲備規模**（2026-05-01 issuer release）：
>   - ~US\$141bn 直接與間接 T-bill 暴險
>   - ~US\$20bn 實體黃金
>   - ~US\$7bn Bitcoin
> - **直接贖回**：限驗證 Tether 客戶；贖回為「個人合約權利」（CLAIM_060）
> - **禁止對象**：美國人（限 ECP 例外）、加拿大人、新加坡人、被制裁人、特定司法管轄（CLAIM_061）

**Speaker notes**

USDT cannot be modelled as a pure cash-equivalent. The published gold and
Bitcoin exposures shift its risk profile out of the "T-bill wrapper"
category that USDC inhabits. The verified-customer requirement is a much
stricter gate than USDC's Circle Mint requirement.

中文 delivery prompt: 強調「USDT 不能當純 cash equivalent」，且贖回管制比 USDC 嚴格得多。

**Source claims**: CLAIM_028, CLAIM_029, CLAIM_060, CLAIM_061
**Key figures**: KF_001 (~US\$141bn T-bill), KF_002 (~US\$20bn 黃金), KF_003 (~US\$7bn BTC)

## Slide 9 — Paxos family — unified terms govern PYUSD / USDP / USDG / Paxos 體系：三幣同一條款

**Body**

> - **發行實體**（CLAIM_072）：
>   - **Paxos Trust, N.A.** 發行 USDP、PYUSD、BUSD（僅供贖回）
>   - **Paxos Digital Singapore + PIE** 共同發行 USDG
> - **直接贖回**：只限 Paxos Customer；Non-Customer Token Holder 無此權利（CLAIM_073）
> - **持有人收益**：明文「不設計來產生 returns、profits、增值或財務利益」（CLAIM_074）
> - **儲備限制**：FDIC 存款 + 美國政府擔保債（直接或 repo）+ 政府 MMF（CLAIM_075）
> - **凍結與升級**：適用所有持有人，不只 Customer（CLAIM_076）

**Speaker notes**

The Paxos USD Stablecoin Agreement governs all three tokens in one
contract. The "PYUSD vs USDP vs USDG" distinction is real at the issuer
entity level (Trust vs Digital + PIE), but the redemption gating and
no-holder-yield rules are uniform. The all-holders scope of the
freeze-and-upgrade right is the strongest issuer-side control in the v0.3
archive.

中文 delivery prompt: 重點是「三幣同一條款」這個結構，以及 Paxos 對所有持有人的 freeze 權限。

**Source claims**: CLAIM_072, CLAIM_073, CLAIM_074, CLAIM_075, CLAIM_076

## Slide 10 — USDP — discontinued separate reserve report / USDP：月度儲備組成報告已停發

**Body**

> - **歷史問題**：本研究長期掛在 unresolved 的「USDP 月度儲備報告 PDF 缺漏」
> - **真相**（CLAIM_081）：Paxos 已正式停止提供 separate monthly reserve composition report
> - **仍維持**（CLAIM_080）：KPMG LLP 月度 attestation（自 2025-02-28 起；之前為 WithumSmith+Brown）
> - **框架**：AICPA examination / attestation 標準 — **不是 financial-statement audit**

**Speaker notes**

This closes a long-standing v0.2 deficiency. The report was not missing
because of an archival gap; it was discontinued by the issuer. The
attestation under AICPA standards continues monthly, but should not be
described as an audit. The terminology distinction is load-bearing.

中文 delivery prompt: 借這張 slide 第一次正式強調「attestation ≠ audit」的實例。

**Source claims**: CLAIM_080, CLAIM_081

## Slide 11 — GUSD — Gemini Customer only + three reserve accounts / GUSD：限 Gemini 客戶 + 三類儲備帳戶

**Body**

> - **直接贖回**：只限 Gemini Customer；對 non-Customer，「obtaining or using GUSD 不構成任何關係 / 任何義務」（CLAIM_077）
> - **儲備結構**（CLAIM_078）：
>   - Gemini Dollar Omnibus Accounts — FDIC 存款
>   - Gemini Dollar Money Market Accounts — 投資於美國政府證券之 MMF
>   - Gemini Dollar Treasury Accounts — 美國國債
>   - 統一 1:1 比例管理
> - **贖回時限承諾**：對 Customer 之 sell Order 為「Timely」= 不超過 1 個 Business Day（CLAIM_079）

**Speaker notes**

GUSD is the cleanest example of the "platform-customer vs lawful-holder"
distinction in the v0.3 archive. The agreement explicitly disclaims any
relationship with non-customers. The one-Business-Day timing is the
strongest written redemption-timing commitment among issuers examined.

中文 delivery prompt: 借 GUSD 例子解釋「Customer-only redemption gating」是普遍 pattern，不是 Gemini 特例。

**Source claims**: CLAIM_077, CLAIM_078, CLAIM_079
**Key figures**: KF_017 (1 Business Day "Timely" commitment)

## Slide 12 — RLUSD — Standard Custody NY trust / RLUSD：紐約信託發行

**Body**

> - **發行人**：Standard Custody & Trust Company, LLC（Ripple Labs 子公司）
> - **監管**：紐約 limited purpose trust company；依 NYDFS 2022 指引
> - **儲備揭露**：美元存款、美國國債、現金等價物；隔離存放於合格存款 / 託管機構
> - **託管**：2025-07 起以 BNY 為主託管
> - **使用限制**：Ripple 條款允許因禁止行為暫停 / 終止 RLUSD 服務（CLAIM_057）
> - **未解問題**：直接贖回適格範圍與合約層級凍結 / 黑名單機制仍待單獨抽取

**Speaker notes**

RLUSD is the youngest entrant. It demonstrates how the NYDFS 2022 guidance
structures GUSD-like and RLUSD-like products. The product-page reserve and
custody detail is medium confidence; the direct redeemer scope still needs
terms-level extraction.

中文 delivery prompt: RLUSD 是新進入者，主要證明 NYDFS 框架仍是運作中的 state-level 規則。

**Source claims**: CLAIM_007, CLAIM_008, CLAIM_032, CLAIM_033, CLAIM_057

## Slide 13 — FDUSD — FDD / FDUSD via FD121 (BVI) / FDUSD：FDD 條款下的 BVI 發行架構

**Body**

> - **發行人**：FD121 (BVI) Limited
> - **託管 / 監管**：BVI 註冊 + HK 相關託管安排
> - **儲備揭露**：美元 + 定存 + T-bill / 政府擔保債（儲備 ≥ 流通量）
> - **直接贖回**：只限 FD121 Account 持有人；非適格 / 未註冊者無權售予 FD121（CLAIM_062）
> - **暫停權**：reserves、liquidity、市場波動、emergency、法律等情境下可暫停 / 限制（CLAIM_063）
> - **美國排除**：FD121 帳戶條款排除美國個人 / 實體（CLAIM_064）
> - **術語**：條款內以「FDD」為合約短名，與市場通稱「FDUSD」為同一資產（來源 URL：`/legal/fdd-terms`）

**Speaker notes**

FDUSD is the canonical "exchange / trading stablecoin" — multi-chain
deployment, ISAE 3000 limited assurance, BVI issuer with HK trust /
custody. The contractual short-name discrepancy (FDD vs FDUSD) is preserved
in the source language; both refer to the same asset.

中文 delivery prompt: FDUSD 是交易所場景代表；點出 ISAE 3000 是「limited assurance」、不是 reasonable assurance 或 audit。

**Source claims**: CLAIM_009, CLAIM_010, CLAIM_062, CLAIM_063, CLAIM_064

## Slide 14 — DAI / USDS — Maker → Sky rebrand / DAI/USDS：MakerDAO 轉 Sky Protocol

**Body**

> - **核心機制**（CLAIM_098）：使用者把 governance-approved 抵押資產存入 Maker Vault；以超額抵押換得 Dai / USDS
> - **清算機制**（CLAIM_099）：跌破 Liquidation Ratio 即自動 Collateral Auction → Reverse Collateral Auction；不足部分由 Protocol Surplus 或 MKR / SKY 稀釋承擔
> - **儲蓄模組**（CLAIM_100）：DSR / Sky Savings Rate 經 sUSDS 給付
> - **外部 actors**（CLAIM_101）：Keepers、Oracles、Global Settlers（後者有單方 Emergency Shutdown 權）
> - **Sky 改版**（CLAIM_102）：sUSDS（yield）、stUSDS（SKY-backed lending 風險資本）、SKY（治理）；USDC ↔ USDS 1:1 零費率轉換；**美國境內 sUSDS / stUSDS / Ecosystem Rewards 不可用**

**Speaker notes**

DAI / USDS is the canonical crypto / RWA-collateralised category. It does
not satisfy the GENIUS Act reserve composition rule, the MiCA ART
reserve-of-assets requirement, or the BoE backing-asset rule on its own
terms — and it is not authorised under any of those regimes. The Sky
rebrand adds a Customer-facing PSM-style USDC ↔ USDS bridge, which makes
it look like a fiat-backed stablecoin at the user-facing layer despite the
underlying mechanics being entirely different.

中文 delivery prompt: 強調「DAI / USDS 是『另一條進入美元體系的通道』，不是 fiat-backed 的延伸」。

**Source claims**: CLAIM_098, CLAIM_099, CLAIM_100, CLAIM_101, CLAIM_102
**Key figures**: KF_024 (Sky Savings Rate 3.65%), KF_025 (stUSDS 5.86%), KF_026 (sUSDS 規模 6.23bn)

**Visual**: 建議自行畫 Vault → Collateral Auction → Surplus / MKR-SKY dilution 流程圖

## Slide 15 — USDe — synthetic dollar via delta-neutral hedge / USDe：合成美元、Delta-中性對沖

**Body**

> - **基本機制**（CLAIM_103）：whitelisted Mint User 存入 backing 資產 → 鑄出 USDe；協議同時在衍生交易所開等額空頭 perp → **1:1 抵押（非超額）**
> - **託管架構**（CLAIM_104）：backing assets 留在 Off-Exchange Settlement 機構託管；Ethena **delegate but never transfer** 給衍生交易所
> - **月度 attestation**（CLAIM_105）：custodians 驗證存在 / 控制 / 估值；明文「none of the backing assets reside directly on exchange partners」
> - **Reserve Fund**（CLAIM_106）：負 funding 期備援 + 末端買家
>   - 組成：USDC + USDT（USD-M）+ 較小 ETH 配置（ETH-M）
>   - 安全：4/10 multi-sig（鑰匙在 Ethena Labs contributors）
>   - 規模：US\$46.6m（Q4 2024）；2023-11 模型基準 US\$20m
> - **收益層**（CLAIM_066）：USDe 本身不付 yield；sUSDe 為 reward-accruing wrapper

**Speaker notes**

USDe is the canonical synthetic-dollar instrument. The 1:1 collateralisation
is structurally different from DAI / USDS overcollateralisation and from
fiat-backed reserves. The Off-Exchange Custody architecture mitigates but
does not eliminate exchange-side counterparty risk, and it does not
address off-exchange custodian default risk or sustained negative-funding
risk. The Reserve Fund is sized in millions, not billions, and is the
absorbing layer for adverse funding regimes.

中文 delivery prompt: USDe 是衍生品工程；風險完全不同於 fiat-backed 與 DAI。Reserve Fund 規模小到讀書會該知道。

**Source claims**: CLAIM_065, CLAIM_066, CLAIM_067, CLAIM_103, CLAIM_104, CLAIM_105, CLAIM_106
**Key figures**: KF_018 (Reserve Fund US\$46.6m), KF_019 (4/10 multi-sig), KF_021 (sUSDe APY 19%), KF_022 (BTC funding 11%), KF_023 (ETH funding 12.6%)

**Visual**: 建議自行畫 spot + short perp 對沖示意圖（Mint User → spot custody / short perp on exchange → 對沖閉合）

## Slide 16 — Direct redemption gating — the recurring pattern / 直接贖回閘門：一個重複出現的模式

**Body**

> 八家發行者，「客戶身分 + KYC + 適格管轄」是普遍贖回門檻 — 無例外。
>
> | 發行者 | 客戶身分要求 | 排除對象 |
> | --- | --- | --- |
> | USDC | Circle Mint account in good standing | 文件未明列 |
> | USDT | 驗證 Tether 客戶 | 美國人（限 ECP 例外）、加拿大人、新加坡人、被制裁人 |
> | PYUSD / USDP / USDG | Paxos Customer（受 OCC / MAS / FIN-FSA 監管實體） | 依司法管轄 |
> | FDUSD | FD121 Account | 美國個人 / 實體 |
> | GUSD | Gemini Customer | 文件未明列 |
> | USDe | Whitelisted Mint User（KYC / AML 完成） | 美國使用者不得成為 Mint User |
>
> 結論：「Redeemable at par」是描述 model；真正的 redemption right 由 counterparty contract 決定。

**Speaker notes**

This is the deck's load-bearing "do not confuse product page with right"
slide. The matrix shows the pattern is universal, not idiosyncratic.
A market participant holding a fiat-backed stablecoin on a chain without
issuer footprint typically has neither direct redemption nor any
contractual relationship with the issuer; they hold a bearer-style
secondary claim only.

中文 delivery prompt: 借此 slide 回到 Guardrail #2（Product page ≠ Direct right），並提醒：許多市場使用者實際上沒有任何直接 redemption right。

**Source claims**: CLAIM_058, CLAIM_060, CLAIM_062, CLAIM_065, CLAIM_073, CLAIM_077

# Part 2 — Reserves & dollar money markets（儲備與美元貨幣市場：5 張）

## Slide 17 — Reserve composition matrix / 儲備組成對照

**Body**

> | 發行者 | 法幣存款 | 短 T-bill / Treasury | Repo / Reverse Repo | MMF | 非現金（黃金 / BTC） | 央行存款 |
> | --- | --- | --- | --- | --- | --- | --- |
> | USDC | ✓ | ✓ | ✓ | ✓（Circle Reserve Fund） | – | – |
> | USDT | ✓ | ✓（~141bn） | – | – | ✓（~20bn 金、~7bn BTC） | – |
> | PYUSD / USDP / USDG（Paxos） | ✓（FDIC） | ✓ | ✓ | ✓ | – | – |
> | GUSD | ✓（FDIC） | ✓ | – | ✓（美國政府證券） | – | – |
> | DAI / USDS | – | RWA Vault 中可能 | – | – | – | – |
> | USDe | Reserve Fund：USDC / USDT | – | – | – | ETH 配置 | – |
> | BoE 2025（提案） | – | UK gilts ≤60% | – | – | – | **40-95%（強制）** |

**Speaker notes**

The matrix shows two structural points. First, all fiat-backed stablecoins
share a Treasury-bill backbone, but they differ in whether they hold bank
deposits, repos, MMF shares, or non-cash exposures alongside it. Second,
the BoE 2025 proposed regime is the only one to require central-bank
deposits as part of backing assets, and is structurally different from
the others.

中文 delivery prompt: 點出「T-bill 是最大公因數，央行存款是 BoE 獨有」這兩個結構特徵。

**Source claims**: CLAIM_026, CLAIM_028, CLAIM_034, CLAIM_075, CLAIM_078, CLAIM_090, CLAIM_098, CLAIM_106
**Visual**: 跨發行者熱力表（slide-ready）；可考慮以「Yes / Partial / No」三色標示

## Slide 18 — USDC vs USDT — same wrapper, different backing / USDC vs USDT：同樣的包裝、不同的底層

**Body**

> - **USDC**（CLAIM_026 / 027）
>   - 主要為 cash + 銀行存款 + 短 T-bill + Circle Reserve Fund
>   - 風險：銀行存款集中、託管商集中、贖回適格性
> - **USDT**（CLAIM_028 / 029，2026-05-01）
>   - ~US\$141bn 直接 / 間接 T-bill 暴險
>   - ~US\$20bn 實體黃金
>   - ~US\$7bn Bitcoin
>   - 風險：非現金部位 mark-to-market、贖回適格、託管 / 監管不對稱
> - **共同**：兩者皆採 AICPA / ISAE attestation，非 financial-statement audit

**Speaker notes**

USDC and USDT are routinely treated as the same product. They are not.
The non-cash exposures in USDT prevent it from being modelled as a pure
cash equivalent, and shift its volatility profile materially. The
attestation regimes look superficially similar but are different
engagements with different scopes.

中文 delivery prompt: 提醒「兩者經常被當作 interchangeable，但實際差很多」；非現金部位 mark-to-market 是關鍵差異。

**Source claims**: CLAIM_026, CLAIM_027, CLAIM_028, CLAIM_029
**Key figures**: KF_001, KF_002, KF_003
**Visual**: 並列圓餅圖（USDC 與 USDT 各一）；圓餅可用 KF_001/002/003 與 USDC 公開比例

## Slide 19 — T-bill demand channel / 對短期國債需求的傳遞通道

**Body**

> Fiat-backed 規模成長 → 對下列美元貨幣市場資產需求上升：
>
> - **≤93-day Treasuries**（GENIUS Act 法定上限；MiCA 對 EMT 60% 同幣別存款部位之外的儲備同質要求）
> - **Overnight repurchase agreements**（隔夜）
> - **Government MMF shares**（限投資前述底層之政府 MMF）
>
> 學界與央行已對此通道建模：
>
> - BIS WP 1270：穩定幣對安全資產價格之影響
> - ECB WP 3174：全球安全資產通道
> - Fed IFDP 1334：取決於資金來源與儲備組成（CLAIM_048）

**Speaker notes**

The T-bill channel is the most quantitative link between stablecoin growth
and dollar money markets. The 93-day maturity cap under GENIUS Act
Sec. 4(1)(A) is the precise mechanism that channels stablecoin reserve
demand into the very short end of the Treasury curve. ECB and BIS working
papers model the resulting safe-asset price effect.

中文 delivery prompt: 借此 slide 第一次把「穩定幣成長 → 短期國債需求」的傳遞通道明確化。

**Source claims**: CLAIM_026, CLAIM_028, CLAIM_075, CLAIM_084；BIS WP1270、ECB WP3174
**Key figures**: KF_004 (93-day cap)

## Slide 20 — Why crypto / RWA and synthetic stablecoins do not aggregate / 為什麼 DAI/USDS 與 USDe 不能與 fiat-backed 加總

**Body**

> - **DAI / USDS**：透過 RWA Vault 與 PSM；governance-approved 抵押資產為主要 backing，不是 issuer-held T-bills
> - **USDe**：透過 perp hedge；backing 為現貨資產（USDT、ETH 等）+ Reserve Fund（USDC + USDT + ETH，~$46.6m）
> - **結論**：兩者進入美元貨幣市場的通道與規模與 fiat-backed 不同；估算「穩定幣對 T-bill 需求」時不能加總
> - **規模參照**（CLAIM_106）：USDe Reserve Fund < $50m vs USDT 流通量 ~$150bn — 數量級差距明顯

**Speaker notes**

Aggregating DAI / USDS and USDe with fiat-backed stablecoins when
estimating Treasury demand is an analytical error common in industry
reporting. The mechanism by which DAI / USDS holds Treasury exposure
(governance-approved RWA Vaults) is fundamentally different from
issuer-held reserves; the mechanism by which USDe touches Treasuries
(via its USDC / USDT Reserve Fund allocation) is small in absolute terms.

中文 delivery prompt: 用「Reserve Fund 50m vs USDT 150bn」對比，讓聽眾感受到數量級差距。

**Source claims**: CLAIM_098, CLAIM_103, CLAIM_106；chapter 3 guardrail 段
**Key figures**: KF_018 (USDe Reserve Fund $46.6m)

## Slide 21 — Reserve income asymmetry / 儲備收益歸誰

**Body**

> - **規則統一**：發行者收儲備收益、持有人合約上明文無權利
> - **issuer terms 層級**：
>   - USDC（CLAIM_059）、USDe（CLAIM_066）、Paxos USD Stablecoins（CLAIM_074）皆明文 no holder yield
> - **法規層級**：
>   - GENIUS Sec. 4(11) 統一禁止任何 interest / yield（CLAIM_086）
>   - MiCA Art. 40 對 ART 同樣禁止（CLAIM_071）
> - **例外架構**：
>   - sUSDe / sUSDS / stUSDS 為「分離的 reward-accruing wrapper」，不是 USDe / USDS 本身
>   - 學界用語：「stablecoin = par-value claim, wrapper = yield-bearing security」

**Speaker notes**

Reserve income captured by the issuer is structurally significant for the
business model. The GENIUS Act and MiCA ART both legislatively prohibit
the issuer from passing this income to holders in the form of interest or
yield. The "reward-accruing wrapper" architecture (sUSDe, sUSDS, stUSDS)
is the workaround — it separates the par-value claim from the income
right at the contract level.

中文 delivery prompt: 強調「par-value claim 與 yield-bearing claim 是分離的兩個合約」，這是合規與商業模型同時要求的設計。

**Source claims**: CLAIM_059, CLAIM_066, CLAIM_071, CLAIM_074, CLAIM_086

# Part 3 — Law & regulation（法律與監管：11 張）

## Slide 22 — Four jurisdictions on one map / 四司法管轄一覽

**Body**

> 五個制度，六個比較維度（細節下文）：
>
> | 制度 | 司法管轄 | 立法 / 諮詢年度 | 規範主體 |
> | --- | --- | --- | --- |
> | GENIUS Act | US 聯邦 | 2025 立法（PL 119-27） | Permitted payment stablecoin issuer |
> | MiCA ART | EU | 2023 立法（生效中） | Asset-referenced token issuer |
> | MiCA EMT | EU | 2023 立法（生效中） | E-money token issuer |
> | BoE 系統性 | UK | 2023 討論稿 / 2025 諮詢 | Recognised systemic stablecoin issuer |
> | NYDFS 指引 | New York | 2022 | DFS-regulated virtual currency entity |

**Speaker notes**

This is the index slide for Part 3. Four jurisdictions, five regimes
(MiCA splits into two). The next 10 slides walk through each one and end
with a six-dimension cross-jurisdiction comparison.

中文 delivery prompt: 開場提醒「不要把『穩定幣監管』當作單一制度」；五制度同時存在、且有重疊但不等價。

**Source claims**: CLAIM_082-087, CLAIM_069-071, CLAIM_088-091, CLAIM_036-040

## Slide 23 — GENIUS Act — eligible issuer & transition / GENIUS Act：適格發行者與三年過渡

**Body**

> - **Sec. 3(a)**：非 "permitted payment stablecoin issuer" 不得在美國發行 payment stablecoin（CLAIM_082）
> - **Sec. 3(c)**：Treasury 可發布 limited safe harbors（限縮、de minimis）
> - **Sec. 3(b)（CLAIM_083）**：
>   - 立法後 **3 年**起，digital asset service provider 不得向美國人提供 / 銷售非適格發行人發行之 payment stablecoin
>   - 外國發行人需具備守 lawful order 之 technological capability，並透過 Sec. 18 互惠安排
> - **Sec. 3(f)**：違反 Sec. 3(a) 最高罰金 \$1m、刑期 5 年

**Speaker notes**

Two ideas matter here. First, the issuer perimeter is enumerated — only
"permitted" entities may issue. Second, the 3-year distribution transition
gate means that DASPs (exchanges, brokers, custodians) will be the
chokepoint for market access; foreign issuers must affirmatively comply
with US lawful orders to be distributed in the US after the transition.

中文 delivery prompt: 強調「3 年過渡」是市場真正的時點 — 之後 DASPs 變成 gatekeeper。

**Source claims**: CLAIM_082, CLAIM_083
**Key figures**: KF_005 (3-year transition), KF_007 ($1M fine)

## Slide 24 — GENIUS Act — reserve composition rule / GENIUS Act：儲備組成規則

**Body**

> **Sec. 4(1)(A)** 列舉式 HQLA 清單（CLAIM_084）：
>
> 1. US 鑄幣與 currency（含 Federal Reserve notes）、Fed 帳戶餘額
> 2. Insured depository institution 之 demand deposits（subject to FDIC/NCUA 限制）
> 3. **Treasury bills/notes/bonds，剩餘或原始到期 ≤93 天**
> 4. Overnight repurchase agreements，以該等 Treasuries 為擔保
> 5. Overnight reverse repurchase agreements，超額擔保、tri-party 或中央清算
> 6. 投資於上述底層之政府 MMF
> 7. 經 primary regulator 核准之其他類似流動性政府資產
>
> **Sec. 4(1)(C)-(D) + 4(3)**：月度儲備組成公布；註冊會計師事務所月度 examination；CEO/CFO 認證受 18 U.S.C. 1350(c) 刑責約束（CLAIM_085）

**Speaker notes**

The 93-day Treasury cap is the most consequential single number in the
statute. It channels stablecoin reserve demand into the very short end of
the Treasury curve and constrains issuer interest-rate risk. The monthly
disclosure and registered-public-accounting-firm examination is the
federal-statute version of the AICPA attestation regime already used by
issuers.

中文 delivery prompt: 重點是「93 天上限」與「月度 + 註冊會計師檢視 + CEO/CFO 刑責認證」三層保護。

**Source claims**: CLAIM_084, CLAIM_085
**Key figures**: KF_004 (93 天), KF_006 (月度 examination)

## Slide 25 — GENIUS Act — yield prohibition & insolvency priority / GENIUS Act：禁付收益＋客戶破產優先

**Body**

> - **Sec. 4(11)**（CLAIM_086）：
>   - 任何 permitted 或 foreign payment stablecoin issuer，**不得單純因 holding / use / retention** 而給予持有人任何形式之 interest 或 yield（含現金、tokens、其他 consideration）
> - **Sec. 11**（CLAIM_087）：
>   - 在任何 permitted payment stablecoin issuer 之 insolvency 程序中
>   - 客戶就其持有之 payment stablecoin 對發行人之債權
>   - **優先於非客戶**（但與其他客戶就同 stablecoin 之債權相互平等）

**Speaker notes**

The yield prohibition is the federal-statute equivalent of MiCA ART
Article 40 and ports the issuer-terms no-yield language across all
permitted issuers. The customer-priority insolvency rule is the most
holder-protective insolvency rule in the v0.3 archive — stronger than
NYDFS reserve segregation, stronger than the BoE shortfall reserve, and
stronger than MiCA Article 47's operational wind-down plan in pure
priority terms.

中文 delivery prompt: 強調「客戶破產優先」是 GENIUS Act 最 holder-protective 的條款 — 比歐盟、英國、紐約都強。

**Source claims**: CLAIM_086, CLAIM_087

## Slide 26 — MiCA ART vs EMT / MiCA：ART 與 EMT 是兩套規則

**Body**

> | 維度 | ART（asset-referenced token） | EMT（e-money token） |
> | --- | --- | --- |
> | 發行人 | 經 authorised ART issuer | 必為 credit institution 或 e-money institution（Art. 48） |
> | 儲備 | 至少等於持有人債權、segregated（Art. 36） | ≥30% 同幣別存款於 credit institution + 餘額於 secure low-risk 同幣別資產（Art. 54） |
> | 贖回權 | Permanent redemption right against issuer（Art. 39）；funds 或 referenced assets；原則無 fee | At-any-time, par-value 贖回（Art. 49） |
> | 利息 | 禁止（Art. 40） | Art. 49 par-value 規則使利息不可實現 |

**Speaker notes**

The single most important thing for the reading group is that ART and EMT
are different regimes for different products. ART covers tokens
referenced to multiple assets or to a non-EU currency; EMT covers tokens
referenced to a single EU official currency. Most USD-pegged stablecoins
operating in the EU register as EMTs (USDC, USDT EU entity, etc.), not as
ARTs.

中文 delivery prompt: 強調「ART 與 EMT 不是同一套規則」。

**Source claims**: CLAIM_042, CLAIM_043, CLAIM_069, CLAIM_070, CLAIM_071
**Key figures**: KF_008 (ART 60% deposits in referenced currency), KF_009 (EMT 30% deposits)

## Slide 27 — MiCA significant-token + recovery / redemption plans / MiCA significant-token 與復原 / 贖回計畫

**Body**

> - **Significant-ART（CLAIM_094）**：EBA 在符合 Art. 43(1) 至少三項時 classify；額外義務包含 FRAND custody、liquidity management policy、EBA RTS **同幣別存款 ≥60%**
> - **Significant-EMT（CLAIM_097）**：EBA 分類；Art. 58(1) 套用 Art. 45(1)-(4) + **半年獨立 audit**
> - **每位 ART issuer 須備**：
>   - **Recovery plan（CLAIM_095, Art. 46）**：含 liquidity fees on redemptions、日贖回上限、redemption suspension；competent authority 可暫停贖回
>   - **Redemption (wind-down) plan（CLAIM_096, Art. 47）**：因主管機關判定無力履約時啟動，含臨時管理人指定

**Speaker notes**

This is the load-bearing tier-2 layer of MiCA. Recovery plans formalise
the redemption-suspension power that the issuer-terms layer (Paxos terms,
FDUSD terms, USDC terms) already implies; redemption (wind-down) plans
formalise the operational insolvency machinery in a way the GENIUS Act
chose not to.

中文 delivery prompt: 強調「歐盟採營運層 wind-down 計畫；美國採法定破產優先」 — 兩個方向完全不同。

**Source claims**: CLAIM_094, CLAIM_095, CLAIM_096, CLAIM_097
**Key figures**: KF_008 (60% deposits floor), KF_010 (6-month audit)

## Slide 28 — BoE 2023 → 2025 evolution / BoE：從 100% 央行存款到 40/60 split

**Body**

> - **2023 討論稿**（CLAIM_088）：偏好 **100% Bank of England 央行存款** backing；理由：消除 credit / liquidity / market risk 並維持 singleness of money
> - **2025 諮詢修正**（CLAIM_090）：
>   - **至少 40%** unremunerated BoE 央行存款
>   - **最多 60%** 短期英鎊計價英國公債
>   - Step-up regime：systemic-at-launch 發行人初期可達 **95%** 英國公債、隨規模回到 60%
>   - **業界回饋**：100% 央行存款不可行（無收益、商業模式不可持續）
> - **發行人額外義務**：recovery & administration plan + 法定信託 shortfall reserve（CLAIM_089）

**Speaker notes**

The BoE 2023-to-2025 trajectory is instructive. The Bank originally
preferred the cleanest financial-stability rule (100% central-bank
deposits) and accepted significant softening based on industry
consultation responses about business model viability. The compromise
40/60 rule still gives the BoE a central-bank-deposit floor that no other
regime has.

中文 delivery prompt: 帶觀眾看「制度設計如何受業界回饋而修正」這個過程；不要把法規當作 static。

**Source claims**: CLAIM_088, CLAIM_089, CLAIM_090
**Key figures**: KF_011 (40% CBD), KF_012 (60% gilts), KF_013 (95% step-up)

## Slide 29 — BoE holding limits — a UK-only feature / BoE 持有上限：英國獨有設計

**Body**

> **2025 諮詢提出量化持有上限**（CLAIM_091）：
>
> - **個人**：£20,000 per-coin
>   - 對照：digital pound 諮詢之個人持有區間 £10,000–£20,000
> - **企業**：£10 million
>   - 例外：零售商與服務於零售客戶之中介可申請豁免
>
> GENIUS Act 與 MiCA 皆無類似的量化上限。

**Speaker notes**

This is the most distinctive single feature of the UK regime. No other
jurisdiction has a quantitative holding cap. The cap appears designed to
limit deposit-substitution effects on UK banks — i.e., to prevent a
single stablecoin from acquiring a deposit-like funding base large enough
to be a banking-system competitor.

中文 delivery prompt: 強調「量化持有上限」是 BoE 獨有；可能是為了限制 stablecoin 對英國商業銀行存款的替代。

**Source claims**: CLAIM_091
**Key figures**: KF_014 (£20,000), KF_015 (£10m)

## Slide 30 — ESMA supervisory practice / ESMA：實務監管預期

**Body**

> - **CASP 授權監管簡報（CLAIM_092）**：
>   - **「沒有低風險 CASP」**
>   - 加重審查觸發門檻（任一即可）：
>     - >1,000,000 EU 年活躍用戶 或 €3,000,000,000 資產負債表
>     - >200,000 跨境（home Member State 外）年活躍用戶
>     - 複雜集團結構（EMI / MiFID / CASP 多框架）
>     - 關鍵職能外包 或 外包至 EU 境外
> - **Article 82 transfer service 指引（CLAIM_093）**：
>   - Pre-contractual disclosure：DLT 網絡、執行時限、不可逆時點、費用、拒絕條件、責任
>   - **TOFR（EU 2023/1113）Article 14 旅行規則合規**為轉帳執行前置條件

**Speaker notes**

ESMA's supervisory practice is the operational complement to the MiCA
statutory text. The "no low-risk CASPs" principle and the quantitative
elevated-scrutiny thresholds shape how national competent authorities
treat actual stablecoin distribution platforms in the EU. The TOFR
Article 14 compliance gate makes the EU travel-rule regime live for
crypto-asset transfers.

中文 delivery prompt: 借這張提醒「實務監管預期」與「法定條文」是兩個層次，前者更直接影響執行細節。

**Source claims**: CLAIM_092, CLAIM_093
**Key figures**: KF_029 (1M EU users), KF_030 (€3B BS), KF_031 (200k cross-border)

## Slide 31 — Cross-jurisdiction comparison (1/2) / 跨管轄比較（上）

**Body**

> 五制度（GENIUS、MiCA ART、MiCA EMT、BoE、NYDFS）在三個維度上對比。
>
> 詳見並用 `07_final_report/comparison_table_slide_31.md` 的完整表格。
>
> 核心 takeaway：
>
> - **適格發行者**：五制度都採許可制；認定機制不同（美國列舉、歐盟 dual-track ART / EMT、英國 HMT 認定、紐約 DFS 授權）
> - **儲備組成**：T-bills 是最大公因數；BoE 為唯一強制要求 CBD floor
> - **贖回權**：時限與費率規則最分歧 — NYDFS 預設 T+2、MiCA ART 為 permanent、GENIUS 為定義式義務、BoE 含 safeguarding + redemption-fee 限制

**Speaker notes**

This is split slide 1/2. The visual is the full table from
`comparison_table_slide_31.md`. The takeaway is that the regimes converge
structurally but diverge on the precise mix of reserve assets and on
redemption timing.

中文 delivery prompt: 不需逐格念表；指出「五制度在結構上趨同、在細節上差異實質」即可。

**Source claims**: chapter 4 末比較表上半
**Visual**: 直接複製 `comparison_table_slide_31.md` 中之表格

## Slide 32 — Cross-jurisdiction comparison (2/2) / 跨管轄比較（下）

**Body**

> 同五制度，三個更分歧的維度。
>
> 詳見並用 `07_final_report/comparison_table_slide_32.md` 的完整表格。
>
> 核心 takeaway：
>
> - **破產 / 清算**：美國 = 客戶優先（法定）；歐盟 = 營運清算計畫 + 臨時管理人；英國 = 法定信託 + shortfall reserve；紐約 = 月度 / 年度 CPA 檢視
> - **持有人收益**：高度一致禁止
> - **Significant-token 門檻**：美國無；歐盟與英國各有不同型態的「規模門檻 → 額外義務」設計

**Speaker notes**

The bottom-half table is where the regimes diverge most. The US chose a
bankruptcy-priority rule; the EU chose an operational wind-down plan; the
UK chose a statutory trust plus shortfall reserve; New York chose monthly
examination. The yield prohibition is the only dimension where convergence
is essentially complete.

中文 delivery prompt: 強調「破產處理與 significant-token 是制度差異最大的維度」 — 也是跨境等價 (equivalence) 判斷最難的地方。

**Source claims**: chapter 4 末比較表下半
**Visual**: 直接複製 `comparison_table_slide_32.md` 中之表格

# Part 4 — Central-bank & policy framing（央行與政策框架：4 張）

## Slide 33 — Fed IFDP 1334 — a conditional channel / Fed IFDP 1334：取決於模型的傳遞通道

**Body**

> Federal Reserve IFDP 1334（Liao & Caramichael, 2022, p. 2 Abstract）：
>
> 穩定幣對銀行與 credit provision 之衝擊 **取決於**：
>
> 1. 流入資金的來源
> 2. 儲備組成的選擇
>
> 兩種模型對比：
>
> - **Two-tiered banking**：穩定幣發行可與傳統信貸並存
> - **Narrow-bank**：加深 disintermediation 但強化 peg 穩定
>
> 結論：**沒有確定的衝擊路徑**，取決於制度與營運選擇。

**Speaker notes**

The Fed framing is conditional, not deterministic. This is the analytical
template that policymakers and academics tend to adopt: the question is
not "will stablecoins disrupt banking?" but "under which institutional
configuration?". This framing is what allows GENIUS Act, MiCA, and BoE to
arrive at different reserve composition rules without any of them being
obviously wrong.

中文 delivery prompt: 強調「央行框架是 conditional 的；不同制度選擇導出不同結果」。

**Source claims**: CLAIM_044, CLAIM_047, CLAIM_048

## Slide 34 — IMF — Making Stablecoins Stable / IMF：穩定幣穩定化的取捨

**Body**

> IMF WP/26/74（Li et al., April 2026, p. 2 Abstract）：
>
> - 無監管 private 穩定幣均衡是 **次優**（issuers 持有風險資產 → 提高 run risk）
> - 安全資產 backing 可降低 run risk
> - 但同時 **壓縮 issuer 利潤** → 削弱 issuance 誘因
> - **隱含**：若僅以儲備規則處理，需要替代營收機制（如服務費、infrastructure rent）才能維持發行誘因

**Speaker notes**

The IMF Diamond-Dybvig-style framing identifies the central trade-off that
all four jurisdictions are trying to manage. GENIUS, MiCA, BoE all chose
to impose safe-asset backing rules — and all four implicitly assume that
issuers will find non-reserve-income revenue to sustain operations
(transaction fees, infrastructure services, ecosystem rewards). This is
why the no-holder-yield rules are uniform across regimes.

中文 delivery prompt: 連到 Slide 21（持有人收益不對稱）：制度設計把儲備收益保留給 issuer 是 by design，不是 oversight。

**Source claims**: CLAIM_049

## Slide 35 — IMF — 18% / $300bn event study / IMF：18% / $300bn 事件研究

**Body**

> IMF WP/26/52（Copestake et al., March 2026, p. 2 Abstract）：
>
> - **事件研究**：美國有利穩定幣 payment 法案訊息
> - **發現**：上市既有支付公司股票市值縮水 **18%**（約 **US\$300 billion**）
> - **細分**：
>   - 跨境支付為主的 incumbents 受影響更大
>   - 受網絡效應保護的 incumbents 受影響較小
>   - 已提供 crypto 相關服務之 incumbents 受影響較小
> - **重要警語**：此為市場預期證據，**不是已實現的支付採用**

**Speaker notes**

This is the strongest quantitative signal in the central-bank / IMF
literature that stablecoins are being priced as a credible challenge to
incumbent payment firms. It is also the most prone to misreading: the
\$300bn figure is market-cap reduction at event windows, not stablecoin
payment volume. The deck preserves the distinction.

中文 delivery prompt: 強調「18% / $300bn 是市場預期，不是實際採用」 — 這是 Guardrail #3 的學術佐證。

**Source claims**: CLAIM_050
**Key figures**: KF_027 (18%), KF_028 (~$300bn)

## Slide 36 — Taiwan-specific synthesis — open / 台灣場景綜整：尚未做

**Body**

> 本研究 v0.3 **尚未完成台灣面向綜整**。
>
> 已備好的框架（CLAIM_044–CLAIM_050）可投射的主題：
>
> - NTD 穩定幣與央行立場
> - FX 監控與外匯管制（資金外移管道風險）
> - Digital dollarisation 對台灣支付體系的影響
> - 銀行存款替代（deposit substitution）與本地銀行流動性
> - 貨幣主權與美元穩定幣作為「事實上美元化」載體
>
> 必要來源：CBC（中央銀行）公報、TWFRC（金融研究院）報告。
>
> **建議**：v0.4 以既有 CBC / TWFRC 來源做台灣綜整，不引入新外部來源。

**Speaker notes**

This is an honest "not done yet" slide. The framework from Fed and IMF is
in place; the Taiwan-specific application is open work. The reading group
may want to discuss which themes are most worth prioritising for v0.4.

中文 delivery prompt: 直白告訴聽眾「v0.3 還沒做台灣面向」；邀請讀書會討論優先順序。

**Source claims**: unresolved_open_questions.md / chapter 9.3 第 5 點

# Part 5 — USDPT and cross-border（USDPT 與跨境支付：4 張）

## Slide 37 — What is documented about USDPT / USDPT：目前已有的證據

**Body**

> v0.3 archive 內的 **primary-source 支撐**：
>
> - **Western Union 2026 launch release**（CLAIM_051 / 052）：
>   - USDPT 為 U.S. Dollar Payment Token
>   - 建於 Solana
>   - 由 Anchorage Digital Bank 發行
>   - 與 Digital Asset Network 並推
>   - 「fully backed by U.S. dollars」（無 USDPT-specific reserve report）
> - **Anchorage OCC comment letter**（CLAIM_051）：佐證 Anchorage 為預期發行人
> - **Fireblocks release**（CLAIM_053）：
>   - 提供 wallet / settlement / financial-operations 基礎設施
>   - 包含 SWIFT MT940/MT942 格式輸出（**back-office 對帳，非 settlement**）

**Speaker notes**

This slide lists what we know. It is deliberately concrete — only what
primary sources support, no inferred architecture. The Fireblocks MT940 /
MT942 line is a particular trap: it's accounting message format support,
not settlement.

中文 delivery prompt: 用「我們只知道這些」開場，為 Slide 38–39 的限制做鋪墊。

**Source claims**: CLAIM_051, CLAIM_052, CLAIM_053

## Slide 38 — Four-layer separation / 四層分離框架

**Body**

> 任何 USDPT 結論必須分四層分析，**不可一概以「USDPT 取代 SWIFT」概括**：
>
> 1. **Layer 1 — 消費者匯款 UX**：WU app / 代理櫃台（既有）
> 2. **Layer 2 — WU 代理網絡**：全球 cash-in / cash-out 通道（既有）
> 3. **Layer 3 — 穩定幣發行 + 鏈上轉帳**：Anchorage 發行 USDPT on Solana；Fireblocks orchestration（規劃中）
> 4. **Layer 4 — 儲備 + 銀行 / correspondent 結算**：USDPT 儲備 + SWIFT messaging + Fedwire / CHIPS（規劃中，最少文件）

**Speaker notes**

The four-layer framing is the load-bearing analytical move of the chapter
on USDPT. Layers 1-2 exist today and are documented; Layer 3 is partially
documented (Anchorage / Solana / Fireblocks); Layer 4 is least documented.
Any "USDPT replaces SWIFT" claim conflates Layer 4 with Layer 3.

中文 delivery prompt: 強調四層各自有不同的成熟度與文件支撐 — 不可混為一談。

**Source claims**: chapter 6 framing；AGENTS.md guardrail
**Visual**: 使用 `06_flow_diagrams/usdpt_settlement_flow.md`（已重畫為四 swim-lane）

## Slide 39 — What is NOT documented (frozen) / 尚未取得（且決定 freeze）

**Body**

> v0.3 **不在公開檔案** 內的關鍵 USDPT 文件：
>
> 1. Product terms（直接持有人權利）
> 2. USDPT-specific reserve report（與 WU 公司財報分離）
> 3. On-chain 合約地址
> 4. 客戶到客戶 end-to-end settlement workflow
> 5. WU 代理是否處理 USDPT 之 cash-out
>
> v0.3 user decision：**freeze、不啟動 web-scraping**。
>
> 等待主要來源公布；若 v0.4 取得，依 registry → digest → claim → matrix → chapter 工作流補入。

**Speaker notes**

Honesty slide. The freeze decision is deliberate; chasing dynamic HTML
risks producing speculative claims that violate the guardrails. The
reading group should understand that the framework is in place to absorb
the missing documents once they appear, but the framework will not stretch
to fill in the gap.

中文 delivery prompt: 明確告訴聽眾「v0.3 決定不去 scrape」，原因是 guardrail compliance，不是技術困難。

**Source claims**: chapter 9.2.1；unresolved_open_questions.md

## Slide 40 — Why conditional framing matters / 為何必須條件式敘事

**Body**

> 在沒有 workflow 文件之前，**以下宣稱皆無法支撐**：
>
> - 「USDPT 取代 SWIFT」
> - 「USDPT 取代 correspondent banking」
> - 「USDPT 取代 Fedwire / CHIPS」
> - 「USDPT 取代 WU 零售匯款管道」
>
> 本研究保留 **可能改變後端 workflow** 的描述，但不做 **取代** 的結論。
>
> 這是 AGENTS.md 不可協商規則 #4 的直接應用。

**Speaker notes**

This slide is the explicit statement of the guardrail. The reason for the
discipline is not academic conservatism; it is that the four-layer framing
in Slide 38 makes clear that the substitutions implied by "USDPT replaces
SWIFT" cross layers and require documentary support that does not exist.

中文 delivery prompt: 直接念出規則 #4：「無 workflow 文件即不可宣稱替代」。

**Source claims**: AGENTS.md non-negotiable rule #4；chapter 6 framing

# Part 6 — On-chain data（鏈上數據：3 張）

## Slide 41 — Volume ≠ payment demand / 轉帳量不等於支付需求

**Body**

> 鏈上 transfer volume 包含以下類別，**不能直接等同於實際支付需求**：
>
> - 交易所內部 / 跨交易所流動
> - 跨鏈 bridge 流動
> - 套利 / 做市流動
> - 協議內部流動（restaking、collateral 移轉等）
>
> Adjusted-volume datasets（Visa Onchain Analytics、Artemis）嘗試扣除上述
> 類別，但 **方法論不互通**，且 v0.3 archive **尚未取得 reproducible export**。

**Speaker notes**

This is Guardrail #3 in operational form. Stablecoin "supply growth",
"market cap", and "transfer volume" headlines should be treated as raw
signals only, not as evidence of payment adoption. The methodology
adjustments matter, and the underlying data is paywalled in many cases.

中文 delivery prompt: 借此 slide 把市場常見的「穩定幣支付量達 X 萬億」這類數字打折扣。

**Source claims**: AGENTS.md non-negotiable rule #5；chapter 7 framing

## Slide 42 — What DeFiLlama supply data can and cannot say / DeFiLlama 供給資料的可用範圍

**Body**

> - **可用於**：
>   - 各 stablecoin 流通量隨時間變化
>   - 鏈別分布（Ethereum / Solana / Tron 等）
>   - 發行者市占
> - **不可用於**：
>   - 實際支付規模
>   - 持有人類別（zk 不揭露）
>   - 商業 / 零售比重
>   - 跨境匯款 vs 國內支付區分
> - 來源：DeFiLlama stablecoin API（已 archived 於 source registry）

**Speaker notes**

DeFiLlama is fit for supply-side analysis but is structurally unable to
report on the use-case mix. Confusing "supply" with "payment volume" is a
common analytical error in industry reporting. The methodology distinction
should be preserved in any final report figure.

中文 delivery prompt: 把 DeFiLlama 當「供給快照」用、不當「使用快照」用。

**Source claims**: CLAIM_054 （Artemis methodology basis）；market_data_source_digest

## Slide 43 — What is missing / 缺什麼

**Body**

> v0.3 **未取得** 的關鍵市場數據：
>
> 1. Visa Onchain Analytics adjusted-volume export
> 2. Artemis methodology 超出 `CLAIM_054` 的細部說明
> 3. McKinsey-Artemis 聯合分析（manual download）
>
> 後果：
>
> - Chapter 7 結論僅停在 **定性** 層級
> - 「穩定幣已取代匯款 / 卡片支付 / 零售支付」 之數量級宣稱不予支持
>
> v0.4 條件：取得任一 reproducible export 後，依工作流補入。

**Speaker notes**

The freeze decision applies here just as it does for USDPT. The data is
not unobtainable; it is paywalled or behind dynamic interfaces that the
v0.3 scope decision deliberately excluded.

中文 delivery prompt: 與 Slide 39（USDPT 缺什麼）一起用，建立「v0.3 對缺資料的態度是 freeze 而非 guess」的訊息。

**Source claims**: unresolved_open_questions.md v0.2 deferrals

# Part 7 — Failure cases（失敗案例：2 張，視時間可省）

注意：v0.3 對失敗案例的「分類」已 anchored 到既有 claim；但「個案研究」（Terra UST、Iron Finance、USDC SVB depeg、Tether 歷史儲備爭議、DAI 黑色星期四）在 v0.3 不在 source archive 內。投影片若要含個案，需由報告人自行引用，或 commission v0.4 extraction。

## Slide 44 — Risk taxonomy anchored to v0.3 evidence / v0.3 evidence 已支撐的風險分類

**Body**

> 八類風險，各對應 v0.3 claim：
>
> 1. **Reserve / 託管風險**：CLAIM_069、CLAIM_075、CLAIM_084、CLAIM_090
> 2. **贖回風險**：CLAIM_058、CLAIM_073、CLAIM_077、CLAIM_095
> 3. **銀行存款風險**：CLAIM_075（Paxos）、CLAIM_084（GENIUS Sec 4(1)(A)(ii)）
> 4. **市場流動性風險**：CLAIM_094（MiCA Art 45 stress test）、CLAIM_089（BoE shortfall reserve）
> 5. **Oracle / 抵押風險**：CLAIM_099、CLAIM_101（DAI / USDS）
> 6. **治理風險**：CLAIM_098、CLAIM_101、CLAIM_106（USDe 4/10 multi-sig）
> 7. **Basis / funding 風險**：CLAIM_103、CLAIM_104、CLAIM_106
> 8. **監管風險**：CLAIM_082、CLAIM_086、CLAIM_087、CLAIM_096

**Speaker notes**

The taxonomy itself is anchored. Specific historical case studies are not
yet in the v0.3 source archive. This slide presents the analytical
framework without overpromising.

中文 delivery prompt: 點出「我們知道風險存在於哪些通道」而不是「我們知道哪一場 historical 失敗」。

**Source claims**: chapter 8.1 全段

## Slide 45 — Lessons preserved as guardrails / 失敗案例如何形塑研究 guardrail

**Body**

> 過去失敗事件直接落地為本研究的五條 guardrail：
>
> | 過去模式 | 對應 Guardrail |
> | --- | --- |
> | 早期 transparency 爭議 | Attestation ≠ Audit |
> | 市場 narrative 誇大採用 | Volume ≠ Payment demand |
> | 媒體誤把 SWIFT 視為 settlement | SWIFT 是 messaging |
> | Terra UST 2022 崩潰 | 三類穩定幣不可加總 |
> | 業界敘事超越 primary evidence | 保留 open question 不猜測 |
>
> 個案層為 v0.4 open work，候選包含：
>
> - 2023-03 USDC SVB depeg
> - 2022 Terra UST 崩潰
> - 2017-2021 Tether 儲備揭露爭議
> - 2020-03 DAI 黑色星期四
> - 已記錄之 USDe 負 funding 事件（待）

**Speaker notes**

Even without case studies in the archive, the guardrails themselves are
historical-failure-shaped. This slide makes that lineage explicit and
invites the v0.4 case-study extraction prioritisation.

中文 delivery prompt: 借「失敗如何形塑 guardrail」收尾失敗案例段；不是個案，但是個案的累積教訓。

**Source claims**: AGENTS.md non-negotiable rules；chapter 8.3 / 8.4

# Part 8 — Closing（收尾：4 張）

## Slide 46 — What the evidence supports / 證據可支撐什麼

**Body**

> 六條 v0.3 高信心結論：
>
> 1. **穩定幣是美元流動性的重組，不是替代** — CLAIM_026-034、CLAIM_075、CLAIM_078
> 2. **持有人直接贖回權窄於 product page 語言** — CLAIM_058、CLAIM_060、CLAIM_073、CLAIM_077、CLAIM_065
> 3. **Attestation ≠ Audit；現已寫入聯邦法** — CLAIM_080、CLAIM_085、CLAIM_097
> 4. **四司法管轄六維比較：結構趨同、細節分歧** — chapter 4 比較表
> 5. **央行框架是 conditional 通道，不是確定性威脅** — CLAIM_048、CLAIM_049、CLAIM_050
> 6. **三類穩定幣不可加總** — CLAIM_098、CLAIM_103、CLAIM_106

**Speaker notes**

This is the "if you remember six things" slide. Each finding is keyed to a
claim cluster; speaker can drill into any if asked.

中文 delivery prompt: 用「六條」作為收尾的核心訊息；其他都是支撐。

**Source claims**: chapter 9.1 全段

## Slide 47 — What is conditional / 條件式可言

**Body**

> 兩條 v0.3 條件式結論（**未取得 primary evidence 之前不可強化為斷言**）：
>
> 1. **USDPT 為 planned product，不是運作中系統**
>    - 已有：launch、issuer 身分、infrastructure partnerships
>    - 未取得：product terms、reserve report、合約地址、workflow
>    - 結論：不可宣稱 USDPT 取代 SWIFT / 對應行 / Fedwire / CHIPS / WU 零售匯款管道
> 2. **支付需求結論止於 qualitative**
>    - 已有：Fed / IMF 之 conditional framing
>    - 未取得：Visa adjusted volume、Artemis methodology beyond CLAIM_054
>    - 結論：「穩定幣已取代匯款 / 卡片」之數量級宣稱不予支持

**Speaker notes**

These two are the load-bearing conditional pieces. If a reader takes one
piece away from this slide, it should be: a research report can be honest
about what it does not support and still be useful.

中文 delivery prompt: 強調「條件式 ≠ 沒結論」 — 條件式是研究紀律的體現。

**Source claims**: chapter 9.2

## Slide 48 — What remains unresolved / 五項仍未解

**Body**

> 1. **USDPT 產品層** — product terms / reserve / contract / workflow
> 2. **Adjusted on-chain 支付量** — Visa、Artemis 方法論
> 3. **CLARITY Act 對 stablecoin-specific 條款** — 與 market-structure 條款分離
> 4. **跨境等價（equivalence）認定** — GENIUS Sec 3(b)(2) / Sec 18 與 MiCA / BoE / NYDFS 之 substantially-similar 判斷
> 5. **台灣場景綜整** — NTD 穩定幣、FX 監控、digital dollarisation、deposit substitution、貨幣主權

**Speaker notes**

The unresolved list is the v0.4 backlog. Each item is concrete enough to
commission, and the workflow to absorb new evidence is in place.

中文 delivery prompt: 對讀書會說「這五項是下一輪研究的 backlog」 — 邀請討論優先順序。

**Source claims**: chapter 9.3

## Slide 49 — Reading-group framing questions / 留給讀書會的三個問題

**Body**

> 留三個問題給讀書會討論：
>
> 1. **「對哪個持有人、對哪個 counterparty、在哪個司法管轄」**才是真正的問題 — Slide 16 (8 issuers × redemption gating) 是工作工具
> 2. **儲備規則正在收斂、但速度不一** — GENIUS / MiCA / BoE 在 HQLA 上重疊、在 remuneration 與央行存款角色上分歧；未來 12-24 個月制度才會穩定
> 3. **監管範圍與經濟範圍是否對齊？** — DAI / USDS、USDe 在四套 payment stablecoin 法定中皆 out of scope，但經濟上已非小規模；perimeter 是否該擴大？

**Speaker notes**

The three discussion questions are designed to invite specific responses
rather than open-ended commentary. Each one connects to a specific part of
the deck (Slide 16, Slide 31-32, Slide 4) so the speaker can redirect
discussion back to evidence if needed.

中文 delivery prompt: 用三個問題收尾；不下結論，讓讀書會討論成為研究的一部分。

**Source claims**: chapter 9.4 三點

# Appendix slides（附錄，視聽眾時間決定是否放）

## Slide A1 — Claim map / 引用對照表

**Body**

> 投影片內的來源簡稱 → CLAIM_XXX → source_id 對照
>
> 全 106 條 claim 的對照存於：
>
> - `03_claim_tables/claim_table_master.csv`
> - `01_sources/source_registry.csv`
>
> 投影片內所有引用都可由 CLAIM ID 反查至 primary source 的 local archive path。

**Speaker notes**

This slide signals to academic-minded audience members that the deck is
fully traceable. The CSVs in the repository contain the full citation
chain.

中文 delivery prompt: 簡短帶過；強調「可以反查到原始 source」即可。

**Source claims**: 全部 106 條

## Slide A2 — Disclaimer / 免責與範圍

**Body**

> - 本研究 **不構成投資建議**
> - USDPT 結構為 **inferred from launch announcement**，不是確認的 production architecture
> - 儲備數字均為 **point-in-time attestation / examination**，不是 audit
> - 鏈上 transfer volume **不等於** 實際支付需求
> - 三類穩定幣（fiat-backed / crypto-RWA / synthetic-dollar）**不可加總**
> - MiCA ART 與 EMT 規則 **分開處理**
> - 來源 cut-off 日期：2026-05-15

**Speaker notes**

The disclaimer slide is required for an academic reading group; it codifies
the five guardrails in a compact form and adds a cut-off date.

中文 delivery prompt: 必放；給聽眾與後續引用者一個 clear 的 disclaimer。

**Source claims**: AGENTS.md non-negotiable rules

## Slide A3 — Source registry / 來源登錄

**Body**

> 130 個 archived primary source，分類如下：
>
> | 類別 | 筆數 |
> | --- | --- |
> | issuer | 46 |
> | central_bank | 14 |
> | law | 16 |
> | payment_settlement | 6 |
> | archive_reference | 1 |
> | project_management | 2 |
> | 其他（含 USDPT 9 筆、deficiency 補件等） | 約 45 |
>
> 全清單見 `01_sources/source_registry.csv`，含每筆 local path / SHA-256 / status。

**Speaker notes**

This slide is for the technically-minded audience member who wants to know
the raw inventory. Optional unless explicitly asked.

中文 delivery prompt: 視時間決定要不要展開；如不展開，跳過即可。

**Source claims**: 全 registry
**Key figures**: KF_033 (130 sources)

# Speaker checklist before the session

當天上場前 8 點檢查清單：

1. 是否要在 Slide 1 加入個人 / 機構抬頭？
2. Slide 17、Slide 31、Slide 32、Slide 38、Slide 44 五張為視覺重點，請確認設計版本而非 markdown 表格直接貼上。
3. Slide 18 並列圓餅圖需確認 USDC 比例來源（產生自 CLAIM_026 transparency 報告，可在備考用）。
4. Slide 14（DAI/USDS）與 Slide 15（USDe）建議自行畫流程圖；目前 `06_flow_diagrams/` 內未含此兩張。
5. Slide 38 之 USDPT 四層 swim-lane 已重畫於 `06_flow_diagrams/usdpt_settlement_flow.md`，可直接 Mermaid 渲染或重繪。
6. 若時間 < 60 分鐘，建議砍 Slide 12（RLUSD）、Slide 36（Taiwan）、Slide 42、Slide 43（market data）、Slide 44/45（failure cases）；保留 Part 0、Part 3、Part 8。
7. 若時間 > 90 分鐘，可在 Slide 33–35 加入 Q&A 中段。
8. 附錄 A1–A3 視 audience 興趣決定要不要打開。

# End of script
