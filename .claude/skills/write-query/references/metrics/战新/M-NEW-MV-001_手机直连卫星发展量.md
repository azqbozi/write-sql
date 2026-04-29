---
metric_id: "M-NEW-MV-001"
metric_name: "手机直连卫星发展量"
domain: "战新"
category: "移动"
period: "日/月/年"
cdap_flow: "手机直连卫星发展模型"
owners:
  business: "李小院"
  technical: "林泳洁"
source_file: "移动.md"
---

# [M-NEW-MV-001] 手机直连卫星发展量

## 指标属性

| 字段 | 值 |
|------|-----|
| 业务板块 | 战新 |
| 业务分类 | 移动 |
| 统计周期 | 日/月/年 |
| 业务口径责任人 | 李小院 |
| 技术口径责任人 | 林泳洁 |
| CDAP生产流程 | 手机直连卫星发展模型 |

## 业务口径

(未填写)

## 技术口径（SQL）

```sql
SELECT count(distinct acc_nbr)
FROM view_dwm_yz_zlwx_list_day_final
WHERE data_type='offer' 
AND date_format(create_date,'yyyyMM') = '202603'
AND day_id='20260331'
AND corp_id='200';
```

## 参数化建议

- 将固定月份参数化（如 `par_month_id`、`month_id`、`day_id`）。
- 若涉及日期范围，建议统一为 `${start_day}` / `${end_day}`。

## 依赖说明

- 相关表请通过 `metric_table_map.md` 与 `metric_bridge.md` 映射到 A 层表文档。
