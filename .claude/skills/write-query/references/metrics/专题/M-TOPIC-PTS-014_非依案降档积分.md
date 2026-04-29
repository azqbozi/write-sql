---
metric_id: "M-TOPIC-PTS-014"
metric_name: "非依案降档积分"
domain: "专题"
category: "积分"
period: "日/月/年"
cdap_flow: "降档清单"
owners:
  business: "邓颖科"
  technical: "朱创伟"
source_file: "积分.md"
---

# [M-TOPIC-PTS-014] 非依案降档积分

## 指标属性

| 字段 | 值 |
|------|-----|
| 业务板块 | 专题 |
| 业务分类 | 积分 |
| 统计周期 | 日/月/年 |
| 业务口径责任人 | 邓颖科 |
| 技术口径责任人 | 朱创伟 |
| CDAP生产流程 | 降档清单 |

## 业务口径

(未填写)

## 技术口径（SQL）

```sql
SELECT subst_name,branch_name,sum(score) jf -- 非依案积分
FROM view_ads_yz_jd_list WHERE par_month_id=202604
AND 
  jd_scene NOT IN ('拆挽场景', '续约场景', '跨月受理')
  AND jd_prod_offer_code NOT IN (
    'YD5G03-030-1-1',
    'YD4G03-268-1-1',
    'YD0203-A114-1-1',
    'YD4G03-587-1-2',
    'YD4G03-587-1-1',
    'YD4G03-B646-1-1',
    'YD4G03-529-1-1'
  )
```

## 参数化建议

- 将固定月份参数化（如 `par_month_id`、`month_id`、`day_id`）。
- 若涉及日期范围，建议统一为 `${start_day}` / `${end_day}`。

## 依赖说明

- 相关表请通过 `metric_table_map.md` 与 `metric_bridge.md` 映射到 A 层表文档。
