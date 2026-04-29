---
metric_id: "M-TOPIC-REV-007"
metric_name: "结算分成"
domain: "专题"
category: "收入"
period: "月"
cdap_flow: "（修改结算）YZSR子流程-1-收入生产"
owners:
  business: "吕智"
  technical: "黎可馨"
source_file: "收入.md"
---

# [M-TOPIC-REV-007] 结算分成

## 指标属性

| 字段 | 值 |
|------|-----|
| 业务板块 | 专题 |
| 业务分类 | 收入 |
| 统计周期 | 月 |
| 业务口径责任人 | 吕智 |
| 技术口径责任人 | 黎可馨 |
| CDAP生产流程 | （修改结算）YZSR子流程-1-收入生产 |

## 业务口径

(未填写)

## 技术口径（SQL）

```sql
SELECT sum(a9) AS sh,par_month_id
FROM zone_gz.view_分局缩写（th,lw,py....）_ads_srhx_serv_list_mon
WHERE par_month_id = 202501 --统计月份
GROUP BY par_month_id
;
```

## 参数化建议

- 将固定月份参数化（如 `par_month_id`、`month_id`、`day_id`）。
- 若涉及日期范围，建议统一为 `${start_day}` / `${end_day}`。

## 依赖说明

- 相关表请通过 `metric_table_map.md` 与 `metric_bridge.md` 映射到 A 层表文档。
