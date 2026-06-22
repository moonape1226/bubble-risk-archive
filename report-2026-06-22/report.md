# 2026-06-22 市場泡沫風險評估報告
> 報告日期：2026-06-22；執行日：2026-06-22 Asia/Taipei；ISO 週次：2026-W26；前次基準：report-2026-06-18（4天前）

## §1 六維度風險條圖
| 維度 | 條圖 | 本次 | 前次 | Δ |
|---|---|---:|---:|---:|
| 估值溢價 | ▰▰▰▰▰▰▰▰▱▱ | 80 | 80 | 0 |
| 市場廣度 | ▰▰▰▱▱▱▱▱▱▱ | 33 | 37 | -4 |
| 投機行為 | ▰▰▰▰▰▰▱▱▱▱ | 69 | 70 | -1 |
| 散戶情緒 | ▰▰▰▰▰▱▱▱▱▱ | 53 | 54 | -1 |
| 貨幣與信貸環境 | ▰▰▰▰▰▰▰▱▱▱ | 75 | 66 | +9 |
| 結構性槓桿 | ▰▰▰▰▰▰▰▱▱▱ | 71 | 70 | +1 |
| **加權總分** | ▰▰▰▰▰▰▱▱▱▱ | **66【高】** | 65 | +1 |

## §2 歷史錨點相似度
| 錨點 | 相似度 | 條圖 | 標記 |
|---|---:|---|---|
| 1997 早期建設 | 50% | ▰▰▰▰▰▱▱▱▱▱ |  |
| 1998 LTCM 衝擊 | 40% | ▰▰▰▰▱▱▱▱▱▱ |  |
| 1999 晚期狂熱 | 70% | ▰▰▰▰▰▰▰▱▱▱ | ◀ 最貼近 |
| 2000/3 頂點 | 25% | ▰▰▱▱▱▱▱▱▱▱ |  |
| 2021/12 Meme 頂 | 50% | ▰▰▰▰▰▱▱▱▱▱ |  |

## §3 三角訊號
| 指標 | 本次數值 | vs 前次 |
|---|---|---|
| S&P 500 | 7,500.58 | —（本週無新日序，Δ 不可用） |
| WTI 原油 | $84.65 /bbl | —（本週無新日序，Δ 不可用） |
| 10Y Treasury | 4.49% | —（本週無新日序，Δ 不可用） |

**三者狀態**：穩定共存。本週 FRED 日序未推進（最新 DGS10 觀測 2026-06-17 早於前次基準日 06-18，S&P 最新 06-18 ＝前次基準），三資產皆無可比週變動方向；公開信用利差極窄、S&P 距 200DMA +8.66% 未達 +10% 拉伸閾值，故判穩定共存（非基準日，但 Δ 不可用）。

- 股市：S&P 500 7,500.58（2026-06-18），距 200DMA +8.66%、距 52 週 MA +10.62%，價格高位但本週無新日序可判方向。
- WTI 原油：$84.65 /bbl（2026-06-15），絕對水位偏高（油價對通膨預期具上行壓力），本週無新日序方向。
- 10Y 殖利率：4.49%（2026-06-17），主要驅動本週不可分解（無日序）；水位仍受實質利率（DFII10 2.23%）與錨定通膨預期（T10YIE 2.25%）共同支撐。

**格局轉變**：前次格局「穩定共存」（讀自 report-2026-06-18 之 score.json `regime`），本次仍判「穩定共存」——三資產三角面上穩定、未見同向拉伸；惟財務扳機已自非銀信貸側獨立擊發（見「結論」），三角穩定不等於 financing 環境穩定。

**10Y 成因拆解**：本週 Δ 分解不可用——無日序資料（script `decomposition.status = unavailable_no_daily_history`；最新 DGS10 觀測 06-17 早於前次基準日 06-18，無新週變動可算）。水位：DGS10 4.49%、DFII10 2.23%、T10YIE 2.25%（皆 FRED API）。
- ΔDFII10 實質殖利率週變動：不可用（無日序）
- ΔT10YIE 損益平衡通膨週變動：不可用（無日序）
- 判定：不可判（無週變動資料；嚴禁以水位代 Δ）

**扳機鏈：油 → 通膨預期 → Fed 受限 → refinancing 成本**：WTI $84.65 偏高 → CPI YoY 4.17%（CPIAUCSL，資料月 2026-05，已 ≥4%）且 T5YIFR 5y5y forward 2.23%（錨定、未失控）→ Fed 受限（6/17 FOMC 12-0 維持 3.50–3.75%；CME FedWatch 顯示年底約四成「升息」機率、近乎零降息，能源通膨使降息空間受壓）→ refinancing 成本維持高位。能源通膨壓縮 Fed put 可得性，為本鏈「Fed 受限」環節之數據基礎；CPI 一律引 script 值（非新聞偶得）。

**⚠ 結論**：扳機狀態：已擊發。判定依據（決定性，由重至輕取第一個成立者）——私募信貸 gate proration / breach 成立：Blackstone BCRED（$79B）於 2026-06-04 首度限制贖回，投資人申請贖回 10%、僅獲准 5%（前一季尚以高管自有資金全額滿足 7.9% 申請），構成實際的 redemption cap proration。雖 HY OAS 2.63%、IG OAS 0.74% 仍處循環低點（公開利差自滿側），非銀信貸側已先行點火，正呼應「公開 mark-to-market 利差可能低估早期 financing 壓力」之設計。歷史意義：估值＋槓桿（crash potential energy）已高位，financing 扳機自非銀側擊發、Fed 受通膨制約難以快速放水，整體配置偏向晚期循環。

## 六維度評分

| 維度 | 權重 | 分數 | 一句話論述（含來源） |
|---|---:|---:|---|
| 1. 估值溢價 | 22% | 80 | Shiller CAPE 40.43（GuruFocus, 2026-06-01）、S&P 500 trailing P/E ~26、Mag 7 加權 P/E 32.78（MAGS, 2026-06-20）、ECY ≈ 1/40.43 − 2.23/100 ≈ +0.24%（近零，1929/2000 級校準）；hyperscaler capex 仍上修（$725B、Meta 上調至 $125–145B）支撐倍數，惟未取得直接 GPU 利用率/租金證據，結論降述為「capex/Nvidia 營收仍支撐，但未取得直接利用率證據」。 |
| 2. 市場廣度 | 13% | 33 | RSP（等權）YTD +9.7% 領先 SPY（市值權）+8.4%（24/7 Wall St., 2026-06-10）＝參與度轉健康/擴散，故較前次下調；惟 Top-10 集中度 38.6%、Mag 7 ~32%（結構仍高）、近期 A/D 偏弱（6/16 僅 44% 上漲、Nasdaq 100 60% 在 50DMA 上）。 |
| 3. 投機行為 | 18% | 69 | SpaceX 2026-06-12 史上最大 IPO（SPCX $150）＋ AI-concentrated pipeline（占 pipeline value ~92%）＋ SPAC 申報（Osprey III $261M、Leader's Advantage $150M）；microcap moonshot ≥1（CDT +101% 6/18 量子題材；FreeCast +230%/週、BYAH +190% 為候補）；Cboe equity put/call 0.59 偏低（call 方向性投機，confirmation）；insider Form 4 合格 0 件。 |
| 4. 散戶情緒 | 12% | 53 | CNN F&G 37（Fear，2026-06-18，明顯降溫）、AAII 淨偏空（bull 36.6% / bear 39.4%）＝情緒面冷；但 FINRA margin debt $1.42T（2026-05）、YoY +53.7%（1999/2007/2021 頂部級別警訊）、+8.5% MoM、家庭持股佔金融資產 45.76%（BOGZ1FL153064486Q, 2026-Q1，近歷史高位）、NAAIM 92.83（擁擠多頭）＝部位/槓桿面熱；兩者相抵約持平。 |
| 5. 貨幣與信貸環境 | 20% | 75 | 雙向計分，本次落「扳機側（兼自滿側）」：自滿側＝HY OAS 2.63%、IG OAS 0.74%（皆 FRED, 06-17，循環低、利差極窄），全球央行資產負債表持平（WALCL $6.74T、ECB €6.14T、BOJ ¥664.4 兆）；扳機側＝私募信貸 gate proration 已擊發（BCRED 6/4，10% 申請僅准 5%），且 Fed 受 CPI 4.17%/能源通膨制約（FedWatch 年底約四成升息、零降息）。較前次 +9，並於本次新增訊號以質化訊號併列。 |
| 6. 結構性槓桿 | 15% | 71 | 美國槓桿 ETF 總 AUM >$170B、單一個股槓桿 $31.5B（TQQQ $31.3B、SOXL $17.3B/+261% YTD），AUM 近高位；SPX 0DTE 佔比 56–62%（高且持續）；VIX 尾端避險暴增（高履約 VIX call 創量）；AI 基建表外融資 $120B（Oracle/xAI/Meta/CoreWeave SPV）擴張、JPM 估 2026 證券化 $30–40B，惟 CoreWeave $8.5B 為 IG 評級、合約現金流（Meta $19B backlog）擔保、條件穩健；全球擴散訊號本週未觸發。 |

各維度評分採 0–100，分數愈高＝該維度對泡沫風險之貢獻愈大。

## 綜合分數

| 維度 | 權重 | 分數 | 加權貢獻 |
|---|---:|---:|---:|
| 估值溢價 | 22% | 80 | 17.60 |
| 市場廣度 | 13% | 33 | 4.29 |
| 投機行為 | 18% | 69 | 12.42 |
| 散戶情緒 | 12% | 53 | 6.36 |
| 貨幣與信貸環境 | 20% | 75 | 15.00 |
| 結構性槓桿 | 15% | 71 | 10.65 |
| **加權總分** | 100% | — | **66.32 → 66** |

加權總分 = Σ(分數 × 權重)/100 = 66.32，half-up 四捨五入 → **66**。風險等級對照（40–64 警戒／65–84 高）：**66 → 高**。

邊界帶：總分 66 距 警戒/高 邊界 ≤ 2 分，評分固有噪音約 ±2–3，等級判讀需保留餘地。

## 歷史泡沫週期對比

相似度計算：checklist v2

相似度＝命中數 ÷ 特徵數 × 100，四捨五入到最接近的 5%；無資料特徵記未命中。最貼近錨點全列命中明細，其餘列關鍵差異摘要。

**1999 晚期狂熱（7/10 = 70%）◀ 最貼近**
- ① 估值溢價 ≥75：**命中**（80）
- ② CAPE ≥38：**命中**（40.43）
- ③ 投機行為 ≥60：**命中**（69）
- ④ 本週 moonshot ≥1 或無營收 IPO 佔比偏高：**命中**（CDT +101%、SpaceX 領銜 AI-concentrated IPO）
- ⑤ 市場廣度 ≥45（轉窄）：未命中（33，廣度反而擴散）
- ⑥ D5 落自滿側且 HY OAS <3.5%：**命中**（自滿側、HY OAS 2.63%）
- ⑦ 結構性槓桿 ≥60：**命中**（71）
- ⑧ 散戶情緒 ≥55：未命中（53）
- ⑨ 巨型 IPO pipeline 活躍（30 日內具名 S-1/定價）：**命中**（SpaceX 6/12 上市、OpenAI/Anthropic/xAI 在列）
- ⑩ 扳機狀態＝未擊發：未命中（已擊發）

**其餘錨點（關鍵差異摘要）**
- 1997 早期建設（4/8 = 50%）：命中 ②廣度<45、④capex 上修、⑤散戶<55、⑦HY OAS<4% 未走闊；但估值 80 過高、投機/槓桿過熱、扳機已擊發，與「早期」不符。
- 1998 LTCM 衝擊（3/8 = 40%）：命中 ③非銀壓力披露（BCRED gate）、⑤估值≥60、⑥扳機≥初啟；但 HY OAS 未走闊、無 ≥5% 回檔、Fed 未轉鴿、廣度未急轉弱、ΔT10YIE 無資料。
- 2000/3 頂點（2/8 = 25%）：命中 ②扳機≥初啟、⑧貨幣轉緊（FedWatch 升息傾向）；但估值未達 ≥85、廣度未極窄、無 insider 集中賣出、散戶未達 ≥65、無價格高位回落。
- 2021/12 Meme 頂（4/8 = 50%）：命中 ③槓桿≥65、⑤margin debt YoY≥+40%（+53.7%）、⑥本週 moonshot≥1、⑧CPI≥4% 且 Fed 尚未實質緊縮；但散戶情緒未達 65、無具名社群投機熱、廣度未背離。

**解讀**：本週最似 **1999 晚期狂熱**（70%）——高估值、高投機與結構性槓桿、巨型 IPO pipeline 與 moonshot 並存，但廣度反而擴散、散戶情緒降溫，且關鍵差異在於 financing 扳機已自非銀信貸側擊發（1999 該項未命中），使配置帶有向 2000 初期「估值高位＋ financing 壓力浮現」過渡的色彩。結構性槓桿以期間調整代理觀察（margin debt YoY +53.7%、0DTE 56–62%、槓桿 ETF AUM >$170B）在 1999/2021 類比中皆達高位；S&P 距 200DMA +8.66%、距 52 週 MA +10.62%（Farrell #1/#2），長期相對指數成長趨勢偏離之文章錨點（Dot-com ~95%、1929 ~110%、當前 AI 週期 ~147%）僅供敘事脈絡，不納入每週計分。

## 機構情緒對照

本次無新機構調查數據。（最近一次為 BofA 6 月全球 FMS，調查期 2026-06-05～06-11，於前次 06-18 run 之前發布，非本次新增；JPM 亦無本次新增。）背景參照：6 月 FMS 顯示經理人減碼風險資產、提高現金與債券，淨 45% 預期通膨上行（低於 5 月 66%、4 月 69%），BofA 評語為「FMS 歷史顯示此非風險資產『大頂』，僅夏季獲利了結」。

另：NAAIM Exposure Index 92.83（週 2026-06-17，主動經理人曝險偏高＝擁擠多頭，反向風險升高，Farrell #9）。NAAIM 於「散戶情緒」維度作 positioning-crowding 的 confirmation cross-check 計分，此處僅作敘述對照，不重複計分。

## 本次新增訊號

vs 前次（4 天前，基準 report-2026-06-18）：

- **估值溢價 80（Δ 0）**：CAPE 40.43、Mag 7 P/E 32.78、ECY≈+0.24% 近零；capex 仍上修（$725B、Meta 上調）支撐倍數，惟未取得直接 GPU 利用率證據。
- **市場廣度 33（Δ -4）**：RSP YTD +9.7% 領先 SPY +8.4%（廣度轉健康/擴散），惟 Top-10 集中度 38.6%、近期 A/D 偏弱。
- **投機行為 69（Δ -1）**：SpaceX 6/12 史上最大 IPO 上市；microcap moonshot ≥1（CDT +101% 6/18 量子題材）；put/call 0.59 偏低；insider Form 4 合格 0 件。
- **散戶情緒 53（Δ -1）**：F&G 37（Fear，降溫）、AAII 淨偏空；但 margin debt $1.42T、YoY +53.7%（頂部級別警訊）、家庭持股 45.76% 近高位、NAAIM 92.8 擁擠。
- **貨幣與信貸環境 75（Δ +9）【扳機側】**：雙向計分——自滿側（HY OAS 2.63%、IG OAS 0.74% 循環低）＋扳機側已擊發。質化新訊號（雙向 Δ 遮蔽防護）：**私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）** 出現 gate proration——Blackstone BCRED 於 2026-06-04 首度限制贖回（redemption-request ratio 升至 10%、quarterly redemption cap 僅准 5% ＝ gate proration），前一季尚能全額滿足 7.9%；屬「扳機側」financing 壓力擊發，即使公開利差 Δ 不顯著仍須列示。
- **結構性槓桿 71（Δ +1）**：槓桿 ETF AUM >$170B（單一個股 $31.5B、SOXL +261% YTD）、0DTE 佔比 56–62%、AI 基建表外融資 $120B（Oracle/xAI/Meta/CoreWeave SPV）擴張；CoreWeave $8.5B 為 IG 評級、合約現金流擔保（條件穩健，列背景）。

全球槓桿擴散訊號：**本週擴散訊號未觸發**（韓國 KRX 5/27 上市三星/SK 海力士單一個股 2x 槓桿 ETF 為背景，本週無新核准；TWSE/JPX/ESMA 本週無英文披露）。

## 數據附錄

### Coverage table（每個 `# Data sources` bullet 一列；共 47 列）

| # | 維度 / source bullet | 預定來源與方法 | 狀態 |
|---:|---|---|---|
| 1 | 估值-S&P 500 P/E & Shiller CAPE | multpl/GuruFocus [SEARCH] | ✓ SEARCH-VERIFIED（CAPE 40.43；見 raw） |
| 2 | 估值-Mag 7 加權 P/E & AI leader P/S | Yardeni/MAGS [SEARCH] | ✓ SEARCH-VERIFIED（MAGS 32.78） |
| 3 | 估值-Analyst TP upgrade decomposition | sell-side 14 日掃描 [SEARCH] | ✗ NOT DISCLOSED（近期 NVDA/TSMC 上修在 14 日窗外，僅作背景） |
| 4 | 估值-S&P 500 price-trend deviation | scripts/fetch_macro.py `sp500_trend` | ✓ API（dev200 +8.66%、dev52w +10.62%） |
| 5 | 廣度-RSP vs SPY YTD divergence | 247wallst/Yahoo [SEARCH] | ✓ SEARCH-VERIFIED（RSP +9.7% / SPY +8.4%） |
| 6 | 廣度-Top-10 concentration | etfdb/247wallst [SEARCH] | ✓ SEARCH-VERIFIED（38.6%、Mag7 ~32%） |
| 7 | 廣度-A/D ratio、new high/low | StockCharts/Yahoo [SEARCH] | ✓ SEARCH-VERIFIED（6/16 44% 上漲、N100 60%>50DMA） |
| 8 | 散戶-CNN Fear & Greed | cnn.com [SEARCH] | ✓ SEARCH-VERIFIED（37 Fear） |
| 9 | 散戶-Margin Debt + ratio + YoY | FINRA/dshort/GuruFocus [SEARCH] | ✓ SEARCH-VERIFIED（$1.42T、YoY +53.7%、/GDP 4.1%） |
| 10 | 散戶-AAII Investor Sentiment | aaii.com [SEARCH] | ✓ SEARCH-VERIFIED（bull 36.6/bear 39.4） |
| 11 | 散戶-社交情緒代理（Reddit/X） | [SEARCH] best-effort | ✗ NOT DISCLOSED（本週無具名顯著熱點） |
| 12 | 散戶-家庭持股佔金融資產比 | fetch_macro.py BOGZ1FL153064486Q | ✓ API（45.76%，2026-Q1） |
| 13 | 散戶-NAAIM Exposure Index | naaim/ycharts [SEARCH] best-effort | ✓ SEARCH-VERIFIED（92.83，週 06-17） |
| 14 | 機構-BofA FMS & JPM survey | [SEARCH] best-effort（月頻） | ✓ SEARCH-VERIFIED（6 月 FMS；非本次新增） |
| 15 | 貨幣-Fed funds DFEDTARU/DFEDTARL | fetch_macro.py FRED | ✓ API（3.75/3.50，Δ0） |
| 16 | 貨幣-HY OAS BAMLH0A0HYM2 | fetch_macro.py FRED | ✓ API（2.63%） |
| 17 | 貨幣-IG OAS BAMLC0A0CM | fetch_macro.py FRED | ✓ API（0.74%） |
| 18 | 貨幣-10Y DGS10 | fetch_macro.py FRED | ✓ API（4.49%） |
| 19 | 貨幣-10Y real DFII10 | fetch_macro.py FRED | ✓ API（2.23%） |
| 20 | 貨幣-10Y breakeven T10YIE | fetch_macro.py FRED | ✓ API（2.25%） |
| 21 | 貨幣-WTI DCOILWTICO | fetch_macro.py FRED | ✓ API（$84.65） |
| 22 | 貨幣-CPI YoY CPIAUCSL | fetch_macro.py FRED（yoy_pct） | ✓ API（4.17%，資料月 2026-05） |
| 23 | 貨幣-5y5y forward T5YIFR | fetch_macro.py FRED | ✓ API（2.23%） |
| 24 | 貨幣-FedWatch 隱含路徑 | CME/Reuters [SEARCH] best-effort | ✓ SEARCH-VERIFIED（維持 3.50–3.75%；年底約四成升息） |
| 25 | 貨幣-Fed balance sheet WALCL | fetch_macro.py FRED | ✓ API（$6,736,424M） |
| 26 | 貨幣-全球央行 ECB/BOJ | fetch_macro.py ECBASSETSW+JPNASSETS | ✓ API（ECB 6,135,633；BOJ 6,643,630；worst-case 取最舊 BOJ 05-01） |
| 27 | 貨幣-PBoC aggregate financing | [SEARCH] best-effort | ✗ NOT DISCLOSED（無當期英文摘要） |
| 28 | 貨幣-私募信貸/非銀基金贖回壓力 | [SEARCH] best-effort | ✓ SEARCH-VERIFIED（BCRED 6/4 gate proration；見 raw） |
| 29 | AI-Hyperscaler capex guidance | 財報/[SEARCH] required | ✓ SEARCH-VERIFIED（$725B、Meta 上調 $125–145B） |
| 30 | AI-token volume growth | [SEARCH] best-effort | ✗ NOT DISCLOSED（本季無量化披露） |
| 31 | AI-OpenAI/Anthropic 營收 | [SEARCH] best-effort | ✗ NOT DISCLOSED（無當期具名披露） |
| 32 | AI-hyperscaler 客戶集中度 | 財報 [SEARCH] best-effort | ✓ SEARCH-VERIFIED（CoreWeave Meta $19B backlog，質化） |
| 33 | AI-compute 供需/過剩 | [SEARCH] best-effort | ✗ NOT DISCLOSED（未取得直接利用率/租金證據） |
| 34 | 投機-+AI rename/SPAC/無營收 IPO 潮 | [SEARCH] 7 日 | ✓ SEARCH-VERIFIED（SpaceX IPO、SPAC Osprey/Leader's 申報） |
| 35 | 投機-IPO market heat | Renaissance/Nasdaq [SEARCH] | ✓ SEARCH-VERIFIED（SpaceX 史上最大、AI-concentrated） |
| 36 | 投機-Microcap moonshots | Finviz/Benzinga [SEARCH] required | ✓ SEARCH-VERIFIED（≥1：CDT +101% 6/18） |
| 37 | 投機-Upcoming AI IPOs | S-1/具名報導 [SEARCH] | ✓ SEARCH-VERIFIED（SpaceX 已上市、OpenAI/Anthropic/xAI 在列） |
| 38 | 投機-Insider selling Form 4 | SEC EDGAR required | ✓ SEARCH-VERIFIED（0 件，14 日內無合格 cluster） |
| 39 | 投機-Cboe equity put/call | Cboe/ycharts [SEARCH] best-effort | ✓ SEARCH-VERIFIED（0.59，06-17） |
| 40 | 結構-美國槓桿 ETF AUM | etf.com/ETFGI [SEARCH] | ✓ SEARCH-VERIFIED（>$170B；單一個股 $31.5B） |
| 41 | 結構-美國單一個股槓桿 ETF 核准 | SEC/etf.com [SEARCH] | ✓ SEARCH-VERIFIED（0 件 本窗無新核准；既有 NVDL/TSLL 等） |
| 42 | 結構-全球槓桿產品核准（KRX/TWSE/JPX/ESMA） | 各監理機關 [SEARCH] best-effort | ✓ SEARCH-VERIFIED（韓 5/27 背景；本週無新核准、擴散未觸發） |
| 43 | 結構-0DTE option volume | Cboe/SpotGamma [SEARCH] | ✓ SEARCH-VERIFIED（SPX 0DTE 56–62%） |
| 44 | 結構-Options total volume（OCC） | OCC/Cboe [SEARCH] | ✓ SEARCH-VERIFIED（SPX ADV 創高 ~3.9M、index 5M/日） |
| 45 | 結構-VIX/SKEW/stock-bond correlation | Cboe/SpotGamma [SEARCH] | ✓ SEARCH-VERIFIED（尾端避險暴增、put skew 走平） |
| 46 | 結構-margin debt/市值 比（confirmation） | 引用散戶維度 | derived（cross-reference，不重複計分） |
| 47 | 結構-AI 基建債務/vendor-financing | [SEARCH] best-effort | ✓ SEARCH-VERIFIED（CoreWeave $8.5B IG；$120B 表外） |

### 原始數據表（每筆計分用資料一列）

| 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|
| Shiller CAPE | 40.43 | GuruFocus https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio | 2026-06-01 | 2026-06-22 10:30 (UTC+8) |
| S&P 500 trailing P/E | ~26 | Advisor Perspectives dshort（P/E10 2026-05） | 2026-05 | 2026-06-22 10:30 (UTC+8) |
| Mag 7 加權 P/E（MAGS） | 32.78 | StockCircle https://stockcircle.com/stocks/mags/pe-ratio | 2026-06-20 | 2026-06-22 10:30 (UTC+8) |
| S&P 500 spot | 7,500.58 | FRED API (series_id=SP500) | 2026-06-18 | 2026-06-22 10:10 (UTC+8) |
| S&P 200DMA / 偏離 | 6,902.63 / +8.66% | FRED API (SP500, sp500_trend) | 2026-06-18 | 2026-06-22 10:10 (UTC+8) |
| S&P 52週MA / 偏離 | 6,780.67 / +10.62% | FRED API (SP500, sp500_trend) | 2026-06-18 | 2026-06-22 10:10 (UTC+8) |
| RSP YTD / SPY YTD | +9.7% / +8.4% | 247wallst https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/ | 2026-06-10 | 2026-06-22 10:30 (UTC+8) |
| Top-10 集中度 / Mag7 | 38.6% / ~32% | etfdb / 247wallst | 2026-03-31 | 2026-06-22 10:30 (UTC+8) |
| A/D（6/16） | 2,383 漲 / 2,905 跌（44%） | StockCharts/streetstats | 2026-06-16 | 2026-06-22 10:30 (UTC+8) |
| CNN F&G | 37（Fear） | https://www.cnn.com/markets/fear-and-greed | 2026-06-18 | 2026-06-22 10:30 (UTC+8) |
| FINRA margin debt | $1.42T（+8.5% MoM、+53.7% YoY） | dshort https://www.advisorperspectives.com/dshort/updates/2026/06/16/margin-debt-finra | 2026-05 | 2026-06-22 10:30 (UTC+8) |
| Margin debt / GDP | 4.1% | GuruFocus #4266 | 2026-04 | 2026-06-22 10:30 (UTC+8) |
| AAII bull / bear / neutral | 36.6% / 39.4% / 24.1% | https://www.aaii.com/sentimentsurvey | 2026-06 週 | 2026-06-22 10:30 (UTC+8) |
| 家庭持股佔金融資產 | 45.76% | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 (Q1) | 2026-06-22 10:10 (UTC+8) |
| NAAIM Exposure | 92.83 | naaim.org / ycharts | 2026-06-17 | 2026-06-22 10:30 (UTC+8) |
| Fed funds（上/下限） | 3.75% / 3.50% | FRED API (DFEDTARU/DFEDTARL) | 2026-06-21 | 2026-06-22 10:10 (UTC+8) |
| HY OAS | 2.63% | FRED API (series_id=BAMLH0A0HYM2) | 2026-06-17 | 2026-06-22 10:10 (UTC+8) |
| IG OAS | 0.74% | FRED API (series_id=BAMLC0A0CM) | 2026-06-17 | 2026-06-22 10:10 (UTC+8) |
| 10Y nominal (DGS10) | 4.49% | FRED API (series_id=DGS10) | 2026-06-17 | 2026-06-22 10:10 (UTC+8) |
| 10Y real (DFII10) | 2.23% | FRED API (series_id=DFII10) | 2026-06-17 | 2026-06-22 10:10 (UTC+8) |
| 10Y breakeven (T10YIE) | 2.25% | FRED API (series_id=T10YIE) | 2026-06-18 | 2026-06-22 10:10 (UTC+8) |
| WTI | $84.65 | FRED API (series_id=DCOILWTICO) | 2026-06-15 | 2026-06-22 10:10 (UTC+8) |
| CPI YoY | 4.17% | FRED API (series_id=CPIAUCSL, yoy_pct) | 2026-05-01 | 2026-06-22 10:10 (UTC+8) |
| 5y5y forward (T5YIFR) | 2.23% | FRED API (series_id=T5YIFR) | 2026-06-18 | 2026-06-22 10:10 (UTC+8) |
| Fed BS (WALCL) | $6,736,424M | FRED API (series_id=WALCL) | 2026-06-17 | 2026-06-22 10:10 (UTC+8) |
| ECB BS (ECBASSETSW) | €6,135,633M | FRED API (series_id=ECBASSETSW) | 2026-06-12 | 2026-06-22 10:10 (UTC+8) |
| BOJ BS (JPNASSETS) | ¥6,643,630（億円） | FRED API (series_id=JPNASSETS) | 2026-05-01 | 2026-06-22 10:10 (UTC+8) |
| FedWatch（6 月） | 維持 3.50–3.75% 96%+；年底約四成升息、零降息 | CME FedWatch / Reuters | 2026-06-17 | 2026-06-22 10:30 (UTC+8) |
| Hyperscaler capex 2026 | $725B（+77% YoY）；Meta 上調 $125–145B | Tom's Hardware / CNBC / Statista | 2026-06 | 2026-06-22 10:30 (UTC+8) |
| 私募信貸 gate（BCRED） | 申請 10%、准 5%（gate proration） | Bloomberg https://www.bloomberg.com/news/articles/2026-06-04/blackstone-bcred-joins-private-credit-funds-limiting-redemptions | 2026-06-04 | 2026-06-22 10:30 (UTC+8) |
| 私募信貸（Oaktree，對照） | Q2 贖回降至 4.5%（<5% cap） | Bloomberg 2026-06-17 | 2026-06-17 | 2026-06-22 10:30 (UTC+8) |
| Microcap moonshot | CDT +101%（量子題材，~$1.4 收）；FreeCast +230%/週；BYAH +190% | Yahoo/Stocktwits/ts2.tech | 2026-06-18 | 2026-06-22 10:30 (UTC+8) |
| SpaceX IPO | SPCX $150（史上最大） | dealroom/builtin/renaissance | 2026-06-12 | 2026-06-22 10:30 (UTC+8) |
| Cboe equity put/call | 0.59 | ycharts https://ycharts.com/indicators/cboe_equity_put_call_ratio | 2026-06-17 | 2026-06-22 10:30 (UTC+8) |
| 槓桿 ETF 總 AUM | >$170B；單一個股 $31.5B；TQQQ $31.3B；SOXL $17.3B（+261% YTD） | etf.com | 2026-06 | 2026-06-22 10:30 (UTC+8) |
| SPX 0DTE 佔比 | 56–62% | Cboe/IBKR | 2026-02～2026-06 | 2026-06-22 10:30 (UTC+8) |
| AI 基建融資 | CoreWeave $8.5B DDTL（IG, A3/A(low)，Meta $19B backlog 擔保）；表外 SPV ~$120B | CoreWeave IR / Cryptopolitan | 2026 | 2026-06-22 10:30 (UTC+8) |
| 韓國單一個股槓桿 ETF | 16 檔（三星/SK 海力士 2x）上市 | KED/Korea Herald | 2026-05-27 | 2026-06-22 10:30 (UTC+8) |

附註：(1) 本次 FRED 日序未推進（最新 10Y 觀測 06-17 早於前次基準 06-18），故 §3 三角訊號之週變動與 10Y 成因拆解皆標「不可用——無日序資料」，未以水位代 Δ。(2) Analyst TP 上修（如 MS NVDA $285、Goldman TSMC +35%）多在 14 日窗外，僅作背景，未計入計分 Δ。(3) 私募信貸 March/Feb 事件（BCRED 全額滿足 7.9%、Blue Owl OBDC II 永久關閉贖回）在 30 日窗外，僅作背景；本次以窗內 6/4 BCRED gate proration 為扳機依據。(4) 所有 FRED 列均以 series_id 引用，未含任何 api_key。

## 本次分數存檔
```json
{
  "date": "2026-06-22",
  "iso_week": "2026-W26",
  "weekday": "Monday",
  "timezone": "Asia/Taipei",
  "valuation": 80,
  "breadth": 33,
  "speculation": 69,
  "retail": 53,
  "monetary": 75,
  "structural": 71,
  "total": 66,
  "tier": "高",
  "regime": "穩定共存"
}
```

本報告為相對風險溫度計，非擇時訊報。
