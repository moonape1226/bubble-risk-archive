# 2026-06-04 市場泡沫風險評估報告
> 報告日期：2026-06-04；執行日：2026-06-04 Asia/Taipei；ISO 週次：2026-W23；前次基準：report-2026-06-01（3天前）

## §1 六維度風險條圖

| 維度 | 條圖 | 本次 | 前次 | Δ |
|---|---|---:|---:|---:|
| 估值溢價 | ▰▰▰▰▰▰▰▰▱▱ | 81 | 82 | −1 |
| 市場廣度 | ▰▰▰▰▱▱▱▱▱▱ | 45 | 45 | 0 |
| 投機行為 | ▰▰▰▰▰▰▰▱▱▱ | 70 | 70 | 0 |
| 散戶情緒 | ▰▰▰▰▰▰▱▱▱▱ | 62 | 66 | −4 |
| 貨幣與信貸環境 | ▰▰▰▰▰▰▱▱▱▱ | 66 | 64 | +2 |
| 結構性槓桿 | ▰▰▰▰▰▰▰▱▱▱ | 72 | 74 | −2 |
| **加權總分** | ▰▰▰▰▰▰▱▱▱▱ | **68【高】** | 68 | 0 |

本週無任一維度 |Δ| ≥ 10（⚠ 未觸發）。「全球槓桿擴散訊號」本週未觸發（◆ 未標示），詳見 §結構性槓桿與本次新增訊號。

## §2 歷史錨點相似度

| 錨點 | 相似度 | 條圖 | 標記 |
|---|---:|---|---|
| 1997 早期建設 | 25% | ▰▰▱▱▱▱▱▱▱▱ |  |
| 1998 LTCM 衝擊 | 20% | ▰▰▱▱▱▱▱▱▱▱ |  |
| 1999 晚期狂熱 | 85% | ▰▰▰▰▰▰▰▰▱▱ | ◀ 最貼近 |
| 2000/3 頂點 | 60% | ▰▰▰▰▰▰▱▱▱▱ |  |
| 2021/12 Meme 頂 | 68% | ▰▰▰▰▰▰▱▱▱▱ |  |

## §3 三角訊號

| 指標 | 本次數值 | vs 前次 |
|---|---|---|
| S&P 500 | ≈7,553（2026-06-03 收盤） | ▼ −0.4%（前次 ~7,580；6/2 創歷史新高 7,609.78 後因伊朗攻擊回落 −0.74%） |
| WTI 原油 | $95.68 /bbl（2026-06-04） | ▲ +9.7%（前次 ~$87.2） |
| 10Y Treasury | 4.49%（2026-06-04） | ▲ +4 bps（前次 ~4.45%） |

**三者狀態**：出現分歧（WTI 原油在重新定價地緣政治風險）。三者並非同向偏高，而是油價與殖利率走升、股市自歷史新高回落，呈現「地緣供給衝擊 + 通膨重定價」的早期格局。

- 股市：S&P 500 於 2026-06-02 首度收上 7,600（收 7,609.78，歷史新高），但 06-03 因伊朗向科威特、巴林發射飛彈下跌 0.74%，最近收盤約 7,553，較前次基準 7,580 小幅回落約 0.4%；位置仍處歷史高位區。
- WTI 原油：$95.68/桶，較前次 $87.2 大漲約 9.7%，連三日上行；扭轉 5 月全月跌勢，地緣風險溢價回歸為主因。
- 10Y 殖利率：4.49%，較前次 4.45% 上行約 4 bps；主要驅動為油價推升的通膨預期與避險／供給雙向拉鋸。

**格局轉變**：前次為「股強、油弱、債中立」的偏需求疲軟格局；本次轉為「股自高點回落、油急升、債走高」的地緣供給衝擊格局——油價而非股市成為本週的重新定價核心。

**10Y 成因拆解（`ΔDGS10 ≈ ΔDFII10 + ΔT10YIE`，拆的是週變動、非水位）**：本週 Δ 分解不可用——無日序資料。FRED API（api.stlouisfed.org）與 US Treasury 日序 XML（home.treasury.gov）於本環境經 WebFetch 皆回傳 HTTP 403，EIA API 亦 403，三者日序序列均無法取得；僅由 WebSearch 取得 spot 水位，依 Fetch protocol「若任一腿退回 WebSearch（僅 spot、無日序）則不得捏造 Δ」之規則，本段不輸出 ΔDFII10／ΔT10YIE 數值。

- ΔDFII10 實質殖利率週變動：不可用（無日序）。spot 參考：DFII10 ≈ 2.08%（2026-06-03）。
- ΔT10YIE 損益平衡通膨週變動：不可用（無日序）。spot 參考：T10YIE ≈ 2.41%（由 DGS10 4.49% − DFII10 2.08% 推算，標 `derived`，僅為水位參考、非 Δ）。
- 判定：不可用（real-rate-driven / breakeven-driven 無法判定，缺週變動日序）。

**扳機鏈：油 → 通膨預期 → Fed 受限 → refinancing 成本**：本週扳機鏈出現啟動跡象。伊朗對科威特、巴林的飛彈攻擊推升 WTI 至 $95.68（+9.7%），地緣供給衝擊直接強化能源通膨路徑；疊加 4 月 FOMC「連三次按兵不動 + 4 票異議（1992 年 10 月以來最多）」的鷹派分歧，油價驅動的通膨上行將壓縮 Fed put 的可得性，使寬鬆空間在下行情境中更受約束。下次 FOMC 為 06-16/17，市場預期續按兵不動。

**⚠ 結論**：油價急升 + 10Y 上行 + 股市自歷史高位回落，是泡沫後期疊加外生地緣衝擊的高風險配置雛形；惟信用利差尚未擴張（HY OAS 2.72%、IG OAS 77 bps 均近歷史最緊、無再融資壓力訊號），扳機尚未正式擊發。此處 ⚠ 標示之依據為油價驅動的通膨重定價觸發鏈已啟動，而非六維度同向偏高。

## 六維度評分

### 1. 估值溢價：81 / 100（weight 22%）

- **Shiller CAPE 41.44（2026-06-01，GuruFocus）**：略低於前次 41.6；為史上次高，僅 2000 年科網頂部曾更高；普通 P/E 27.5（20 年均值 25.4）。
- **Mag 7 前向 P/E 分歧**：GOOGL 約 17×（最便宜）、META 約 19.3×、MSFT 約 24.5×、AMZN 約 36×（trailing）；加權前向約 30× 一帶，仍顯著高於歷史。
- **超大規模廠商 capex 仍在上調（支撐但累積尾部）**：2026 年群體 capex 指引升至約 $725B（年增約 77%），4 月底財報全面上修——Meta $125–145B（兩端各 +$10B）、GOOGL $175–185B、AMZN 約 $200B、MSFT $110–120B。capex 未見削減，估值短期有基本面支撐，但資本支出垂直擴張累積了未來折舊與回報落差的尾部風險。
- **AI 算力供需檢核：需求仍在吸收產能，未見過剩**：H100/H200 租賃需求堅挺、多家雲商售罄；HBM/DRAM 合約價 2026 年初轉為「拋物線式」上行（DDR5/LPDDR5 年增約 4–5×），HBM 需求年增約 70%——屬供給偏緊而非過剩。本週未出現利用率走弱、訂單消化、庫存上升等產能過剩證據，故不因過剩而上調估值風險；惟記憶體價格拋物線同時帶來成本通膨疑慮。
- **TP-upgrade 階段訊號：本期以 EPS-driven 為主**：BofA 將 NVDA 目標 $300→$320（2026-05-13），明確錨定「不變的 28× CY2027 P/E」——屬 EPS-driven、非倍數擴張；Bernstein TSMC 目標 $430、UBS TSMC NT$3,000 亦以盈利上修為主軸。本期主要賣方上修的主導槓桿仍是 E 而非倍數，較 2026-Q2「MS TSMC 以 20–30× 目標 PE 擴張」的晚週期訊號為輕，邊際上略為降溫。

**評分邏輯**：CAPE 微降（41.6→41.44）、TP 上修以 EPS-driven 為主、算力供需未見過剩，估值極端但本週無新增惡化，邊際自 82 微降至 81。

### 2. 市場廣度：45 / 100（weight 13%）

- **RSP vs SPY**：等權重 RSP 年初至今續勝市值加權約 5 個百分點，廣度改善方向維持（與前次一致）。
- **Top-10 集中度**：約 40%（歷史常態 20–25%），仍處極高位，6/2 歷史新高主由半導體（NVDA 新 PC AI 晶片）單一板塊驅動，屬窄基領漲。
- **漲跌家數 / 新高新低比**：⛔ FETCH FAILED——本環境未能由 API 或 WebSearch 取得 2026-06 當期具體 A/D 線與新高/新低數值；本維度改以 RSP/SPY 散度與 Top-10 集中度評分，缺 A/D 直接輸入已於此註明。

**評分邏輯**：等權重續勝（改善）與 40% 集中度、窄基領漲（惡化）相互抵銷，A/D 直接證據缺位，維持 45。

### 3. 投機行為：70 / 100（weight 18%）

- **超大型 IPO 管線進入高潮**：SpaceX 已遞交 S-1，預計約 2026-06-12 掛牌、目標估值約 $1.75 兆（若達標為史上最大 IPO），roadshow 排定 06-08 當週；S-1 自陳「持續淨虧損、未必能獲利」。CNBC（05-22）等以「mega-IPO 恐為市場頂部訊號」示警。
- **首日暴衝前例延續**：Cerebras（05-14）首日 +68%、開盤觸發向上熔斷（前次已計入，本週為背景）。
- **微型股主題暴衝（moonshot）本週降溫**：本週掃描最大單日漲幅標的，未發現市值 <$1B、單日 ≥100%、且疊加 2+ 熱門主題搭配弱基本面的合格 moonshot；量子族群（Rigetti、D-Wave 等）單日約 +20–25%，未達 ≥100% 門檻。相對前次（如 ASTC +516% 之類型）froth 降溫——此為投機維度本週唯一的明顯降溫項。
- **+AI 改名**：本週無新增「+AI 改名 → 暴漲」案例；Myseum.AI（04 月）、Bloomberg「peak euphoria 小型股搭 AI 順風車」（05-08）為近月背景，非本週事件。
- **內部人拋售**：✗ NOT DISCLOSED——過去 14 天內未取得具 Form 4 申報日/交易日/EDGAR URL 的成簇拋售明細，依規不引用陳舊名單。

**評分邏輯**：SpaceX 史上最大 IPO 臨近（升溫）與 microcap moonshot 降溫、無新增 +AI 改名（降溫）相抵，維持 70。

### 4. 散戶情緒：62 / 100（weight 12%）

- **CNN Fear & Greed：54（中性，2026-06-03）**，自前次 60（貪婪）回落至中性區，與 06-03 地緣回檔一致。
- **AAII（2026-05-28，本週尚無新調查）**：看多 35.6%、中立 22.6%、看空 41.9%；看空持續高於看多，散戶未呈一面倒頂部式樂觀（新一期週四晨間才公布，本次未取得）。
- **保證金負債**：FINRA 2026-04 名目歷史新高（stock-of-state），淨信用餘額 −$8,710 億；無新月資料。
- **社群情緒**：量子/迷因族群討論度高但未見極端化。

**評分邏輯**：F&G 由貪婪退回中性（54）、AAII 仍淨看空，散戶熱度本週溫和降溫，自 66 下調至 62。

### 5. 貨幣與信貸環境：66 / 100（weight 20%）

- **Fed funds 3.50–3.75%**：連三次按兵不動，4 月 FOMC 4 票異議（1992-10 以來最多）；下次 06-16/17，市場預期續按兵不動。
- **HY OAS 2.72%**：近歷史最緊（歷史低點 2.41%、中位約 4.5%），信用市場定價近乎完美。
- **IG OAS 77 bps（2026-05-12）**：處後金融海嘯以來最低十分位，逼近 2007-02 週期最緊，風險溢價被高度壓縮。
- **10Y 名目 4.49%（06-04）**，較前次 4.45% 上行約 4 bps；spot 實質 DFII10 ≈ 2.08%、breakeven ≈ 2.41%（derived）。**週變動 Δ 分解不可用——無日序資料**（FRED/Treasury/EIA 日序 API 於本環境 403），故不輸出 real-rate vs breakeven 之 Δ 歸因，僅以 spot 水位說明。
- **WTI $95.68（06-04）**：較前次 $87.2 大漲 9.7%，伊朗攻擊科威特/巴林之地緣供給衝擊；強化能源通膨上行路徑。
- **Fed 資產負債表 WALCL ≈ $6.7 兆（2026-05-27）**：Fed 已結束 QT，邊際偏中性。
- **全球流動性交叉檢核**：ECB 續行 QT（2026 約 €500B 不再投資）、BOJ 縮表幅度極小、中國持續寬鬆部分對沖全球緊縮；整體偏緊但中國提供邊際緩衝。

**評分邏輯**：油價急升重啟能源通膨與 Fed 受限風險、信用利差（HY 2.72%/IG 77bps）近歷史最緊顯示風險定價極度自滿，邊際風險自 64 上調至 66。已明確標註 10Y Δ 分解、無 A/D 等缺位輸入未冒充為已觀測。

### 6. 結構性槓桿：72 / 100（weight 15%）

- **槓桿 ETF AUM**：美國槓桿 ETF 市場逾 $170B；TQQQ $31.3B、SOXL 約 $11B、NVDL 一年報酬 +172%；市場走高同步推升 AUM 至高位區。
- **美國單一股票槓桿 ETF 新上市**：本期未見顯著新單一股票槓桿 ETF 上市事件（既有 NVDL/TSLL/CONL 等持續運作）。
- **全球槓桿擴散**：南韓 FSC 已核准並於 5 月下旬（約 05-22）上市三星、SK 海力士之 2 倍單一股票槓桿 ETF。**本週僅南韓單一市場，未出現「同一週 2+ 非美市場核准」，故「全球槓桿擴散訊號」本週未觸發（本週擴散訊號未觸發）**；台灣 TWSE、日本 JPX、歐洲 ESMA 本週無英文揭露的新核准。
- **0DTE 佔比**：約 59–60% 的 SPX 選擇權成交量，處 55–65% 偏高帶。
- **選擇權總量（OCC 2026-05）**：股票選擇權 803.1M（年增 25.5%）、指數 122.6M（年增 32.8%）、ETF 540.5M（年增 23.3%），總量處高位、年增雙位數。
- **VIX 期限結構 / SKEW / 股債相關**：VIX 期限結構偏正常 contango、跨資產偏自滿，作為擁擠選擇權的確認訊號。
- **AI 基建債融資 / vendor-financing 迴圈（升溫）**：CoreWeave 5 月完成 $3.1B DDTL 5.0（首個公開銀團 HPC 基建擔保融資），3 月另完成 $8.5B DDTL 4.0（首個投資級 HPC 擔保融資，Moody's A3）；NVIDIA 以每股 $87.20 投資 CoreWeave $2B 普通股（NVDA 投資、CoreWeave 又採購 NVDA GPU 之循環融資特徵）；Meta 簽約約 $21B（至 2032）、Jane Street 約 $6B。新增大額、抵押品偏向客戶合約之基建債與循環融資為本月結構性升溫。
- **保證金/權益市值比（僅確認）**：FINRA 2026-04 保證金名目新高，作為確認、不重複計分。

**評分邏輯**：依 rubric——AUM 加速近高位、0DTE 約 60%、單一非美市場核准（南韓，未達同週 2+ 之 ◆ 觸發門檻）、AI 基建債與循環融資本月明顯擴張，落於 61–80 高段。因前次推升至 74 的 ◆ 擴散訊號本週未再觸發，邊際自 74 下調至 72；AI 基建循環融資升溫使其維持高檔。

## 綜合分數

| 維度 | 分數 | 權重 | 加權分 |
|---|---:|---:|---:|
| 估值溢價 | 81 | 22% | 17.82 |
| 市場廣度 | 45 | 13% | 5.85 |
| 投機行為 | 70 | 18% | 12.60 |
| 散戶情緒 | 62 | 12% | 7.44 |
| 貨幣與信貸環境 | 66 | 20% | 13.20 |
| 結構性槓桿 | 72 | 15% | 10.80 |
| **加權總分** | | **100%** | **67.71 → 68** |

**綜合評分：68 / 100　　風險等級：高**（區間：低 0–39｜溫和 40–49｜警戒 50–59｜高 60–79｜極度狂熱 80–100）

## 歷史泡沫週期對比

- **1997 早期建設（相似度 25%）**：同為技術建設期的資本投入敘事，但今日 CAPE（41.4）遠高於 1997，估值與槓桿結構更晚期，僅基礎建設期的「敘事吸引資本」特徵相通。
- **1998 LTCM 衝擊（相似度 20%）**：缺乏可比的槓桿爆破與信用事件——當前信用利差近歷史最緊、無再融資壓力，與 1998 中段去槓桿衝擊方向相反。
- **1999 晚期狂熱（相似度 85%，◀ 最貼近）**：CAPE 逼近 2000 頂部、AI 取代網際網路敘事、超大型 IPO 狂熱（SpaceX 史上最大 IPO 臨近）、信用利差極緊、機構高度超配；結構性槓桿以期間調整型代理（0DTE 約 60%、槓桿 ETF 擴散、AI 基建循環融資）對應彼時的散戶槓桿與期權投機。
- **2000/3 頂點（相似度 60%）**：估值極端可比，但本週廣度仍在改善（RSP 續勝）、capex 仍在上修而非反轉，研判尚未抵達「盈利預期反轉」的頂點階段。
- **2021/12 Meme 頂（相似度 68%）**：0DTE 約 60%、槓桿 ETF 普及、保證金名目新高為強共鳴；惟 F&G 僅中性（54）而非 2021 式全面狂熱，且利率非零，散戶情緒尚未達 2021 頂部的一致樂觀。

**詮釋**：當前最貼近 **1999 晚期狂熱**而非 2000/3 頂點——估值極端且超大型 IPO 狂熱升溫（SpaceX），但廣度改善與 capex 持續上修顯示仍處頂部前的「最後一段上行（melt-up）」階段。據此判斷週期位置偏晚期但未見盈利反轉的觸頂訊號；本週新增的油價地緣衝擊，則是 1999 所無、可能加速重定價的外生扳機，須密切追蹤其是否傳導至信用利差。

## 機構情緒對照

本次無新機構調查數據。

（背景參考，非本次新增：最新一期為 BofA 2026 年 5 月基金經理調查——200 位、$5,170 億 AUM，現金 3.9%、股票淨超配 +50% OW、僅 4% 預期硬著陸，已於前次基準 report-2026-06-01 計入；JPMorgan 最新公開目標為 2026 年底 S&P 500 7,600（04-21，EPS $330），本次無新調查或新目標更新。AAII 僅作散戶對照，不列為機構數據。）

## 本次新增訊號

比較基準：vs 前次（3天前，report-2026-06-01）。

| 維度 | 前次 | 本次 | Δ | 觸發事件 |
|---|---:|---:|---:|---|
| 估值溢價 | 82 | 81 | −1 | CAPE 微降至 41.44；NVDA 等 TP 上修以 EPS-driven 為主（28× 不變）；算力供需仍偏緊無過剩 |
| 市場廣度 | 45 | 45 | 0 | RSP 續勝 SPY 約 5ppt；Top-10 約 40%；A/D ⛔ FETCH FAILED |
| 投機行為 | 70 | 70 | 0 | SpaceX S-1（約 06-12、$1.75 兆）升溫；microcap moonshot 本週降溫（無 ≥100% 合格標的） |
| 散戶情緒 | 66 | 62 | −4 | CNN F&G 由 60 退至 54（中性）；AAII 仍淨看空 |
| 貨幣與信貸環境 | 64 | 66 | +2 | WTI 因伊朗攻擊 +9.7% 至 $95.68；10Y +4bps 至 4.49%；HY 2.72%/IG 77bps 近最緊 |
| 結構性槓桿 | 74 | 72 | −2 | ◆ 擴散訊號本週未觸發；CoreWeave $3.1B DDTL 5.0 + NVDA $2B 循環融資升溫 |
| **總分** | **68** | **68** | **0** | melt-up 與情緒降溫相抵，總分持平於「高」 |

**本週最重要訊號：**
1. ⚠ 地緣供給衝擊重定價：伊朗攻擊科威特/巴林，WTI +9.7% 至 $95.68，油 → 通膨預期 → Fed 受限扳機鏈啟動（信用利差尚未擴張）。
2. SpaceX S-1 遞交、預計約 06-12 掛牌（目標 $1.75 兆，史上最大 IPO 之一），mega-IPO 頂部警訊升溫。
3. 散戶熱度降溫：CNN F&G 自 60 退回中性 54；S&P 500 於 6/2 創新高 7,609.78 後 6/3 回落 0.74%。
4. AI 基建循環融資升溫：CoreWeave $3.1B DDTL 5.0、NVDA 以 $87.20/股投資 $2B（循環 vendor-financing 特徵）。
5. 「全球槓桿擴散訊號」本週未觸發（僅南韓單一市場、且為 5 月下旬既有上市）；本週擴散訊號未觸發。

## 數據附錄

**Coverage 表（涵蓋 # Data sources 全部 39 條，依章節順序，各一列一狀態）**

| 維度 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|
| 估值-S&P500 P/E & Shiller CAPE [SEARCH] | GuruFocus/multpl WebSearch | ✓ SEARCH-VERIFIED |
| 估值-Mag7 加權 P/E & AI 龍頭 P/S | WebSearch | ✓ SEARCH-VERIFIED |
| 估值-Mag7/TSMC TP 上修拆解 [SEARCH]（best-effort） | WebSearch（BofA/Bernstein） | ✓ SEARCH-VERIFIED |
| 廣度-RSP vs SPY YTD 散度 | WebSearch | ✓ SEARCH-VERIFIED |
| 廣度-Top-10 集中度 | WebSearch | ✓ SEARCH-VERIFIED |
| 廣度-漲跌比 & 新高/新低比 | WebSearch | ⛔ FETCH FAILED |
| 散戶-CNN Fear & Greed [SEARCH] | WebSearch | ✓ SEARCH-VERIFIED |
| 散戶-保證金負債 & 負債/市值比 | FINRA/WebSearch | ✓ SEARCH-VERIFIED |
| 散戶-AAII 調查 [SEARCH] | WebSearch（05-28） | ✓ SEARCH-VERIFIED |
| 散戶-社群情緒（Reddit/X） | WebSearch | ✓ SEARCH-VERIFIED |
| 機構-BofA FMS & JPM 調查 | WebSearch | ✓ SEARCH-VERIFIED |
| 貨幣-Fed funds DFEDTARU/DFEDTARL [API→Search] | FRED 403→WebSearch | ✓ SEARCH-VERIFIED |
| 貨幣-HY OAS BAMLH0A0HYM2 [API→Search] | FRED 403→WebSearch | ✓ SEARCH-VERIFIED |
| 貨幣-IG OAS BAMLC0A0CM [API→Search] | FRED 403→WebSearch | ✓ SEARCH-VERIFIED |
| 貨幣-10Y DGS10 [API→Treasury→Search] | FRED/Treasury 403→WebSearch（spot） | ✓ SEARCH-VERIFIED |
| 貨幣-10Y 實質 DFII10 [API→Treasury→Search] | FRED/Treasury 403→WebSearch（spot） | ✓ SEARCH-VERIFIED |
| 貨幣-10Y breakeven T10YIE [API→derived→Search] | FRED 403→derived spot（4.49−2.08） | ✓ SEARCH-VERIFIED |
| 貨幣-WTI DCOILWTICO [API→EIA→Search] | FRED/EIA 403→WebSearch | ✓ SEARCH-VERIFIED |
| 貨幣-Fed 資產負債表 WALCL [API→DDP→Search] | FRED 403→WebSearch | ✓ SEARCH-VERIFIED |
| 貨幣-全球央行流動性 ECB/BOJ/PBoC | WebSearch（PBoC 質化） | ✓ SEARCH-VERIFIED |
| AI-超大規模廠商 capex 指引 MSFT/GOOGL/AMZN/META | WebSearch | ✓ SEARCH-VERIFIED |
| AI-token 量成長率（best-effort） | WebSearch | ✗ NOT DISCLOSED |
| AI-OpenAI/Anthropic 年化營收（best-effort） | WebSearch | ✗ NOT DISCLOSED |
| AI-超大規模廠商客戶集中度（best-effort） | WebSearch | ✗ NOT DISCLOSED |
| AI-算力供需與過剩風險 [SEARCH]（best-effort） | WebSearch（GPU/HBM 價） | ✓ SEARCH-VERIFIED |
| 投機-+AI 改名/SPAC/無營收 IPO 暴衝（7 日） | WebSearch | ✓ SEARCH-VERIFIED |
| 投機-IPO 熱度（家數/首日漲幅/無營收佔比） | WebSearch | ✓ SEARCH-VERIFIED |
| 投機-微型股主題 moonshot [SEARCH] | WebSearch（本週無合格標的） | ✓ SEARCH-VERIFIED |
| 投機-即將 IPO（OpenAI/Anthropic/xAI/SpaceX） | WebSearch（SpaceX S-1） | ✓ SEARCH-VERIFIED |
| 投機-內部人拋售 Form 4 [SEC EDGAR] | EDGAR/WebSearch | ✗ NOT DISCLOSED |
| 槓桿-美國槓桿 ETF AUM [SEARCH] | WebSearch | ✓ SEARCH-VERIFIED |
| 槓桿-美國單一股票槓桿 ETF 核准/上市 | EDGAR/ETF.com/WebSearch | ✓ SEARCH-VERIFIED |
| 槓桿-全球槓桿產品核准 KRX/TWSE/JPX/ESMA | WebSearch（南韓） | ✓ SEARCH-VERIFIED |
| 槓桿-0DTE 選擇權量 CBOE | WebSearch | ✓ SEARCH-VERIFIED |
| 槓桿-選擇權總量 OCC 月報 | WebSearch（2026-05） | ✓ SEARCH-VERIFIED |
| 槓桿-跨資產衍生品 VIX 期限/SKEW/股債相關 | WebSearch | ✓ SEARCH-VERIFIED |
| 槓桿-保證金負債/FRED BOGZ1FL073164003.Q（僅確認） | FINRA/WebSearch | ✓ SEARCH-VERIFIED |
| 槓桿-AI 基建債融資/vendor-financing [SEARCH]（best-effort） | WebSearch（CoreWeave） | ✓ SEARCH-VERIFIED |

**原始數據與 SEARCH-VERIFIED 追溯**（檢索時間戳 2026-06-04 Asia/Taipei；FRED `api.stlouisfed.org`、US Treasury `home.treasury.gov`、EIA `api.eia.gov` 之 WebFetch 皆回 HTTP 403，故以下宏觀序列均為 WebSearch spot，金鑰已redacted不顯示）

| 指標 | 數值 | 來源 / query | 發布/資料日期 | 狀態 |
|---|---|---|---|---|
| S&P 500（歷史新高收盤） | 7,609.78 | TheStreet/Motley Fool「S&P 500 finishes above 7,600」 | 2026-06-02 | ✓ SEARCH-VERIFIED |
| S&P 500（最近收盤，−0.74%） | ≈7,553 | TheStreet/CNBC「June 3 2026 stock market」（Iran 飛彈） | 2026-06-03 | ✓ SEARCH-VERIFIED |
| Shiller CAPE | 41.44 | GuruFocus economic_indicators/56 | 2026-06-01 | ✓ SEARCH-VERIFIED |
| S&P 500 普通 P/E | 27.5 | GuruFocus/multpl | 2026-06 | ✓ SEARCH-VERIFIED |
| Mag7 前向 P/E（GOOGL/META/MSFT/AMZN） | 17 / 19.3 / 24.5 / ~36 | Motley Fool「cheapest Mag7」 | 2026-05-30 | ✓ SEARCH-VERIFIED |
| 超大規模廠商 2026 capex 群體 | 約 $725B（+77% YoY） | Yahoo Finance「hyperscaler capex $725B」 | 2026-04（財報） | ✓ SEARCH-VERIFIED |
| GPU 租賃/HBM 價（供需偏緊） | H100 起 ~$1.38/hr；HBM 需求 +70% YoY | SemiAnalysis/IntuitionLabs | 2026-05 | ✓ SEARCH-VERIFIED |
| NVDA TP 上修 | $300→$320（28× 不變，EPS-driven） | TheStreet「BofA resets Nvidia target」 | 2026-05-13 | ✓ SEARCH-VERIFIED |
| TSMC TP | Bernstein $430 / UBS NT$3,000 | TradingKey/TipRanks | 2026-05 | ✓ SEARCH-VERIFIED |
| RSP vs SPY YTD | RSP +約 5ppt | 247WallSt/Benzinga「equal-weight outpacing」 | 2026-06（YTD） | ✓ SEARCH-VERIFIED |
| Top-10 集中度 | 約 40% | 247WallSt/Benzinga | 2026-05/06 | ✓ SEARCH-VERIFIED |
| 漲跌比/新高新低 | 未取得當期值 | WebSearch（僅概念性、無 2026-06 數值） | 日期不可見 | ⛔ FETCH FAILED |
| CNN Fear & Greed | 54（中性） | CNN/feargreedmeter | 2026-06-03 | ✓ SEARCH-VERIFIED |
| AAII 看多/中立/看空 | 35.6% / 22.6% / 41.9% | AAII sentimentsurvey | 2026-05-28 | ✓ SEARCH-VERIFIED |
| FINRA 保證金負債 | 名目歷史新高；淨信用 −$8,710 億 | FINRA（前次延續） | 2026-04 | ✓ SEARCH-VERIFIED |
| BofA FMS（背景） | 現金 3.9%、股票 +50% OW、硬著陸 4% | Axios/Trustnet/HedgeFundTips | 2026-05（05-08~14 調查） | ✓ SEARCH-VERIFIED |
| JPM S&P 500 目標（背景） | 7,600（EPS $330） | TheStreet/TradingView | 2026-04-21 | ✓ SEARCH-VERIFIED |
| Fed funds 目標區間 | 3.50–3.75%（連三次按兵；4 票異議） | Fed/Investing.com；FRED DFEDTARU/DFEDTARL 403 | 2026-04-29（下次 06-16/17） | ✓ SEARCH-VERIFIED |
| HY OAS（series_id=BAMLH0A0HYM2） | 2.72% | GuruFocus/TradingEconomics；FRED API 403 | 2026-06 | ✓ SEARCH-VERIFIED |
| IG OAS（series_id=BAMLC0A0CM） | 77 bps | investmentgrade.com；FRED API 403 | 2026-05-12 | ✓ SEARCH-VERIFIED |
| 10Y 名目（series_id=DGS10） | 4.49% | TradingEconomics；FRED/Treasury 403（spot，無日序） | 2026-06-04 | ✓ SEARCH-VERIFIED |
| 10Y 實質（series_id=DFII10） | 2.08% | TradingEconomics/Fed H.15；FRED/Treasury 403（spot） | 2026-06-03 | ✓ SEARCH-VERIFIED |
| 10Y breakeven（series_id=T10YIE，derived） | ≈2.41%（4.49−2.08） | derived spot（標 derived，非 Δ） | 2026-06-03/04 | ✓ SEARCH-VERIFIED |
| WTI（series_id=DCOILWTICO） | $95.68 /bbl | TradingEconomics/OilPrice；FRED/EIA 403 | 2026-06-04 | ✓ SEARCH-VERIFIED |
| Fed 資產負債表（series_id=WALCL） | 約 $6.7 兆 | macrotrends/AAF；FRED API 403 | 2026-05-27 | ✓ SEARCH-VERIFIED |
| 全球流動性 ECB/BOJ/PBoC | ECB QT≈€500B（2026）、BOJ 微縮、中國寬鬆對沖 | CPRAM/BMO/CapitalWars | 2026 | ✓ SEARCH-VERIFIED |
| AI token 量成長 | 未揭露 | WebSearch | — | ✗ NOT DISCLOSED |
| OpenAI/Anthropic 年化營收 | 未揭露（本季無新揭露/可信外洩） | WebSearch | — | ✗ NOT DISCLOSED |
| 超大規模廠商 AI 客戶集中度 | 未揭露 | WebSearch | — | ✗ NOT DISCLOSED |
| SpaceX IPO | S-1 已遞交，約 06-12 掛牌，目標 $1.75 兆 | CNBC/Yahoo/DealRoom | 2026-05-21~22 | ✓ SEARCH-VERIFIED |
| Cerebras IPO 首日（背景） | +68%（定價 $185，募 $56 億） | 多源（前次計入） | 2026-05-14 | ✓ SEARCH-VERIFIED |
| Microcap moonshot（本週） | 無 ≥100% 合格標的；量子族群 +20–25% | Finviz/HeyGoTrade/StockTitan | 2026-06（本週） | ✓ SEARCH-VERIFIED |
| +AI 改名（本週） | 無新增暴漲案例；Myseum.AI（04）背景 | Benzinga/Bloomberg | 2026-04~05 | ✓ SEARCH-VERIFIED |
| 內部人拋售 Form 4 | 14 日內無申報級明細 | SEC EDGAR/WebSearch | — | ✗ NOT DISCLOSED |
| 槓桿 ETF AUM | 市場 >$170B；TQQQ $31.3B；SOXL ~$11B；NVDL +172%/yr | etf.com/Tickeron | 2026-05/06 | ✓ SEARCH-VERIFIED |
| 美國新單一股票槓桿 ETF 上市 | 本期無顯著新上市事件 | ETF.com/EDGAR/WebSearch | 2026-06 | ✓ SEARCH-VERIFIED |
| 南韓單一股票 2x 槓桿 ETF（三星/SK海力士） | FSC 核准，約 05-22 上市 | Bloomberg/KoreaTimes/AjuPress | 2026-05-22 | ✓ SEARCH-VERIFIED |
| 0DTE 佔 SPX 量 | 約 59–60% | SpotGamma/Cboe/Traders Magazine | 2026（最新） | ✓ SEARCH-VERIFIED |
| OCC 選擇權總量（2026-05） | 股票 803.1M / 指數 122.6M / ETF 540.5M | OCC（Securities Finance Times） | 2026-05（06-02 公布） | ✓ SEARCH-VERIFIED |
| VIX 期限結構/SKEW | 正常 contango、跨資產偏自滿 | Cboe/vixcentral | 2026-06 | ✓ SEARCH-VERIFIED |
| AI 基建債（CoreWeave） | DDTL 5.0 $3.1B（05）、DDTL 4.0 $8.5B（03）、NVDA $2B 入股 @$87.20、Meta $21B、Jane St $6B | SEC 8-K（CoreWeave） | 2026-03~05 | ✓ SEARCH-VERIFIED |

## 本次分數存檔
```json
{
  "date": "2026-06-04",
  "iso_week": "2026-W23",
  "weekday": "Thursday",
  "timezone": "Asia/Taipei",
  "valuation": 81,
  "breadth": 45,
  "speculation": 70,
  "retail": 62,
  "monetary": 66,
  "structural": 72,
  "total": 68,
  "tier": "高"
}
```

本報告為相對風險溫度計，非擇時訊號。
