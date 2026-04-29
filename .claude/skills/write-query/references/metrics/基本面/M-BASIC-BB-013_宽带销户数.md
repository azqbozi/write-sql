---
metric_id: "M-BASIC-BB-013"
metric_name: "宽带销户数"
domain: "基本面"
category: "宽带"
period: "月/年"
cdap_flow: "宽带离网报表+531离网数据"
owners:
  business: "林正欣"
  technical: "陈浩南"
source_file: "宽带.md"
---

# [M-BASIC-BB-013] 宽带销户数

## 指标属性

| 字段 | 值 |
|------|-----|
| 业务板块 | 基本面 |
| 业务分类 | 宽带 |
| 统计周期 | 月/年 |
| 业务口径责任人 | 林正欣 |
| 技术口径责任人 | 陈浩南 |
| CDAP生产流程 | 宽带离网报表+531离网数据 |

## 业务口径

(未填写)

## 技术口径（SQL）

```sql
SELECT  sum(case when is_cz_last=0 and is_cancel_user=0 and is_new_user=0 and is_cz=1 then -1 else 1 end)
FROM view_ads_yz_tb_comm_cm_all_final
WHERE  par_month_id =202603
AND ((is_cz_last=0 AND is_cancel_user=0 AND is_new_user=0 AND is_cz=1)--非转计
OR (is_cz_last=1 AND (is_wl_cancel_user=1 or is_cz=0)))--物理拆机、计转非
AND prod_type=40 AND kd_desc='普通宽带'
AND  prod_id NOT IN (48,52,57,600039000,1100)  --剔除专线，城域网
AND COALESCE(kd_prod_offer_id,'-1')  NOT IN ('500046067' ) --剔除快捷宽带主账号
;
```

## 参数化建议

- 将固定月份参数化（如 `par_month_id`、`month_id`、`day_id`）。
- 若涉及日期范围，建议统一为 `${start_day}` / `${end_day}`。

## 依赖说明

- 相关表请通过 `metric_table_map.md` 与 `metric_bridge.md` 映射到 A 层表文档。
