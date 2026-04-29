---
metric_id: "M-TOPIC-MV-004"
metric_name: "移动T+n停机率"
domain: "专题"
category: "移动"
period: "月"
cdap_flow: "移动入网质量模型"
owners:
  business: "张建新"
  technical: "陈绮慧"
source_file: "移动.md"
---

# [M-TOPIC-MV-004] 移动T+n停机率

## 指标属性

| 字段 | 值 |
|------|-----|
| 业务板块 | 专题 |
| 业务分类 | 移动 |
| 统计周期 | 月 |
| 业务口径责任人 | 张建新 |
| 技术口径责任人 | 陈绮慧 |
| CDAP生产流程 | 移动入网质量模型 |

## 业务口径

(未填写)

## 技术口径（SQL）

```sql
SELECT month_id AS `统计月份`,rw_month AS `入网月份T`,tn_id AS `T+n的n`
,count(distinct serv_id) AS `分母：T月入网的移动号码数`
,count(distinct case when is_stop_tn=1 then serv_id end) AS `分子：分母中的用户在入网T+n月已停机的用户数`
FROM zone_gz.view_分局缩写（th,lw,py....）_ads_yz_yd_ydrwzt_list
WHERE month_id=202603 --统计月份
GROUP BY month_id,rw_month,tn_id
;
```

## 参数化建议

- 将固定月份参数化（如 `par_month_id`、`month_id`、`day_id`）。
- 若涉及日期范围，建议统一为 `${start_day}` / `${end_day}`。

## 依赖说明

- 相关表请通过 `metric_table_map.md` 与 `metric_bridge.md` 映射到 A 层表文档。
