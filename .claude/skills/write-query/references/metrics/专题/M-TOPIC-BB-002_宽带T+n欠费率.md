---
metric_id: "M-TOPIC-BB-002"
metric_name: "宽带T+n欠费率"
domain: "专题"
category: "宽带"
period: "月"
cdap_flow: "移动宽带质态监控需求"
owners:
  business: "邱礼佳"
  technical: "钟雨君"
source_file: "宽带.md"
---

# [M-TOPIC-BB-002] 宽带T+n欠费率

## 指标属性

| 字段 | 值 |
|------|-----|
| 业务板块 | 专题 |
| 业务分类 | 宽带 |
| 统计周期 | 月 |
| 业务口径责任人 | 邱礼佳 |
| 技术口径责任人 | 钟雨君 |
| CDAP生产流程 | 移动宽带质态监控需求 |

## 业务口径

(未填写)

## 技术口径（SQL）

```sql
--T+1欠费率=value1/value2：
SELECT subst_id,subst_name,concat('T+',mm_diff) as t_bs,
  count(case when is_qf='是' and is_kjzj='否' then serv_id else null end) as value1, -- 总体欠费量
    count(case when is_kjzj='否' then serv_id else null end) as value2 -- 总体量
FROM view_ads_zt_kdx_list
WHERE par_month_id = 202603 -- 统计月份
AND concat('T+',mm_diff) in ('T+0','T+1','T+2','T+3','T+6','T+12') and mm_diff = 1 -- 1个月前入网
GROUP BY subst_id,subst_name,mm_diff;
```

## 参数化建议

- 将固定月份参数化（如 `par_month_id`、`month_id`、`day_id`）。
- 若涉及日期范围，建议统一为 `${start_day}` / `${end_day}`。

## 依赖说明

- 相关表请通过 `metric_table_map.md` 与 `metric_bridge.md` 映射到 A 层表文档。
