# 指标层（B）

本目录是唯一的指标字典位置（单份维护）。

| 内容 | 路径 |
|------|------|
| 指标总索引与 90+ 指标列表 | [`INDEX.md`](INDEX.md) |
| 专题指标 | [`专题/`](专题/) |
| 基本面指标 | [`基本面/`](基本面/) |
| 战新指标 | [`战新/`](战新/) |
| 指标名 → CDAP 生产流程 | [`../metric_table_map.md`](../metric_table_map.md) |
| CDAP 流程 → 表文档桥接 | [`../metric_bridge.md`](../metric_bridge.md) |

维护规则：新增或修订指标时，只改 `metrics/` 目录下文件，并同步 `metric_table_map.md` 与 `metric_bridge.md`（若涉及新流程或新表）。

