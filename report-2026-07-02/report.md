# 2026-07-02 市場泡沫風險評估報告
> 報告日期：2026-07-02；執行日：2026-07-02 Asia/Taipei；ISO 週次：2026-W27；前次基準：report-2026-06-29（3天前）

## §1 六維度風險條圖
| 維度 | 條圖 | 本次 | 前次 | Δ |
|---|---|---:|---:|---:|
| 估值溢價 | ▰▰▰▰▰▰▰▱▱▱ | 79 | 78 | +1 |
| 市場廣度 | ▰▰▰▱▱▱▱▱▱▱ | 30 | 32 | -2 |
| 投機行為 | ▰▰▰▰▰▰▱▱▱▱ | 62 | 66 | -4 |
| 散戶情緒 | ▰▰▰▰▰▱▱▱▱▱ | 55 | 53 | +2 |
| 貨幣與信貸環境 | ▰▰▰▰▰▰▰▱▱▱ | 74 | 75 | -1 |
| 結構性槓桿 | ▰▰▰▰▰▰▰▱▱▱ | 75 | 72 | +3 |
| **加權總分** | ▰▰▰▰▰▰▱▱▱▱ | **65【高】** | 65 | 0 |

## §2 歷史錨點相似度
| 錨點 | 相似度 | 條圖 | 標記 |
|---|---:|---|---|
| 1997 早期建設 | 50% | ▰▰▰▰▰▱▱▱▱▱ |  |
| 1998 LTCM 衝擊 | 25% | ▰▰▱▱▱▱▱▱▱▱ |  |
| 1999 晚期狂熱 | 80% | ▰▰▰▰▰▰▰▰▱▱ | ◀ 最貼近 |
| 2000/3 頂點 | 15% | ▰▱▱▱▱▱▱▱▱▱ |  |
| 2021/12 Meme 頂 | 65% | ▰▰▰▰▰▰▱▱▱▱ |  |

## §3 三角訊號
| 指標 | 本次數值 | vs 前次 |
|---|---|---|
| S&P 500 | 7,483.23 | ▲ +0.58%（前次 ~7,440.43） |
| WTI 原油 | $71.87 /bbl | —（本次方向不可用——無腳本日序） |
| 10Y Treasury | 4.44% | ▲ +6 bps（前次 ~4.38%） |

**三者狀態**：穩定共存。S&P 500 小幅 ▲（+0.58%、距 200DMA +7.85% 未達 +10% 拉伸閾值）、WTI 無新日序（DCOILWTICO latest 06-29 即前次基準日、script 未供 chg_pct）、10Y 小幅 ▲（+6 bps）。三者中兩項小幅同向 ▲、一項方向不可得，無同向拉伸（dev200 < +10%）、亦無確認之反向分歧，依「格局判定規則」落「穩定共存（其餘情形，多為小幅／持平、未見拉伸）」。惟此「穩定」僅在價格三角面：financing 側自前次「已擊發」明顯回落至自滿，價格穩定不等於信用／槓桿環境轉健康。

- 股市：S&P 500 7,483.23（FRED SP500，2026-07-01），較前次 ~7,440.43（06-29）▲ +0.58%；距 200DMA +7.85%、距 52 週 MA +9.68%（較前次 +6.2% / +8.03% 略升，價格拉伸溫和回升、仍未及 +10% 閾值）。
- WTI 原油：$71.87 /bbl（FRED DCOILWTICO，2026-06-29）；script latest 觀測（06-29）即前次基準日、無新日序 chg_pct，方向不可用——無腳本日序，不觸發方向性 ⚠；油價續處低檔（背景，不計方向），對通膨預期上行壓力中性偏冷。
- 10Y 殖利率：4.44%（FRED DGS10，2026-06-30），較前次 4.38% ▲ +6 bps；主要驅動為實質利率（ΔDFII10 +4 bps 主導、ΔT10YIE +1 bp）。

**格局轉變**：前次格局「穩定共存」（讀自 report-2026-06-29 之 score.json `regime`），本次仍判「穩定共存」——價格三角面小幅同向偏多但未見拉伸；惟 financing 扳機自前次「已擊發」回落至「未擊發」（急性私募信貸贖回壓力消退、公開利差收窄至循環低點），信用面自滿與 Fed 受限並存，格局標籤未變但底層 financing 側質變（見結論、本次新增訊號）。

**10Y 成因拆解（`ΔDGS10 ≈ ΔDFII10 + ΔT10YIE`，拆的是週變動、非水位）**：本週 10Y +6 bps。三項 Δ 皆取自各自 FRED 序列日史（script `decomposition`，對齊前次基準 06-29）；T10YIE 為 FRED 直取（非 derived）。嚴禁以 breakeven 水位（2.23%）代 Δ。
- ΔDFII10 實質殖利率週變動：+4 bps、上行
- ΔT10YIE 損益平衡通膨週變動：+1 bp、幾近持平
- 判定：real-rate-driven（實質利率主導；恆等式 +6 ≈ +4 + +1 成立，佐證歸因）

**扳機鏈：油 → 通膨預期 → Fed 受限 → refinancing 成本**：油側靜默（WTI $71.87 低檔、無新日序）、通膨預期錨定（T10YIE 2.23% +1 bp、T5YIFR 5y5y forward 2.20% +0 bp），「油→通膨預期」環節中性偏冷。Fed-constraint 環節仍由 realized 通膨撐住：CPI YoY 4.17%（CPIAUCSL，資料月 2026-05，≥4%，引 script 值非新聞偶得）。Fed 路徑：CME FedWatch 顯示 7/29 FOMC ~70% 維持 3.50–3.75%、年底期貨隱含 ~4.0%、6 月點陣圖中位 3.8%（自 3 月 3.4% 上修，暗示至少一次升息傾向）——市場端偏鷹、升息風險 > 降息。整體：扳機鏈「油→通膨預期」環節冷卻，但 Fed put 因 realized CPI 4.17% + 鷹派點陣圖而受限、難快速放水，形成「froth 難擠、亦難放大」的僵局。

**結論**：扳機狀態：未擊發。判定（決定性，由重至輕取第一個成立者）——（已擊發）私募信貸 gate proration / breach：本窗（06-02~07-02）內僅 Antares Strategic Credit（A-STAR）6/11 半年度回購 redemption-request ratio 10.3% > 7.5% quarterly redemption cap 之 gate proration（按 ~73% 比例分配），惟該基金同期淨流入 ~$78M，屬單一基金 idiosyncratic、不符「多基金惡化 redemption-request 趨勢 / 多基金 net inflow→outflow flip」門檻；前次驅動「已擊發」之多基金 gate 潮（Cliffwater / BCRED / Apollo，5 月底~6 月初）本窗內未再擴大、Fed FSR（2026-05）評為「limited and manageable」；HY OAS 週 Δ -5 bps（非 ≥ +50）；無窗內具名新再融資／信用事件——已擊發不成立。（初啟）breakeven 主導之 10Y 上行且 WTI 同步上行→否（real-rate-driven、WTI 冷）；HY OAS 連兩期走闊→否（本次 -5 bps 收窄）；D5 rationale 標「扳機側」→否（本次自滿側）——初啟不成立。故落未擊發。三者配置歷史意義：估值（CAPE 41.66）＋結構性槓桿（75）之 crash potential energy 仍居高位，但 financing 扳機自前次「已擊發」回落至「未擊發」——急性私募信貸贖回壓力消退、公開利差（HY 2.75% / IG 0.76%）收窄至循環低點——此「平靜」屬自滿側 froth，非結構轉健康；Fed 受 realized 通膨制約使 Fed put 仍受限。整體配置：高位潛在下行位能 × financing 扳機暫熄，屬晚期循環之自滿階段（呼應 §2 之 1999 最貼近）。（三者未同向偏高、扳機未擊發，故本段標題不加 ⚠。）

（以上五段一律用粗體小標、非 `##` / `###` 標題。）

## 六維度評分

### 1. 估值溢價 (weight 22%) — 79（Δ +1）
Shiller CAPE 41.66（multpl.com 07-01，較前次 40.70 續升、遠高於 >38 euphoria 閾值、逼近 dot-com / 2021 級別）、S&P 500 trailing P/E 32.19（multpl 07-01，約長期均值 16.2 之 2 倍；forward P/E ~20 高於 10 年均 ~19）、Mag 7 加權 P/E ~28–33x（MAGS 前次基準 ~33、本次自由來源估 ~28x 偏舊、仍屬高位；單一來源、直抓 403）。**Excess CAPE Yield（利率調整交叉檢核）**：ECY ≈ 1/41.66 − 2.20/100 ≈ **+0.20%**（較前次 +0.27% 續逼近零、係 CAPE 走高所致；接近 0 屬 1929 / 2000 級別訊號——股相對債極貴，為本維度最強警訊，僅作 CAPE 校準、不單獨計分）。TP-upgrade phase：窗內（06-18~29）sell-side 上修以 **EPS-driven 為主**（TSMC BofA $490→$590、Susquehanna $500→$575、UBS 皆以 AI 需求／能見度帶動 EPS；AMD Cantor $500→$700 為 multiple＋EPS 混合），未見 2+ bellwether 同季 multiple-driven re-rating，late-cycle 倍數追逐訊號中性。AI compute reality check：**供給偏緊、非過剩**——GPU 雲端租金分歧但整體緊俏（H100/B200 多家售罄）、HBM/DRAM 契約價續漲（DRAM 產業營收 1Q26 +81% QoQ、DDR2 3Q26 +35–40%、HBM 2027 倍增），capacity 仍被利用率/需求吸收；capex 全面仍上修（stock-of-state、Q1-set carry：$725B、MSFT ~$190B、Alphabet $180–190B、AMZN ~$200B、Meta $125–145B），AI 基本面撐住估值、無系統性過剩缺口。價格趨勢偏離（Farrell #1/#2/#4）：S&P 距 200DMA +7.85%、距 52 週 MA +9.68%（溫和拉伸、未達 +10%）。綜合：估值極貴（CAPE / ECY 為核心風險）但基本面未裂、價格拉伸溫和，較前次 +1。

### 2. 市場廣度 (weight 13%) — 30（Δ -2）
RSP（equal-weight）**領先** SPY（cap-weight）：RSP YTD ~+11.97% vs SPY ~+9.24%（差 ~+2.5–2.7 pt，equal-weight 勝出＝廣度邊際轉佳；Mag 7 1H26 落後大盤）；A/D 正向（07-01 NYSE ~1.48:1、Nasdaq ~1.55:1）、新高 > 新低（NYSE 349 vs 154，~2.3:1）、~62% 成分股站上 50/200DMA（健康、非狂熱）。惟 Top-10 集中度 ~37–39%（Mag 7 ~33–34%）仍屬歷史極端（史均 ~24%）。參與度本身健康、僅集中度偏高，落「輕微轉窄」低段；因 RSP 較前次更明確領先（廣度續轉佳），較前次 -2。

### 3. 投機行為 (weight 18%) — 62（Δ -4）
microcap thematic moonshot 本週（06-25~07-01 嚴格窗）**0 件**（✓ SEARCH-VERIFIED（0 件）；QUBT 6/29 僅 +7.68%、未達 ≥100%；INHD +3,661%、CAST +888%、BYAH +126% 皆為 6 月中上旬、窗外；逢美股 7/3 休市之短週）。insider 集中賣出**本次 0 件**（前次 AMAT cluster 6/15–16 已滾出 14 日窗；NVDA 黃仁勳 6/20–23 為單人 10b5-1、非 cluster；EDGAR/openinsider 直連 403，經次級來源掃描無合格 14 日窗內多人 cluster）——自前次「命中」轉「未命中」，為本次投機降溫主因。+AI rename / SPAC：Ionic（IOND）6/29 crypto→AI/HPC 轉向 S-1（窗內）；Agility Robotics（Churchill XI→AGLT）6/24 機器人 SPAC（$2.5B、窗緣外）。IPO 熱度偏高但回落：Renaissance IPO 指數 YTD +23.9% vs S&P +8.1%（自前次 +26.3% 降）、週內 3 檔 IPO + 4 檔 SPAC 掛牌、生技無營收首日 pop 續見（Kardigan +37.5%）。巨型 IPO pipeline：OpenAI 6/8、SpaceX 6/12 上市（~$1.77T）於 30 日窗內、Anthropic S-1（6/1）窗緣外，惟 OpenAI/Anthropic 實際上市延至 2027（前瞻轉冷）。Cboe equity put/call 0.64（06-30，confirmation，略偏 call、未破 0.50 極端）。投機四訊號（moonshot 0 / insider 0↓ / IPO 熱度↓ / pipeline 持平）三降一持，較前次 -4。

### 4. 散戶情緒 (weight 12%) — 55（Δ +2）
CNN Fear & Greed **32「Fear」**（07-01，低檔、逆勢／背離訊號，為本維度主要下壓）。惟槓桿與部位側偏熱：FINRA Margin Debt 5 月 ~$1.42 兆（連二月創高，MoM +8.5%、**YoY +53.7%**——遠逾 +40–50% 之歷史頂部級別警訊：1999 / 2007 / 2021；stock-of-state carry，資料月 2026-05）；家庭持股佔金融資產比 45.76%（FRED BOGZ1FL153064486Q，Q1 2026，近歷史高位、Farrell #5，季頻沿用不計週 Δ）；AAII bull 44.9% / bear 36.1%（週 ~06-25、偏多）；社群投機熱：Wendy's（WEN）6/24 +26%、r/wsb >18,000 讚、量能 ~203M 股（DORK 籃：DNUT/OPEN/RKLB/KSS）。NAAIM Exposure Index 98.59（06-24，自 92.83 升＝主動經理人近滿倉、擁擠多頭、Farrell #9；confirmation cross-check、微調不主計）。綜合：F&G「Fear」壓抑情緒面，但 margin debt YoY 創頂級警訊 + 家庭持股近高 + NAAIM 擁擠 + WEN 迷因熱推升，淨較前次 +2。

### 5. 貨幣與信貸環境 (weight 20%) — 74（Δ -1）｜**本次側別：自滿側**
HY OAS 2.75%（BAMLH0A0HYM2，06-30，週 Δ **-5 bps**、近循環低點、續收窄＝信用自滿加深）、IG OAS 0.76%（BAMLC0A0CM，06-30，週 Δ 0、循環低點）；Fed funds 3.50–3.75%（DFEDTARU 3.75 / DFEDTARL 3.50，07-01）、市場端偏鷹（FedWatch 7/29 ~70% 維持、年底 ~4.0%、點陣圖中位 3.8%↑、升息風險 > 降息）；realized 通膨仍封頂 Fed put：CPI YoY 4.17%（CPIAUCSL，資料月 2026-05）、T5YIFR 2.20%（+0 bp）。全球流動性偏鬆：WALCL $6.736 兆（06-24）、ECB €6.117 兆（ECBASSETSW，06-26）、BOJ ¥664.3 兆（06-24 月序 2026-05，較 4 月微升；script fetch_failed 改 WebSearch）、PBoC 續挺（TSF +7.7% YoY、6/25 MLF 淨 +¥200B、「維持充裕流動性」）。10Y 成因：+6 bps、real-rate-driven（見 §3）。**私募信貸贖回壓力（private-credit / non-bank fund liquidity stress）**：本窗僅 Antares A-STAR 6/11 gate proration（redemption-request ratio 10.3% > 7.5% quarterly redemption cap、按 ~73% 比例分配），惟同期淨流入 ~$78M、屬單一基金 idiosyncratic，不符多基金惡化趨勢 / net inflow→outflow flip 門檻；前次「已擊發」之多基金 gate 潮（Cliffwater / BCRED / Apollo）本窗內未再擴大、Fed FSR 評「manageable」——**故本次不計入扳機側**。IG OAS / WALCL / ECB / BOJ 皆具現值於上。判分側別：**自滿側**（利差循環低點 + 全球流動性偏鬆之 froth），落「寬鬆且信用自滿」61–80 段；Fed 受 realized 通膨制約使 froth 難快速放大亦難擠出。因急性 financing 扳機自前次消退（前次 75 部分反映扳機側），信用自滿雖加深（HY -5bps），淨較前次 -1。**雙向 Δ 遮蔽防護**：本次為「扳機側 → 自滿側」逆向過渡，score Δ 僅 -1 遮蔽了 financing 側質變（扳機由已擊發回落未擊發），已於 §3 結論與本次新增訊號以質化訊號標明。

### 6. 結構性槓桿 (weight 15%) — 75（Δ +3）
US 槓桿 ETF AUM：單一個股型近循環高（NVDL ~$4.45B、SOXL ~$25–26B、TSLL ~$5.43B、CONL ~$0.5B），廣基 3x TQQQ ~$34B（自 6/18 ~$39.8B 回落）、SQQQ ~$2.23B（淨流出）。US single-stock 槓桿 ETF **發行潮**（14 日窗）：Corgi 31 檔 2x 單一個股 ETF（6/24 15 檔 + 6/26 16 檔，含 NVDA/TSLA/AMD/COIN/GOOGL/META/MSFT/PLTR 等）、Tradr 5 檔（7/1，CIEX/QNTU/RMBX/TSEU/TTMX）——共 36 檔兩週內上市，槓桿工具擴散加速（SEC 仍守 2x 上限）。0DTE 佔 SPX option volume ~61%（Cboe，5 月創高、自 4 月 ~52% 升；55–65 段高位、未持續 > 65%）；OCC 選擇權量高檔（4 月 ~1.446B 口、equity +19.5% YoY；2025 全年 15.2B +26%）。VIX 16.45（07-01、contango 正常）、Cboe SKEW ~144.5（偏高、尾部定價升）、股債相關偏正（分散化保護轉弱）。**AI infrastructure debt financing / vendor-financing loops**：本月（30 日窗）多筆大型設施——CoreWeave $1.25B + €2B 2032 到期優先票據（6/11）、Applied Digital $1.59B 擔保票據（6/9）＋ Goldman $550M RCF（6/8）＋優先股承諾增至 $2B（6/26）、Switch 循環信貸擴至 >$6B + $3.5B LC（近 $10B）、Blue Owl / Corscale $975M 資料中心再融資（6/8）；Nvidia 2026 YTD >$40B AI 股權 + 循環 vendor-financing 爭議（~97% 營運現金再投入客戶、分析性非新披露）。全球槓桿擴散：**本週擴散訊號未觸發**——本週（7 日窗）無非美單一個股槓桿/反向 ETF 新核准（韓國轉監管收緊 Samsung/SK Hynix 槓桿 ETF、歐洲 Leverage Shares 6/12 窗外），未達「2+ 非美市場同週核准」floor 條件。綜合：AI 基建債務潮 + 單一個股槓桿 ETF 發行潮 + 0DTE 創高推升；惟 0DTE 未 > 65%、TQQQ AUM 回落、全球擴散未觸發，未達 81+，較前次 +3。

## 綜合分數

| 維度 | 分數 | 權重 | 加權 |
|---|---:|---:|---:|
| 估值溢價 | 79 | 22% | 17.38 |
| 市場廣度 | 30 | 13% | 3.90 |
| 投機行為 | 62 | 18% | 11.16 |
| 散戶情緒 | 55 | 12% | 6.60 |
| 貨幣與信貸環境 | 74 | 20% | 14.80 |
| 結構性槓桿 | 75 | 15% | 11.25 |
| **加權總分** | | **100%** | **65.09 → 65** |

加權總分 65.09（half-up 取整 65）→ **風險等級：高**（65–84）。
邊界帶：總分 65 距 警戒/高 邊界 ≤ 2 分，評分固有噪音約 ±2–3，等級判讀需保留餘地。

## 歷史泡沫週期對比

相似度計算：checklist v2

每錨點逐項依本次六維度分數與已抓取數據判定命中，相似度 = 命中數 ÷ 特徵數 × 100、四捨五入到最近 5%。輸入摘要：估值 79、廣度 30、投機 62、散戶 55、D5 74（自滿側）、結構 75；扳機狀態＝未擊發；regime＝穩定共存；CAPE 41.66；HY OAS 2.75%（Δ-5bps）；margin debt YoY +53.7%；CPI YoY 4.17%；dev200 +7.85%；S&P chg +0.58%；ΔT10YIE +1bp；moonshot 0；insider cluster 0；巨型 IPO S-1 窗內（OpenAI 6/8、SpaceX 6/12）；社群迷因 WEN 具名。

**1999 晚期狂熱（8/10 = 80%）◀ 最貼近**：命中 ①估值≥75（79）、②CAPE≥38（41.66）、③投機≥60（62）、⑥D5 自滿側且 HY<3.5%（2.75%）、⑦結構≥60（75）、⑧散戶≥55（55）、⑨巨型 IPO pipeline 活躍（OpenAI 6/8 S-1 / SpaceX 6/12 定價，30 日窗內）、⑩扳機未擊發；未命中 ④本週 moonshot 0 且無營收 IPO 佔比未見偏高、⑤廣度<45（30、廣度反而轉佳）。

**2021/12 Meme 頂（5/8 = 65%）**：命中 ②社群投機熱（WEN 具名）、③結構≥65（75）、④流動性氾濫（央行資產負債表微擴 + D5 74 自滿側 ≥60）、⑤margin debt YoY≥+40%（+53.7%）、⑧CPI YoY≥4%（4.17%）且 Fed 尚未實質緊縮（維持觀望、未實升）；未命中 ①散戶≥65（55）、⑥本週 moonshot 0、⑦廣度≥50（30、無指數-廣度背離）。

**1997 早期建設（4/8 = 50%）**：命中 ②廣度<45（30）、④capex 仍上修、⑦HY OAS<4% 且本次未走闊（-5bps）、⑧扳機未擊發；未命中 ①估值 79 逾 40–74 上緣、③投機 62 ≥50、⑤散戶 55 非 <55、⑥結構 75 非 <50——估值/投機/槓桿皆遠超「早期建設」。

**1998 LTCM 衝擊（2/8 = 25%）**：命中 ③具名非銀壓力事件披露（Antares A-STAR gate proration，惟 idiosyncratic）、⑤估值≥60（79）；未命中 ①HY Δ≥+30bps 或 VIX>25（-5bps / VIX 16.45）、②S&P 回檔≥5%（+0.58%）、④Fed 轉鴿（實偏鷹）、⑥扳機≥初啟（未擊發）、⑦廣度 Δ≥+8（-2）、⑧ΔT10YIE≤0（+1bp）。

**2000/3 頂點（1/8 = 15%）**：命中 ⑧貨幣轉緊（FedWatch 隱含年底 ~4.0% / 點陣圖 3.8%↑＝隱含緊縮偏向）；未命中 ①估值≥85（79）、②扳機≥初啟（未擊發）、③廣度≥60（30）、④dev200 自 >+10% 回落 或 回檔≥5%（皆否）、⑤投機≥70（62）、⑥insider cluster≥1（0）、⑦散戶≥65（55）。

**解讀**：本週最貼近 **1999 晚期狂熱**（80%）——估值極端（CAPE 41.66、ECY ~+0.2%）、結構性槓桿高（AI 基建債務潮 + 單一個股槓桿 ETF 發行潮）、巨型 IPO pipeline 活躍、信用自滿（HY/IG 循環低點）、散戶部位偏滿（margin debt YoY +53.7%），但**尚未**呈現 2000/3 頂點特徵（無 insider 集中賣出、無廣度極端狹窄、投機未達狂熱 ≥70、扳機未擊發），故居晚期循環之「狂熱建構」而非「見頂」階段；次貼近 2021/12（65%）反映迷因（WEN）+ margin 槓桿 + CPI>4% 之類比。結構性槓桿以期別調整解讀：本次以 0DTE（61%）、單一個股槓桿 ETF、AI 基建債務為主要載體，對應 1999 之保證金/期權投機、2021 之迷因/槓桿產品。跨期錨點（Farrell #1/#2）：S&P 週 200DMA/52週 MA 偏離 +7.85% / +9.68%（溫和）；長程指數成長趨勢偏離文章錨點（Dot-com ~95%、1929 ~110%、當前 AI 週期 ~147%）僅作敘事脈絡、不週算。

## 機構情緒對照

本次有新機構調查數據：**BofA Global Fund Manager Survey**（發布 ~2026-06-17，調查 6/5–11、198 位經理人、$540B AUM）——6 月投資人**減碼風險**（增現金與債券、減股票/房地產/商品，但對全球成長仍偏正）；尾部風險排序：①二次通膨 34%、②**AI 泡沫 28%**（自 5 月躍升至第二）、③債市失序 19%。高比例「預期崩盤」本身為逆向訊號、且「AI 泡沫」憂慮升溫與本報告估值/結構風險方向一致。JPM 機構調查：本窗無新正式調查發布（僅 6 月展望評論），不納入。

NAAIM Exposure Index 98.59（週頻，06-24，自 92.83 升）——主動經理人近滿倉、擁擠多頭（Farrell #9 逆向訊號）；NAAIM 於 散戶情緒 作 confirmation 計分、此處僅敘述脈絡。AAII 僅作散戶對照（bull 44.9%）、非機構數據。

## 本次新增訊號

比較基準：vs 前次（3天前，report-2026-06-29）。

- **貨幣與信貸環境（D5，雙向計分）｜側別逆轉：扳機側 → 自滿側（質化新訊號）**：前次因多基金私募信貸 gate 潮（Cliffwater / BCRED / Apollo）判「已擊發／扳機側」；本窗（06-02~07-02）該多基金潮**未再擴大**，僅存 Antares A-STAR 6/11 單一基金 gate proration（redemption-request ratio 10.3% > 7.5% cap、且同期淨流入 ~$78M＝idiosyncratic），Fed FSR 評「manageable」，HY OAS 週 -5 bps 收窄至循環低點。扳機狀態自「已擊發」回落「未擊發」。score Δ 僅 -1（74）遮蔽此質變——**分數高位主因已由「financing 扳機」轉為「信用自滿 froth」**；此為「扳機側→自滿側」逆向過渡，依雙向 Δ 遮蔽防護於此明列。
- **結構性槓桿 +3（75）**：AI infrastructure debt financing 本月多筆大型設施（CoreWeave $1.25B+€2B 6/11、Applied Digital $1.59B 6/9＋$550M RCF＋$2B 優先股 6/26、Switch 近 $10B、Blue Owl/Corscale $975M 6/8）；US 單一個股槓桿 ETF 兩週發行 36 檔（Corgi 31＋Tradr 5）；0DTE 佔 SPX ~61%（創高）。全球槓桿擴散：**本週擴散訊號未觸發**（無 2+ 非美市場同週核准）。
- **投機行為 -4（62）**：microcap moonshot 0 件（✓（0 件））、insider 集中賣出自前次「命中」轉 0 件（AMAT cluster 滾出 14 日窗）、IPO 熱度回落（Renaissance YTD +26.3%→+23.9%）；巨型 IPO pipeline（OpenAI 6/8/SpaceX 6/12）持平但實際上市延 2027。
- **散戶情緒 +2（55）**：margin debt 5 月創高 YoY +53.7%（頂部級別）、NAAIM 98.59↑、社群迷因 WEN 具名轉熱；惟 CNN F&G 32「Fear」壓抑。
- **估值溢價 +1（79）**：CAPE 40.70→41.66、ECY +0.27%→+0.20%（續逼近零）；AI compute 供給仍緊（非過剩）、capex 全面上修撐住基本面。
- **市場廣度 -2（30）**：RSP 更明確領先 SPY（YTD ~+11.97% vs ~+9.24%）、A/D 正向、新高>新低，參與度轉佳；Top-10 集中度 ~38% 仍極端。
- 總分 65（Δ 0）、等級「高」不變、regime「穩定共存」不變（詳 §3 格局轉變）。

## 數據附錄

### Coverage table（每列對應一個 `# Data sources` bullet，共 47 列）

| # | 維度 / source bullet | 預定來源與方法 | 狀態 |
|---|---|---|---|
| 1 | 估值-S&P 500 P/E & Shiller CAPE | multpl / gurufocus [SEARCH] | ✓ SEARCH-VERIFIED（P/E 32.19、CAPE 41.66，multpl 07-01） |
| 2 | 估值-Mag 7 加權 P/E & AI leader P/S | 財報/彙整 [DIRECT] | ✓ SEARCH-VERIFIED（Mag 7 加權 P/E ~28–33x；MAGS 前次 ~33、自由來源 ~28x 偏舊、直抓 403） |
| 3 | 估值-Analyst TP upgrade decomposition | 賣方 TP [SEARCH] best-effort | ✓ SEARCH-VERIFIED（TSMC BofA/Susquehanna/UBS、AMD Cantor，06-18~29，EPS-driven 為主） |
| 4 | 估值-S&P 500 price-trend deviation | scripts/fetch_macro.py（SP500） | ✓ API（dev200 +7.85% / dev52w +9.68%，07-01） |
| 5 | 廣度-RSP vs SPY YTD | slickcharts / yahoo [SEARCH] | ✓ SEARCH-VERIFIED（RSP ~+11.97% vs SPY ~+9.24% YTD） |
| 6 | 廣度-Top-10 集中度 | slickcharts / index data [SEARCH] | ✓ SEARCH-VERIFIED（Top-10 ~37–39%、Mag 7 ~33–34%） |
| 7 | 廣度-A/D、新高/新低 | wsj / barchart [SEARCH] | ✓ SEARCH-VERIFIED（A/D ~1.5:1；NH 349 vs NL 154，07-01） |
| 8 | 散戶-CNN Fear & Greed | cnn [SEARCH] | ✓ SEARCH-VERIFIED（32「Fear」，07-01） |
| 9 | 散戶-Margin Debt + YoY + /市值 | FINRA / advisorperspectives [SEARCH] | ✓ SEARCH-VERIFIED（$1.42T、+8.5% MoM、+53.7% YoY，5 月；/市值精確比未公布） |
| 10 | 散戶-AAII | aaii [SEARCH] | ✓ SEARCH-VERIFIED（bull 44.9%/bear 36.1%，週~06-25） |
| 11 | 散戶-社交情緒代理 | reddit / X [SEARCH] best-effort | ✓ SEARCH-VERIFIED（WEN +26% 6/24、DORK 籃） |
| 12 | 散戶-家庭持股佔金融資產比 | scripts/fetch_macro.py（BOGZ1FL153064486Q） | ✓ API（45.76%，Q1 2026） |
| 13 | 散戶-NAAIM Exposure Index | naaim / ycharts [SEARCH] best-effort | ✓ SEARCH-VERIFIED（98.59，06-24） |
| 14 | 機構-BofA FMS & JPM survey | 機構調查 [SEARCH] best-effort | ✓ SEARCH-VERIFIED（BofA FMS 06-17 新；JPM 無新） |
| 15 | D5-Fed funds（DFEDTARU/DFEDTARL） | scripts/fetch_macro.py | ✓ API（3.75%/3.50%，07-01） |
| 16 | D5-HY OAS（BAMLH0A0HYM2） | scripts/fetch_macro.py | ✓ API（2.75%、Δ-5bps，06-30） |
| 17 | D5-IG OAS（BAMLC0A0CM） | scripts/fetch_macro.py | ✓ API（0.76%、Δ0，06-30） |
| 18 | D5-10Y（DGS10） | scripts/fetch_macro.py | ✓ API（4.44%、Δ+6bps，06-30） |
| 19 | D5-10Y 實質（DFII10） | scripts/fetch_macro.py | ✓ API（2.20%、Δ+4bps，06-30） |
| 20 | D5-10Y breakeven（T10YIE） | scripts/fetch_macro.py | ✓ API（2.23%、Δ+1bp，07-01；FRED 直取非 derived） |
| 21 | D5-WTI（DCOILWTICO） | scripts/fetch_macro.py | ✓ API（$71.87，06-29，level-only 無 chg_pct） |
| 22 | D5-CPI YoY（CPIAUCSL） | scripts/fetch_macro.py | ✓ API（YoY 4.17%，資料月 2026-05） |
| 23 | D5-5y5y forward（T5YIFR） | scripts/fetch_macro.py | ✓ API（2.20%、Δ0，07-01） |
| 24 | D5-Fed funds path（CME FedWatch） | CME/Reuters [SEARCH] best-effort | ✓ SEARCH-VERIFIED（7/29 ~70% 維持、年底 ~4.0%/點陣圖 3.8%） |
| 25 | D5-Fed 資產負債表（WALCL） | scripts/fetch_macro.py | ✓ API（$6.736 兆，06-24） |
| 26 | D5-全球央行 ECB/BOJ（ECBASSETSW+JPNASSETS） | scripts/fetch_macro.py（BOJ 失敗改 SEARCH） | ✓ SEARCH-VERIFIED（worst-case；ECB €6.117 兆 ✓API、BOJ ¥664.3 兆 ✓SEARCH，月序 2026-05） |
| 27 | D5-PBoC aggregate financing | PBoC/NBS [SEARCH] best-effort | ✓ SEARCH-VERIFIED（TSF +7.7% YoY、6/25 MLF 淨+¥200B） |
| 28 | D5-私募信貸贖回壓力 | BDC/interval fund [SEARCH] best-effort | ✓ SEARCH-VERIFIED（Antares A-STAR 6/11 proration、idiosyncratic＋淨流入；多基金潮未再擴大） |
| 29 | AI-Hyperscaler capex guidance | 財報 [SEARCH] required | ✓ SEARCH-VERIFIED（$725B、全面上修，Q1-set carry-forward） |
| 30 | AI-token volume growth | [SEARCH] best-effort | ✓ SEARCH-VERIFIED（Google >3.2 quadrillion tokens/月 ~7x YoY，carry） |
| 31 | AI-OpenAI/Anthropic 營收 | [SEARCH] best-effort | ✓ SEARCH-VERIFIED（Anthropic ~$45B / OpenAI ~$33B ARR，press 估計，carry） |
| 32 | AI-hyperscaler 客戶集中度 | 財報 [SEARCH] best-effort | ✓ SEARCH-VERIFIED（CoreWeave MSFT ~67%、top-3 >80%，carry Q1） |
| 33 | AI-compute 供需/過剩 | [SEARCH] best-effort | ✓ SEARCH-VERIFIED（供給偏緊非過剩；GPU 售罄、HBM/DRAM 契約價漲） |
| 34 | 投機-+AI rename/SPAC/無營收 IPO（7d） | [SEARCH] | ✓ SEARCH-VERIFIED（Ionic 6/29；Agility 6/24 窗緣外） |
| 35 | 投機-IPO market heat | renaissance [SEARCH] | ✓ SEARCH-VERIFIED（IPO 指數 YTD +23.9%、週 3 IPO+4 SPAC） |
| 36 | 投機-microcap moonshots | finviz/benzinga [SEARCH] required | ✓ SEARCH-VERIFIED（0 件，嚴格 7 日窗） |
| 37 | 投機-Upcoming AI IPOs | S-1/具名 [SEARCH] best-effort | ✓ SEARCH-VERIFIED（OpenAI 6/8 S-1、SpaceX 6/12 上市；延 2027） |
| 38 | 投機-insider Form 4 clusters | SEC EDGAR [SEARCH] required | ✓ SEARCH-VERIFIED（0 件；14 日窗無合格 cluster；EDGAR/openinsider 403） |
| 39 | 投機-Cboe equity put/call | cboe/ycharts [SEARCH] best-effort | ✓ SEARCH-VERIFIED（0.64，06-30） |
| 40 | 結構-US 槓桿 ETF AUM | etf.com/etfdb [SEARCH] | ✓ SEARCH-VERIFIED（NVDL ~$4.45B、SOXL ~$25–26B、TSLL ~$5.43B、TQQQ ~$34B↓、SQQQ ~$2.23B、CONL ~$0.5B） |
| 41 | 結構-US 單一個股槓桿 ETF 核准/上市 | SEC/etf.com [SEARCH] | ✓ SEARCH-VERIFIED（Corgi 31 檔 6/24&6/26、Tradr 5 檔 7/1） |
| 42 | 結構-全球槓桿產品核准（KRX/TWSE/JPX/ESMA） | 監管 feed [SEARCH] best-effort | ✗ NOT DISCLOSED（本週無非美單一個股槓桿核准；本週擴散訊號未觸發） |
| 43 | 結構-0DTE option volume | Cboe [SEARCH] | ✓ SEARCH-VERIFIED（~61% SPX，5 月創高） |
| 44 | 結構-Options total volume（OCC） | theocc.com [SEARCH] | ✓ SEARCH-VERIFIED（4 月 ~1.446B 口、equity +19.5% YoY；5 月總量未公布明細） |
| 45 | 結構-VIX/SKEW/股債相關 | cboe/ycharts [SEARCH] | ✓ SEARCH-VERIFIED（VIX 16.45 contango、SKEW ~144.5、股債相關偏正） |
| 46 | 結構-margin debt 交叉引用（confirmation） | 引用散戶 #9 | derived（$1.42T / +53.7% YoY 作確認，不重複計分） |
| 47 | 結構-AI infrastructure debt financing | [SEARCH] best-effort | ✓ SEARCH-VERIFIED（CoreWeave $1.25B+€2B 6/11、APLD $1.59B 6/9＋$550M＋$2B 6/26、Switch ~$10B、Blue Owl $975M 6/8） |

### Raw data table（計分用具體數據點）

| 指標 | 數值 | 來源（FRED series ID / URL） | 資料日期 | 抓取 timestamp |
|---|---|---|---|---|
| S&P 500 spot | 7,483.23 | FRED SP500（scripts/fetch_macro.py） | 2026-07-01 | 2026-07-02 (UTC+8) |
| S&P 200DMA 偏離 | +7.85%（52wk +9.68%） | FRED SP500 derived（sp500_trend） | 2026-07-01 | 2026-07-02 (UTC+8) |
| S&P vs 前次 | +0.58%（prior 7,440.43 @06-29） | FRED SP500（sp500_trend.chg_pct） | 2026-06-29→07-01 | 2026-07-02 (UTC+8) |
| Shiller CAPE | 41.66 | multpl.com/shiller-pe | 2026-07-01 | 2026-07-02T02:18Z |
| S&P 500 trailing P/E | 32.19 | multpl.com/s-p-500-pe-ratio | 2026-07-01 | 2026-07-02T02:18Z |
| Excess CAPE Yield | +0.20%（1/41.66 − 2.20/100） | derived（CAPE、DFII10） | 2026-07-01 | 2026-07-02 (UTC+8) |
| Mag 7 加權 P/E | ~28–33x | Yahoo/Yardeni via search（MAGS 前次基準 ~33） | ~2026-06（偏舊） | 2026-07-02T02:20Z |
| Analyst TP 上修 | TSMC $490→$590(BofA)/$500→$575(Susq)；AMD $500→$700(Cantor) | TheStreet/Investing/TipRanks via search | 2026-06-20~29 | 2026-07-02T02:22Z |
| AI compute 供需 | 供給緊、HBM/DRAM 契約價漲（DRAM 1Q26 +81% QoQ） | TrendForce / SemiAnalysis via search | 2026-06-01~22 | 2026-07-02T02:25Z |
| Hyperscaler capex 2026 | $725B（MSFT ~$190B/Alphabet $180–190B/AMZN ~$200B/Meta $125–145B） | Tom's Hardware（Q1-set carry） | 2026-Q1 | 2026-07-02 (carry) |
| RSP / SPY YTD | ~+11.97% / ~+9.24%（差 ~+2.5pt） | Yahoo Finance / totalrealreturns via search | ~2026-06-30 | 2026-07-02T02:20Z |
| Top-10 集中度 | ~37–39%（Mag 7 ~33–34%） | Wikipedia S&P500 / Forbes via search | 2026-06 | 2026-07-02T02:20Z |
| A/D、新高/新低 | NYSE ~1.48:1；NH 349 / NL 154 | Kitco/Reuters wrap；investcom via search | 2026-07-01 | 2026-07-02T02:20Z |
| CNN Fear & Greed | 32「Fear」 | cnn.com/markets/fear-and-greed via search | 2026-07-01 | 2026-07-02T02:19Z |
| Margin Debt | $1.42T、+8.5% MoM、+53.7% YoY | advisorperspectives.com/dshort（FINRA） | 2026-05（發布 06-24） | 2026-07-02T02:19Z |
| AAII | bull 44.9% / neutral 18.9% / bear 36.1% | aaii.com/sentimentsurvey via search | 週~2026-06-25 | 2026-07-02T02:19Z |
| 社群迷因 | WEN +26%（6/24）、量 ~203M 股 | Yahoo Finance / AltIndex via search | 2026-06-24 | 2026-07-02T02:19Z |
| 家庭持股佔金融資產 | 45.76% | FRED BOGZ1FL153064486Q | 2026-01-01（Q1） | 2026-07-02 (UTC+8) |
| NAAIM Exposure | 98.59（自 92.83） | naaim.org / macromicro via search | 2026-06-24 | 2026-07-02T02:19Z |
| BofA FMS | 6 月減碼風險；尾部風險 AI 泡沫 28%(#2) | Mace News / TradingView via search | 2026-06-17（調查 6/5–11） | 2026-07-02T02:19Z |
| Fed funds target | 3.50–3.75% | FRED DFEDTARU 3.75 / DFEDTARL 3.50 | 2026-07-01 | 2026-07-02 (UTC+8) |
| HY OAS | 2.75%（Δ -5bps） | FRED BAMLH0A0HYM2 | 2026-06-30 | 2026-07-02 (UTC+8) |
| IG OAS | 0.76%（Δ 0） | FRED BAMLC0A0CM | 2026-06-30 | 2026-07-02 (UTC+8) |
| 10Y / 實質 / breakeven | 4.44% / 2.20% / 2.23%（Δ +6 / +4 / +1 bps） | FRED DGS10 / DFII10 / T10YIE | 2026-06-30~07-01 | 2026-07-02 (UTC+8) |
| WTI | $71.87 | FRED DCOILWTICO | 2026-06-29 | 2026-07-02 (UTC+8) |
| CPI YoY | 4.17% | FRED CPIAUCSL | 2026-05 | 2026-07-02 (UTC+8) |
| 5y5y forward | 2.20%（Δ 0） | FRED T5YIFR | 2026-07-01 | 2026-07-02 (UTC+8) |
| CME FedWatch | 7/29 ~70% 維持；年底 ~4.0%/點陣圖 3.8% | CME / CNBC via search | 2026-06-29 | 2026-07-02T02:19Z |
| WALCL | $6,735,645M | FRED WALCL | 2026-06-24 | 2026-07-02 (UTC+8) |
| ECB / BOJ 資產 | €6.117 兆 / ¥664.3 兆 | FRED ECBASSETSW / Trading Economics(BOJ) | 06-26 / 2026-05 | 2026-07-02 |
| PBoC | TSF +7.7% YoY；6/25 MLF 淨 +¥200B | Trading Economics / Crypto Briefing via search | 2026-05~06 | 2026-07-02T02:19Z |
| 私募信貸 | Antares A-STAR：req 10.3%>7.5% cap、proration ~73%、淨流入 ~$78M | SEC SC TO-I/A via search | 2026-06-11 | 2026-07-02T02:19Z |
| microcap moonshot | 0 件（嚴格 7 日窗） | finviz/stocktitan via search | 2026-06-25~07-01 | 2026-07-02T02:24Z |
| insider Form 4 cluster | 0 件（14 日窗無合格 cluster） | SEC EDGAR/openinsider（403）→ search | 2026-06-18~07-01 | 2026-07-02T02:27Z |
| 巨型 IPO pipeline | OpenAI 6/8 S-1、SpaceX 6/12 上市 ~$1.77T；延 2027 | Crypto Briefing / Renaissance via search | 2026-06-08~12 | 2026-07-02T02:21Z |
| Cboe equity put/call | 0.64 | ycharts via search | 2026-06-30 | 2026-07-02T02:27Z |
| 槓桿 ETF AUM | NVDL ~$4.45B / SOXL ~$25–26B / TSLL ~$5.43B / TQQQ ~$34B / SQQQ ~$2.23B / CONL ~$0.5B | etf.com/etfdb via search | ~2026-06-30 | 2026-07-02T02:21Z |
| 單一個股槓桿 ETF 上市 | Corgi 31 檔(6/24&6/26)、Tradr 5 檔(7/1) | PRNewswire via search | 2026-06-24~07-01 | 2026-07-02T02:21Z |
| 0DTE 佔 SPX | ~61%（5 月創高） | Cboe Insights / PRNewswire via search | 2026-05（發布 06-02） | 2026-07-02T02:21Z |
| OCC 選擇權量 | 4 月 ~1.446B 口（equity +19.5% YoY） | theocc.com via search | 2026-04（發布 05-04） | 2026-07-02T02:23Z |
| VIX / SKEW | 16.45（contango）/ ~144.5 | Saxo / Cboe via search | 2026-07-01 | 2026-07-02T02:24Z |
| AI infra 債務 | CoreWeave $1.25B+€2B(6/11)、APLD $1.59B(6/9)+$550M+$2B(6/26)、Switch ~$10B、Blue Owl $975M(6/8) | 公司 PR / SEC 8-K / DCD via search | 2026-06-08~26 | 2026-07-02T02:20Z |

**附註**：(1) 巨集數據由 `scripts/fetch_macro.py`（FRED API，urllib）取得，所有 FRED 列以 series_id 引用、未含任何 api_key。(2) JPNASSETS（BOJ）本次 script `fetch_failed`，改 WebSearch 取現貨（¥664.3 兆，資料月 2026-05）；ECB/BOJ 合併列取 worst-case（BOJ 之 SEARCH 狀態）。(3) §3 三角：S&P chg 取 script `sp500_trend.chg_pct`（+0.58% → ▲）；10Y 取 `decomposition.d_dgs10_bps`（+6 bps → ▲）；WTI DCOILWTICO 僅回報 latest（06-29 即前次基準日）、無 chg_pct，方向標 —、不觸發 ⚠。(4) capex / Mag 7 P/E / CAPE / margin debt / 家庭持股 / token / ARR / 客戶集中度為 stock-of-state，依 Constraints 豁免 within-window 發布日規則，均附現值/資料季度快照。(5) 多數市場/事件源（SEC EDGAR、openinsider、cnn、cboe、slickcharts、etf.com 等）於本 runtime 直抓 403，經 WebSearch 取值並附來源，屬 ✓ SEARCH-VERIFIED 成功檢索。(6) 私募信貸多基金前次已計數之 gate 事件（Cliffwater/BCRED/Apollo）為窗緣背景、非本次新訊號，未重複列入 本次新增訊號。

## 本次分數存檔
```json
{
  "date": "2026-07-02",
  "iso_week": "2026-W27",
  "weekday": "Thursday",
  "timezone": "Asia/Taipei",
  "valuation": 79,
  "breadth": 30,
  "speculation": 62,
  "retail": 55,
  "monetary": 74,
  "structural": 75,
  "total": 65,
  "tier": "高",
  "regime": "穩定共存"
}
```

本報告為相對風險溫度計，非擇時訊號。
