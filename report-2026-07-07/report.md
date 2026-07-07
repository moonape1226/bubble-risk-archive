# 2026-07-07 市場泡沫風險評估報告
> 報告日期：2026-07-07；執行日：2026-07-07 Asia/Taipei；ISO 週次：2026-W28；前次基準：report-2026-07-06（1天前）

**總評**：總分 64【警戒】（Δ 0）；扳機狀態：已擊發；最貼近錨點：1997 早期建設（50%）。

## §1 六維度風險條圖
| 維度 | 條圖 | 本次 | 前次 | Δ |
|---|---|---:|---:|---:|
| 估值溢價 | ▰▰▰▰▰▰▰▱▱▱ | 79 | 79 | 0 |
| 市場廣度 | ▰▰▰▱▱▱▱▱▱▱ | 30 | 30 | 0 |
| 投機行為 | ▰▰▰▰▰▱▱▱▱▱ | 58 | 58 | 0 |
| 散戶情緒 | ▰▰▰▰▰▱▱▱▱▱ | 50 | 50 | 0 |
| 貨幣與信貸環境 | ▰▰▰▰▰▰▰▱▱▱ | 75 | 75 | 0 |
| 結構性槓桿 | ▰▰▰▰▰▰▰▱▱▱ | 75 | 75 | 0 |
| **加權總分** | ▰▰▰▰▰▰▱▱▱▱ | **64【警戒】** | 64 | 0 |

## §2 歷史錨點相似度
| 錨點 | 相似度 | 條圖 | 標記 |
|---|---:|---|---|
| 1997 早期建設 | 50% | ▰▰▰▰▰▱▱▱▱▱ | ◀ 最貼近 |
| 1998 LTCM 衝擊 | 50% | ▰▰▰▰▰▱▱▱▱▱ |  |
| 1999 晚期狂熱 | 40% | ▰▰▰▰▱▱▱▱▱▱ |  |
| 2000/3 頂點 | 15% | ▰▱▱▱▱▱▱▱▱▱ |  |
| 2021/12 Meme 頂 | 40% | ▰▰▰▰▱▱▱▱▱▱ |  |

## §3 三角訊號
| 指標 | 本次數值 | vs 前次 |
|---|---|---|
| S&P 500 | 7,537.43 | 持平（無新觀測） |
| WTI 原油 | $71.87 /bbl | 持平（無新觀測） |
| 10Y Treasury | 4.49% | 持平（無新觀測） |

**三者狀態**：穩定共存——本次 script 對三序列均回報 `no_new_obs: true`（前次執行日 2026-07-06 與最新有效觀測同日，市場資料尚無新觀測），三者週變動皆為 0（持平），未見任一方向拉伸，`sp500_trend.dev200_pct` +8.49% 亦 < +10%（regime：穩定共存）：

- 股市：S&P 500 **7,537.43**（`sp500_trend.latest`，2026-07-06；距 200-DMA **+8.49%**、距 52 週 MA **+10.31%**，價格中度拉伸、200-DMA 偏離未達 +10%）；vs 前次 持平（無新觀測）
- WTI 原油：**$71.87/bbl**（`DCOILWTICO`，2026-06-29，處相對低檔、非多月高點）；vs 前次 持平（無新觀測）
- 10Y 殖利率：**4.49%**（`DGS10`，2026-07-02）；本週無新觀測、週變動 0 bps，驅動因素無變動

**格局轉變**：前次 不可判 → 本次 穩定共存（前次 `regime` 讀自 report-2026-07-06 `score.json`＝不可判；本次 script 已供 `no_new_obs` 零 delta，格局依判定規則正常計算為 穩定共存——為資料可得性恢復，非市場相位反轉）。

**10Y 成因拆解**（週變動 Δ，bps）：本週無新觀測（`decomposition.driver == "none"`，各項 Δ 皆 0）：
- ΔDFII10 實質殖利率週變動：**0 bps**（無新觀測；水位 2.26%，`DFII10`，2026-07-02）
- ΔT10YIE 損益平衡通膨週變動：**0 bps**（無新觀測；水位 2.24%，`T10YIE`，2026-07-06）
- 判定：**無變動（無新觀測）**（`ΔDGS10 ≈ ΔDFII10 + ΔT10YIE` 恆等於 0＋0；不以任何水位充當 Δ）

**扳機鏈**：
- **A 通膨鏈：油 → 通膨預期 → Fed 受限 → refinancing 成本**——「油」端未施壓：WTI $71.87 處相對低檔、非通膨推手；惟 **CPI YoY 4.17%**（`CPIAUCSL`，資料月 2026-05）仍在 ≥4% 高檔、**5y5y forward 2.21%**（`T5YIFR`，2026-07-06）通膨預期未回落，壓縮 Fed 寬鬆空間；CME FedWatch 顯示 2026-07-29 FOMC 高機率按兵不動。鏈條的擊發並非來自油價，而是**非銀信用端**（見 B / 結論）。
- **B 槓桿鏈：衝擊 → NBFI 去槓桿 → margin spiral → 國債市場失序**（BIS AER 2026 Ch II 傳導鏈；2025-04 swap-spread unwind 為原型）——本週無基差交易槓桿新證據：未取得當週 CFTC 槓桿基金美債期貨淨空倉、MOVE 急升或 repo stress 之具名披露（✗ NOT DISCLOSED，best-effort，不杜撰）；10Y 本週零變動、無 real-rate 主導的異常上行，本鏈未見點火。

⚠ **結論**：**扳機狀態：已擊發**——判定依據為「私募信貸 gate proration / breach」：Blue Owl 兩檔非交易 BDC（OCIC/OTIC）維持 5% 季度贖回上限並依比例撥付（proration），第二季贖回請求續在高位（BofA 估 Q2 為贖回高峰）；Blackstone BCRED 第一季以 $400M 自有資金頂住 7.9% 請求、第二季 BofA 估贖回升至約 12% 並預期限制提領（[PitchBook](https://pitchbook.com/news/articles/private-credit-bdc-redemption-requests-likely-to-peak-in-q2-2026-bofa)、[Alternatives Watch](https://www.alternativeswatch.com/2026/07/02/private-credit-interval-funds-redemption-limits/)）。歷史意義：此為 1998 LTCM 型「融資扳機」特徵——公開市場利差（HY/IG OAS 2.74%/0.75%）尚未反映、非銀信用先行承壓，與極窄公開利差的自滿側並存，形成「froth 與扳機同框」的不穩定配置。此標籤為 §2 checklist 與 D5 的共用輸入，不寫入 score.json。（註：gate proration 為延續性事件、非本週新升級。）

## 六維度評分

### 1. 估值溢價 — 79（weight 22%，Δ 0）

- **S&P 500 Shiller CAPE** **39.46**（2026-07-01，[GuruFocus](https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio)；[multpl](https://www.multpl.com/shiller-pe) ~41.6）——高於長期均值 ~32.3 約 22%，絕對水位仍極端。
- **S&P 500 trailing P/E** **25.6**（2026-07-06，[GuruFocus](https://www.gurufocus.com/economic_indicators/57/sp-500-pe-ratio)）——本益比高檔，與 CAPE 同向。
- **Mag 7 加權前瞻 P/E** ~**29×**（stock-of-state，2026 上半年，[Fortune](https://fortune.com/2026/01/11/magnificent-7-stock-market-dominance-cracking-nvidia-microsoft-apple-meta-alphabet-amazon-tesla/)）——龍頭估值仍溢價於歷史。
- **Excess CAPE Yield（`ECY = 1/CAPE − DFII10/100`）** ~**0.27%**（derived：1/39.46 − 2.26/100；CAPE 41.6 則 ~0.14%）——逼近 0，屬 1929/2000 級別跨時代訊號；CAPE 高位十年裡實質利率把它推向真正極端（confirmation，不主計分）。
- **價格趨勢偏離（Farrell #1/#2/#4）** S&P 500 距 200-DMA **+8.49%**、距 52 週 MA **+10.31%**（`sp500_trend`，FRED SP500 計算，2026-07-06）——中度拉伸、200-DMA 偏離未達 +10%，均值回歸下行位能中等；與 P/E/CAPE 互補、不重複計分。
- **AI 基本面 reality check**：hyperscaler capex 指引仍在上修（2026 合計 ~$725B、YoY +77%；MSFT $190B、GOOGL ~$190B、AMZN ~$200B、META $115–135B，[Tom's Hardware](https://www.tomshardware.com/tech-industry/big-tech/big-techs-ai-spending-plans-reach-725-billion)），且 GPU 租金仍緊、供給售罄至 2026 年 8–9 月——產能仍被利用率吸收、無過剩證據，估值風險未因基本面惡化而升溫。
- **AI compute 供需 reality check**：本次未取得當週新的 GPU 租金／HBM 定價／利用率直接證據（沿用背景：租金偏緊、無過剩訊號）；依規格，無直接利用率證據時結論降為「capex / Nvidia 營收仍支撐，但未取得直接利用率證據」（相關利用率／定價 item 標 ✗ NOT DISCLOSED）。
- **TP-upgrade phase signal**：本期未取得過去 14 日具名合格 sell-side TP 上修拆解（✗ NOT DISCLOSED，不納入計分）。
- **結論**：估值裸值極端（CAPE 39.5、ECY 近 0）但價格拉伸中等、hyperscaler capex 與 GPU 供需暫撐基本面；1 天內無新觀測、無估值面質變，維持 **79**（落 rubric 高緣、未達頂點級 85+）。

### 2. 市場廣度 — 30（weight 13%，Δ 0）

- **RSP（等權）vs SPY（市值權）YTD** +9.67% **領先** +8.38%（2026-06 中旬，[24/7 Wall St.](https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/)）——廣度呈擴散／健康、非轉窄。
- **Top-10 集中度** **35.59%**（2026-04，[AhaSignals](https://ahasignals.com/sp500-concentration-risk/)）——已自 2025 年底 ~40.7% 高峰回落但仍歷史偏高，龍頭同綁 AI 具相關性風險。
- **A/D 廣度** ~50% 個股在 50-DMA 之上（中性，2026-06-09，[IndexMood](https://indexmood.com/breadth/advance-decline/today/)）——新高／新低大致均衡。
- **結論**：RSP 領先 + 集中度回落屬健康訊號，惟集中度仍歷史偏高；1 天內無新廣度數據，維持 **30**（落 rubric「21–40 輕微轉窄」偏低緣）。

### 3. 投機行為 — 58（weight 18%，Δ 0）

- **Microcap thematic moonshots** **0 檔合格**（✓ SEARCH-VERIFIED（0 件）；本週未見符合「單日 ≥100%、<$1B、2+ 疊加主題、弱基本面、附 PR/8-K URL」之單一標的；量子/AI 銅板股背景熱度仍在，惟無合格單日事件）——此為「無營收暴衝」主指標、本週靜。
- **+AI 改名 / SPAC / 無營收 IPO 暴衝** **0 件**（✓ SEARCH-VERIFIED（0 件）；未見具名 +AI 改名或殼股 SPAC 暴衝）。
- **IPO 市場熱度**：本週活躍但非無營收暴衝——Bending Spoons 7/1 首日 +40% 隨後回吐、當週多檔定價（7/6 週 7–9 檔/日，[stockanalysis IPO calendar](https://stockanalysis.com/ipos/calendar/)、[Renaissance Capital](https://www.renaissancecapital.com/IPO-Center/Stats)）；質地偏成長股、未見無營收股暴衝。
- **Upcoming AI IPO pipeline（liquidity-drain / 晚期訊號）**：OpenAI、Anthropic 均於 2026-06 向 SEC 保密遞交 S-1（[Built In](https://builtin.com/articles/top-tech-ipos-2026)、[indmoney](https://www.indmoney.com/blog/us-stocks/spacex-openai-anthropic-ipo-explained)）；SpaceX 已於 2026-06-12 掛牌（SPCX，首日 +19%，[CNBC](https://www.cnbc.com/2026/06/12/spacex-ipo-spcx-live-updates.html)）——巨型 IPO pipeline 活躍（30 日內具名 S-1／定價），為流動性抽離／敘事定價的晚期背景（✓ SEARCH-VERIFIED）。
- **Insider Form 4 clusters（14 日）** **0 件合格**（✓ SEARCH-VERIFIED（0 件）；過去 14 日未取得附 EDGAR filing/transaction 日期之合格 AI 龍頭叢集）。
- **OpenAI / Anthropic 營收軌跡**（集中度背景）：Anthropic run-rate ~$44B（2026-05，[indmoney](https://www.indmoney.com/blog/us-stocks/spacex-openai-anthropic-ipo-explained)）、OpenAI ~$24B（2026-04）——強勁，屬敘事／集中度背景、非泡沫切點。
- **Cboe equity put/call ratio** ✗ NOT DISCLOSED（confirmation only，缺值不調分）。
- **結論**：本週急性投機事件面續靜（moonshot 0、+AI 改名 0、insider 0），惟巨型 IPO pipeline 活躍為晚期背景；1 天內無質變，維持 **58**（落 rubric「41–60 投機升溫」偏上緣）。

### 4. 散戶情緒 — 50（weight 12%，Δ 0）

- **CNN Fear & Greed** **32（Fear）**（2026-07-02，[MacroMicro](https://en.macromicro.me/charts/50108/cnn-fear-and-greed)、[feargreedmeter](https://feargreedmeter.com/fear-and-greed-index)）——情緒面偏懼。
- **AAII 多頭** **31.4%**（週 2026-07-02，↓13.6pp、低於 37.5% 歷史均值、七週來第六次偏低，[SeekingAlpha](https://seekingalpha.com/news/4609705-bullish-sentiment-falls-sharply-while-bearish-views-rise-aaii-survey-shows)）——散戶調查偏空（本週無新號、沿用最新一週）。
- **FINRA margin debt** 5 月 **$1.42T**、MoM +8.5%、**YoY +53.7%**（2026-05 月頻，[Advisor Perspectives](https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra)）——YoY ≥ +40–50% 屬 1999/2007/2021 頂部級別警訊，部位面 froth。
- **家庭持股佔金融資產比** **45.76%**（`BOGZ1FL153064486Q`，資料季 2026-Q1／2026-01-01）——接近歷史高位、後續加碼空間有限（Farrell #5，季頻、不計週 Δ）。
- **NAAIM Exposure** **84.69**（2026-07-01 週頻，[YCharts](https://ycharts.com/indicators/naaim_number)）——主動經理人曝險偏高＝擁擠多頭（Farrell #9 confirmation cross-check，不主計分）。
- **Social sentiment proxies** ✗ NOT DISCLOSED（本週無具名 WSB/cashtag 熱點，best-effort，不調分）。
- **結論**：情緒（F&G 32／AAII 31.4%）轉懼、部位（margin +53.7% YoY／家庭 45.76%／NAAIM 84.69）滿倉，兩者背離、淨值落中位；1 天內無新讀數，維持 **50**。

### 5. 貨幣與信貸環境 — 75（weight 20%，Δ 0；**扳機側**）

- **Fed funds 目標區間** **3.50–3.75%**（`DFEDTARU` 3.75／`DFEDTARL` 3.50，2026-07-06，Δ 0）——政策維持限制性。
- **Fed funds path（FedWatch）**：2026-07-29 FOMC 高機率按兵不動（best-effort，[CME FedWatch](https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html)）。
- **HY OAS** **2.74%**（`BAMLH0A0HYM2`，2026-07-03）、**IG OAS** **0.75%**（`BAMLC0A0CM`，2026-07-03）——公開信用利差近循環低點、極窄（**自滿側**）。
- **CPI YoY** **4.17%**（`CPIAUCSL`，資料月 2026-05）、**5y5y forward** **2.21%**（`T5YIFR`，2026-07-06）——實質通膨高檔、通膨預期未回落，壓縮 Fed 寬鬆空間（扳機側證據）。
- **10Y 名目殖利率** **4.49%**（`DGS10`，2026-07-02；本週 Δ 0 bps、無新觀測）——refinancing 成本維持高檔。
- **Fed 資產負債表 WALCL** **$6.72T**（$6,724,564M，`WALCL`，2026-07-01）——量能持平。
- **ECB／BOJ 資產**（全球流動性 confirmation，非第七維度）：ECB **€6.12T**（`ECBASSETSW`，2026-06-26）、BOJ **¥639.55T**（`JPNASSETS`，2026-06-01）。
- **PBoC aggregate financing** ✗ NOT DISCLOSED（best-effort）。
- **私募信貸贖回壓力（扳機側，已擊發）**：Blue Owl OCIC/OTIC 維持 5% 上限依比例撥付、Q2 為贖回高峰；BCRED Q1 以 $400M 自有資金頂住 7.9%、Q2 BofA 估升至約 12% 並預期限制提領（[PitchBook](https://pitchbook.com/news/articles/private-credit-bdc-redemption-requests-likely-to-peak-in-q2-2026-bofa)、[Alternatives Watch](https://www.alternativeswatch.com/2026/07/02/private-credit-interval-funds-redemption-limits/)）——一般宏觀/非銀信用流動性，與 D6 的 AI 基建私募信貸分開、不重複計分。
- **結論（扳機側）**：gate proration 持續的 financing 壓力，與極窄公開 HY/IG OAS 的自滿並存，雙向皆推高分數；1 天內無新觀測、質態未變，維持 **75**。判分側別：**扳機側**（financing 壓力已擊發）。

### 6. 結構性槓桿 — 75（weight 15%，Δ 0）

- **美國槓桿 ETF 總 AUM** **~$198B** 創高（TQQQ $31.3B、SOXL $17.3B、NVDL $4B+/12 個月 +172%，[CryptoBriefing](https://cryptobriefing.com/leveraged-etfs-record-198b-aum/)、[ETF.com](https://www.etf.com/sections/news/nvdl-returned-172-one-year-new-era-leveraged-etfs-working)）；日均量 ~$45B、較上半年紀錄 +50%（Goldman，[SeekingAlpha](https://seekingalpha.com/news/4607458-leveraged-etfs-explode-in-2026-with-volumes-up-50-percent)）——AUM/量能加速。
- **美國單一個股槓桿 ETF 新核准（30 日）** 0 件（✓ SEARCH-VERIFIED（0 件），本週無新核准/上市）。
- **0DTE 佔 SPX 量** **~60–63%**（2026-02 創 63% 紀錄、近月續逾 60%，[Cboe](https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august/)、[IBKR](https://www.interactivebrokers.com/campus/traders-insight/securities/options/spx-0dte-options-jumped-to-record/)）——落 rubric「55–65%」高緣。
- **Options total volume（OCC 月報）**：OCC 月報未單獨取得；以 Cboe 指數期權量創高 + 槓桿 ETF ADV ~$45B（+50%）為 proxy（✓ SEARCH-VERIFIED，proxy）。
- **VIX / SKEW** **15.81 / 145.38**（2026-07-06 收，盤中曾 150.02，[Cboe SKEW](https://www.cboe.com/us/indices/dashboard/skew/)、[Yahoo ^VIX](https://finance.yahoo.com/quote/%5EVIX/)）——低波動＋高尾部避險溢價，交叉資產自滿（confirmation；stock-bond corr 未單獨量化）。
- **margin debt / 市值 ratio（cross-ref）**：引散戶 margin debt +53.7% YoY 作 confirmation，不在此重複計分。
- **AI 基建債務融資 / vendor-financing**：沿用背景——CoreWeave DDTL 4.0（$8.5B，03-31）/ 5.0（$3.1B，05-18）、Sharon AI $1.6B（06）、Nvidia GPU-backstop 循環融資（[MLQ](https://mlq.ai/news/nvidia-launches-gpu-backstop-financing-model-takes-cut-of-cloud-revenue-from-neocloud-partners/)）；本週無新增合格披露（30 日內已披露設施作 refinancing-sensitivity 背景，不加計分）。
- **全球槓桿產品擴散**：南韓單一個股槓桿 ETF（5 月底上市、6 月兩度熔斷、國會 07-06 啟動檢討）為延續性背景；台/日仍僅指數型槓桿。**本週無 2+ 非美市場新核准 → 本週擴散訊號未觸發**（Special rule 樓地板 81 不啟動）。
- **美債基差交易槓桿** ✗ NOT DISCLOSED（best-effort；本週未取得 CFTC 槓桿基金淨空倉/MOVE/repo stress 具名當週讀數，缺值不調分）。
- **結論**：AUM 創高 + 0DTE 60–63% + AI 基建債務續擴，落 rubric「61–80 加速」；1 天內無新核准、無擴散觸發，維持 **75**。

## 綜合分數

| 維度 | 分數 | 權重 | 加權 |
|---|---:|---:|---:|
| 估值溢價 | 79 | 22% | 17.38 |
| 市場廣度 | 30 | 13% | 3.90 |
| 投機行為 | 58 | 18% | 10.44 |
| 散戶情緒 | 50 | 12% | 6.00 |
| 貨幣與信貸環境 | 75 | 20% | 15.00 |
| 結構性槓桿 | 75 | 15% | 11.25 |
| **加權總分** |  | **100%** | **63.97 → 64** |

加權總分 63.97，half-up 四捨五入 → **64**；依風險等級對照表（40–64＝警戒）判定 **等級：警戒**。
邊界帶：總分 64 距 警戒/高 邊界 ≤ 2 分，評分固有噪音約 ±2–3，等級判讀需保留餘地。

## 歷史泡沫週期對比

相似度計算：checklist v2

本週最貼近（同分取表列在前者）**1997 早期建設（50%）**，與 **1998 LTCM 衝擊（50%）** 並列——反映「高估值 + 健康廣度 + 非銀信用扳機已擊發」的混合相位。最貼近錨點全項命中明細：

- **1997 早期建設 50%（4/8）**：命中「市場廣度 < 45（30）✓、hyperscaler capex 續上修 ✓、散戶情緒 < 55（50）✓、HY OAS < 4% 且未走闊（2.74%）✓」；未命中「估值溢價 40–74（本次 79 過高）✗、投機行為 < 50（58）✗、結構性槓桿 < 50（75）✗、扳機狀態＝未擊發（本次已擊發）✗」。
- **1998 LTCM 衝擊 50%（4/8）**：命中「具名非銀/槓桿機構壓力披露（私募信貸 gate proration）✓、估值溢價 ≥60（79）✓、扳機狀態 ≥ 初啟（已擊發）✓、ΔT10YIE ≤ 0（本週 0 bps，通膨預期非主因）✓」；未命中 HY OAS 週Δ≥+30bps 或 VIX>25（VIX 15.81）✗、S&P 回檔 ≥5%（持平）✗、Fed 轉鴿（按兵不動）✗、市場廣度 Δ≥+8（Δ 0）✗。
- **1999 晚期狂熱 40%（4/10）**：命中「估值溢價 ≥75（79）✓、CAPE ≥38（39.46）✓、結構性槓桿 ≥60（75）✓、巨型 IPO pipeline 活躍（OpenAI/Anthropic 06 月具名 S-1、SpaceX 06-12 定價）✓」；未命中 投機≥60（58）、moonshot≥1（0）、廣度≥45（30）、D5 自滿側且 HY<3.5%（本次扳機側）、散戶≥55（50）、扳機未擊發（已擊發）。
- **2000/3 頂點 15%（1/8）**：僅命中「扳機狀態 ≥ 初啟（已擊發）✓」；估值未達 ≥85（79）、廣度未極窄（30）、無 insider cluster（0）、散戶未達 ≥65（50）、貨幣未轉緊、dev200 未自 >10% 回落（+8.49%）、投機未達 ≥70。
- **2021/12 Meme 頂 40%（3/8）**：命中「結構性槓桿 ≥65（75）✓、margin debt YoY ≥+40%（+53.7%）✓、CPI YoY ≥4%（4.17%）且 Fed 未實質緊縮 ✓」；未命中 散戶≥65（50）、社群投機熱具名（無）、流動性氾濫且 D5 自滿側（本次扳機側）、本週 moonshot≥1（0）、廣度≥50（30）。

**解讀**：當前週最像 1997 早期建設（廣度健康、capex 續增、公開信用利差仍窄），但估值溢價（79、ECY 近 0）已遠高於 1997 區間，且私募信貸 gate proration「已擊發」使 1998 LTCM 型融資扳機同分並列（50%）——顯示週期位置是「高估值 + 健康廣度 + 非銀信用扳機已現」的**混合相位**，而非乾淨的建設早期。以期別調整看結構性槓桿（margin debt YoY +53.7%、槓桿 ETF/0DTE、AI 基建債務）與 2021/12 的槓桿特徵同框（40%）：位能（估值/槓桿）已高、廣度尚廣、擴散未觸發，最該盯的是已擊發的非銀融資扳機是否外溢至公開利差。長期指數成長趨勢偏離參照（Dot-com ~95%、1929 ~110%、當前 AI 週期 ~147%，RIA/Farrell）僅作跨期敘事錨、非本週計分。

## 機構情緒對照

本次無新機構調查數據。（BofA Global Fund Manager Survey 最新為 6 月號，調查期早於前次基準；當期顯示經理人加現金/債、減股票，仍「steadfastly bullish」看成長。JPM 機構調查本次亦無新號。）

另按規格補充週頻 **NAAIM Exposure Index**：最新 **84.69**（2026-07-01，[YCharts](https://ycharts.com/indicators/naaim_number)）——主動經理人曝險偏高＝擁擠多頭，作為反向 cross-check（Farrell #9）；本值計於散戶情緒維度、於此僅敘述。

## 本次新增訊號

比較基準：vs 前次（1天前，report-2026-07-06）。本次六維度分數與加權總分皆與前次持平（Δ 0）——僅 1 天間隔、macro 全序列 `no_new_obs`、且無急性事件升級，故無數值變動；以下列本次質化訊號與資料狀態變化：

- **格局：不可判 → 穩定共存**：本次 script 對三角訊號三序列均回報 `no_new_obs: true`（成功的 Δ=0 結果），格局依判定規則正常計算為 穩定共存並持久化；前次因 script 未供日序方向而記 不可判。此為資料可得性恢復，非市場相位反轉。
- **貨幣與信貸環境（D5，扳機側質化訊號）**：依「雙向 Δ 遮蔽防護」——即使分數未動，本次仍落**扳機側**，須列為質化新訊號：私募信貸 gate proration 持續（Blue Owl OCIC/OTIC 5% 上限依比例撥付、Q2 為贖回高峰；BCRED Q2 BofA 估贖回升至約 12% 並預期限制提領）。分數未動因公開 HY/IG OAS 極窄的自滿側先前已把 D5 撐在高位。
- **投機行為（Δ 0）— 巨型 IPO pipeline 具名化**：OpenAI、Anthropic 2026-06 保密遞交 S-1、SpaceX 06-12 定價——巨型 AI IPO pipeline 活躍（本次由 ✗ NOT DISCLOSED 升級為具名 ✓），為晚期 liquidity-drain 背景；惟本週急性投機（moonshot 0、+AI 改名 0、insider 0）續靜，故投機分數維持 58 未升。
- **§2 錨點微調**：1998 LTCM 由 40%→50%（ΔT10YIE 本週為有效 0 bps，命中「≤0」）、1999 由 30%→40%（IPO pipeline 命中）；均為本週資料可得性/事件具名化帶動的 checklist 命中變化，最貼近仍為 1997（50%，與 1998 並列、取表列在前者）。
- **全球槓桿擴散**：南韓單一個股槓桿 ETF 熔斷/國會檢討為延續性背景；**本週無 2+ 非美市場新核准，本週擴散訊號未觸發**。

## 數據附錄

**原始數據表**（每列一個計分用具體數據點）

| 指標 | 數值 | 來源（FRED series ID / URL）| 資料日期 | 抓取 timestamp |
|---|---|---|---|---|
| S&P 500 Shiller CAPE | 39.46（multpl ~41.6） | GuruFocus / multpl.com | 2026-07-01 | 2026-07-07 11:40 CST |
| S&P 500 trailing P/E | 25.6 | GuruFocus | 2026-07-06 | 2026-07-07 11:40 CST |
| Mag 7 加權前瞻 P/E | ~29× | Fortune | 2026 上半年（stock-of-state） | 2026-07-07 11:40 CST |
| S&P 500 距 200-DMA / 52wMA | +8.49% / +10.31% | FRED SP500（`sp500_trend`，script） | 2026-07-06 | 2026-07-07 script |
| S&P 500 spot | 7,537.43 | FRED SP500（`sp500_trend`，script） | 2026-07-06 | 2026-07-07 script |
| Excess CAPE Yield | ~0.27%（derived） | 1/CAPE − DFII10/100 | 2026-07-02 | 2026-07-07 11:40 CST |
| RSP vs SPY YTD | +9.67% vs +8.38% | 24/7 Wall St. | 2026-06 中旬 | 2026-07-07 11:40 CST |
| Top-10 集中度 | 35.59% | AhaSignals | 2026-04 | 2026-07-07 11:40 CST |
| A/D 廣度 | ~50% 個股 > 50-DMA（中性） | IndexMood | 2026-06-09 | 2026-07-07 11:40 CST |
| CNN Fear & Greed | 32（Fear） | MacroMicro / CNN / feargreedmeter | 2026-07-02 | 2026-07-07 11:40 CST |
| FINRA margin debt | $1.42T（MoM +8.5%、YoY +53.7%） | FINRA / Advisor Perspectives | 2026-05（月頻） | 2026-07-07 11:40 CST |
| AAII 多頭 | 31.4%（↓13.6pp） | AAII / SeekingAlpha | 2026-07-02 | 2026-07-07 11:40 CST |
| 家庭持股佔金融資產比 | 45.76% | FRED（series_id=BOGZ1FL153064486Q） | 2026-01-01（季頻 2026-Q1） | 2026-07-07 script |
| NAAIM Exposure | 84.69 | YCharts / naaim.org | 2026-07-01 | 2026-07-07 11:40 CST |
| Fed funds（上/下限） | 3.75% / 3.50% | FRED（series_id=DFEDTARU / DFEDTARL） | 2026-07-06 | 2026-07-07 script |
| HY OAS | 2.74% | FRED（series_id=BAMLH0A0HYM2） | 2026-07-03 | 2026-07-07 script |
| IG OAS | 0.75% | FRED（series_id=BAMLC0A0CM） | 2026-07-03 | 2026-07-07 script |
| 10Y 名目殖利率 | 4.49% | FRED（series_id=DGS10） | 2026-07-02 | 2026-07-07 script |
| 10Y 實質殖利率 | 2.26% | FRED（series_id=DFII10） | 2026-07-02 | 2026-07-07 script |
| 10Y 損益平衡通膨 | 2.24% | FRED（series_id=T10YIE） | 2026-07-06 | 2026-07-07 script |
| WTI 原油 | $71.87 | FRED（series_id=DCOILWTICO） | 2026-06-29 | 2026-07-07 script |
| CPI YoY | 4.17% | FRED（series_id=CPIAUCSL，yoy） | 2026-05-01（月頻） | 2026-07-07 script |
| 5y5y forward 通膨預期 | 2.21% | FRED（series_id=T5YIFR） | 2026-07-06 | 2026-07-07 script |
| CME FedWatch（07-29 按兵） | 高機率 hold | CME Group | 2026-07 初 | 2026-07-07 11:40 CST |
| Fed 資產負債表 WALCL | $6,724,564M（$6.72T） | FRED（series_id=WALCL） | 2026-07-01 | 2026-07-07 script |
| ECB 資產 | €6,117,260M（€6.12T） | FRED（series_id=ECBASSETSW） | 2026-06-26 | 2026-07-07 script |
| BOJ 資產 | ¥6,395,509 億（¥639.55T） | FRED（series_id=JPNASSETS） | 2026-06-01 | 2026-07-07 script |
| 私募信貸贖回壓力 | Blue Owl OCIC/OTIC 5% 上限 proration、Q2 贖回高峰；BCRED Q2 ~12%（BofA） | PitchBook / Alternatives Watch | 2026-07-02 揭露 | 2026-07-07 11:40 CST |
| Hyperscaler 2026 capex | 合計 ~$725B（+77%）；MSFT $190B / GOOGL ~$190B / AMZN ~$200B / META $115–135B | Tom's Hardware | 2026-Q1 指引（stock-of-state） | 2026-07-07 11:40 CST |
| OpenAI / Anthropic ARR | ~$24B / ~$44B run-rate | VentureBeat / indmoney | 2026-04 / 2026-05 | 2026-07-07 11:40 CST |
| Upcoming AI IPO pipeline | OpenAI/Anthropic 06 月保密 S-1；SpaceX 06-12 掛牌 SPCX | Built In / CNBC / indmoney | 2026-06 | 2026-07-07 11:40 CST |
| 美國槓桿 ETF AUM | $198B（TQQQ $31.3B、SOXL $17.3B、NVDL $4B+）；ADV ~$45B（+50%） | CryptoBriefing / ETF.com / Goldman(SeekingAlpha) | 2026-H1 | 2026-07-07 11:40 CST |
| 0DTE 佔 SPX 量 | ~60–63% | Cboe / IBKR | 2026-02～近月 | 2026-07-07 11:40 CST |
| VIX / SKEW | 15.81 / 145.38（盤中曾 150.02） | Cboe / Yahoo | 2026-07-06 | 2026-07-07 11:40 CST |
| AI 基建債務 | CoreWeave DDTL 4.0 $8.5B（03-31）/ 5.0 $3.1B（05-18）；Sharon AI $1.6B（06）；Nvidia GPU-backstop | SEC 8-K / MLQ | 2026-03～06 | 2026-07-07 11:40 CST |
| 南韓單一個股槓桿 ETF | 5 月底上市、6 月兩度熔斷、國會 07-06 檢討 | BigGo / Korea Herald | 2026-07-06 | 2026-07-07 11:40 CST |

**Coverage 覆蓋率表**（每列對應一個 `# Data sources` bullet；共 48 列）

| 維度 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|
| 估值：S&P 500 P/E + Shiller CAPE | multpl / GuruFocus [SEARCH] | ✓ SEARCH-VERIFIED（CAPE 39.46 / PE 25.6） |
| 估值：Mag 7 加權 P/E + AI leader P/S | 個股加權 vs 10 年均 | ✓ SEARCH-VERIFIED（Mag7 fwd ~29×，stock-of-state） |
| 估值：analyst TP upgrade decomposition | sell-side TP 拆解 [SEARCH，best-effort] | ✗ NOT DISCLOSED（14 日內無合格上修） |
| 估值：S&P 500 price-trend deviation | FRED SP500 → `sp500_trend`（script） | ✓ API（dev200 +8.49% / dev52w +10.31%） |
| 廣度：RSP vs SPY YTD divergence | ETF 比較 | ✓ SEARCH-VERIFIED（+9.67% vs +8.38%） |
| 廣度：Top-10 concentration | slickcharts / 研究 | ✓ SEARCH-VERIFIED（35.59%） |
| 廣度：A/D ratio + new high/low | 廣度指標 | ✓ SEARCH-VERIFIED（~50% > 50-DMA） |
| 散戶：CNN Fear & Greed | cnn.com [SEARCH] | ✓ SEARCH-VERIFIED（32 Fear） |
| 散戶：Margin Debt（FINRA） | FINRA 月頻 + YoY + /市值 | ✓ SEARCH-VERIFIED（$1.42T，+53.7% YoY） |
| 散戶：AAII 調查 | aaii.com [SEARCH] | ✓ SEARCH-VERIFIED（多頭 31.4%） |
| 散戶：Social sentiment proxies | Reddit/X [best-effort] | ✗ NOT DISCLOSED（無具名熱點） |
| 散戶：Household equity allocation | FRED BOGZ1FL153064486Q（script，季頻） | ✓ API（45.76%，2026-Q1） |
| 散戶：NAAIM Exposure Index | naaim/ycharts [SEARCH，best-effort] | ✓ SEARCH-VERIFIED（84.69） |
| 機構：BofA FMS + JPM 調查 | 月頻 [best-effort] | ✗ NOT DISCLOSED（前次後無新號） |
| 貨幣：Fed funds DFEDTARU/DFEDTARL | FRED（script） | ✓ API（3.75/3.50） |
| 貨幣：HY OAS BAMLH0A0HYM2 | FRED（script） | ✓ API（2.74%） |
| 貨幣：IG OAS BAMLC0A0CM | FRED（script） | ✓ API（0.75%） |
| 貨幣：10Y DGS10 | FRED（script） | ✓ API（4.49%） |
| 貨幣：10Y 實質 DFII10 | FRED（script） | ✓ API（2.26%） |
| 貨幣：10Y breakeven T10YIE | FRED（script） | ✓ API（2.24%，直抓非 derived） |
| 貨幣：WTI DCOILWTICO | FRED（script） | ✓ API（$71.87） |
| 貨幣：CPI YoY CPIAUCSL | FRED（script，月頻） | ✓ API（4.17%） |
| 貨幣：5y5y forward T5YIFR | FRED（script） | ✓ API（2.21%） |
| 貨幣：Fed funds path FedWatch | CME [SEARCH，best-effort] | ✓ SEARCH-VERIFIED（高機率 hold） |
| 貨幣：Fed 資產負債表 WALCL | FRED（script，週頻） | ✓ API（$6.72T） |
| 貨幣：ECB/BOJ ECBASSETSW/JPNASSETS | FRED（script） | ✓ API（€6.12T / ¥639.55T） |
| 貨幣：PBoC aggregate financing | NBS/PBoC 英文摘要 [best-effort] | ✗ NOT DISCLOSED |
| 貨幣：私募信貸/非銀基金流動性壓力 | BDC/interval fund [SEARCH，best-effort] | ✓ SEARCH-VERIFIED（gate proration 已擊發） |
| AI：Hyperscaler capex guidance | MSFT/GOOGL/AMZN/META 季報（stock-of-state） | ✓ SEARCH-VERIFIED（$725B，+77%） |
| AI：AI token volume growth | Anthropic/OpenAI/Google 揭露 [best-effort] | ✗ NOT DISCLOSED |
| AI：OpenAI/Anthropic 營收 | The Information/Reuters [best-effort] | ✓ SEARCH-VERIFIED（$24B / $44B run-rate） |
| AI：Hyperscaler 客戶集中度 | 財報質化 [best-effort] | ✗ NOT DISCLOSED |
| AI：AI compute 供需/過剩 | GPU 租金/HBM/利用率 [SEARCH，best-effort] | ✗ NOT DISCLOSED（本週無新直接利用率證據） |
| 投機：+AI 改名/SPAC/無營收 IPO（7d） | 新聞掃描 | ✓ SEARCH-VERIFIED（0 件） |
| 投機：IPO 市場熱度 | IPO 日曆/首日/無營收佔比 | ✓ SEARCH-VERIFIED（活躍、無無營收暴衝） |
| 投機：Microcap thematic moonshots | Finviz/Benzinga 掃描（required 週篩） | ✓ SEARCH-VERIFIED（0 件） |
| 投機：Upcoming AI IPOs | S-1/具名報導 [best-effort] | ✓ SEARCH-VERIFIED（OpenAI/Anthropic 06 月 S-1、SpaceX 定價） |
| 投機：Insider Form 4 clusters | SEC EDGAR [SEC EDGAR] | ✓ SEARCH-VERIFIED（0 件） |
| 投機：Cboe put/call ratio | Cboe/YCharts [SEARCH，best-effort] | ✗ NOT DISCLOSED |
| 結構：美國槓桿 ETF AUM | etf.com/ETFGI [SEARCH] | ✓ SEARCH-VERIFIED（$198B） |
| 結構：美國單一個股槓桿 ETF 核准 | SEC EDGAR/ETF.com | ✓ SEARCH-VERIFIED（0 件新核准） |
| 結構：全球槓桿產品核准 KRX/TWSE/JPX/ESMA | 各監管 [best-effort] | ✓ SEARCH-VERIFIED（南韓背景；本週擴散訊號未觸發） |
| 結構：0DTE option volume | Cboe/SpotGamma | ✓ SEARCH-VERIFIED（~60–63%） |
| 結構：Options total volume（OCC 月報） | OCC 月報 | ✓ SEARCH-VERIFIED（Cboe 量創高 + ADV ~$45B proxy；OCC 月報未單獨取得） |
| 結構：VIX/SKEW/stock-bond corr | Cboe [同類合併，worst-case] | ✓ SEARCH-VERIFIED（VIX 15.81/SKEW 145.38；stock-bond corr 未單獨量化） |
| 結構：margin debt/市值 ratio（cross-ref） | 引散戶 margin debt，confirmation only | ✓ SEARCH-VERIFIED（引 margin debt +53.7% YoY） |
| 結構：AI 基建債務/vendor-financing | 30 日掃描 [SEARCH，best-effort] | ✓ SEARCH-VERIFIED（CoreWeave/Sharon AI/Nvidia backstop，背景） |
| 結構：美債基差交易槓桿（CFTC/MOVE/repo） | CFTC TFF/MOVE/OFR [SEARCH，best-effort] | ✗ NOT DISCLOSED（本週無當週具名讀數） |

**✓ SEARCH-VERIFIED traceability（非 0 件列）**

| 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|
| CAPE / PE | S&P 500 Shiller CAPE trailing PE July 2026 | gurufocus.com/economic_indicators/56、/57；multpl.com | 2026-07-01 / 07-06 | 2026-07-07 11:40 CST |
| RSP/SPY | RSP vs SPY YTD 2026 divergence | 247wallst.com | 2026-06-10 | 2026-07-07 11:40 CST |
| Top-10 集中度 | S&P 500 top 10 concentration 2026 | ahasignals.com/sp500-concentration-risk | 2026-04 | 2026-07-07 11:40 CST |
| A/D 廣度 | S&P 500 advance decline breadth July 2026 | indexmood.com/breadth | 2026-06-09 | 2026-07-07 11:40 CST |
| CNN F&G | CNN Fear Greed today July 2026 | en.macromicro.me/charts/50108；feargreedmeter.com | 2026-07-02 | 2026-07-07 11:40 CST |
| Margin debt | FINRA margin debt 2026 May | advisorperspectives.com/dshort | 2026-05 | 2026-07-07 11:40 CST |
| AAII | AAII sentiment July 2026 | seekingalpha.com/news/4609705 | 2026-07-02 | 2026-07-07 11:40 CST |
| NAAIM | NAAIM exposure index July 2026 | ycharts.com/indicators/naaim_number | 2026-07-01 | 2026-07-07 11:40 CST |
| FedWatch | CME FedWatch July 2026 FOMC | cmegroup.com FedWatch | 2026-07 初 | 2026-07-07 11:40 CST |
| 私募信貸 | private credit BDC redemption Blue Owl BCRED July 2026 | pitchbook.com；alternativeswatch.com | 2026-07-02 | 2026-07-07 11:40 CST |
| Hyperscaler capex | MSFT GOOGL AMZN META capex 2026 | tomshardware.com | 2026-Q1 指引 | 2026-07-07 11:40 CST |
| OpenAI/Anthropic 營收 | OpenAI Anthropic ARR 2026 | venturebeat.com；indmoney.com | 2026-04 / 05 | 2026-07-07 11:40 CST |
| Upcoming AI IPO | OpenAI Anthropic SpaceX S-1 IPO 2026 | builtin.com；cnbc.com；indmoney.com | 2026-06 | 2026-07-07 11:40 CST |
| 槓桿 ETF AUM | leveraged ETF AUM NVDL TQQQ SOXL 2026 | cryptobriefing.com；etf.com；seekingalpha.com/news/4607458 | 2026-H1 | 2026-07-07 11:40 CST |
| 0DTE | 0DTE share SPX volume 2026 | cboe.com insights；interactivebrokers.com | 2026-02～近月 | 2026-07-07 11:40 CST |
| VIX/SKEW | VIX SKEW today July 2026 | cboe.com/us/indices SKEW；finance.yahoo.com/quote/%5EVIX | 2026-07-06 | 2026-07-07 11:40 CST |
| IPO 市場熱度 | IPO market this week July 2026 first day pop | renaissancecapital.com；stockanalysis.com/ipos/calendar | 2026-07 初 | 2026-07-07 11:40 CST |
| AI 基建債務 | CoreWeave neocloud debt financing 2026 | sec.gov 8-K；mlq.ai | 2026-03～06 | 2026-07-07 11:40 CST |
| 南韓槓桿 | single stock leveraged ETF Korea 2026 | finance.biggo.com；koreaherald.com | 2026-07-06 | 2026-07-07 11:40 CST |

**✓ SEARCH-VERIFIED（0 件）screens** — query、來源、timestamp（URL/發布日可為 —）：

| 篩選項 | search query | 檢查來源 | 結果 | 抓取 timestamp |
|---|---|---|---|---|
| +AI 改名/SPAC（7d） | AI rename ticker change SPAC no-revenue IPO surge July 2026 | Benzinga/MarketWatch movers、IPO 新聞 | 0 件合格 | 2026-07-07 11:40 CST |
| Microcap moonshots（週篩） | biggest microcap gainers 100% single day quantum AI space July 2026 | Finviz/Yahoo gainers/StockTwits | 0 件（無合格單日 ≥100% 事件） | 2026-07-07 11:40 CST |
| Insider Form 4 clusters（14d） | insider selling Form 4 cluster AI tech July 2026 SEC EDGAR | SEC EDGAR/GuruFocus/secform4 | 0 件（無附日期合格叢集） | 2026-07-07 11:40 CST |
| 美國單一個股槓桿 ETF 新核准（30d） | single stock leveraged ETF approval SEC EDGAR launch 2026 | SEC EDGAR/ETF.com | 0 件新核准 | 2026-07-07 11:40 CST |

**方法/失敗註記**：本次 `scripts/fetch_macro.py`（prior-run date 2026-07-06）回傳全序列 `status: ok`（FRED API），且對每一序列與 `sp500_trend`、`decomposition` 均回報 `no_new_obs: true`（前次執行日與最新有效觀測同日）——此為「Δ=0（無新觀測）」的成功結果，故 §3 三者標 持平（無新觀測）、10Y 週 Δ 拆解各項為 0 bps（`driver: none`）、格局依規則正常計算並持久化為 穩定共存（非 不可判）。best-effort 的美債基差交易槓桿本週無當週具名讀數（✗ NOT DISCLOSED）。FRED 金鑰全程未印出。

## 本次分數存檔
```json
{
  "date": "2026-07-07",
  "iso_week": "2026-W28",
  "weekday": "Tuesday",
  "timezone": "Asia/Taipei",
  "valuation": 79,
  "breadth": 30,
  "speculation": 58,
  "retail": 50,
  "monetary": 75,
  "structural": 75,
  "total": 64,
  "tier": "警戒",
  "regime": "穩定共存"
}
```

本報告為相對風險溫度計，非擇時訊號。
