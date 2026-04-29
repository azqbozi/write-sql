---
metric_id: "M-BASIC-DBL-005"
metric_name: "双线净增线数"
domain: "基本面"
category: "双线"
period: "日/月/年"
cdap_flow: "双线全量清单"
owners:
  business: "董永建"
  technical: "许馨丹"
source_file: "双线.md"
---

# [M-BASIC-DBL-005] 双线净增线数

## 指标属性

| 字段 | 值 |
|------|-----|
| 业务板块 | 基本面 |
| 业务分类 | 双线 |
| 统计周期 | 日/月/年 |
| 业务口径责任人 | 董永建 |
| 技术口径责任人 | 许馨丹 |
| CDAP生产流程 | 双线全量清单 |

## 业务口径

(未填写)

## 技术口径（SQL）

```sql
SELECT prod_desc --双线类型
,subst_name --划小局向
,branch_name --划小营服
,count(case when bh_type='新入网' then serv_id else null end)-count(case when bh_type='拆机' then serv_id else null end) jz_cnt --净增线数（入-拆）
FROM view_ads_yz_sx_qlyz_list
WHERE par_month_id=202604 --统计月份
AND bh_type in ('新入网','拆机')
AND prod_type2 in (60,70)
GROUP BY prod_desc,subst_name,branch_name
;
```

## 参数化建议

- 将固定月份参数化（如 `par_month_id`、`month_id`、`day_id`）。
- 若涉及日期范围，建议统一为 `${start_day}` / `${end_day}`。

## 依赖说明

- 相关表请通过 `metric_table_map.md` 与 `metric_bridge.md` 映射到 A 层表文档。
