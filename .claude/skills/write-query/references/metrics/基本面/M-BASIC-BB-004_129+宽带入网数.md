---
metric_id: "M-BASIC-BB-004"
metric_name: "129+宽带入网数"
domain: "基本面"
category: "宽带"
period: "日/月/年"
cdap_flow: "日生产"
owners:
  business: "刘丽娜"
  technical: "陈浩南"
source_file: "宽带.md"
---

# [M-BASIC-BB-004] 129+宽带入网数

## 指标属性

| 字段 | 值 |
|------|-----|
| 业务板块 | 基本面 |
| 业务分类 | 宽带 |
| 统计周期 | 日/月/年 |
| 业务口径责任人 | 刘丽娜 |
| 技术口径责任人 | 陈浩南 |
| CDAP生产流程 | 日生产 |

## 业务口径

(未填写)

## 技术口径（SQL）

```sql
SELECT count(serv_id)
FROM view_ads_yz_tb_comm_cm_all_final 
WHERE par_month_id =202603
AND is_cancel_user = 0
AND prod_type = 40
AND kd_desc = '普通宽带'
AND mainstream_net_type = 10
AND is_cz = 1
AND COALESCE(KD_PROD_OFFER_ID,'-1') NOT LIKE '%500046067%' --剔除快捷宽带主账号
AND rh_tc_value >= 129 AND is_rh_ykj = 1 --融合129+ 
;
```

## 参数化建议

- 将固定月份参数化（如 `par_month_id`、`month_id`、`day_id`）。
- 若涉及日期范围，建议统一为 `${start_day}` / `${end_day}`。

## 依赖说明

- 相关表请通过 `metric_table_map.md` 与 `metric_bridge.md` 映射到 A 层表文档。
