# 2026-06-04 市場泡沫風險評估報告
> 報告日期：2026-06-04；執行日：2026-06-04 Asia/Taipei；ISO 週次：2026-W23；前次基準：report-2026-06-01（3天前）

## §1 六維度風險條圖

| 維度 | 條圖 | 本次 | 前次 | Δ |
|---|---|---:|---:|---:|
| 估值溢價 | ▰▰▰▰▰▰▰▰▱▱ | 81 | 82 | −1 |
| 市場廣度 | ▰▰▰▰▱▱▱▱▱▱ | 45 | 45 | 0 |
| 投機行為 | ▰▰▰▰▰▰▰▱▱▱ | 71 | 70 | +1 |
| 散戶情緒 | ▰▰▰▰▰▰▱▱▱▱ | 63 | 66 | −3 |
| 貨幣與信貸環境 | ▰▰▰▰▰▰▱▱▱▱ | 65 | 64 | +1 |
| 結構性槓桿 | ▰▰▰▰▰▰▰▱▱▱ | 73 | 74 | −1 |
| **加權總分** | ▰▰▰▰▰▰▱▱▱▱ | **68【高】** | 68 | 0 |

（權重 22/13/18/12/20/15；|Δ|≥10 才標 ⚠，本次無任一維度達標。「全球槓桿擴散訊號」本週未觸發，結構性槓桿不加 ◆。）

## §2 歷史錨點相似度

| 錨點 | 相似度 | 條圖 | 標記 |
|---|---:|---|---|
| 1997 早期建設 | 25% | ▰▰▱▱▱▱▱▱▱▱ |  |
| 1998 LTCM 衝擊 | 22% | ▰▰▱▱▱▱▱▱▱▱ |  |
| 1999 晚期狂熱 | 60% | ▰▰▰▰▰▰▱▱▱▱ | ◀ 最貼近 |
| 2000/3 頂點 | 42% | ▰▰▰▰▱▱▱▱▱▱ |  |
| 2021/12 Meme 頂 | 48% | ▰▰▰▰▱▱▱▱▱▱ |  |

## §3 三角訊號

| 指標 | 本次數值 | vs 前次 |
|---|---|---|
| S&P 500 | 7,553.68（2026-06-03 收盤） | ▼ −0.3%（前次 7,580.06） |
| WTI 原油 | $95.75 /bbl（2026-06-03） | ▲ +9.8%（前次 $87.2） |
| 10Y Treasury | 4.48%（2026-06-04） | ▲ +3 bps（前次 4.45%） |

**三者狀態**：出現分歧（原油在重新定價）。股市自 6/02 盤中歷史高點（>7,609）小幅回落、9 連漲中止，油價與殖利率同步走高。

- 股市：S&P 500 收 7,553.68，較前次 −0.3%，仍高懸於 50 日均線（~7,100）之上、RSI ~75 過熱區；6/02 才創 7,609 新高後拉回。
- WTI 原油：$95.75/bbl，較前次急彈 +9.8%，受美伊和談不確定性與中東地緣風險、連續第六週原油庫存去化推升。
- 10Y 殖利率：4.48%，較前次 +3 bps，主要受強於預期的民間就業（5 月 +12.2 萬）與油價推升的通膨溢價驅動。

**格局轉變**：前次（6/01）為「股強、油弱（5 月 −17%）、債中立」；本次轉為「股微幅回落、油價急彈、殖利率小幅上行」——油價由空翻多，成為通膨／殖利率鏈條的新邊際變數。

**10Y 成因拆解（`ΔDGS10 ≈ ΔDFII10 + ΔT10YIE`，拆的是週變動、非水位）**：本執行環境直連 FRED／Treasury 均遭 WAF 403，`scripts/fetch_macro.py` 全序列 `fetch_failed`、`decomposition.status = unavailable_no_daily_history`，故 **本週 Δ 分解不可用——無日序資料**，不臆造 Δ。僅列當前 spot 水位供參：

- ΔDFII10 實質殖利率週變動：不可用（spot 2.08%，2026-06-03）
- ΔT10YIE 損益平衡通膨週變動：不可用（spot 約 2.40%，以 DGS10−DFII10 `derived`；FRED 直接序列最近可見 2.5%＠2026-05-08）
- 判定：分解不可用（無日序，real/breakeven 主導歸因本週無法判定）

**扳機鏈：油 → 通膨預期 → Fed 受限 → refinancing 成本**：WTI 單週 +9.8% 是本週最顯著的鏈條啟動跡象；若油價續揚並滲入損益平衡通膨，將壓縮 4 月 29 日 FOMC（3.50–3.75%、4 票鷹派異議為 1992 年以來最多）的降息空間，降低「Fed put」可得性。惟目前信用利差仍極緊（HY OAS 2.72%、IG OAS 0.76%），refinancing 端尚未出現壓力，鏈條僅在「通膨預期」前段醞釀。

**結論**：估值（CAPE 近歷史次高）+ 槓桿（margin debt 創高、0DTE ~60%）構成高位勢能；融資面（信用利差極緊）尚未轉緊，計時扳機未擊發。三者未同向偏高（股微跌、油債上行），故不加 ⚠；但油價急彈為本週新增的通膨—利率觀察點，須留意其是否由地緣短脈衝轉為持續性重定價。

## 六維度評分

### 1. 估值溢價：81 / 100（weight 22%）

**一句話評分依據：** Shiller CAPE 約 41.4–42.5（GuruFocus 41.44＠6/01、multpl 42.53），仍逾長期均值（~17.3）2.4 倍、為 1999 年峰值 44.19 的約 95%；S&P 500 trailing P/E ~27.4–28.5、forward ~21.8；Mag 7 仍全面溢價（NVDA forward ~47、MSFT ~24.5、GOOGL ~17.4）——估值極致但本週未再升溫，S&P 自高點小幅回落，分數自 82 微降至 81。

- **AI 基本面現實檢查（capex）：** 仍在「上調」而非下修——Meta 將 2026 capex 由 $1,150–1,350 億上修至 $1,250–1,450 億，四大 hyperscaler 合計約 $7,000–7,250 億（YoY +約 77%）。capex 未見轉折，估值風險尚未因 capex 削減而跳升。
- **AI compute 供需檢查：** Google I/O（5/19）揭露月處理 token 達 3.2 quadrillion（YoY 約 7 倍）、OpenAI APIs ~150 億 token/分鐘，需求側強勁；TrendForce 顯示 HBM/DRAM 供給偏緊、HBM4 報價 mid-2026 約 +30%——記憶體偏緊與 token 爆量指向「產能仍被利用率吸收」，未見 overcapacity 訊號。惟未取得 GPU 租賃利用率直接證據（標 ✗ NOT DISCLOSED），不據此斷言供需完全平衡。
- **TP-upgrade 階段訊號：** Morgan Stanley 將 NVDA 目標調至 $288（約 22× CY2027 EPS $13.08），論述核心為「$8,840 億資料中心營收、領先市場共識約 $1,000 億」——偏 **EPS／營收驅動** 而非單純倍數擴張；Marvell 6/02 單日 +32.5%（Huang 稱其為「下一家兆元公司」）屬敘事性大型股動能。本期主流上調未呈現「跨 2+ 旗艦同步倍數重定價」的晚週期型態，故不額外加旗。

### 2. 市場廣度：45 / 100（weight 13%）

**一句話評分依據：** RSP（等權）YTD 領先 SPY 約 5 個百分點（廣度方向仍正面），但前十大權重仍約 35.6–37%、僅 52.2% 成分股站上 50 日均線（短線參與度偏低）、指數 RSI ~75 過熱，創高主要仍由 AI／半導體主導，廣度未全面啟動，維持 45。

- RSP vs SPY：RSP YTD 總報酬約 +9.7%，領先 SPY 約 5 ppt（mega-cap 主導鬆動）。
- 前十大集中度：約 35.6%（4 月 S&P DJI）至逾 37%（部分來源），仍處歷史高位。
- 漲跌與新高新低：6/02 指數 7,609.78 遠高於 200 日均線（~6,842），惟新高家數「中等」、短長期均線參與度均「低於平均」，內部廣度落後於指數價格。

### 3. 投機行為：71 / 100（weight 18%）

**一句話評分依據：** SpaceX 巨型 IPO 由 S-1 具體化為「最快 6/12 於 Nasdaq 掛牌（SPCX）、擬募資至多 $750 億、估值逾 $2 兆」，為史上規模空前、典型晚週期訊號；惟本週未出現合格 microcap moonshot（沖抵部分過熱），分數自 70 微升至 71。

- +AI 改名／SPAC：本週未發現合格「+AI 改名」個案；IPO 管線仍約 92% 為 AI／AI-adjacent（史上最集中）。
- IPO 熱度：SpaceX 擬募 $750 億（CNBC「Mega-IPO 恐為市場頂部訊號」5/22）；SpaceX、OpenAI 仍未獲利即籌備天量上市。
- Microcap thematic moonshots：依篩選條件（單日 ≥100%、市值 <$1B、堆疊 2+ 熱門主題、弱基本面）掃描本週最大漲幅股，**本週無合格標的**（6 月領漲如 VIDA +53%、LEGN +42% 均未達單日 +100% 門檻；Marvell +32.5% 為大型股，不符 microcap）。
- 內部人賣股：過去 14 日未取得具 Form 4 申報日／交易日／EDGAR URL 的內部人群聚賣壓明細，標 ✗ NOT DISCLOSED，不引用陳舊名單。
- OpenAI／Anthropic 營收軌跡（集中度風險）：OpenAI 約 $250 億年化（2 月）／月營收約 $20 億；Anthropic 約 $300 億年化（4 月，自 2025 年底 $90 億陡升）——營收高速成長同時亦凸顯敘事集中。
- 即將上市巨型 IPO（流動性抽水）：SpaceX 6/12、OpenAI／Anthropic 2026 年內，合計潛在抽水可觀。

### 4. 散戶情緒：63 / 100（weight 12%）

**一句話評分依據：** CNN Fear & Greed 由前次 60（貪婪）回落至 54（中性，6/03），疊加 margin debt 創高但 AAII 看空仍高於看多，散戶並非一面倒頂部式樂觀，分數自 66 降至 63。

- CNN Fear & Greed：54（中性，2026-06-03；6/02 盤中曾 59）。
- Margin Debt：FINRA 4 月 $1.30 兆創歷史新高（MoM +6.8%、YoY +53.3%）；margin debt / 美股總市值約 2.0–2.1%（以 ~$63 兆市值估算的概略比值，避免僅看絕對水位）。5 月數據尚未發布。
- AAII（最新可得 2026-05-28 期，本週四新印未見明確更新）：看多 35.6%（低於長期均值）、中立 22.6%、看空 41.9%。
- 社群情緒代理：WSB／Reddit 熱議仍集中 NVDA、MRVL、ASTS 等 AI 敘事股；屬科技成長題材而非廣泛迷因狂熱。
- 註：機構情緒另列於下方，不在本維度計分。

### 5. 貨幣與信貸環境：65 / 100（weight 20%）

**一句話評分依據：** 信用利差仍極緊（HY OAS 2.72%、IG OAS 0.76%）對風險定價近乎完美，惟 WTI 急彈 +9.8% 與 10Y 微升至 4.48% 使「油→通膨→Fed 受限」鏈條邊際升溫，分數自 64 微升至 65。

- Fed funds：3.50–3.75%（4/29 FOMC 連 3 次按兵不動，8–4 票，4 票異議為 1992 年以來最多；下次 6/17）。
- HY OAS：2.72%（遠低於長期均值 ~3.94%／中位 4.53%，逼近歷史低點）。
- IG OAS：0.76%（76 bps，5 月；極緊）。
- 10Y 名目殖利率週變動拆解：本週 Δ 分解不可用——無日序資料（FRED/Treasury 直連 403、腳本 fetch_failed）。spot：DGS10 4.48%、DFII10 2.08%、breakeven（derived）約 2.40%。名目 10Y 相對前次 spot 約 +3 bps，但 real/breakeven Δ 歸因無法判定，不臆造。
- Fed 資產負債表：WALCL 約 $6.7 兆（5/27），QT 持續。
- 全球流動性交叉檢查：ECB 資產（至 5/22）大致持平、BOJ 持續收縮、Fed QT——整體偏中性偏緊；PBoC／NBS 本期未取得英文當期彙整（標 ✗ NOT DISCLOSED，僅此子項）。
- 三角交叉訊號：見 §3。WTI 上行配合殖利率上行，支持「油→通膨預期」前段；但信用利差未走闊、refinancing 壓力未現，扳機未擊發。

### 6. 結構性槓桿：73 / 100（weight 15%）

**一句話評分依據：** 0DTE 佔 SPX 量已達約 60–63%（Cboe，2 月 63%）、margin debt 創高、槓桿 ETF 總規模逾 $1,700 億且加速、SKEW 136.86 顯示尾部避險升溫，惟「全球槓桿擴散訊號」本週未觸發（非 2+ 非美市場同週核准），分數自 74 微降至 73、不加 ◆。

- US 槓桿 ETF AUM：TQQQ $313 億、SOXL $173 億、TSLL $65 億；槓桿 ETF 整體逾 $1,700 億並持續膨脹。
- US 單一個股槓桿 ETF 核准／上市（近 30 日）：GraniteShares autocallable PLTR（PLA）、HOOD（AHD）5/19 上市；Direxion 5 月底推 Gold/Silver/BTC/ETH 2x（UGLD/USLV/BTCU/EVMU）——產品擴張活躍。
- 全球槓桿產品擴散：南韓 5/22 上市 Samsung、SK hynix 單一個股 2x 槓桿／反向 ETF（6/29 將推個股週選擇權）；CSOP SK hynix 2x ETF（$53.8 億）5/8 超越 TSLL 成全球最大單一個股槓桿 ETF。台灣／日本本期無新核准披露。**僅南韓單一市場、非 2+ 市場同週，故「全球槓桿擴散訊號」本週未觸發。**
- 0DTE：約佔 SPX 量 59–63%（2 月 63%；2020 年僅約 5%），短期博弈文化深化、負凸性放大風險。
- 期權總量（OCC，5 月）：股票期權 8.031 億口（YoY +25.5%）、指數期權 1.226 億口（+32.8%）、ETF 期權 5.405 億口（+23.3%）——量能仍處高檔。
- 跨資產確認：VIX 15.77（6/02，低／自滿）、期限結構穩定 contango；Cboe SKEW 136.86（6/03，尾部避險偏高）；股債相關性 2026 年轉正（Oxford Economics），削弱債券避險效能、邊際提高組合脆弱度。
- Margin debt／市值比交叉確認：4 月 $1.30 兆、比值約 2.0–2.1%（僅作確認，不重複計分）。
- AI 基建債務／vendor-financing：過去 30 日未見「新」大型 facility 披露（標 ✗ NOT DISCLOSED 之週度事件訊號）；背景列示——CoreWeave $85 億 DDTL（3/31，Moody's A3、Meta 合約擔保，近 12 月累計約 $280 億債股承諾）、Oracle/xAI/Meta/CoreWeave 透過 SPV 將約 $1,200 億 AI 債務移出表外。目前條款未見惡化、抵押未見減損，僅作再融資敏感度背景，不加計分。

## 綜合分數

| 維度 | 分數 | 權重 | 加權分 |
|---|---:|---:|---:|
| 估值溢價 | 81 | 22% | 17.82 |
| 市場廣度 | 45 | 13% | 5.85 |
| 投機行為 | 71 | 18% | 12.78 |
| 散戶情緒 | 63 | 12% | 7.56 |
| 貨幣與信貸環境 | 65 | 20% | 13.00 |
| 結構性槓桿 | 73 | 15% | 10.95 |
| **合計** | | **100%** | **67.96 → 68** |

**綜合評分：68 / 100　　風險等級：高**（區間：低 0–39｜溫和 40–59｜警戒 60–69｜高 70–79… 本框架沿用既有分級，68 落於「高」風險帶，與前次同級。）

## 歷史泡沫週期對比

- **1997 早期建設（25%）：** 當前 AI 資本支出狂潮確有「基礎建設早期」色彩，但估值（CAPE ~42）已遠超 1997 年水準，週期位置明顯更後段，相似度低。
- **1998 LTCM 衝擊（22%）：** 缺乏當前的系統性槓桿去化或對沖基金爆雷觸媒，信用利差極緊而非走闊，方向相反，相似度低。
- **1999 晚期狂熱（60%）：** 最貼近。CAPE ~42 為 1999 峰值 94–95%、AI 敘事接棒網際網路、IPO 高度集中（92% 為 AI、SpaceX 擬募 $750 億）、信用利差極緊、機構 5 月現金跌破 4% 賣訊——晚週期「最後一段上漲」特徵齊備。
- **2000/3 頂點（42%）：** 估值可比，但 2000 年 3 月已伴隨廣度急速惡化與升息末段；當前廣度仍邊際改善、Fed 處於按兵不動而非緊縮末端，尚未完全對齊頂點。
- **2021/12 Meme 頂（48%）：** 0DTE ~60%、margin debt 創高、槓桿 ETF 擴散具高度行為相似性；惟散戶情緒（F&G 54 中性、AAII 看空>看多）未達 2021 年底全面狂熱，且利率為 3.5–3.75% 而非零利率。

**詮釋（2 句）：** 本週最相似於 **1999 晚期狂熱**——估值與機構配置處於歷史性高位、AI／IPO 敘事狂熱，但廣度尚未崩壞、信用面尚未轉緊，顯示仍處「泡沫後期但計時扳機未擊發」階段。結構性槓桿以週期調整視角衡量（1999/2000 以 margin debt 與指數期權投機為代理、2021 以 0DTE 與槓桿 ETF 為代理）皆指向高位，意味一旦 AI 盈利預期或油價—利率鏈條轉向，去槓桿的反身性下行空間可觀。

## 機構情緒對照

本次無新機構調查數據。（BofA Global FMS 5 月期已於前次 6/01 報告納入，6 月期預計約 6 月中發布；JPM 最新機構調查與年底目標價於截止前未見更新。）背景參照：5 月 FMS 現金配置 3.9%（跌破 4.0% 賣訊）、股票淨超配 +50% OW（2001 年以來最大單月跳升）、僅 4% 預期硬著陸——逆向賣訊仍懸而未解，須待 6 月期確認是否延續。AAII 僅作散戶對照，不視為機構數據。

## 本次新增訊號

比較基準：vs 前次（3天前，report-2026-06-01）。

| 維度 | 前次 | 本次 | Δ | 觸發事件 |
|---|---:|---:|---:|---|
| 估值溢價 | 82 | 81 | −1 | S&P 自 6/02 新高回落、9 連漲中止；CAPE 持平於高位、capex 仍上修 |
| 市場廣度 | 45 | 45 | 0 | RSP 仍領先 SPY ~5 ppt，惟 RSI ~75、參與度偏低 |
| 投機行為 | 70 | 71 | +1 | SpaceX 巨型 IPO 具體化（6/12、募資至多 $750 億、估值 >$2 兆）；本週無合格 microcap moonshot |
| 散戶情緒 | 66 | 63 | −3 | CNN F&G 60→54（貪婪轉中性） |
| 貨幣與信貸環境 | 64 | 65 | +1 | WTI +9.8%、10Y 微升至 4.48%，油—通膨鏈邊際升溫；HY/IG OAS 仍極緊 |
| 結構性槓桿 | 74 | 73 | −1 | 0DTE ~60%、SKEW 136.86、OCC 量創高；南韓單一市場槓桿擴散，**本週擴散訊號未觸發** |
| **總分** | **68** | **68** | **0** | 維持「高」風險帶；3 日間隔變動皆 <±10 |

**本次重點：**
1. **SpaceX 巨型 IPO 由申報轉為臨門**：最快 6/12 於 Nasdaq（SPCX）掛牌、擬募資至多 $750 億、估值逾 $2 兆——史上規模空前，典型晚週期頂部訊號（CNBC 5/22「Mega-IPO 恐示頂」）。
2. **油價由空翻多**：WTI 5 月 −17% 後本週急彈 +9.8% 至約 $95.75，啟動 §3「油→通膨預期→Fed 受限」鏈條前段。
3. **散戶情緒降溫**：CNN F&G 自貪婪（60）回落至中性（54）。
4. **槓桿結構維持高位**：0DTE ~60–63%、margin debt 4 月創 $1.30 兆、槓桿 ETF 逾 $1,700 億、SKEW 136.86。
5. **全球槓桿擴散**：南韓 5/22 上市三星／SK 海力士單一個股 2x／反向 ETF，惟為單一市場，**「全球槓桿擴散訊號」本週未觸發**（需 2+ 非美市場同週核准）。

## 數據附錄

### 來源涵蓋表（Coverage table，對應 `# Data sources` 每一 bullet，共 38 列）

| 維度 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|
| 估值-S&P 500 P/E 與 Shiller CAPE | multpl / GuruFocus [SEARCH] | ✓ SEARCH-VERIFIED |
| 估值-Mag 7 加權 P/E 與 AI 龍頭 P/S | 各家估值彙整 | ✓ SEARCH-VERIFIED |
| 估值-分析師 TP 上調拆解（best-effort） | Bloomberg/TheStreet/Benzinga [SEARCH] | ✓ SEARCH-VERIFIED |
| 廣度-RSP vs SPY YTD | etfcentral / Bloomberg | ✓ SEARCH-VERIFIED |
| 廣度-前十大集中度 | S&P DJI / slickcharts | ✓ SEARCH-VERIFIED |
| 廣度-漲跌家數／新高新低 | StreetStats / MarketInOut | ✓ SEARCH-VERIFIED |
| 散戶-CNN Fear & Greed | CNN / feargreedmeter [SEARCH] | ✓ SEARCH-VERIFIED |
| 散戶-Margin Debt 及市值比 | FINRA / Advisor Perspectives | ✓ SEARCH-VERIFIED |
| 散戶-AAII | AAII [SEARCH] | ✓ SEARCH-VERIFIED |
| 散戶-社群情緒（Reddit/X） | WSB trackers / AltIndex | ✓ SEARCH-VERIFIED |
| 機構-BofA FMS 與 JPM survey | BofA / Axios / Trustnet | ✓ SEARCH-VERIFIED |
| 貨幣-Fed funds DFEDTARU/L | FRED 腳本失敗→WebSearch | ✓ SEARCH-VERIFIED |
| 貨幣-HY OAS BAMLH0A0HYM2 | FRED 腳本失敗→GuruFocus | ✓ SEARCH-VERIFIED |
| 貨幣-IG OAS BAMLC0A0CM | FRED 腳本失敗→TradingEconomics | ✓ SEARCH-VERIFIED |
| 貨幣-10Y DGS10 | FRED 腳本失敗→TradingEconomics | ✓ SEARCH-VERIFIED |
| 貨幣-10Y real DFII10 | FRED 腳本失敗→TradingEconomics | ✓ SEARCH-VERIFIED |
| 貨幣-10Y breakeven T10YIE | FRED 腳本失敗→derived（DGS10−DFII10） | ✓ SEARCH-VERIFIED |
| 貨幣-WTI DCOILWTICO | FRED 腳本失敗→TradingEconomics/CNBC | ✓ SEARCH-VERIFIED |
| 貨幣-Fed 資產負債表 WALCL | FRED 腳本失敗→AAF/Macrotrends | ✓ SEARCH-VERIFIED |
| 貨幣-全球央行流動性（ECB/BOJ/PBoC） | FRED ECBASSETSW / 一般搜尋（PBoC 未取得） | ✓ SEARCH-VERIFIED |
| AI-Hyperscaler capex guidance | 財報 / CNBC / Tom's Hardware | ✓ SEARCH-VERIFIED |
| AI-token 量成長（best-effort） | Google I/O 2026 / OpenAI | ✓ SEARCH-VERIFIED |
| AI-OpenAI/Anthropic 營收（best-effort） | Sacra / SaaStr / RootData | ✓ SEARCH-VERIFIED |
| AI-hyperscaler 客戶集中度（best-effort） | 財報電話會（本期無量化披露） | ✗ NOT DISCLOSED |
| AI-compute 供需/overcapacity（best-effort）[SEARCH] | TrendForce HBM/DRAM + token 量 | ✓ SEARCH-VERIFIED |
| 投機-+AI 改名/SPAC/IPO 暴增 | 一般搜尋 / Renaissance | ✓ SEARCH-VERIFIED |
| 投機-IPO 熱度 | CNBC / Bloomberg / Yahoo | ✓ SEARCH-VERIFIED |
| 投機-Microcap moonshots [SEARCH] | StockTitan / Finviz（本週無合格標的） | ✓ SEARCH-VERIFIED |
| 投機-即將上市 AI IPO | CNBC / Bloomberg / Built In | ✓ SEARCH-VERIFIED |
| 投機-內部人賣股 Form 4 [EDGAR] | SEC EDGAR（14 日內無明細） | ✗ NOT DISCLOSED |
| 結構-US 槓桿 ETF AUM [SEARCH] | etf.com / Yahoo Finance | ✓ SEARCH-VERIFIED |
| 結構-US 單一個股槓桿 ETF 核准/上市 | GlobeNewswire / ETF Express | ✓ SEARCH-VERIFIED |
| 結構-全球槓桿產品核准（KRX/TWSE/JPX/ESMA） | Seoul Economic / Korea Herald | ✓ SEARCH-VERIFIED |
| 結構-0DTE 期權量 | Cboe Insights | ✓ SEARCH-VERIFIED |
| 結構-期權總量 OCC | OCC 月報（5 月） | ✓ SEARCH-VERIFIED |
| 結構-VIX 期限結構/SKEW/股債相關 | Cboe / Macrotrends / Oxford Economics | ✓ SEARCH-VERIFIED |
| 結構-Margin debt/市值比 交叉確認 | FINRA / dshort | ✓ SEARCH-VERIFIED |
| 結構-AI 基建債務/vendor-financing（best-effort）[SEARCH] | CoreWeave IR / Bloomberg（30 日內無新案） | ✗ NOT DISCLOSED |

（38 列＝`# Data sources` 38 bullet；✗ NOT DISCLOSED 三項皆為 Fetch protocol best-effort／Form 4 明確允許項，無 required 源以 ✗ 掩蓋。）

### SEARCH-VERIFIED 追溯與原始數據

所有數值經 WebSearch 取得；本執行環境 Bash/Python 直連外網（含 FRED/Treasury/EIA/example.com）一律回 403，故 macro 序列改由 WebSearch 取 spot（無日序、Δ 分解不可用）。檢索 timestamp 均為 2026-06-04（Asia/Taipei）。

| 指標 | 數值 | 來源／URL | 發布／資料日期 | 狀態 |
|---|---|---|---|---|
| S&P 500 收盤 | 7,553.68（−0.74%） | CNBC https://www.cnbc.com/2026/06/03/stock-market-today-live-updates.html | 2026-06-03 | ✓ SEARCH-VERIFIED |
| S&P 500 盤中新高 | >7,609.78 | TheStreet stock-market-today | 2026-06-02 | ✓ SEARCH-VERIFIED |
| Shiller CAPE | 41.44（GuruFocus）／42.53（multpl） | gurufocus.com/economic_indicators/56 ; multpl.com/shiller-pe | 2026-06-01 / 當前 | ✓ SEARCH-VERIFIED |
| S&P 500 trailing P/E | 27.42（GuruFocus）／~28.5 | gurufocus.com/economic_indicators/57 | 2026-06-02 | ✓ SEARCH-VERIFIED |
| S&P 500 forward P/E | ~21.8 | macromicro / ISABELNET | 2026-05 | ✓ SEARCH-VERIFIED |
| Mag 7 P/E（NVDA fwd / MSFT fwd / GOOGL fwd） | ~47 / ~24.5 / ~17.4 | Motley Fool / Nasdaq | 2026-05 | ✓ SEARCH-VERIFIED |
| MS NVDA 目標價 | $288（~22× CY27 EPS $13.08） | Investing.com / TheStreet | 2026-05（近 14 日內） | ✓ SEARCH-VERIFIED |
| Marvell 單日漲幅 | +32.5% | CNBC 2026/06/02 | 2026-06-02 | ✓ SEARCH-VERIFIED |
| RSP YTD 總報酬 / 領先 SPY | +9.7% / ~+5 ppt | etfcentral / 247wallst | 2026 YTD | ✓ SEARCH-VERIFIED |
| 前十大集中度 | ~35.6%（4 月）至 >37% | S&P DJI / pionline | 2026-04~05 | ✓ SEARCH-VERIFIED |
| 成分站上 50DMA / RSI | 52.2% / 75.04 | StreetStats | 2026-06-02 | ✓ SEARCH-VERIFIED |
| CNN Fear & Greed | 54（中性；6/02 盤中 59） | CNN / feargreedmeter.com | 2026-06-03 | ✓ SEARCH-VERIFIED |
| FINRA margin debt | $1.30 兆（MoM +6.8%、YoY +53.3%） | Advisor Perspectives dshort | 2026-04（5/20 發布） | ✓ SEARCH-VERIFIED |
| margin debt / 市值比 | ~2.0–2.1%（概估） | 自算（margin/~$63T 市值） | 2026-04 | ✓ SEARCH-VERIFIED |
| AAII（多/中/空） | 35.6% / 22.6% / 41.9% | aaii.com/sentimentsurvey | 2026-05-28（本週新印未明確更新） | ✓ SEARCH-VERIFIED |
| WSB 熱門股 | NVDA, MRVL, ASTS | AltIndex / tradestie | 2026-06-02~03 | ✓ SEARCH-VERIFIED |
| BofA FMS 現金/股票超配（5 月期） | 3.9% / +50% OW | Axios / Trustnet | 2026-05（5/20） | ✓ SEARCH-VERIFIED |
| Fed funds 目標區間 | 3.50–3.75%（8–4 票） | Fed FOMC / fedprimerate | 2026-04-29 | ✓ SEARCH-VERIFIED |
| HY OAS（BAMLH0A0HYM2） | 2.72% | GuruFocus 5735 | 2026-06（5 月值） | ✓ SEARCH-VERIFIED |
| IG OAS（BAMLC0A0CM） | 0.76%（76 bps） | TradingEconomics | 2026-05 | ✓ SEARCH-VERIFIED |
| 10Y DGS10 | 4.48% | TradingEconomics / CNBC US10Y | 2026-06-04 | ✓ SEARCH-VERIFIED |
| 10Y real DFII10 | 2.08% | TradingEconomics 10Y TIPS | 2026-06-03 | ✓ SEARCH-VERIFIED |
| 10Y breakeven T10YIE | ~2.40%（derived）；FRED 直接最近 2.5%＠5/08 | 自算 DGS10−DFII10 / FRED T10YIE | 2026-06-03 / 2026-05-08 | ✓ SEARCH-VERIFIED |
| WTI 原油 | ~$95.75 /bbl | TradingEconomics / CNBC @CL.1 | 2026-06-03 | ✓ SEARCH-VERIFIED |
| Fed 資產負債表 WALCL | ~$6.7 兆 | AAF / Macrotrends | 2026-05-27 | ✓ SEARCH-VERIFIED |
| ECB 資產 / BOJ | 大致持平（至 5/22）/ 持續收縮 | FRED ECBASSETSW / 一般搜尋 | 2026-05-22 | ✓ SEARCH-VERIFIED |
| PBoC 當期英文彙整 | 未取得 | — | — | ✗ NOT DISCLOSED（僅此子項） |
| Hyperscaler 2026 capex 合計 | ~$7,000–7,250 億（YoY +~77%） | Tom's Hardware / Statista | 2026-Q1 財報季 | ✓ SEARCH-VERIFIED |
| Meta capex 上修 | $1,150–1,350 億 → $1,250–1,450 億 | CreditSights / 財報 | 2026-Q1 | ✓ SEARCH-VERIFIED |
| Alphabet / Amazon 2026 capex | $1,800–1,900 億 / ~$2,000 億 | Tom's Hardware / CNBC | 2026-Q1 | ✓ SEARCH-VERIFIED |
| Google 月處理 token | 3.2 quadrillion（YoY ~7×） | Google I/O 2026 keynote | 2026-05-19 | ✓ SEARCH-VERIFIED |
| OpenAI / Anthropic 年化營收 | ~$250 億（2 月）/ ~$300 億（4 月） | Sacra / SaaStr / RootData | 2026-02~04 | ✓ SEARCH-VERIFIED |
| HBM/DRAM 價格 | 偏緊；HBM4 mid-2026 ~+30% | TrendForce 20260602 | 2026-06-02 | ✓ SEARCH-VERIFIED |
| GPU 租賃利用率 | 未取得直接證據 | — | — | ✗ NOT DISCLOSED（AI overcapacity 子項） |
| SpaceX IPO | Nasdaq SPCX 最快 6/12、募資至多 $750 億、估值 >$2 兆 | CNBC / Bloomberg / Yahoo | 2026-05-22~06-03 | ✓ SEARCH-VERIFIED |
| IPO 管線 AI 佔比 | ~92% | Yahoo / Built In | 2026-05 | ✓ SEARCH-VERIFIED |
| Microcap moonshot（本週） | 無合格標的（VIDA +53%、LEGN +42% 未達門檻） | StockTitan rankings | 2026-06 | ✓ SEARCH-VERIFIED |
| 內部人 Form 4 群聚（14 日） | 無明細 | SEC EDGAR | — | ✗ NOT DISCLOSED |
| 槓桿 ETF AUM（TQQQ/SOXL/TSLL） | $313 億 / $173 億 / $65 億；整體 >$1,700 億 | etf.com / Yahoo | 2026-05~06 | ✓ SEARCH-VERIFIED |
| US 單一個股槓桿 ETF 新上市 | GraniteShares PLA/AHD（5/19）、Direxion 2x 套組（5 月底） | GlobeNewswire / ETF Express | 2026-05-19~28 | ✓ SEARCH-VERIFIED |
| 南韓單一個股槓桿/反向 ETF | 三星/SK 海力士 2x，5/22 上市 | Seoul Economic / Korea Herald | 2026-05-22 | ✓ SEARCH-VERIFIED |
| CSOP SK hynix 2x ETF | $53.8 億（全球最大單一個股槓桿 ETF） | Seoul Economic / TradingKey | 2026-05-08 | ✓ SEARCH-VERIFIED |
| 0DTE 佔 SPX 量 | ~59–63%（2 月 63%） | Cboe Insights | 2026-02~ | ✓ SEARCH-VERIFIED |
| OCC 5 月期權量 | 股票 8.031 億／指數 1.226 億／ETF 5.405 億口 | OCC（Securities Finance Times） | 2026-05（6/02 發布） | ✓ SEARCH-VERIFIED |
| VIX | 15.77 | Macrotrends / FRED VIXCLS | 2026-06-02 | ✓ SEARCH-VERIFIED |
| Cboe SKEW | 136.86 | Cboe / Yahoo ^SKEW | 2026-06-03 | ✓ SEARCH-VERIFIED |
| 股債相關性 | 2026 轉正 | Oxford Economics | 2026 | ✓ SEARCH-VERIFIED |
| CoreWeave $8.5B DDTL（背景） | Moody's A3、Meta 合約擔保 | CoreWeave IR / Bloomberg | 2026-03-31 | ✗ NOT DISCLOSED（30 日內無新案；背景） |
| AI 表外 SPV 債務（背景） | ~$1,200 億（Oracle/xAI/Meta/CoreWeave） | Cryptopolitan / Quartz | 2026（持續） | ✗ NOT DISCLOSED（30 日內無新案；背景） |

**附註：** FRED API key 與 EIA API key 已於環境變數存在，但本執行環境對 FRED/Treasury/EIA 主機之直連（urllib + UA）回 HTTP 403（WAF），`scripts/fetch_macro.py` 全序列 `fetch_failed`、`decomposition unavailable_no_daily_history`，故 10Y 週變動 Δ 分解本週不可用，所有 macro 數值改以 WebSearch spot 呈現，未臆造任何 Δ。報告未輸出任何金鑰或含 `api_key=` 之 URL。

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
  "retail": 63,
  "monetary": 65,
  "structural": 73,
  "total": 68,
  "tier": "高"
}
```

本報告為相對風險溫度計，非擇時訊號。
