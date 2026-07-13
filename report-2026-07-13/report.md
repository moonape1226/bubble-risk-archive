# 2026-07-13 市場泡沫風險評估報告
> 報告日期：2026-07-13；執行日：2026-07-13 Asia/Taipei；ISO 週次：2026-W29；前次基準：report-2026-07-09（4天前）

**總評**：總分 64【警戒】（Δ 0）；扳機狀態：已擊發；最貼近錨點：1997 早期建設（50%）。

## §1 六維度風險條圖
| 維度 | 條圖 | 本次 | 前次 | Δ |
|---|---|---:|---:|---:|
| 估值溢價 | ▰▰▰▰▰▰▰▱▱▱ | 79 | 79 | 0 |
| 市場廣度 | ▰▰▰▱▱▱▱▱▱▱ | 30 | 30 | 0 |
| 投機行為 | ▰▰▰▰▰▱▱▱▱▱ | 58 | 58 | 0 |
| 散戶情緒 | ▰▰▰▰▰▱▱▱▱▱ | 51 | 50 | +1 |
| 貨幣與信貸環境 | ▰▰▰▰▰▰▰▱▱▱ | 75 | 75 | 0 |
| 結構性槓桿 | ▰▰▰▰▰▰▰▱▱▱ | 77 | 77 | 0 |
| **加權總分** | ▰▰▰▰▰▰▱▱▱▱ | **64【警戒】** | 64 | 0 |

## §2 歷史錨點相似度
| 錨點 | 相似度 | 條圖 | 標記 |
|---|---:|---|---|
| 1997 早期建設 | 50% | ▰▰▰▰▰▱▱▱▱▱ | ◀ 最貼近 |
| 1998 LTCM 衝擊 | 40% | ▰▰▰▰▱▱▱▱▱▱ |  |
| 1999 晚期狂熱 | 30% | ▰▰▰▱▱▱▱▱▱▱ |  |
| 2000/3 頂點 | 25% | ▰▰▱▱▱▱▱▱▱▱ |  |
| 2021/12 Meme 頂 | 50% | ▰▰▰▰▰▱▱▱▱▱ |  |

## §3 三角訊號
| 指標 | 本次數值 | vs 前次 |
|---|---|---|
| S&P 500 | 7,575.39 | 持平 +0.42%（前次 ≈7,543.64） |
| WTI 原油 | $69.6 /bbl | 持平（無新觀測，前次 ≈$69.6） |
| 10Y Treasury | 4.54% | 持平（無新觀測，前次 4.54%） |

**三者狀態**：穩定共存——三者本次方向皆為「持平」（S&P +0.42% 低於 0.5% 門檻；WTI、10Y 皆 `no_new_obs`），未見同向拉伸，S&P `dev200_pct` ≈+8.76%（< +10%）。

- 股市：S&P 500 ≈7,575.39（2026-07-10 收），較前次 +0.42%（門檻內＝持平），距 200 日均線 +8.76%、距 52 週均線 +10.53%——價格延伸偏高但非急拉。
- WTI 原油：≈$69.6/bbl（2026-07-06，無新觀測），與前次持平。
- 10Y 殖利率：4.54%（2026-07-09，無新觀測），本次無新觀測、名目零變動；breakeven 微升 +1 bp 為唯一非零項。

**格局轉變**：前次格局＝穩定共存（讀自 report-2026-07-09 的 `regime`）→ 本次格局＝穩定共存，格局未轉變。

**10Y 成因拆解**（`ΔDGS10 ≈ ΔDFII10 + ΔT10YIE`，拆的是週變動、非水位）：
- ΔDFII10 實質殖利率週變動：≈0 bps（無新觀測，2026-07-09）
- ΔT10YIE 損益平衡通膨週變動：≈+1 bp（2026-07-10，微升）
- 判定：無變動（無新觀測）——10Y 名目本次無新觀測（Δ 0 bps，`decomposition.driver` 記 breakeven 僅反映 breakeven 端 +1 bp 的微動，不改整體無變動結論）。

**扳機鏈**：
- **A 通膨鏈：油 → 通膨預期 → Fed 受限 → refinancing 成本**——此鏈維持「受限」狀態但本週未再加速。油價持平（WTI ≈$69.6，無新觀測），通膨端仍偏高：CPI YoY **4.17%**（`CPIAUCSL`，2026-05 資料月）、5y5y forward **2.20%**（`T5YIFR`，2026-07-10，週 Δ +2 bps）皆未回落。Fed 受限環節本週明顯強化：CME FedWatch 在 2026-07-08 六月會議紀要＋CPI 後由「近全數持平」重定價為 7/29 會議 ≈70% 持平／≈25% 升息／≈0% 降息，年底路徑漂向 ≈4%——Fed put 可得性下降（降息門檻升高），屬扳機側。無當期電價／能源瓶頸新報導，AI 資料中心電力通膨外溢本週不作額外輸入。
- **B 槓桿鏈：衝擊（典型：財政風險再定價）→ NBFI 去槓桿 → margin spiral → 國債市場失序 → 官方市場功能回應**——本鏈**乾柴堆積但未點火**。衝擊節點：10Y 期限溢價 `THREEFYTP10` ≈0.73%（2026-07-02，序列自身 trailing ≈7d +3.3 bps，溫和）、美債標售需求穩健（7/8 10Y 標售 bid-to-cover 2.59；7/9 30Y 小幅 stop-through、需求偏firm），財政再定價壓力溫和、未急升。NBFI 節點：CFTC 槓桿基金美債期貨淨空倉仍處報導的 ≈$1T 紀錄區（script `cftc_lev_funds` 本次 `fetch_failed`，值來自 WebSearch），MOVE ≈68.89（2026-07-10，較前次 ≈65.76 微升、仍屬低波），無基差／swap-spread 平倉報導。官方回應節點：`repo_stress` 顯示 SOFR−IORB −12 bps、SOFR99−IORB 0 bps、SRF 動用 0，無 funding 壓力、無市場功能干預。real-rate 主導的異常 10Y 上行本週不存在（10Y 無新觀測）。本鏈證據 best-effort，本週無基差交易槓桿的新積累／釋放事件。

**結論**：⚠ **扳機狀態：已擊發**——判定命中「私募信貸 gate proration / breach」：Q2 2026 多檔非交易 BDC／私募信貸區間基金實際觸及贖回上限並依比例撥付（BCRED 首度執行 5% gate proration、Apollo ADS 16.8% 撥付、Blue Owl OCIC/OTIC 合計 $4.7B 撥付，詳 §D5／本次新增訊號），此為 1998 LTCM 型「融資扳機」特徵：非銀信用先於公開 mark-to-market 利差（HY/IG OAS 仍史窄）出現一階壓力。與 D5 rationale「扳機側」一致。三者配置的歷史意義：估值＋槓桿＝崩跌位能，融資緊縮＝時點扳機；本週公開利差自滿（HY 2.7%／IG 0.76%）與非銀融資扳機並存，屬「自滿側 froth 與扳機側 financing 壓力同框」的高風險配置，但三角資產本身未同向偏高（穩定共存）、槓桿鏈 B 尚未點火，故失序尚屬局部（結構化產品閘門）而非國債市場層級。

## 六維度評分

### 1. 估值溢價 — 79（weight 22%，Δ 0）

- **S&P 500 trailing P/E** ≈**32.60**（2026-07-10，multpl.com/s-p-500-pe-ratio）——較前次 32.18 微升，近歷史高位。
- **Shiller CAPE** ≈**42.18**（2026-07-10，multpl.com/shiller-pe；GuruFocus 交叉檢核 41.76 @2026-07-01）——較前次 41.64 微升，逼近歷史高（≈44）。
- **Excess CAPE Yield（ECY）** ≈**0.06%**（`1/42.18 − 2.31/100`，derived 自 CAPE 與 DFII10 2.31%）——接近 0，屬 1929／2000 級別的股相對債極貴訊號（confirmation，不主計分）。
- **Mag 7 加權 P/E** trailing ≈**40**、forward ≈**28**（MarketXLS／Yardeni，2026 年中）——絕對高，但對 S&P 溢價為近十年最窄（相對自身歷史反而 de-rate）。
- **價格趨勢偏離（Farrell #1/#2/#4）** S&P 距 200 日均線 **+8.76%**、距 52 週均線 **+10.53%**（`sp500_trend`，2026-07-10）——價格延伸偏高但未達急拉，與 P/E/CAPE 互補、不重複計分。
- **AI capex 現實檢核**：hyperscaler FY2026 capex 指引合計 ≈**$725B（+77% YoY）仍在上修**（Meta 上調至 $125–145B；MSFT/GOOGL/AMZN 維持高檔，最近季 stock-of-state）——基本面敘事仍撐估值。
- **AI compute 供需現實檢核**：GPU 現貨租金軟（H100 ≈$1.87–2.99/hr，較 2024 峰 −64–75%）但一年期合約價反升 ≈+40%、on-demand「售罄」；伺服器 DRAM 3Q26 合約 +13–18% QoQ（TrendForce 2026-07-09，較 1Q26 +81% 明顯減速）；美國 2026 資料中心約半數延後／取消、瓶頸轉為電力／電網——供給仍被合約與 token 需求吸收但邊際鬆動，屬缺口尚未成形、非惡化確認。
- **AI 營收對 capex 缺口現實檢核**：分母年化 capex ≈$725B（分子：top-4＋Oracle）vs 分子已披露 AI 終端年化營收——Anthropic ≈$47B run-rate（2026-05 自陳）、OpenAI ≈$24–25B、MSFT AI 業務 >$37B run-rate（FQ3 FY26）——量級缺口仍大且 capex 指引續升，回本假設後移，屬估值風險上修的質化依據（缺口未收斂）。
- **Hyperscaler financing-mix 現實檢核**：capex 已超過部分廠商 FCF、發債佔比上升（Amazon 7 月 $25B 發債、Nvidia 6/15 $25B IG 債；見 D6）——同一份 guidance 的脆弱性上升（confirmation，不主計分）。
- **AI 信用定價分歧（equity-vs-credit schism）**：本週分歧方向混合——Oracle 5yr CDS ≈**198 bp**（16 年新高、走闊）為後期訊號側；CoreWeave 5yr CDS 反壓縮至 ≈**452 bp**（自去年 881 bp／前次 ≈665 bp 大幅收斂，信用回穩）為分歧未解側。整體仍屬「兩個市場只有一個是對的」（confirmation，不主計分；缺 AI BBB+ CDS vs CDX IG 淨差，該項 ✗ NOT DISCLOSED）。
- **折舊年限變動（盈餘品質）**：過去 30 日無新 10-K/10-Q 折舊年限或殘值假設變更披露（財報季未啟）（✗ NOT DISCLOSED；缺值不調分）。
- **backlog 重複計算風險（RPO double-counting）**：Oracle RPO ≈**$638B（+363% YoY）、>50% 來自 OpenAI**；OpenAI 對外承諾總額估 >$1T 被 Oracle／Broadcom／Microsoft／Nvidia 等多方分別計入——同一終端現金流僅一份卻支撐多家 backlog，屬營收品質訊號（confirmation，不主計分）。
- **TP-upgrade phase signal**：過去 14 日具名升評 Morgan Stanley NVDA 重申 Buy／TP $288（2026-07-10，EPS vs multiple 分解未披露）、Morgan Stanley TSMC 上調 5%／NT$2,088（明示 EPS-driven，上修 EPS 估值 +7–8%）——本期主導槓桿偏 EPS 側、非跨多檔的 multiple re-rating（TP 分解 best-effort，多數銀行未披露分解，✗ NOT DISCLOSED）。
- **結論**：分數維持 **79**（rubric 高位）。P/E/CAPE 微升、ECY 近 0、Mag7 高檔、趨勢偏離 +8.76% 與 capex 續升的敘事撐盤同框；供需邊際鬆動與缺口未收斂尚未轉為 guidance 下修，故較前次持平不降。

### 2. 市場廣度 — 30（weight 13%，Δ 0）

- **RSP（等權）vs SPY（市值權）YTD**：RSP ≈+9.7–10.7% vs SPY ≈+7.5–8.4%（2026 年中，24/7 Wall St./Yahoo Finance）——**等權領先市值權 ≈+2–3 pp**，廣度為「轉寬／健康」方向，非背離。
- **Top-10 集中度**：≈**36.40%**（2026-07-02，SPDR 持股經 P&I）——絕對偏高（NVDA ≈7.0%、AAPL ≈6.3%、MSFT ≈4.6%），但未再創高。
- **Advance/Decline 與新高/新低**：NYSE A/D 線於 2026 年 7 月同步創 12 個月新高、確認指數新高（StockCharts/Leuthold，質化）——廣度確認、健康；精確每日 A/D 比與 NH/NL 數位於動態儀表板，本次未取得數值（質化確認）。
- **結論**：分數維持 **30**（rubric 0–20/21–40 交界偏健康）。等權領先＋A/D 線確認新高＝廣度健康／轉寬，唯 Top-10 集中度 ≈36% 仍偏高構成殘餘風險；淨評與前次持平。

### 3. 投機行為 — 58（weight 18%，Δ 0）

- **+AI 改名／SPAC**：本週出現 **1 件**具名 +AI 改名——Envirotech Vehicles（EVTV）2026-07-10 更名 **Azio AI Holdings**、2026-07-13 起以 **AZIO** 交易，由 EV 廠轉定位「AI 資料中心／GPU 算力」平台，並搭 7/9 一紙 $27.9M（可擴至 $100M）AI 基礎設施協議（Business Wire 2026-07-10）——典型 EV 空殼轉 AI 敘事＋改名。無新 SPAC／空殼熱潮。
- **Microcap thematic moonshots**：本週 **0 件**合格（<$1B 市值、單日 ≥100%、堆疊 2+ 熱主題＋弱基本面）——✓ SEARCH-VERIFIED（0 件）；QUBT／D-Wave 等量子小型股僅屬觀察名單、無單日翻倍。
- **IPO 熱度**：2026 YTD ≈83 檔、6 月最忙（19 檔）、截至 5/31 募資 $34.2B（+163.9% YoY）；本週檔期含 Tailored Brands（≈$500M 申報）等，市場活躍但秩序尚可，未見無營收 IPO 暴衝（first-day pop／無營收佔比本次未取得精確值）。
- **Insider selling clusters**：required 螢幕已執行；二手彙整（LevelFields）指 7 月首週 IT 類股內部人賣出 ≈$110M（含 Workday／Arista／CrowdStrike），但 **SEC EDGAR Form 4 一手確認本次無法完成**（EDGAR 主機遭本執行環境 egress 政策封鎖），依「具名 insider 需 Form 4 URL」約束，本次不計入任何具名一手申報＝**0 件合格 Form 4 cluster**（✓ SEARCH-VERIFIED（0 件合格）；二手彙整僅列背景、不計分）。
- **OpenAI / Anthropic 營收軌跡（集中度風險）**：Anthropic ≈$47B、OpenAI ≈$24–25B run-rate（見 D1）——AI 需求高度集中於少數終端。
- **大型 IPO pipeline（流動性抽離風險）**：SpaceX（含 xAI）confidential S-1 2026-04-01、Anthropic draft S-1 2026-06-01、OpenAI confidential S-1 2026-06-09（皆 >30 日窗、作背景不作本週事件）——巨型上市抽水潛在壓力仍在。
- **Cboe equity-only put/call**：≈**0.55–0.57**（2026-07-09/07-10）——未破 0.50，但屬 call 偏重／自滿區（confirmation，不主計分）。
- **結論**：分數維持 **58**（rubric 41–60「投機升溫」）。1 件 +AI 改名（AZIO）為孤立新事件，moonshot 仍 0、insider 一手未確認、put/call 自滿未極端、IPO 活躍但秩序尚可——投機體感整體與前次持平，不足以推升一個等級。

### 4. 散戶情緒 — 51（weight 12%，Δ +1）

- **CNN Fear & Greed**：≈**48「Neutral」**（2026-07-10，經 MacroMicro/Benzinga 鏡像；cnn.com 直抓 403）——較前次 43「Fear」回升 5 點、脫離恐懼區。
- **Margin Debt**：**$1.42T、YoY +53.7%、MoM +8.5%（2026-05，記錄高）**（FINRA 經 Advisor Perspectives，報告 2026-06-24）——月頻 stock-of-state，6 月數尚未發布、沿用 5 月；YoY +53.7% 屬 1999／2007／2021 頂部級別警訊。
- **AAII 散戶調查**：**Bull 36.3%／Bear 37.2%／Neutral 26.5%**（2026-07-10）——較前次（07-02：Bull 31.4%／Bear 42.3%）多方 +4.9pp、空方 −5.1pp，空頭氣氛明顯收斂。
- **家庭持股佔金融資產比**：**45.76%**（`BOGZ1FL153064486Q`，2026-Q1 資料日 2026-01-01）——歷史高位、後續加碼空間有限（Farrell #5，季頻沿用、不計週 Δ）。
- **社交情緒代理**：Wendy's（WEN）迷因軋空活躍（放空比 ≈82% 流通股、WSB「Save Wendy's」貼文 >2.3 萬讚、6 月底單日 +24–42%，7/9 收 $7.59）——散戶投機脈動存在但屬單一低流通標的（即時 WSB mention 排行 403，具名為代表性、非確認排行）。
- **NAAIM Exposure Index**：**82.95**（2026-07-08，較 07-01 的 84.69 微降）——主動經理人仍高曝險＝擁擠多頭（Farrell #9，confirmation cross-check，不主計分）。
- **結論**：分數升至 **51**（Δ +1，rubric 41–60 下緣）。F&G 由 Fear 回升至 Neutral、AAII 空頭收斂＋迷因脈動（WEN）＝散戶情緒邊際回溫；但 F&G 仍「Neutral」非「Greed」、margin debt 沿用未創新，故僅微升 1 分。

### 5. 貨幣與信貸環境 — 75（weight 20%，Δ 0；扳機側）

- **Fed funds rate**：目標區間 **3.50–3.75%**（`DFEDTARU` 3.75%／`DFEDTARL` 3.50%，2026-07-12，無變動）。
- **市場隱含路徑（CME FedWatch，best-effort）**：2026-07-08 讀數——7/29 會議 ≈70% 持平／≈25% 升息／≈0% 降息，年底路徑漂向 ≈4%；六月紀要＋CPI 後由「近全數持平」轉為「持平但升息風險上升」——Fed 寬鬆空間受壓（扳機側證據；缺 07-13 當日快照不調分）。
- **Realized inflation vs expectations**：CPI YoY **4.17%**（`CPIAUCSL`，2026-05）高檔、5y5y forward **2.20%**（`T5YIFR`，2026-07-10，+2 bps）未回落——通膨仍壓縮 Fed 寬鬆空間，屬扳機側。
- **10Y 期限溢價（term premium）**：`THREEFYTP10` **0.7322%**（2026-07-02，Kim-Wright 三因子模型，序列自身 trailing ≈7d +3.3 bps）——財政風險再定價溫和上行、未急升。
- **repo 資金壓力（SOFR−IORB）與 SRF 動用**：`repo_stress`——SOFR−IORB **−12 bps**、SOFR99−IORB **0 bps**、SRF 動用 **$0bn**（as_of 2026-07-09）——secured-funding 無壓力、無官方流動性 backstop 動用（例行性動用亦無）。
- **美債標售需求（auction，best-effort）**：7/8 10Y 標售 bid-to-cover **2.59**（穩健）、7/9 30Y 小幅 stop-through（3 月來首見、需求偏 firm）——無 tail、財政供給壓力事件本週不成立（confirmation；缺值不調分）。
- **HY OAS**：**2.70%**（`BAMLH0A0HYM2`，2026-07-09，週 Δ 0 bps／無新觀測）——接近循環低、極窄、自滿側訊號。
- **IG OAS**：**0.76%**（`BAMLC0A0CM`，2026-07-09，無新觀測）——史窄、信用自滿。
- **10Y nominal 週變動拆解**：ΔDGS10 ≈0 bps（無新觀測）＝ΔDFII10 ≈0 bps ＋ ΔT10YIE ≈+1 bp；本週無殖利率淨變動，估值折現／再融資壓力無新增（詳 §3）。
- **Fed balance sheet**：`WALCL` **$6.74T**（6,735,609 百萬美元，2026-07-08，無新觀測）——量化緊縮步調持平。
- **全球央行流動性交叉檢核**：ECB `ECBASSETSW` **€5.98T**（5,983,015 百萬歐元，2026-07-03）、BOJ `JPNASSETS` **¥639.55T**（6,395,509 億日圓，2026-06-01）皆持平；PBoC 本期無當期英文彙整（✗ NOT DISCLOSED，best-effort，不調分）——全球流動性持平、未見氾濫式擴張。
- **私募信貸贖回壓力（扳機側，event-driven）**：Q2 2026 多檔非交易 BDC／私募信貸區間基金**實際觸及 5% 季度贖回上限並比例撥付（gate proration）**——BCRED 首度執行 5% gate（贖回需求 ≈10% NAV／≈$4.5B，2026-06-04 披露，且撤除 Q1 的上限上調 backstop）、Apollo ADS 16.8%／≈$2.4B（2026-06-22，撥付約 45%）、Blue Owl OCIC 18.8%＋OTIC 38.1% 合計 $4.7B（2026-07-02，維持 5% cap 撥付）。多基金 redemption 上限實際觸發＝financing-cycle 緊縮已抵達非銀信用，餵入 §3 融資扳機。Apollo（6/22）、Blue Owl（7/2）落在 30 日窗內；此為前次已存在之扳機側狀態延續、非本次新披露。
- **結論**：分數維持 **75**（雙向計分／**扳機側**）。私募信貸多基金 gate proration 持續＋FedWatch 轉向升息風險（Fed put 可得性下降）為扳機側；同時 HY 2.70%／IG 0.76% 史窄自滿——「自滿側 froth 與扳機側 financing 壓力同框」推高分數。macro 全數持平（多序列 `no_new_obs`）、國債標售穩健、repo 無壓，故分數較前次持平；扳機側質變見「本次新增訊號」。

### 6. 結構性槓桿 — 77（weight 15%，Δ 0）

- **US 槓桿 ETF AUM**：TQQQ ≈$29–37B、SOXL ≈$14B、NVDL ≈$4B；TQQQ＋SOXL 2026 YTD 淨流出合計 ≈$14B（漲勢中仍流出）；美國槓桿 ETF 總 AUM ≈$198–213B（記錄高）（etf.com／cryptobriefing／GraniteShares）——水位高但邊際淨流出。
- **US 單一股票槓桿 ETF 核准／發行（近 30 日）**：**大量**——SK Hynix ADR（SKHY）7/10 when-issued、7/13 正式交易觸發 2x 產品潮：ProShares SKHU（2x，預定 7/13）、Leverage Shares SKHX／Direxion SKHL 在途；Tradr 5 檔 2x long（CIEN/QNT/RMBS/TSEM/TTMI，7/1）＋2x short（AAOI/ORCL，預定 7/15）；Leverage Shares 6 檔（GOOGL/AMZN/META/AAPL，7/7 上線）——美國單股槓桿產品擴散顯著。
- **全球（非美）槓桿產品核准（本週）**：**本週擴散訊號未觸發**——韓／台／日／歐本週無新單股槓桿／反向 ETF 核准（✗ NOT DISCLOSED）。背景：韓國 4 月已核准之單股槓桿 ETF 正遭國會 7/6 檢討（負面監管、非新核准）；台灣僅提高基金個股上限 10%→25%（非單股槓桿 ETF）；SK Hynix 2x 產品為**美國掛牌**、不計非美核准。**未達 2+ 非美市場同週核准**，rubric floor 81 未啟動。
- **0DTE 佔 SPX 期權量**：≈**61–63%**（Cboe，2Q26 ADV 3.1M 紀錄／6 月 ADV 3.3M 紀錄；「61% share」貼文）——持續 >60%，高檔。
- **Options 總量（OCC 月報）**：6 月 **16.03 億口、+45.0% YoY**（OCC，報告 2026-07-02，記錄）——衍生品投機量創高。
- **跨資產／相關性確認**：VIX 期限結構 contango（VIX1D 11.61 → VIX3M 19.00）、Cboe SKEW ≈**149.6**（偏高、避險付溢價）、3 個月隱含相關 COR3M ≈7.81（近循環低、分散化）（Saxo，2026-07-01 快照，較執行日 ≈1–2 週）——尾端避險升溫但整體波動平靜（confirmation）。
- **Margin debt / 市值 交叉檢核**：$1.42T、YoY +53.7%（見 D4）——確認零售槓桿處頂部級別（confirmation，不在此重複計分）。
- **AI 基礎設施債務融資／vendor-financing loops**：本月持續擴張——Amazon 7 月 **$25B** 發債（AI/資料中心 capex）、QTS ≈$2B 中旬定價、AI 相關高收益債 YTD 至 7/8 已吸收 ≈$31.9B；Nvidia revenue-share／backstop AI 雲 ≈7/4 上線（210k GPU，vendor-finance/循環流風險）；背景：Nvidia 6/15 $25B IG 債（7 tranche、$85B 訂單，資助其對 OpenAI/Anthropic/Intel 承諾）、Oracle/xAI/Meta/CoreWeave 表外 SPV ≈$120B。collateral-light 循環網續增（惟 CoreWeave 信用本週反回穩、CDS 收斂，見 D1）。
- **銀行對 NBFI 放款**：`LNFACBW027SBOG` **$2.00T**（1,995.08 億美元→兆換算，2026-07-01，週 Δ 0/無新觀測）——bank–NBFI linkage 水位持平（confirmation，不主計分）。
- **美債基差交易槓桿（best-effort）**：script `cftc_lev_funds`／`move_index`／`ofr_repo` 本次 `fetch_failed`，改走 WebSearch——CFTC 槓桿基金美債期貨淨空倉仍處 ≈$1T 紀錄區（精確當週值未鎖定）、MOVE ≈68.89（2026-07-10，較前次 65.76 微升、仍低波），無基差／swap-spread 失序平倉報導——乾柴高位但未點火（見 §3 槓桿鏈 B）。
- **結論**：分數維持 **77**（rubric 61–80）。0DTE 續 >60%、OCC 量創高、US 單股槓桿產品擴散強、AI 基礎設施循環債續增（Amazon $25B 新發、Nvidia revenue-share）＝結構性槓桿高檔；惟全球擴散訊號未觸發（無 floor-81）、MOVE 仍低波、無失序平倉，CoreWeave 信用反回穩——淨評與前次持平。

## 綜合分數

| 維度 | 分數 | 權重 | 加權 |
|---|---:|---:|---:|
| 估值溢價 | 79 | 22% | 17.38 |
| 市場廣度 | 30 | 13% | 3.90 |
| 投機行為 | 58 | 18% | 10.44 |
| 散戶情緒 | 51 | 12% | 6.12 |
| 貨幣與信貸環境 | 75 | 20% | 15.00 |
| 結構性槓桿 | 77 | 15% | 11.55 |
| **加權總分** | | **100%** | **64.39 → 64** |

加權總分 = Σ(分數 × 權重)/100 = 64.39，half-up 四捨五入 → **64**；對照 tier 表（40–64＝警戒）→ **警戒**。

邊界帶：總分 64 距 警戒/高 邊界 ≤ 2 分，評分固有噪音約 ±2–3，等級判讀需保留餘地。

## 歷史泡沫週期對比

相似度計算：checklist v2

逐項對本次六維度分數與已抓取數據判定命中；相似度 = 命中數 ÷ 特徵數 × 100，四捨五入到最近 5%。無資料特徵記未命中。

**最貼近＝1997 早期建設（4/8 命中，50%）** 全項明細：
- ①估值溢價 40–74：✗（79 > 74）
- ②市場廣度 < 45：✓（30）
- ③投機行為 < 50：✗（58）
- ④hyperscaler capex 指引仍上修：✓（FY26 ≈$725B 續升）
- ⑤散戶情緒 < 55：✓（51）
- ⑥結構性槓桿 < 50：✗（77）
- ⑦HY OAS < 4% 且本次未走闊：✓（2.70%、週 Δ 0）
- ⑧扳機狀態＝未擊發：✗（已擊發）

其餘錨點摘要（關鍵差異項）：
- **2021/12 Meme 頂（4/8，50%，與 1997 同分，依表列順序 1997 在前取最貼近）**：命中 ②社群投機熱（WEN）、③結構性槓桿 ≥65（77）、⑤margin debt YoY ≥+40%（+53.7%）、⑧CPI YoY ≥4% 且 Fed 未實質緊縮（4.17%）；未命中散戶 ≥65（51）、moonshot（0）、廣度 ≥50（30）、流動性氾濫（央行持平＋D5 扳機側非自滿側）。
- **1998 LTCM 衝擊（3/8，40%）**：命中 ③具名非銀／槓桿壓力披露（私募信貸 gate）、⑤估值 ≥60（79）、⑥扳機狀態 ≥初啟（已擊發）；未命中 HY 週 Δ≥+30bps／VIX>25、S&P 回檔 ≥5%、Fed 轉鴿（反轉為鷹）、廣度 Δ≥+8、ΔT10YIE ≤0（+1 bp）。
- **1999 晚期狂熱（3/10，30%）**：命中 估值 ≥75（79）、CAPE ≥38（42.18）、結構性槓桿 ≥60（77）；未命中投機 ≥60、moonshot／無營收 IPO、廣度 ≥45、D5 自滿側＋HY<3.5%（D5 屬扳機側）、散戶 ≥55、30 日內具名巨型 S-1、扳機＝未擊發。
- **2000/3 頂點（2/8，25%）**：命中 扳機狀態 ≥初啟（已擊發）、貨幣轉緊（FedWatch 升息風險升）；未命中估值 ≥85、廣度 ≥60、dev200 自 >+10% 回落／回檔 ≥5%、投機 ≥70、insider 合格 cluster、散戶 ≥65。

**兩句解讀**：本週配置最貼近「1997 早期建設」與「2021/12 Meme 頂」兩極並列（各 50%）——一端是估值高／廣度健康／capex 續升的「早期建設」骨架，另一端是 margin debt YoY +53.7%、0DTE >60%、AI 循環槓桿、迷因脈動的「晚期槓桿狂熱」特徵，唯獨已出現非銀信用融資扳機（已擊發）將其推離純 1997。這意味當前處「早期建設敘事仍在、但槓桿與融資壓力已具晚期特徵」的混合位置——真實技術突破吸引超過商業回報所能支撐的資本（BIS AER 2026 Ch I：AI 相關投資 ≈1% of US GDP、IT 投資合計 ≈5% 已超 dot-com 峰），最須盯的是 AI 信用重定價（Oracle CDS 走闊）與私募信貸閘門是否外溢至公開利差。長期指數成長趨勢偏離（Dot-com ≈95%、1929 ≈110%、當前 AI 週期 ≈147%；RIA/Farrell）作跨期敘事錨、不進 checklist。

## 機構情緒對照

本次無新機構調查數據。（BofA Fund Manager Survey 與 JPM 機構調查為月頻，自前次 2026-07-09 運行以來無新一期發布。）

另補 weekly contrarian 交叉檢核：**NAAIM Exposure Index 82.95**（2026-07-08，較 07-01 的 84.69 微降）——主動經理人仍處高曝險、擁擠多頭（Farrell #9）；NAAIM 於 D4 作 confirmation 計分、此處僅敘述，不改「本次無新機構調查數據」判定。

## 本次新增訊號

比較基準：vs 前次（4天前，report-2026-07-09）。

- **散戶情緒 +1（50 → 51）**：CNN F&G 由 43「Fear」回升至 48「Neutral」（07-10）、AAII 空方由 42.3% 收斂至 37.2%／多方升至 36.3%（07-10）、WEN 迷因軋空脈動——散戶情緒邊際回溫，唯 margin debt 沿用 5 月（+53.7% YoY）、F&G 未進 Greed，故僅 +1。
- **貨幣與信貸環境（D5）＝扳機側，score Δ 0——質化新訊號（雙向 Δ 遮蔽防護）**：私募信貸多基金 gate proration 持續（BCRED 首度執行 5% gate／Apollo ADS 16.8% 撥付／Blue Owl 合計 $4.7B 撥付，Q2 2026），且 CME FedWatch（07-08）由「近全數持平」重定價為「持平＋≈25% 升息風險、≈0% 降息」——Fed put 可得性下降。分數未動因先前已因扳機側偏高（前次即 75／扳機側）；扳機狀態延續「已擊發」。此為前次已存在之扳機側狀態延續，非本次首度披露。
- **投機行為質化訊號（score Δ 0）**：本週新增 1 件 +AI 改名（EVTV → **AZIO**，7/13 起交易，EV 空殼轉「AI 資料中心」敘事）——孤立事件，未改維度分數；moonshot 仍 0、insider 一手 Form 4 未能確認（EDGAR 遭封鎖）。
- **結構性槓桿質化訊號（score Δ 0）**：US 單股槓桿 ETF 擴散顯著（SK Hynix SKHU/SKHX/SKHL、Tradr AAOI/ORCL 2x short、Leverage Shares GOOGL/AMZN/META/AAPL）、AI 基礎設施新債（Amazon $25B、QTS ≈$2B）、Nvidia revenue-share 循環流——惟**全球（非美）擴散訊號未觸發（本週擴散訊號未觸發，未達 2+ 非美市場同週核准）**，MOVE 仍低波、無失序平倉，故分數未動。
- 其餘維度（估值 79、廣度 30、投機 58、貨幣 75、結構 77）分數與前次持平。格局：穩定共存 → 穩定共存（未轉變）。

## 數據附錄

**Coverage table（每個 `# Data sources` bullet 一列，共 57 列）**

| 維度 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|
| 估值｜S&P 500 P/E＋Shiller CAPE | multpl.com [primary: SEARCH] | ✓ SEARCH-VERIFIED（P/E 32.60、CAPE 42.18 @07-10；GuruFocus CAPE 交叉檢核） |
| 估值｜Mag 7 加權 P/E、AI leader P/S | MarketXLS／Yardeni [SEARCH] | ✓ SEARCH-VERIFIED（trailing ≈40／forward ≈28） |
| 估值｜Analyst TP upgrade decomposition | 賣方研報 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（MS NVDA $288、MS TSMC EPS-driven；多數銀行分解未披露 → 部分 ✗ NOT DISCLOSED） |
| 估值｜S&P 200-DMA/52週MA 趨勢偏離 | `scripts/fetch_macro.py` `sp500_trend`（FRED SP500 派生） | ✓ API（dev200 +8.76%／dev52w +10.53%） |
| 估值｜AI 信用定價分歧（equity-vs-credit schism） | 信用市場 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（Oracle CDS ≈198bp、CoreWeave ≈452bp；BBB+ vs CDX 淨差 ✗ NOT DISCLOSED） |
| 廣度｜RSP vs SPY YTD 背離 | 24/7 Wall St./Yahoo [SEARCH] | ✓ SEARCH-VERIFIED（RSP ≈+9.7–10.7% vs SPY ≈+7.5–8.4%） |
| 廣度｜Top-10 集中度 | slickcharts／SPDR 持股 [SEARCH]（slickcharts 403） | ✓ SEARCH-VERIFIED（36.40% @07-02） |
| 廣度｜A/D、新高/新低 | StockCharts/Leuthold [SEARCH] | ✓ SEARCH-VERIFIED（A/D 線 12M 新高、確認；精確比質化） |
| 散戶｜CNN Fear & Greed | cnn.com [primary: SEARCH]（cnn 403，經 MacroMicro/Benzinga） | ✓ SEARCH-VERIFIED（48 Neutral @07-10） |
| 散戶｜Margin Debt（水位＋YoY＋/市值） | FINRA/Advisor Perspectives [SEARCH]（月頻 stock-of-state） | ✓ SEARCH-VERIFIED（$1.42T、+53.7% YoY、2026-05；沿用） |
| 散戶｜AAII 投資人情緒 | aaii.com [primary: SEARCH] | ✓ SEARCH-VERIFIED（Bull 36.3%/Bear 37.2% @07-10） |
| 散戶｜社交情緒代理（Reddit/X） | WSB/cashtag [SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（WEN 軋空；即時排行 403、列背景） |
| 散戶｜家庭持股佔金融資產比 | `fetch_macro.py` `BOGZ1FL153064486Q` | ✓ API（45.76% @2026-Q1） |
| 散戶｜NAAIM Exposure Index | naaim/ycharts [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（82.95 @07-08） |
| 機構｜BofA FMS＋JPM 機構調查 | 賣方調查 [SEARCH]（月頻，best-effort） | ✗ NOT DISCLOSED（自前次無新一期） |
| 貨幣｜Fed funds rate（DFEDTARU/DFEDTARL） | `fetch_macro.py` FRED API | ✓ API（3.75%/3.50% @07-12） |
| 貨幣｜HY OAS（BAMLH0A0HYM2） | `fetch_macro.py` FRED API | ✓ API（2.70% @07-09，Δ0/no_new_obs） |
| 貨幣｜IG OAS（BAMLC0A0CM） | `fetch_macro.py` FRED API | ✓ API（0.76% @07-09，no_new_obs） |
| 貨幣｜10Y 殖利率（DGS10） | `fetch_macro.py` FRED API | ✓ API（4.54% @07-09，no_new_obs） |
| 貨幣｜10Y 實質殖利率（DFII10） | `fetch_macro.py` FRED API | ✓ API（2.31% @07-09，no_new_obs） |
| 貨幣｜10Y breakeven（T10YIE） | `fetch_macro.py` FRED API | ✓ API（2.24% @07-10，Δ+1bp） |
| 貨幣｜WTI（DCOILWTICO） | `fetch_macro.py` FRED API | ✓ API（$69.6 @07-06，no_new_obs） |
| 貨幣｜CPI YoY（CPIAUCSL） | `fetch_macro.py` FRED API（月頻） | ✓ API（4.17% @2026-05） |
| 貨幣｜5y5y forward（T5YIFR） | `fetch_macro.py` FRED API | ✓ API（2.20% @07-10，+2bps） |
| 貨幣｜10Y 期限溢價（THREEFYTP10） | `fetch_macro.py` FRED API | ✓ API（0.7322% @07-02，+3.3bps） |
| 貨幣｜repo 資金壓力＋SRF（SOFR/SOFR99/IORB/RPONTTLD） | `fetch_macro.py` `repo_stress` | ✓ API（SOFR−IORB −12bps、SRF $0bn @07-09） |
| 貨幣｜美債標售需求（auction） | Reuters/TreasuryDirect [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（10Y BTC 2.59 @07-08；30Y stop-through @07-09） |
| 貨幣｜FedWatch 隱含路徑 | CME/Reuters [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（7/29 ≈70%持平/25%升息 @07-08） |
| 貨幣｜Fed balance sheet（WALCL） | `fetch_macro.py` FRED API | ✓ API（$6.74T @07-08，no_new_obs） |
| 貨幣｜ECB/BOJ 資產負債表（ECBASSETSW/JPNASSETS） | `fetch_macro.py` FRED API | ✓ API（€5.98T @07-03／¥639.55T @06-01） |
| 貨幣｜PBoC aggregate financing | NBS/PBoC [SEARCH]（best-effort） | ✗ NOT DISCLOSED（無當期英文彙整） |
| 貨幣｜私募信貸/非銀基金贖回壓力 | BDC 披露 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（BCRED/Apollo/Blue Owl Q2 gate proration @06-04/06-22/07-02） |
| AI｜Hyperscaler capex 指引 | 季報 [SEARCH]（stock-of-state） | ✓ SEARCH-VERIFIED（FY26 ≈$725B、+77% YoY、續升） |
| AI｜AI token volume 成長 | Anthropic/OpenAI/Google [SEARCH]（best-effort） | ✗ NOT DISCLOSED（本季無量化披露） |
| AI｜OpenAI/Anthropic 年化營收 | The Information/Reuters [SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（Anthropic ≈$47B／OpenAI ≈$24–25B run-rate） |
| AI｜客戶集中度＋backlog 重複計算（RPO） | 財報電話 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（Oracle RPO $638B、>50% OpenAI） |
| AI｜compute 供需/過剩 | SemiAnalysis/TrendForce [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（GPU 現貨 −64–75%／合約 +40%；DRAM +13–18% QoQ；資料中心約半數延後） |
| AI｜Hyperscaler 融資結構（capex vs FCF/發債） | 季報 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（capex 超 FCF、發債佔比升；Amazon $25B/Nvidia $25B） |
| AI｜AI 營收對 capex 缺口 | 組合披露 [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（年化 capex ≈$725B vs 終端營收低十億級；缺口未收斂） |
| AI｜GPU/伺服器折舊年限變動 | 10-K/10-Q [primary: SEARCH]（best-effort，30日事件掃描） | ✗ NOT DISCLOSED（過去 30 日無新變更） |
| AI｜資本週期階段 | 供需增速+進出場事件 [SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（neocloud 續融資、資料中心約半數延後＝晚期 capex） |
| 投機｜+AI rename/SPAC/無營收 IPO 暴衝（7日） | [SEARCH] | ✓ SEARCH-VERIFIED（AZIO 改名 @07-10；無新 SPAC 熱） |
| 投機｜IPO 熱度（count/first-day/無營收佔比） | Renaissance/iposcoop [SEARCH]（Renaissance 403） | ✓ SEARCH-VERIFIED（YTD ≈83 檔；first-day/無營收佔比未取得精確值） |
| 投機｜Microcap thematic moonshots（週） | Finviz/Benzinga [primary: SEARCH]（required 週螢幕） | ✓ SEARCH-VERIFIED（0 件） |
| 投機｜Upcoming AI IPOs（30日具名） | S-1/具名報導 [SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（SpaceX/Anthropic/OpenAI S-1 皆 >30 日，作背景） |
| 投機｜Insider selling Form 4 clusters（14日） | SEC EDGAR [primary: EDGAR]（required） | ✓ SEARCH-VERIFIED（0 件合格 Form 4；EDGAR 遭 egress 封鎖，二手彙整列背景不計分） |
| 投機｜Cboe equity put/call | Cboe/ycharts [primary: SEARCH]（best-effort） | ✓ SEARCH-VERIFIED（0.55–0.57 @07-09/07-10） |
| 結構｜US 槓桿 ETF AUM | etf.com/ETFGI [primary: SEARCH] | ✓ SEARCH-VERIFIED（TQQQ ≈$29–37B/SOXL ≈$14B/NVDL ≈$4B；總 ≈$198–213B） |
| 結構｜US 單股槓桿 ETF 核准/發行 | SEC EDGAR/ETF.com [SEARCH] | ✓ SEARCH-VERIFIED（SK Hynix SKHU/SKHX/SKHL、Tradr、Leverage Shares 多檔 @07-01–07-13） |
| 結構｜全球槓桿產品核准（本週） | KRX/TWSE/JPX/ESMA [SEARCH]（best-effort） | ✗ NOT DISCLOSED（本週擴散訊號未觸發） |
| 結構｜0DTE 佔 SPX 量 | Cboe/SpotGamma [SEARCH]（Cboe 403） | ✓ SEARCH-VERIFIED（≈61–63%，Q2 ADV 紀錄） |
| 結構｜Options 總量（OCC 月報） | theocc.com [SEARCH] | ✓ SEARCH-VERIFIED（6 月 16.03 億口、+45% YoY @07-02） |
| 結構｜VIX 期限/SKEW/股債相關 | Cboe/Saxo [SEARCH] | ✓ SEARCH-VERIFIED（SKEW ≈149.6、VIX contango、COR3M ≈7.81 @07-01） |
| 結構｜margin debt/市值 交叉檢核（BOGZ1FL073164003.Q） | 交叉引用 D4（confirmation） | ✓ SEARCH-VERIFIED（$1.42T/+53.7% YoY，D4 引用，不重複計分） |
| 結構｜AI 基礎設施債務/vendor-financing loops | [primary: SEARCH]（best-effort，30日） | ✓ SEARCH-VERIFIED（Amazon $25B/QTS ≈$2B/AI HY YTD ≈$31.9B/Nvidia revenue-share @07-04） |
| 結構｜銀行對 NBFI 放款（LNFACBW027SBOG） | `fetch_macro.py` FRED API | ✓ API（$2.00T @07-01，no_new_obs） |
| 結構｜美債基差交易槓桿（CFTC/MOVE/repo） | script→WebSearch [primary: script]（best-effort） | ✓ SEARCH-VERIFIED（CFTC 淨空倉 ≈$1T 紀錄區、MOVE ≈68.89 @07-10；script blocks fetch_failed） |

**Raw-data table（計分用具體數據點）**

| 指標 | 數值 | 來源（FRED series ID / URL）| 資料日期 | 抓取 timestamp |
|---|---|---|---|---|
| S&P 500 trailing P/E | 32.60 | multpl.com/s-p-500-pe-ratio | 2026-07-10 | 2026-07-13 09:20 UTC+8 |
| Shiller CAPE | 42.18 | multpl.com/shiller-pe | 2026-07-10 | 2026-07-13 09:20 UTC+8 |
| ECY | 0.06%（derived 1/CAPE − DFII10） | 派生（CAPE 42.18／DFII10 2.31%） | 2026-07-10 | 2026-07-13 09:20 UTC+8 |
| Mag 7 加權 P/E | ≈40 trailing／≈28 forward | MarketXLS/Yardeni | 2026 年中 | 2026-07-13 09:20 UTC+8 |
| S&P dev200 / dev52w | +8.76%／+10.53% | FRED SP500（sp500_trend） | 2026-07-10 | 2026-07-13 09:05 UTC+8 |
| Oracle 5yr CDS | ≈198 bp | Markit 經 ainvest/bondblox | 2026（當期，精確日不可見） | 2026-07-13 09:20 UTC+8 |
| CoreWeave 5yr CDS | ≈452 bp | Yahoo Finance | 2026-06-11 | 2026-07-13 09:20 UTC+8 |
| Hyperscaler FY26 capex 合計 | ≈$725B（+77% YoY） | Tom's Hardware/公司季報 | 2026-Q1 財報 | 2026-07-13 09:20 UTC+8 |
| Anthropic run-rate | ≈$47B | Epoch AI/VentureBeat | 2026-05 | 2026-07-13 09:20 UTC+8 |
| OpenAI run-rate | ≈$24–25B | 公司確認/futuresearch | 2026 | 2026-07-13 09:20 UTC+8 |
| Oracle RPO | $638B（>50% OpenAI） | Motley Fool | 2026-07-02 | 2026-07-13 09:20 UTC+8 |
| RSP / SPY YTD | ≈+9.7–10.7% / ≈+7.5–8.4% | 24/7 Wall St./Yahoo | 2026 年中 | 2026-07-13 09:20 UTC+8 |
| Top-10 集中度 | 36.40% | SPDR 持股經 P&I | 2026-07-02 | 2026-07-13 09:20 UTC+8 |
| CNN Fear & Greed | 48（Neutral） | cnn.com 經 MacroMicro/Benzinga | 2026-07-10 | 2026-07-13 09:20 UTC+8 |
| FINRA Margin Debt | $1.42T（+53.7% YoY） | FINRA/Advisor Perspectives | 2026-05（報告 06-24） | 2026-07-13 09:20 UTC+8 |
| AAII Bull/Bear | 36.3%／37.2% | aaii.com | 2026-07-10 | 2026-07-13 09:20 UTC+8 |
| 家庭持股佔金融資產比 | 45.76% | FRED BOGZ1FL153064486Q | 2026-Q1（01-01） | 2026-07-13 09:05 UTC+8 |
| NAAIM Exposure | 82.95 | naaim/ycharts | 2026-07-08 | 2026-07-13 09:20 UTC+8 |
| Fed funds（上/下限） | 3.75%／3.50% | FRED DFEDTARU/DFEDTARL | 2026-07-12 | 2026-07-13 09:05 UTC+8 |
| HY OAS | 2.70% | FRED BAMLH0A0HYM2 | 2026-07-09 | 2026-07-13 09:05 UTC+8 |
| IG OAS | 0.76% | FRED BAMLC0A0CM | 2026-07-09 | 2026-07-13 09:05 UTC+8 |
| 10Y / 10Y 實質 / breakeven | 4.54%／2.31%／2.24% | FRED DGS10/DFII10/T10YIE | 07-09/07-09/07-10 | 2026-07-13 09:05 UTC+8 |
| WTI | $69.6 | FRED DCOILWTICO | 2026-07-06 | 2026-07-13 09:05 UTC+8 |
| CPI YoY | 4.17% | FRED CPIAUCSL | 2026-05 | 2026-07-13 09:05 UTC+8 |
| 5y5y forward | 2.20%（+2bps） | FRED T5YIFR | 2026-07-10 | 2026-07-13 09:05 UTC+8 |
| 10Y 期限溢價 | 0.7322%（+3.3bps） | FRED THREEFYTP10 | 2026-07-02 | 2026-07-13 09:05 UTC+8 |
| SOFR−IORB／SOFR99−IORB／SRF | −12bps／0bps／$0bn | FRED SOFR/SOFR99/IORB/RPONTTLD | 2026-07-09 | 2026-07-13 09:05 UTC+8 |
| WALCL | $6.74T（6,735,609 百萬美元） | FRED WALCL | 2026-07-08 | 2026-07-13 09:05 UTC+8 |
| ECB／BOJ 資產 | €5.98T／¥639.55T | FRED ECBASSETSW/JPNASSETS | 07-03／06-01 | 2026-07-13 09:05 UTC+8 |
| 銀行對 NBFI 放款 | $2.00T（1,995.08 億美元） | FRED LNFACBW027SBOG | 2026-07-01 | 2026-07-13 09:05 UTC+8 |
| 私募信貸 gate（BCRED/Apollo/Blue Owl） | 首度 5% gate／16.8%撥付／$4.7B撥付 | AltsWire/CNBC/Bloomberg | 06-04/06-22/07-02 | 2026-07-13 09:20 UTC+8 |
| 美債標售（10Y BTC／30Y） | 2.59／stop-through | KuCoin/TreasuryDirect | 07-08／07-09 | 2026-07-13 09:20 UTC+8 |
| FedWatch（7/29） | ≈70%持平/25%升息/0%降息 | CME/MacroMicro | 2026-07-08 | 2026-07-13 09:20 UTC+8 |
| US 槓桿 ETF AUM | TQQQ ≈$29–37B/SOXL ≈$14B/NVDL ≈$4B | etf.com/GraniteShares | 2026 年中 | 2026-07-13 09:20 UTC+8 |
| 0DTE 佔 SPX 量 | ≈61–63% | Cboe | 2026-Q2/06 | 2026-07-13 09:20 UTC+8 |
| OCC 6 月總量 | 16.03 億口（+45% YoY） | theocc.com | 2026-07-02 | 2026-07-13 09:20 UTC+8 |
| SKEW／VIX 期限／COR3M | 149.6／contango／7.81 | Saxo/Cboe | 2026-07-01 | 2026-07-13 09:20 UTC+8 |
| AI 基礎設施新債 | Amazon $25B／QTS ≈$2B／AI HY YTD ≈$31.9B | PitchBook/IndexBox/TechTimes | 2026-07（≈07-04–07-08） | 2026-07-13 09:20 UTC+8 |
| CFTC 槓桿基金淨空倉／MOVE | ≈$1T 紀錄區／≈68.89 | CFTC(WebSearch)/Yahoo ^MOVE | 07-07／07-10 | 2026-07-13 09:20 UTC+8 |
| +AI 改名 | EVTV → AZIO | Business Wire | 2026-07-10 | 2026-07-13 09:20 UTC+8 |

**SEARCH-VERIFIED traceability**

| 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|
| S&P P/E＋CAPE | S&P 500 trailing P/E Shiller CAPE July 2026 multpl | multpl.com/s-p-500-pe-ratio；multpl.com/shiller-pe | 2026-07-10 | 2026-07-13 09:20 UTC+8 |
| CNN F&G | CNN Fear and Greed Index today July 2026 | cnn.com/markets/fear-and-greed（403）；en.macromicro.me/charts/50108 | 2026-07-10 | 2026-07-13 09:20 UTC+8 |
| AAII | AAII investor sentiment survey July 10 2026 bullish bearish | aaii.com/sentimentsurvey；insights.aaii.com | 2026-07-10 | 2026-07-13 09:20 UTC+8 |
| NAAIM | NAAIM exposure index latest July 2026 | ycharts.com/indicators/naaim_number；naaim.org | 2026-07-08 | 2026-07-13 09:20 UTC+8 |
| Top-10 集中度 | S&P 500 top 10 concentration percent July 2026 | pionline.com/.../pi-sp500-index-concentration | 2026-07-02 | 2026-07-13 09:20 UTC+8 |
| RSP vs SPY | RSP vs SPY equal weight YTD 2026 divergence | 247wallst.com/investing/2026/06/10/rsp-vs-spy... | 2026-06（年中） | 2026-07-13 09:20 UTC+8 |
| Moonshots | biggest microcap stock gainers 100% single day quantum AI July 2026 | Finviz/Benzinga/StockTitan movers（0 件） | 2026-07-06–10 | 2026-07-13 09:20 UTC+8 |
| +AI rename | AI rename ticker change SPAC July 2026 Azio EVTV | businesswire.com/news/home/20260710628386 | 2026-07-10 | 2026-07-13 09:20 UTC+8 |
| Insider Form 4 | insider selling Form 4 cluster AI leaders July 2026 openinsider | levelfields.ai（403 一手 EDGAR 封鎖，0 件合格） | 2026-07 首週 | 2026-07-13 09:20 UTC+8 |
| 私募信貸 gate | BCRED Apollo Blue Owl redemption gate proration Q2 2026 | altswire.com；cnbc.com/2026/06/23；bloomberg 07-02 | 06-04/06-22/07-02 | 2026-07-13 09:20 UTC+8 |
| FedWatch | CME FedWatch rate hike cut probability July 2026 | cmegroup.com FedWatch；macromicro.me/charts/144242 | 2026-07-08 | 2026-07-13 09:20 UTC+8 |
| 美債標售 | Treasury 10Y 30Y auction July 2026 bid to cover tail | kucoin.com news；treasurydirect.gov/auctions/results | 07-08/07-09 | 2026-07-13 09:20 UTC+8 |
| Leveraged ETF AUM | TQQQ SOXL NVDL AUM outflows July 2026 | etf.com/.../dumping-tqqq-soxl；graniteshares.com/etfs/nvdl | 2026 年中 | 2026-07-13 09:20 UTC+8 |
| 單股槓桿發行 | single-stock leveraged ETF launch July 2026 SK Hynix Tradr | proshares.com press；globenewswire 07-07；usnews 07-10 | 07-01–07-13 | 2026-07-13 09:20 UTC+8 |
| 0DTE | 0DTE SPX options share volume 2026 Cboe | cboe.com/insights；ir.cboe.com June 2026 volume | 2026-Q2/06 | 2026-07-13 09:20 UTC+8 |
| OCC 量 | OCC monthly options volume June 2026 | theocc.com/newsroom/.../07-02-june-2026 | 2026-07-02 | 2026-07-13 09:20 UTC+8 |
| AI 基礎設施債 | AI data center debt financing CoreWeave Amazon bond July 2026 | pitchbook.com/.../tops-250b；techtimes 07-04；indexbox | 06-15–07-08 | 2026-07-13 09:20 UTC+8 |
| CFTC/MOVE | CFTC leveraged funds Treasury net short MOVE index July 2026 | cftc.gov TFF（block）；finance.yahoo.com/quote/%5EMOVE | 07-07/07-10 | 2026-07-13 09:20 UTC+8 |
| Oracle/CoreWeave CDS | Oracle CoreWeave CDS spread AI credit July 2026 | ainvest/bondblox；finance.yahoo.com CoreWeave credit | 2026-06–07 | 2026-07-13 09:20 UTC+8 |
| VIX/SKEW | VIX term structure SKEW stock bond correlation July 2026 | home.saxo/.../options-brief-01072026 | 2026-07-01 | 2026-07-13 09:20 UTC+8 |
| Anthropic/OpenAI 營收 | OpenAI Anthropic annualized revenue run-rate 2026 | epoch.ai；venturebeat；futuresearch.ai | 2026-05 | 2026-07-13 09:20 UTC+8 |
| capex 供需 | GPU rental HBM DRAM pricing data center delay 2026 | semianalysis；trendforce.com | 2026-07（TrendForce 07-09） | 2026-07-13 09:20 UTC+8 |

**Macro script 說明**：`python3 scripts/fetch_macro.py 2026-07-09` 於 2026-07-13 執行，FRED 全序列 `status: ok`（多序列因前次基準日=最新觀測日而 `no_new_obs: true`，Δ=0 為成功結果）；`repo_stress` ok；`cftc_lev_funds`／`move_index`／`ofr_repo` `fetch_failed`（改走 best-effort WebSearch）。金鑰未輸出。

## 本次分數存檔
```json
{
  "date": "2026-07-13",
  "iso_week": "2026-W29",
  "weekday": "Monday",
  "timezone": "Asia/Taipei",
  "valuation": 79,
  "breadth": 30,
  "speculation": 58,
  "retail": 51,
  "monetary": 75,
  "structural": 77,
  "total": 64,
  "tier": "警戒",
  "regime": "穩定共存"
}
```

本報告為相對風險溫度計，非擇時訊號。
