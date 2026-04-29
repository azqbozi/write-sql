---
metric_id: "M-BASIC-MV-016"
metric_name: "移动当月携入号码数"
domain: "基本面"
category: "移动"
period: "月"
cdap_flow: "jm每日流程_月重跑"
owners:
  business: "李小院"
  technical: "吉敏"
source_file: "移动.md"
---

# [M-BASIC-MV-016] 移动当月携入号码数

## 指标属性

| 字段 | 值 |
|------|-----|
| 业务板块 | 基本面 |
| 业务分类 | 移动 |
| 统计周期 | 月 |
| 业务口径责任人 | 李小院 |
| 技术口径责任人 | 吉敏 |
| CDAP生产流程 | jm每日流程_月重跑 |

## 业务口径

(未填写)

## 技术口径（SQL）

```sql
SELECT count(serv_id) 
FROM zone_gz.view_ads_yz_yd_xhzw_list 
WHERE par_month_id='202603'   --统计月份
AND xz_type='携入'
;
```

## 参数化建议

- 将固定月份参数化（如 `par_month_id`、`month_id`、`day_id`）。
- 若涉及日期范围，建议统一为 `${start_day}` / `${end_day}`。

## 依赖说明

- 相关表请通过 `metric_table_map.md` 与 `metric_bridge.md` 映射到 A 层表文档。
