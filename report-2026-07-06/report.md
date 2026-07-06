# 2026-07-06 市場泡沫風險評估報告
> 報告日期：2026-07-06；執行日：2026-07-06 Asia/Taipei；ISO 週次：2026-W28；前次基準：report-2026-07-02（4天前）

## §1 六維度風險條圖
| 維度 | 條圖 | 本次 | 前次 | Δ |
|---|---|---:|---:|---:|
| 估值溢價 | ▰▰▰▰▰▰▰▱▱▱ | 79 | 79 | 0 |
| 市場廣度 | ▰▰▰▱▱▱▱▱▱▱ | 30 | 30 | 0 |
| 投機行為 | ▰▰▰▰▰▱▱▱▱▱ | 58 | 62 | −4 |
| 散戶情緒 | ▰▰▰▰▰▱▱▱▱▱ | 50 | 55 | −5 |
| 貨幣與信貸環境 | ▰▰▰▰▰▰▰▱▱▱ | 75 | 74 | +1 |
| 結構性槓桿 | ▰▰▰▰▰▰▰▱▱▱ | 75 | 75 | 0 |
| **加權總分** | ▰▰▰▰▰▰▱▱▱▱ | **64【警戒】** | 65 | −1 |

## §2 歷史錨點相似度
| 錨點 | 相似度 | 條圖 | 標記 |
|---|---:|---|---|
| 1997 早期建設 | 50% | ▰▰▰▰▰▱▱▱▱▱ | ◀ 最貼近 |
| 1998 LTCM 衝擊 | 40% | ▰▰▰▰▱▱▱▱▱▱ |  |
| 1999 晚期狂熱 | 30% | ▰▰▰▱▱▱▱▱▱▱ |  |
| 2000/3 頂點 | 15% | ▰▱▱▱▱▱▱▱▱▱ |  |
| 2021/12 Meme 頂 | 40% | ▰▰▰▰▱▱▱▱▱▱ |  |

## §3 三角訊號
| 指標 | 本次數值 | vs 前次 |
|---|---|---|
| S&P 500 | 7,483.24 | — |
| WTI 原油 | $71.87 /bbl | — |
| 10Y Treasury | 4.48% | — |

**三者狀態**：本次方向不可用——腳本未供日序 delta（`decomposition` 回報 `unavailable_no_daily_history`、`sp500_trend` 與 `DCOILWTICO` 均無 `chg_pct`／`prior`），無法判定三者相位（regime：不可判）。以下僅列本次水位：

- 股市：S&P 500 7,483.24（2026-07-02，距 200-DMA +7.78%、距 52 週 MA +9.6%，價格中度拉伸但未達 +10%）；本次方向不可用——無腳本日序
- WTI 原油：$71.87/bbl（2026-06-29，處相對低檔、非多月高點）；本次方向不可用——無腳本日序
- 10Y 殖利率：4.48%（2026-07-01）；主要驅動因素本週不可拆解——無日序資料

**格局轉變**：前次 穩定共存 → 本次 不可判（本次三者方向不可用，非基準日；前次 `regime` 讀自 report-2026-07-02 `score.json`）。

**10Y 成因拆解**：本週 Δ 分解不可用——無日序資料（`decomposition.status == unavailable_no_daily_history`）。僅列水位：DGS10 4.48%、DFII10 2.25%、T10YIE 2.23%（均 FRED API，2026-07-01/02）；不以任何水位充當 Δ。

**扳機鏈：油 → 通膨預期 → Fed 受限 → refinancing 成本**：本鏈的「油」端未施壓——WTI $71.87 處相對低檔，非通膨推手；惟 CPI YoY 4.17%（`CPIAUCSL`，資料月 2026-05）仍在 ≥4% 高檔、5y5y forward（`T5YIFR`）2.22%，通膨預期未回落，壓縮 Fed 寬鬆空間——CME FedWatch 顯示 2026-07-29 FOMC 有 75.6% 機率按兵不動（2026-07-04）。鏈條的擊發並非來自油價，而是**非銀信用端**：私募信貸 gate proration 持續、Fitch 報 4 月美國私募信貸違約率創 6% 新高，financing 收縮已觸及非銀信用。

⚠ **結論**：**扳機狀態：已擊發**——判定依據為「私募信貸 gate proration / breach」：Blue Owl 兩檔非交易 BDC（OCIC/OTIC）第二季贖回請求 $4.7B、維持 5% 季度贖回上限並依比例撥付（proration）；Blackstone BCRED 第二季約 10% 贖回請求僅約半數獲償（2026-07-02 股東信）。歷史意義：此為 1998 LTCM 型「融資扳機」特徵——公開市場利差（HY/IG OAS）尚未反映、但非銀信用先行承壓；與當前極窄的公開利差（自滿側）並存，形成「froth 與扳機同框」的不穩定配置。此標籤為 §2 checklist 與 D5 的共用輸入，不寫入 score.json。（註：gate proration 為延續性事件、非本週新升級；本週新增的量化錨點為 Fitch 6% 違約率與 Q2 股東信揭露。）

## 六維度評分

### 1. 估值溢價 — 79（weight 22%，Δ 0）
S&P 500 Shiller CAPE ~39.5–41.6（[GuruFocus](https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio) 39.46 @2026-07-01；[multpl](https://www.multpl.com/shiller-pe/table/by-month) ~41.6）、trailing P/E ~25.4（[GuruFocus](https://www.gurufocus.com/economic_indicators/57/sp-500-pe-ratio) @2026-07-02；FactSet TTM ~27.8）、Mag 7 加權前瞻 P/E ~29×（[Fortune](https://fortune.com/2026/01/11/magnificent-7-stock-market-dominance-cracking-nvidia-microsoft-apple-meta-alphabet-amazon-tesla/)）——估值絕對水位仍極端。**Excess CAPE Yield（`ECY = 1/CAPE − DFII10/100`）**：以 CAPE 39.5、DFII10 2.25% 計 `derived` ≈ 1/39.5 − 0.0225 ≈ **0.28%**（CAPE 41.6 則 ≈ 0.15%），逼近 0，屬 1929/2000 級別的跨時代訊號——CAPE 高位十年裡，實質利率把它推向真正的極端。**價格趨勢偏離（Farrell #1/#2/#4）**：S&P 500 距 200-DMA +7.78%、距 52 週 MA +9.6%（`sp500_trend`，FRED SP500 計算），中度拉伸但未達 +10%，均值回歸下行位能中等、非最濃。**AI 基本面 reality check**：hyperscaler capex 指引仍在上修（2026 合計 $725B、YoY +77%；MSFT $190B、GOOGL ~$190B、AMZN ~$200B、META $115–135B，[Tom's Hardware](https://www.tomshardware.com/tech-industry/big-tech/big-techs-ai-spending-plans-reach-725-billion)），且 GPU 租金反升 ~40%、供給「售罄至 2026 年 8–9 月」（[Thunder Compute](https://www.thundercompute.com/blog/ai-gpu-rental-market-trends)、[SemiAnalysis](https://newsletter.semianalysis.com/p/the-great-gpu-shortage-rental-capacity)）——產能仍被利用率吸收、無過剩證據，估值風險未因基本面惡化而升溫。**TP-upgrade phase signal**：本期未取得過去 14 日具名合格 sell-side TP 上修拆解（✗ NOT DISCLOSED），不納入計分。綜合：估值裸值極端（CAPE、ECY 近 0）但價格拉伸中等、基本面暫撐，維持 79。

### 2. 市場廣度 — 30（weight 13%，Δ 0）
RSP（等權）YTD +9.67% **領先** SPY（市值權）+8.38%（[24/7 Wall St.](https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/)，@2026-06 中旬）——廣度呈**擴散/健康**、非轉窄。Top-10 集中度 35.59%（2026-04，[AhaSignals](https://ahasignals.com/sp500-concentration-risk/)），已自 2025 年底 40.7% 高峰回落但仍歷史偏高（HHI 185 vs 5 年均 142）。A/D 中性（~50% 個股在 50-DMA 之上，@2026-06-09，[IndexMood](https://indexmood.com/breadth/advance-decline/today/)）。RSP 領先與集中度回落屬健康訊號，惟集中度仍高、且龍頭同綁 AI 具相關性風險，落在 rubric「21–40 輕微轉窄」偏低緣、維持 30。

### 3. 投機行為 — 58（weight 18%，Δ −4）
本週投機**事件面轉靜**：(a) microcap thematic moonshot **0 檔合格**（✓ SEARCH-VERIFIED（0 件）；本週未見符合「單日 ≥100%、<$1B、2+ 疊加主題、弱基本面、附 PR/8-K URL」之單一標的，惟量子/AI 銅板股背景熱度仍高——S&P Kensho 量子指數 YTD +69%、IonQ +60%，[Motley Fool](https://www.fool.com/investing/stock-market/market-sectors/information-technology/ai-stocks/quantum-computing-stocks/)）；(b) 無具名 +AI 改名 / SPAC 事件（✓ SEARCH-VERIFIED（0 件））；(c) IPO 市場溫和、未見無營收暴衝（✓ SEARCH-VERIFIED，[stockanalysis IPO calendar](https://stockanalysis.com/ipos/calendar/)）；(d) AI 龍頭 insider Form 4 cluster **0 件合格**（過去 14 日未取得附 EDGAR filing/transaction 日期之合格叢集，✓ SEARCH-VERIFIED（0 件））。OpenAI/Anthropic 營收軌跡強勁（Anthropic ~$30B ARR、OpenAI $24B，2026-04，[VentureBeat](https://venturebeat.com/technology/anthropic-says-it-hit-a-30-billion-revenue-run-rate-after-crazy-80x-growth)），為集中度/敘事風險背景、非泡沫切點。Cboe put/call ✗ NOT DISCLOSED（confirmation only，不調分）。相對前次（62），本週急性投機訊號全數轉靜（moonshot 0/週），故降至 58（落 rubric「41–60 投機升溫」偏上緣）。

### 4. 散戶情緒 — 50（weight 12%，Δ −5）
情緒面**轉保守**：CNN Fear & Greed **32（Fear）**（@2026-07-02，[MacroMicro](https://en.macromicro.me/charts/50108/cnn-fear-and-greed)）、AAII 多頭降 13.6pp 至 **31.4%**（低於 37.5% 歷史均值，七週來第六次偏低，[SeekingAlpha](https://seekingalpha.com/news/4609705-bullish-sentiment-falls-sharply-while-bearish-views-rise-aaii-survey-shows)）。惟**部位面仍偏 froth**：FINRA margin debt 5 月創 $1.42T、MoM +8.5%、**YoY +53.7%**（[Advisor Perspectives](https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra)、[GuruFocus](https://www.gurufocus.com/economic_indicators/4264/finra-investor-margin-debt)）——YoY ≥ +40–50% 屬 1999/2007/2021 頂部級別警訊；家庭持股佔金融資產比 45.76%（`BOGZ1FL153064486Q`，資料季 2026-Q1/2026-01-01，接近歷史高位，Farrell #5）；NAAIM 曝險 84.69（@2026-07-01，週頻，高擁擠多頭，Farrell #9 confirmation cross-check）。情緒（F&G/AAII）與部位（margin/家庭/NAAIM）背離：前者轉懼、後者滿倉，淨值落中位，較前次（55）下修至 50。

### 5. 貨幣與信貸環境 — 75（weight 20%，Δ +1；**扳機側**）
政策面：Fed funds 3.50–3.75%（DFEDTARU 3.75 / DFEDTARL 3.50，Δ 0）、CME FedWatch 2026-07-29 FOMC 75.6% 按兵不動（@2026-07-04，[CME](https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html)）。**公開信用利差極窄（自滿側）**：HY OAS **2.75%**、IG OAS **0.75%**（`BAMLH0A0HYM2`/`BAMLC0A0CM`，FRED API @2026-07-02，近循環低點）。**通膨端壓縮 Fed 空間**：CPI YoY 4.17%（`CPIAUCSL`，資料月 2026-05）、5y5y forward 2.22%（`T5YIFR`）；10Y 4.48%（本週 Δ 分解不可用——無日序）。Fed 資產負債表 WALCL $6.7246T（2026-07-01）；ECB 資產 €6.1173T（`ECBASSETSW`，2026-06-26）、BOJ ¥6,395.5T×億（`JPNASSETS`，2026-06-01）為全球流動性 confirmation、非第七維度；PBoC ✗ NOT DISCLOSED。**私募信貸贖回壓力（扳機側，已擊發）**：Blue Owl 兩檔非交易 BDC 第二季贖回請求 $4.7B（Q1 $5.4B 略降）、維持 5% 上限依比例撥付；BCRED 第二季 ~10% 請求僅半數獲償；Fitch 報 4 月美國私募信貸違約率創 **6%** 新高（[Benzinga](https://www.benzinga.com/markets/private-markets/26/07/60256219/blue-owl-records-4-7-billion-in-redemption-requests-as-private-credit-pressure-lingers)、[Alternatives Watch 2026-07-02](https://www.alternativeswatch.com/2026/07/02/private-credit-interval-funds-redemption-limits/)）。此為一般宏觀/非銀信用流動性，與結構性槓桿的 AI 基建私募信貸分開、不重複計分。**判分側別：扳機側**——gate proration 持續 + 違約率創高的 financing 壓力，與極窄公開利差的自滿並存，雙向皆推高分數；較前次（74）微升至 75。

### 6. 結構性槓桿 — 75（weight 15%，Δ 0）
美國槓桿 ETF 總 AUM 創 **$198B** 新高（TQQQ $29–39B、SOXL $13–28B、NVDL YTD +68.4%，[CryptoBriefing](https://cryptobriefing.com/leveraged-etfs-record-198b-aum/)）；日均量約 $45B、較上半年紀錄再 **+50%**（Goldman，[SeekingAlpha](https://seekingalpha.com/news/4607458-leveraged-etfs-explode-in-2026-with-volumes-up-50-percent)）——AUM/量能加速。**0DTE 佔 SPX 量約 60–63%**（2026-02 創 63% 紀錄、近月續逾 60%，[Cboe](https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-record-62-share-in-august/)、[IBKR](https://www.interactivebrokers.com/campus/traders-insight/securities/options/spx-0dte-options-jumped-to-record/)），落 rubric「55–65%」高緣。VIX 15.81 / SKEW 150.02（@2026-07-02，[Cboe SKEW](https://www.cboe.com/us/indices/dashboard/skew/)）——低波動＋高尾部避險溢價，交叉資產自滿。**AI 基建債務融資**：CoreWeave DDTL 4.0（$8.5B，2026-03-31，Moody's A3）、DDTL 5.0（$3.1B，2026-05-18，首檔公開聯貸 HPC 融資）；Sharon AI 2026-06 私募 $1.6B（Nvidia AI factory）；Nvidia GPU-backstop 融資模式（循環 vendor-financing，[MLQ](https://mlq.ai/news/nvidia-launches-gpu-backstop-financing-model-takes-cut-of-cloud-revenue-from-neocloud-partners/)）——結構性槓桿在 AI capex 交易內擴張。**全球擴散**：南韓單一個股槓桿 ETF（5 月底上市，僅三星/SK 海力士合格）6 月兩度觸發熔斷、國會 2026-07-06 啟動檢討（[BigGo](https://finance.biggo.com/news/f23c7efe-a31f-4e10-92c8-28d5c46c8ee8)、[Korea Herald](https://www.koreaherald.com/article/10722289)）；台/日仍僅指數型槓桿、無單一個股產品。**本週無 2+ 非美市場新核准 → 本週擴散訊號未觸發**（Special rule 樓地板 81 不啟動）。綜合 AUM 創高 + 0DTE 60–63% + AI 基建債務續擴，落 rubric「61–80 加速」、維持 75。

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

本週最貼近 **1997 早期建設（50%）**：命中「市場廣度 < 45（30）✓、hyperscaler capex 續上修 ✓、散戶情緒 < 55（50）✓、HY OAS < 4% 且未走闊（2.75%）✓」，未命中「估值溢價 40–74（本次 79 過高）✗、投機行為 < 50（58）✗、結構性槓桿 < 50（75）✗、扳機狀態＝未擊發（本次已擊發）✗」= 4/8。但本相似度須與其他錨點合讀——當前並非乾淨的早期建設：

- **1998 LTCM 衝擊 40%**（3/8）：命中「具名非銀/槓桿機構壓力披露（私募信貸 gate proration）✓、估值溢價 ≥60（79）✓、扳機狀態 ≥ 初啟（已擊發）✓」；未命中 HY OAS 週Δ≥+30bps 或 VIX>25（VIX 15.8）、S&P 回檔 ≥5%（方向不可用）、Fed 轉鴿、廣度 Δ≥+8、ΔT10YIE≤0（無資料）。
- **1999 晚期狂熱 30%**（3/10）：命中「估值溢價 ≥75（79）✓、CAPE ≥38（~39.5）✓、結構性槓桿 ≥60（75）✓」；未命中 投機≥60、moonshot≥1、廣度≥45、D5 自滿側且 HY<3.5%（本次扳機側）、散戶≥55、巨型 IPO pipeline、扳機未擊發。
- **2000/3 頂點 15%**（1/8）：僅命中「扳機狀態 ≥ 初啟（已擊發）✓」；估值未達 ≥85、廣度未極窄、無 insider cluster、散戶未達 ≥65、貨幣未轉緊、dev200 未自 >10% 回落。
- **2021/12 Meme 頂 40%**（3/8）：命中「結構性槓桿 ≥65（75）✓、margin debt YoY ≥+40%（+53.7%）✓、CPI YoY ≥4%（4.17%）且 Fed 未實質緊縮 ✓」；未命中 散戶≥65、社群投機熱具名、流動性氾濫且 D5 自滿側、本週 moonshot≥1、廣度≥50。

**解讀**：當前週最像 1997 早期建設（廣度健康、capex 續增、公開信用利差仍窄），但估值溢價（79，含 ECY 近 0）已遠高於 1997 區間、且私募信貸 gate proration「已擊發」（1998 LTCM 型融資扳機，40%）——顯示週期位置是「高估值 + 健康廣度 + 非銀信用扳機初現」的**混合相位**，而非乾淨的建設早期。結構性槓桿以期別調整看（margin debt YoY +53.7%、槓桿 ETF/0DTE、AI 基建債務）與 2021/12 的槓桿特徵同框（40%）：位能（估值/槓桿）已高、但廣度尚廣、擴散未觸發，最該盯的是已擊發的非銀融資扳機是否外溢至公開利差。長期指數成長趨勢偏離參照（Dot-com ~95%、1929 ~110%、當前 AI 週期 ~147%，RIA/Farrell）僅作跨期敘事錨、非本週計分。

## 機構情緒對照

本次無新機構調查數據。（BofA Global Fund Manager Survey 最新為 6 月號，調查期 2026-06-05～06-11，早於前次基準 2026-07-02，非本次新增；當期顯示經理人加現金/債、減股票地產商品，但仍「steadfastly bullish」看成長，BofA 稱「非風險資產大頂、僅暑期收籌碼」，[Hedge Fund Tips](https://www.hedgefundtips.com/june-2026-bank-of-america-global-fund-manager-survey-results-summary/)。JPM 機構調查本次亦無新號。）

另按規格補充週頻 **NAAIM Exposure Index**：最新 84.69（@2026-07-01，[YCharts](https://ycharts.com/indicators/naaim_number)）——主動經理人曝險偏高＝擁擠多頭，作為反向 cross-check（Farrell #9），本值計於散戶情緒維度、於此僅敘述。

## 本次新增訊號

比較基準：vs 前次（4天前，report-2026-07-02）。

- **投機行為 −4（62→58）**：本週急性投機事件面全數轉靜——microcap moonshot 0 檔合格、無具名 +AI 改名/SPAC、IPO 無無營收暴衝、insider Form 4 合格叢集 0 件；量子/AI 銅板股背景熱度仍在但無單一單日 ≥100% 合格標的。
- **散戶情緒 −5（55→50）**：CNN F&G 轉 Fear（32）、AAII 多頭降至 31.4%（低於均值）——情緒面轉保守；惟 margin debt 5 月創 $1.42T（YoY +53.7%，頂部級別）、NAAIM 84.69、家庭持股 45.76% 高位，部位面仍 froth，故未大跌。
- **貨幣與信貸環境 +1（74→75；扳機側質化訊號）**：依 D5「雙向 Δ 遮蔽防護」——即使分數幾乎未動，本次落**扳機側**須列為質化新訊號：私募信貸 gate proration 持續（Blue Owl 兩檔 5% 上限依比例撥付、Q2 請求 $4.7B；BCRED Q2 ~10% 僅半數獲償），且 Fitch 報 4 月美國私募信貸違約率創 6% 新高——financing 壓力已觸及非銀信用。分數未大動，因公開 HY/IG OAS 仍極窄的自滿側先前已把 D5 撐在高位。
- **格局：穩定共存 → 不可判**：本次 script 未供三角訊號日序方向 delta（`decomposition` 無日序、`sp500_trend`/`DCOILWTICO` 無 chg），三者相位不可判、`regime` 記 不可判；此為資料可得性變動、非市場相位反轉。
- **全球槓桿擴散**：南韓單一個股槓桿 ETF 6 月熔斷、國會 07-06 啟動檢討為延續性背景；**本週無 2+ 非美市場新核准，本週擴散訊號未觸發**。
- **總分 −1（65→64）、等級 高 → 警戒**：主要由投機/散戶兩維下修帶動，落警戒/高邊界帶（±2）、屬噪音區，非趨勢性降溫。

## 數據附錄

**原始數據表**（每列一個計分用具體數據點）

| 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|
| S&P 500 Shiller CAPE | 39.46（multpl ~41.6） | FRED 非提供；GuruFocus / multpl.com | 2026-07-01 | 2026-07-06 09:18 CST |
| S&P 500 trailing P/E | 25.44（FactSet TTM ~27.8） | GuruFocus | 2026-07-02 | 2026-07-06 09:18 CST |
| Mag 7 加權前瞻 P/E | ~29× | Fortune | 2026-01（stock-of-state） | 2026-07-06 09:18 CST |
| S&P 500 距 200-DMA / 52wMA | +7.78% / +9.6% | FRED SP500（`sp500_trend`，script） | 2026-07-02 | 2026-07-06 script |
| Excess CAPE Yield | ~0.28%（derived） | 1/CAPE − DFII10/100 | 2026-07-02 | 2026-07-06 09:18 CST |
| RSP vs SPY YTD | +9.67% vs +8.38% | 24/7 Wall St. | 2026-06 中旬 | 2026-07-06 09:18 CST |
| Top-10 集中度 | 35.59%（HHI 185） | AhaSignals | 2026-04 | 2026-07-06 09:18 CST |
| A/D 廣度 | ~50% 個股 > 50-DMA（中性） | IndexMood | 2026-06-09 | 2026-07-06 09:18 CST |
| CNN Fear & Greed | 32（Fear） | MacroMicro / CNN | 2026-07-02 | 2026-07-06 09:18 CST |
| FINRA margin debt | $1.42T（MoM +8.5%、YoY +53.7%） | FINRA / Advisor Perspectives | 2026-05（月頻） | 2026-07-06 09:18 CST |
| AAII 多頭 | 31.4%（↓13.6pp） | AAII / SeekingAlpha | 2026-07 初 | 2026-07-06 09:18 CST |
| 家庭持股佔金融資產比 | 45.76% | FRED（series_id=BOGZ1FL153064486Q） | 2026-01-01（季頻） | 2026-07-06 script |
| NAAIM Exposure | 84.69 | YCharts / naaim.org | 2026-07-01 | 2026-07-06 09:18 CST |
| Fed funds（上/下限） | 3.75% / 3.50% | FRED（series_id=DFEDTARU / DFEDTARL） | 2026-07-05 | 2026-07-06 script |
| HY OAS | 2.75% | FRED（series_id=BAMLH0A0HYM2） | 2026-07-02 | 2026-07-06 script |
| IG OAS | 0.75% | FRED（series_id=BAMLC0A0CM） | 2026-07-02 | 2026-07-06 script |
| 10Y 名目殖利率 | 4.48% | FRED（series_id=DGS10） | 2026-07-01 | 2026-07-06 script |
| 10Y 實質殖利率 | 2.25% | FRED（series_id=DFII10） | 2026-07-01 | 2026-07-06 script |
| 10Y 損益平衡通膨 | 2.23% | FRED（series_id=T10YIE） | 2026-07-02 | 2026-07-06 script |
| WTI 原油 | $71.87 | FRED（series_id=DCOILWTICO） | 2026-06-29 | 2026-07-06 script |
| CPI YoY | 4.17% | FRED（series_id=CPIAUCSL，yoy） | 2026-05-01（月頻） | 2026-07-06 script |
| 5y5y forward 通膨預期 | 2.22% | FRED（series_id=T5YIFR） | 2026-07-02 | 2026-07-06 script |
| CME FedWatch（07-29 按兵） | 75.6% | CME Group | 2026-07-04 | 2026-07-06 09:18 CST |
| Fed 資產負債表 WALCL | $6,724,564M | FRED（series_id=WALCL） | 2026-07-01 | 2026-07-06 script |
| ECB 資產 | €6,117,260M | FRED（series_id=ECBASSETSW） | 2026-06-26 | 2026-07-06 script |
| BOJ 資產 | ¥639,550,900M | FRED（series_id=JPNASSETS） | 2026-06-01 | 2026-07-06 script |
| 私募信貸贖回壓力 | Blue Owl Q2 請求 $4.7B、5% 上限 proration；BCRED Q2 ~10% 半數獲償；Fitch 4 月違約率 6% | Benzinga / Alternatives Watch / PitchBook | 2026-07-02 揭露 | 2026-07-06 09:18 CST |
| Hyperscaler 2026 capex | 合計 $725B（+77%）；MSFT $190B / GOOGL ~$190B / AMZN ~$200B / META $115–135B | Tom's Hardware | 2026-Q1 指引（stock-of-state） | 2026-07-06 09:18 CST |
| OpenAI / Anthropic ARR | ~$24B / ~$30B | VentureBeat / Epoch AI | 2026-04 | 2026-07-06 09:18 CST |
| AI compute 供需 | H100 租金 +40%（→$2.35/hr）、產能售罄至 8–9 月、HBM 受限 | Thunder Compute / SemiAnalysis / TrendForce | 2026-07 | 2026-07-06 09:18 CST |
| 美國槓桿 ETF AUM | $198B（TQQQ $29–39B、SOXL $13–28B、NVDL +68% YTD）；ADV ~$45B（+50%） | CryptoBriefing / Goldman(SeekingAlpha) | 2026-H1 | 2026-07-06 09:18 CST |
| 0DTE 佔 SPX 量 | ~60–63%（2026-02 創 63%） | Cboe / IBKR | 2026-02～近月 | 2026-07-06 09:18 CST |
| VIX / SKEW | 15.81 / 150.02 | Cboe / Yahoo | 2026-07-02 | 2026-07-06 09:18 CST |
| AI 基建債務 | CoreWeave DDTL 4.0 $8.5B（03-31）/ 5.0 $3.1B（05-18）；Sharon AI $1.6B（06）；Nvidia GPU-backstop | SEC 8-K / MLQ | 2026-03～06 | 2026-07-06 09:18 CST |
| 南韓單一個股槓桿 ETF | 5 月底上市、6 月兩度熔斷、國會 07-06 檢討 | BigGo / Korea Herald | 2026-07-06 | 2026-07-06 09:18 CST |

**Coverage 覆蓋率表**（每列對應一個 `# Data sources` bullet；共 47 列）

| 維度 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|
| 估值：S&P 500 P/E + Shiller CAPE | multpl / GuruFocus [SEARCH] | ✓ SEARCH-VERIFIED |
| 估值：Mag 7 加權 P/E + AI leader P/S | 個股加權 vs 10 年均 | ✓ SEARCH-VERIFIED（Mag7 fwd ~29×，stock-of-state） |
| 估值：analyst TP upgrade decomposition | sell-side TP 拆解 [SEARCH，best-effort] | ✗ NOT DISCLOSED（14 日內無合格上修） |
| 估值：S&P 500 price-trend deviation | FRED SP500 → `sp500_trend`（script） | ✓ API（dev200 +7.78% / dev52w +9.6%） |
| 廣度：RSP vs SPY YTD divergence | ETF 比較 | ✓ SEARCH-VERIFIED |
| 廣度：Top-10 concentration | slickcharts / 研究 | ✓ SEARCH-VERIFIED |
| 廣度：A/D ratio + new high/low | 廣度指標 | ✓ SEARCH-VERIFIED |
| 散戶：CNN Fear & Greed | cnn.com [SEARCH] | ✓ SEARCH-VERIFIED（32 Fear） |
| 散戶：Margin Debt（FINRA） | FINRA 月頻 + YoY + /市值 | ✓ SEARCH-VERIFIED（$1.42T，+53.7% YoY） |
| 散戶：AAII 調查 | aaii.com [SEARCH] | ✓ SEARCH-VERIFIED（多頭 31.4%） |
| 散戶：Social sentiment proxies | Reddit/X [best-effort] | ✗ NOT DISCLOSED（無具名熱點） |
| 散戶：Household equity allocation | FRED BOGZ1FL153064486Q（script，季頻） | ✓ API（45.76%，2026-Q1） |
| 散戶：NAAIM Exposure Index | naaim/ycharts [SEARCH，best-effort] | ✓ SEARCH-VERIFIED（84.69） |
| 機構：BofA FMS + JPM 調查 | 月頻 [best-effort] | ✗ NOT DISCLOSED（前次後無新號） |
| 貨幣：Fed funds DFEDTARU/DFEDTARL | FRED（script） | ✓ API（3.75/3.50） |
| 貨幣：HY OAS BAMLH0A0HYM2 | FRED（script） | ✓ API（2.75%） |
| 貨幣：IG OAS BAMLC0A0CM | FRED（script） | ✓ API（0.75%） |
| 貨幣：10Y DGS10 | FRED（script） | ✓ API（4.48%） |
| 貨幣：10Y 實質 DFII10 | FRED（script） | ✓ API（2.25%） |
| 貨幣：10Y breakeven T10YIE | FRED（script） | ✓ API（2.23%，直抓非 derived） |
| 貨幣：WTI DCOILWTICO | FRED（script） | ✓ API（$71.87） |
| 貨幣：CPI YoY CPIAUCSL | FRED（script，月頻） | ✓ API（4.17%） |
| 貨幣：5y5y forward T5YIFR | FRED（script） | ✓ API（2.22%） |
| 貨幣：Fed funds path FedWatch | CME [SEARCH，best-effort] | ✓ SEARCH-VERIFIED（75.6% 按兵） |
| 貨幣：Fed 資產負債表 WALCL | FRED（script，週頻） | ✓ API（$6.7246T） |
| 貨幣：ECB/BOJ ECBASSETSW/JPNASSETS | FRED（script） | ✓ API（€6.117T / ¥639.55T×億） |
| 貨幣：PBoC aggregate financing | NBS/PBoC 英文摘要 [best-effort] | ✗ NOT DISCLOSED |
| 貨幣：私募信貸/非銀基金流動性壓力 | BDC/interval fund [SEARCH，best-effort] | ✓ SEARCH-VERIFIED（gate proration 已擊發） |
| AI：Hyperscaler capex guidance | MSFT/GOOGL/AMZN/META 季報（stock-of-state） | ✓ SEARCH-VERIFIED（$725B，+77%） |
| AI：AI token volume growth | Anthropic/OpenAI/Google 揭露 [best-effort] | ✗ NOT DISCLOSED |
| AI：OpenAI/Anthropic 營收 | The Information/Reuters [best-effort] | ✓ SEARCH-VERIFIED（$24B / $30B） |
| AI：Hyperscaler 客戶集中度 | 財報質化 [best-effort] | ✗ NOT DISCLOSED |
| AI：AI compute 供需/過剩 | GPU 租金/HBM/利用率 [SEARCH，best-effort] | ✓ SEARCH-VERIFIED（租金 +40%、售罄，無過剩） |
| 投機：+AI 改名/SPAC/無營收 IPO（7d） | 新聞掃描 | ✓ SEARCH-VERIFIED（0 件） |
| 投機：IPO 市場熱度 | IPO 日曆/首日/無營收佔比 | ✓ SEARCH-VERIFIED（溫和、無暴衝） |
| 投機：Microcap thematic moonshots | Finviz/Benzinga 掃描（required 週篩） | ✓ SEARCH-VERIFIED（0 件） |
| 投機：Upcoming AI IPOs | S-1/具名報導 [best-effort] | ✗ NOT DISCLOSED |
| 投機：Insider Form 4 clusters | SEC EDGAR [SEC EDGAR] | ✓ SEARCH-VERIFIED（0 件） |
| 投機：Cboe put/call ratio | Cboe/YCharts [SEARCH，best-effort] | ✗ NOT DISCLOSED |
| 結構：美國槓桿 ETF AUM | etf.com/ETFGI [SEARCH] | ✓ SEARCH-VERIFIED（$198B） |
| 結構：美國單一個股槓桿 ETF 核准 | SEC EDGAR/ETF.com | ✓ SEARCH-VERIFIED（0 件新核准） |
| 結構：全球槓桿產品核准 KRX/TWSE/JPX/ESMA | 各監管 [best-effort] | ✓ SEARCH-VERIFIED（南韓背景；本週擴散訊號未觸發） |
| 結構：0DTE option volume | Cboe/SpotGamma | ✓ SEARCH-VERIFIED（~60–63%） |
| 結構：Options total volume（OCC） | OCC 月報 | ✓ SEARCH-VERIFIED（Cboe 指數期權量創高為 proxy；OCC 月報未單獨取得） |
| 結構：VIX/SKEW/stock-bond corr | Cboe [同類合併，worst-case] | ✓ SEARCH-VERIFIED（VIX 15.81/SKEW 150.02；stock-bond corr 未單獨量化） |
| 結構：margin debt/市值 ratio（cross-ref） | 引散戶 margin debt，confirmation only | ✓ SEARCH-VERIFIED（引 margin debt +53.7% YoY） |
| 結構：AI 基建債務/vendor-financing | 30 日掃描 [SEARCH，best-effort] | ✓ SEARCH-VERIFIED（CoreWeave/Sharon AI/Nvidia backstop） |

**✓ SEARCH-VERIFIED traceability（非 0 件列）**

- CAPE/PE：query「Shiller CAPE ratio S&P 500 July 2026 multpl」「S&P 500 trailing PE July 2026」→ gurufocus.com/economic_indicators/56、/57、multpl.com；資料日 2026-07-01/02；抓取 2026-07-06 09:18 CST。
- RSP/SPY：query「RSP vs SPY YTD 2026 divergence」→ 247wallst.com（2026-06-10）；抓取 2026-07-06 09:18 CST。
- Top-10：query「S&P 500 top 10 concentration 2026」→ ahasignals.com/sp500-concentration-risk；資料 2026-04；抓取 09:18 CST。
- A/D：query「S&P 500 advance decline breadth July 2026」→ indexmood.com/breadth；資料 2026-06-09；抓取 09:18 CST。
- CNN F&G：query「CNN Fear Greed today July 2026」→ en.macromicro.me/charts/50108；資料 2026-07-02；抓取 09:18 CST。
- Margin debt：query「FINRA margin debt 2026 May」→ advisorperspectives.com/dshort（2026-06-24）、gurufocus 4264；資料月 2026-05；抓取 09:18 CST。
- AAII：query「AAII sentiment July 2026」→ seekingalpha.com/news/4609705；資料 2026-07 初；抓取 09:18 CST。
- NAAIM：query「NAAIM exposure index July 2026」→ ycharts.com/indicators/naaim_number；資料 2026-07-01；抓取 09:18 CST。
- FedWatch：query「CME FedWatch July 2026 FOMC」→ cmegroup.com FedWatch；資料 2026-07-04；抓取 09:18 CST。
- 私募信貸：query「private credit BCRED Blue Owl redemption July 2026」→ benzinga.com（2026-07）、alternativeswatch.com（2026-07-02）；抓取 09:18 CST。
- Hyperscaler capex：query「MSFT GOOGL AMZN META capex 2026 Q1」→ tomshardware.com big-tech AI spending；資料 2026-Q1 指引；抓取 09:18 CST。
- OpenAI/Anthropic：query「OpenAI Anthropic ARR 2026」→ venturebeat.com、epoch.ai；資料 2026-04；抓取 09:18 CST。
- AI compute：query「GPU H100 rental price utilization overcapacity 2026」→ thundercompute.com、semianalysis.com；資料 2026-07；抓取 09:18 CST。
- 槓桿 ETF AUM：query「leveraged ETF AUM NVDL TQQQ SOXL 2026」→ cryptobriefing.com、seekingalpha.com/news/4607458；資料 2026-H1；抓取 09:18 CST。
- 0DTE：query「0DTE share SPX volume 2026」→ cboe.com insights、interactivebrokers.com；資料 2026-02～近月；抓取 09:18 CST。
- VIX/SKEW：query「VIX SKEW today July 2026」→ cboe.com/us/indices SKEW、finance.yahoo.com/quote/%5EVIX；資料 2026-07-02；抓取 09:18 CST。
- AI 基建債務：query「CoreWeave neocloud debt financing June 2026」→ sec.gov 8-K、mlq.ai；資料 2026-03～06；抓取 09:18 CST。
- 南韓槓桿：query「single stock leveraged ETF Korea 2026」→ finance.biggo.com、koreaherald.com；資料 2026-07-06；抓取 09:18 CST。

**✓ SEARCH-VERIFIED（0 件）screens** — query、來源、timestamp（URL/發布日可為 —）：

- +AI 改名/SPAC（7d）：query「AI rename ticker change SPAC July 2026」「no-revenue speculative IPO surge」→ 檢查 Benzinga/MarketWatch movers、IPO 新聞；本週 0 件合格；抓取 2026-07-06 09:18 CST。
- Microcap moonshots（週篩）：query「biggest microcap gainers 100% single day quantum AI space late June July 2026」→ Finviz/Yahoo gainers/StockTwits；本週無單一單日 ≥100%、<$1B、2+ 主題、弱基本面且附 PR/8-K 之合格標的（量子/AI 銅板股背景熱但無合格單日事件）；抓取 09:18 CST。
- Insider Form 4 clusters（14d）：query「insider selling Form 4 cluster AI tech June July 2026 SEC」→ SEC EDGAR/GuruFocus insider；過去 14 日無附 filing/transaction 日期之合格叢集；抓取 09:18 CST。
- 美國單一個股槓桿 ETF 新核准（30d）：query「single stock leveraged ETF approval SEC EDGAR launch 2026」→ 本週無新核准/上市合格件；抓取 09:18 CST。

**方法/失敗註記**：本次 `scripts/fetch_macro.py` 回傳全序列 `status: ok`（FRED API），惟 `decomposition.status == unavailable_no_daily_history`，且 `sp500_trend`/`DCOILWTICO` 未附 `chg_pct`/`prior`——故 §3 三者「vs 前次」方向與 10Y 週 Δ 拆解本次不可用（不臆造 Δ），`regime` 記 不可判。金鑰全程未印出。

## 本次分數存檔
```json
{
  "date": "2026-07-06",
  "iso_week": "2026-W28",
  "weekday": "Monday",
  "timezone": "Asia/Taipei",
  "valuation": 79,
  "breadth": 30,
  "speculation": 58,
  "retail": 50,
  "monetary": 75,
  "structural": 75,
  "total": 64,
  "tier": "警戒",
  "regime": "不可判"
}
```

本報告為相對風險溫度計，非擇時訊報。
