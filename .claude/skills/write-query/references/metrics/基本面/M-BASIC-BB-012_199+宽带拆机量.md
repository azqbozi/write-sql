---
metric_id: "M-BASIC-BB-012"
metric_name: "199+宽带拆机量"
domain: "基本面"
category: "宽带"
period: "日/月/年"
cdap_flow: "宽带离网报表+531离网数据"
owners:
  business: "林正欣"
  technical: "陈浩南"
source_file: "宽带.md"
---

# [M-BASIC-BB-012] 199+宽带拆机量

## 指标属性

| 字段 | 值 |
|------|-----|
| 业务板块 | 基本面 |
| 业务分类 | 宽带 |
| 统计周期 | 日/月/年 |
| 业务口径责任人 | 林正欣 |
| 技术口径责任人 | 陈浩南 |
| CDAP生产流程 | 宽带离网报表+531离网数据 |

## 业务口径

(未填写)

## 技术口径（SQL）

```sql
SELECT count(serv_id)
FROM view_ads_yz_tb_comm_cm_all_final a  
JOIN (
SELECT serv_id,rh_tc_value FROM view_ads_yz_tb_comm_cm_all_final WHERE par_month_id=202512 AND is_rh_ykj=1 AND  is_cancel_user=0 --去年12月在网融合199+
AND prod_type=40 AND kd_desc='普通宽带' AND rh_tc_value>=199
AND prod_id NOT IN (48,52,57,600039000,1100)  --剔除专线，城域网
AND coalesce(kd_prod_offer_id,'-1')  NOT IN ('500046067' ) --剔除快捷宽带主账号
) b  ON a.serv_id=b.serv_id
WHERE par_month_id=202603 --统计月份
AND a.prod_type=40              
AND a.kd_desc='普通宽带'
AND is_cz_last=1 AND is_wl_cancel_user=1 --上月出账的物理拆机号码      
AND coalesce(kd_prod_offer_id,'-1')  NOT IN ('500046067' ) --剔除快捷宽带主账号
;
```

## 参数化建议

- 将固定月份参数化（如 `par_month_id`、`month_id`、`day_id`）。
- 若涉及日期范围，建议统一为 `${start_day}` / `${end_day}`。

## 依赖说明

- 相关表请通过 `metric_table_map.md` 与 `metric_bridge.md` 映射到 A 层表文档。
