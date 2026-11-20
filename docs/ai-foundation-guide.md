# 《AI版奠基文件》先讀這裡

這是一份兩頁的入口，寫給初次接觸的 AI 治理、安全與代理系統研究者。[全文](ai-foundation.md)約十五萬字，分零至十四部與兩份附錄；這一頁說明它主張什麼、和常見做法差在哪裡、證據到哪裡為止，以及依你的目的從哪裡讀起。

## 這份文件是什麼

《AI版奠基文件》把《生命導航學》對定位、中介與動態關係的理解，轉譯到人與 AI 共同工作的情境：目標、資訊、角色與環境持續變動時，參與者如何看清自己正在承接什麼，讓判斷、行動與後果仍能接上，並在現實回應中調整下一步。

它不是一份可直接執行的規格，也不是已驗證的方法。它是一份共同定位的底稿：說明理論怎麼理解這些關係，哪些部分已轉成可查驗的工程描述，哪些還沒有承接。

## 核心主張

1. **位置先於能力。** 同一項能力，放在不同的人、目的、權限與後果之中，承接的是不同的事。能做，不等於被委託；被委託，不等於獲准；獲准，也不等於已完成。（[第一部](ai-foundation.md#reading-005)、[1.2](ai-foundation.md#reading-007)）
2. **注意、搜尋、行動與事實各有資格，不能互相代領。** 一個異常值得注意，不表示可以任意調查；查明一件事，不表示查明的人有權處置。工程上壓縮成「候選路徑不等於行動資格，行動資格不等於事實資格」（Candidate Path ≠ Action Qualification ≠ Fact Qualification），並以承重約束檢查每一步的決定、代價與後果落在誰身上。（[第二部](ai-foundation.md#reading-011)、[四權＋一承重約束](ai-foundation.md#reading-059)）
3. **送達不等於接手。** 起點、終點與事實都在，不表示兩點之間已有一條走得通的路；交出訊息，也不等於對方已能用它判斷。（[第四部](ai-foundation.md#reading-026)、[7.4](ai-foundation.md#reading-055)）
4. **世界要會回應。** 牆阻斷不可走的路，坡讓偏離的後果回到行動迴路，橋把回報送到有資格承接的位置。三者作用不同，不能互相替代。（[第五部](ai-foundation.md#reading-032)）
5. **框架和成果都會失格。** 路徑失敗與框架失格要分開。曾經有效的方法、量尺與文件，在條件改變後要能退位；退位撤銷的是當下效力，歷史仍然保存。（[第三部](ai-foundation.md#reading-019)、[第十四部](ai-foundation.md#reading-114)）
6. **區分即生成，讀的是方向。** 判斷不是在兩個答案中挑一個：看出原本混在一起的兩件事那一刻，下一步就同時出現。讓關係轉動的那一處（文件稱為「樞」）不是事先選好的，而是在區分中浮到前景。在持續的工作流裡，一個階段目標達成也是讀數，會成為下一階段的材料；單一任務完成就停下，仍是正當的結果。（[4.2](ai-foundation.md#reading-028)、[9.4–9.5](ai-foundation.md#reading-073)、[14.1](ai-foundation.md#reading-116)、[附錄二第七節](ai-foundation.md#appendix-engineering-distinction-generation)）
7. **生機不是分數。** 仍在運轉不等於有生機；局部的好結果要接回他者的代價；每個位置讀自己的方向，沒有人或系統替整個場算出總分。（[第十三部](ai-foundation.md#reading-105)、[13.7](ai-foundation.md#reading-112a)）

## 和常見做法差在哪裡

下表不是評判其他做法，只標出這份文件多問了哪一題。

| 常見的設計 | 這份文件多問的 |
|---|---|
| 行動前設一道閘門，通過即放行 | 資格會隨新的現實撤回；承重是貫穿整段關係的檢查，不是一次蓋章（[2.5](ai-foundation.md#reading-016)、[附錄二第六節](ai-foundation.md#appendix-engineering-holographic-bearing)） |
| 加一個驗證者或投票，提高正確率 | 第二份讀數要被指定，也要來源獨立；份數多不等於資格高（[5.6](ai-foundation.md#reading-038)、[7.1](ai-foundation.md#reading-052)） |
| 讓人類在迴路中確認 | 交給人之後，還要看人是否拿得到足以判斷的依據（[7.4](ai-foundation.md#reading-055)） |
| 以固定目標與量尺優化，達標即停 | 量尺本身也會失去作用資格；持續工作流中，達標是讀數，不是停止讀取的訊號（[13.6](ai-foundation.md#reading-112)、[14.1](ai-foundation.md#reading-116)） |
| 把判斷寫成在選項中挑一個答案 | 區分的同時就生成下一步；只貼上 A、B 標籤再照原劇本走，寫到的只是區分的外形（[附錄二第七節](ai-foundation.md#appendix-engineering-distinction-generation)） |

## 證據到哪裡為止

- 研究包含十四輪探索性實驗（E1–E14），以小規模沙盒與單一作者設計為主；完整歷程與反例見[實驗脈絡重力帳](../research/research-ledger.md)。
- 文件中的工程描述多為轉譯與查驗方向。有實驗支持的部分，正文與來源註標明其範圍。
- 第十四次實驗結案時，原定治理零件的效果未充分受測。之後轉向的治理演算法仍在 v0.x，尚未公開。
- 作者確認、AI 的同意與文字的流暢，都不替代獨立實驗證據。可查與不可查的範圍見[來源與可查核範圍](../SOURCE_STATUS.md)。

## 依目的的讀法

- **先抓主張：** [卷首](ai-foundation.md#reading-preface) → [第一部](ai-foundation.md#reading-005) → [第二部](ai-foundation.md#reading-011) → [4.1–4.2](ai-foundation.md#reading-027) → [附錄二第七節](ai-foundation.md#appendix-engineering-distinction-generation)。
- **代理系統的安全與工程：** [第二部](ai-foundation.md#reading-011)、[第四部](ai-foundation.md#reading-026)、[第五部](ai-foundation.md#reading-032)、[第七部](ai-foundation.md#reading-050)、[附錄二](ai-foundation.md#appendix-engineering-translation)。
- **評測與量尺：** [第八部](ai-foundation.md#reading-057)、[第十三部](ai-foundation.md#reading-105)、[附錄二第六節](ai-foundation.md#appendix-engineering-holographic-bearing)。
- **想看理論來源：** 先讀[體系發展參照地圖](system-development-map.md)，它是母理論的公開入口。

## 幾個用語

- **Reality：** 須被接觸與核對的現實，包括事實、他者的回應、時間、權限、代價與後果；不限於測試分數。
- **讀數／第二讀數：** 讀數是此刻實際取得的材料；第二讀數是能和原判斷對照、來源獨立的另一份。
- **承重：** 決定、責任、代價與後果，是否落在能承擔的位置。
- **樞：** 使兩端可被區分、關係得以轉動的位置。它本身沒有內容，不是事先選好的元件。
- **中介：** 依當下定位，讓必要關係實際接上的作用；可以是提問、轉達、邊界、減量或退出。
- **退位：** 撤去失格事物的當下效力，同時保存它的歷史。
- **UNKNOWN：** 保留為未知的狀態。它仍能支持有限而合格的下一步，但不能被想像補成事實。
- **生機：** 生命或關係能繼續生成新回應與下一步的方向；不是活動量，也不是單一分數。

---

本頁為 2026-11-20 新增的閱讀入口，依《AI版奠基文件》v0.7 整理，不新增理論或實驗結果；內容若與全文有出入，以全文為準。
