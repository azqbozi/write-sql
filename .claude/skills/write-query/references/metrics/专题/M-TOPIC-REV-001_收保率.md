---
metric_id: "M-TOPIC-REV-001"
metric_name: "收保率"
domain: "专题"
category: "收入"
period: "月/年"
cdap_flow: "关于客经收保本地划小数据"
owners:
  business: "林彩虹"
  technical: "谢宇"
source_file: "收入.md"
---

# [M-TOPIC-REV-001] 收保率

## 指标属性

| 字段 | 值 |
|------|-----|
| 业务板块 | 专题 |
| 业务分类 | 收入 |
| 统计周期 | 月/年 |
| 业务口径责任人 | 林彩虹 |
| 技术口径责任人 | 谢宇 |
| CDAP生产流程 | 关于客经收保本地划小数据 |

## 业务口径

(未填写)

## 技术口径（SQL）

```sql
--收保率=（（存量收入）/统计月份）*12/拍照收入
--存量收入
SELECT sum(charge_year_2023) AS cl_sr 
FROM view_ads_clzz_list 
WHERE par_month_id=202603;

--拍照收入
SELECT sum(charge_year_2023) AS cl_sr 
FROM view_ads_pzkh_list 
WHERE par_month_id=202512;
```

## 参数化建议

- 将固定月份参数化（如 `par_month_id`、`month_id`、`day_id`）。
- 若涉及日期范围，建议统一为 `${start_day}` / `${end_day}`。

## 依赖说明

- 相关表请通过 `metric_table_map.md` 与 `metric_bridge.md` 映射到 A 层表文档。
