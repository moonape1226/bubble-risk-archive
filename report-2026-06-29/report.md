# 2026-06-29 市場泡沫風險評估報告
> 報告日期：2026-06-29；執行日：2026-06-29 Asia/Taipei；ISO 週次：2026-W27；前次基準：report-2026-06-25（4天前）

## §1 六維度風險條圖
| 維度 | 條圖 | 本次 | 前次 | Δ |
|---|---|---:|---:|---:|
| 估值溢價 | ▰▰▰▰▰▰▰▱▱▱ | 78 | 79 | -1 |
| 市場廣度 | ▰▰▰▱▱▱▱▱▱▱ | 32 | 33 | -1 |
| 投機行為 | ▰▰▰▰▰▰▱▱▱▱ | 66 | 70 | -4 |
| 散戶情緒 | ▰▰▰▰▰▱▱▱▱▱ | 53 | 51 | +2 |
| 貨幣與信貸環境 | ▰▰▰▰▰▰▰▱▱▱ | 75 | 76 | -1 |
| 結構性槓桿 | ▰▰▰▰▰▰▰▱▱▱ | 72 | 73 | -1 |
| **加權總分** | ▰▰▰▰▰▰▱▱▱▱ | **65【高】** | 67 | -2 |

## §2 歷史錨點相似度
| 錨點 | 相似度 | 條圖 | 標記 |
|---|---:|---|---|
| 1997 早期建設 | 50% | ▰▰▰▰▰▱▱▱▱▱ |  |
| 1998 LTCM 衝擊 | 50% | ▰▰▰▰▰▱▱▱▱▱ |  |
| 1999 晚期狂熱 | 60% | ▰▰▰▰▰▰▱▱▱▱ | ◀ 最貼近 |
| 2000/3 頂點 | 25% | ▰▰▱▱▱▱▱▱▱▱ |  |
| 2021/12 Meme 頂 | 50% | ▰▰▰▰▰▱▱▱▱▱ |  |

## §3 三角訊號
| 指標 | 本次數值 | vs 前次 |
|---|---|---|
| S&P 500 | 7,354.02 | 持平（-0.05%，前次 ~7,357.49） |
| WTI 原油 | $78.94 /bbl | 持平（latest 06-22 與前次同一觀測、無新日序 Δ） |
| 10Y Treasury | 4.40% | —（本次方向不可用——無腳本日序） |

**三者狀態**：穩定共存。本期 S&P 持平（chg -0.05%，距 200DMA +6.2% 未達 +10% 拉伸閾值）、WTI 無新觀測（latest 仍為 06-22）、10Y 週向因 script `decomposition` 不可用而不可判；無任一 ▲ 同向拉伸、亦無可確認之 ▲/▼ 分歧，依「格局判定規則」落「穩定共存（其餘情形）」。惟此「穩定」僅在價格三角面：financing 扳機於非銀私募信貸側持續且本窗內擴大擊發（見「結論」），價格穩定不等於 financing / leverage 環境穩定。

- 股市：S&P 500 7,354.02（FRED SP500，2026-06-26），較前次 ~7,357.49（06-25）持平（-0.05%）；距 200DMA +6.2%、距 52 週 MA +8.03%（皆較前次 +6.56% / +8.44% 再回落，價格拉伸續減弱）。
- WTI 原油：$78.94 /bbl（FRED DCOILWTICO，2026-06-22）；script latest 觀測（06-22）即為前次基準日已採用之同一觀測、無更新日序 Δ，標「持平」；油價自前波回落後維持低檔，對通膨預期上行壓力中性（見扳機鏈）。
- 10Y 殖利率：4.40%（FRED DGS10，2026-06-25）；本次 script `decomposition` 回報 `unavailable_no_daily_history`、無對齊前次基準之週 Δ，方向不可用——無腳本日序，不觸發方向性 ⚠。

**格局轉變**：前次格局「穩定共存」（讀自 report-2026-06-25 之 score.json `regime`），本次仍判「穩定共存」——三資產價格三角面未見同向拉伸（S&P 持平、WTI 無新觀測、10Y 週向不可得）；惟 financing 扳機自非銀私募信貸側持續且擴大擊發（Cliffwater / BCRED / Apollo 等多基金 gate proration），價格穩定與結構性脆弱並存，與前次同調。

**10Y 成因拆解（`ΔDGS10 ≈ ΔDFII10 + ΔT10YIE`，拆的是週變動、非水位）**：本週 Δ 分解不可用——無日序資料。script `decomposition.status = unavailable_no_daily_history`，且 DGS10 / DFII10 最近觀測日（2026-06-25）即為前次基準日、未較前次推進，無對齊前次之週 Δ 可拆。報現貨水位（非 Δ）：DGS10 4.40%、DFII10 2.19%、T10YIE 2.20%。
- ΔDFII10 實質殖利率週變動：不可用——無日序資料
- ΔT10YIE 損益平衡通膨週變動：不可用——無日序資料（script T10YIE 僅含 06-25→06-26 之 1 日 Δ -1 bp，非對齊前次基準的週 Δ，不作週 Δ 採用）
- 判定：不可判——無週 Δ 分解；嚴禁以 breakeven 水位（2.20%）代 Δ。

**扳機鏈：油 → 通膨預期 → Fed 受限 → refinancing 成本**：油價側本週靜默（WTI $78.94，無新觀測）；通膨預期錨定（T10YIE 2.20%、T5YIFR 5y5y forward 2.19%、週 Δ 0 bp），「油 → 通膨預期」環節中性。Fed-constraint 環節仍由 realized 通膨撐住：CPI YoY 4.17%（CPIAUCSL，資料月 2026-05，≥4%，引 script 值非新聞偶得）。Fed 路徑側本週「市場端轉緩」——CME FedWatch 顯示維持 3.50–3.75%（6/17 FOMC 12-0 維持），年底約 78% 維持、約 15% 降息、約 5% 升息，較前次（約四成升息傾向）顯著去除升息定價、降息機率反超升息；惟 Fed 點陣圖 2026 年底中位仍 3.8%（鷹派），realized CPI 4.17% 制約快速放水。整體：扳機鏈「油→通膨預期」靜默、Fed 市場端壓力略紓但 realized 通膨仍封住寬鬆上限。

**⚠ 結論**：扳機狀態：已擊發。判定（決定性，由重至輕取第一個成立者）——私募信貸 gate proration / breach **成立且本窗內持續擴大**：過去 30 日內多檔大型非交易 BDC / interval fund 出現 redemption-request ratio 上行並觸及 quarterly redemption cap 之 gate proration——Cliffwater CLF 第二季申請 ~17%（自 Q1 ~14% 升、cap 自 7% 下調至 5%、按比例分配約 29 cents/dollar，Bloomberg 6/2）、Blackstone BCRED 第二季申請 ~10% NAV（自 ~8% 升、按 5% cap proration、贖回窗 6/7 收）、Apollo（ADS / OCIC-OTIC 家族）第二季退出申請 ~17%（按 5% cap 限縮，CNBC 6/23）、KKR KREST 第二季 tender 按比例分配（贖回壓力延續）；非交易 BDC 板塊延續史上首見之季度淨流出（net inflow→outflow flip，Moody's / PitchBook）。雖 HY OAS 2.78%（FRED 06-25，較前次 2.71% 微升 +7 bps）、IG OAS 0.76% 仍處循環低點（公開 mark-to-market 利差自滿側、尚未反映），非銀信貸側已先行、且較前次持續擴大，正呼應「公開利差可能低估早期 financing 壓力」之設計。三者價格配置歷史意義：估值＋槓桿（crash potential energy）仍高位，financing 扳機自非銀側持續擊發、Fed 受 realized 通膨制約難快速放水，整體配置偏向晚期循環；惟本週投機側明顯降溫（moonshot 0 件、巨型 IPO 延至 2027、FedWatch 去除升息定價、put/call 回升），2000/3-top 色彩較前次消退（見 §2），扳機風險主要集中於 financing 一側。

（以上五段一律用粗體小標、非 `##` / `###` 標題。）

## 六維度評分

| 維度 | 權重 | 分數 | 一句話論述（含來源） |
|---|---:|---:|---|
| 1. 估值溢價 | 22% | 78 | Shiller CAPE 40.70（multpl 06-26，較前次 40.94 微落、仍近紀錄高）、S&P 500 trailing P/E 31.45（multpl 06-26；GuruFocus 法 ~26）、Mag 7 加權 P/E（MAGS）~33.33（StockAnalysis 06-26，較前次 31.86 微升；單一來源、直抓 403）、ECY ≈ 1/40.70 − 2.19/100 ≈ +0.27%（較前次 +0.15% 略遠離零，係實質利率 DFII10 2.29%→2.19% 回落所致，非估值轉便宜）；窗內 sell-side TP 上修以 **EPS-driven 為主**（Micron BofA $950→$1,550，6/23–24，Anthropic HBM take-or-pay 帶動 EPS 能見度；NVDA JPM $265→$280，小幅 earnings-led），非 multiple-driven re-rating，late-cycle 倍數追逐訊號較前期弱；capex 全面仍上修（$725B、MSFT ~$190B、Alphabet $180–190B、AMZN ~$200B、Meta $125–145B），AI compute 無系統性過剩（HBM/DRAM 緊俏、契約價 +20%/翻倍，僅前代 H100 雲端租金回落），惟記憶體成本通膨為毛利風險、且 6/26 CNBC 報導「tokenmaxxing→efficiency」需求敘事微轉；S&P 距 200DMA 自 +6.56% 再落至 +6.2%（價格拉伸續減弱），故較前次 -1。 |
| 2. 市場廣度 | 13% | 32 | RSP（等權）YTD ~+10% 仍領先 SPY（市值權）~+7.5%（financecharts/ytdreturn，06-26），領先幅度自前次 ~+1.3pt 擴大至 ~+2.5–3pt＝參與度偏健康/擴散；Top-10 集中度 ~36–37%（slickcharts/P&I，較前次 ~38% 微降、Mag 7 ~32.7%）；A/D 即時 ratio / 新高新低原始值未取得（barchart/streetstats 等 403，⛔），可考代理：~63% S&P 成分股站上 50DMA（自月初 50% 改善）、淨新高 10 日均 2.3%（自月初 ~10.1% 收斂，新高動能轉弱）。廣度面整體略偏健康（等權領先擴大、集中度微降），新高動能收斂為反向小負，淨 -1。 |
| 3. 投機行為 | 18% | 66 | **明顯降溫**：本週 microcap moonshot **0 件**（✓ SEARCH-VERIFIED（0 件），自前次 2 件 CDT/CAST 退；當週大漲 CAST/VTAK 為動能/軋空、無 2+ 主題催化、不合格）；**巨型 IPO pipeline 轉冷**——OpenAI / Anthropic 6/26 報導**將上市延至 2027**（援引 SpaceX 上市後表現），SpaceX 已於 6/12 上市（$135、~$1.75T）、OpenAI 6/8 / Anthropic 6/1 confidential S-1 仍在 30 日窗內；Cboe equity put/call 0.67（06-25，自前次 0.56 回升＝call 方向性投機略退，confirmation）；IPO 熱度回落（Renaissance IPO 指數 YTD +23.9% vs S&P +8.1%，自前次 +26.3% 降，當週某二手車數位化 IPO 首日 -47%）；themed SPAC 維持（Churchill XI→Agility Robotics 6/24 機器人、SVAQ→EigenQ 6/17 量子）；insider 集中賣出**仍命中**（AMAT CEO Dickerson 6/15–16 83,000 股、CTO Nalamasu 35,000 股、董事 Iannotti ~9,250 股，交易日在 14 日窗緣；NVDA 黃仁勳 6/20–23 100,000 股 ~$14.4M 10b5-1；EDGAR 直連 403、經 StockTitan Form 4 鏡像佐證）。投機四訊號三降一持（moonshot↓、IPO pipeline↓、put/call↓熱度；insider 持平），較前次 -4。 |
| 4. 散戶情緒 | 12% | 53 | 情緒/部位**分歧轉熱**：CNN F&G **25（Fear，06-26，自前次 28 再降溫）** 為唯一偏冷項；但調查/部位/社群三線轉熱——AAII bull **跳升至 44.9%（週 06-25，+8.4pt、6 週來首破歷史均值 37.5%、bull>bear 翻多）**、NAAIM Exposure **98.59（週 06-24，自 92.83 升、近滿倉擁擠多頭，Farrell #9）**、social **重燃**（Wendy's WEN 6/26 r/wallstreetbets 軋空、量 +1,970%、StockTwits #1，DORK 籃 / PLTR / SOUN）；槓桿面 FINRA margin debt $1.42T（2026-05 新印 6/24 發布、創高、+53.7% YoY＝1999/2007/2021 頂部級別、free credit -$991.7B 創低）、家庭持股佔金融資產 45.76%（BOGZ1FL153064486Q，資料日 2026-01-01，近歷史高位）。F&G 偏冷拖低、但 AAII 翻多＋NAAIM 近滿倉＋social 重燃＋margin 創高托高，淨 +2。 |
| 5. 貨幣與信貸環境 | 20% | 75 | 雙向計分，本次落「扳機側（兼自滿側）」：自滿側＝HY OAS 2.78%（FRED 06-25，較前次 2.71% +7 bps、仍循環低）、IG OAS 0.76%（+2 bps，FRED 06-25），全球央行資產負債表持平/緩步 QT（WALCL $6.736T、ECB €6.12T、BOJ ¥664.4 兆、PBoC 轉軟 AFRE +8.4%/M2 +7%）；扳機側＝**私募信貸 gate proration 本窗內持續擴大**（Cliffwater CLF Q2 ~17%、cap 7%→5%、按比例 ~29¢/$ Bloomberg 6/2；BCRED Q2 ~10% NAV、5% cap proration、窗 6/7 收；Apollo Q2 ~17%、5% cap，CNBC 6/23；KKR KREST Q2 tender 比例分配；非交易 BDC 板塊延續史上首見淨流出），且 Fed 受 realized CPI 4.17% 制約。本週 Fed 市場端轉緩（FedWatch 去除升息定價、降息機率 15% 反超升息 5%）與 HY OAS 微升 +7 bps（自滿略退）部分抵銷扳機側擴大，淨 -1。rationale 落「扳機側」。required 輸入齊備：IG OAS 0.76%、WALCL $6.736T、ECB €6.12T、BOJ ¥664.4 兆（BOJ script fetch_failed→WebSearch）皆有現值。 |
| 6. 結構性槓桿 | 15% | 72 | 美國槓桿 ETF 總 AUM **維持紀錄 ~$198B**（leveraged equity ~$157B、日均量 +50%），惟單一個股槓桿 ETF NAV **回落**（SOXL ~$17.3B、NVDL ~$3.7B，均較前次 $34B/$4.5B 顯著縮水，主因 6/23 半導體暴跌後 NAV drawdown；TQQQ ~$31.3B）＝產品層面小幅去槓桿；單一個股槓桿 ETF **發行續垂直**（窗內 ~25+ 檔：SpaceX 10 檔 6/15、Leverage Shares 9 檔 6/23、Roundhill 2X DRAM「RAM」6/24、Tradr 5 檔 6/26 公告 7/1 上市、SK Hynix 槓桿 ETF 7/2 生效）；SPX 0DTE 佔比 ~60–62%（Cboe，紀錄區間）；SKEW 143（尾端避險偏高）、VIX ~18.9 contango（即期平靜）、**股債相關轉正**（60/40 分散失效、跨資產自滿之脆弱訊號，AQR/VaaS 6 月）；AI 基建債務窗內**擴大**（Nvidia $25B IG 債 6/15 史上最大＋circular financing 節點、Meta El Paso ~$13B SPV ＋路州 ~$29–30B Blue Owl/PIMCO、Applied Digital $1.59B 票據 6/9＋$550M RCF 5/29、CoreWeave 關聯 $850M 垃圾債 6/2）。全球擴散訊號（2+ 非美市場新核准）**本週未觸發**（韓國反向監理回頭）。發行/AI 債續熱 vs 單股 AUM 回落＋擴散未觸發，淨 -1。 |

各維度評分採 0–100，分數愈高＝該維度對泡沫風險之貢獻愈大。

## 綜合分數

| 維度 | 權重 | 分數 | 加權貢獻 |
|---|---:|---:|---:|
| 估值溢價 | 22% | 78 | 17.16 |
| 市場廣度 | 13% | 32 | 4.16 |
| 投機行為 | 18% | 66 | 11.88 |
| 散戶情緒 | 12% | 53 | 6.36 |
| 貨幣與信貸環境 | 20% | 75 | 15.00 |
| 結構性槓桿 | 15% | 72 | 10.80 |
| **加權總分** | 100% | — | **65.36 → 65** |

加權總分 = Σ(分數 × 權重)/100 = 65.36，half-up 四捨五入 → **65**。風險等級對照（40–64 警戒／65–84 高）：**65 → 高**。

邊界帶：總分 65 距 警戒/高 邊界 ≤ 2 分（落 63–66 帶），評分固有噪音約 ±2–3，等級判讀需保留餘地（本週小幅降溫使總分自 67 降至 65，緊貼 警戒/高 分界）。

## 歷史泡沫週期對比

相似度計算：checklist v2

相似度＝命中數 ÷ 特徵數 × 100，四捨五入到最接近的 5%；無資料特徵記未命中。最貼近錨點全列命中明細，其餘列關鍵差異摘要。

**1999 晚期狂熱（6/10 = 60%）◀ 最貼近**
- ① 估值溢價 ≥75：**命中**（78）
- ② CAPE ≥38：**命中**（40.70）
- ③ 投機行為 ≥60：**命中**（66）
- ④ 本週 moonshot ≥1 或無營收 IPO 佔比偏高：未命中（moonshot 0 件；當週 IPO 熱度回落、無顯著無營收佔比訊號）
- ⑤ 市場廣度 ≥45（轉窄）：未命中（32，廣度反而擴散/RSP 領先擴大）
- ⑥ D5 落自滿側且 HY OAS <3.5%：**命中**（自滿側＋HY OAS 2.78%）
- ⑦ 結構性槓桿 ≥60：**命中**（72）
- ⑧ 散戶情緒 ≥55：未命中（53）
- ⑨ 巨型 IPO pipeline 活躍（30 日內具名 S-1/定價）：**命中**（OpenAI 6/8、Anthropic 6/1 confidential S-1；SpaceX 6/12 定價上市；惟 OpenAI/Anthropic 實際上市已延至 2027，pipeline 前瞻轉冷）
- ⑩ 扳機狀態＝未擊發：未命中（已擊發）

**其餘錨點（關鍵差異摘要）**
- 1997 早期建設（4/8 = 50%）：命中 ②廣度<45、④capex 上修、⑤散戶<55（53）、⑦HY OAS<4% 且本次未實質走闊（+7 bps 視為噪音）；但估值 78 過高、投機/槓桿仍熱、扳機已擊發，與「早期」不符。
- 1998 LTCM 衝擊（4/8 = 50%）：命中 ③具名非銀/槓桿機構壓力披露（多基金私募信貸 gate proration）、⑤估值≥60（78）、⑥扳機≥初啟（已擊發）、⑧ΔT10YIE≤0（T10YIE 1 日 -1 bp，通膨預期非主因）；但 HY OAS 未走闊（+7 bps）、無 ≥5% 回檔、FedWatch 雖去升息但基準仍維持（非實質轉鴿降息）、廣度未急轉弱。與前次同為 50%。
- 2000/3 頂點（2/8 = 25%）：命中 ②扳機≥初啟（已擊發）、⑥insider 集中賣出（AMAT 14 日內合格 cluster）；但估值未達 ≥85、廣度未極窄、無 dev200 自 >+10% 回落、**投機已降至 66<70**、散戶未達 ≥65、**貨幣未轉緊**（FedWatch 反去除升息定價、ΔT10YIE 未主導上行）。**較前次（50%）顯著回落**——投機降溫與 Fed 升息定價消退使 top 過渡色彩消退。
- 2021/12 Meme 頂（4/8 = 50%）：命中 ②社群投機熱（Wendy's WEN 等具名軋空，**本次新命中**）、③槓桿≥65（72）、⑤margin debt YoY≥+40%（+53.7%）、⑧CPI≥4% 且 Fed 尚未實質緊縮；但散戶情緒未達 65、本週 moonshot 0（自前次命中轉未命中）、廣度未背離、央行資產負債表未擴張。與前次同為 50%（社群熱換入、moonshot 換出）。

**解讀**：本週最似 **1999 晚期狂熱**（60%，自前次 70% 回落，主因 moonshot 0 件使 ④ 失命中）——高估值、結構性槓桿與巨型 IPO 名單並存，但廣度反而擴散、散戶 F&G 28→25 偏冷、投機降溫。關鍵變化在 **2000/3 頂點相似度自 50% 回落至 25%**（投機自 70 降至 66、FedWatch 去除升息定價＝貨幣未轉緊），自前次的「向 2000 初期過渡」色彩本週**消退**，配置回到「1999 晚期狂熱＋非銀 financing 扳機獨立擊發」的格局。結構性槓桿以期間調整代理觀察（margin debt YoY +53.7%、0DTE ~60–62%、槓桿 ETF AUM $198B、AI 基建債務擴大）在 1999/2021 類比中皆達高位；S&P 距 200DMA +6.2%、距 52 週 MA +8.03%（Farrell #1/#2，較前次再回落），長期相對指數成長趨勢偏離之文章錨點（Dot-com ~95%、1929 ~110%、當前 AI 週期 ~147%）僅供敘事脈絡，不納入每週計分。

## 機構情緒對照

本次無新機構調查數據。（最近一次為 BofA 6 月全球 FMS，外勤 6/5–11、發布於前次 run 前，非本次新增；JPM 亦無本次新增之獨立機構部位調查；未見 7 月 FMS。）背景參照：6 月 FMS 顯示經理人「減碼風險、提高現金與債券」，美股超配自 5 月淨 +20%（紀錄樂觀）回落至 6 月淨 +17%，三大尾端風險為（1）二次通膨 34%、（2）AI 泡沫 28%、（3）債券殖利率失序上行 19%；BofA 定調「非風險資產大頂、僅去風險」。

另：NAAIM Exposure Index 98.59（週 2026-06-24，自 92.83 升、主動經理人近滿倉＝擁擠多頭，反向風險升高，Farrell #9）。NAAIM 於「散戶情緒」維度作 positioning-crowding 的 confirmation cross-check 計分，此處僅作敘述對照，不重複計分。私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）本窗內於多檔半流動性基金持續擴大（Cliffwater / BCRED / Apollo / KKR），BofA 預期 redemption 申請於 2026-Q2 見高峰，屬機構資金面的 financing 緊縮訊號。

## 本次新增訊號

vs 前次（4 天前，基準 report-2026-06-25）：

- **估值溢價 78（Δ -1）**：CAPE 40.70（微落）、Mag 7 P/E ~33.33（微升）、ECY ≈ +0.27%（較前次 +0.15% 略遠離零，係實質利率回落、非轉便宜）；窗內 TP 上修以 EPS-driven 為主（Micron $950→$1,550、NVDA $265→$280），multiple-driven re-rating 訊號弱；S&P 距 200DMA +6.56%→+6.2%（拉伸續減弱），故微降。
- **市場廣度 32（Δ -1）**：RSP YTD ~+10% 對 SPY ~+7.5%、領先幅度自 ~+1.3pt 擴大至 ~+2.5–3pt（廣度擴散）、Top-10 ~38%→~36–37%（微降）；新高動能收斂（淨新高 10 日均 ~10.1%→2.3%）為反向小負；A/D 即時 ratio 未取得（來源 403，⛔），未以舊值代當期。
- **投機行為 66（Δ -4）**：**microcap moonshot 自 2 件轉 0 件**（✓ SEARCH-VERIFIED（0 件））、**OpenAI/Anthropic 上市延至 2027**（6/26，liquidity-drain 風險前瞻轉緩）、Cboe put/call 0.56→0.67（call 方向性投機退）、IPO 指數 YTD +26.3%→+23.9%（熱度回落、當週一檔 IPO 首日 -47%）；insider 集中賣出仍命中（AMAT cluster 6/15–16＋NVDA 黃仁勳 6/20–23，窗內、Form 4 鏡像佐證）、themed SPAC 維持（Agility Robotics 6/24）。投機四訊號三降一持。
- **散戶情緒 53（Δ +2）**：CNN F&G 28→**25（Fear，再降溫）** 為唯一偏冷；但 **AAII bull 36.6%→44.9%（翻多、6 週來首破均值）**、**NAAIM 92.83→98.59（近滿倉）**、**social 重燃（Wendy's WEN 6/26 軋空、量 +1,970%）**、margin debt $1.42T 創高 +53.7% YoY、家庭持股 45.76% 近高位。部位/調查/社群轉熱托高主分。
- **貨幣與信貸環境 75（Δ -1）【扳機側】**：雙向計分——自滿側（HY OAS 2.71%→2.78% +7 bps、IG OAS 0.76% 循環低）＋扳機側持續擊發。質化新訊號（雙向 Δ 遮蔽防護）：**私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）本窗內持續且擴大**——Cliffwater CLF Q2 ~17%（自 14% 升、cap 7%→5%、按比例 ~29¢/$，Bloomberg 6/2）、BCRED Q2 ~10% NAV（自 ~8% 升、5% cap proration、窗 6/7 收）、Apollo Q2 ~17%（5% cap 限縮，CNBC 6/23 為最新披露）、KKR KREST Q2 tender 比例分配；非交易 BDC 板塊延續史上首見季度淨流出（net inflow→outflow flip）。屬「扳機側」financing 壓力持續擊發，即使公開利差 Δ 不顯著（HY OAS +7 bps）、分數僅 -1（因先前已因自滿＋扳機偏高），仍須列示。另：FedWatch 本週去除升息定價、降息機率（15%）反超升息（5%），Fed 市場端壓力略紓（自滿略退），與扳機側擴大互抵。
- **結構性槓桿 72（Δ -1）**：槓桿 ETF 總 AUM 維持 $198B、惟單一個股槓桿 ETF NAV 回落（SOXL $34B→~$17.3B、NVDL $4.5B→~$3.7B，6/23 半導體暴跌後 drawdown）；單股槓桿 ETF 發行續垂直（Roundhill 2X DRAM 6/24、Tradr 5 檔 6/26→7/1、SK Hynix 7/2）；SPX 0DTE ~60–62%、SKEW 143、**股債相關轉正**（跨資產自滿脆弱訊號）；AI 基建債務窗內擴大（Nvidia $25B IG 債 6/15、Meta El Paso ~$13B＋路州 ~$29–30B、Applied Digital $1.59B 6/9＋$550M RCF 5/29、CoreWeave 關聯 $850M 垃圾債 6/2）。

全球槓桿擴散訊號：**本週擴散訊號未觸發**（韓國本週為**監理回頭檢討/限制**——FSS 警示 5 月核准單一個股槓桿 ETF「過於倉促」、6/23 KOSPI 近 -10% flash crash、Samsung/SK Hynix 觸發熔斷；TWSE / JPX 本週無單一個股槓桿新核准、ESMA 為 passported 掛牌非核准）。美國端單一個股槓桿 ETF 雖續垂直發行，但「全球擴散訊號」特例規則限於 2+ 非美市場同週核准，本週不適用該 floor。

## 數據附錄

### Coverage table（每個 `# Data sources` bullet 一列；共 47 列）

| # | 維度 / source bullet | 預定來源與方法 | 狀態 |
|---:|---|---|---|
| 1 | 估值-S&P 500 P/E & Shiller CAPE | multpl/GuruFocus [SEARCH] | ✓ SEARCH-VERIFIED（CAPE 40.70；P/E 31.45；見 raw） |
| 2 | 估值-Mag 7 加權 P/E & AI leader P/S | MAGS/StockAnalysis [SEARCH] | ✓ SEARCH-VERIFIED（MAGS ~33.33，單一來源、直抓 403） |
| 3 | 估值-Analyst TP upgrade decomposition | sell-side 14 日掃描 [SEARCH] | ✓ SEARCH-VERIFIED（Micron BofA $950→$1,550 EPS-driven 6/23–24；NVDA JPM $265→$280；見 raw） |
| 4 | 估值-S&P 500 price-trend deviation | scripts/fetch_macro.py `sp500_trend` | ✓ API（dev200 +6.2%、dev52w +8.03%） |
| 5 | 廣度-RSP vs SPY YTD divergence | financecharts/ytdreturn [SEARCH] | ✓ SEARCH-VERIFIED（RSP ~+10% / SPY ~+7.5%） |
| 6 | 廣度-Top-10 concentration | slickcharts/P&I [SEARCH] | ✓ SEARCH-VERIFIED（~36–37%、Mag 7 ~32.7%） |
| 7 | 廣度-A/D ratio、new high/low | StockCharts/Barchart/streetstats [SEARCH] | ⛔ FETCH FAILED（即時 A/D ratio / 新高低原始值；來源 403。可考代理：~63% 站上 50DMA、淨新高 10 日均 2.3%，rationale 已註明未以舊值代當期） |
| 8 | 散戶-CNN Fear & Greed | cnn.com [SEARCH] | ✓ SEARCH-VERIFIED（25 Fear，MacroMicro 鏡像） |
| 9 | 散戶-Margin Debt + ratio + YoY | FINRA/dshort [SEARCH] | ✓ SEARCH-VERIFIED（$1.42T、+53.7% YoY，2026-05 新印 6/24 發布） |
| 10 | 散戶-AAII Investor Sentiment | aaii.com [SEARCH] | ✓ SEARCH-VERIFIED（bull 44.9%，週 06-25 翻多） |
| 11 | 散戶-社交情緒代理（Reddit/X） | [SEARCH] best-effort | ✓ SEARCH-VERIFIED（Wendy's WEN 6/26 軋空、量 +1,970%；DORK 籃） |
| 12 | 散戶-家庭持股佔金融資產比 | fetch_macro.py BOGZ1FL153064486Q | ✓ API（45.76%，資料日 2026-01-01） |
| 13 | 散戶-NAAIM Exposure Index | naaim/ycharts [SEARCH] best-effort | ✓ SEARCH-VERIFIED（98.59，週 06-24） |
| 14 | 機構-BofA FMS & JPM survey | [SEARCH] best-effort（月頻） | ✓ SEARCH-VERIFIED（6 月 FMS；非本次新增、無 7 月 FMS） |
| 15 | 貨幣-Fed funds DFEDTARU/DFEDTARL | fetch_macro.py FRED | ✓ API（3.75/3.50，Δ0） |
| 16 | 貨幣-HY OAS BAMLH0A0HYM2 | fetch_macro.py FRED | ✓ API（2.78%，較前次 +7 bps） |
| 17 | 貨幣-IG OAS BAMLC0A0CM | fetch_macro.py FRED | ✓ API（0.76%） |
| 18 | 貨幣-10Y DGS10 | fetch_macro.py FRED | ✓ API（4.40%，06-25；無日序週 Δ） |
| 19 | 貨幣-10Y real DFII10 | fetch_macro.py FRED | ✓ API（2.19%，06-25） |
| 20 | 貨幣-10Y breakeven T10YIE | fetch_macro.py FRED | ✓ API（2.20%，06-26） |
| 21 | 貨幣-WTI DCOILWTICO | fetch_macro.py FRED | ✓ API（$78.94，06-22） |
| 22 | 貨幣-CPI YoY CPIAUCSL | fetch_macro.py FRED（yoy_pct） | ✓ API（4.17%，資料月 2026-05） |
| 23 | 貨幣-5y5y forward T5YIFR | fetch_macro.py FRED | ✓ API（2.19%，Δ0，06-26） |
| 24 | 貨幣-FedWatch 隱含路徑 | CME/growbeansprout [SEARCH] best-effort | ✓ SEARCH-VERIFIED（維持 3.50–3.75%；年底 ~78% 維持/~15% 降/~5% 升） |
| 25 | 貨幣-Fed balance sheet WALCL | fetch_macro.py FRED | ✓ API（$6,735,645M，06-24） |
| 26 | 貨幣-全球央行 ECB/BOJ | fetch_macro.py ECBASSETSW + JPNASSETS（BOJ 腳本 fetch_failed→WebSearch） | ✓ SEARCH-VERIFIED（ECB €6,119,940M API；BOJ ¥664.4 兆 search，worst-case 取 BOJ search） |
| 27 | 貨幣-PBoC aggregate financing | [SEARCH] best-effort | ✓ SEARCH-VERIFIED（AFRE +8.4% YoY、M2 +7%、淨投放 ~¥2T YTD，方向性） |
| 28 | 貨幣-私募信貸/非銀基金贖回壓力 | [SEARCH] best-effort | ✓ SEARCH-VERIFIED（多基金 gate proration 本窗內擴大；見 raw） |
| 29 | AI-Hyperscaler capex guidance | 財報/[SEARCH] required | ✓ SEARCH-VERIFIED（$725B、全面上修，Q1 set、carry-forward） |
| 30 | AI-token volume growth | [SEARCH] best-effort | ✓ SEARCH-VERIFIED（Google >3.2 quadrillion tokens/月、~7x YoY；6/26 efficiency-shift 反訊號） |
| 31 | AI-OpenAI/Anthropic 營收 | [SEARCH] best-effort | ✓ SEARCH-VERIFIED（Anthropic ~$45B / OpenAI ~$33B ARR，press 估計、有會計爭議） |
| 32 | AI-hyperscaler 客戶集中度 | 財報 [SEARCH] best-effort | ✓ SEARCH-VERIFIED（CoreWeave MSFT ~67%、top-3 >80%、backlog $99.4B） |
| 33 | AI-compute 供需/過剩 | [SEARCH] best-effort | ✓ SEARCH-VERIFIED（無系統性過剩；HBM/DRAM +20%/翻倍緊俏，僅 H100 租金回落） |
| 34 | 投機-+AI rename/SPAC/無營收 IPO 潮 | [SEARCH] 7 日 | ✓ SEARCH-VERIFIED（無 literal AI-rename；Agility Robotics 6/24、EigenQ 6/17 themed SPAC） |
| 35 | 投機-IPO market heat | Renaissance/Nasdaq [SEARCH] | ✓ SEARCH-VERIFIED（IPO 指數 YTD +23.9%、3 IPO+4 SPAC、一檔首日 -47%） |
| 36 | 投機-Microcap moonshots | Finviz/Benzinga [SEARCH] required | ✓ SEARCH-VERIFIED（0 件；CAST/VTAK 無 2+ 主題催化、不合格） |
| 37 | 投機-Upcoming AI IPOs | S-1/具名報導 [SEARCH] | ✓ SEARCH-VERIFIED（OpenAI 6/8、Anthropic 6/1 S-1；6/26 延至 2027；SpaceX 6/12 已上市） |
| 38 | 投機-Insider selling Form 4 | SEC EDGAR required | ✓ SEARCH-VERIFIED（AMAT cluster 6/15–16＋NVDA 黃仁勳 6/20–23；EDGAR 直連 403、Form 4 鏡像佐證，見 raw） |
| 39 | 投機-Cboe equity put/call | Cboe/ycharts [SEARCH] best-effort | ✓ SEARCH-VERIFIED（0.67，06-25） |
| 40 | 結構-美國槓桿 ETF AUM | etf.com/ETFGI [SEARCH] | ✓ SEARCH-VERIFIED（總 ~$198B；TQQQ ~$31.3B、SOXL ~$17.3B、NVDL ~$3.7B） |
| 41 | 結構-美國單一個股槓桿 ETF 核准/發行 | SEC/etf.com [SEARCH] | ✓ SEARCH-VERIFIED（窗內 ~25+ 檔：SpaceX 10、Leverage Shares 9 6/23、Roundhill DRAM 6/24、Tradr 5 6/26、SK Hynix 7/2） |
| 42 | 結構-全球槓桿產品核准（KRX/TWSE/JPX/ESMA） | 各監理機關 [SEARCH] best-effort | ✗ NOT DISCLOSED（本週無新核准；韓國為監理檢討/限制，非核准；TWSE/JPX/ESMA 無英文新核准） |
| 43 | 結構-0DTE option volume | Cboe/SpotGamma [SEARCH] | ✓ SEARCH-VERIFIED（SPX 0DTE ~60–62%） |
| 44 | 結構-Options total volume（OCC） | OCC/Cboe [SEARCH] | ✓ SEARCH-VERIFIED（2026-05 equity 803.1M +25.5% YoY、總 ~1.47B/月） |
| 45 | 結構-VIX/SKEW/stock-bond correlation | Cboe/SpotGamma [SEARCH] | ✓ SEARCH-VERIFIED（VIX ~18.9 contango、SKEW 143、股債相關轉正） |
| 46 | 結構-margin debt/市值 比（confirmation） | 引用散戶維度 | derived（cross-reference，不重複計分） |
| 47 | 結構-AI 基建債務/vendor-financing | [SEARCH] best-effort | ✓ SEARCH-VERIFIED（窗內 Nvidia $25B 6/15、Meta El Paso $13B/路州 $29–30B、Applied Digital $1.59B 6/9、CoreWeave 關聯 $850M 6/2） |

### 原始數據表（每筆計分用資料一列）

| 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|
| Shiller CAPE | 40.70 | multpl https://www.multpl.com/shiller-pe | 2026-06-26 | 2026-06-29 (UTC+8) |
| S&P 500 trailing P/E | 31.45（multpl；GuruFocus 法 ~26） | https://www.multpl.com/ | 2026-06-26 | 2026-06-29 (UTC+8) |
| Mag 7 加權 P/E（MAGS） | ~33.33（單一來源、直抓 403） | StockAnalysis https://stockanalysis.com/etf/mags/ | 2026-06-26 | 2026-06-29 (UTC+8) |
| S&P 500 spot | 7,354.02 | FRED API (series_id=SP500) | 2026-06-26 | 2026-06-29 (UTC+8) |
| S&P 200DMA / 偏離 | 6,924.97 / +6.2% | FRED API (SP500, sp500_trend) | 2026-06-26 | 2026-06-29 (UTC+8) |
| S&P 52週MA / 偏離 | 6,807.46 / +8.03% | FRED API (SP500, sp500_trend) | 2026-06-26 | 2026-06-29 (UTC+8) |
| S&P prior spot / chg | 7,357.49 / -0.05% | FRED API (sp500_trend prior_spot) | 2026-06-25 | 2026-06-29 (UTC+8) |
| Analyst TP（Micron BofA） | $950→$1,500→$1,550（EPS-driven） | https://www.thestreet.com/investing/stocks/mu-micron-stock-price-target-bank-of-america-raises-june-2026 | 2026-06-23~24 | 2026-06-29 (UTC+8) |
| Analyst TP（NVDA JPM） | $265→$280（earnings-led） | https://finance.yahoo.com/news/jpmorgan-revamps-nvidia-stock-price-153700952.html | 2026-06（約） | 2026-06-29 (UTC+8) |
| RSP YTD / SPY YTD | ~+10% / ~+7.5%（領先擴大） | financecharts/ytdreturn https://www.ytdreturn.com/rsp/ | 2026-06-26 | 2026-06-29 (UTC+8) |
| Top-10 集中度 | ~36–37%（Mag 7 ~32.7%、NVDA ~7.0%） | Slickcharts/P&I https://www.slickcharts.com/sp500 | 2026-06 | 2026-06-29 (UTC+8) |
| 廣度代理（50DMA/新高） | ~63% 站上 50DMA；淨新高 10 日均 2.3% | streetstats https://streetstats.finance/markets/breadth-momentum/SP500 | 2026-06-24~26 | 2026-06-29 (UTC+8) |
| A/D ratio（即時） | 未取得（來源 403，⛔） | StockCharts/Barchart | — | 2026-06-29 (UTC+8) |
| CNN F&G | 25（Fear，盤中 24.77） | https://www.cnn.com/markets/fear-and-greed（鏡像 macromicro 50108） | 2026-06-26 | 2026-06-29 (UTC+8) |
| FINRA margin debt | $1.4156T（+8.5% MoM、+53.7% YoY；free credit -$991.7B） | dshort https://www.advisorperspectives.com/dshort/updates/2026/06/24/margin-debt-finra | 2026-05（6/24 發布） | 2026-06-29 (UTC+8) |
| AAII bull | 44.9%（翻多、+8.4pt） | https://www.aaii.com/sentimentsurvey | 週 2026-06-25 | 2026-06-29 (UTC+8) |
| 家庭持股佔金融資產 | 45.76% | FRED API (series_id=BOGZ1FL153064486Q) | 2026-01-01 | 2026-06-29 (UTC+8) |
| NAAIM Exposure | 98.59 | naaim.org / ycharts | 週 2026-06-24 | 2026-06-29 (UTC+8) |
| Social（Wendy's WEN） | 6/26 軋空、量 +1,970%（~203M 股）、StockTwits #1 | Yahoo/AltIndex https://altindex.com/wallstreetbets | 2026-06-26 | 2026-06-29 (UTC+8) |
| Fed funds（上/下限） | 3.75% / 3.50% | FRED API (DFEDTARU/DFEDTARL) | 2026-06-28 | 2026-06-29 (UTC+8) |
| HY OAS | 2.78%（較前次 2.71% +7 bps） | FRED API (series_id=BAMLH0A0HYM2) | 2026-06-25 | 2026-06-29 (UTC+8) |
| IG OAS | 0.76% | FRED API (series_id=BAMLC0A0CM) | 2026-06-25 | 2026-06-29 (UTC+8) |
| 10Y nominal (DGS10) | 4.40%（無日序週 Δ） | FRED API (series_id=DGS10) | 2026-06-25 | 2026-06-29 (UTC+8) |
| 10Y real (DFII10) | 2.19% | FRED API (series_id=DFII10) | 2026-06-25 | 2026-06-29 (UTC+8) |
| 10Y breakeven (T10YIE) | 2.20%（1 日 Δ -1 bp） | FRED API (series_id=T10YIE) | 2026-06-26 | 2026-06-29 (UTC+8) |
| WTI | $78.94（latest 06-22，無新觀測） | FRED API (series_id=DCOILWTICO) | 2026-06-22 | 2026-06-29 (UTC+8) |
| CPI YoY | 4.17% | FRED API (series_id=CPIAUCSL, yoy_pct) | 2026-05-01 | 2026-06-29 (UTC+8) |
| 5y5y forward (T5YIFR) | 2.19%（Δ0） | FRED API (series_id=T5YIFR) | 2026-06-26 | 2026-06-29 (UTC+8) |
| Fed BS (WALCL) | $6,735,645M | FRED API (series_id=WALCL) | 2026-06-24 | 2026-06-29 (UTC+8) |
| ECB BS (ECBASSETSW) | €6,119,940M | FRED API (series_id=ECBASSETSW) | 2026-06-19 | 2026-06-29 (UTC+8) |
| BOJ BS（總資產） | ¥664.4 兆（JPNASSETS 腳本 fetch_failed→search） | Trading Economics https://tradingeconomics.com/japan/central-bank-balance-sheet | 2026-05 | 2026-06-29 (UTC+8) |
| FedWatch | 維持 3.50–3.75%（6/17 FOMC 12-0）；年底 ~78% 維持/~15% 降/~5% 升；點陣圖中位 3.8% | CME FedWatch / growbeansprout / centralbank.watch | 2026-06-27 | 2026-06-29 (UTC+8) |
| PBoC | AFRE +8.4% YoY、M2 +7%、淨投放 ~¥2T YTD | China Daily Asia / Macau Business | 2026-05 | 2026-06-29 (UTC+8) |
| 私募信貸 gate（多基金） | Cliffwater CLF Q2 ~17%（cap 7%→5%、~29¢/$）；BCRED Q2 ~10% NAV（5% cap）；Apollo Q2 ~17%（5% cap，CNBC 6/23）；KKR KREST Q2 tender 比例分配；BDC 板塊淨流出 | Bloomberg/CNBC/PitchBook https://www.cnbc.com/2026/06/23/apollo-private-credit-fund-withdrawals-redemptions.html | 2026-Q2（窗內 6/2~6/23 披露） | 2026-06-29 (UTC+8) |
| Hyperscaler capex 2026 | $725B（+77% YoY）；MSFT ~$190B、Alphabet $180–190B、AMZN ~$200B、Meta $125–145B | Tom's Hardware https://www.tomshardware.com/tech-industry/big-tech/big-techs-ai-spending-plans-reach-725-billion | 2026-04~06 | 2026-06-29 (UTC+8) |
| AI token 成長 | Google >3.2 quadrillion tokens/月（~7x YoY）；6/26「tokenmaxxing→efficiency」反訊號 | Google blog / CNBC https://www.cnbc.com/2026/06/26/openai-anthropic-new-ai-spending-reality-as-users-shift-to-efficiency.html | 2026-05~06 | 2026-06-29 (UTC+8) |
| OpenAI/Anthropic ARR | Anthropic ~$45B、OpenAI ~$33B（press 估計、會計爭議） | The Information / Sacra https://www.theinformation.com/articles/openai-tops-25-billion-annualized-revenue-anthropic-narrows-gap | 2026-05~06 | 2026-06-29 (UTC+8) |
| AI 客戶集中度 | CoreWeave MSFT ~67% FY25、top-3 >80%、backlog $99.4B（3/31） | CoreWeave Q1 8-K (SEC) https://www.sec.gov/Archives/edgar/data/0001769628/000176962826000220/coreweave1q26earningspress.htm | 2026-Q1 | 2026-06-29 (UTC+8) |
| AI compute 供需 | 無系統性過剩；HBM3E +20%/DRAM 翻倍、SK hynix/Micron 2026 售罄；僅 H100 雲端租金 -64~75% | TrendForce/SK hynix https://news.skhynix.com/2026-market-outlook-focus-on-the-hbm-led-memory-supercycle/ | 2026-Q2 | 2026-06-29 (UTC+8) |
| Microcap moonshot | 0 件（CAST/VTAK 為軋空/動能、無 2+ 主題催化、不合格） | StockTitan/Benzinga（已掃 Finviz/Yahoo/StockTwits） | 2026-06-22~29 | 2026-06-29 (UTC+8) |
| themed SPAC | Churchill XI→Agility Robotics（6/24 機器人）；SVAQ→EigenQ（6/17 量子，窗緣） | Boardroom Alpha https://www.boardroomalpha.com/research/spac-market-update-june-24-2026-ccxi-qsea | 2026-06-24 | 2026-06-29 (UTC+8) |
| IPO 熱 | Renaissance IPO 指數 YTD +23.9% vs S&P +8.1%（自 +26.3% 降）；3 IPO+4 SPAC；一檔首日 -47% | Renaissance https://www.renaissancecapital.com/IPO-Center/News/120104 | 2026-06-26 | 2026-06-29 (UTC+8) |
| 巨型 IPO pipeline | OpenAI 6/8 / Anthropic 6/1 S-1；6/26 報導延至 2027；SpaceX 6/12 上市（$135、~$1.75T） | Crypto Briefing https://cryptobriefing.com/openai-anthropic-ipo-filings-spacex/ | 2026-06-01~26 | 2026-06-29 (UTC+8) |
| Insider（AMAT cluster） | CEO Dickerson 83,000 股（6/15–16）；CTO Nalamasu 35,000 股；董事 Iannotti ~9,250 股 | StockTitan Form 4 鏡像 https://www.stocktitan.net/sec-filings/AMAT/form-4-applied-materials-inc-de-insider-trading-activity-cb3a6ad6dbd2.html（EDGAR 直連 403） | 交易 2026-06-15~16 | 2026-06-29 (UTC+8) |
| Insider（NVDA） | 黃仁勳 100,000 股 ~$14.4M（6/20、6/23，10b5-1，單人非 cluster） | Globe&Mail / OpenInsider | 交易 2026-06-20~23 | 2026-06-29 (UTC+8) |
| Cboe equity put/call | 0.67（自前次 0.56 回升） | ycharts https://ycharts.com/indicators/cboe_equity_put_call_ratio | 2026-06-25 | 2026-06-29 (UTC+8) |
| 槓桿 ETF 總 AUM | ~$198B；TQQQ ~$31.3B、SOXL ~$17.3B、NVDL ~$3.7B、TSLL ~$4–4.9B | Crypto Briefing/Seeking Alpha https://cryptobriefing.com/leveraged-etfs-record-198b-aum/ | 2026-06 | 2026-06-29 (UTC+8) |
| 美單股槓桿 ETF 發行（窗內） | SpaceX ~10 檔（6/15）；Leverage Shares 9 檔（6/23）；Roundhill 2X DRAM「RAM」（6/24）；Tradr 5 檔（6/26→7/1）；SK Hynix（7/2） | PRNewswire https://www.prnewswire.com/news-releases/leverage-shares-by-themes-unveils-nine-new-2x-single-stock-etfs-tracking-key-players-in-the-technology-supply-chain-302807131.html | 2026-06-15~26 | 2026-06-29 (UTC+8) |
| 韓國槓桿 ETF 監理回頭 | FSS 警示「過於倉促」、6/23 KOSPI 近 -10% flash crash、Samsung/SK Hynix 熔斷 | KED Global https://www.kedglobal.com/policy/newsView/ked202606230001 | 2026-06-23~24 | 2026-06-29 (UTC+8) |
| SPX 0DTE 佔比 | ~60–62%（紀錄區間） | Cboe https://www.cboe.com/insights/posts/the-state-of-the-options-industry-2025 | 2026（最新） | 2026-06-29 (UTC+8) |
| OCC options 量 | 2026-05 equity 803.1M（+25.5% YoY）、index 122.6M、總 ~1.47B/月；4 月創高 | OCC https://www.theocc.com/market-data/market-data-reports/volume-and-open-interest/monthly-weekly-volume-statistics | 2026-05 | 2026-06-29 (UTC+8) |
| VIX / SKEW / 股債相關 | VIX ~18.9（contango）、SKEW 143.14、股債相關轉正（60/40 失效） | Cboe/AQR https://www.cboe.com/us/indices/dashboard/skew/ | 2026-06-23~25 | 2026-06-29 (UTC+8) |
| AI 基建債務（窗內） | Nvidia $25B IG 債（6/15，史上最大、circular）；Meta El Paso ~$13B SPV ＋路州 ~$29–30B；Applied Digital $1.59B（6/9）＋$550M RCF（5/29）；CoreWeave 關聯 $850M 垃圾債（6/2） | Bloomberg/SEC https://www.bloomberg.com/news/articles/2026-06-15/nvidia-kicks-off-first-high-grade-bond-offering-since-2021 | 2026-05-29~06-15 | 2026-06-29 (UTC+8) |

附註：(1) 巨集數據由 `scripts/fetch_macro.py`（FRED API，urllib）取得，所有 FRED 列均以 series_id 引用、未含任何 api_key。(2) JPNASSETS（BOJ）腳本本次 `fetch_failed`，改以 WebSearch 取現貨（¥664.4 兆，Trading Economics，資料月 2026-05），ECB/BOJ 合併列 worst-case 取 BOJ 之 search 狀態。(3) §3 三角訊號之 S&P chg 取自 script `sp500_trend.chg_pct`（-0.05% 持平）；10Y 因 script `decomposition` 回報 `unavailable_no_daily_history`、且 DGS10/DFII10 最近觀測（06-25）即前次基準日、未推進，無對齊前次之週 Δ，方向標 —、10Y 成因拆解標「本週 Δ 分解不可用——無日序資料」、不觸發方向性 ⚠；WTI script latest（06-22）即前次已採用之同一觀測、無新日序 Δ，標「持平」。(4) Insider AMAT cluster：SEC EDGAR / openinsider 直連經 egress proxy 403（組織政策），故以 StockTitan Form 4 鏡像佐證，交易日 6/15–16 在 14 日窗緣；NVDA 黃仁勳為單人 10b5-1、非 cluster。(5) 私募信貸多基金數據多為 Q2 2026 披露於本窗內（6/2~6/23），確切 as-of 日於次級來源略糊，金額/比例可靠、精確日以 SEC SC TO-I 為準。(6) AI infra 債務窗內新訊號為 Nvidia $25B 債（6/15）、Applied Digital $1.59B 票據（6/9）＋$550M RCF（5/29）、CoreWeave 關聯 $850M 垃圾債（6/2）、Meta El Paso/路州（進行中）；CoreWeave $8.5B/$3.1B DDTL（5 月中下旬）為窗緣背景。(7) Mag 7 P/E、CAPE、margin debt、capex、家庭持股為 stock-of-state，依 Constraints 豁免 within-window 發布日規則，但均附現值快照日。

## 本次分數存檔
```json
{
  "date": "2026-06-29",
  "iso_week": "2026-W27",
  "weekday": "Monday",
  "timezone": "Asia/Taipei",
  "valuation": 78,
  "breadth": 32,
  "speculation": 66,
  "retail": 53,
  "monetary": 75,
  "structural": 72,
  "total": 65,
  "tier": "高",
  "regime": "穩定共存"
}
```

本報告為相對風險溫度計，非擇時訊號。
