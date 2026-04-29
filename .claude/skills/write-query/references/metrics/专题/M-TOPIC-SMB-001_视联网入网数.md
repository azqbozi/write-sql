---
metric_id: "M-TOPIC-SMB-001"
metric_name: "视联网入网数"
domain: "专题"
category: "小业务"
period: "日/月/年"
cdap_flow: "视联网发展"
owners:
  business: "林颖斌/陈冠文"
  technical: "钟雨君"
source_file: "小业务.md"
---

# [M-TOPIC-SMB-001] 视联网入网数

## 指标属性

| 字段 | 值 |
|------|-----|
| 业务板块 | 专题 |
| 业务分类 | 小业务 |
| 统计周期 | 日/月/年 |
| 业务口径责任人 | 林颖斌/陈冠文 |
| 技术口径责任人 | 钟雨君 |
| CDAP生产流程 | 视联网发展 |

## 业务口径

(未填写)

## 技术口径（SQL）

```sql
--统计视联网月新增=tykj_yxz+tyyy_yxz+pahy_yxz：
   SELECT subst_id,subst_name,branch_id,branch_name,area_id,area_name,channel_type_2011,channel_subtype_2011,region_type,
 count(distinct case when action_type='tykj_dd' AND prod_id IN (500005461,500005463,600019000) then serv_id else null end)
   + count(distinct case when action_type='tykj_dd' AND attr_value like('%AI%') then serv_id else null end)
   + count(distinct case when action_type='tykj_dd' AND offer_label='TYKJ-AI-202211' then msinfo_id else null end) tykj_yxz, --天翼看家月新增 
    count(distinct case when action_type='tyyy_dd' AND offer_code NOT IN ('ZH0003-432-1-2') then msinfo_id else null end) 
   - count(distinct case when action_type='tyyy_dd' AND offer_label='TYYY-SPHJJM-202211' then msinfo_id else null end) tyyy_yxz, --天翼云眼月新增
    count(distinct case when action_type='pahy_dd' then msinfo_id else null end) pahy_yxz --平安慧眼月新增   
 FROM view_ads_yz_slw_136_list
 WHERE par_month_id='202604'  -- 统计月份
 AND date_format(subs_stat_date,'yyyyMMdd') between '20260401' and '20260415' -- 统计日期范围
 GROUP BY subst_id,subst_name,branch_id,branch_name,area_id,area_name,channel_type_2011,channel_subtype_2011,region_type;
```

## 参数化建议

- 将固定月份参数化（如 `par_month_id`、`month_id`、`day_id`）。
- 若涉及日期范围，建议统一为 `${start_day}` / `${end_day}`。

## 依赖说明

- 相关表请通过 `metric_table_map.md` 与 `metric_bridge.md` 映射到 A 层表文档。
