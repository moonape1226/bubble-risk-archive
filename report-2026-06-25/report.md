# 2026-06-25 市場泡沫風險評估報告
> 報告日期：2026-06-25；執行日：2026-06-25 Asia/Taipei；ISO 週次：2026-W26；前次基準：report-2026-06-22（3天前）

## §1 六維度風險條圖
| 維度 | 條圖 | 本次 | 前次 | Δ |
|---|---|---:|---:|---:|
| 估值溢價 | ▰▰▰▰▰▰▰▱▱▱ | 79 | 80 | -1 |
| 市場廣度 | ▰▰▰▱▱▱▱▱▱▱ | 33 | 33 | 0 |
| 投機行為 | ▰▰▰▰▰▰▰▱▱▱ | 70 | 69 | +1 |
| 散戶情緒 | ▰▰▰▰▰▱▱▱▱▱ | 51 | 53 | -2 |
| 貨幣與信貸環境 | ▰▰▰▰▰▰▰▱▱▱ | 76 | 75 | +1 |
| 結構性槓桿 | ▰▰▰▰▰▰▰▱▱▱ | 73 | 71 | +2 |
| **加權總分** | ▰▰▰▰▰▰▱▱▱▱ | **67【高】** | 66 | +1 |

## §2 歷史錨點相似度
| 錨點 | 相似度 | 條圖 | 標記 |
|---|---:|---|---|
| 1997 早期建設 | 50% | ▰▰▰▰▰▱▱▱▱▱ |  |
| 1998 LTCM 衝擊 | 50% | ▰▰▰▰▰▱▱▱▱▱ |  |
| 1999 晚期狂熱 | 70% | ▰▰▰▰▰▰▰▱▱▱ | ◀ 最貼近 |
| 2000/3 頂點 | 50% | ▰▰▰▰▰▱▱▱▱▱ |  |
| 2021/12 Meme 頂 | 50% | ▰▰▰▰▰▱▱▱▱▱ |  |

## §3 三角訊號
| 指標 | 本次數值 | vs 前次 |
|---|---|---|
| S&P 500 | 7,365.46 | ▼ -1.44%（前次 ~7,472.79） |
| WTI 原油 | $78.94 /bbl | ▼ -6.7%（前次 ~$84.65） |
| 10Y Treasury | 4.50% | 持平（Δ -1 bps，前次 4.51%） |

**三者狀態**：穩定共存。本期方向為 ▼ / ▼ / 持平（無任一 ▲、亦非 ▲/▼ 分歧），且 S&P 距 200DMA +6.56% 未達 +10% 拉伸閾值，依「格局判定規則」落入「穩定共存」。惟此「穩定」僅在價格三角面：本週實為半導體領頭的小幅 risk-off（6/23 Nasdaq -2.21%、SK 海力士 -12%、Micron -11.4%、SMH -6.5%），疊加韓國單一個股槓桿 ETF 暴跌（KOSPI 當日近 -10%）、AVGO 財報指引未驚喜與更鷹派 Fed 疑慮；financing 扳機則在非銀信貸側獨立擊發（見「結論」），三角穩定不等於 financing / leverage 環境穩定。

- 股市：S&P 500 7,365.46（FRED SP500，2026-06-23），較前次 ~7,472.79（06-22）▼ -1.44%；距 200DMA +6.56%、距 52 週 MA +8.44%（皆較前次回落，價格拉伸減弱）。
- WTI 原油：$78.94 /bbl（FRED DCOILWTICO，2026-06-22），較前次 ~$84.65（06-15 觀測）▼ -6.7%；油價回落緩解通膨預期上行壓力（見扳機鏈）。
- 10Y 殖利率：4.50%（FRED DGS10，2026-06-23），週 Δ -1 bp（持平），主要驅動為損益平衡通膨回落（breakeven 主導）。

**格局轉變**：前次格局「穩定共存」（讀自 report-2026-06-22 之 score.json `regime`），本次仍判「穩定共存」——三資產價格三角面未見同向拉伸（皆持平至小幅下行）；惟 financing 扳機自非銀私募信貸側持續且擴大擊發（多基金 gate proration），leverage 側亦見韓國槓桿 ETF 暴跌的實質化壓力，價格穩定與結構性脆弱並存。

**10Y 成因拆解（`ΔDGS10 ≈ ΔDFII10 + ΔT10YIE`，拆的是週變動、非水位）**：本週 10Y 名目 -1 bp，拆解取自 script `decomposition`（FRED 各序列歷史，prior 對齊 06-22）：
- ΔDFII10 實質殖利率週變動：+1 bp（2.28% → 2.29%）
- ΔT10YIE 損益平衡通膨週變動：-5 bps（2.23% → 2.18%）
- 判定：**breakeven-driven**（ΔT10YIE -5 主導，ΔDFII10 +1；10Y 微跌係通膨預期回落所致，實質利率近持平）。恆等式 -1 ≈ +1 + (-5) 於四捨五入下成立。

**扳機鏈：油 → 通膨預期 → Fed 受限 → refinancing 成本**：本週油價回落（WTI $84.65 → $78.94，▼ -6.7%）→ 損益平衡通膨同步回落（T10YIE -5 bps 至 2.18%、T5YIFR 5y5y forward 2.17%、週 Δ -1 bp，仍錨定）→ 通膨預期側對 Fed 的壓力本週「略為紓緩」，惟 realized CPI YoY 仍達 4.17%（CPIAUCSL，資料月 2026-05，≥4%），Fed 寬鬆空間仍受 realized 通膨制約（6/17 FOMC 維持 3.50–3.75%、CME FedWatch 年底約四成「升息」機率、近乎零降息）→ refinancing 成本維持高位。本鏈「油 → 通膨預期」環節本週走弱（disinflationary），但「Fed 受限」仍由 4.17% 的 realized CPI 撐住；CPI 一律引 script 值（非新聞偶得）。

**⚠ 結論**：扳機狀態：已擊發。判定（決定性，由重至輕取第一個成立者）——私募信貸 gate proration / breach **成立且擴大**：本月（過去 30 日內）多檔大型非交易 BDC / interval fund 出現 redemption-request ratio 飆升並觸及 quarterly redemption cap 的 gate proration / breach——Blue Owl OCIC 申請達 21.9%、OTIC 達 40.7%（按 5% cap 比例分配），Apollo Debt Solutions 第二季申請 16.8%（throttled），Cliffwater CLF 申請 ~14%（按 7% interval-fund cap 分配），KKR KREST 第二季 tender 按 74% 比例分配，Blackstone BCRED 第二季亦觸發 gate 並錄得約 -3% NAV 淨流出；非交易 BDC 板塊更出現**史上首見的季度淨流出**（Q1 2026），構成跨多基金的 net inflow→outflow flip。雖 HY OAS 2.71%（週 +6 bps）、IG OAS 0.74% 仍處循環低點（公開 mark-to-market 利差自滿側、尚未反映），非銀信貸側已先行、且較前次（單一 BCRED）顯著擴大，正呼應「公開利差可能低估早期 financing 壓力」之設計。三者價格配置歷史意義：估值＋槓桿（crash potential energy）仍高位，financing 扳機自非銀側擴大擊發、Fed 受 realized 通膨制約難快速放水，整體配置偏向晚期循環，且本週新增 leverage 側（韓國槓桿 ETF 暴跌、美國單一個股槓桿 ETF 爆量發行）與 insider 集中賣出（AMAT）的 2000/3-top 色彩。

## 六維度評分

| 維度 | 權重 | 分數 | 一句話論述（含來源） |
|---|---:|---:|---|
| 1. 估值溢價 | 22% | 79 | Shiller CAPE 40.94（multpl, 2026-06-24，較前次 40.43 微升、仍近紀錄高）、S&P 500 trailing P/E ~26（GuruFocus 25.1 / WorldPeRatio 26.7, 06-23）、Mag 7 加權 P/E 31.86（MAGS, StockAnalysis，較前次 32.78 微降）、ECY ≈ 1/40.94 − 2.29/100 ≈ +0.15%（較前次 +0.24% 更貼近零，1929/2000 級校準）；capex 全面仍上修（$725B、MSFT ~$190B、Alphabet $175–190B、AMZN ~$200B、Meta $125–145B）支撐倍數，AI compute 無過剩跡象（瓶頸由 GPU 移向 HBM/DRAM，contract price +58–63% QoQ），惟記憶體成本通膨為毛利風險；S&P 距 200DMA 自 +8.66% 回落至 +6.56%（價格拉伸減弱，均值回歸位能下降），故較前次 -1。 |
| 2. 市場廣度 | 13% | 33 | RSP（等權）YTD +9.67% 仍領先 SPY（市值權）+8.38%（PortfoliosLab/247wallst, 06-10）＝參與度偏健康/擴散；本週 risk-off 由 mega-cap 半導體領跌（NVDA/Micron/TSM/SK 海力士），narrow leaders 受創反使相對廣度未惡化；惟 Top-10 集中度 ~38%（NVDA 7.90%/AAPL 6.78%/GOOGL 6.03%…，結構仍高）。本週 A/D 即時值未取得（barchart $S5FI / $ADRN 來源 403），最近可考為 6/16 之 44% 上漲（負廣度），rationale 已註明該即時輸入缺漏、未以舊值代當期計分。Δ0。 |
| 3. 投機行為 | 18% | 70 | insider **集中賣出轉為命中**：Applied Materials（AMAT，半導體設備龍頭）CEO Gary Dickerson 6/15–16 賣 83,000 股約 $49.2M、SVP Nalamasu ~$14.4M、SVP Raja ~$25.2M（合計 ~$65M+ 多人 cluster，Form 4 交易日在窗內；EDGAR 直連 403，經 StockTitan Form 4 鏡像/investing.com 佐證）＋ NVDA 黃仁勳 6/20–23 單人賣 ~$14.4M（10b5-1）；microcap moonshot ≥1（本週 2 檔：CDT +101% 6/18 量子+AI；FreeCast CAST +171% 6/20 衛星+串流，皆 going-concern 弱基本面）；+AI 改名 BIRD→Smartbird（Allbirds 轉 AI 基建、+40%）、QUBT 併購；SPAC 加速（YTD 14 件 $2.7B、Osprey Acquisition III $261M）；IPO 熱（Renaissance IPO 指數 YTD +26.3% vs S&P +9%）；Cboe equity put/call 0.56（較前次 0.59 更低，call 方向性投機，confirmation）。較前次 +1。 |
| 4. 散戶情緒 | 12% | 51 | 情緒面**續冷**：CNN F&G **28（Fear，2026-06-24，自前次 37 進一步降溫、逼近 Extreme Fear）**、AAII 淨偏空（bull 36.6%/bear 39.4%，週 06-18，無新週）；但部位/槓桿面仍熱：FINRA margin debt $1.42T（2026-05，無新印，沿用）、YoY +53.7%（1999/2007/2021 頂部級別警訊）、家庭持股佔金融資產 45.76%（BOGZ1FL153064486Q, 2026-Q1，近歷史高位）、NAAIM 92.83（週 06-17，擁擠多頭，confirmation）。F&G 大幅降溫拉低主分，部位面高位托底，淨 -2。 |
| 5. 貨幣與信貸環境 | 20% | 76 | 雙向計分，本次落「扳機側（兼自滿側）」：自滿側＝HY OAS 2.71%（週 +6 bps，仍循環低）、IG OAS 0.74%（Δ0，FRED 06-23），全球央行資產負債表持平/緩步 QT（WALCL $6.74T、ECB €6.12T、BOJ ¥664.4 兆）；扳機側＝**私募信貸 gate proration 較前次擴大**（Blue Owl/Apollo/Cliffwater/KKR/BCRED 多基金第二季觸發 cap 比例分配、非交易 BDC 史上首見淨流出），且 Fed 受 realized CPI 4.17% 制約（FedWatch 年底約四成升息、零降息）。本週 disinflationary 緩解（油 ▼、breakeven -5 bps）部分抵銷，淨 +1。rationale 落「扳機側」。 |
| 6. 結構性槓桿 | 15% | 73 | 美國槓桿 ETF 總 AUM **創高 ~$198B**（前次 >$170B；TQQQ ~$36–40B、SOXL ~$34B，皆顯著放大）；單一個股槓桿 ETF **爆量發行**（SpaceX 上市帶動 ~10 檔 2X SPCX、Leverage Shares 6/16 八檔＋6/23 九檔科技供應鏈 2X、Roundhill 2X DRAM「RAM」6/24）；SPX 0DTE 佔比 ~61%（Cboe 紀錄高）；SKEW 143（尾端避險偏高）、VIX ~19.5 contango（即期平靜）；**韓國單一個股槓桿 ETF 暴跌實質化**（6/23 KOSPI 近 -10%、flash crash、監理回頭檢討 $290B 槓桿 ETF 熱潮）＝槓桿產品放大下行的風險實現；AI 基建債務窗內新增 Nvidia $25B IG 債（6/15，史上最大、vendor-financing 核心節點）＋ Meta El Paso ~$13B（進行中），CoreWeave $3.1B DDTL（5/18）為窗外背景。全球擴散訊號（2+ 非美市場新核准）本週未觸發。較前次 +2。 |

各維度評分採 0–100，分數愈高＝該維度對泡沫風險之貢獻愈大。

## 綜合分數

| 維度 | 權重 | 分數 | 加權貢獻 |
|---|---:|---:|---:|
| 估值溢價 | 22% | 79 | 17.38 |
| 市場廣度 | 13% | 33 | 4.29 |
| 投機行為 | 18% | 70 | 12.60 |
| 散戶情緒 | 12% | 51 | 6.12 |
| 貨幣與信貸環境 | 20% | 76 | 15.20 |
| 結構性槓桿 | 15% | 73 | 10.95 |
| **加權總分** | 100% | — | **66.54 → 67** |

加權總分 = Σ(分數 × 權重)/100 = 66.54，half-up 四捨五入 → **67**。風險等級對照（40–64 警戒／65–84 高）：**67 → 高**。

（總分 67 距 警戒/高 邊界 3 分，未落入 ±2 邊界帶 [63–66]，故本節不加邊界帶註記。）

## 歷史泡沫週期對比

相似度計算：checklist v2

相似度＝命中數 ÷ 特徵數 × 100，四捨五入到最接近的 5%；無資料特徵記未命中。最貼近錨點全列命中明細，其餘列關鍵差異摘要。

**1999 晚期狂熱（7/10 = 70%）◀ 最貼近**
- ① 估值溢價 ≥75：**命中**（79）
- ② CAPE ≥38：**命中**（40.94）
- ③ 投機行為 ≥60：**命中**（70）
- ④ 本週 moonshot ≥1 或無營收 IPO 佔比偏高：**命中**（CDT +101%、CAST +171%；IPO 指數 YTD +26%）
- ⑤ 市場廣度 ≥45（轉窄）：未命中（33，廣度反而擴散/RSP 領先）
- ⑥ D5 落自滿側且 HY OAS <3.5%：**命中**（自滿側、HY OAS 2.71%）
- ⑦ 結構性槓桿 ≥60：**命中**（73）
- ⑧ 散戶情緒 ≥55：未命中（51）
- ⑨ 巨型 IPO pipeline 活躍（30 日內具名 S-1/定價）：**命中**（OpenAI 6/8、Anthropic 6/1 confidential S-1；SpaceX 6/12 定價上市）
- ⑩ 扳機狀態＝未擊發：未命中（已擊發）

**其餘錨點（關鍵差異摘要）**
- 1997 早期建設（4/8 = 50%）：命中 ②廣度<45、④capex 上修、⑤散戶<55、⑦HY OAS<4% 且本次未實質走闊（+6 bps 視為噪音）；但估值 79 過高、投機/槓桿過熱、扳機已擊發，與「早期」不符。
- 1998 LTCM 衝擊（4/8 = 50%）：命中 ③具名非銀/槓桿機構壓力披露（多基金私募信貸 gate proration）、⑤估值≥60、⑥扳機≥初啟、⑧ΔT10YIE≤0（-5 bps，通膨預期非主因）；但 HY OAS 未走闊、無 ≥5% 回檔、Fed 未轉鴿、廣度未急轉弱。較前次升（新增 ⑧ 命中、私募信貸壓力擴大）。
- 2000/3 頂點（4/8 = 50%）：命中 ②扳機≥初啟、⑤投機≥70、⑥insider 集中賣出（AMAT 14 日內合格 cluster）、⑧貨幣轉緊（FedWatch 升息傾向）；但估值未達 ≥85、廣度未極窄、散戶未達 ≥65、無 dev200 自 >+10% 回落。**較前次（25%）顯著上升**，反映 insider 分配與投機達門檻的 top 過渡色彩。
- 2021/12 Meme 頂（4/8 = 50%）：命中 ③槓桿≥65、⑤margin debt YoY≥+40%（+53.7%）、⑥本週 microcap moonshot≥1、⑧CPI≥4% 且 Fed 尚未實質緊縮；但散戶情緒未達 65、無具名社群投機熱、廣度未背離、央行資產負債表未擴張。

**解讀**：本週最似 **1999 晚期狂熱**（70%）——高估值、高投機與結構性槓桿、巨型 IPO pipeline 與 moonshot 並存，但廣度反而擴散、散戶情緒（F&G 28 Fear）降溫。關鍵變化在於 **2000/3 頂點相似度自 25% 跳升至 50%**（insider 集中賣出 AMAT、投機達 ≥70、扳機已擊發、Fed 轉緊傾向），配置帶有自 1999 晚期向 2000 初期「估值高位＋financing 壓力浮現＋leverage 實質化」過渡的色彩。結構性槓桿以期間調整代理觀察（margin debt YoY +53.7%、0DTE ~61%、槓桿 ETF AUM 創高 $198B、韓國槓桿 ETF 暴跌）在 1999/2021 類比中皆達高位；S&P 距 200DMA +6.56%、距 52 週 MA +8.44%（Farrell #1/#2，較前次回落），長期相對指數成長趨勢偏離之文章錨點（Dot-com ~95%、1929 ~110%、當前 AI 週期 ~147%）僅供敘事脈絡，不納入每週計分。

## 機構情緒對照

本次無新機構調查數據。（最近一次為 BofA 6 月全球 FMS，於前次 run 前發布，非本次新增；JPM 亦無本次新增；未見 7 月 FMS 或新機構調查。）背景參照：6 月 FMS 顯示經理人減碼風險資產、提高現金與債券；對照 5 月 FMS 曾轉為股票 50% 超配，6 月轉防禦，反映機構情緒於 5→6 月降溫。

另：NAAIM Exposure Index 92.83（週 2026-06-17，主動經理人曝險偏高＝擁擠多頭，反向風險升高，Farrell #9）。NAAIM 於「散戶情緒」維度作 positioning-crowding 的 confirmation cross-check 計分，此處僅作敘述對照，不重複計分。私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）本週於多檔半流動性基金擴大（Blue Owl / Apollo / Cliffwater / KKR / BCRED），BofA 預期 redemption 申請於 2026-Q2 見高峰，屬機構資金面的 financing 緊縮訊號。

## 本次新增訊號

vs 前次（3 天前，基準 report-2026-06-22）：

- **估值溢價 79（Δ -1）**：CAPE 40.94（微升）、Mag 7 P/E 31.86（微降）、ECY≈+0.15%（更貼近零）；capex 全面仍上修支撐倍數；S&P 距 200DMA 自 +8.66% 回落至 +6.56%（價格拉伸減弱），故微降。
- **市場廣度 33（Δ 0）**：RSP YTD +9.67% 仍領先 SPY +8.38%（廣度健康/擴散），本週 risk-off 由 mega-cap 半導體領跌、未使相對廣度惡化；Top-10 ~38% 仍高。本週 A/D 即時值未取得（來源 403），未以舊值代當期。
- **投機行為 70（Δ +1）**：**insider 集中賣出由「0 件」轉為命中**——AMAT（半導體龍頭）CEO Dickerson 6/15–16 賣 ~$49.2M、SVP Nalamasu ~$14.4M、SVP Raja ~$25.2M（多人 cluster，Form 4 交易日在 14 日窗內；EDGAR 直連 403、經 Form 4 鏡像佐證）＋NVDA 黃仁勳單人 ~$14.4M（10b5-1）；本週 moonshot 2 檔（CDT +101%、CAST +171%）；BIRD→Smartbird +AI 改名；SPAC 加速；put/call 0.56 偏低。
- **散戶情緒 51（Δ -2）**：CNN F&G **28（Fear，自 37 進一步降溫）**、AAII 淨偏空；但 margin debt YoY +53.7%（頂部級別）、家庭持股 45.76% 近高位、NAAIM 92.83 擁擠托底。
- **貨幣與信貸環境 76（Δ +1）【扳機側】**：雙向計分——自滿側（HY OAS 2.71% +6 bps、IG OAS 0.74% 循環低）＋扳機側擴大擊發。質化新訊號（雙向 Δ 遮蔽防護）：**私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）較前次（單一 BCRED）顯著擴大**——Blue Owl OCIC redemption-request ratio 21.9%、OTIC 40.7%（按 5% quarterly redemption cap 比例分配＝gate proration）、Apollo Debt Solutions 16.8%（throttled）、Cliffwater ~14%（按 7% cap 分配）、KKR KREST tender 按 74% 分配、BCRED 第二季觸發 gate 且約 -3% NAV 淨流出；非交易 BDC 板塊出現史上首見季度淨流出（net inflow→outflow flip）。屬「扳機側」financing 壓力擴大擊發，即使公開利差 Δ 不顯著仍須列示。
- **結構性槓桿 73（Δ +2）**：槓桿 ETF AUM **創高 $198B**（TQQQ ~$36–40B、SOXL ~$34B）、SPX 0DTE ~61%（紀錄高）、SKEW 143；**美國單一個股槓桿 ETF 爆量發行**（SpaceX ~10 檔、Leverage Shares 6/16 八檔＋6/23 九檔、Roundhill 2X DRAM 6/24）；**韓國單一個股槓桿 ETF 暴跌實質化**（6/23 KOSPI 近 -10%、flash crash、監理檢討）；AI 基建債務窗內新增 Nvidia $25B IG 債（6/15）＋Meta El Paso ~$13B。

全球槓桿擴散訊號：**本週擴散訊號未觸發**（韓國本週為**監理回頭檢討/限制**單一個股槓桿 ETF、postpone 單股週選，非新核准；TWSE 僅研議、JPX/ESMA 本週無英文新核准披露）。美國端單一個股槓桿 ETF 雖大量發行，但「全球擴散訊號」特例規則限於 2+ 非美市場同週核准，本週不適用該 floor。

## 數據附錄

### Coverage table（每個 `# Data sources` bullet 一列；共 47 列）

| # | 維度 / source bullet | 預定來源與方法 | 狀態 |
|---:|---|---|---|
| 1 | 估值-S&P 500 P/E & Shiller CAPE | multpl/GuruFocus [SEARCH] | ✓ SEARCH-VERIFIED（CAPE 40.94；見 raw） |
| 2 | 估值-Mag 7 加權 P/E & AI leader P/S | MAGS/StockAnalysis [SEARCH] | ✓ SEARCH-VERIFIED（MAGS 31.86） |
| 3 | 估值-Analyst TP upgrade decomposition | sell-side 14 日掃描 [SEARCH] | ✓ SEARCH-VERIFIED（TSMC Susquehanna $575←$500, 6/20，EPS-driven；見 raw） |
| 4 | 估值-S&P 500 price-trend deviation | scripts/fetch_macro.py `sp500_trend` | ✓ API（dev200 +6.56%、dev52w +8.44%） |
| 5 | 廣度-RSP vs SPY YTD divergence | 247wallst/PortfoliosLab [SEARCH] | ✓ SEARCH-VERIFIED（RSP +9.67% / SPY +8.38%） |
| 6 | 廣度-Top-10 concentration | Wikipedia/P&I [SEARCH] | ✓ SEARCH-VERIFIED（~38%、NVDA 7.90%） |
| 7 | 廣度-A/D ratio、new high/low | StockCharts/Barchart [SEARCH] | ⛔ FETCH FAILED（本週即時值；$S5FI/$ADRN 來源 403，最近可考 6/16 之 44%，rationale 已註明缺漏未代當期） |
| 8 | 散戶-CNN Fear & Greed | cnn.com [SEARCH] | ✓ SEARCH-VERIFIED（28 Fear） |
| 9 | 散戶-Margin Debt + ratio + YoY | FINRA/dshort [SEARCH] | ✓ SEARCH-VERIFIED（$1.42T、YoY +53.7%；無新印沿用 2026-05） |
| 10 | 散戶-AAII Investor Sentiment | aaii.com [SEARCH] | ✓ SEARCH-VERIFIED（bull 36.6/bear 39.4，週 06-18） |
| 11 | 散戶-社交情緒代理（Reddit/X） | [SEARCH] best-effort | ✗ NOT DISCLOSED（本週無具名顯著熱點） |
| 12 | 散戶-家庭持股佔金融資產比 | fetch_macro.py BOGZ1FL153064486Q | ✓ API（45.76%，2026-Q1） |
| 13 | 散戶-NAAIM Exposure Index | naaim/ycharts [SEARCH] best-effort | ✓ SEARCH-VERIFIED（92.83，週 06-17） |
| 14 | 機構-BofA FMS & JPM survey | [SEARCH] best-effort（月頻） | ✓ SEARCH-VERIFIED（6 月 FMS；非本次新增、無 7 月 FMS） |
| 15 | 貨幣-Fed funds DFEDTARU/DFEDTARL | fetch_macro.py FRED | ✓ API（3.75/3.50，Δ0） |
| 16 | 貨幣-HY OAS BAMLH0A0HYM2 | fetch_macro.py FRED | ✓ API（2.71%，+6 bps） |
| 17 | 貨幣-IG OAS BAMLC0A0CM | fetch_macro.py FRED | ✓ API（0.74%，Δ0） |
| 18 | 貨幣-10Y DGS10 | fetch_macro.py FRED | ✓ API（4.50%，-1 bp） |
| 19 | 貨幣-10Y real DFII10 | fetch_macro.py FRED | ✓ API（2.29%，+1 bp） |
| 20 | 貨幣-10Y breakeven T10YIE | fetch_macro.py FRED | ✓ API（2.18%，-5 bps） |
| 21 | 貨幣-WTI DCOILWTICO | fetch_macro.py FRED | ✓ API（$78.94） |
| 22 | 貨幣-CPI YoY CPIAUCSL | fetch_macro.py FRED（yoy_pct） | ✓ API（4.17%，資料月 2026-05） |
| 23 | 貨幣-5y5y forward T5YIFR | fetch_macro.py FRED | ✓ API（2.17%，-1 bp） |
| 24 | 貨幣-FedWatch 隱含路徑 | CME/Reuters [SEARCH] best-effort | ✓ SEARCH-VERIFIED（維持 3.50–3.75%；年底約四成升息） |
| 25 | 貨幣-Fed balance sheet WALCL | fetch_macro.py FRED | ✓ API（$6,736,424M，06-17） |
| 26 | 貨幣-全球央行 ECB/BOJ | fetch_macro.py ECBASSETSW + JPNASSETS（BOJ 腳本 fetch_failed→WebSearch） | ✓ SEARCH-VERIFIED（ECB €6,119,940M API；BOJ ¥664.4 兆 search，worst-case 取 BOJ search） |
| 27 | 貨幣-PBoC aggregate financing | [SEARCH] best-effort | ✓ SEARCH-VERIFIED（AFRE +8.9% YoY、淨投放 ~¥1.4T/月，方向性） |
| 28 | 貨幣-私募信貸/非銀基金贖回壓力 | [SEARCH] best-effort | ✓ SEARCH-VERIFIED（多基金 gate proration；見 raw） |
| 29 | AI-Hyperscaler capex guidance | 財報/[SEARCH] required | ✓ SEARCH-VERIFIED（$725B、全面上修） |
| 30 | AI-token volume growth | [SEARCH] best-effort | ✓ SEARCH-VERIFIED（Google >3T tokens/日、OpenRouter 5x；混合 vintage） |
| 31 | AI-OpenAI/Anthropic 營收 | [SEARCH] best-effort | ✓ SEARCH-VERIFIED（Anthropic $30B ARR、OpenAI ~$24–25B ARR，4 月） |
| 32 | AI-hyperscaler 客戶集中度 | 財報 [SEARCH] best-effort | ✓ SEARCH-VERIFIED（CoreWeave Meta backlog，質化） |
| 33 | AI-compute 供需/過剩 | [SEARCH] best-effort | ✓ SEARCH-VERIFIED（無過剩；瓶頸由 GPU→HBM/DRAM，DRAM +58–63% QoQ） |
| 34 | 投機-+AI rename/SPAC/無營收 IPO 潮 | [SEARCH] 7 日 | ✓ SEARCH-VERIFIED（BIRD→Smartbird、QUBT 併購、SPAC Osprey III $261M） |
| 35 | 投機-IPO market heat | Renaissance/Nasdaq [SEARCH] | ✓ SEARCH-VERIFIED（IPO 指數 YTD +26.3%、Kardigan +37.5% pop） |
| 36 | 投機-Microcap moonshots | Finviz/Benzinga [SEARCH] required | ✓ SEARCH-VERIFIED（2 件：CDT +101%、CAST +171%） |
| 37 | 投機-Upcoming AI IPOs | S-1/具名報導 [SEARCH] | ✓ SEARCH-VERIFIED（OpenAI 6/8、Anthropic 6/1 S-1；SpaceX 6/12 已上市） |
| 38 | 投機-Insider selling Form 4 | SEC EDGAR required | ✓ SEARCH-VERIFIED（AMAT 多人 cluster 6/15–16＋NVDA 黃仁勳；EDGAR 直連 403、Form 4 鏡像佐證，見 raw） |
| 39 | 投機-Cboe equity put/call | Cboe/ycharts [SEARCH] best-effort | ✓ SEARCH-VERIFIED（0.56，06-23） |
| 40 | 結構-美國槓桿 ETF AUM | etf.com/ETFGI [SEARCH] | ✓ SEARCH-VERIFIED（創高 $198B；TQQQ ~$36–40B、SOXL ~$34B） |
| 41 | 結構-美國單一個股槓桿 ETF 核准/發行 | SEC/etf.com [SEARCH] | ✓ SEARCH-VERIFIED（窗內爆量：SpaceX ~10 檔、Leverage Shares 6/16+6/23 共 17 檔、Roundhill DRAM 6/24） |
| 42 | 結構-全球槓桿產品核准（KRX/TWSE/JPX/ESMA） | 各監理機關 [SEARCH] best-effort | ✗ NOT DISCLOSED（本週無新核准；韓國為監理檢討/限制，非核准；TWSE/JPX/ESMA 無英文新核准） |
| 43 | 結構-0DTE option volume | Cboe/SpotGamma [SEARCH] | ✓ SEARCH-VERIFIED（SPX 0DTE ~61%，紀錄高） |
| 44 | 結構-Options total volume（OCC） | OCC/Cboe [SEARCH] | ✓ SEARCH-VERIFIED（SPX 量創高、單日 >4.7M 合約） |
| 45 | 結構-VIX/SKEW/stock-bond correlation | Cboe/SpotGamma [SEARCH] | ✓ SEARCH-VERIFIED（VIX ~19.5 contango、SKEW 143、股債相關偏高） |
| 46 | 結構-margin debt/市值 比（confirmation） | 引用散戶維度 | derived（cross-reference，不重複計分） |
| 47 | 結構-AI 基建債務/vendor-financing | [SEARCH] best-effort | ✓ SEARCH-VERIFIED（窗內 Nvidia $25B IG 債 6/15、Meta El Paso ~$13B） |

### 原始數據表（每筆計分用資料一列）

| 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|
| Shiller CAPE | 40.94 | multpl https://www.multpl.com/shiller-pe | 2026-06-24 | 2026-06-25 (UTC+8) |
| S&P 500 trailing P/E | ~26（GuruFocus 25.1 / WorldPeRatio 26.7） | https://www.gurufocus.com/economic_indicators/57/sp-500-pe-ratio | 2026-06-23 | 2026-06-25 (UTC+8) |
| Mag 7 加權 P/E（MAGS） | 31.86 | StockAnalysis https://stockanalysis.com/etf/mags/ | 2026-06-24（即時） | 2026-06-25 (UTC+8) |
| S&P 500 spot | 7,365.46 | FRED API (series_id=SP500) | 2026-06-23 | 2026-06-25 (UTC+8) |
| S&P 200DMA / 偏離 | 6,912.07 / +6.56% | FRED API (SP500, sp500_trend) | 2026-06-23 | 2026-06-25 (UTC+8) |
| S&P 52週MA / 偏離 | 6,792.14 / +8.44% | FRED API (SP500, sp500_trend) | 2026-06-23 | 2026-06-25 (UTC+8) |
| S&P prior spot / chg | 7,472.79 / -1.44% | FRED API (sp500_trend prior_spot) | 2026-06-22 | 2026-06-25 (UTC+8) |
| TSMC Susquehanna TP | $575 ←$500（EPS-driven） | search（Susquehanna note, 2026-06-20） | 2026-06-20 | 2026-06-25 (UTC+8) |
| RSP YTD / SPY YTD | +9.67% / +8.38% | 247wallst https://247wallst.com/investing/2026/06/10/rsp-vs-spy-does-equal-weight-beat-the-cap-weighted-sp-500/ | 2026-06-10 | 2026-06-25 (UTC+8) |
| Top-10 集中度 | ~38%（NVDA 7.90%/AAPL 6.78%/GOOGL 6.03%） | P&I https://www.pionline.com/data-rankings/chart-of-the-day/pi-sp500-index-concentration/ | 2026-06 | 2026-06-25 (UTC+8) |
| 半導體 selloff（6/23） | Nasdaq -2.21%、Micron -11.4%、TSM -5.2%、SMH -6.5%、SK 海力士 -12% | TheStreet/Yahoo https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-june-23-2026 | 2026-06-23 | 2026-06-25 (UTC+8) |
| A/D（最近可考 6/16） | 2,383 漲 / 2,905 跌（44%）；本週即時值 403 不可得 | StockCharts/streetstats | 2026-06-16 | 2026-06-25 (UTC+8) |
| CNN F&G | 28（Fear） | https://www.cnn.com/markets/fear-and-greed | 2026-06-24 | 2026-06-25 (UTC+8) |
| FINRA margin debt | $1.42T（+53.7% YoY） | dshort https://www.advisorperspectives.com/dshort/updates/2026/06/16/margin-debt-finra | 2026-05（無新印沿用） | 2026-06-25 (UTC+8) |
| AAII bull/bear/neutral | 36.6% / 39.4% / 24.1% | https://www.aaii.com/sentimentsurvey | 2026-06-18 週 | 2026-06-25 (UTC+8) |
| 家庭持股佔金融資產 | 45.76% | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 (Q1) | 2026-06-25 (UTC+8) |
| NAAIM Exposure | 92.83 | naaim.org / ycharts | 2026-06-17 | 2026-06-25 (UTC+8) |
| Fed funds（上/下限） | 3.75% / 3.50% | FRED API (DFEDTARU/DFEDTARL) | 2026-06-24 | 2026-06-25 (UTC+8) |
| HY OAS | 2.71%（+6 bps） | FRED API (series_id=BAMLH0A0HYM2) | 2026-06-23 | 2026-06-25 (UTC+8) |
| IG OAS | 0.74%（Δ0） | FRED API (series_id=BAMLC0A0CM) | 2026-06-23 | 2026-06-25 (UTC+8) |
| 10Y nominal (DGS10) | 4.50%（-1 bp） | FRED API (series_id=DGS10) | 2026-06-23 | 2026-06-25 (UTC+8) |
| 10Y real (DFII10) | 2.29%（+1 bp） | FRED API (series_id=DFII10) | 2026-06-23 | 2026-06-25 (UTC+8) |
| 10Y breakeven (T10YIE) | 2.18%（-5 bps） | FRED API (series_id=T10YIE) | 2026-06-24 | 2026-06-25 (UTC+8) |
| WTI | $78.94 | FRED API (series_id=DCOILWTICO) | 2026-06-22 | 2026-06-25 (UTC+8) |
| CPI YoY | 4.17% | FRED API (series_id=CPIAUCSL, yoy_pct) | 2026-05-01 | 2026-06-25 (UTC+8) |
| 5y5y forward (T5YIFR) | 2.17%（-1 bp） | FRED API (series_id=T5YIFR) | 2026-06-24 | 2026-06-25 (UTC+8) |
| Fed BS (WALCL) | $6,736,424M | FRED API (series_id=WALCL) | 2026-06-17 | 2026-06-25 (UTC+8) |
| ECB BS (ECBASSETSW) | €6,119,940M | FRED API (series_id=ECBASSETSW) | 2026-06-19 | 2026-06-25 (UTC+8) |
| BOJ BS（總資產） | ¥664.4 兆（JPNASSETS 腳本 fetch_failed→search） | Trading Economics https://tradingeconomics.com/japan/central-bank-balance-sheet | 2026-05 | 2026-06-25 (UTC+8) |
| FedWatch | 維持 3.50–3.75% >96%；年底約四成升息、零降息 | CME FedWatch / REX 預覽 | 2026-06-17 | 2026-06-25 (UTC+8) |
| PBoC | AFRE +8.9% YoY、M2 +8.3%、淨投放 ~¥1.4T/月 | People's Daily / Central Banking | 2026-06 | 2026-06-25 (UTC+8) |
| 私募信貸 gate（多基金） | Blue Owl OCIC 21.9%/OTIC 40.7%（5% cap 分配）；Apollo 16.8% throttled；Cliffwater ~14%（7% cap）；KKR KREST tender 74%；BCRED Q2 gate、-3% NAV | Morningstar/InvestmentNews/AltsWire/PitchBook https://www.morningstar.com/alternative-investments/blue-owl-offers-harsh-lesson-semiliquid-fund-investors | 2026-Q2（窗內披露） | 2026-06-25 (UTC+8) |
| Hyperscaler capex 2026 | $725B（+77% YoY）；MSFT ~$190B、Alphabet $175–190B、AMZN ~$200B、Meta $125–145B（全面上修） | Tom's Hardware https://www.tomshardware.com/tech-industry/big-tech/big-techs-ai-spending-plans-reach-725-billion | 2026-06 | 2026-06-25 (UTC+8) |
| AI token 成長 | Google >3T tokens/日（5 月）；OpenRouter 週 5T→25T（6 個月 5x） | CNBC https://www.cnbc.com/2026/06/10/wall-street-needs-crash-course-in-tokens-ahead-openai-anthropic-ipos.html | 2026-06-10 | 2026-06-25 (UTC+8) |
| OpenAI/Anthropic ARR | Anthropic $30B（4/7）、OpenAI ~$24–25B | VentureBeat/Epoch https://epoch.ai/data-insights/anthropic-openai-revenue | 2026-04 | 2026-06-25 (UTC+8) |
| AI compute 供需 | 無過剩；HBM/DRAM contract +58–63% QoQ（短缺至 2026）；H100 雲端租金回落但 B200 仍緊 | TrendForce https://www.trendforce.com/presscenter/news/20260331-12995.html | 2026-Q2 | 2026-06-25 (UTC+8) |
| Microcap moonshot | CDT +101%（6/18，量子+AI，rev 弱/going-concern）；FreeCast CAST +171%（6/20，衛星+串流，rev $92.9k） | ts2.tech/timothysykes https://www.timothysykes.com/news/freecastinc-cast-news-2026_06_20/ | 2026-06-18~20 | 2026-06-25 (UTC+8) |
| +AI 改名 | BIRD→Smartbird（Allbirds 轉 AI 基建，+40%、convertible $50M→$100M） | timothysykes https://www.timothysykes.com/news/smartbird-inc-cl-a-new-bird-news-2026_06_22/ | 2026-06-22 | 2026-06-25 (UTC+8) |
| SPAC | YTD 14 件 $2.7B（加速）；Osprey Acquisition III $261M、JAB I $150M、TVIV $150M | Renaissance/BoardroomAlpha https://www.renaissancecapital.com/IPO-Center/News/119845/SPAC-Osprey-Acquisition-III-files-for-a-$261-million-IPO-targeting-energy-a | 2026-06-18 | 2026-06-25 (UTC+8) |
| IPO 熱 | Renaissance IPO 指數 YTD +26.3% vs S&P +9.0%；Kardigan +37.5% pop；76 件 YTD | Renaissance https://www.renaissancecapital.com/IPO-Center/News/119949/US-IPO-Weekly-Recap-Another-biotech-IPO-pops-during-the-short-holiday-week | 2026-06-19 | 2026-06-25 (UTC+8) |
| 巨型 IPO pipeline | SpaceX 6/12 $135（~$75B 募資、~$1.8T 估值）；OpenAI 6/8、Anthropic 6/1 confidential S-1 | CNBC/TechCrunch https://techcrunch.com/2026/06/08/following-anthropic-openai-files-confidentially-for-ipo/ | 2026-06-01~12 | 2026-06-25 (UTC+8) |
| Insider（AMAT cluster） | CEO Dickerson 83,000 股 ~$49.2M（6/15–16）；SVP Nalamasu ~$14.4M；SVP Raja ~$25.2M | StockTitan Form 4 鏡像 https://www.stocktitan.net/sec-filings/AMAT/form-4-applied-materials-inc-de-insider-trading-activity-cb3a6ad6dbd2.html ; investing.com（EDGAR 直連 403） | 交易 2026-06-15~16 | 2026-06-25 (UTC+8) |
| Insider（NVDA） | 黃仁勳 100,000 股 ~$14.4M（6/20、6/23，10b5-1，單人非 cluster） | Bloomberg/Globe&Mail | 交易 2026-06-20~23 | 2026-06-25 (UTC+8) |
| Cboe equity put/call | 0.56 | ycharts https://ycharts.com/indicators/cboe_equity_put_call_ratio | 2026-06-23 | 2026-06-25 (UTC+8) |
| 槓桿 ETF 總 AUM | 創高 ~$198B（leveraged equity ~$157B）；TQQQ ~$36–40B、SOXL ~$34B、NVDL ~$4.5B、TSLL ~$5.4B | Cryptobriefing https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ | 2026-06 | 2026-06-25 (UTC+8) |
| 美單股槓桿 ETF 發行（窗內） | SpaceX ~10 檔（6/13–15）；Leverage Shares 6/16 八檔+6/23 九檔；Roundhill 2X DRAM「RAM」6/24 | etfdb/PRNewswire https://www.prnewswire.com/news-releases/leverage-shares-by-themes-unveils-nine-new-2x-single-stock-etfs-tracking-key-players-in-the-technology-supply-chain-302807131.html | 2026-06-13~24 | 2026-06-25 (UTC+8) |
| 韓國槓桿 ETF 暴跌 | KOSPI 6/23 近 -10%、flash crash、監理檢討 $290B 槓桿 ETF；單股週選 postpone | KED Global/Bloomberg https://www.kedglobal.com/policy/newsView/ked202606230001 | 2026-06-23 | 2026-06-25 (UTC+8) |
| SPX 0DTE 佔比 | ~61%（紀錄高） | Cboe https://www.cboe.com/insights/posts/spx-0-dte-options-jump-to-61-share-on-retail-resurgence/ | 2026-05（最新月） | 2026-06-25 (UTC+8) |
| VIX / VIX3M / SKEW | VIX ~19.5、VIX3M 21.06（contango）、SKEW 143.14 | Cboe/Yahoo https://www.cboe.com/us/indices/dashboard/skew/ | 2026-06-23~24 | 2026-06-25 (UTC+8) |
| AI 基建債務（窗內） | Nvidia $25B IG 債（7 tranches，~3x 超額認購，史上最大）；Meta El Paso ~$13B（MS/JPM） | Bloomberg https://www.bloomberg.com/news/articles/2026-06-15/nvidia-kicks-off-first-high-grade-bond-offering-since-2021 | 2026-06-15 / 05-04 | 2026-06-25 (UTC+8) |

附註：(1) 巨集數據由 `scripts/fetch_macro.py`（FRED API，urllib）取得，所有 FRED 列均以 series_id 引用、未含任何 api_key。(2) JPNASSETS（BOJ）腳本本次 `fetch_failed`，改以 WebSearch 取現貨（¥664.4 兆，Trading Economics，資料月 2026-05），ECB/BOJ 合併列 worst-case 取 BOJ 之 search 狀態。(3) §3 三角訊號之 S&P chg、10Y Δ 取自 script `sp500_trend` / `decomposition`（決定性）；WTI 因 script latest（06-22）即為前次基準日觀測、無更新日序 Δ，改與前次 run 已存之 $84.65（06-15 觀測）比較，標 ▼ -6.7%。(4) Insider AMAT cluster：SEC EDGAR / openinsider 直連經 egress proxy 403（組織政策），故以 StockTitan Form 4 鏡像＋investing.com 佐證，交易日 6/15–16 在 14 日窗內；此為 AI/半導體領頭企業合格多人 cluster。(5) 私募信貸多基金數據多為 Q1/Q2 2026 披露於本窗內，確切 as-of 日於次級來源略糊，金額/比例可靠、精確日以 SEC SC TO-I/TO-C 為準。(6) AI infra DDTL/SPV（CoreWeave $8.5B 3/30、$3.1B 5/18、xAI/Meta Hyperion 2025）多為窗外背景，僅 Nvidia $25B 債（6/15）與 Meta El Paso（進行中）為窗內新訊號。

## 本次分數存檔
```json
{
  "date": "2026-06-25",
  "iso_week": "2026-W26",
  "weekday": "Thursday",
  "timezone": "Asia/Taipei",
  "valuation": 79,
  "breadth": 33,
  "speculation": 70,
  "retail": 51,
  "monetary": 76,
  "structural": 73,
  "total": 67,
  "tier": "高",
  "regime": "穩定共存"
}
```

本報告為相對風險溫度計，非擇時訊號。
