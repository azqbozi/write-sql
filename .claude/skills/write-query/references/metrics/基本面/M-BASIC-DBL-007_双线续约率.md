---
metric_id: "M-BASIC-DBL-007"
metric_name: "双线续约率"
domain: "基本面"
category: "双线"
period: "日/月/年"
cdap_flow: "双线清单"
owners:
  business: "董永建"
  technical: "许馨丹"
source_file: "双线.md"
---

# [M-BASIC-DBL-007] 双线续约率

## 指标属性

| 字段 | 值 |
|------|-----|
| 业务板块 | 基本面 |
| 业务分类 | 双线 |
| 统计周期 | 日/月/年 |
| 业务口径责任人 | 董永建 |
| 技术口径责任人 | 许馨丹 |
| CDAP生产流程 | 双线清单 |

## 业务口径

(未填写)

## 技术口径（SQL）

```sql
--最新续约率（最新状态更新至limit_month+2，即延迟2个月以上续约的号码无法统计到已续约）
SELECT prod_desc --双线类型
,limit_month --到期月份
,subst_name --局向
,branch_name --营服
,count(serv_id) dq_cnt --到期数量
,count(case when xy_desc='已续约' then serv_id else null end) xy_cnt --续约数量
,count(case when xy_desc='已续约' then serv_id else null end)/count(serv_id) xuyue_lv--续约率
FROM view_ads_yz_sx_xy_list_all
WHERE limit_month=202604 --到期月
GROUP BY prod_desc,limit_month,subst_name,branch_name
;

--历史时间点续约率（需要限制拍照月份T，可取到期月份范围T-2~T+6）
SELECT case when prod_type2=60 then '互联网专线' else '组网专线' end prod_desc --双线类型
,limit_month --到期月份
,subst_name --局向
,branch_name --营服
,count(serv_id) dq_cnt --到期数量
,count(case when xy_desc='已续约' then serv_id else null end) xy_cnt --续约数量
,count(case when xy_desc='已续约' then serv_id else null end)/count(serv_id) xuyue_lv--续约率
FROM view_ads_yz_sx_xy_list
WHERE par_month_id=202603 --拍照月（T）
AND limit_month=202603 --到期月（可取数范围T-2~T+6）
GROUP BY case when prod_type2=60 then '互联网专线' else '组网专线' end,limit_month,subst_name,branch_name
;
```

## 参数化建议

- 将固定月份参数化（如 `par_month_id`、`month_id`、`day_id`）。
- 若涉及日期范围，建议统一为 `${start_day}` / `${end_day}`。

## 依赖说明

- 相关表请通过 `metric_table_map.md` 与 `metric_bridge.md` 映射到 A 层表文档。
