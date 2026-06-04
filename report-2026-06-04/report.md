# 2026-06-04 市場泡沫風險評估報告
> 報告日期：2026-06-04；執行日：2026-06-04（Asia/Taipei）；ISO 週次：2026-W23；前次基準：report-2026-06-01（3天前）
>
> 註：執行時點為 Asia/Taipei 6/4 13:40，美股 6/4 盤尚未開市，故市場／FRED 之「本次」最新有效觀測為 6/3，前次基準對齊 6/1 收盤。FRED 官方 API（環境金鑰）、`fredgraph.csv`、WebFetch 於本環境網路政策下均被阻擋（API host 非允許清單；website 路徑 403），所有 FRED 系列改以 WebSearch 取得當前可用值，標記 ✓ SEARCH-VERIFIED（非抓取失敗）；T10YIE 無法直接抓取，於 §3 以 `DGS10 − DFII10` 推算並標 derived。

## §1 六維度風險條圖

| 維度 | 條圖 | 本次 | 前次 | Δ |
|---|---|---:|---:|---:|
| 估值溢價 | ▰▰▰▰▰▰▰▰▱▱ | 81 | 82 | −1 |
| 市場廣度 | ▰▰▰▰▱▱▱▱▱▱ | 48 | 45 | +3 |
| 投機行為 | ▰▰▰▰▰▰▰▱▱▱ | 72 | 70 | +2 |
| 散戶情緒 | ▰▰▰▰▰▰▱▱▱▱ | 62 | 66 | −4 |
| 貨幣與信貸環境 | ▰▰▰▰▰▰▱▱▱▱ | 65 | 64 | +1 |
| 結構性槓桿 | ▰▰▰▰▰▰▰▱▱▱ | 72 | 74 | −2 |
| **加權總分** | ▰▰▰▰▰▰▱▱▱▱ | **68【高】** | 68 | 0 |

本週無任一維度 |Δ| ≥ 10（⚠ 未觸發）；「全球槓桿擴散訊號」本週未觸發（◆ 未標記）。

## §2 歷史錨點相似度

| 錨點 | 相似度 | 條圖 | 標記 |
|---|---:|---|---|
| 1997 早期建設 | 22% | ▰▰▱▱▱▱▱▱▱▱ |  |
| 1998 LTCM 衝擊 | 20% | ▰▰▱▱▱▱▱▱▱▱ |  |
| 1999 晚期狂熱 | 58% | ▰▰▰▰▰▱▱▱▱▱ | ◀ 最貼近 |
| 2000/3 頂點 | 42% | ▰▰▰▰▱▱▱▱▱▱ |  |
| 2021/12 Meme 頂 | 46% | ▰▰▰▰▱▱▱▱▱▱ |  |

## §3 三角訊號

| 指標 | 本次數值 | vs 前次 |
|---|---|---|
| S&P 500 | 7,553.68（6/3 收盤） | ▼ −0.6%（前次 7,599.96，6/1） |
| WTI 原油 | $94.0 /桶（6/3） | ▲ +4%（前次 ~$90，6/1，約略） |
| 10Y Treasury | 4.49%（6/3） | 持平 +1bp（前次 4.48%，6/1） |

**三者狀態**：出現分歧（WTI 原油在重新定價）

- 股市：7,553.68（6/3），自 6/1 歷史收盤高 7,599.96 回落 −0.6%，仍距歷史高點不到 1%，6/2 曾首度收上 7,600。
- WTI 原油：$94.0（6/3），連三日上漲、較 6/1 約 +4%；美伊停火惡化、地緣風險溢價回升推動由空翻多。
- 10Y 殖利率：4.49%（6/3），較 6/1（4.48%）近乎持平（+1bp），主要由實質利率小幅推動。

**格局轉變**：前次（6/1）為「股強、油弱、債中立」；本次轉為「股微幅回檔、油急升、債持平」——油價由空翻多，三角由共振偏多轉為分歧。

**10Y 成因拆解（`ΔDGS10 ≈ ΔDFII10 + ΔT10YIE`，拆的是週變動、非水位）**：本段拆 6/1→6/3 的 10Y 週變動（bps）。

- ΔDFII10 實質殖利率週變動：約 +3 bps（上行；6/1 ~2.05% → 6/3 2.08%）
- ΔT10YIE 損益平衡通膨週變動：約 −2 bps（下行，derived；6/1 ~2.43% → 6/3 2.41%）
- 判定：real-rate-driven（惟整體幅度極小，ΔDGS10 僅 +1bp）。註：T10YIE 因 FRED API／CSV／WebFetch 三路均被本環境網路政策阻擋而無法直接抓序列，故以 `DGS10 − DFII10` 推算並標 `derived`；此時 `ΔDGS10 ≈ ΔDFII10 + ΔT10YIE` 為定義恆等、僅佐證歸因，非獨立交叉驗證。

**扳機鏈：油 → 通膨預期 → Fed 受限 → refinancing 成本**：油價急升理論上經通膨預期傳導至殖利率，但本週 breakeven 不升反微降，顯示市場尚未把油價上漲計入長期通膨預期，扳機鏈尚未啟動。Fed 維持 3.50–3.75%、6/16–17 FOMC 市場預期按兵不動；4/29 會議 4 票異議（偏鴿，Miran 主張降息）顯示 Fed put 仍相對可得，惟能源通膨上行風險使鴿派空間受限。

**結論**：估值極度拉伸（CAPE 41.4）疊加結構性槓桿偏高構成「崩跌位能」，但融資面尚未收緊——HY OAS 仍約 2.7% 處歷史極緊、信用利差未擴大、refinancing 壓力未現——時點扳機未擊發。三者未同向偏高、油價分歧上行，當前屬泡沫後期但尚未進入擊發階段（基準未觸發 ⚠）。

## 六維度評分

### 1. 估值溢價：81 / 100（權重 22%）

Shiller CAPE 41.44（6/1，GuruFocus／multpl）為歷史長期均值約 17.3 之 2.4 倍、僅次於 1999/12 峰值 44.19；S&P 500 本益比 27.5（6/2，multpl）高於 20 年均值 25.4；hyperscaler 2026 capex 指引仍在上調（Meta 上修至 $125–145B、合計約 $700B、近 2025 兩倍，約 75% 投向 AI 基建）對估值形成基本面支撐，但本週指數自高點回落、CAPE 微降，故由 82 微降至 81。AI 運算供需／利用率方面，本次未取得 GPU 租金、HBM/DRAM 價格、交期或稼動率等直接證據，依規則降級結論為「capex／Nvidia 營收仍支撐，但未取得直接利用率證據」，相關利用率項目標 ✗ NOT DISCLOSED。TP 上調相位：最近一筆合格賣方大幅上調為 UBS 對 Micron $535→$1,625（約 5 月底，target PE 擴張幅度大於 EPS 修正），屬 multiple-driven；搭配 Morgan Stanley TSMC 20–30× target PE 之 re-rating 校準錨，顯示上調主導槓桿仍偏向 multiple 而非 E（晚周期訊號）。

### 2. 市場廣度：48 / 100（權重 13%）

RSP 對 SPY 之 YTD 領先收斂、訊號轉混（一來源顯示 RSP 10.12% 對 SPY 11.69% 已落後），且 6/2–6/3 的新高由晶片股主導（「chipmakers drive S&P to record」）、最擁擠交易為 long semis 73%，顯示窄幅大型權值股重新主導；前十大權值與科技板塊集中度仍高（科技 >30%）。廣度較前次略轉差，由 45 上調至 48。

### 3. 投機行為：72 / 100（權重 18%）

SpaceX（SPCX）路演約於 6/4 啟動、目標 6/12 掛牌、估值約 $1.75 兆、募資約 $75B（史上最大 IPO，已併入 xAI），為本週最新投機催化劑；2026 AI／科技 IPO 管線合計約 $3.12 兆（OpenAI ~$1T、Anthropic ~$300B、Databricks ~$134B），CNBC 等分析師明言「mega-IPO 可能是頂部訊號」。微型股月內多檔翻倍（Wolfspeed、Innodata +86% 跳空、Ambiq、Hyliion 因美國海軍 KARNO +40%、Rackspace），但本週（6/1–6/4）未發現符合嚴格條件（單日 ≥100%、市值 <$1B、雙主題堆疊 + 弱基本面）之 moonshot，標 ✗ NOT DISCLOSED。內部人賣壓：本次未取得 14 日內具 Form 4 申報日／交易日／EDGAR URL 之合格資料，標 ✗ NOT DISCLOSED（不引用過時名單）。SpaceX 迫近 + AI IPO 狂熱延續推升本維度，由 70 上調至 72。

### 4. 散戶情緒：62 / 100（權重 12%）

CNN 恐懼貪婪指數 54（中立，6/3）較前次 60（貪婪）回落，顯示散戶情緒降溫；AAII（最新可得 5/28）看多 35.6%／中立 22.6%／看空 41.9%，看空仍高於看多、未達頂部式樂觀；FINRA 保證金負債 4 月 $1.304 兆創歷史新高（MoM +6.8%、YoY +53.3%），名目槓桿水位偏高但為月頻、未更新。F&G 降溫為主導因素，由 66 下調至 62。

### 5. 貨幣與信貸環境：65 / 100（權重 20%）

Fed 維持 3.50–3.75%、6/16–17 預期按兵不動、4 票異議；HY OAS 約 2.72%（ICE BofA，最新快照）仍處歷史極緊、IG OAS 約 80bps，信用風險溢價幾被消磨；10Y 4.49%（6/3）週變動近乎持平（+1bp，實質利率主導、breakeven 微降）；WALCL 約 $6.71 兆（5/27），QT 已於 2025/12 結束、每月仍約 $25B 縮減，全球流動性大致持平偏緊。油價急升加入「能源通膨 → Fed 受限」之上行風險，惟尚未經 breakeven 傳導，由 64 微升至 65。

### 6. 結構性槓桿：72 / 100（權重 15%）

美國槓桿 ETF 總規模逾 $170B 創高（SOXL $17.3B／2026 +261%、TQQQ $31.3B／+38.6%），惟近期 TQQQ／SOXL 出現獲利了結淨流出；0DTE 約佔 S&P 500 期權量 45–50%（CBOE，沿用）；SKEW 143.24（6/3）偏高、VIX 15.77（6/2）偏低顯示跨資產自滿。AI 基建債務：CoreWeave 於 5/18 完成 $3.1B DDTL 5.0（Ba2／BB+，首檔公開銀團 HPC 基建抵押融資），加計先前 $8.5B DDTL 4.0（A3，Meta 合約背書），YTD 債+股逾 $20B，GPU 抵押債屬 AI capex 交易內生槓桿、為 30 日內新增訊號。全球擴散：南韓 5/22 起上市單一股票槓桿 ETF（三星、SK 海力士，2×）為單一市場、且非本週事件；本週無 2 個以上非美市場同週核准，**全球槓桿擴散訊號未觸發**，不設 81 分樓地板。綜合 AUM 創高但部分流出、AI 基建債持續擴張、0DTE 偏高，由 74 下調至 72（移除前次誤標之 ◆，依規則重評）。

## 綜合分數

| 維度 | 分數 | 權重 | 加權分 |
|---|---:|---:|---:|
| 估值溢價 | 81 | 22% | 17.82 |
| 市場廣度 | 48 | 13% | 6.24 |
| 投機行為 | 72 | 18% | 12.96 |
| 散戶情緒 | 62 | 12% | 7.44 |
| 貨幣與信貸環境 | 65 | 20% | 13.00 |
| 結構性槓桿 | 72 | 15% | 10.80 |
| **合計** | | **100%** | **68.26 → 68** |

**綜合評分：68 / 100　　風險等級：高**（區間：0–39 低／40–59 溫和／60–79 高／80–100 極度狂熱；本制度 60–79 標示為「高」，「警戒」為 50 分級舊稱，已對齊新等級表）

## 歷史泡沫週期對比

- **1997 早期建設（22%）**：當前已遠離基建早期、估值早已極端化，僅 AI 資本支出狂潮之「建設」氛圍部分呼應，相似度低。
- **1998 LTCM 衝擊（20%）**：屬中周期槓桿爆破型衝擊，當前無對應之系統性去槓桿事件、波動極低（VIX 15.8），相似度低。
- **1999 晚期狂熱（58%）**：CAPE 41.4 已達 1999 峰值 44.19 之 94%、AI 取代網際網路敘事、史上最大 IPO（SpaceX $1.75 兆）與 $3.12 兆 IPO 管線呼應當年 IPO 熱潮、HY 利差極緊、機構超配股票——多維共鳴，為本週最貼近錨點。
- **2000/3 頂點（42%）**：估值面已逼近頂點特徵，但廣度尚未全面崩壞、信用利差未擴大、Fed 尚未進入緊縮末段，距「頂點擊發」仍有距離。
- **2021/12 Meme 頂（46%）**：0DTE、槓桿 ETF（>$170B）、保證金負債創高、散戶槓桿等行為面高度相似；惟利率為 3.50–3.75% 而非零利率，貨幣背景明顯不同（以期間調整之槓桿代理比較）。

**詮釋**：本週最相似於 1999 晚期狂熱（58%）——估值與敘事狂熱俱在、史上最大 IPO 迫近，屬泡沫「最後一段上漲」的晚周期位置；惟信用利差仍極緊、廣度未崩、Fed put 相對可得，尚未出現 2000/3 式的擊發條件，意味當前位於晚周期但非即將見頂的確認點。

## 機構情緒對照

本次無新機構調查數據。

（背景，非本次新增：BofA 5 月 FMS〔調查期 5/8–5/14，200 位、$5,170 億 AUM〕已於 6/1 前次報告納入——現金 3.9%〔跌破 4.0% 賣出訊號〕、股票配置創紀錄單月跳升、最擁擠交易為 long global semiconductors 73%〔自 4 月 24% 跳升〕、Mag 7 14%、油 6%。6 月 FMS 與最新 JPM 機構調查截至執行時點尚未發布，故本次不計入評分變動。AAII 僅作散戶對照、非機構數據。）

## 本次新增訊號

比較基準：vs 前次（3天前，report-2026-06-01）。

| 維度 | 前次 | 本次 | Δ | 主要原因 |
|---|---:|---:|---:|---|
| 估值溢價 | 82 | 81 | −1 | 指數自高點回落、CAPE 微降至 41.44；capex 指引仍上調 |
| 市場廣度 | 45 | 48 | +3 | 6/2–6/3 晶片股主導新高、RSP 領先收斂，窄幅化 |
| 投機行為 | 70 | 72 | +2 | SpaceX 路演啟動／6/12 掛牌迫近（$1.75 兆，史上最大 IPO） |
| 散戶情緒 | 66 | 62 | −4 | CNN F&G 60→54（貪婪轉中立），散戶降溫 |
| 貨幣與信貸環境 | 64 | 65 | +1 | 油價急升加入能源通膨上行風險；HY OAS 仍極緊 |
| 結構性槓桿 | 74 | 72 | −2 | 移除前次誤標 ◆、本週無擴散觸發；惟 AI 基建債續擴張 |
| **總分** | **68** | **68** | **0** | 估值／散戶降溫被投機／廣度上行抵銷，整體持平 |

**本次重點**：
1. WTI 原油由空翻多（連三日漲、6/3 約 $94），美伊停火惡化推升地緣風險溢價；三角由共振轉分歧。
2. SpaceX（SPCX）路演約 6/4 啟動、目標 6/12 掛牌，估值 $1.75 兆、募資 ~$75B——史上最大 IPO，投機情緒指標。
3. CNN 恐懼貪婪指數自 60 降至 54，散戶情緒由貪婪轉中立。
4. CoreWeave 5/18 完成 $3.1B DDTL 5.0（首檔公開銀團 GPU 基建抵押融資），AI 基建債務續擴張。
5. 「全球槓桿擴散訊號」**本週擴散訊號未觸發**（南韓單一股票槓桿 ETF 屬 5/22 既有事件、單一市場，無 2 個以上非美市場同週核准）。

## 數據附錄

抓取時間戳統一為 2026-06-04T13:40+08:00（Asia/Taipei）。FRED 系列：官方 API（環境金鑰，金鑰已隱去）與 `fredgraph.csv` 之 host 不在本環境網路允許清單、WebFetch 對 FRED 回 403，三路直抓／API 均失敗，改以 WebSearch 取得當前可用值，標 ✓ SEARCH-VERIFIED（非 ⛔）。

| 指標 | 數值 | 來源 / FRED series | 資料日期 | 狀態 |
|---|---|---|---|---|
| S&P 500 收盤 | 7,553.68 | The Motley Fool / TheStreet（SP500） | 2026-06-03 | ✓ SEARCH-VERIFIED |
| S&P 500 前次收盤 | 7,599.96（紀錄收盤） | Yahoo Finance / CNBC | 2026-06-01 | ✓ SEARCH-VERIFIED |
| S&P 500 首破 7,600 收盤 | >7,600 | CNBC | 2026-06-02 | ✓ SEARCH-VERIFIED |
| Shiller CAPE | 41.44 | GuruFocus / multpl | 2026-06-01 | ✓ SEARCH-VERIFIED |
| 1999 CAPE 峰值 | 44.19 | Shiller / multpl | 1999-12 | ✓ SEARCH-VERIFIED |
| S&P 500 P/E | 27.5（20年均 25.4） | multpl | 2026-06-02 | ✓ SEARCH-VERIFIED |
| WTI 原油 | $94.0 /桶 | Fortune（DCOILWTICO 代理） | 2026-06-03 | ✓ SEARCH-VERIFIED |
| WTI 原油（6/2） | $92.21 | Fortune | 2026-06-02 | ✓ SEARCH-VERIFIED |
| WTI 原油 前次（約略） | ~$90 /桶 | 由 5/30 $87.2 與 6/2 $92.21 內插推估 | 2026-06-01 | ✓ SEARCH-VERIFIED（約略） |
| 10Y Treasury（DGS10） | 4.49% | Trading Economics / FRED DGS10 | 2026-06-03 | ✓ SEARCH-VERIFIED |
| 10Y 前次（DGS10） | 4.48% | Trading Economics / FRED DGS10 | 2026-06-01 | ✓ SEARCH-VERIFIED |
| 10Y 實質殖利率（DFII10） | 2.08% | Trading Economics / FRED DFII10 | 2026-06-03 | ✓ SEARCH-VERIFIED |
| 10Y 實質殖利率 前次（DFII10） | ~2.05% | FRED DFII10（6/2 2.05% 推近） | 2026-06-01 | ✓ SEARCH-VERIFIED（約略） |
| 10Y breakeven（T10YIE） | 2.41%（=DGS10−DFII10） | derived（FRED 無法直抓） | 2026-06-03 | derived |
| ΔDGS10 / ΔDFII10 / ΔT10YIE | +1 / +3 / −2 bps | 由上列各序列 6/1→6/3 計算 | 2026-06-01→06-03 | ✓ / ✓ / derived |
| Fed funds 目標區間 | 3.50–3.75% | Fed FOMC（DFEDTARU/L） | 2026-04-29 | ✓ SEARCH-VERIFIED |
| FOMC 異議票 | 4 票（1992/10 以來最多） | Fed FOMC 聲明 | 2026-04-29 | ✓ SEARCH-VERIFIED |
| 6 月 FOMC 預期 | 按兵不動（6/16–17） | Polymarket / Trading Economics | 2026-06 | ✓ SEARCH-VERIFIED |
| HY OAS（BAMLH0A0HYM2） | ~2.72% | ICE BofA / FRED（最新快照，6/3 日值未取得） | 2026-05（snapshot） | ✓ SEARCH-VERIFIED |
| IG OAS（BAMLC0A0CM） | ~80 bps | ICE BofA / FRED | 2026 上半（snapshot） | ✓ SEARCH-VERIFIED |
| Fed 資產（WALCL） | ~$6.71 兆 | AAF / FRED WALCL | 2026-05-27 | ✓ SEARCH-VERIFIED |
| CNN 恐懼貪婪指數 | 54（中立） | CNN Business / Benzinga | 2026-06-03 | ✓ SEARCH-VERIFIED |
| AAII 看多/中立/看空 | 35.6% / 22.6% / 41.9% | AAII | 2026-05-28（最新可得） | ✓ SEARCH-VERIFIED |
| FINRA 保證金負債 | $1.304 兆（MoM +6.8%、YoY +53.3%，創高） | FINRA / Advisor Perspectives | 2026-04 | ✓ SEARCH-VERIFIED |
| RSP vs SPY YTD | 訊號轉混（RSP 10.12% vs SPY 11.69%；另有來源 RSP 領先 ~5ppt） | PortfoliosLab / 247WallSt | 2026 YTD | ✓ SEARCH-VERIFIED |
| 科技板塊權重（市值加權） | >30% | etf.com / kavout | 2026-06 | ✓ SEARCH-VERIFIED |
| BofA FMS 現金（背景） | 3.9%（跌破 4% 賣出訊號） | BofA Global Research / Axios | 2026-05 調查 | ✓ SEARCH-VERIFIED |
| BofA FMS 最擁擠交易（背景） | long semis 73% | BofA / hedgefundtips | 2026-05 調查 | ✓ SEARCH-VERIFIED |
| 槓桿 ETF 總規模 | >$170B（SOXL $17.3B、TQQQ $31.3B） | etf.com | 2026 | ✓ SEARCH-VERIFIED |
| 0DTE 佔 SPX 期權量 | ~45–50% | CBOE（沿用） | 2026-05/06 | ✓ SEARCH-VERIFIED |
| VIX | 15.77 | Vol Vibes / FRED VIXCLS | 2026-06-02 | ✓ SEARCH-VERIFIED |
| SKEW | 143.24 | Cboe / Yahoo | 2026-06-03 | ✓ SEARCH-VERIFIED |
| 南韓單一股票槓桿 ETF | 5/22 上市（三星、SK 海力士，2×） | Seoul Economic Daily / Bloomberg | 2026-05-22 | ✓ SEARCH-VERIFIED |
| 台灣/日本/歐洲 同類核准 | 本週無英文揭露 | KRX/TWSE/JPX/ESMA | 2026-06 | ✗ NOT DISCLOSED |
| CoreWeave DDTL 5.0 | $3.1B（Ba2/BB+，首檔公開銀團 HPC 抵押） | CoreWeave IR / Morningstar | 2026-05-18 | ✓ SEARCH-VERIFIED |
| CoreWeave DDTL 4.0 | $8.5B（A3，Meta 合約背書） | CoreWeave IR | 2026（背景） | ✓ SEARCH-VERIFIED |
| Hyperscaler 2026 capex | ~$700B（AMZN $200B、GOOGL $175–185B、META $125–145B 上修、MSFT $110–120B） | Tom's Hardware / Futurum | 2026 指引 | ✓ SEARCH-VERIFIED |
| Anthropic run-rate 營收 | ~$44B 年化、Q2 首次營業利益 ~$559M | FT / CNBC | 2026-05 | ✓ SEARCH-VERIFIED |
| SpaceX IPO（SPCX） | 6/12 目標掛牌、$1.75 兆、募資 ~$75B、路演 ~6/4 | CNBC / TechCrunch / cryptonews | 2026-05-20 申報 | ✓ SEARCH-VERIFIED |
| AI IPO 管線估值 | ~$3.12 兆（12 檔） | dealroom / Bloomberg | 2026-05 | ✓ SEARCH-VERIFIED |
| TP 上調（multiple-driven） | UBS Micron $535→$1,625；MS TSMC 20–30× | UBS / Morgan Stanley | 2026-05（~14日窗內） | ✓ SEARCH-VERIFIED |
| 本週合格 microcap moonshot | 無（單日≥100%＋雙主題＋弱基本面） | Benzinga movers | 2026-06-01→04 | ✗ NOT DISCLOSED |
| AI 內部人賣壓 Form 4（14日內） | 無合格申報級資料 | SEC EDGAR | 2026-06 | ✗ NOT DISCLOSED |
| GPU 租金／HBM 價格／稼動率 | 未取得直接證據 | 多來源 | 2026-06 | ✗ NOT DISCLOSED |
| PBoC 流動性 | 無當期英文摘要 | PBoC/NBS | 2026-06 | ✗ NOT DISCLOSED |

**✓ SEARCH-VERIFIED 追溯（要項）：**

- 「10Y / DFII10」：query `10-year Treasury yield DGS10 / TIPS real yield DFII10 early June 2026` → Trading Economics（US 10Y Treasury，發布日 2026-06-03，10Y 4.49%、TIPS 2.08%）；URL https://tradingeconomics.com/united-states/government-bond-yield 、 https://tradingeconomics.com/united-states/10-year-tips-yield ；抓取 2026-06-04T13:40+08:00；原意源 FRED DGS10/DFII10。
- 「S&P 6/3」：query `S&P 500 closing price June 1 June 2 June 3 June 4 2026` → The Motley Fool / TheStreet（資料日 2026-06-02/03）；URL https://www.fool.com/coverage/stock-market-today/2026/06/02/ ；抓取 2026-06-04T13:40+08:00；原意源 S&P DJI / Yahoo。
- 「WTI 6/3」：query `WTI crude oil settlement price June 1 2026 and June 3 2026` → Fortune（資料日 2026-06-03，$94.00；6/2 $92.21）；URL https://fortune.com/article/price-of-oil-06-03-2026/ ；抓取 2026-06-04T13:40+08:00；原意源 CME/EIA DCOILWTICO。
- 「CAPE」：query `S&P 500 Shiller CAPE ratio current June 2026 multpl` → GuruFocus（資料日 2026-06-01，41.44）；URL https://www.gurufocus.com/economic_indicators/56/sp-500-shiller-cape-ratio ；抓取 2026-06-04T13:40+08:00；原意源 multpl/Shiller。
- 「CNN F&G」：query `CNN Fear and Greed Index today June 2026` → Benzinga（資料日 2026-06-03，54）；URL https://www.benzinga.com/markets/equities/26/06/52895973/ ；抓取 2026-06-04T13:40+08:00；原意源 CNN Business。
- 「南韓單一股票槓桿 ETF」：query `single-stock leveraged ETF approval Korea ... 2026` → Seoul Economic Daily（資料日 2026-04-21，5/22 上市）；URL https://en.sedaily.com/markets/2026/04/21/korea-to-allow-single-stock-leveraged-etfs-on-samsung-sk ；抓取 2026-06-04T13:40+08:00；原意源 KRX/Korea FSC。
- 「CoreWeave DDTL 5.0」：query `CoreWeave AI data center debt financing May 2026` → CoreWeave IR / Morningstar（資料日 2026-05-18，$3.1B Ba2/BB+）；URL https://investors.coreweave.com/news/news-details/2026/CoreWeave-Closes-3-1-Billion-Loan-Facility... ；抓取 2026-06-04T13:40+08:00；原意源 公司新聞稿/SEC。
- 「SpaceX IPO」：query `upcoming AI IPO ... SpaceX timing valuation June 2026 S-1` → CNBC / TechCrunch（S-1 申報 2026-05-20、6/12 目標、$1.75 兆）；URL https://techcrunch.com/2026/05/20/the-spacex-ipo-filing-ai-bets-starship-dreams-elon-musk/ ；抓取 2026-06-04T13:40+08:00；原意源 SEC EDGAR。

## 本次分數存檔
```json
{
  "date": "2026-06-04",
  "iso_week": "2026-W23",
  "weekday": "Thursday",
  "timezone": "Asia/Taipei",
  "valuation": 81,
  "breadth": 48,
  "speculation": 72,
  "retail": 62,
  "monetary": 65,
  "structural": 72,
  "total": 68,
  "tier": "高"
}
```

本報告為相對風險溫度計，非擇時訊號。
