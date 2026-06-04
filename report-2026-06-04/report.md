# 2026-06-04 市場泡沫風險評估報告
> 報告日期：2026-06-04；執行日：2026-06-04 Asia/Taipei；ISO 週次：2026-W23；前次基準：report-2026-06-01（3天前）

## §1 六維度風險條圖

| 維度 | 條圖 | 本次 | 前次 | Δ |
|---|---|---:|---:|---:|
| 估值溢價 | ▰▰▰▰▰▰▰▰▱▱ | 81 | 82 | −1 |
| 市場廣度 | ▰▰▰▰▱▱▱▱▱▱ | 46 | 45 | +1 |
| 投機行為 | ▰▰▰▰▰▰▰▱▱▱ | 71 | 70 | +1 |
| 散戶情緒 | ▰▰▰▰▰▰▱▱▱▱ | 64 | 66 | −2 |
| 貨幣與信貸環境 | ▰▰▰▰▰▰▱▱▱▱ | 65 | 64 | +1 |
| 結構性槓桿 | ▰▰▰▰▰▰▰▱▱▱ | 73 | 74 | −1 |
| **加權總分** | ▰▰▰▰▰▰▱▱▱▱ | **68【高】** | 68 | 0 |

本週無任一維度 |Δ| ≥ 10（⚠ 未觸發）；「全球槓桿擴散訊號」本週未觸發（◆ 未標示）。

## §2 歷史錨點相似度

| 錨點 | 相似度 | 條圖 | 標記 |
|---|---:|---|---|
| 1997 早期建設 | 25% | ▰▰▱▱▱▱▱▱▱▱ |  |
| 1998 LTCM 衝擊 | 22% | ▰▰▱▱▱▱▱▱▱▱ |  |
| 1999 晚期狂熱 | 82% | ▰▰▰▰▰▰▰▰▱▱ | ◀ 最貼近 |
| 2000/3 頂點 | 70% | ▰▰▰▰▰▰▰▱▱▱ |  |
| 2021/12 Meme 頂 | 68% | ▰▰▰▰▰▰▱▱▱▱ |  |

## §3 三角訊號

| 指標 | 本次數值 | vs 前次 |
|---|---|---|
| S&P 500 | 7,553.68（2026-06-03 收盤） | ▼ −0.6%（前次 7,599.96，06-01 收盤紀錄高點） |
| WTI 原油 | $95.68 /bbl（2026-06-04） | ▲ +5%（前次 ~$91，06-01；美伊地緣風險溢價） |
| 10Y Treasury | 4.49%（2026-06-03） | ▲ +2 bps（前次 4.47%，06-01） |

**三者狀態**：出現分歧（油價在重新定價）。股市自 06-01 紀錄高點小幅回落、仍貼近高位，原油受美伊地緣風險急彈、扭轉 5 月 −17% 的跌勢，10Y 殖利率受實質利率推升而微升。三者並非同步創高，故「同向偏高」的高風險配置本週未成立。

- 股市：S&P 500 7,553.68（06-03 收盤），較 06-01 紀錄高點 7,599.96 回落 ~0.6%，但仍處歷史高位附近，YTD 約 +9–10%。
- WTI 原油：$95.68/bbl（06-04），較 06-01 約 +5%；美伊和談不確定性帶來地緣風險溢價，連三日上行並突破 $95。
- 10Y 殖利率：4.49%（06-03），主要驅動為實質利率（DFII10）走升突破 2.0%，非通膨預期帶動。

**格局轉變**：前次（06-01）為「股強、油弱（5 月重挫）、債中立」；本次轉為「股微幅消化、油急彈重新定價、債因實質利率微升」——油市由空翻多是本週最大邊際變化。

**10Y 成因拆解（`ΔDGS10 ≈ ΔDFII10 + ΔT10YIE`，拆的是週變動、非水位）**：以前次基準日 2026-06-01 對齊。

- ΔDFII10 實質殖利率週變動：約 +4 bps（2.04% → 2.08%，突破 2.0%，為近一年首見），方向 ▲。（✓ SEARCH-VERIFIED，當前值 2.08%，06-03）
- ΔT10YIE 損益平衡通膨週變動：⛔ FETCH FAILED — T10YIE 序列本次經 FRED API（403）、直抓 macrotrends（403）、WebSearch（無當日數值）三管道均未取得當日有效觀測；依規定不以 `DGS10 − DFII10` 推算填入 Δ，故本項缺值，恆等式校驗無法完成。
- 判定：偏 real-rate-driven（依可取得的 ΔDFII10 +4 bps 主導、ΔDGS10 僅 +2 bps，實質利率升幅大於名目，隱含 breakeven 偏軟；惟 ΔT10YIE 未能獨立驗證，判定僅供參考）。

**扳機鏈：油 → 通膨預期 → Fed 受限 → refinancing 成本**：本週 WTI 急彈（+5%，美伊地緣溢價），具備啟動「油 → 通膨預期」的潛在條件；但本次 10Y 上行為實質利率主導、而非 breakeven 主導，顯示油價尚未明顯傳導至通膨預期端，扳機鏈尚未進入「Fed 受限」階段。Fed put 可得性：4 月 FOMC 4 票鷹派異議（1992 年 10 月以來最多）已壓縮寬鬆空間，下次 FOMC 為 6/16–17（執行日後），市場預期續按兵不動於 3.50–3.75%；實質利率與油價同升使 Fed 短期內難轉鴿。

**結論**：估值極端（CAPE 41.44）＋結構性槓桿偏高（保證金負債創 $1.30 兆新高、槓桿 ETF AUM > $170B、AI 基建債務擴張）＝崩跌「位能」偏高；但「點火」的融資收緊條件本週尚未擊發——HY OAS 仍 2.72%（近歷史最緊）、信用利差未走闊、股市僅小幅離高。三者呈分歧（油在重新定價）而非同步創高，故本段不加 ⚠。

## 六維度評分

### 1. 估值溢價：81 / 100（weight 22%）

Shiller CAPE 41.44（2026-06-01，GuruFocus；長期均值約 17、僅次於 2000 年峰值 44.2），S&P 500 forward P/E 約 28–29×，Mag 7 估值區間由 MSFT ~26× 至 TSLA ~400×；hyperscaler 2026 capex 指引合計 $725B（YoY +77%）且本季仍在上修（MSFT $190B、Alphabet 上修至 $180–190B、Meta 上修至 $125–145B），資本支出未見下修暫撐估值，但同時抬升「一旦下修則估值風險陡升」的脆弱性。AI 算力供需 reality check：本次未取得直接利用率／GPU 租賃／HBM 定價／交期等證據，依規定不主張「需求正在吸收產能」，結論下修為「capex / Nvidia 營收仍支撐，但未取得直接利用率證據」（相關利用率／定價項標 ✗ NOT DISCLOSED）。TP-upgrade phase signal：本期 14 日內未取得可驗證的重大 sell-side 目標價上修拆解（✗ NOT DISCLOSED）。CAPE 與前次（41.6）大致持平、疊加 06-03 小幅回落，分數自 82 微降至 81。

### 2. 市場廣度：46 / 100（weight 13%）

RSP（等權）YTD 約 +5.5%、SPY（市值權）YTD 約 −0.2%，等權跑贏約 5+ ppt（廣度改善訊號續存，PortfoliosLab / 247WallSt）；惟 S&P 500 前十大權重仍約 35.6%（高位）、前五大逾 25%，集中度未解除。等權持續領先支撐廣度評分維持中性偏低，分數自 45 微升至 46。

### 3. 投機行為：71 / 100（weight 18%）

SpaceX（SPCX）IPO 進度升級：最快 2026-06-12 於那斯達克掛牌、尋求募資至多 $75B、估值逾 $2 兆（CNBC / Bloomberg，2026 年 6 月初），規模為現代史上罕見，強化「mega-IPO 作為頂部訊號 + 流動性抽離」之晚期特徵；Cerebras（CBRS）首日 +68%、次日 −10%（05-14，較舊、屬背景）。主題狂熱續燒：S&P Kensho 量子指數至 5 月底 +69.3%、Rigetti TTM +5,700%、IonQ +712%、市值逾 $121 億。Microcap thematic moonshot：本週未確認到符合條件（單日 ≥100%、< $1B 市值、≥2 熱門主題堆疊、弱基本面）之具體標的（✗ NOT DISCLOSED）。Insider selling：14 日內未取得具 SEC EDGAR Form 4 申報日／成交日之 AI 領導股內部人賣壓叢集（✗ NOT DISCLOSED）。綜合 SpaceX IPO 升級與持續性主題froth，分數自 70 微升至 71。

### 4. 散戶情緒：64 / 100（weight 12%）

CNN Fear & Greed 自前次 60（貪婪）回落至約 54–57（中性偏貪婪，06-03，CNN / MacroMicro）；AAII（最新一期）看多 39.3%（前次 35.6%）、看空 36.6%（前次 41.9%）、中立 24.1%，看多連四週高於均值——散戶調查偏暖；FINRA 保證金負債 2026 年 4 月 $1.30 兆創歷史新高（MoM +6.8%、YoY +53.3%、佔 GDP 4.09% 創高，Advisor Perspectives / YCharts）。F&G 降溫與 AAII 升溫互相抵銷、保證金負債創高提供槓桿確認，淨評估略降，分數自 66 降至 64。（機構情緒另列，不在此評分。）

### 5. 貨幣與信貸環境：65 / 100（weight 20%）

聯邦基金利率 3.50–3.75%（連續按兵不動，下次 FOMC 6/16–17 預期續持平；4 月 8–4 票、4 票異議為 1992 年來最多）；ICE BofA HY OAS 約 2.72%（06-01，近歷史最緊、遠低於中位 4.53%）、IG OAS 約 77 bps（05-12，post-GFC 底部十分位），信用市場定價近乎完美。10Y 名目 4.49%（+2 bps）、實質 DFII10 2.08%（+4 bps，突破 2.0%）為輕微緊縮訊號；T10YIE 直抓失敗（見 §3）。Fed 資產約 $6.7 兆（QT 已於 2025-12 結束）。WTI 急彈帶來邊際通膨上行風險。三角交叉訊號：本週為「股微落、油升、債微升」之分歧格局，非同步創高（詳 §3）；實質利率主導的 10Y 上行對估值與再融資成本構成壓力，但信用利差未走闊，傳導尚屬早期。實質利率走升 + 油價反彈，分數自 64 微升至 65。

### 6. 結構性槓桿：73 / 100（weight 15%）

美國槓桿 ETF 總 AUM 已逾 $170B（etf.com）：TQQQ $31.3B、SOXL $17.3B（YTD +261%）、NVDL／TSLL 等單股槓桿產品續膨脹；0DTE 約佔 S&P 500 期權 45–50%（背景值，本次無新 CBOE 數據）；VIX 約 15.8（06-03）顯示低波動自滿。全球擴散：南韓單股 2x 槓桿 ETF（Samsung、SK hynix）已於 5 月下旬上市（屬前次區間、非本週新事件），本週未見 2+ 個非美市場同週新核准——**本週擴散訊號未觸發**（◆ 未標示）。AI 基建債務／vendor-financing：CoreWeave 完成 $8.5B 投資級評等（Moody’s A3 / DBRS A(low)）之 GPU 抵押 DDTL 4.0 融資（SOFR+2.25% 浮動 / ~5.9% 固定、2032 到期、客戶合約背書）、Crusoe 自 Brookfield 取得 $750M 信用額度（Stargate 德州園區）——條款雖以客戶合約背書、評等良好（屬「匹配合約、條款穩定」一端），但規模龐大且 CoreWeave 淨損倍增至約 $3.15 億、對利率與算力需求放緩敏感，使 AI capex 交易的結構性槓桿維持偏高。前次的 ◆ 觸發係源自 BofA 現金 < 4%（5 月調查、無 6 月更新、屬陳舊）；依本提示嚴格定義 ◆ 僅限「全球槓桿擴散訊號」，本週未觸發，分數自 74 微降至 73（屬標示校正，非槓桿水位實質下降）。

## 綜合分數

| 維度 | 分數 | 權重 | 加權分 |
|---|---:|---:|---:|
| 估值溢價 | 81 | 22% | 17.82 |
| 市場廣度 | 46 | 13% | 5.98 |
| 投機行為 | 71 | 18% | 12.78 |
| 散戶情緒 | 64 | 12% | 7.68 |
| 貨幣與信貸環境 | 65 | 20% | 13.00 |
| 結構性槓桿 | 73 | 15% | 10.95 |
| **加權總分** | | **100%** | **68.21 → 68** |

**綜合評分：68 / 100　　風險等級：高**（等級序：低 / 溫和 / 警戒 / 高 / 極度狂熱）

## 歷史泡沫週期對比

| 參照點 | 相似度 | 一句話理由 |
|---|---:|---|
| 1997 早期建設 | 25% | AI 基建投資週期啟動、敘事成形，但估值與投機尚未達當前極端。 |
| 1998 LTCM 衝擊 | 22% | 缺乏當前的系統性去槓桿事件，信用利差近最緊而非走闊。 |
| 1999 晚期狂熱 | 82% | CAPE 41.4 逼近 2000 峰值、AI 主題狂熱、mega-IPO 管線（SpaceX 逾 $2 兆）、HY OAS 壓縮、機構超配——晚期但盈利仍撐。 |
| 2000/3 頂點 | 70% | 估值極端與集中度高度相似，惟廣度仍由等權改善、尚未見明確上行轉折。 |
| 2021/12 Meme 頂 | 68% | 保證金負債創高、0DTE 與槓桿 ETF（含單股 2x）普及、散戶 FOMO——惟利率為 3.5–3.75% 非零利率。 |

**解讀（2 句）：** 本週最貼近 1999 晚期狂熱——估值已達歷史頂部區間、投機與槓桿（含單股槓桿 ETF、AI 基建債務、record 保證金負債）廣泛擴散，但企業盈利與 capex 仍在上修、信用利差未走闊，屬「位能高、扳機未擊發」的泡沫後段而非破裂點。對照 2000/3 頂點（70%）的差異在於廣度仍由 RSP 等權改善、尚無明確的上行動能轉折，意味週期定位偏「最後一段上漲」而非已確認見頂。

## 機構情緒對照

本次無新機構調查數據。最近一期為 BofA Global Fund Manager Survey（2026 年 5 月，5/8–5/14 調查、200 位、$517B AUM）：現金 3.9%（自 4 月 4.3% 大降、跌破 4.0% 賣出訊號閾值）、淨超配股票 +50%（2001 年來單月最大跳升）、僅 4% 預期硬著陸——該期已於前次（06-01）報告反映，6 月調查通常於月中發布、截至執行日尚未釋出。JPMorgan 最新 S&P 500 目標價更新截至執行日未正式披露（✗ NOT DISCLOSED）。（AAII 僅作散戶對照，不列為機構數據。）

## 本次新增訊號

比較基準：vs 前次（3天前，report-2026-06-01）。

| 維度 | 前次 | 本次 | Δ | 觸發事件 / 理由 |
|---|---:|---:|---:|---|
| 估值溢價 | 82 | 81 | −1 | CAPE 41.44 ~持平；capex 仍上修但 06-03 小幅回落 |
| 市場廣度 | 45 | 46 | +1 | RSP +5.5% vs SPY −0.2% YTD，等權續領先 |
| 投機行為 | 70 | 71 | +1 | SpaceX IPO 升級：6/12 掛牌、募資至多 $75B、估值逾 $2 兆 |
| 散戶情緒 | 66 | 64 | −2 | CNN F&G 60→~55 降溫；AAII 看多升至 39.3%；保證金負債 $1.30 兆創高 |
| 貨幣與信貸環境 | 64 | 65 | +1 | 實質利率 DFII10 突破 2.0%；WTI 急彈 +5%；HY OAS 仍 2.72% |
| 結構性槓桿 | 74 | 73 | −1 | 本週擴散訊號未觸發（◆ 標示校正）；CoreWeave $8.5B、Crusoe $750M AI 基建債務 |
| **總分** | **68** | **68** | **0** | 高風險區持平 |

**全球槓桿擴散訊號：本週未觸發**（無 2+ 非美市場於同週新核准單股槓桿／反向 ETF；南韓 Samsung/SK hynix 2x 為 5 月下旬事件，屬背景趨勢而非本週新觸發）。

## 數據附錄

| 指標 | 數值 | 來源 / FRED ID | 日期 | 狀態 |
|---|---|---|---|---|
| S&P 500 收盤 | 7,553.68 | CNBC / TheStreet | 2026-06-03 | ✓ SEARCH-VERIFIED |
| S&P 500 前次收盤（紀錄高） | 7,599.96 | CNBC / Yahoo Finance | 2026-06-01 | ✓ SEARCH-VERIFIED |
| WTI 原油 | $95.68 /bbl | OilPrice / TradingEconomics | 2026-06-04 | ✓ SEARCH-VERIFIED |
| WTI 前次（估） | ~$91 /bbl | Fortune / CNBC（06-01 盤中急彈後回吐） | 2026-06-01 | ✓ SEARCH-VERIFIED |
| 10Y Treasury (DGS10) | 4.49% | YCharts / MacroMicro（FRED DGS10） | 2026-06-03 | ✓ SEARCH-VERIFIED |
| 10Y DGS10 前次 | 4.47% | FRED DGS10（搜尋摘要） | 2026-06-01 | ✓ SEARCH-VERIFIED |
| 10Y 實質利率 (DFII10) | 2.08% | TipsWatch / TradingEconomics（FRED DFII10） | 2026-06-03 | ✓ SEARCH-VERIFIED |
| 10Y DFII10 前次（估） | ~2.04% | 推估自 06-03 2.08%（−0.03 前一交易日） | 2026-06-01 | ✓ SEARCH-VERIFIED |
| 10Y breakeven (T10YIE) | — | FRED T10YIE / macrotrends / WebSearch | 2026-06-04 | ⛔ FETCH FAILED（API 403、直抓 403、搜尋無當日值；不以 DGS10−DFII10 推算） |
| ICE BofA HY OAS (BAMLH0A0HYM2) | 2.72% | GuruFocus（FRED BAMLH0A0HYM2） | 2026-06-01 | ✓ SEARCH-VERIFIED |
| ICE BofA IG OAS (BAMLC0A0CM) | ~77 bps | investmentgrade.com（FRED BAMLC0A0CM） | 2026-05-12 | ✓ SEARCH-VERIFIED |
| 聯邦基金利率 (DFEDTARU/L) | 3.50–3.75% | Fed FOMC / TradingEconomics | 2026-04-29 | ✓ SEARCH-VERIFIED |
| 下次 FOMC | 2026-06-16/17 | Federal Reserve | 行事曆 | ✓ SEARCH-VERIFIED |
| Fed 資產 (WALCL) | ~$6.7 兆 | AAF / Fed（FRED WALCL） | 2026-05-27 | ✓ SEARCH-VERIFIED |
| Shiller CAPE | 41.44 | GuruFocus / Shiller | 2026-06-01 | ✓ SEARCH-VERIFIED |
| S&P 500 forward P/E | ~28–29× | FactSet / 搜尋摘要 | 2026 年 5–6 月 | ✓ SEARCH-VERIFIED |
| Mag 7 P/E 區間 | MSFT ~26× ～ TSLA ~400× | Bloomberg / 搜尋摘要 | 2026 年 5–6 月 | ✓ SEARCH-VERIFIED |
| 2026 hyperscaler capex 合計 | $725B（YoY +77%） | Tom's Hardware / Yahoo | 2026 Q1 財報 | ✓ SEARCH-VERIFIED |
| MSFT / Alphabet / Meta capex 指引 | $190B / $180–190B↑ / $125–145B↑ | 各公司 Q1 2026 財報 | 2026 Q1 | ✓ SEARCH-VERIFIED |
| RSP YTD | +5.5% | PortfoliosLab / 247WallSt | 2026 YTD | ✓ SEARCH-VERIFIED |
| SPY YTD | −0.2% | PortfoliosLab | 2026 YTD | ✓ SEARCH-VERIFIED |
| S&P 500 前十大權重 | ~35.6% | S&P DJI（沿用前期快照） | 2026 年 5 月 | ✓ SEARCH-VERIFIED |
| CNN Fear & Greed | ~54–57（中性偏貪婪） | CNN / MacroMicro / feargreedmeter | 2026-06-03 | ✓ SEARCH-VERIFIED |
| AAII 看多 / 看空 / 中立 | 39.3% / 36.6% / 24.1% | AAII | 最新一期（2026 年 6 月初） | ✓ SEARCH-VERIFIED |
| FINRA 保證金負債 | $1.30 兆（MoM +6.8%、YoY +53.3%） | Advisor Perspectives / YCharts | 2026-04 | ✓ SEARCH-VERIFIED |
| 保證金負債 / GDP | 4.09%（創高） | GuruFocus | 2026-04 | ✓ SEARCH-VERIFIED |
| 槓桿 ETF 總 AUM | > $170B | etf.com | 2026 年 5–6 月 | ✓ SEARCH-VERIFIED |
| TQQQ / SOXL AUM | $31.3B / $17.3B | etf.com / Yahoo | 2026 年 5–6 月 | ✓ SEARCH-VERIFIED |
| 0DTE 佔 SPX 期權 | ~45–50%（背景） | CBOE（沿用前期） | 2026 年 5 月 | ✓ SEARCH-VERIFIED |
| VIX | ~15.8 | FRED VIXCLS / Yahoo | 2026-06-03 | ✓ SEARCH-VERIFIED |
| Cboe SKEW | — | Cboe | 2026-06 | ✗ NOT DISCLOSED（本次未取得當期數值） |
| SpaceX IPO | 6/12 掛牌、募資至多 $75B、估值逾 $2 兆 | CNBC / Bloomberg | 2026 年 6 月初 | ✓ SEARCH-VERIFIED |
| CoreWeave 融資 | $8.5B DDTL（A3 / A(low)、SOFR+2.25%、2032 到期） | CoreWeave IR / Morningstar | 2026 年（近月） | ✓ SEARCH-VERIFIED |
| Crusoe 融資 | $750M Brookfield 信用額度（Stargate） | DCD / NBC | 2026 年（近月） | ✓ SEARCH-VERIFIED |
| 南韓單股 2x 槓桿 ETF | Samsung / SK hynix，2x，5 月下旬上市 | Korea Herald / Bloomberg | 2026-05（背景） | ✓ SEARCH-VERIFIED |
| 量子主題（Kensho 指數） | +69.3%（至 5 月底）；Rigetti TTM +5,700%；IonQ +712% | US News / 搜尋摘要 | 2026 年 5–6 月 | ✓ SEARCH-VERIFIED |
| BofA FMS（最近期） | 現金 3.9%、淨超配股票 +50% | BofA Global Research | 2026-05 調查 | ✓ SEARCH-VERIFIED |
| 微型股 moonshot（本週具體標的） | — | Finviz / Benzinga / StockTwits | 2026-06 第 1 週 | ✗ NOT DISCLOSED |
| AI 領導股 insider Form 4 叢集（14 日內） | — | SEC EDGAR | 2026-06 | ✗ NOT DISCLOSED |
| TP-upgrade 拆解（14 日內） | — | sell-side / 搜尋 | 2026-06 | ✗ NOT DISCLOSED |
| PBoC 流動性英文摘要 | — | PBoC / NBS | 2026-06 | ✗ NOT DISCLOSED |

附註：FRED CSV（fredgraph.csv）與多個直抓來源（macrotrends 等）在本執行環境回傳 HTTP 403（datacenter IP 遭 WAF 阻擋），故 FRED 系列改以 WebSearch 取得當前可用值並標示 ✓ SEARCH-VERIFIED；僅 T10YIE 當日值三管道皆未取得，標 ⛔ FETCH FAILED。

## 本次分數存檔

```json
{
  "date": "2026-06-04",
  "iso_week": "2026-W23",
  "weekday": "Thursday",
  "timezone": "Asia/Taipei",
  "valuation": 81,
  "breadth": 46,
  "speculation": 71,
  "retail": 64,
  "monetary": 65,
  "structural": 73,
  "total": 68,
  "tier": "高"
}
```

本報告為相對風險溫度計，非擇時訊號。
