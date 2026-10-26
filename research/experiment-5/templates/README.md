# 第5次附錄可取用範本

兩個template.yaml逐字抽自已核投稿全文附錄C、D，未改欄位。兩個posthoc-example.yaml為2026-10-26依第5節表2及5.2決策重建的教學填例，不是原實驗輸出、真實授權或自動沙盒。未知人員、日期、endpoint均未猜填；authorization例明示NOT VALID、NOT ISSUED。填例採JSON語法（YAML 1.2相容），可用Python標準json直接讀取。

原報告：[第5次投稿全文](../report.md)。這些檔案不會自行發出請求或執行動作。

## 使用方法

下載所需的 `.template.yaml` 後另存副本填寫；對照同名 `.posthoc-example.yaml` 理解欄位。空白模板不是授權，填完也不會自動產生授權或執行動作。

填例使用 JSON 語法，是 YAML 1.2 的子集；可用 `python -m json.tool unknown-packet.posthoc-example.yaml` 或 `python -m json.tool authorization-ticket.posthoc-example.yaml` 檢查。空白原模板是一般 YAML，不適用這兩條 JSON 命令。四份文件均無網路或 API 呼叫，不需要金鑰；這是交接文件配套，不是自動執行沙盒。
