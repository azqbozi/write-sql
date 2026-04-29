---
metric_id: "M-BASIC-DBL-008"
metric_name: "存量双线提值积分（高套）"
domain: "基本面"
category: "双线"
period: "日/月/年"
cdap_flow: "双线存量提值折高套"
owners:
  business: "董永建"
  technical: "许馨丹"
source_file: "双线.md"
---

# [M-BASIC-DBL-008] 存量双线提值积分（高套）

## 指标属性

| 字段 | 值 |
|------|-----|
| 业务板块 | 基本面 |
| 业务分类 | 双线 |
| 统计周期 | 日/月/年 |
| 业务口径责任人 | 董永建 |
| 技术口径责任人 | 许馨丹 |
| CDAP生产流程 | 双线存量提值折高套 |

## 业务口径

(未填写)

## 技术口径（SQL）

```sql
SELECT subst_name,branch_name,sum(yz_tz) yz_tz
FROM view_ads_yz_sx_cltz_gt
WHERE par_month_id=202604
AND bh_type='提值'
GROUP BY subst_name,branch_name
;
```

## 参数化建议

- 将固定月份参数化（如 `par_month_id`、`month_id`、`day_id`）。
- 若涉及日期范围，建议统一为 `${start_day}` / `${end_day}`。

## 依赖说明

- 相关表请通过 `metric_table_map.md` 与 `metric_bridge.md` 映射到 A 层表文档。
