---
metric_id: "M-TOPIC-MV-008"
metric_name: "单移终补续约率"
domain: "专题"
category: "移动"
period: "月"
cdap_flow: "移动续约_移动续约日模型"
owners:
  business: "邓颖科"
  technical: "陈绮慧"
source_file: "移动.md"
---

# [M-TOPIC-MV-008] 单移终补续约率

## 指标属性

| 字段 | 值 |
|------|-----|
| 业务板块 | 专题 |
| 业务分类 | 移动 |
| 统计周期 | 月 |
| 业务口径责任人 | 邓颖科 |
| 技术口径责任人 | 陈绮慧 |
| CDAP生产流程 | 移动续约_移动续约日模型 |

## 业务口径

(未填写)

## 技术口径（SQL）

```sql
SELECT
,count(case when disc_type_dl='终端补贴' AND yd_prod_type1='后付费单产品' AND (disc_grp_type='公众' or (disc_grp_type='政企'AND serv_type='个人名')) then msobjgrp_id end)  --分母
,count(case when disc_type_dl='终端补贴' AND yd_prod_type1='后付费单产品' AND (disc_grp_type='公众' or (disc_grp_type='政企'AND serv_type='个人名')) AND xy_state='已续约' then msobjgrp_id end)  --分子
FROM zone_gz.view_分局缩写（th,lw,py....）_ads_yz_ydxy_daily_list
WHERE subst_id=划小局向id
AND month_id=202603 --统计月份
AND limit_month=202603 --到期月份
;
```

## 参数化建议

- 将固定月份参数化（如 `par_month_id`、`month_id`、`day_id`）。
- 若涉及日期范围，建议统一为 `${start_day}` / `${end_day}`。

## 依赖说明

- 相关表请通过 `metric_table_map.md` 与 `metric_bridge.md` 映射到 A 层表文档。
