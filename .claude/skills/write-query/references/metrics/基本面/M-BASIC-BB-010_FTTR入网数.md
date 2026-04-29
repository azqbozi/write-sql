---
metric_id: "M-BASIC-BB-010"
metric_name: "FTTR入网数"
domain: "基本面"
category: "宽带"
period: "日/月/年"
cdap_flow: "FTTR报表"
owners:
  business: "谢钊铭"
  technical: "陈浩南"
source_file: "宽带.md"
---

# [M-BASIC-BB-010] FTTR入网数

## 指标属性

| 字段 | 值 |
|------|-----|
| 业务板块 | 基本面 |
| 业务分类 | 宽带 |
| 统计周期 | 日/月/年 |
| 业务口径责任人 | 谢钊铭 |
| 技术口径责任人 | 陈浩南 |
| CDAP生产流程 | FTTR报表 |

## 业务口径

(未填写)

## 技术口径（SQL）

```sql
SELECT count(eqpt_sn)
FROM view_dwm_fttr_list
WHERE  par_month_id='202309'
AND substr(create_date,1,6)=par_month_id
```

## 参数化建议

- 将固定月份参数化（如 `par_month_id`、`month_id`、`day_id`）。
- 若涉及日期范围，建议统一为 `${start_day}` / `${end_day}`。

## 依赖说明

- 相关表请通过 `metric_table_map.md` 与 `metric_bridge.md` 映射到 A 层表文档。
