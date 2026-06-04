# 2026-06-04 市場泡沫風險評估報告
> 報告日期：2026-06-04；執行日：2026-06-04（Asia/Taipei）；ISO 週次：2026-W23；前次基準：report-2026-06-01（3天前）

## §1 六維度風險條圖

| 維度 | 條圖 | 本次 | 前次 | Δ |
|---|---|---:|---:|---:|
| 估值溢價 | ▰▰▰▰▰▰▰▰▱▱ | 81 | 82 | −1 |
| 市場廣度 | ▰▰▰▰▱▱▱▱▱▱ | 45 | 45 | 0 |
| 投機行為 | ▰▰▰▰▰▰▰▱▱▱ | 71 | 70 | +1 |
| 散戶情緒 | ▰▰▰▰▰▰▱▱▱▱ | 64 | 66 | −2 |
| 貨幣與信貸環境 | ▰▰▰▰▰▰▱▱▱▱ | 67 | 64 | +3 |
| 結構性槓桿 | ▰▰▰▰▰▰▰▱▱▱ | 76 | 74 | +2 |
| **加權總分** | ▰▰▰▰▰▰▱▱▱▱ | **69【高】** | 68 | +1 |

註：本週無任一維度 |Δ| ≥ 10，故無 ⚠ 標記。結構性槓桿「全球槓桿擴散訊號」本週未觸發（無 2 個以上非美市場於同一週核准單一個股槓桿／反向 ETF），故「本次」分數後不加 ◆，詳見 §結構性槓桿與本次新增訊號。

## §2 歷史錨點相似度

| 錨點 | 相似度 | 條圖 | 標記 |
|---|---:|---|---|
| 1997 早期建設 | 26% | ▰▰▱▱▱▱▱▱▱▱ |  |
| 1998 LTCM 衝擊 | 22% | ▰▰▱▱▱▱▱▱▱▱ |  |
| 1999 晚期狂熱 | 62% | ▰▰▰▰▰▰▱▱▱▱ | ◀ 最貼近 |
| 2000/3 頂點 | 42% | ▰▰▰▰▱▱▱▱▱▱ |  |
| 2021/12 Meme 頂 | 55% | ▰▰▰▰▰▱▱▱▱▱ |  |

## §3 三角訊號

| 指標 | 本次數值 | vs 前次 |
|---|---|---|
| S&P 500 | 7,599（2026-06-03 收盤） | ▲ +0.3%（前次 ~7,580；6/2 創 7,609.78 新高後回落） |
| WTI 原油 | ~$94.0 /bbl（2026-06-03） | ▲ +7.8%（前次 ~$87.2） |
| 10Y Treasury | 4.49%（2026-06-03/04） | ▲ +4 bps（前次 ~4.45%） |

**三者狀態**：同向偏高（不穩定）。前次格局為「股強、油弱、債中立」的分歧；本週因美伊衝突升溫推升原油，三者同步走高，形成歷史上偏不穩定的配置。

- 股市：S&P 500 6/2 收 7,609.78 創歷史新高，6/3 小幅回落 0.14% 至 ~7,599，仍處紀錄高位、RSI ~75（超買）。
- WTI 原油：~$94/桶，較前次 ~$87.2 上漲約 7.8%，連三日走高，美伊談判破裂與中東緊張帶來地緣風險溢價。
- 10Y 殖利率：4.49%，主要驅動為油價推升通膨預期（breakeven 主導），實質利率變動相對小。

**格局轉變**：前次「股強／油弱／債中立」的分歧格局 → 本次轉為「股、油、債同向偏高」的不穩定共振格局。

**10Y 成因拆解（`ΔDGS10 ≈ ΔDFII10 + ΔT10YIE`，拆的是週變動、非水位）**：本段拆 10Y 之**週變動**（bps），對齊前次基準日 2026-06-01。

- ΔDFII10 實質殖利率週變動：約 −2 bps（實質利率小幅走低；當前 DFII10 ~2.08%）
- ΔT10YIE 損益平衡通膨週變動：約 +6 bps（通膨預期隨油價上行；`derived`）
- 判定：**breakeven-driven**（ΔT10YIE 主導，ΔDFII10 反向小幅）

> 資料限制：本環境 FRED API 與 fredgraph.csv 皆遭 WAF 阻擋（HTTP 403），無法直接抓取序列歷史；T10YIE 以 `DGS10 − DFII10` 推算並標 `derived`，故 `ΔDGS10 ≈ ΔDFII10 + ΔT10YIE` 為定義恆等、僅佐證歸因方向，非獨立交叉驗證。前次基準日之 DFII10／T10YIE 未能由 FRED 獨立取得，上述分項 bps 為依油價驅動之方向性估計；breakeven-driven 之判定由「年底升息機率一週內由 60% 升至 85%」的市場重定價佐證（見扳機鏈）。

**扳機鏈：油 → 通膨預期 → Fed 受限 → refinancing 成本**：本鏈本週正在啟動。油價急升推高 10Y breakeven，市場對 Fed 年底升息機率由約 60%（一週前）跳升至約 85%（6/3）。亞特蘭大／達拉斯聯儲均就 2026 伊朗油價衝擊對通膨之風險發表評論。Fed put 可得性下降：通膨預期上行使聯準會在景氣轉弱時的寬鬆空間受限，將扳機點往前推。

⚠ **結論**：股／油／10Y 同向偏高為歷史上偏不穩定的「泡沫後期最後一段」配置；本週信用面尚未擊發（HY OAS 2.72%、IG OAS ~76 bps 仍極緊，未見再融資壓力），故為「位能升高、尚未引爆」。油價驅動之 breakeven 上行與升息重定價，是本週最值得警戒的觸發機制變化。

## 六維度評分

### 1. 估值溢價：81 / 100（權重 22%）

**核心數據**
- Shiller CAPE：41.44（2026-06-01，GuruFocus），約為歷史中位數（~16）2.5 倍，僅次於 1999–2000 科網頂部（~44）。
- S&P 500 前向 P/E：約 28–29×（歷史均值約 16×）。
- Mag 7 加權 P/E：高檔（自 MSFT ~27× 至 TSLA 高倍數），AI 半導體溢價延續。
- AI 基本面檢查：hyperscaler 2026 capex 合計約 $725B（年增 ~77%），Meta 將全年指引由 $115–145B **上調**至 $125–145B；capex 仍在上修而非下修 → 估值風險未因 capex 轉向而急升。
- AI 算力供需檢查：本週證據顯示**為供給緊俏而非過剩**——H100 一年期租金半年內 +40%，HBM／DRAM 售罄、產能預訂至 2026 年 8–9 月；需求仍在吸收新增產能，未見利用率惡化。
- TP-upgrade 階段訊號：Goldman 將 TSMC 目標由 NT$1,720 上調至 NT$2,330（+35%，ADR ~$370–375），理由為「AI token 需求指數成長、供給受限」；Morgan Stanley／Goldman NVDA $285（$1T 資料中心假設）。多名旗艦股之上調以「結構性 re-rating／長存續 AI 需求」敘事為主，**multiple-driven 成分明顯且跨 2 檔以上**（TSMC、NVDA）→ 晚週期訊號；惟有實質 token 需求佐證，屬 mixed-偏 multiple。

**評分邏輯**：CAPE 持平於 41.4（前次 41.6），6/3 指數小幅回落，估值極致但本週未再擴張；capex 續升、無算力過剩，基本面支撐仍在；TP 上調轉向 multiple-driven 為晚週期風險。綜合自 82 微降至 **81**。

### 2. 市場廣度：45 / 100（權重 13%）

**核心數據**
- RSP（等權）對 SPY（市值權）：RSP 年初至今仍領先約 5 個百分點（廣度相對改善）。
- 前十大集中度：~35.6%（HHI 185 vs 5 年均 142，仍偏高）。
- 內部廣度：僅約 52.2% 成分股站上 50 日均線（參與度低於平均），新高家數於紀錄指數位下「中等」，RSI ~75 偏超買。

**評分邏輯**：等權續勝市值權，廣度未惡化；但 6/2 新高仍由晶片股（Marvell 等）主導、半數成分股未過 50 日線，顯示上漲集中度仍高。維持 **45**。

### 3. 投機行為：71 / 100（權重 18%）

**核心數據**
- 大型 IPO 啟動潮（本週）：SpaceX（含 xAI）6/4 啟動路演、擬募 ~$75B、估值 ~$1.75 兆、擬掛 Nasdaq（SPCX），規模將為史上最大 IPO；Anthropic 6/1 機密遞件 S-1（Series H $65B、估值 ~$965B）；OpenAI 規劃 Q4 IPO（~$1 兆）。三者合計募資潛在 >$240B（流動性抽離風險）。
- 個股事件：Marvell 6/2 因黃仁勳「下一個兆元股」評論單日 +32%；核能 X-energy 上市首日 +27%（AI 帶動）。
- Microcap thematic moonshots：本週掃描 Finviz／Benzinga／Yahoo gainers，**未發現符合條件之 microcap moonshot**（<$1B、單日 ≥100%、2+ 熱門主題堆疊、弱基本面）；量子板塊（Rigetti、IonQ 等）續強但無本週新觸發之 moonshot（前期 ASTC 2026-05-27 已過窗）。
- 內線賣超：過去 14 天無可查得之具 Form 4 申報日／交易日／金額之 AI 領導股叢集（✗ NOT DISCLOSED）。

**評分邏輯**：SpaceX 路演與 Anthropic S-1 同週啟動的「mega-IPO 牆」是本週最強投機訊號，市場普遍視超大型 IPO 為頂部訊號之一；惟本週無新增 microcap moonshot、內線資料不足。自 70 微升至 **71**。

### 4. 散戶情緒：64 / 100（權重 12%）

**核心數據**
- CNN Fear & Greed：54（中性偏貪婪，2026-06-03），較前次 60 回落。
- FINRA 保證金負債（2026 年 4 月）：$1.30 兆創歷史新高（月增 +6.8%、年增 +53.3%）；淨信用餘額 −$8,710 億。保證金負債／美股總市值約 ~1.9%（以 Wilshire 5000 ~$68 兆估算，屬估計值），仍處歷史高檔。
- AAII（最新公布為 2026-05-27 當週）：看多 35.6%、中立 22.6%、看空 41.9%（看空 > 看多，未達頂部式樂觀）。
- 社群情緒：r/wallstreetbets 熱門為 NVDA、MRVL、ASTS；retail 投機回潮、gamma-squeeze 式 call 買盤組織化（社群將此輪比擬 1999）。

**評分邏輯**：保證金槓桿創紀錄、社群投機回潮支撐高分，但 F&G 由 60 → 54 降溫、AAII 看空仍偏高，散戶尚未一面倒。自 66 降至 **64**。
（註：機構情緒另列於「機構情緒對照」，不在本維度計分。）

### 5. 貨幣與信貸環境：67 / 100（權重 20%）

**核心數據**
- 聯邦基金利率：3.50–3.75%（2026-04-29 FOMC 連 3 次按兵不動；下次會議 6/16–17）。**重大轉變：市場對年底升息機率由約 60%（一週前）跳升至約 85%（6/3）**，因油價衝擊推升通膨疑慮。
- HY OAS：2.72%（近歷史最緊，中位數約 4.5%）。
- IG OAS：約 76 bps（0.76%，2026 年 5 月；5/12 為 77 bps），亦處極緊。
- 10Y 名目殖利率週變動拆解（對齊前次基準日 2026-06-01）：ΔDGS10 ≈ +4 bps（4.45%→4.49%）= ΔDFII10 ≈ −2 bps + ΔT10YIE ≈ +6 bps（`derived`）→ **breakeven-driven**（油 → 通膨預期）。詳見 §3 與資料限制說明。
- Fed 資產負債表（WALCL）：QT 持續，自 2022 年中峰值累計縮減約 $2.1 兆，最新 H.4.1 至 2026-05-28；本週無轉向訊號。
- 全球流動性交叉檢查：ECB QT 持續（資產負債表自 2022 年中 €8.8 兆降至 2025 年底約 €6.1 兆，2026 年續不再投資）、BOJ 預期 2026 年 6 月再升息（朝 ~1%）、整體 DM 流動性偏緊；PBoC 本週無英文披露（✗ NOT DISCLOSED）。
- 三角交叉訊號：股／油／10Y 同向偏高（見 §3）；本週為 breakeven-driven 10Y 上行，支持「油 → 通膨預期 → Fed 受限 → refinancing 成本」傳導，惟信用利差尚未走闊。

**評分邏輯**：信用利差仍極緊（HY 2.72%、IG ~76bps）暫壓低分數，但油價衝擊使升息重定價（60%→85%）、breakeven 上行、Fed 與 ECB QT 續行、BOJ 升息，政策路徑明顯轉向不利且 Fed put 可得性下降。自 64 升至 **67**。

### 6. 結構性槓桿：76 / 100（權重 15%）

**核心數據**
- 槓桿 ETF AUM：美國槓桿 ETF 總 AUM 創紀錄 ~$239B，CNBC 6/3 報導「兩個月內翻倍」；TQQQ ~$27B、SOXL ~$9.7B、TSLL ~$6.5B。
- 0DTE 期權：佔 SPX 量約 56–59%（高於前次 45–50%）。
- 期權總量：OCC 2026 年 5 月個股期權 8.031 億口（年增 +25.5%）、指數期權 1.226 億口（+32.8%）、ETF 期權 5.405 億口（+23.3%）。
- 全球槓桿擴散：南韓 Samsung／SK Hynix 單一個股 2x ETF（4/28 核准、5/22 上市）持續膨脹，日成交逾 10 兆韓元、被稱「資金黑洞」；惟屬前期核准之延續，**本週無 2 個以上非美市場同週核准**，台／日／ESMA 本週無新單一個股槓桿 ETF 核准。→「全球槓桿擴散訊號」**本週擴散訊號未觸發**（不加 ◆、不套用 81 分下限）。
- AI 基建債務／廠商融資環：CoreWeave $8.5B 投資級 GPU 擔保貸款（A3／Meta $19B 合約背書，3/31 closed）+ 近期 $3.1B DDTL 5.0 facility，YTD 累計 >$20B 債務／權益；Crusoe $852M。屬 AI capex 交易內部之結構性槓桿。
- 交叉確認：保證金負債／市值比（~1.9% 估）來自散戶情緒，僅作確認、不重複計分；VIX 16.05（6/1，低、期貨正價差）顯示跨資產自滿。

**評分邏輯（對照 rubric）**：0DTE >55%、槓桿 ETF AUM 兩個月翻倍且創紀錄、韓國單一個股槓桿持續擴張、AI 基建債務 YTD >$20B，整體落於 61–80 區間偏上。惟本週全球擴散特別訊號未觸發（無同週 2+ 市場核准），AI 基建債務多為已揭露之投資級／合約背書、未見條款惡化或再融資壓力。自 74 升至 **76**（無 ◆）。

## 綜合分數

| 維度 | 分數 | 權重 | 加權分 |
|---|---:|---:|---:|
| 估值溢價 | 81 | 22% | 17.82 |
| 市場廣度 | 45 | 13% | 5.85 |
| 投機行為 | 71 | 18% | 12.78 |
| 散戶情緒 | 64 | 12% | 7.68 |
| 貨幣與信貸環境 | 67 | 20% | 13.40 |
| 結構性槓桿 | 76 | 15% | 11.40 |
| **合計** | | **100%** | **68.93 → 69** |

**綜合評分：69 / 100　　風險等級：高**

風險等級對照：低 / 溫和 / 警戒 / 高 / 極度狂熱。69 分落於「高」（顯著泡沫風險，需謹慎；尚未達 85+ 之「極度狂熱」歷史頂部特徵）。

## 歷史泡沫週期對比

- **1997 早期建設（26%）**：當前已遠離「早期建設」階段，估值與投機程度遠高於 1997；相似度低。
- **1998 LTCM 衝擊（22%）**：當前無系統性去槓桿衝擊，信用利差極緊而非走闊；相似度低。
- **1999 晚期狂熱（62%，◀ 最貼近）**：CAPE ~41.4 逼近 1999 峰值、AI 敘事 re-rating、mega-IPO 牆（SpaceX／Anthropic／OpenAI）、HY 利差極緊、機構超配，與 1999 末科網狂熱結構最相似。結構性槓桿以期權／0DTE、槓桿 ETF、保證金為當代對應工具。
- **2000/3 頂點（42%）**：尚缺 2000 年 3 月「盈利證偽 + 利差初步走闊」的引爆組合；當前 capex 續升、算力供不應求、利差仍緊，未到證偽點。
- **2021/12 Meme 頂（55%）**：散戶投機回潮、0DTE 與槓桿 ETF AUM 創紀錄、保證金新高與 2021 高度相似；惟當前利率為 3.50–3.75%（非零利率），且本週油價衝擊帶來 2021 所無之通膨／升息壓力。

**詮釋**：本週最貼近 **1999 晚期狂熱**——估值極致、敘事驅動 re-rating、超大型 IPO 集中，屬「泡沫後期最後一段上漲」。惟與 1999 的純粹失速去通膨環境不同，本週疊加油價驅動之通膨／升息重定價（偏 2021/2022 利率風險），意味本輪潛在觸發點更可能來自「利率／再融資」而非單純盈利證偽，位置上仍在頂部區間但尚未引爆。

## 機構情緒對照

本次無新機構調查數據。

最近一次為 BofA 全球基金經理調查（2026 年 5 月：現金 3.9%、跌破 4% 反向賣出訊號、股票淨超配 +50% OW），已於前次（report-2026-06-01）反映；6 月 BofA FMS 通常於月中（~6/16）發布，截至執行日尚未釋出，JPM 亦無新機構調查更新（✗ NOT DISCLOSED）。AAII 僅作散戶對照、不列為機構數據。

## 本次新增訊號

比較基準：vs 前次（3天前，report-2026-06-01）。

| 維度 | 前次 | 本次 | Δ | 觸發事件 |
|---|---:|---:|---:|---|
| 估值溢價 | 82 | 81 | −1 | CAPE 持平 41.4、6/3 回落；TP 上調轉 multiple-driven（TSMC NT$1,720→2,330、NVDA $285）；capex 續升、算力供不應求 |
| 市場廣度 | 45 | 45 | 0 | RSP 仍領先 ~5ppt；僅 52.2% 站上 50 日線；新高仍晶片股主導 |
| 投機行為 | 70 | 71 | +1 | SpaceX 6/4 路演（~$75B/$1.75兆）、Anthropic 6/1 S-1（~$965B）；本週無新 microcap moonshot |
| 散戶情緒 | 66 | 64 | −2 | CNN F&G 60→54 降溫；保證金 $1.30兆新高；AAII 看空 41.9% 仍偏高 |
| 貨幣與信貸環境 | 64 | 67 | +3 | 油價衝擊：年底升息機率 60%→85%；10Y breakeven-driven +4bps；HY 2.72%/IG ~76bps 仍緊 |
| 結構性槓桿 | 74 | 76 | +2 | 槓桿 ETF AUM 兩月翻倍創 ~$239B；0DTE ~56–59%；CoreWeave $8.5B+$3.1B AI 基建債務 |
| **總分** | **68** | **69** | **+1** | 連續第三次上行 |

**本次最重要訊號**
1. **油價衝擊重塑貨幣面**：美伊衝突推 WTI ~$87→$94，10Y breakeven-driven 上行，年底升息機率 60%→85%（Fed put 可得性下降）。
2. **三角訊號轉為同向偏高（不穩定）**：前次股強油弱的分歧 → 本週股／油／10Y 同步走高。
3. **Mega-IPO 牆同週啟動**：SpaceX 路演 + Anthropic S-1，潛在募資 >$240B，頂部訊號特徵。
4. **結構性槓桿加速**：美國槓桿 ETF AUM 兩個月翻倍至創紀錄 ~$239B、0DTE 佔比升至 ~56–59%。
5. **全球槓桿擴散訊號本週未觸發**：南韓單一個股槓桿 ETF 為前期核准之延續，本週無 2+ 非美市場同週核准（背景趨勢，非新觸發）。

## 數據附錄

**Coverage table（對應 `# Data sources` 每一 bullet，依章節順序，共 38 列）**

| 維度 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|
| 估值-1 S&P 500 P/E 與 Shiller CAPE | multpl／GuruFocus [SEARCH]；CAPE 41.44（2026-06-01）、前向 P/E ~28–29× | ✓ SEARCH-VERIFIED |
| 估值-2 Mag 7 加權 P/E 與 AI 龍頭 P/S | 搜尋彙整；Mag 7 高檔、AI 半導體溢價延續 | ✓ SEARCH-VERIFIED |
| 估值-3 分析師 TP 上調拆解（best-effort）| Goldman TSMC NT$1,720→2,330、MS/GS NVDA $285；multiple-driven 佔優 | ✓ SEARCH-VERIFIED |
| 廣度-4 RSP vs SPY YTD | 搜尋；RSP 領先 SPY ~5ppt YTD | ✓ SEARCH-VERIFIED |
| 廣度-5 前十大集中度 | 搜尋；~35.6%、HHI 185 | ✓ SEARCH-VERIFIED |
| 廣度-6 漲跌家數／新高新低 | 搜尋；52.2% 站上 50 日線、新高中等、RSI ~75 | ✓ SEARCH-VERIFIED |
| 散戶-7 CNN Fear & Greed | cnn.com [SEARCH]；54（2026-06-03） | ✓ SEARCH-VERIFIED |
| 散戶-8 Margin Debt 與佔市值比 | FINRA；$1.30兆（2026-04，+6.8% MoM）、佔市值 ~1.9%（估） | ✓ SEARCH-VERIFIED |
| 散戶-9 AAII 散戶調查 | AAII [SEARCH]；看多 35.6%／看空 41.9%（2026-05-27 當週，最新公布） | ✓ SEARCH-VERIFIED |
| 散戶-10 社群情緒（Reddit/X）| WSB 熱門 NVDA/MRVL/ASTS；retail 投機回潮 | ✓ SEARCH-VERIFIED |
| 機構-11 BofA FMS 與 JPM 調查 | 6 月 FMS 未發布；最近為 5 月（現金 3.9%）；JPM 無新調查 | ✗ NOT DISCLOSED |
| 貨幣-12 Fed funds DFEDTARU/DFEDTARL | [API→SEARCH]；3.50–3.75%（FRED API/csv 403，改 SEARCH） | ✓ SEARCH-VERIFIED |
| 貨幣-13 HY OAS BAMLH0A0HYM2 | [API→SEARCH]；2.72%（FRED API/csv 403，改 SEARCH） | ✓ SEARCH-VERIFIED |
| 貨幣-14 IG OAS BAMLC0A0CM | [API→SEARCH]；~76 bps（5 月；FRED API/csv 403，改 SEARCH） | ✓ SEARCH-VERIFIED |
| 貨幣-15 10Y DGS10 | [API→SEARCH]；4.49%（2026-06-03/04；FRED API/csv 403，改 SEARCH） | ✓ SEARCH-VERIFIED |
| 貨幣-16 10Y 實質 DFII10 | [API→SEARCH]；2.08%（2026-06-03；FRED API/csv 403，改 SEARCH） | ✓ SEARCH-VERIFIED |
| 貨幣-17 10Y breakeven T10YIE | [API→SEARCH]；5 月 2.45%、當前拆解值 `derived`（DGS10−DFII10≈2.41%；FRED 403） | ✓ SEARCH-VERIFIED |
| 貨幣-18 WTI DCOILWTICO | [API→SEARCH]；~$94/桶（2026-06-03；FRED API/csv 403，改 SEARCH） | ✓ SEARCH-VERIFIED |
| 貨幣-19 Fed 資產負債表 WALCL | [API→SEARCH]；QT 續行、累計縮 ~$2.1兆、H.4.1 至 2026-05-28（FRED 403，改 SEARCH） | ✓ SEARCH-VERIFIED |
| 貨幣-20 全球央行流動性（ECB/BOJ/PBoC）| ECB QT(~€6.1兆)、BOJ 6 月擬升息；PBoC 無英文披露 | ✓ SEARCH-VERIFIED |
| AI-21 Hyperscaler capex 指引 | 搜尋；2026 合計 ~$725B（+77%），Meta 上修至 $125–145B | ✓ SEARCH-VERIFIED |
| AI-22 AI token 量成長（best-effort）| 僅 Goldman 質性引用「token 需求指數成長」，無量化季度披露 | ✗ NOT DISCLOSED |
| AI-23 OpenAI/Anthropic 營收（best-effort）| Anthropic ~$47B run-rate（6 月）、OpenAI ~$20–25B | ✓ SEARCH-VERIFIED |
| AI-24 Hyperscaler AI 客戶集中度（best-effort）| 無量化披露 | ✗ NOT DISCLOSED |
| AI-25 AI 算力供需／過剩風險（best-effort）| 證據為供給緊俏（H100 租金 +40%、HBM/DRAM 售罄、產能訂至 8–9 月），非過剩 | ✓ SEARCH-VERIFIED |
| 投機-26 +AI 改名/SPAC/無營收 IPO 潮（7d）| 搜尋；mega-IPO 啟動（SpaceX/Anthropic）、X-energy +27%；無明確 +AI 改名案 | ✓ SEARCH-VERIFIED |
| 投機-27 IPO 熱度（家數/首日/無營收占比）| 2025 共 161 件、前十大首日 +37%；無營收占比未精確披露 | ✓ SEARCH-VERIFIED |
| 投機-28 Microcap thematic moonshots | Finviz/Benzinga/Yahoo 掃描；本週無符合條件（<$1B、單日≥100%、2+主題、弱基本面） | ✓ SEARCH-VERIFIED |
| 投機-29 即將 AI IPO（OpenAI/Anthropic/xAI/SpaceX）| SpaceX 6/4 路演 SPCX、Anthropic 6/1 S-1、OpenAI Q4（窗內具名來源） | ✓ SEARCH-VERIFIED |
| 投機-30 內線賣超 Form 4 [SEC EDGAR] | 過去 14 天無可查得之具申報日/金額之 AI 領導股叢集 | ✗ NOT DISCLOSED |
| 槓桿-31 美國槓桿 ETF AUM（NVDL/TSLL/CONL/TQQQ/SOXL/SQQQ）| 創紀錄 ~$239B、兩月翻倍；TQQQ ~$27B、SOXL ~$9.7B、TSLL ~$6.5B | ✓ SEARCH-VERIFIED |
| 槓桿-32 美國單一個股槓桿 ETF 核准/上市 | 本週無新核准/上市（掃描 SEC/ETF.com） | ✓ SEARCH-VERIFIED |
| 槓桿-33 全球槓桿產品核准（KRX/TWSE/JPX/ESMA）| 韓 Samsung/SK Hynix 2x（4/28 核准、5/22 上市）續膨脹；本週台/日/ESMA 無新核准 | ✓ SEARCH-VERIFIED |
| 槓桿-34 0DTE 期權量 | CBOE/SpotGamma；佔 SPX ~56–59% | ✓ SEARCH-VERIFIED |
| 槓桿-35 期權總量（OCC 月報）| OCC 5 月：個股 8.031億(+25.5%)、指數 1.226億(+32.8%)、ETF 5.405億 | ✓ SEARCH-VERIFIED |
| 槓桿-36 跨資產衍生品（VIX 期限結構/SKEW/股債相關）| VIX 16.05（6/1）、期貨正價差；股債相關上升；SKEW 無明確值 | ✓ SEARCH-VERIFIED |
| 槓桿-37 保證金負債/市值比（確認用，不重複計分）| $1.30兆／~$68兆 ≈ ~1.9%（估），僅確認 | ✓ SEARCH-VERIFIED |
| 槓桿-38 AI 基建債務/廠商融資環（best-effort）| CoreWeave $8.5B+$3.1B、Crusoe $852M、YTD >$20B | ✓ SEARCH-VERIFIED |

**原始數據重點**

| 指標 | 數值 | 來源 | 日期 | 狀態 |
|---|---|---|---|---|
| S&P 500 收盤 | 7,599（6/2 創 7,609.78 新高） | CNBC/Motley Fool/TheStreet | 2026-06-03 | ✓ SEARCH-VERIFIED |
| Shiller CAPE | 41.44 | GuruFocus | 2026-06-01 | ✓ SEARCH-VERIFIED |
| WTI 原油 | ~$94/桶（部分報價至 $95.7） | TradingEconomics/Oilprice | 2026-06-03 | ✓ SEARCH-VERIFIED |
| 10Y DGS10 | 4.49% | TradingEconomics/Fed H.15 | 2026-06-03/04 | ✓ SEARCH-VERIFIED |
| 10Y 實質 DFII10 | 2.08% | TradingEconomics | 2026-06-03 | ✓ SEARCH-VERIFIED |
| 10Y breakeven T10YIE | 2.45%（5 月）；當前 ~2.41% `derived` | FRED/TradingEconomics | 2026-05 / 推算 | ✓ SEARCH-VERIFIED（current derived）|
| HY OAS | 2.72% | FRED/TradingEconomics | 2026-05 | ✓ SEARCH-VERIFIED |
| IG OAS | ~76 bps（5/12 為 77bps） | FRED/TradingEconomics | 2026-05 | ✓ SEARCH-VERIFIED |
| Fed funds 目標 | 3.50–3.75% | Fed FOMC | 2026-04-29 | ✓ SEARCH-VERIFIED |
| 年底升息機率 | ~85%（一週前 ~60%） | TradingEconomics/市場定價 | 2026-06-03 | ✓ SEARCH-VERIFIED |
| CNN Fear & Greed | 54 | CNN Business | 2026-06-03 | ✓ SEARCH-VERIFIED |
| FINRA 保證金負債 | $1.30兆（+6.8% MoM、+53.3% YoY） | FINRA/Advisor Perspectives | 2026-04 | ✓ SEARCH-VERIFIED |
| AAII 看多/看空 | 35.6% / 41.9% | AAII | 2026-05-27 當週 | ✓ SEARCH-VERIFIED |
| Hyperscaler 2026 capex | ~$725B（+77%）；Meta 上修 $125–145B | Tom's Hardware/CNBC | 2026 | ✓ SEARCH-VERIFIED |
| Anthropic run-rate | ~$47B（6 月） | VentureBeat/MSN | 2026-06 | ✓ SEARCH-VERIFIED |
| GPU 租金/記憶體 | H100 一年租金半年 +40%、HBM/DRAM 售罄 | SemiAnalysis/TrendForce | 2026-05/06 | ✓ SEARCH-VERIFIED |
| 槓桿 ETF 總 AUM | ~$239B（兩月翻倍） | CNBC/Tekedia | 2026-06-03 | ✓ SEARCH-VERIFIED |
| 0DTE 佔 SPX | ~56–59% | Cboe/IBKR | 2026 | ✓ SEARCH-VERIFIED |
| OCC 5 月期權量 | 個股 8.031億/指數 1.226億/ETF 5.405億 | OCC | 2026-05 | ✓ SEARCH-VERIFIED |
| 韓單一個股槓桿 ETF | Samsung/SK Hynix 2x，日成交 >10兆韓元 | Seoul Economic/CNBC | 2026-06-03 | ✓ SEARCH-VERIFIED |
| CoreWeave AI 基建債務 | $8.5B（IG，A3，Meta 背書，3/31）+$3.1B DDTL | Bloomberg/CoreWeave IR | 2026 | ✓ SEARCH-VERIFIED |
| VIX | 16.05（期貨正價差） | S&P/StreetStats | 2026-06-01 | ✓ SEARCH-VERIFIED |
| SpaceX IPO | 路演 6/4、~$75B、估值 ~$1.75兆、SPCX | CNBC/TradingKey | 2026-06 | ✓ SEARCH-VERIFIED |
| Anthropic S-1 | 機密遞件、估值 ~$965B、Series H $65B | Fortune/TheNextWeb | 2026-06-01 | ✓ SEARCH-VERIFIED |

> 註：本環境 FRED `api.stlouisfed.org` 與 `fredgraph.csv` 經 WebFetch 皆回 HTTP 403（WAF），FRED 系列改以 WebSearch 取得當前值（✓ SEARCH-VERIFIED）；T10YIE 當前拆解值以 `DGS10 − DFII10` 推算並標 `derived`。前次基準日 FRED 原始觀測未能由 FRED 獨立取得，10Y 分項 Δ 為方向性估計（見 §3 資料限制）。FRED_API_KEY 已依規不輸出於本報告任何處。

## 本次分數存檔
```json
{
  "date": "2026-06-04",
  "iso_week": "2026-W23",
  "weekday": "Thursday",
  "timezone": "Asia/Taipei",
  "valuation": 81,
  "breadth": 45,
  "speculation": 71,
  "retail": 64,
  "monetary": 67,
  "structural": 76,
  "total": 69,
  "tier": "高"
}
```

本報告為相對風險溫度計，非擇時訊號。
