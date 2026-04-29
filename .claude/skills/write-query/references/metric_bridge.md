# CDAP 生产流程 → 表结构文档（桥接）

> 将 [metric_table_map.md](metric_table_map.md) 中的「CDAP生产流程」映射到本仓库 **`references/tables/` 下实际存在的 md 文件**。  
> **重要**：本仓库里 `tables/{序号}_*.md` 的**文件名序号**与 [TABLE_INDEX.md](TABLE_INDEX.md) 中「CDAP 清单序号」**并不总一致**（历史转换/两套编号）。找表时建议 **表名 + Hive 表名** 与 [TABLE_INDEX](TABLE_INDEX.md) 交叉验证。  
> 表不在下表时，以 [metrics/INDEX](metrics/INDEX.md) 中该指标的 **技术口径 (SQL)** 的 `FROM` 为准，再在 `tables/` 下按 Hive 表名搜索。

| CDAP生产流程（关键词） | tables/ 中的文件（A 层） | 说明 |
|----------------------|--------------------------|------|
| 日生产 | [tables/069_全业务资料表.md](tables/069_全业务资料表.md) | 移动/宽带等大量日模型 |
| 宽带新装清单 | [tables/062_宽带新装清单.md](tables/062_宽带新装清单.md) | |
| 移动宽带质态监控需求 | [tables/093_移动宽带质态监控多维表-宽带清单.md](tables/093_移动宽带质态监控多维表-宽带清单.md) | 宽带 T+n 等 |
| 净增积分请单 / 净增积分清单 | [tables/007_净增积分清单.md](tables/007_净增积分清单.md) | TABLE_INDEX 中可能记为 63 |
| 发展存量积分清单 | [tables/012_发展存量积分清单.md](tables/012_发展存量积分清单.md) | |
| 台阶收入清单打标 | [tables/101_台阶收入清单.md](tables/101_台阶收入清单.md) | |
| 双线全量清单 | [tables/033_双线全量清单.md](tables/033_双线全量清单.md) | |
| 降档清单 | [tables/104_降档清单.md](tables/104_降档清单.md) | `ads_yz_jd_list` |
| 揽装积分清单 | [tables/081_揽装积分清单.md](tables/081_揽装积分清单.md) | |
| 视联网发展 | [tables/092_视联网发展规模清单.md](tables/092_视联网发展规模清单.md) | |
| FTTR报表 | [tables/002_fttr清单.md](tables/002_fttr清单.md) | |
| 移动日报 | [tables/069_全业务资料表.md](tables/069_全业务资料表.md) | 具体以指标 SQL 为准 |
| 移动续约_移动续约日模型 | [tables/030_移动续约清单.md](tables/030_移动续约清单.md)、[tables/031_移动续约多维表.md](tables/031_移动续约多维表.md) | 以指标 SQL 为准 |
| 移动入网质量模型 | [tables/069_全业务资料表.md](tables/069_全业务资料表.md) | |
| jm每日流程_月重跑 | [tables/069_全业务资料表.md](tables/069_全业务资料表.md) | |
| 商客市场短信 | [tables/058_商客新建档客户清单.md](tables/058_商客新建档客户清单.md) 等 | 以 [metrics/专题/INDEX.md](metrics/专题/INDEX.md) 检索对应 metric_id 后为准 |
| 手机直连卫星发展模型 | — | 以指标技术口径 `FROM` 为准 |
| 资源明细清单生成 | — | 见 [metrics/战新/INDEX.md](metrics/战新/INDEX.md) |
| 宽带离网 / 离网报表 | 视指标 | 可搜 `tables/` 中带「离网」「拆机」的清单 |
| （修改结算）YZSR子流程-1-收入生产 | [tables/097_基本面月清单.md](tables/097_基本面月清单.md)、[tables/048_全量科目级收入.md](tables/048_全量科目级收入.md) 等 | 收入类以指标 SQL 为准 |
| 关于客经收保本地划小数据 | [tables/047_最终版划小收入.md](tables/047_最终版划小收入.md) 等 | 见指标字典-收入 |
| 小微清单2024 | [tables/029_小微清单2024.md](tables/029_小微清单2024.md) | CDAP 清单序号 029 |

## 使用方式

1. 在 `metric_table_map` 中查到某指标的「CDAP生产流程」。  
2. 上表左列**模糊匹配**；打开对应 `tables/` 文件核对 **Hive 表名** 与指标 SQL 是否一致。  
3. 若无行可匹配，在 [metrics/INDEX](metrics/INDEX.md) 打开该指标，以 **技术口径 (SQL)** 为准，再用 `grep` / 搜索在 `tables/` 中找同 Hive 名的 md。



