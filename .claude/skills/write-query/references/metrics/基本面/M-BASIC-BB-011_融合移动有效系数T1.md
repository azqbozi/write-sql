---
metric_id: "M-BASIC-BB-011"
metric_name: "融合移动有效系数T1"
domain: "基本面"
category: "宽带"
period: "月/年"
cdap_flow: "融合质态-有效"
owners:
  business: "邱礼佳"
  technical: "陈浩南"
source_file: "宽带.md"
---

# [M-BASIC-BB-011] 融合移动有效系数T1

## 指标属性

| 字段 | 值 |
|------|-----|
| 业务板块 | 基本面 |
| 业务分类 | 宽带 |
| 统计周期 | 月/年 |
| 业务口径责任人 | 邱礼佳 |
| 技术口径责任人 | 陈浩南 |
| CDAP生产流程 | 融合质态-有效 |

## 业务口径

(未填写)

## 技术口径（SQL）

```sql
SELECT (sum(ydyx_points)+sum(ts_points))/count(distinct serv_id) as rate_points --移动有效总系数
FROM view_ads_yz_rpt_ztrh_list_cy a
WHERE par_month_id=202602 --限制月份(号码入网月份) 
AND rh_type_ykj = '新宽带新移动' --t+1仅有新宽新移 
AND coalesce(kd_desc,'-1')<>'校园翼起来' --去除校园宽带
AND coalesce(prod_type3,'-1') not in( 'WiFi宽带','物联宽带','快捷宽带','副宽','门禁宽带','酒店宽带')--去除场景宽带
```

## 参数化建议

- 将固定月份参数化（如 `par_month_id`、`month_id`、`day_id`）。
- 若涉及日期范围，建议统一为 `${start_day}` / `${end_day}`。

## 依赖说明

- 相关表请通过 `metric_table_map.md` 与 `metric_bridge.md` 映射到 A 层表文档。
