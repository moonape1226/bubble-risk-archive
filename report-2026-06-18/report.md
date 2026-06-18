# 2026-06-18 市場泡沫風險評估報告
> 報告日期：2026-06-18；執行日：2026-06-18（Asia/Taipei）；ISO 週次：2026-W25；前次基準：report-2026-06-15（3天前）

## §1 六維度風險條圖

| 維度 | 條圖 | 本次 | 前次 | Δ |
|---|---|---:|---:|---:|
| 估值溢價 | ▰▰▰▰▰▰▰▰▱▱ | 80 | 80 | 0 |
| 市場廣度 | ▰▰▰▱▱▱▱▱▱▱ | 37 | 37 | 0 |
| 投機行為 | ▰▰▰▰▰▰▰▱▱▱ | 70 | 71 | -1 |
| 散戶情緒 | ▰▰▰▰▰▱▱▱▱▱ | 54 | 51 | +3 |
| 貨幣與信貸環境 | ▰▰▰▰▰▰▱▱▱▱ | 66 | 66 | 0 |
| 結構性槓桿 | ▰▰▰▰▰▰▰▱▱▱ | 70 | 70 | 0 |
| **加權總分** | ▰▰▰▰▰▰▱▱▱▱ | **65【高】** | 65 | 0 |

## §2 歷史錨點相似度

| 錨點 | 相似度 | 條圖 | 標記 |
|---|---:|---|---|
| 1997 早期建設 | 65% | ▰▰▰▰▰▰▱▱▱▱ |  |
| 1998 LTCM 衝擊 | 25% | ▰▰▱▱▱▱▱▱▱▱ |  |
| 1999 晚期狂熱 | 70% | ▰▰▰▰▰▰▰▱▱▱ | ◀ 最貼近 |
| 2000/3 頂點 | 25% | ▰▰▱▱▱▱▱▱▱▱ |  |
| 2021/12 Meme 頂 | 50% | ▰▰▰▰▰▱▱▱▱▱ |  |

## §3 三角訊號

| 指標 | 本次數值 | vs 前次 |
|---|---|---|
| S&P 500 | 7,420.1 | ▼ -1.78%（前次 ~7,554.29，6/15） |
| WTI 原油 | $95.0 /bbl | 持平（DCOILWTICO 最新觀測 6/8，與前次同一觀測，無新印；註：現貨已重挫至 ~$75，見下） |
| 10Y Treasury | 4.43% | ▼ -4 bps（前次 ~4.47%，6/15） |

**三者狀態**：穩定共存（股小幅回落、油 FRED 序列持平、債小幅下行，未見價格拉伸或方向分歧）

- 股市：S&P 500 於 6/17 收 7,420.1，較前次基準 6/15 的 7,554.29 回落 -1.78%（script `sp500_trend.chg_pct`）；距 200 日均線 +7.58%、距 52 週均線 +9.53%，較前次（+7.98%／+9.98%）回落、拉伸度略降、未達 +10% 門檻。FOMC 偏鷹與油價回落帶來小幅風險趨避。
- WTI 原油：DCOILWTICO $95.0/桶（FRED 最新觀測 6/8，與前次同一觀測 → §3 依決定性規則標持平）；惟現貨油價本週已重挫至 ~$75/bbl（6/17，tradingeconomics，連五黑、為 3 月來低點，美伊和談／IEA 預警 2027 年供給過剩）——FRED 週序列尚未反映此跌勢，扳機鏈上游實際在降溫。
- 10Y 殖利率：4.43%（DGS10，6/16），週 Δ -4 bps；實質端 DFII10 2.14%（-1 bps）、breakeven T10YIE 2.26%（-6 bps）、5y5y forward T5YIFR 2.21%（-3 bps）——通膨預期端本週回落為主因。

**格局轉變**：前次格局 穩定共存 → 本次 穩定共存（持穩）；股小幅回落、油 FRED 持平（現貨轉跌）、債小幅下行，三者未同向上行、未觸發價格拉伸或方向分歧。

**10Y 成因拆解（`ΔDGS10 ≈ ΔDFII10 + ΔT10YIE`，拆的是週變動、非水位）**：本週 10Y 名目下行 -4 bps，由 FRED `DGS10`／`DFII10`／`T10YIE` 各自日序歷史（本次執行日最近觀測 − 前次基準日 6/15 觀測）計算：

- ΔDFII10 實質殖利率週變動：-1 bps（2.15%→2.14%）
- ΔT10YIE 損益平衡通膨週變動：-6 bps（2.32%→2.26%）
- 判定：breakeven-driven（通膨預期端主導本週 10Y 下行；ΔT10YIE -6 bps 主導、ΔDFII10 僅 -1 bps）。三序列最新觀測日略有差異（DGS10/DFII10 6/16、T10YIE 6/17），故恆等式為近似（-4 ≈ -1 + -6），僅佐證歸因方向、非獨立交叉檢核。

**扳機鏈：油 → 通膨預期 → Fed 受限 → refinancing 成本**：上游 WTI 現貨自 $95 重挫至 ~$75（美伊和談、IEA 預警 2027 供給過剩），CPI YoY +4.17%（CPIAUCSL，5 月）雖維持三年高檔，但通膨預期端本週同步回落——5y5y forward（T5YIFR）2.21%（週 -3 bps）、10Y breakeven -6 bps——「油 → 通膨預期」環節本週明顯降溫。惟政策端逆向：6/16–17 FOMC 雖維持 3.50–3.75%，但移除前次寬鬆語意、2026 年點陣圖中位數自 3.4% 上調至 3.8%（暗示年內至少一次升息、9/18 位委員預期升息），Warsh 主席措辭轉鷹——Fed put 可得性受限的是「政策路徑」而非「即期通膨」。整體扳機鏈：市場端通膨壓力降溫（偏緩），但 Fed 政策路徑轉鷹（偏緊）相互拉扯。

**結論**：扳機狀態：未擊發。三者未同向偏高（股、債、油現貨皆下行），信用利差仍處循環低點自滿（HY OAS 2.71%、IG OAS 0.75%，本次未實質走闊），私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）無新披露，HY OAS 週 Δ 僅 +5 bps（遠未達 +50 bps 擊發門檻）。當前配置的歷史意義仍為「估值＋槓桿位能高、但 financing 計時扳機尚未啟動」，接近 1999 晚期狂熱的相對位置而非頂部擊發；本週甚至出現「市場端通膨／油價降溫」的反向暖意，惟散戶槓桿（margin debt 創高、YoY +53.7%）與 FOMC 轉鷹為新增的兩股對沖力量，須持續觀察。

## 六維度評分

### 1. 估值溢價—80（前次 80，Δ 0）

Shiller CAPE 40.49（gurufocus，2026-06-01，高於長期均值 32.22 約 26%、處 2000 年來最高區間之一；ycharts 41.02、multpl 41.92 略高，取 gurufocus 與前次同源）；S&P 500 trailing P/E 約 25.3（≈ 20 年均值 25.4）。**Excess CAPE Yield（derived）** `ECY = 1/CAPE − DFII10/100 = 1/40.49 − 2.14/100 ≈ 0.33%`，極度壓縮、接近 0，屬 1929／2000 級別的跨時代估值警訊（僅作 CAPE 之 confirmation，不單獨計分；gurufocus 自家定義之 Excess CAPE Yield 1.35 採不同公式，僅供參照）。Mag 7 加權 forward P/E 約 28x（離散度大：GOOGL ~17.4 最低、META ~19.8、MSFT >25、TSLA >400x）。AI 基本面檢核：hyperscaler 2026 capex 指引仍維持高檔上修（四大合計約 $700–725B，carry-forward Q1 2026 財報、本期無新財報，stock-of-state），未見削減。AI 算力供需：GPU-backed 債務側揭露顯示 H100 租金自 2023 高點已跌約 70–90%、且資產折舊年限（6 年）長於工程可用年限（3–4 年），過剩／資產減損風險上升（best-effort，與結構性槓桿 AI 基建債合讀）；惟本期未取得本週新利用率數據，不據此加劇估值。價格趨勢偏離：距 200 日均線 +7.58%、距 52 週 +9.53%（sp500_trend），較前次（+7.98%／+9.98%）小幅回落，價格拉伸略降。TP-upgrade 相位：本期無 14 日內合格 sell-side TP 上修可拆解。基本面估值極端但本週小幅回落抵消 CAPE 微升→維持 80。

### 2. 市場廣度—37（前次 37，Δ 0）

廣度訊號分歧：一方面，S&P 500 等權指數（SPXEW）與 Russell 2000 於 6 月中雙雙創歷史新高，等權續領先、median 個股參與改善（cryptodaily / brucewoodcapital，2026-06），屬廣度轉健康的正面訊號；另一方面 Top-10 集中度仍約 39%（capitalgroup／streetstats，歷史性偏高）、約 53–59% 成分股站上 50 日均線。等權創高（偏健康）與集中度仍極高（偏風險）互抵→維持 37。

### 3. 投機行為—70（前次 71，Δ -1）

mega-IPO pipeline 仍活躍但本週無新擊發：SpaceX 已於 6/11 定價、6/12 上市（SPCX，本週進入次級交易、IPO 熱度由事件轉常態）；OpenAI（6/8 S-1，目標 9 月、估值 ~$1T）、Anthropic（6/1 機密 S-1，~$900B）pipeline 維持活躍（30 日內具名）。+AI 改名：本週 7 日窗內無新合格案例（AI Financial Corp→AIFC 屬 4/29、逾窗；前次 Junee→SuperX 屬上週）。Microcap moonshot：本週 0 件符合準則（≥100% 單日、<$1B、2+ 主題堆疊、弱基本面）——月度大漲股（INHD +2,892%、STAK、CAST 等屬月／YTD 累計，無本週單日 ≥100%＋多主題堆疊＋弱基本面之合格確認），列 0 件並以背景處理。Insider Form 4：14 日內無合格集中賣出 cluster（0 件）。SPAC 動能延續（Q1 2026 62 檔背景）。Cboe equity put/call 本週無新即期值（best-effort，不調分）。SpaceX 投機熱由事件轉常態、本週無新改名／moonshot、且小幅風險趨避→由 71 微降至 70。

### 4. 散戶情緒—54（前次 51，Δ +3）

**Margin Debt 5 月創新高 $1.42T、月增 +8.5%、年增 +53.7%**（FINRA，advisorperspectives，2026-06-16 發布）——YoY +53.7% 已越過歷史頂部級別門檻（1999／2007／2021 屢現於 +40–50%），為本維度最關鍵的新增槓桿訊號（前次沿用 4 月 $1.304T，本期為 5 月新印）。CNN Fear & Greed 40（Fear，cnn/macromicro，6/17），較前次 34 回升但仍處 Fear 區、未轉貪婪。AAII：看多約 30.4%（連四週低於歷史均值 37.5%，情緒偏空，aaii/ycharts）。家庭持股佔金融資產比 45.76%（FRED BOGZ1FL153064486Q，資料季度 2026-01-01，近歷史高位）。NAAIM 曝險指數 79.27（資料週 6/10，ycharts，仍偏高＝主動經理人擁擠多頭，positioning-crowding 反向交叉檢核）。社群投機本週無決定性新熱度→✗ NOT DISCLOSED（不調降主分）。部位／槓桿端（margin debt 創高且 YoY 越頂部門檻、家庭持股高、NAAIM 高）明顯升溫，但情緒調查端（F&G 仍 Fear、AAII 偏空）尚未轉貪婪、形成抵消→由 51 升至 54。

### 5. 貨幣與信貸環境—66（前次 66，Δ 0；自滿側）

Fed funds 維持 3.50–3.75%（DFEDTARU 3.75／DFEDTARL 3.50，6/17，Δ 0）；惟 6/16–17 FOMC 轉鷹：移除前次寬鬆語意、2026 年點陣圖中位數自 3.4% 上調至 3.8%（暗示年內至少一次升息，9/18 位委員預期升息、8 位按兵、1 位降息）、Warsh 主席稱聲明「更短更簡」（cnbc/federalreserve，6/17）。HY OAS 2.71%（BAMLH0A0HYM2，6/16，週 +5 bps，仍接近循環低點＝信用自滿，本次未實質走闊）；IG OAS 0.75%（BAMLC0A0CM，6/16，+2 bps，極窄）。10Y 4.43%（DGS10，6/16，週 -4 bps）；通膨預期端回落：breakeven T10YIE 2.26%（-6 bps）、5y5y forward T5YIFR 2.21%（-3 bps）、現貨油價 ~$75（自 $95 重挫）。CPI YoY +4.17%（CPIAUCSL，5 月）維持三年高檔。Fed 資產負債表 WALCL $6.725T（6/10）；全球央行流動性：ECB 資產 €6.136T（ECBASSETSW，6/12）、BOJ 資產 ¥664.4T（JPNASSETS，5/1），維持高位。PBoC 本次無當期英文披露→✗ NOT DISCLOSED。私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）：本次無新披露之 gate proration / breach、多基金 redemption-request ratio 惡化、或 net inflow→outflow flip→✗ NOT DISCLOSED。雙向計分下，信用利差史低自滿為主導（自滿側）；本週「市場端通膨／油價」反而降溫（偏緩扳機側），惟 FOMC 政策路徑轉鷹（偏緊 Fed 受限）作為對沖——兩股力量相抵、且無實際 financing 擊發事件，分數維持 66。所有 required 貨幣輸入（IG OAS、WALCL、ECB／BOJ）均取得當期值。

### 6. 結構性槓桿—70（前次 70，Δ 0）

美國槓桿 ETF 總 AUM 約 $170B（單一股槓桿產品近 $50B；TQQQ ~$29B、SOXL ~$14B 為大宗）。US 單一股槓桿 ETF 上市潮延續且加劇：SpaceX 上市後 6/15 單日即有約 11 檔 SpaceX 連結槓桿／反向 ETF 上市（含 GraniteShares SPAL/SNK 2x；etf.com/yahoo），SEC 維持 2x 上限。全球槓桿擴散：本週未見 KRX／TWSE／JPX 英文新核准；歐洲 Leverage Shares 3x SpaceX ETP 屬上週（6/12）——**本週擴散訊號未觸發**（未達 2+ 非美市場同週新核准）。0DTE 佔 SPX 選擇權量約 60%（Cboe，記錄高區間，~2.4M 口/日）；VIX 16.41（6/17，自前次 17.68 回落，波動偏低＝自滿）；SKEW ~142（6/12 最近觀測，>130＝尾部避險需求高，本期無新印）——「base case 自滿、尾部已避險」。AI 基建債務融資：neocloud 部門 GPU-backed 債務累計逾 $20B；CoreWeave $8.5B IG 級 GPU-backed DDTL（A3／A(low)、SOFR+2.25%）為背景；JPMorgan 估 2026–27 年 data-center 證券化年發行達 $30–40B（佔 CMBS+ABS 7–10%）——AI 基建債持續結構性擴張（背景＋證券化展望為新增框架），且 GPU 租金跌 70–90%、資產年限錯配為潛在減損觸發。0DTE 高、單一股槓桿產品爆量擴張與 AI 基建債擴張支撐高分，惟全球擴散未觸發、VIX 回落、TQQQ/SOXL 流向中性→維持 70。

## 綜合分數

| 維度 | 權重 | 分數 | 加權 |
|---|---:|---:|---:|
| 估值溢價 | 22% | 80 | 17.60 |
| 市場廣度 | 13% | 37 | 4.81 |
| 投機行為 | 18% | 70 | 12.60 |
| 散戶情緒 | 12% | 54 | 6.48 |
| 貨幣與信貸環境 | 20% | 66 | 13.20 |
| 結構性槓桿 | 15% | 70 | 10.50 |
| **加權總計** | **100%** | — | **65.19 → 65** |

加權總分 65.19，half-up 四捨五入為 **65**，風險等級 **高**（65–84）。

邊界帶：總分 65 距 警戒/高 邊界 ≤ 2 分，評分固有噪音約 ±2–3，等級判讀需保留餘地。

## 歷史泡沫週期對比

相似度計算：checklist v2

依各錨點固定特徵清單，逐項以本次六維度分數與已抓取數據判定命中（命中數 ÷ 特徵數 × 100，取最近 5%）：

**1999 晚期狂熱（10 項，命中 7 → 70% ◀ 最貼近）**：①估值溢價 ≥ 75（80）✔；②CAPE ≥ 38（40.49）✔；③投機行為 ≥ 60（70）✔；④本週 moonshot ≥ 1 或無營收 IPO 佔比偏高（moonshot 0、mega-IPO 具營收）✘；⑤市場廣度 ≥ 45 轉窄（37）✘；⑥D5 自滿側且 HY OAS < 3.5%（自滿側、2.71%）✔；⑦結構性槓桿 ≥ 60（70）✔；⑧散戶情緒 ≥ 55（54）✘；⑨巨型 IPO pipeline 活躍（SpaceX 6/11 定價、OpenAI 6/8 S-1、Anthropic 6/1 S-1，皆 30 日內）✔；⑩扳機狀態＝未擊發 ✔。

其餘錨點摘要：
- **1997 早期建設（命中 5 → 65%）**：市場廣度 < 45 ✔、capex 仍上修 ✔、散戶 < 55（54）✔、HY OAS < 4% 仍近循環低點 ✔、扳機未擊發 ✔；惟估值（80，逾 40–74 上限）、投機（70 ≥ 50）、結構性槓桿（70 ≥ 50）三項超出早期建設區間 ✘——計時／信用面似早期，但位階特徵已晚於 1997。
- **2021/12 Meme 頂（命中 4 → 50%，較前次 40% 升）**：結構性槓桿 ≥ 65（70）✔、流動性氾濫（央行表高位＋D5 ≥ 60 自滿側）✔、**margin debt YoY ≥ +40%（+53.7%，本週越門檻）✔（新增命中）**、CPI YoY ≥ 4% 且 Fed 未實質緊縮（4.17%、僅鷹派指引未實升）✔；惟散戶情緒（54 < 65）、社群投機、moonshot、廣度背離（37）未命中 ✘——槓桿與流動性面已貼近 Meme 頂，但散戶全面狂熱與 meme 投機仍缺。
- **1998 LTCM 衝擊（命中 2 → 25%，較前次 15% 升）**：估值 ≥ 60（80）✔、ΔT10YIE ≤ 0（-6 bps，通膨預期非主因）✔；無利差暴衝／VIX>25、無回檔 ≥5%、無具名非銀壓力、Fed 未轉鴿（反轉鷹）、扳機未達初啟、廣度未急轉弱 ✘。
- **2000/3 頂點（命中 2 → 25%，較前次 15% 升）**：投機 ≥ 70（70）✔、貨幣轉緊（FOMC 點陣圖上調至 3.8%、暗示升息＝FedWatch 隱含緊縮）✔；惟估值未達 ≥85（80）、扳機未達初啟、廣度未極窄、無 dev200 高位回落、無 insider 集中賣出、散戶 < 65 ✘。

**解讀**：本週最貼近 **1999 晚期狂熱**（70%）——高估值（CAPE 40.49、ECY ~0.33%）、結構性槓桿偏高、mega-IPO pipeline 活躍、信用利差史低自滿並存，但市場廣度尚未極端轉窄、散戶情緒未全面狂熱、financing 扳機未擊發。值得注意的是 2021/12 Meme 頂相似度因 margin debt YoY +53.7% 越過 +40% 門檻而升至 50%——散戶槓桿面正向 Meme 頂特徵靠攏。以週期位置而言，仍屬「晚期狂熱、頂部計時扳機尚未啟動」；結構性槓桿以期間調整觀之（0DTE ~60%、單一股槓桿 ETF 爆量、AI 基建債擴張）對應 1999 的保證金／衍生品投機。長期相對成長趨勢偏離（Dot-com ~95%、1929 ~110%、當前 AI 週期 ~147%；RIA/Farrell）僅作敘事錨點，週度偏離已於估值溢價計分。

## 機構情緒對照

**BofA Global Fund Manager Survey 6 月版「The Frozen Bulls」已發布**（調查期 6/5–6/11，198 位經理人、$540B AUM，axios/trustnet/tradingview，自前次基準 6/15 以來新增）：

- 部位：6 月經理人增持現金與債券、減碼股票／不動產／商品（pare risk）；惟仍維持股票加碼、對全球成長信心提升。BofA 綜合情緒指標降至 6.0（5 月 6.6），偏多但轉趨節制。
- 最擁擠交易：**創紀錄 80% 受訪者點名「long global semiconductors」為市場最擁擠交易**——AI 主題擁擠度達極端（高擁擠＝反向風險升高）。
- 尾部風險：第二波通膨為最大尾部風險（34%）；對「AI 泡沫」的擔憂自兩個月前 5% 急升至 28%。
- 現金水位：較 5 月回升（de-risking）。
- 反向解讀：機構對股票仍偏多但開始減風險、且對 AI 泡沫的警覺急升＋半導體擁擠創高，屬晚期循環的「擁擠多頭＋自我警覺上升」訊號。AAII 僅作散戶對照（看多 ~30%，偏空），非機構數據。

另就週頻主動經理人曝險：**NAAIM Exposure Index 79.27**（資料週 6/10，ycharts），仍偏高，作為反向交叉檢核（高曝險＝擁擠多頭，Farrell #9）；NAAIM 於 散戶情緒 維度作 confirmation，非本節計分。

## 本次新增訊號

對比 vs 前次（3天前），report-2026-06-15 → 2026-06-18：

- **散戶情緒 +3（51→54）**：FINRA 5 月 margin debt 創新高 $1.42T、月增 +8.5%、**年增 +53.7%**（advisorperspectives，6/16 發布）——YoY 越過 1999／2007／2021 頂部級別門檻（+40–50%），為本次最關鍵新增槓桿訊號；CNN F&G 自 34 回升至 40（仍 Fear）。情緒調查端尚未轉貪婪，故升幅受抵消。
- **投機行為 -1（71→70）**：SpaceX IPO 熱度由事件轉次級常態；本週 7 日窗內無新 +AI 改名、microcap moonshot 0 件、insider Form 4 無 14 日合格集中賣出；mega-IPO pipeline（OpenAI 6/8、Anthropic 6/1 S-1）維持活躍。
- **貨幣與信貸環境 0（66，自滿側）— 雙向 Δ 遮蔽防護質化說明**：分數未動，但本次有兩股質化質變相互拉扯：(1) **FOMC 6/16–17 轉鷹**（維持 3.50–3.75%，移除寬鬆語意，2026 點陣圖中位數 3.4%→3.8% 暗示升息）——Fed 政策路徑受限趨緊（偏扳機側暖機，但屬政策端、非 financing 擊發）；(2) 市場端通膨／油價降溫（油現貨 $95→~$75、breakeven -6 bps、5y5y -3 bps）——偏緩。**惟無任何 financing 擊發事件（私募信貸 gate proration/breach、多基金 redemption 反轉、再融資壓力顯現皆無），HY OAS 週 Δ 僅 +5 bps，扳機狀態維持「未擊發」、D5 維持「自滿側」。** 列此以符雙向 Δ 遮蔽防護要求。
- **機構情緒（質化新增）**：BofA 6 月 FMS「The Frozen Bulls」發布——經理人減風險、創紀錄 80% 點名半導體為最擁擠交易、AI 泡沫擔憂 5%→28%（晚期循環擁擠＋自我警覺訊號）。
- **全球槓桿擴散**：本週擴散訊號未觸發（無 2+ 非美市場同週單一股槓桿核准；美國本週 SpaceX 連結槓桿 ETF 上市約 11 檔屬境內、非全球擴散）。

## 數據附錄

### 原始數據表（計分用具體數據點）

| 指標 | 數值 | 來源（FRED series ID / URL）| 資料日期 | 抓取 timestamp |
|---|---|---|---|---|
| Shiller CAPE | 40.49（ycharts 41.02／multpl 41.92）| gurufocus.com/economic_indicators/56 | 2026-06-01 | 2026-06-18T09:05+08:00 |
| S&P 500 trailing P/E | ~25.3（20y 均 25.4）| multpl.com | 2026-06 | 2026-06-18T09:05+08:00 |
| Excess CAPE Yield（derived）| ECY = 1/40.49 − 2.14/100 ≈ 0.33% | derived（CAPE × DFII10）| 2026-06 | 2026-06-18T09:05+08:00 |
| Mag 7 加權 forward P/E | ~28x（GOOGL ~17.4／META ~19.8／TSLA >400x）| yardeni / roundhill / fool | 2026-06 | 2026-06-18T09:05+08:00 |
| S&P 500 趨勢偏離 | dev200 +7.58%／dev52w +9.53%（spot 7,420.1）| FRED SP500（sp500_trend）| 2026-06-17 | 2026-06-18T09:02+08:00 |
| RSP/SPY 廣度 | 等權 SPXEW 與 Russell 2000 6 月中創高（等權續領先）| brucewoodcapital / cryptodaily | 2026-06 | 2026-06-18T09:05+08:00 |
| Top-10 集中度 | ~39% | capitalgroup / streetstats | 2026-06 | 2026-06-18T09:05+08:00 |
| A/D・50DMA 上方比例 | ~53–59% 站上 50DMA | streetstats.finance | 2026-06 | 2026-06-18T09:05+08:00 |
| CNN Fear & Greed | 40（Fear）| cnn.com/markets/fear-and-greed | 2026-06-17 | 2026-06-18T09:05+08:00 |
| Margin Debt | $1.42T（月 +8.5%、**YoY +53.7%**，創高）| advisorperspectives.com/dshort 2026-06-16 | 2026-05 | 2026-06-18T09:05+08:00 |
| AAII 看多 | ~30.4%（連四週低於均值 37.5%）| aaii.com/sentimentsurvey / ycharts | 2026-06 | 2026-06-18T09:05+08:00 |
| 家庭持股佔金融資產比 | 45.76% | FRED BOGZ1FL153064486Q | 2026-01-01(Q) | 2026-06-18T09:02+08:00 |
| NAAIM Exposure | 79.27 | ycharts.com/indicators/naaim_number | 2026-06-10 | 2026-06-18T09:05+08:00 |
| BofA FMS 6 月 | 「Frozen Bulls」：減風險、80% semis 最擁擠、AI 泡沫憂 5%→28%、情緒 6.0 | axios/trustnet/tradingview | 2026-06-05/11 | 2026-06-18T09:05+08:00 |
| Fed funds | 3.75% / 3.50%（6/16–17 維持，點陣圖 2026 中位 3.8%）| FRED DFEDTARU/DFEDTARL；cnbc/federalreserve | 2026-06-17 | 2026-06-18T09:02+08:00 |
| HY OAS | 2.71%（週 +5 bps）| FRED BAMLH0A0HYM2 | 2026-06-16 | 2026-06-18T09:02+08:00 |
| IG OAS | 0.75%（週 +2 bps）| FRED BAMLC0A0CM | 2026-06-16 | 2026-06-18T09:02+08:00 |
| 10Y DGS10 | 4.43%（週 -4 bps）| FRED DGS10 | 2026-06-16 | 2026-06-18T09:02+08:00 |
| 10Y 實質 DFII10 | 2.14%（週 -1 bps）| FRED DFII10 | 2026-06-16 | 2026-06-18T09:02+08:00 |
| 10Y breakeven T10YIE | 2.26%（週 -6 bps）| FRED T10YIE | 2026-06-17 | 2026-06-18T09:02+08:00 |
| WTI DCOILWTICO | $95.0（FRED 序列最新 6/8）；現貨 ~$75（6/17）| FRED DCOILWTICO；tradingeconomics | 2026-06-08／2026-06-17 | 2026-06-18T09:02+08:00 |
| CPI YoY | +4.17%（CPIAUCSL，5 月）| FRED CPIAUCSL | 2026-05-01 | 2026-06-18T09:02+08:00 |
| 5y5y forward T5YIFR | 2.21%（週 -3 bps）| FRED T5YIFR | 2026-06-17 | 2026-06-18T09:02+08:00 |
| Fed 資產負債表 WALCL | $6.725T | FRED WALCL | 2026-06-10 | 2026-06-18T09:02+08:00 |
| ECB / BOJ 資產 | €6.136T / ¥664.4T | FRED ECBASSETSW / JPNASSETS | 2026-06-12／2026-05-01 | 2026-06-18T09:02+08:00 |
| 0DTE 佔 SPX | ~60%（~2.4M 口/日）| cboe.com insights / spotgamma | 2026-06 | 2026-06-18T09:05+08:00 |
| VIX / SKEW | 16.41（6/17）/ ~142（6/12，無新印）| cboe / yahoo ^VIX ^SKEW | 2026-06-17／2026-06-12 | 2026-06-18T09:05+08:00 |
| 槓桿 ETF AUM | 總 ~$170B、單一股槓桿近 $50B | etf.com / pionline | 2026-06 | 2026-06-18T09:05+08:00 |
| US 單一股槓桿上市 | 6/15 約 11 檔 SpaceX 連結槓桿/反向 ETF（SPAL/SNK 等）| finance.yahoo.com GraniteShares / etf.com | 2026-06-15 | 2026-06-18T09:05+08:00 |
| AI 基建債 | neocloud GPU 債 >$20B；CoreWeave $8.5B IG；JPM 估證券化 $30–40B(2026–27)；GPU 租金 -70~90% | qz.com / finviz / investors.coreweave.com | 2026-06 | 2026-06-18T09:05+08:00 |
| SpaceX IPO（背景）| 6/11 定價 $135、6/12 上市 SPCX | cnbc / teslanorth | 2026-06-11/12 | 2026-06-18T09:05+08:00 |

附註：FRED 全序列以 `scripts/fetch_macro.py`（Python urllib + UA）直抓 FRED API 成功（status ok），API key 全程未輸出；10Y 週 Δ 分解取自 script `decomposition`（ΔDGS10 -4＝ΔDFII10 -1 ＋ ΔT10YIE -6 之近似，driver breakeven）。WTI DCOILWTICO 序列最新觀測仍為 6/8 $95、與前次同觀測 → §3 依決定性規則標持平，另註現貨已跌至 ~$75。

### Coverage table（每個 `# Data sources` bullet 一列，狀態）

| 維度 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|
| Valuation: S&P 500 P/E & Shiller CAPE | multpl / gurufocus [primary: SEARCH] | ✓ SEARCH-VERIFIED（CAPE 40.49；query「Shiller CAPE June 2026」；URL gurufocus.com/economic_indicators/56；日期 2026-06-01；ts 09:05）|
| Valuation: Mag 7 weighted P/E & AI leader P/S | sell-side / aggregators | ✓ SEARCH-VERIFIED（~28x；query「Mag 7 forward PE June 2026」；URL yardeni.com/charts/magnificent-7 + roundhill；日期 2026-06；ts 09:05）|
| Valuation: Analyst TP upgrade decomposition（best-effort）| Bloomberg/Reuters/CNBC [primary: SEARCH] | ✗ NOT DISCLOSED（14 日內無合格 TP 上修可拆解）|
| Valuation: S&P 500 price-trend deviation | scripts/fetch_macro.py sp500_trend | ✓ API（dev200 +7.58%／dev52w +9.53%；FRED SP500）|
| Breadth: RSP vs SPY YTD divergence | search | ✓ SEARCH-VERIFIED（等權 SPXEW 創高、續領先；URL brucewoodcapital.com／cryptodaily.co.uk；日期 2026-06；ts 09:05）|
| Breadth: Top-10 concentration | search | ✓ SEARCH-VERIFIED（~39%；URL capitalgroup.com／streetstats.finance；日期 2026-06；ts 09:05）|
| Breadth: Advance/decline, new high/low | search | ✓ SEARCH-VERIFIED（~53–59% > 50DMA；URL streetstats.finance；日期 2026-06；ts 09:05）|
| Retail: CNN Fear & Greed | cnn [primary: SEARCH] | ✓ SEARCH-VERIFIED（40 Fear；URL cnn.com/markets/fear-and-greed；日期 2026-06-17；ts 09:05）|
| Retail: Margin Debt（FINRA + ratio + YoY）| FINRA monthly | ✓ SEARCH-VERIFIED（$1.42T 5 月、+8.5% MoM、+53.7% YoY、創高；URL advisorperspectives.com/dshort/updates/2026/06/16；日期 2026-05；ts 09:05）|
| Retail: AAII survey | aaii [primary: SEARCH] | ✓ SEARCH-VERIFIED（看多 ~30.4%；URL aaii.com/sentimentsurvey／ycharts；日期 2026-06；ts 09:05）|
| Retail: Social sentiment proxies（best-effort）| Reddit/X | ✗ NOT DISCLOSED（本週無決定性新熱度，不調降主分）|
| Retail: Household equity allocation | FRED BOGZ1FL153064486Q（script）| ✓ API（45.76%，資料季度 2026-01-01）|
| Retail: NAAIM Exposure Index（best-effort）| naaim/ycharts [primary: SEARCH] | ✓ SEARCH-VERIFIED（79.27；URL ycharts.com/indicators/naaim_number；日期 2026-06-10；ts 09:05）|
| Institutional: BofA / JPM survey（best-effort, monthly）| BofA/JPM | ✓ SEARCH-VERIFIED（BofA 6 月「Frozen Bulls」6/5–11；URL axios.com/2026/.../bofa＋trustnet/tradingview；日期 2026-06；ts 09:05；JPM 無當期新版）|
| Monetary: Fed funds DFEDTARU/DFEDTARL | FRED（script）| ✓ API（3.75% / 3.50%；組合列，最差 ok）|
| Monetary: High Yield OAS BAMLH0A0HYM2 | FRED（script）| ✓ API（2.71%，+5 bps）|
| Monetary: Investment Grade OAS BAMLC0A0CM | FRED（script）| ✓ API（0.75%，+2 bps）|
| Monetary: 10Y Treasury DGS10 | FRED（script）| ✓ API（4.43%，-4 bps）|
| Monetary: 10Y real DFII10 | FRED（script）| ✓ API（2.14%，-1 bps）|
| Monetary: 10Y breakeven T10YIE | FRED（script）| ✓ API（2.26%，-6 bps）|
| Monetary: WTI DCOILWTICO | FRED（script）| ✓ API（$95.0，6/8；現貨 ~$75 另註）|
| Monetary: CPI YoY CPIAUCSL | FRED（script）| ✓ API（+4.17%，5 月）|
| Monetary: 5y5y forward T5YIFR | FRED（script）| ✓ API（2.21%，-3 bps）|
| Monetary: Fed funds path FedWatch（best-effort）| CME [primary: SEARCH] | ✓ SEARCH-VERIFIED（6/16–17 維持 3.50–3.75%、點陣圖 2026 中位 3.8% 暗示升息；URL cnbc.com/2026/06/17／federalreserve.gov；日期 2026-06-17；ts 09:05）|
| Monetary: Fed balance sheet WALCL | FRED（script）| ✓ API（$6.725T）|
| Monetary: Global ECB / BOJ balance sheets | FRED ECBASSETSW / JPNASSETS（script）| ✓ API（€6.136T / ¥664.4T；組合列）|
| Monetary: PBoC aggregate financing（best-effort）| NBS/PBoC | ✗ NOT DISCLOSED（無當期英文披露）|
| Monetary: Private-credit / non-bank liquidity stress（best-effort）| [primary: SEARCH] | ✗ NOT DISCLOSED（無 gate proration/breach、無多基金 redemption 惡化或 inflow→outflow flip）|
| AI: Hyperscaler capex guidance | MSFT/GOOGL/AMZN/META earnings | ✓ SEARCH-VERIFIED（~$700–725B，Q1 2026 沿用 stock-of-state；URL cnbc/tomshardware；ts 09:05）|
| AI: AI token volume growth（best-effort）| Anthropic/OpenAI/Google | ✗ NOT DISCLOSED（本季無新揭露）|
| AI: OpenAI / Anthropic annualized revenue（best-effort）| The Information/Reuters | ✗ NOT DISCLOSED（無當季營收揭露／可信外洩；僅見估值）|
| AI: Hyperscaler AI customer concentration（best-effort）| earnings calls | ✗ NOT DISCLOSED（無正式集中度揭露）|
| AI: AI compute supply/demand & overcapacity（best-effort）| [primary: SEARCH] | ✓ SEARCH-VERIFIED（GPU 租金 -70~90%、資產年限錯配；URL qz.com/gpu-collateralized-debt／finviz；日期 2026-06；ts 09:05）|
| Spec: +AI rename / SPAC / no-rev IPO surge（7d）| search | ✓ SEARCH-VERIFIED（0 件本週新改名；query「AI rename SPAC June 2026」；檢查 stocktitan/finviz/sec；URL/日期 —；ts 09:05）|
| Spec: IPO market heat | search | ✓ SEARCH-VERIFIED（SpaceX 6/12 上市轉次級；URL cnbc/teslanorth；日期 2026-06；ts 09:05）|
| Spec: Microcap thematic moonshots | [primary: SEARCH] | ✓ SEARCH-VERIFIED（0 件 qualifying；query「biggest gainers week June 15 2026 microcap 100% quantum AI」；檢查 stocktitan/stockanalysis/finviz；URL/日期 —；ts 09:05）|
| Spec: Upcoming AI IPOs（OpenAI/Anthropic/xAI/SpaceX）| named-source 30d | ✓ SEARCH-VERIFIED（OpenAI 6/8 S-1、Anthropic 6/1 S-1；URL finance.yahoo.com／builtin.com；日期 2026-06；ts 09:05）|
| Spec: Insider selling Form 4 clusters | [primary: SEC EDGAR] | ✓ SEARCH-VERIFIED（0 件 qualifying；query「insider Form 4 cluster AI leaders June 2026」；檢查 SEC EDGAR；URL/日期 —；ts 09:05）|
| Spec: Cboe equity put/call ratio（best-effort）| [primary: SEARCH] | ✗ NOT DISCLOSED（本週無新即期值；不調降 D3 主分）|
| Structural: US leveraged ETF AUM（NVDL/TSLL/CONL/TQQQ/SOXL/SQQQ）| etf.com [primary: SEARCH] | ✓ SEARCH-VERIFIED（總 ~$170B／單一股近 $50B；URL etf.com／pionline.com；日期 2026-06；ts 09:05）|
| Structural: US single-stock leveraged approvals/launches | SEC EDGAR / ETF.com | ✓ SEARCH-VERIFIED（6/15 約 11 檔 SpaceX 連結槓桿/反向 ETF；URL finance.yahoo.com GraniteShares；日期 2026-06-15；ts 09:05）|
| Structural: Global leveraged approvals（KRX/TWSE/JPX/ESMA）| regulator feeds | ✓ SEARCH-VERIFIED（本週無 2+ 非美新核准、擴散未觸發；歐洲 3x SpaceX ETP 屬上週 6/12；query「leveraged single-stock ETF approval Korea Taiwan Japan June 2026」；URL/日期 —；ts 09:05）|
| Structural: 0DTE option volume | CBOE daily | ✓ SEARCH-VERIFIED（~60%；URL cboe.com insights／spotgamma；日期 2026-06；ts 09:05）|
| Structural: Options total volume | OCC monthly report | ✓ SEARCH-VERIFIED（5 月 ~1.47B 口，沿用最近月報；URL securitiesfinancetimes.com；日期 2026-05；ts 09:05）|
| Structural: VIX term structure / SKEW / stock-bond corr | Cboe/search | ✓ SEARCH-VERIFIED（VIX 16.41 6/17／SKEW ~142 6/12 無新印；URL cboe.com／yahoo ^VIX ^SKEW；組合列最差）|
| Structural: Cross-ref margin debt / BOGZ1FL073164003.Q | confirmation only | ✓ SEARCH-VERIFIED（沿用 散戶情緒 margin debt $1.42T 作 confirmation，不重複計分）|
| Structural: AI infrastructure debt financing / vendor loops（best-effort）| [primary: SEARCH] | ✓ SEARCH-VERIFIED（neocloud GPU 債 >$20B、CoreWeave $8.5B IG、JPM 證券化 $30–40B；URL qz.com／investors.coreweave.com／finviz；日期 2026-06；ts 09:05）|

附註：Coverage 表共 47 列＝`# Data sources` 47 個 top-level bullet，逐列單一狀態。required 源（FRED 全序列、CAPE、廣度、F&G、margin debt、AAII、家庭持股、ECB/BOJ、moonshot/insider 0 件螢幕、槓桿 ETF/approvals/0DTE/VIX-SKEW）皆 ✓ API / ✓ SEARCH-VERIFIED；✗ NOT DISCLOSED 僅用於 best-effort 清單項目。

## 本次分數存檔

```json
{
  "date": "2026-06-18",
  "iso_week": "2026-W25",
  "weekday": "Thursday",
  "timezone": "Asia/Taipei",
  "valuation": 80,
  "breadth": 37,
  "speculation": 70,
  "retail": 54,
  "monetary": 66,
  "structural": 70,
  "total": 65,
  "tier": "高",
  "regime": "穩定共存"
}
```

本報告為相對風險溫度計，非擇時訊號。
