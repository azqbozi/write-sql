---
metric_id: "M-TOPIC-PTS-015"
metric_name: "揽装价值积分剔除一次性小微"
domain: "专题"
category: "积分"
period: "月/年"
cdap_flow: "揽装积分清单"
owners:
  business: "李玉凤"
  technical: "朱创伟"
source_file: "积分.md"
---

# [M-TOPIC-PTS-015] 揽装价值积分剔除一次性小微

## 指标属性

| 字段 | 值 |
|------|-----|
| 业务板块 | 专题 |
| 业务分类 | 积分 |
| 统计周期 | 月/年 |
| 业务口径责任人 | 李玉凤 |
| 技术口径责任人 | 朱创伟 |
| CDAP生产流程 | 揽装积分清单 |

## 业务口径

(未填写)

## 技术口径（SQL）

```sql
SELECT channel_subst_name,sum(jz_points_not_ict) jz_points_not_ict
FROM view_ads_yz_lyf_lz 
WHERE par_day_id=20260331  
GROUP BY channel_subst_name
;
```

## 参数化建议

- 将固定月份参数化（如 `par_month_id`、`month_id`、`day_id`）。
- 若涉及日期范围，建议统一为 `${start_day}` / `${end_day}`。

## 依赖说明

- 相关表请通过 `metric_table_map.md` 与 `metric_bridge.md` 映射到 A 层表文档。
