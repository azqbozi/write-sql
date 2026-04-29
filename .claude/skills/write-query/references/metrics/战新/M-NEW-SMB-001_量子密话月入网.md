---
metric_id: "M-NEW-SMB-001"
metric_name: "量子密话月入网"
domain: "战新"
category: "小业务"
period: "月"
cdap_flow: "jm每日流程_月重跑"
owners:
  business: "康晨"
  technical: "吉敏"
source_file: "小业务.md"
---

# [M-NEW-SMB-001] 量子密话月入网

## 指标属性

| 字段 | 值 |
|------|-----|
| 业务板块 | 战新 |
| 业务分类 | 小业务 |
| 统计周期 | 月 |
| 业务口径责任人 | 康晨 |
| 技术口径责任人 | 吉敏 |
| CDAP生产流程 | jm每日流程_月重跑 |

## 业务口径

(未填写)

## 技术口径（SQL）

```sql
SELECT count(serv_id) 
FROM zone_gz.view_ads_yz_lzmh_sl_list_all 
WHERE month_id='202603'   --统计月份
AND is_dx_staff=0
;
```

## 参数化建议

- 将固定月份参数化（如 `par_month_id`、`month_id`、`day_id`）。
- 若涉及日期范围，建议统一为 `${start_day}` / `${end_day}`。

## 依赖说明

- 相关表请通过 `metric_table_map.md` 与 `metric_bridge.md` 映射到 A 层表文档。
