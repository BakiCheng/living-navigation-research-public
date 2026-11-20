# 生命導航學 Living Navigation

**Baki Cheng｜作者與研究者**

公開儲存庫：[living-navigation-research-public](https://github.com/BakiCheng/living-navigation-research-public)

## In brief (English)

Living Navigation is a practice-based philosophy of self-understanding, developed by the author over many years: how a person, or an agent, can recognise their own position and misalignments in unknown and changing situations, and find a next step that is grounded and actually taken up by someone. This repository holds its public reference map, its translation into AI governance (the *AI Foundation* document), and a research ledger covering fourteen rounds of experiments (E1–E14), including negative results and corrections.

One idea sets the approach apart. Many agent and governance designs treat a judgment as picking the right answer, and stop reading once a goal is marked as met. Here, each distinction is read for direction — does this step leave the situation more able to move, or more stuck? — and in an ongoing workflow every completed stage becomes a reading that feeds the next one. Finishing a single task and stopping remains a legitimate end.

The documents are written in Traditional Chinese. Start with the [system map](docs/system-development-map.md), then the [AI Foundation](docs/ai-foundation.md) (a two-page entry is in [ai-foundation-guide.md](docs/ai-foundation-guide.md)), then the [research ledger](research/research-ledger.md). The evidence is exploratory and small-scale; [SOURCE_STATUS.md](SOURCE_STATUS.md) states what can and cannot be independently checked. The documents are licensed under [CC BY 4.0](LICENSE).

當原來可行的方法失效，我們如何重新看清自己、他人與環境的位置，找到有依據、有人承接的下一步？

生命導航學是我長期投入的研究與創作。它從長期生活經驗與持續自我檢驗出發，關心人在未知與變動中如何辨認位置與錯位、跨過心智幻象、恢復自主與創造，讓生命力朝向生機流轉。這份工作逐步形成理論文件，也透過與AI協作，把原本難以言說的第一人稱動態導航過程，轉成可以閱讀、討論、形式化與沙盒檢驗的活體材料。

最初選擇的入口是驗證：不只核對行動是否符合規格，也追問規格、目的與現實後果是否仍然相合。

這個儲存庫以生命導航學為主體，收錄它進入人機協作與AI研究的轉譯及實驗。AI實驗讓概念接受具體情境、程式狀態機與行為結果的檢查；實驗中的有效結果、失真與反例，再回過頭幫助釐清理論。安全、驗證與治理是這條研究路深入展開的一條應用領域。

它和多數 AI 治理設計的一個差別：常見做法把判斷寫成「選出正確答案」，目標一被記為達成就不再讀取；這裡的判斷讀的是方向——這一步讓局面更能動，還是更卡。在持續的工作流裡，每一段完成都成為下一段的讀數與養分；單一任務完成後停下，仍是正當的結果。

這套體系有兩條應用分支：寫給人的書正在撰寫中，尚未公開；AI 治理的轉譯與實驗收錄於本庫。完整母奠基文件為私人材料，本庫以體系發展參照地圖作為公開入口。

## 路線一　理解理念與體系全景

**未知迷霧中的動態導航 → AI版轉譯入口 → 實證脈絡與收束**

1. **從認識自己與體系全景開始**：閱讀 [《生命導航學》體系發展參照地圖 v0.17](docs/system-development-map.md)。從日常情境與案例進入，認識母願景、3D 螺旋定位、定位與中介如何相互生成、AB 判準與動態承重，以及未知中的五環導航。附目錄、定位模型原圖與五環動線圖；完整母奠基文件仍為私人材料，不需先取得它才能閱讀本篇。
2. **看它如何進入 AI 治理情境**：可先讀兩頁的[《AI版奠基文件》先讀這裡](docs/ai-foundation-guide.md)，再閱讀 [AI版奠基文件 v0.7](docs/ai-foundation.md) 的卷首、第零至十四部及附錄二。看這套思考如何轉譯為資格分流（`Candidate Path ≠ Action Qualification ≠ Fact Qualification`）、四權＋一承重約束、坡與橋的治理地形、動態承重全息場、跨季沉積退位，以及與外部開放世界遞迴框架（如 Google Harness²）之結構對位。
3. **沿實證脈絡看概念如何受檢**：沿 [實驗脈絡重力帳](research/research-ledger.md#ledger-ch-1) 檢視自第一至第十四次實驗（E1～E14）的研究演變、哪些結果改變了理解、何時建立雙讀數，以及各階段的收束。最新的 [E14 結案補錄](research/research-ledger.md#e14-closure-20261113) 區分工程修正、行為觀察與尚未測得的治理效果。

如果你關心人或智慧體如何在未知處境中形成判斷，或希望一起把這些動態關係轉成可閱讀、可使用的作品，可以由這條路進入。

## 路線二　檢視 AI 研究、實作與沙盒驗證

**第5次的可操作介面 → 第9次的行為比較 → 第9.5次的多角色承接 → 第13次的因果世界與容量鏈 → 證據與限制**

| 代表作品 | 在研究什麼 | 可以檢視的內容 |
|---|---|---|
| [第5次研究脈絡的投稿作品：When the Approved Path Breaks](research/experiment-5/report.md) | 原先獲准的路徑走不通時，如何交回未知，而非讓agent自行取得更多權限？ | UNKNOWN Junction Harness全文、介入位置圖、案例推演、結果表與可複製的交接格式；另有 [Apart公開作品頁](https://apartresearch.com/sprints/projects/when-the-approved-path-breaks-an-unknown-junction-harness-for-agentic-ai-incident-response-irpb) |
| [第9次實驗：從看見自己到跨季後果回流](research/experiment-9/closure-report.md) | 看見問題是否會改變行動？經驗換到下一季後，哪些作用留下來？ | 三季沙盒、停用公告的正式比較、回報與退件紀錄，以及舊資料指標漏掉的無來源數字 |
| [第9.5次實驗：獨立讀數與可續作出口](research/experiment-9-5/closure-report.md) | 增加同儕與審核角色後，核准紀錄與合法出口怎樣影響資料送達？ | 正式批次200次運行（每格10次，屬探索規模）、第二份讀數的來源、審核員誤讀、上限轉交與指標更正；原稿的待封存狀態照錄 |
| [第13次實驗：既有證據複核與結案](research/experiment-13/closure-report.md) | 在資訊、審查與排程條件改變時，多角色協作在哪裡中斷，又曾如何接續？ | 真模型與離線結果的區分、一次外加澄清配對、第二回合三筆 Live 及模擬目標達成但流程未收斂的限制；另列先前跨實驗誤引的更正。 |

第5次投稿作品將理論轉成一套具體的事件應對介面，現有驗證是單一作者、非盲的紙上推演。第9次正式批次中，第二季首次交件含舊資料：停用公告條件（癸格）12/20次，其他三格合計4/60次。第9.5次正式批次中，負責人在場時，核准紀錄被指定且獨立的兩格（8b、8c）舊資料送達0/20次；其餘三格（8a、8d、8e）合計11/30次。第13次實驗建立了來源契約、權限與雙視窗排程的多角色沙盒。v0.2.1的一筆Live曾走通合法替代路徑並達成模擬目標，但未在預算內自然停止；現有結果不足以宣稱一般能力或行為邊界已全部測清。

第14次實驗已結案，見重力帳的 [E14 結案補錄](research/research-ledger.md#e14-closure-20261113)。其後的工作轉向治理演算法：把定位、AB 判準與現實回流寫成可執行的核心與沙盒，目前仍在開發與交叉審查中，尚未公開；完成初版後會在本庫另行說明。

## 取用實作材料

- [第5次 YAML 範本與教學填例](research/experiment-5/templates/README.md)：兩份原附錄空白模板、兩份明標事後重建的填例；用於理解與填寫交接內容，不會執行動作。
- [第9.5次固定紀錄離線核對包](research/experiment-9-5/offline-verification/README.md)：原歷史程式、設定、23次選欄軌跡、200次摘要與事後核對工具。使用 Python 標準函式庫，一條命令免費離線檢查，不需要金鑰。
- [第13次既有證據複核與結案說明](research/experiment-13/closure-report.md)：公開結果、主要更正及可查核範圍。完整原碼、測試集與執行紀錄尚未隨本庫提供。

## 作品中的貢獻與證據

我提出問題、方向與語義判準，並在研究過程中校正轉譯、判讀結果及決定取捨。AI協作整理材料、提出可修正的解釋，並參與程式實作、分析與技術表達；各文件保留具體分工。

讀者可以核對三種工作：概念如何變成可操作的規格；規格在某個世界中產生了什麼行為；新證據如何促使原來的主張收窄或修正。作者確認、AI同意或作品評論，各有其用途，均不替代獨立實驗證據。

相關反例與來源在報告編輯註及 [重力帳第六章](research/research-ledger.md#ledger-ch-6) 可查。

## 從研究回到生命導航學

這些實驗是讓生命導航學接受具體檢查的一條路。真正持續追問的仍是：人在變動中如何看清關係、讓理解進入行動，又如何知道何時應續行、轉向或放下原來的方法？

可以閱讀 [《生命導航學》體系發展參照地圖](docs/system-development-map.md)，或沿 [重力帳的全鏈綜合](research/research-ledger.md#ledger-ch-1) 閱讀這條路如何形成。希望進一步討論理念、作品表達或跨域實作的讀者，也可由此找到彼此能接續的問題。

## 文件與版本

最近更新日期：**2026-11-20**（AI 版奠基文件 v0.7、體系地圖 v0.17）。
- [《生命導航學》體系發展參照地圖 v0.17](docs/system-development-map.md)：校正「選樞」措辭，寫明樞不是事先挑的，而是在區分的那一刀中浮到前景，並補一段區分與生成相依；其餘不變。
- [《實驗脈絡重力帳》修訂 9](research/research-ledger.md#return-20261120)：補錄 E14 之後治理演算法階段的位置，以及由演算法卡點回流母理論的一次轉向；非新實驗。
- [《AI版奠基文件》先讀這裡](docs/ai-foundation-guide.md)：新增兩頁的閱讀入口，說明核心主張、與常見做法的差別、證據界線與依目的的讀法；不新增理論或實驗結果。
- [《AI版奠基文件》v0.7（Claude 版）](docs/ai-foundation.md)：補入區分與生成相依、樞在流動中以前景顯形、修補後如何與現實對帳、每個位置讀自己的方向（新增 §13.7），以及治理演算法「第一步接上、後面停住」的共同形狀（附錄二第七節）；取代同日先行公開的三處補記，不新增實驗結果。

先前更新：
- 更新《生命導航學》體系發展參照地圖至 v0.16 公開閱讀版（`docs/system-development-map.md`）；
- 《AI版奠基文件》同步桌機 v0.6 的 E13 證據邊界修訂（`docs/ai-foundation.md`）；這是既有修訂的公開同步，不是 E14 新增理論；
- 《實驗脈絡重力帳》新增 [E14 結案補錄](research/research-ledger.md#e14-closure-20261113)，保留已完成的工程與行為觀察，不作治理零件效益或整體理論成敗的判定；E13 相關段落維持 2026-11-10 複核更正（`research/research-ledger.md`）；
- 第13次報告更新為既有證據複核公開修訂版，附第二回合詳表（`research/experiment-13/closure-report.md`）；
- 同步更正來源索引、地圖與AI版奠基文件的E13證據定位，泛化不必要的私人情境；保留既有署名與Git歷史。

來源版本、提供範圍與歷史更正見 [來源與可查核範圍](SOURCE_STATUS.md)。

## 授權

本庫的文件與圖片以 [Creative Commons 姓名標示 4.0 國際（CC BY 4.0）](https://creativecommons.org/licenses/by/4.0/deed.zh-hant) 授權，全文見 [LICENSE](LICENSE)。只要標示出處，即可分享、翻譯、改寫與再利用，包括商業用途。建議標示方式：Baki Cheng，《生命導航學 Living Navigation》研究庫（living-navigation-research-public），並附原文連結。

文中引用的他人著作、公開論文與外部網頁，依其原有授權，不在本授權範圍內。日後若公開程式碼，另行標示其授權。
