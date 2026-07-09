# 2026-07-09 市場泡沫風險評估報告
> 報告日期：2026-07-09；執行日：2026-07-09 Asia/Taipei；ISO 週次：2026-W28；前次基準：report-2026-07-07（2天前）

**總評**：總分 64【警戒】（Δ 0）；扳機狀態：已擊發；最貼近錨點：1997 早期建設（50%）。

## §1 六維度風險條圖
| 維度 | 條圖 | 本次 | 前次 | Δ |
|---|---|---:|---:|---:|
| 估值溢價 | ▰▰▰▰▰▰▰▱▱▱ | 79 | 79 | 0 |
| 市場廣度 | ▰▰▰▱▱▱▱▱▱▱ | 30 | 30 | 0 |
| 投機行為 | ▰▰▰▰▰▱▱▱▱▱ | 58 | 58 | 0 |
| 散戶情緒 | ▰▰▰▰▰▱▱▱▱▱ | 50 | 50 | 0 |
| 貨幣與信貸環境 | ▰▰▰▰▰▰▰▱▱▱ | 75 | 75 | 0 |
| 結構性槓桿 | ▰▰▰▰▰▰▰▱▱▱ | 77 | 75 | +2 |
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
| S&P 500 | 7,482.71 | 持平（−0.28%，前次 \~7,503.85） |
| WTI 原油 | $69.6 /bbl | 持平（無新觀測） |
| 10Y Treasury | 4.55% | 持平（無新觀測） |

**三者狀態**：穩定共存——S&P 500 本次有新觀測（`sp500_trend.latest` 7,482.71，2026-07-08）但週變動僅 −0.28%（< 0.5% 門檻 → 持平）；WTI（`DCOILWTICO`，2026-07-06）與 10Y（`DGS10`，2026-07-07）本次 `no_new_obs`（持平、無新觀測）。三者無同向拉伸，`sp500_trend.dev200_pct` +7.57% 亦 < +10%（regime：穩定共存）：

- 股市：S&P 500 **7,482.71**（2026-07-08；距 200-DMA **+7.57%**、距 52 週 MA **+9.35%**，價格中度拉伸、200-DMA 偏離未達 +10%）；vs 前次 **持平**（−0.28%，前次 \~7,503.85）
- WTI 原油：**$69.6/bbl**（`DCOILWTICO`，2026-07-06，處相對低檔、非多月高點）；vs 前次 **持平**（無新觀測）
- 10Y 殖利率：**4.55%**（`DGS10`，2026-07-07）；本週無新觀測、週變動 0 bps，驅動因素無變動

**格局轉變**：前次 穩定共存 → 本次 穩定共存（前次 `regime` 讀自 report-2026-07-07 `score.json`＝穩定共存；本次依判定規則計算亦為 穩定共存——格局未轉變）。

**10Y 成因拆解**（週變動 Δ，bps）：本週 10Y 無新觀測（`decomposition.driver == "none"`，各項 Δ 皆 0）：
- ΔDFII10 實質殖利率週變動：**0 bps**（無新觀測；水位 2.30%，`DFII10`，2026-07-07）
- ΔT10YIE 損益平衡通膨週變動：**0 bps**（無新觀測；水位 2.25%，`T10YIE`，2026-07-08）
- 判定：**無變動（無新觀測）**（`ΔDGS10 ≈ ΔDFII10 + ΔT10YIE` 恆等於 0＋0；不以任何水位充當 Δ）

**扳機鏈**：
- **A 通膨鏈：油 → 通膨預期 → Fed 受限 → refinancing 成本**——「油」端未施壓：WTI $69.6 處相對低檔、非通膨推手；惟 **CPI YoY 4.17%**（`CPIAUCSL`，資料月 2026-05）仍在 ≥4% 高檔、**5y5y forward 2.19%**（`T5YIFR`，2026-07-08，週 Δ −3 bps）通膨預期溫和回落但未失錨，Fed 寬鬆空間受壓縮；CME FedWatch 顯示 2026-07-30 FOMC \~96.7% 按兵不動、2026 全年降息機率近零、6 月點陣圖年底中位上修至 3.8%（隱含偏緊）。本鏈的擊發並非來自油價，而是**非銀信用端**（見 B / 結論）。
- **B 槓桿鏈：衝擊（典型：財政風險再定價）→ NBFI 去槓桿 → margin spiral → 國債市場失序 → 官方市場功能回應**（BIS AER 2026 Ch II 傳導鏈；2025-04 swap-spread unwind 為原型）——**乾柴仍高、點火未現**：CFTC 槓桿基金美債期貨淨部位仍為 \~$1T 名目的紀錄級淨空倉（IMF 2026-04 GFSR 引 CFTC TFF，本週無新週度數字），惟 **MOVE \~65.76**（週 −5.3%，`move_index` script 端 `fetch_failed`、以 WebSearch 補）處低波動區、本週無基差／swap-spread 失序平倉披露；`repo_stress` 顯示 **SOFR−IORB −3 bps、SOFR99−IORB +6 bps、SRF 動用 $0**（`as_of` 2026-07-07）——funding 面平穩。10Y 本週零變動、無 real-rate 主導的異常上行，本鏈未見點火。惟本週 AI 信用端出現初步重定價（CoreWeave 高收益債走弱、CDS \~665 bp；Oracle CDS 走闊至 2009 年來最闊）——尚屬 AI 複合體內部分歧、未擴散至國債基差鏈，續盯。

⚠ **結論**：**扳機狀態：已擊發**——判定依「私募信貸 gate proration / breach」：Blackstone BCRED（\~$82B）2026-Q1 贖回請求達 NAV **7.9%（\~$3.7B）、超過 5% 季度贖回上限**，Blackstone 將上限上調至 7% 並對超額**依比例撥付（proration）**；Blue Owl 多檔非交易 BDC 啟動 tender offer 回應產業級贖回潮，Apollo、Ares 亦對非交易 BDC 設贖回上限（[HedgeCo](https://hedgeco.net/news/03/2026/the-liquidity-threshold-analyzing-the-3-7b-redemption-wave-at-blackstones-bcred.html)、[With Intelligence](https://withintelligence.com/insights/apollo-and-ares-cap-redemptions-for-non-traded-bdcs)）——實際 gate 撥付/超限＝1998 LTCM 型「融資扳機」特徵。歷史意義：公開市場利差（HY/IG OAS 2.67%/0.76%）仍近循環低點、極窄自滿，非銀信用先行承壓；本次更疊加 AI 複合體信用初步分歧（CoreWeave/Oracle CDS 走闊）——「froth 與扳機同框」的不穩定配置進一步固化。此標籤為 §2 checklist 與 D5 的共用輸入，不寫入 score.json。

## 六維度評分

### 1. 估值溢價 — 79（weight 22%，Δ 0）

- **S&P 500 Shiller CAPE** **41.64**（2026-07-08，[multpl](https://www.multpl.com/shiller-pe)；[GuruFocus](https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio) 月序 39.75，2026-07-01）——高於長期中位數 \~16 逾一倍、逼近 2000 年 \~44 的歷史極端區，絕對水位極端。
- **S&P 500 trailing P/E** **32.18**（2026-07-08，[multpl](https://www.multpl.com/s-p-500-pe-ratio)；GuruFocus 口徑較低 \~25.6）——本益比高檔，與 CAPE 同向。
- **Excess CAPE Yield（`ECY = 1/CAPE − DFII10/100`）** \~**0.10%**（derived：1/41.64 − 2.30/100；CAPE 39.75 則 \~0.22%）——逼近 0，屬 1929/2000 級別跨時代訊號；CAPE 高位十年裡實質利率（DFII10 2.30%）把它推向真正極端（confirmation，不主計分）。
- **Mag 7 加權 P/E** 前瞻 \~**28×**、trailing 籃 \~**40×**（2025-11～2026-05，[MarketXLS](https://marketxls.com/blog/magnificent-7-valuation-dashboard-excel-may-2026)、[Yardeni](https://yardeni.com/charts/magnificent-7/)）——龍頭估值仍溢價於自身後 2015 常態（低 20×），但未達群體歷史極端；精確 10 年加權均值免費源不可得（標註）。
- **價格趨勢偏離（Farrell #1/#2/#4）** S&P 500 距 200-DMA **+7.57%**、距 52 週 MA **+9.35%**（`sp500_trend`，FRED SP500，2026-07-08）——較前次（+8.49%/+10.31%）**微降**，均值回歸下行位能中等偏低；與 P/E/CAPE 互補、不重複計分。
- **AI 基本面 reality check**：hyperscaler capex 指引仍在上修（2026 合計 \~$650–725B、YoY +77%；MSFT \~$190B、GOOGL $180–190B、AMZN \~$200B、META $125–145B，[Tom's Hardware](https://www.tomshardware.com/tech-industry/big-tech/big-techs-ai-spending-plans-reach-725-billion)），Google token 量 3.2 quadrillion/月、YoY 7×（[CryptoBriefing](https://cryptobriefing.com/google-3-2-quadrillion-tokens-monthly)）——需求端仍旺；惟指引上修部分由記憶體漲價驅動（非純量增）。
- **AI compute 供需 reality check**：**訊號分歧**——GPU 租金自 2024-Q4 大跌 64–75%（H100 現 \~$1.87–2.49/hr，>300 家 neocloud 新進者，零售/neocloud 層有商品化過剩跡象），但上游記憶體急缺（TrendForce：2Q26 DRAM 合約價 +58–63% QoQ、NAND +70–75%，[TrendForce](https://www.trendforce.com/presscenter/news/20260601-13070.html)）——屬「後段價格壓力」而非乾淨的產能吸收；本項為估值風險上修的質化依據（缺口證據雙向、不單憑價格方向計分）。
- **資本週期階段 reality check**：**首現裂縫**——供給增速（top-4 capex +77%）遠超落地（16 GW 2026 美國管線僅 \~5 GW 動工、30–50% 專案傳延後/取消；Microsoft 凍結 \~1.5 GW 自建、AWS 延後部分租約，[SemiAnalysis](https://newsletter.semianalysis.com/p/microsofts-datacenter-freeze)、[DCD](https://www.datacenterdynamics.com/en/news/wells-fargo-amazon-web-services-delays-data-center-leases)）——資本週期由過熱段轉向邊際過剩的早期訊號、估值風險上修的質化依據。
- **AI 營收對 capex 缺口 reality check**：年化 AI 終端營收 \~**$100–150B**（OpenAI \~$25B ARR＋Anthropic \~$47B run-rate＋Microsoft AI \~$37B run-rate）對年化 AI capex \~**$450–580B**（分母：MSFT/GOOGL/AMZN/META＋Oracle 的 \~$650–775B 總 capex 中 AI 佔比 \~75%）——約 **3–5× 缺口**、且 capex 指引仍上修＝回本假設後移、估值對「未來需求兌現」依賴加深（質化上修依據；分母不含未追蹤來源）。
- **AI 信用定價分歧（equity-vs-credit schism）**：本週信貸端**開始重定價**——CoreWeave 高收益債走弱（[Bloomberg 2026-07-02](https://www.bloomberg.com/news/articles/2026-07-02/coreweave-junk-bonds-slide-further-as-investors-question-ai-boom)）、5yr CDS \~665–675 bp；Oracle 5yr CDS 走闊逾 125 bp、「2009 年來最闊」（[RealInvestmentAdvice](https://realinvestmentadvice.com/resources/blog/oracle-and-coreweave-cds-spreads-widening-omen-or-jitters/)），而 IG/超大型科技利差仍史低——信貸開始走闊而股價未跟＝Bulletin 120 意義下的**後期訊號**（confirmation，不主計分；缺值不調分）。
- **backlog 重複計算風險**：Oracle RPO **$638B**（Morgan Stanley 估 OpenAI \~2/3）、CoreWeave backlog $99B（\~40% 為 OpenAI），OpenAI 相關承諾 \~$330B 見於 MSFT/Oracle/CoreWeave 合計 \~$880B RPO——同一終端客戶承諾被多家供應商同時入帳、市場以加總 backlog 定價成長但可支付終端現金流只有一份（營收品質訊號；confirmation，不主計分）。
- **TP-upgrade phase signal**：本期具名合格上修 1 件——Goldman Sachs 調升 **AMD $450 → $640**（2026-07-05，[TheStreet](https://www.thestreet.com/investing/stocks/amd-advanced-micro-devices-inc-stock-price-target-goldman-sachs-july-2026)），理由為 agentic AI 帶動高效能 CPU 需求＝**EPS/需求修正驅動**（非 target-PE 擴張）——未見「多名跨標的的 multiple-driven 再評級」晚期特徵（confirmation，不主計分）。
- **折舊年限變動（盈餘品質）**：過去 30 日無新的伺服器/GPU 折舊年限變動披露（✗ NOT DISCLOSED，不納入計分；背景：MSFT/Google 4→6 年、Meta 4→5.5 年、Oracle 4→5→6 年為既有假設）。
- **結論**：估值裸值極端（CAPE 41.6、ECY \~0.1%）維持高位，價格拉伸微降（dev200 +7.57%）暫抵銷 AI 信用分歧、資本週期裂縫、3–5× 回本缺口等質化惡化；capex/token 需求仍撐頭部基本面，故維持 **79**（落 rubric 高緣、未達頂點級 85+）。

### 2. 市場廣度 — 30（weight 13%，Δ 0）

- **RSP（等權）vs SPY（市值權）YTD** +10.68% **領先** +7.47%（近月 RSP +2.49% vs SPY −0.08%，[24/7 Wall St.](https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/)）——廣度續呈擴散／健康、且領先幅度較前次（+9.67 vs +8.38）擴大。
- **S&P 500 個股 > 50-DMA 佔比** **\~67%**（2026-07-07，[Schwab](https://www.schwab.com/learn/story/stock-market-update-open)；tickeron 引 69%）——多數個股在中期均線之上、參與度健康，非少數權值扛盤。
- **Top-10 集中度** **\~35.6–37%**（2026-04，[AhaSignals](https://ahasignals.com/sp500-concentration-risk/)、[P&I](https://www.pionline.com/data-rankings/chart-of-the-day/pi-sp500-index-concentration/)）——已自 2025 年 \~40.7% 高峰回落但仍歷史偏高，龍頭同綁 AI 具相關性風險（資料 \~3 個月，取 35.6–37% 區間）。
- **結論**：RSP 領先擴大 + 67% 個股 > 50-DMA＝廣度健康，惟集中度仍歷史偏高；本週廣度無惡化，維持 **30**（落 rubric「21–40 輕微轉窄」偏低緣）。

### 3. 投機行為 — 58（weight 18%，Δ 0）

- **Microcap thematic moonshots** **0 檔合格**（✓ SEARCH-VERIFIED（0 件）；Finviz/Yahoo/StockTwits movers 掃描本週未見符合「單日 ≥100%、<$1B、2+ 疊加主題、弱基本面、附 PR/8-K URL」之單一標的；量子/核能銅板股背景熱度仍在，惟 OKLO/QUBT 等多 >$1B 且無合格單日事件）——「無營收暴衝」主指標本週靜。
- **+AI 改名 / SPAC / 無營收 IPO 暴衝** **2 件**（✓ SEARCH-VERIFIED；Envirotech Vehicles **EVTV** EV 殼股併 Azio AI 轉「AI datacenter」2026-07-02、[GlobeNewswire](https://www.globenewswire.com/news-release/2026/07/07/3323307/0/en/Envirotech-Vehicles-NASDAQ-EVTV-Closes-Merger-with-Azio-AI-Ahead-of-Schedule-Positioning-Combined-Company-to-Capture-487-Billion-2026-AI-Infrastructure-Opportunity.html)；K Wave Media→Talivar 全清 BTC 轉 AI/GPU 2026-07-01、[CoinDesk](https://www.coindesk.com/markets/2026/07/02/a-struggling-nasdaq-listed-company-that-tried-to-copy-saylor-s-bitcoin-playbook-is-completely-dumping-crypto-for-ai)——後者當日 −25% 屬去評價非暴衝）——改名投機再現，惟均為小殼股、非廣泛暴衝。
- **IPO 市場熱度**：本週活躍——Parabilis Medicines（**PBLS**）募 $670M、史上最大生技 IPO、首日 +50%（無營收癌症生技）；Bending Spoons 前週 +24%；YTD 193 檔（+7.22% YoY）；Q1 SPAC 62 檔募 >$11.8B（2021 年來最高，但偏有營收標的，[Renaissance Capital](https://www.renaissancecapital.com/IPO-Center/News)、[FTI](https://www.fticonsulting.com/insights/reports/ipo-spac-market-update-q1-2026)）——first-day pop 明顯、含無營收標的。
- **Upcoming AI IPO pipeline（liquidity-drain / 晚期訊號）**：OpenAI 保密 S-1（2026-06-09，\~$25B ARR、\~$852B 估值）、Anthropic 草擬 S-1（2026-06-01，\~$965B post-money）、SpaceX（SPCX）2026-07-07 納入 Nasdaq-100（\~$4.3B 被動流入，[CryptoBriefing](https://cryptobriefing.com/openai-anthropic-ipo-filings-spacex/)）——巨型 IPO pipeline 活躍，晚期流動性抽離背景（✓ SEARCH-VERIFIED）。
- **Insider Form 4 clusters（14 日）** **0 件合格**（✓ SEARCH-VERIFIED（0 件）；SEC EDGAR 主機本次 egress 403、無法取得第一手 filing URL；二手聚合器僅見單一 10b5-1 計劃性賣出 PLTR/Shyam Sankar 2026-07-02 $24.05M——非自主性叢集、且缺 EDGAR URL，依 Constraints 不列為計分具名claim；不構成合格叢集）。
- **OpenAI / Anthropic 營收軌跡**（集中度背景）：OpenAI \~$25B ARR（2026-02）、Anthropic \~$47B run-rate（2026-05，已超越 OpenAI）——強勁，屬敘事/集中度背景、非泡沫切點。
- **Cboe equity put/call ratio** **0.69**（2026-07-08；07-03 為 1.33、07-02 為 0.53，[YCharts](https://ycharts.com/indicators/cboe_equity_put_call_ratio)）——略低於 \~0.70「偏多」門檻、call 方向性投機溫和偏擁擠（confirmation only，缺值不調分）。
- **結論**：本週 +AI 改名再現 2 件、IPO first-day pop 明顯（PBLS +50%），惟 microcap moonshot 主指標仍 0、insider 無合格叢集——投機熱度質態未升，維持 **58**（落 rubric「41–60 投機升溫」偏上緣）。

### 4. 散戶情緒 — 50（weight 12%，Δ 0）

- **CNN Fear & Greed** **43（Fear）**（2026-07-08，[CNN](https://www.cnn.com/markets/fear-and-greed)，Benzinga 佐證）——較前次 32 回升 11 點、仍落 Fear 區、情緒面偏懼未轉貪。
- **AAII 多頭** **31.4%**、中性 26.4%、空頭 **42.3%**（週 2026-07-02，多空差 −10.9pp、多頭七週來第六次低於 37.5% 均值，[SeekingAlpha](https://seekingalpha.com/news/4609705-bullish-sentiment-falls-sharply-while-bearish-views-rise-aaii-survey-shows)）——散戶調查偏空（本週無新號、沿用最新一週）。
- **FINRA margin debt** 5 月 **$1.42T**、MoM +8.5%、**YoY +53.7%**、創歷史新高；淨信用餘額 **−$991.7B** 創低（[Advisor Perspectives](https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra)）——YoY ≥ +40–50% 屬 1999/2007/2021 頂部級別警訊，部位面 froth（月頻 stock-of-state，6 月數據約 7 月底發布）。
- **家庭持股佔金融資產比** **45.76%**（`BOGZ1FL153064486Q`，資料季 2026-Q1／2026-01-01）——接近歷史高位、後續加碼空間有限（Farrell #5，季頻、不計週 Δ）。
- **NAAIM Exposure** **84.69**（2026-07-01 週頻，前值 98.59／06-24 → 下滑，[YCharts](https://ycharts.com/indicators/naaim_number)）——主動經理人曝險仍偏高但轉降＝擁擠多頭略鬆（Farrell #9 confirmation cross-check，不主計分）。
- **Social sentiment proxies** ✓ SEARCH-VERIFIED——WSB 熱門為 NVDA/NBIS/AMZN 及太空股 ASTS/RKLB，屬 AI/太空長線題材、**無經典 meme 逼空**（[AltIndex](https://altindex.com/wallstreetbets)）——非 2021 式散戶投機熱，不上修主分。
- **結論**：情緒（F&G 43 Fear／AAII 空 42.3%）偏懼、部位（margin +53.7% YoY 創高／家庭 45.76%／NAAIM 84.69）滿倉，兩者續背離、淨值落中位；F&G 回升但仍 Fear、部位無新惡化，維持 **50**。

### 5. 貨幣與信貸環境 — 75（weight 20%，Δ 0；**扳機側**）

- **Fed funds 目標區間** **3.50–3.75%**（`DFEDTARU` 3.75／`DFEDTARL` 3.50，2026-07-08，Δ 0）——政策維持限制性。
- **Fed funds path（FedWatch）**：2026-07-30 FOMC \~96.7% 按兵不動、2026 全年降息機率近零、6 月點陣圖年底中位上修至 3.8%（隱含偏緊，best-effort，[CME FedWatch](https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html)；缺值不調分）。
- **HY OAS** **2.67%**（`BAMLH0A0HYM2`，2026-07-07，較前次 2.74% 微收）、**IG OAS** **0.76%**（`BAMLC0A0CM`，2026-07-07）——公開信用利差近循環低點、極窄（**自滿側**）。
- **CPI YoY** **4.17%**（`CPIAUCSL`，資料月 2026-05）、**5y5y forward** **2.19%**（`T5YIFR`，2026-07-08，週 Δ −3 bps）——實質通膨高檔、通膨預期溫和回落但未失錨，Fed 寬鬆空間受壓縮（扳機側證據）。
- **10Y 期限溢價（term premium）** **0.7322%**（`THREEFYTP10`，2026-07-02，週 Δ **+3.3 bps**，Kim-Wright 三因子模型、序列自身 trailing \~7d）——財政風險再定價溫和上行、未達急升，屬扳機側觀察但強度不足。
- **repo 資金壓力（SOFR−IORB）與 SRF 動用**：**SOFR−IORB −3 bps、SOFR99−IORB +6 bps、SRF 動用 $0**（`repo_stress`，`as_of` 2026-07-07）——secured-funding 面平穩、無官方流動性 backstop 異常動用（非扳機側）。
- **美債標售需求（auction tail / bid-to-cover）**：2026-07-08 10 年期標售 bid-to-cover **2.59**、需求穩健、無明顯 tail（[KuCoin/Reuters recap](https://www.kucoin.com/news/flash/us-treasury-10-year-note-auction-clears-at-4-58)）——財政供給壓力事件面未升溫（confirmation；缺值不調分）。
- **10Y 名目殖利率** **4.55%**（`DGS10`，2026-07-07；本週 Δ 0 bps、無新觀測）——refinancing 成本維持高檔。
- **Fed 資產負債表 WALCL** **$6.72T**（$6,724,564M，`WALCL`，2026-07-01）——量能持平。
- **ECB／BOJ 資產**（全球流動性 confirmation，非第七維度）：ECB **€5.98T**（€5,983,015M，`ECBASSETSW`，2026-07-03）、BOJ **¥639.55T**（¥6,395,509 億，`JPNASSETS`，2026-06-01）。
- **PBoC aggregate financing** ✗ NOT DISCLOSED（6 月金融統計排定 2026-07-14 發布、本次未及，best-effort）。
- **私募信貸贖回壓力（扳機側，已擊發）**：BCRED 2026-Q1 贖回請求 NAV **7.9%（\~$3.7B）超過 5% 上限、上調至 7% 並依比例撥付（gate proration）**；Blue Owl 多檔非交易 BDC 啟動 tender offer、Apollo/Ares 對非交易 BDC 設贖回上限（[HedgeCo](https://hedgeco.net/news/03/2026/the-liquidity-threshold-analyzing-the-3-7b-redemption-wave-at-blackstones-bcred.html)、[With Intelligence](https://withintelligence.com/insights/apollo-and-ares-cap-redemptions-for-non-traded-bdcs)）——多基金 redemption 潮＋實際 gate 撥付/超限＝一般宏觀/非銀信用扳機已擊發；與 D6 的 AI 基建私募信貸分開、不重複計分。
- **結論（扳機側）**：確認的 gate proration/超限 financing 壓力，與極窄公開 HY/IG OAS 的自滿並存，雙向皆推高分數；term premium 溫和上行、repo 面平穩、公開利差微收——扳機側較前次更確認但強度未升級，維持 **75**。判分側別：**扳機側**（financing 壓力已擊發）。

### 6. 結構性槓桿 — 77（weight 15%，Δ +2）

- **美國槓桿 ETF AUM**：TQQQ **\~$37–40B**、SOXL \~$14–22B、TSLL $4.37B、NVDL \~$3.7–4.4B（NVDL 近 12 個月淨流出 \~−$3.7B）、SQQQ $1.94B、CONL \~$550M（2026-07-08，[Morningstar](https://www.morningstar.com/etfs/xnas/nvdl/quote)、[etfdb](https://etfdb.com/etf/TQQQ/)）——量能仍高但單一個股多頭產品（NVDL/SQQQ）呈流出、非一致加速。
- **美國單一個股槓桿 ETF 新上市（30 日）**：**多起**——SpaceX IPO 帶動 10 檔槓桿 ETF（2026-06-15）、Tradr 5 檔 2x（CIEN/QNT/RMBS/TSEM/TTMI，2026-07-01）、Leverage Shares 6 檔大型科技 2x（2026-07-07）、Micron 記憶體槓桿 ETF（[etfdb](https://etfdb.com/news/2026/06/15/10-spacex-etfs-launch-spcx-arrives/)、[PRNewswire](https://www.prnewswire.com/news-releases/tradr-to-launch-leveraged-etfs-302811176.html)）——槓桿產品在美續擴散（美國仍 2x 上限、SEC 擋 3x+）。
- **0DTE 佔 SPX 量** **\~60–63%**（2026-02 創 63%；2026-Q2 SPX 0DTE ADV 3.1M/總 5.1M ≈ 61% 創高，2026-06 SPX 0DTE ADV 3.3M 創月紀錄，[Cboe](https://www.cboe.com/insights/posts/)）——落 rubric「55–65%」高緣。
- **Options total volume（OCC 月報）**：OCC 6 月總量頁本次 403 未取得（4 月 1,446,072,023 口、+13.9% YoY 為最近清晰讀數）；以 Cboe 6 月綜合 ADV **23.0M 創月紀錄**、產業 YTD ADV \~69.9M（+38.2% YoY）為 proxy（✓ SEARCH-VERIFIED，proxy）——選擇權量能創高。
- **VIX / SKEW** **16.13 / 145.38**（VIX 2026-07-08，期限結構 contango；SKEW 2026-07-06 收，07-03 曾 150.02，[Yahoo ^VIX](https://finance.yahoo.com/quote/%5EVIX/)、[Cboe SKEW](https://www.cboe.com/us/indices/dashboard/skew/)）——低波動＋高尾部避險溢價，交叉資產自滿；stock-bond 相關處負轉正過渡期（Oxford/IMF，60/40 分散保護下降，confirmation；未單獨量化）。
- **margin debt / 市值 ratio（cross-ref）**：引散戶 margin debt +53.7% YoY 作 confirmation，不在此重複計分。
- **AI 基建債務融資 / vendor-financing loops**：**本月多起新披露**——Nvidia GPU「backstop」revenue-share 循環融資模式（2026-07-01，Sharon AI/Firmus，最多 210k GB GPU，延伸 CoreWeave $6.3B 未售產能保證，[MLQ](https://mlq.ai/news/)）、Sharon AI $1.6B 配售（$900M 股權＋$700M 4.75% 可轉債，2026-06-17/29，綁 Nvidia 六年合作）、SpaceX $20–25B 首發債（2026-06-22，再融資 xAI/Colossus 橋貸，[CNBC](https://www.cnbc.com/2026/06/23/spacex-debt-bond-market-ipo.html)）、CoreWeave $1.25B 9.625%＋€2B 8.500% 優先票據（2026-06-11）、Blue Owl $975M 資料中心再融資（2026-06-08）——collateral-light／circular 特徵密集，且 **CoreWeave 高收益債本週續走弱、CDS \~665 bp**（[Bloomberg](https://www.bloomberg.com/news/articles/2026-07-02/coreweave-junk-bonds-slide-further-as-investors-question-ai-boom)）＝AI 基建債務初現再融資/擔保品敏感度惡化——屬 D6 結構性槓桿上修依據（本次 +2 主因）。
- **銀行對 NBFI 放款** **$1.99T**（$1,988.9B，`LNFACBW027SBOG`，2026-06-24，本週無新觀測）——bank–NBFI linkage 水位偏高但週趨勢持平（BIS AER Ch II 外溢管道 confirmation，不主計分）。
- **全球槓桿產品擴散**：南韓單一個股槓桿 ETF（4 月核准、5 月上市、7-07 跌破發行價、監管檢討）為延續性背景；台/日/歐本週均無新單一個股槓桿核准。**本週無 2+ 非美市場新核准 → 本週擴散訊號未觸發**（Special rule 樓地板 81 不啟動）。
- **美債基差交易槓桿** ✓ SEARCH-VERIFIED——CFTC 槓桿基金美債期貨淨空倉 \~$1T 名目紀錄級（乾柴高，IMF 2026-04 GFSR 引 CFTC TFF；本週無新週度數字，script `cftc_lev_funds` `fetch_failed`）、MOVE \~65.76（週 −5.3%，低波動）、本週無基差/swap-spread 失序平倉披露——正常讀數、屬 confirmation/背景，不因缺當週明細調分。
- **結論**：0DTE 創高 ADV + 選擇權量創月紀錄 + 槓桿產品續擴散維持高檔；本次因 **AI 基建 circular 融資本月密集（Nvidia backstop、Sharon AI、SpaceX xAI 再融資、CoreWeave 高收益債走弱）＝再融資/擔保品敏感度初現惡化**，落 rubric「61–80 加速」偏上，自 75 上修至 **77**；惟無國債市場失序、擴散訊號未觸發，未進 81+ 極端帶。

## 綜合分數

| 維度 | 分數 | 權重 | 加權 |
|---|---:|---:|---:|
| 估值溢價 | 79 | 22% | 17.38 |
| 市場廣度 | 30 | 13% | 3.90 |
| 投機行為 | 58 | 18% | 10.44 |
| 散戶情緒 | 50 | 12% | 6.00 |
| 貨幣與信貸環境 | 75 | 20% | 15.00 |
| 結構性槓桿 | 77 | 15% | 11.55 |
| **加權總分** |  | **100%** | **64.27 → 64** |

加權總分 64.27，half-up 四捨五入 → **64**；依風險等級對照表（40–64＝警戒）判定 **等級：警戒**。
邊界帶：總分 64 距 警戒/高 邊界 ≤ 2 分，評分固有噪音約 ±2–3，等級判讀需保留餘地。

## 歷史泡沫週期對比

相似度計算：checklist v2

本週最貼近（同分取表列在前者）**1997 早期建設（50%）**，與 **1998 LTCM 衝擊（50%）** 並列——反映「高估值 + 健康廣度 + 非銀信用扳機已擊發」的混合相位。最貼近錨點全項命中明細：

- **1997 早期建設 50%（4/8）**：命中「市場廣度 < 45（30）✓、hyperscaler capex 續上修 ✓、散戶情緒 < 55（50）✓、HY OAS < 4% 且未走闊（2.67%，微收）✓」；未命中「估值溢價 40–74（本次 79 過高）✗、投機行為 < 50（58）✗、結構性槓桿 < 50（77）✗、扳機狀態＝未擊發（本次已擊發）✗」。
- **1998 LTCM 衝擊 50%（4/8）**：命中「具名非銀/槓桿機構壓力披露（BCRED gate proration/超限）✓、估值溢價 ≥60（79）✓、扳機狀態 ≥ 初啟（已擊發）✓、ΔT10YIE ≤ 0（本週 0 bps，通膨預期非主因）✓」；未命中 HY OAS 週Δ≥+30bps 或 VIX>25（VIX 16.13、HY 微收）✗、S&P 回檔 ≥5%（−0.28%）✗、Fed 轉鴿（按兵不動、偏緊）✗、市場廣度 Δ≥+8（Δ 0）✗。
- **1999 晚期狂熱 40%（4/10）**：命中「估值溢價 ≥75（79）✓、CAPE ≥38（41.64）✓、結構性槓桿 ≥60（77）✓、巨型 IPO pipeline 活躍（OpenAI/Anthropic 06 月 S-1、SpaceX 07-07 納 Nasdaq-100）✓」；未命中 投機≥60（58）、moonshot≥1 或無營收 IPO 佔比偏高（moonshot 0）、廣度≥45（30）、D5 自滿側且 HY<3.5%（本次扳機側）、散戶≥55（50）、扳機未擊發（已擊發）。
- **2000/3 頂點 15%（1/8）**：僅命中「扳機狀態 ≥ 初啟（已擊發）✓」；估值未達 ≥85（79）、廣度未極窄（30）、無 insider cluster（0）、散戶未達 ≥65（50）、貨幣未轉緊（按兵不動）、dev200 未自 >10% 回落（+7.57%）、投機未達 ≥70。
- **2021/12 Meme 頂 40%（3/8）**：命中「結構性槓桿 ≥65（77）✓、margin debt YoY ≥+40%（+53.7%）✓、CPI YoY ≥4%（4.17%）且 Fed 未實質緊縮 ✓」；未命中 散戶≥65（50）、社群投機熱具名 meme 逼空（無、僅 AI/太空長線題材）、流動性氾濫且 D5 自滿側（本次扳機側）、本週 moonshot≥1（0）、廣度≥50（30）。

**解讀**：當前週最像 1997 早期建設（廣度健康、capex 續增、公開信用利差仍窄），但估值溢價（79、ECY \~0.1%）已遠高於 1997 區間，且 BCRED gate proration「已擊發」使 1998 LTCM 型融資扳機同分並列（50%）——週期位置是「高估值 + 健康廣度 + 非銀信用扳機已現」的**混合相位**，而非乾淨的建設早期。以期別調整看結構性槓桿（margin debt YoY +53.7%、0DTE 60–63%、AI 基建 circular 債務本月密集）與 2021/12 槓桿特徵同框（40%），且本週新增 AI 信用分歧（CoreWeave/Oracle CDS 走闊）與資本週期裂縫（資料中心專案延後）——位能（估值/槓桿）已高、廣度尚廣、擴散未觸發，最該盯的是已擊發的非銀融資扳機與初現的 AI 信用重定價是否外溢至公開利差。長期指數成長趨勢偏離參照（Dot-com \~95%、1929 \~110%、當前 AI 週期 \~147%，RIA/Farrell）僅作跨期敘事錨、非本週計分；BIS AER 2026 Ch I 光纖/vendor-financing 結構類比（vendor-financing loops、backlog 重複計算、資本週期）本週在 Nvidia backstop 循環融資與 Oracle RPO $638B 重複入帳上得到新佐證。

## 機構情緒對照

本次無新機構調查數據。（BofA Global Fund Manager Survey 最新為 6 月號「The Great De-Risking」，調查期早於前次基準：現金水位升至 4.3%（自 5 月 3.9%）、股票淨加碼降至 \~37%、商品淨加碼 \~34% 為 2022-04 來最高、63% 視私募股權/私募信貸為最可能系統性風險源；JPM 機構調查本次亦無新號。）

另按規格補充週頻 **NAAIM Exposure Index**：最新 **84.69**（2026-07-01，前值 98.59／06-24 → 下滑，[YCharts](https://ycharts.com/indicators/naaim_number)）——主動經理人曝險仍偏高但轉降＝擁擠多頭略鬆，作為反向 cross-check（Farrell #9）；本值計於散戶情緒維度、於此僅敘述。

## 本次新增訊號

比較基準：vs 前次（2天前，report-2026-07-07）。本次僅 **結構性槓桿 +2（75→77）**，其餘五維度與加權總分持平（Δ 0）——2 天間隔、macro 多序列 `no_new_obs`，惟本週出現數項質化升級，列示如下：

- **結構性槓桿（+2）— AI 基建 circular 融資本月密集**：Nvidia GPU backstop revenue-share 模式（2026-07-01，Sharon AI/Firmus，最多 210k GPU）、Sharon AI $1.6B（$700M 可轉債）、SpaceX $20–25B 首發債（再融資 xAI/Colossus 橋貸）、CoreWeave $1.25B+€2B 高收益票據——collateral-light/circular 特徵密集，且 CoreWeave 高收益債本週續走弱（CDS \~665 bp）＝再融資/擔保品敏感度初現惡化，D6 自 75 上修至 77。
- **估值溢價（Δ 0）— AI 信用定價分歧初現（後期訊號）**：CoreWeave 高收益債走弱、5yr CDS \~665 bp；Oracle 5yr CDS 走闊逾 125 bp「2009 年來最闊」，而 IG/超大型科技利差仍史低——信貸端開始對 AI 風險重定價而股價未跟＝Bulletin 120 意義下的後期訊號；屬 D1 confirmation，價格拉伸微降抵銷、分數未動。
- **估值溢價（Δ 0）— 資本週期首現裂縫**：16 GW 2026 美國資料中心管線僅 \~5 GW 動工、30–50% 專案傳延後/取消，Microsoft 凍結 \~1.5 GW、AWS 延後租約——供給增速遠超落地、資本週期由過熱轉向邊際過剩早期；capex 指引仍上修，故 D1 未動、列為質化惡化。
- **貨幣與信貸環境（D5，扳機側質化訊號）**：依「雙向 Δ 遮蔽防護」——即使分數未動，本次仍落**扳機側**且較前次更確認：BCRED 2026-Q1 贖回 7.9% 超 5% 上限、上調至 7% 並依比例撥付（實際 gate proration/超限）；Blue Owl tender offer、Apollo/Ares 設上限。分數未動因公開 HY/IG OAS 極窄的自滿側先前已把 D5 撐在高位。
- **投機行為（Δ 0）— +AI 改名再現 2 件**：EVTV（EV 殼股併 Azio AI）、K Wave→Talivar（清 BTC 轉 AI/GPU）——改名投機自前次 0 件回升至 2 件；惟 microcap moonshot 主指標仍 0、insider 無合格叢集，故投機分數維持 58。
- **投機行為（Δ 0）— analyst TP 上修具名化**：Goldman 調升 AMD $450→$640（EPS/需求驅動、非 multiple 擴張）——本次由 ✗ 升級為具名 ✓，但屬 EPS 驅動、非晚期 multiple 再評級。
- **§2 錨點**：與前次一致——最貼近 1997（50%）與 1998（50%）並列（取表列在前者 1997）；1999、2021 各 40%、2000/3 15%，本週 checklist 命中無變化。
- **全球槓桿擴散**：南韓單一個股槓桿 ETF 上市後爭議為延續性背景；**本週無 2+ 非美市場新核准，本週擴散訊號未觸發**。

## 數據附錄

**原始數據表**（每列一個計分用具體數據點）

| 指標 | 數值 | 來源（FRED series ID / URL）| 資料日期 | 抓取 timestamp |
|---|---|---|---|---|
| S&P 500 Shiller CAPE | 41.64（GuruFocus 月序 39.75） | multpl.com / GuruFocus | 2026-07-08 / 07-01 | 2026-07-09 09:30 CST |
| S&P 500 trailing P/E | 32.18（GuruFocus 口徑 \~25.6） | multpl.com | 2026-07-08 | 2026-07-09 09:30 CST |
| Mag 7 加權 P/E | 前瞻 \~28× / trailing 籃 \~40× | MarketXLS / Yardeni | 2025-11～2026-05（stock-of-state） | 2026-07-09 09:30 CST |
| Excess CAPE Yield | \~0.10%（derived） | 1/CAPE − DFII10/100 | 2026-07-08 | 2026-07-09 09:30 CST |
| S&P 500 距 200-DMA / 52wMA | +7.57% / +9.35% | FRED SP500（`sp500_trend`，script） | 2026-07-08 | 2026-07-09 script |
| S&P 500 spot | 7,482.71（前次 7,503.85，−0.28%） | FRED SP500（`sp500_trend`，script） | 2026-07-08 | 2026-07-09 script |
| Goldman AMD TP 上修 | $450 → $640（EPS 驅動） | TheStreet | 2026-07-05 | 2026-07-09 09:30 CST |
| AI 信用分歧 CoreWeave CDS | 5yr \~665–675 bp；高收益債走弱 | Bloomberg / RealInvestmentAdvice | 2026-07-02 | 2026-07-09 09:30 CST |
| AI 信用分歧 Oracle CDS | 5yr 逾 125 bp（2009 來最闊） | Investing.com / RealInvestmentAdvice | 2026-07 初 | 2026-07-09 09:30 CST |
| RSP vs SPY YTD | +10.68% vs +7.47% | 24/7 Wall St. | 2026-06 中旬～07 | 2026-07-09 09:30 CST |
| S&P 500 個股 > 50-DMA | \~67% | Schwab / tickeron | 2026-07-07 | 2026-07-09 09:30 CST |
| Top-10 集中度 | \~35.6–37% | AhaSignals / P&I | 2026-04 | 2026-07-09 09:30 CST |
| CNN Fear & Greed | 43（Fear） | CNN / Benzinga | 2026-07-08 | 2026-07-09 09:30 CST |
| FINRA margin debt | $1.42T（MoM +8.5%、YoY +53.7%、創高；淨信用 −$991.7B） | FINRA / Advisor Perspectives | 2026-05（月頻） | 2026-07-09 09:30 CST |
| AAII 多頭/空頭 | 31.4% / 42.3%（差 −10.9pp） | AAII / SeekingAlpha | 2026-07-02 | 2026-07-09 09:30 CST |
| 家庭持股佔金融資產比 | 45.76% | FRED（series_id=BOGZ1FL153064486Q） | 2026-01-01（季頻 2026-Q1） | 2026-07-09 script |
| NAAIM Exposure | 84.69（前值 98.59） | YCharts / naaim.org | 2026-07-01 | 2026-07-09 09:30 CST |
| Fed funds（上/下限） | 3.75% / 3.50% | FRED（series_id=DFEDTARU / DFEDTARL） | 2026-07-08 | 2026-07-09 script |
| HY OAS | 2.67% | FRED（series_id=BAMLH0A0HYM2） | 2026-07-07 | 2026-07-09 script |
| IG OAS | 0.76% | FRED（series_id=BAMLC0A0CM） | 2026-07-07 | 2026-07-09 script |
| 10Y 名目殖利率 | 4.55% | FRED（series_id=DGS10） | 2026-07-07 | 2026-07-09 script |
| 10Y 實質殖利率 | 2.30% | FRED（series_id=DFII10） | 2026-07-07 | 2026-07-09 script |
| 10Y 損益平衡通膨 | 2.25% | FRED（series_id=T10YIE） | 2026-07-08 | 2026-07-09 script |
| WTI 原油 | $69.6 | FRED（series_id=DCOILWTICO） | 2026-07-06 | 2026-07-09 script |
| CPI YoY | 4.17% | FRED（series_id=CPIAUCSL，yoy） | 2026-05-01（月頻） | 2026-07-09 script |
| 5y5y forward 通膨預期 | 2.19%（週 Δ −3 bps） | FRED（series_id=T5YIFR） | 2026-07-08 | 2026-07-09 script |
| 10Y 期限溢價 | 0.7322%（週 Δ +3.3 bps，trailing 7d） | FRED（series_id=THREEFYTP10，Kim-Wright） | 2026-07-02 | 2026-07-09 script |
| repo 資金壓力 | SOFR−IORB −3 bps；SOFR99−IORB +6 bps；SRF $0 | FRED（SOFR/SOFR99/IORB/RPONTTLD，`repo_stress`） | 2026-07-07 | 2026-07-09 script |
| 美債標售需求（10yr） | bid-to-cover 2.59、無明顯 tail | US Treasury / Reuters recap | 2026-07-08 | 2026-07-09 09:30 CST |
| CME FedWatch（07-30 按兵） | \~96.7% hold、2026 降息近零、點陣 3.8% | CME Group | 2026-07 初 | 2026-07-09 09:30 CST |
| Fed 資產負債表 WALCL | $6,724,564M（$6.72T） | FRED（series_id=WALCL） | 2026-07-01 | 2026-07-09 script |
| ECB 資產 | €5,983,015M（€5.98T） | FRED（series_id=ECBASSETSW） | 2026-07-03 | 2026-07-09 script |
| BOJ 資產 | ¥6,395,509 億（¥639.55T） | FRED（series_id=JPNASSETS） | 2026-06-01 | 2026-07-09 script |
| 私募信貸贖回壓力 | BCRED 7.9% 超 5% 上限、上調 7% 依比例撥付；Blue Owl/Apollo/Ares 設限 | HedgeCo / With Intelligence | 2026-Q1 揭露 | 2026-07-09 09:30 CST |
| Hyperscaler 2026 capex | \~$650–725B（+77%）；MSFT \~$190B / GOOGL $180–190B / AMZN \~$200B / META $125–145B | Tom's Hardware | 2026-Q1 指引（stock-of-state） | 2026-07-09 09:30 CST |
| AI token 量（Google） | 3.2 quadrillion/月（YoY 7×） | CryptoBriefing / DCD | 2026-05～06 | 2026-07-09 09:30 CST |
| OpenAI / Anthropic 營收 | \~$25B ARR / \~$47B run-rate | Sacra / valueaddvc | 2026-02 / 2026-05 | 2026-07-09 09:30 CST |
| customer concentration / RPO | Oracle RPO $638B（OpenAI \~2/3）；CoreWeave backlog $99B；OpenAI \~$330B/$880B | Morgan Stanley / Fool | 2026-07 初 | 2026-07-09 09:30 CST |
| AI compute 供需 | GPU 租金 −64–75%；DRAM 合約 +58–63% QoQ | intuitionlabs / TrendForce | 2026-Q2 | 2026-07-09 09:30 CST |
| Hyperscaler 融資結構 | capex>FCF（Oracle 86% capex/rev、BBB）；債發 Oracle $25B/Alphabet $20B/Amazon $54B；BofA 2026 issuance $175B | CreditSights / Qz / Fortune | 2026-02～03 | 2026-07-09 09:30 CST |
| AI 營收對 capex 缺口 | \~$100–150B 營收 vs \~$450–580B AI capex（3–5×；分母 MSFT/GOOGL/AMZN/META＋Oracle） | 綜合（items 1/3/6） | 2026-02～05 | 2026-07-09 09:30 CST |
| 資本週期階段 | 16GW 管線僅 \~5GW 動工、30–50% 延後；MSFT 凍 1.5GW、AWS 延租 | SemiAnalysis / DCD | 2026-06～07 | 2026-07-09 09:30 CST |
| +AI 改名 | EVTV（Azio AI）07-02；K Wave→Talivar 07-01 | GlobeNewswire / CoinDesk | 2026-07-01～02 | 2026-07-09 09:30 CST |
| IPO 熱度 | PBLS $670M 首日 +50%（無營收）；YTD 193（+7.22%）；Q1 SPAC 62 檔 | Renaissance / FTI | 2026-07 初 | 2026-07-09 09:30 CST |
| Upcoming AI IPO | OpenAI S-1 06-09、Anthropic S-1 06-01、SpaceX 07-07 納 Nasdaq-100 | CryptoBriefing / INDmoney | 2026-06～07 | 2026-07-09 09:30 CST |
| insider（非合格） | PLTR/Sankar 10b5-1 $24.05M（單一計劃性、缺 EDGAR URL、不計分） | StockTitan / Investing.com | 2026-07-02 | 2026-07-09 09:30 CST |
| Cboe equity put/call | 0.69 | YCharts / Cboe | 2026-07-08 | 2026-07-09 09:30 CST |
| 美國槓桿 ETF AUM | TQQQ \~$37–40B、SOXL \~$14–22B、TSLL $4.37B、NVDL \~$4B（流出）、SQQQ $1.94B、CONL \~$550M | Morningstar / etfdb | 2026-07-08 | 2026-07-09 09:30 CST |
| 美國單一個股槓桿 ETF 新上市 | SpaceX 10 檔(06-15)、Tradr 5 檔(07-01)、Leverage Shares 6 檔(07-07)、Micron | etfdb / PRNewswire | 2026-06～07 | 2026-07-09 09:30 CST |
| 0DTE 佔 SPX 量 | \~60–63%（Q2 ADV 3.1M/5.1M ≈ 61%） | Cboe | 2026-Q2 | 2026-07-09 09:30 CST |
| Options total volume | Cboe 6 月綜合 ADV 23.0M 創高；產業 YTD ADV \~69.9M（OCC 4 月 1.446B） | Cboe / OCC / MIAX | 2026-06 | 2026-07-09 09:30 CST |
| VIX / SKEW | 16.13（contango）/ 145.38 | Yahoo / Cboe | 2026-07-08 / 07-06 | 2026-07-09 09:30 CST |
| AI 基建債務 | Nvidia backstop(07-01)、Sharon AI $1.6B(06-17)、SpaceX $20–25B(06-22)、CoreWeave $1.25B+€2B(06-11)、Blue Owl $975M(06-08) | MLQ / Businesswire / CNBC | 2026-06～07 | 2026-07-09 09:30 CST |
| 銀行對 NBFI 放款 | $1,988.9B（$1.99T） | FRED（series_id=LNFACBW027SBOG） | 2026-06-24 | 2026-07-09 script |
| 美債基差交易槓桿 | 槓桿基金淨空倉 \~$1T（紀錄級）；MOVE \~65.76（週 −5.3%） | IMF GFSR / MacroMicro | 2026-04 / 07-08 | 2026-07-09 09:30 CST |

**Coverage 覆蓋率表**（每列對應一個 `# Data sources` bullet；共 57 列）

| 維度 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|
| 估值：S&P 500 P/E + Shiller CAPE | multpl / GuruFocus [SEARCH] | ✓ SEARCH-VERIFIED（CAPE 41.64 / PE 32.18） |
| 估值：Mag 7 加權 P/E + AI leader P/S | 個股加權 vs 10 年均 | ✓ SEARCH-VERIFIED（前瞻 \~28× / trailing 籃 \~40×；10yr 均值未確認） |
| 估值：analyst TP upgrade decomposition | sell-side TP 拆解 [SEARCH，best-effort] | ✓ SEARCH-VERIFIED（Goldman AMD $450→$640，EPS 驅動） |
| 估值：S&P 500 price-trend deviation | FRED SP500 → `sp500_trend`（script） | ✓ API（dev200 +7.57% / dev52w +9.35%） |
| 估值：AI 信用定價分歧（schism） | 信貸/CDS 掃描 [SEARCH，best-effort] | ✓ SEARCH-VERIFIED（CoreWeave CDS \~665bp、Oracle 2009 來最闊） |
| 廣度：RSP vs SPY YTD divergence | ETF 比較 | ✓ SEARCH-VERIFIED（+10.68% vs +7.47%） |
| 廣度：Top-10 concentration | slickcharts / 研究 | ✓ SEARCH-VERIFIED（\~35.6–37%） |
| 廣度：A/D ratio + new high/low | 廣度指標 | ✓ SEARCH-VERIFIED（\~67% 個股 > 50-DMA） |
| 散戶：CNN Fear & Greed | cnn.com [SEARCH] | ✓ SEARCH-VERIFIED（43 Fear） |
| 散戶：Margin Debt（FINRA） | FINRA 月頻 + YoY + /市值 | ✓ SEARCH-VERIFIED（$1.42T，+53.7% YoY，創高） |
| 散戶：AAII 調查 | aaii.com [SEARCH] | ✓ SEARCH-VERIFIED（多頭 31.4%／空 42.3%） |
| 散戶：Social sentiment proxies | Reddit/X [best-effort] | ✓ SEARCH-VERIFIED（WSB NVDA/ASTS/RKLB，無 meme 逼空） |
| 散戶：Household equity allocation | FRED BOGZ1FL153064486Q（script，季頻） | ✓ API（45.76%，2026-Q1） |
| 散戶：NAAIM Exposure Index | naaim/ycharts [SEARCH，best-effort] | ✓ SEARCH-VERIFIED（84.69，轉降） |
| 機構：BofA FMS + JPM 調查 | 月頻 [best-effort] | ✗ NOT DISCLOSED（前次後無新號；6 月號背景） |
| 貨幣：Fed funds DFEDTARU/DFEDTARL | FRED（script） | ✓ API（3.75/3.50） |
| 貨幣：HY OAS BAMLH0A0HYM2 | FRED（script） | ✓ API（2.67%） |
| 貨幣：IG OAS BAMLC0A0CM | FRED（script） | ✓ API（0.76%） |
| 貨幣：10Y DGS10 | FRED（script） | ✓ API（4.55%） |
| 貨幣：10Y 實質 DFII10 | FRED（script） | ✓ API（2.30%） |
| 貨幣：10Y breakeven T10YIE | FRED（script） | ✓ API（2.25%，直抓非 derived） |
| 貨幣：WTI DCOILWTICO | FRED（script） | ✓ API（$69.6） |
| 貨幣：CPI YoY CPIAUCSL | FRED（script，月頻） | ✓ API（4.17%） |
| 貨幣：5y5y forward T5YIFR | FRED（script） | ✓ API（2.19%，Δ −3 bps） |
| 貨幣：10Y 期限溢價 THREEFYTP10 | FRED（script，Kim-Wright） | ✓ API（0.7322%，Δ +3.3 bps） |
| 貨幣：repo 資金壓力 SOFR/SOFR99/IORB/RPONTTLD | FRED（script，`repo_stress`，同類合併） | ✓ API（SOFR−IORB −3bps／SRF $0） |
| 貨幣：美債標售需求 auction | Reuters/Bloomberg recap [SEARCH，best-effort] | ✓ SEARCH-VERIFIED（10yr B/C 2.59、無 tail） |
| 貨幣：Fed funds path FedWatch | CME [SEARCH，best-effort] | ✓ SEARCH-VERIFIED（\~96.7% hold、降息近零） |
| 貨幣：Fed 資產負債表 WALCL | FRED（script，週頻） | ✓ API（$6.72T） |
| 貨幣：ECB/BOJ ECBASSETSW/JPNASSETS | FRED（script） | ✓ API（€5.98T / ¥639.55T） |
| 貨幣：PBoC aggregate financing | NBS/PBoC 英文摘要 [best-effort] | ✗ NOT DISCLOSED（07-14 發布） |
| 貨幣：私募信貸/非銀基金流動性壓力 | BDC/interval fund [SEARCH，best-effort] | ✓ SEARCH-VERIFIED（BCRED gate proration/超限，已擊發） |
| AI：Hyperscaler capex guidance | MSFT/GOOGL/AMZN/META 季報（stock-of-state） | ✓ SEARCH-VERIFIED（$650–725B，+77%，續上修） |
| AI：AI token volume growth | Anthropic/OpenAI/Google 揭露 [best-effort] | ✓ SEARCH-VERIFIED（Google 3.2 quadrillion/月 7×） |
| AI：OpenAI/Anthropic 營收 | Sacra/valueaddvc [best-effort] | ✓ SEARCH-VERIFIED（$25B ARR / $47B run-rate） |
| AI：Hyperscaler 客戶集中度/RPO 重複 | 財報質化 [best-effort] | ✓ SEARCH-VERIFIED（Oracle RPO $638B、OpenAI \~2/3） |
| AI：AI compute 供需/過剩 | GPU 租金/HBM/利用率 [SEARCH，best-effort] | ✓ SEARCH-VERIFIED（GPU 租金 −64–75%、DRAM +58–63% QoQ） |
| AI：Hyperscaler 融資結構 | capex vs FCF/發債 [SEARCH，best-effort] | ✓ SEARCH-VERIFIED（Oracle 86% capex/rev BBB；債發 $175B） |
| AI：AI 營收對 capex 缺口 | 營收/capex 量級對比 [SEARCH，best-effort] | ✓ SEARCH-VERIFIED（3–5× 缺口，分母 top-4＋Oracle） |
| AI：折舊年限變動 | 10-K/10-Q 掃描 [SEARCH，best-effort] | ✗ NOT DISCLOSED（30 日無變動） |
| AI：資本週期階段 | 供給/需求增速+進出場事件 [SEARCH，best-effort] | ✓ SEARCH-VERIFIED（30–50% 專案延後、MSFT 凍 1.5GW） |
| 投機：+AI 改名/SPAC/無營收 IPO（7d） | 新聞掃描 | ✓ SEARCH-VERIFIED（2 件：EVTV、K Wave） |
| 投機：IPO 市場熱度 | IPO 日曆/首日/無營收佔比 | ✓ SEARCH-VERIFIED（PBLS +50% 無營收、YTD 193） |
| 投機：Microcap thematic moonshots | Finviz/Benzinga 掃描（required 週篩） | ✓ SEARCH-VERIFIED（0 件） |
| 投機：Upcoming AI IPOs | S-1/具名報導 [best-effort] | ✓ SEARCH-VERIFIED（OpenAI/Anthropic S-1、SpaceX 納 Nasdaq-100） |
| 投機：Insider Form 4 clusters | SEC EDGAR [SEC EDGAR] | ✓ SEARCH-VERIFIED（0 件；單一 PLTR 10b5-1 非合格叢集、缺 EDGAR URL） |
| 投機：Cboe put/call ratio | Cboe/YCharts [SEARCH，best-effort] | ✓ SEARCH-VERIFIED（0.69） |
| 結構：美國槓桿 ETF AUM | etf.com/ETFGI [SEARCH] | ✓ SEARCH-VERIFIED（TQQQ \~$37–40B 等；NVDL 流出） |
| 結構：美國單一個股槓桿 ETF 核准/上市 | SEC EDGAR/ETF.com | ✓ SEARCH-VERIFIED（SpaceX 10 檔、Tradr 5、Leverage Shares 6） |
| 結構：全球槓桿產品核准 KRX/TWSE/JPX/ESMA | 各監管 [best-effort] | ✓ SEARCH-VERIFIED（0 件新核准；本週擴散訊號未觸發） |
| 結構：0DTE option volume | Cboe/SpotGamma | ✓ SEARCH-VERIFIED（\~60–63%） |
| 結構：Options total volume（OCC 月報） | OCC 月報 | ✓ SEARCH-VERIFIED（Cboe 6 月 ADV 23M 創高 proxy；OCC 6 月頁 403） |
| 結構：VIX/SKEW/stock-bond corr | Cboe [同類合併，worst-case] | ✓ SEARCH-VERIFIED（VIX 16.13/SKEW 145.38；corr 未單獨量化） |
| 結構：margin debt/市值 ratio（cross-ref） | 引散戶 margin debt，confirmation only | ✓ SEARCH-VERIFIED（引 margin debt +53.7% YoY） |
| 結構：AI 基建債務/vendor-financing | 30 日掃描 [SEARCH，best-effort] | ✓ SEARCH-VERIFIED（Nvidia backstop/Sharon AI/SpaceX/CoreWeave） |
| 結構：銀行對 NBFI 放款 LNFACBW027SBOG | FRED（script，週頻） | ✓ API（$1.99T，confirmation） |
| 結構：美債基差交易槓桿（CFTC/MOVE/repo） | CFTC TFF/MOVE/OFR [SEARCH，best-effort] | ✓ SEARCH-VERIFIED（淨空倉 \~$1T、MOVE \~65.76；script 三塊 fetch_failed） |

**✓ SEARCH-VERIFIED traceability（非 0 件列）**

| 項目 | search query | 結果 URL／來源 | 發布或資料日期 | 抓取 timestamp |
|---|---|---|---|---|
| CAPE / PE | S&P 500 Shiller CAPE trailing PE July 8 2026 | multpl.com/shiller-pe、/s-p-500-pe-ratio；gurufocus.com | 2026-07-08 / 07-01 | 2026-07-09 09:30 CST |
| Mag 7 P/E | Magnificent 7 weighted PE forward 2026 | marketxls.com；yardeni.com | 2025-11～2026-05 | 2026-07-09 09:30 CST |
| Goldman AMD | Goldman Sachs AMD price target $640 July 2026 | thestreet.com | 2026-07-05 | 2026-07-09 09:30 CST |
| AI 信用分歧 | CoreWeave Oracle CDS junk bonds widening July 2026 | bloomberg.com；realinvestmentadvice.com | 2026-07-02 | 2026-07-09 09:30 CST |
| RSP/SPY | RSP vs SPY YTD 2026 divergence | 247wallst.com | 2026-06 中旬～07 | 2026-07-09 09:30 CST |
| 廣度 > 50-DMA | S&P 500 percent above 50-day MA July 2026 | schwab.com；tickeron.com | 2026-07-07 | 2026-07-09 09:30 CST |
| Top-10 集中度 | S&P 500 top 10 concentration 2026 | ahasignals.com；pionline.com | 2026-04 | 2026-07-09 09:30 CST |
| CNN F&G | CNN Fear Greed index today July 2026 | cnn.com/markets/fear-and-greed；benzinga.com | 2026-07-08 | 2026-07-09 09:30 CST |
| Margin debt | FINRA margin debt May 2026 record | advisorperspectives.com/dshort | 2026-05 | 2026-07-09 09:30 CST |
| AAII | AAII sentiment July 2 2026 | seekingalpha.com/news/4609705 | 2026-07-02 | 2026-07-09 09:30 CST |
| NAAIM | NAAIM exposure index July 2026 | ycharts.com/indicators/naaim_number | 2026-07-01 | 2026-07-09 09:30 CST |
| Social/WSB | wallstreetbets top tickers July 2026 | altindex.com/wallstreetbets；finviz.com | 2026-07 週 | 2026-07-09 09:30 CST |
| 私募信貸 | BCRED redemption 7.9% gate 5% cap 2026 | hedgeco.net；withintelligence.com | 2026-Q1 | 2026-07-09 09:30 CST |
| 美債標售 | US Treasury 10 year auction bid-to-cover July 8 2026 | kucoin.com/news/flash | 2026-07-08 | 2026-07-09 09:30 CST |
| FedWatch | CME FedWatch July 30 2026 FOMC hold | cmegroup.com FedWatch；macromicro.me | 2026-07 初 | 2026-07-09 09:30 CST |
| Hyperscaler capex | MSFT GOOGL AMZN META capex 2026 725 billion | tomshardware.com；cnbc.com | 2026-Q1 指引 | 2026-07-09 09:30 CST |
| AI token | Google 3.2 quadrillion tokens monthly 2026 | cryptobriefing.com；datacenterdynamics.com | 2026-05～06 | 2026-07-09 09:30 CST |
| OpenAI/Anthropic 營收 | OpenAI Anthropic ARR run-rate 2026 | sacra.com；valueaddvc.com | 2026-02 / 05 | 2026-07-09 09:30 CST |
| RPO 集中度 | Oracle RPO 638 billion OpenAI CoreWeave backlog 2026 | fool.com；Morgan Stanley cite | 2026-07 初 | 2026-07-09 09:30 CST |
| AI compute 供需 | GPU rental price H100 DRAM contract Q2 2026 | intuitionlabs.ai；trendforce.com | 2026-Q2 | 2026-07-09 09:30 CST |
| 融資結構 | hyperscaler capex FCF bond issuance 2026 175 billion | know.creditsights.com；qz.com；fortune.com | 2026-02～03 | 2026-07-09 09:30 CST |
| 資本週期 | data center project delay cancellation Microsoft AWS 2026 | newsletter.semianalysis.com；datacenterdynamics.com | 2026-06～07 | 2026-07-09 09:30 CST |
| +AI 改名 | Envirotech EVTV Azio AI merger；K Wave Talivar AI July 2026 | globenewswire.com；coindesk.com | 2026-07-01～02 | 2026-07-09 09:30 CST |
| IPO 熱度 | IPO this week Parabilis SPAC July 2026 Renaissance | renaissancecapital.com；fticonsulting.com | 2026-07 初 | 2026-07-09 09:30 CST |
| Upcoming AI IPO | OpenAI Anthropic S-1 SpaceX Nasdaq 100 2026 | cryptobriefing.com；indmoney.com | 2026-06～07 | 2026-07-09 09:30 CST |
| Cboe put/call | Cboe equity put call ratio July 8 2026 | ycharts.com；cboe.com | 2026-07-08 | 2026-07-09 09:30 CST |
| 槓桿 ETF AUM | leveraged ETF AUM NVDL TQQQ SOXL July 2026 | morningstar.com；etfdb.com | 2026-07-08 | 2026-07-09 09:30 CST |
| 單一個股槓桿 ETF 新上市 | single stock leveraged ETF launch June July 2026 | etfdb.com；prnewswire.com | 2026-06～07 | 2026-07-09 09:30 CST |
| 全球槓桿核准 | Korea Taiwan Japan Europe single stock leveraged ETF July 2026 | koreaherald.com；kedglobal.com | 2026-07 週 | 2026-07-09 09:30 CST |
| 0DTE | 0DTE SPX volume share Q2 2026 Cboe record | cboe.com；prnewswire.com | 2026-Q2 | 2026-07-09 09:30 CST |
| Options volume | OCC Cboe options volume June 2026 record | stocktitan.net；investing.com | 2026-06 | 2026-07-09 09:30 CST |
| VIX/SKEW | VIX term structure SKEW index July 2026 | finance.yahoo.com；cboe.com | 2026-07-08 / 07-06 | 2026-07-09 09:30 CST |
| AI 基建債務 | Nvidia backstop Sharon AI SpaceX CoreWeave debt June 2026 | mlq.ai；businesswire.com；cnbc.com | 2026-06～07 | 2026-07-09 09:30 CST |
| 美債基差槓桿 | leveraged funds Treasury futures net short MOVE 2026 | imf.org GFSR；macromicro.me | 2026-04 / 07-08 | 2026-07-09 09:30 CST |

**✓ SEARCH-VERIFIED（0 件）screens** — query、來源、timestamp（URL/發布日可為 —）：

| 篩選項 | search query | 檢查來源 | 結果 | 抓取 timestamp |
|---|---|---|---|---|
| Microcap moonshots（週篩） | biggest microcap gainers 100% single day quantum AI space July 2026 | Finviz/Yahoo gainers/StockTwits（多 403） | 0 件（無合格單日 ≥100% 事件） | 2026-07-09 09:30 CST |
| Insider Form 4 clusters（14d） | insider selling Form 4 cluster AI tech July 2026 SEC EDGAR | SEC EDGAR（403）/StockTitan/Investing.com | 0 件合格叢集（單一 PLTR 10b5-1 非合格） | 2026-07-09 09:30 CST |
| 全球單一個股槓桿新核准（7d） | single stock leveraged ETF approval KRX TWSE JPX ESMA July 2026 | Korea Herald/KED/ESMA | 0 件新核准（本週擴散未觸發） | 2026-07-09 09:30 CST |

**方法/失敗註記**：本次 `scripts/fetch_macro.py`（prior-run date 2026-07-07）回傳全 FRED 序列 `status: ok`；多數序列與 `sp500_trend`（S&P 有 07-08 新觀測）、WTI/10Y `no_new_obs`（前次執行日與最新有效觀測同日）——`no_new_obs` 為「Δ=0（無新觀測）」的成功結果，故 §3 WTI/10Y 標 持平（無新觀測）、S&P 標 持平（−0.28%<門檻）、10Y 週 Δ 拆解各項 0 bps（`driver: none`）、格局正常計算為 穩定共存。script 非 FRED 塊 `cftc_lev_funds`/`move_index`/`ofr_repo` 回報 `fetch_failed`，已以 WebSearch 補（美債基差交易槓桿 bullet，best-effort）。SEC EDGAR/多家 movers/OCC/Cboe 主機本次 egress 403，相關值改由 WebSearch 二手來源，已於各列標註。FRED 金鑰全程未印出。

## 本次分數存檔
```json
{
  "date": "2026-07-09",
  "iso_week": "2026-W28",
  "weekday": "Thursday",
  "timezone": "Asia/Taipei",
  "valuation": 79,
  "breadth": 30,
  "speculation": 58,
  "retail": 50,
  "monetary": 75,
  "structural": 77,
  "total": 64,
  "tier": "警戒",
  "regime": "穩定共存"
}
```

本報告為相對風險溫度計，非擇時訊號。
