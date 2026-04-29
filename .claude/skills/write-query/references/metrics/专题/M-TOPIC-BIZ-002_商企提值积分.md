---
metric_id: "M-TOPIC-BIZ-002"
metric_name: "商企提值积分"
domain: "专题"
category: "商企"
period: "日/月/年"
cdap_flow: "商客市场短信"
owners:
  business: "赵璐"
  technical: "谢宇"
source_file: "商企.md"
---

# [M-TOPIC-BIZ-002] 商企提值积分

## 指标属性

| 字段 | 值 |
|------|-----|
| 业务板块 | 专题 |
| 业务分类 | 商企 |
| 统计周期 | 日/月/年 |
| 业务口径责任人 | 赵璐 |
| 技术口径责任人 | 谢宇 |
| CDAP生产流程 | 商客市场短信 |

## 业务口径

(未填写)

## 技术口径（SQL）

```sql
SELECT 
sum(case when date_format(subs_stat_day,'yyyyMM')=202603 AND jz_points_zh>jz_points_ryzh AND rh_type_ykj NOT IN ('新宽带新移动') then jz_points_zh-jz_points_ryzh else null end) as value2
FROM view_ads_yz_shangqi_rw_list 
where par_month_id=202603;
```

## 参数化建议

- 将固定月份参数化（如 `par_month_id`、`month_id`、`day_id`）。
- 若涉及日期范围，建议统一为 `${start_day}` / `${end_day}`。

## 依赖说明

- 相关表请通过 `metric_table_map.md` 与 `metric_bridge.md` 映射到 A 层表文档。
