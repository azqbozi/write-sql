---
metric_id: "M-NEW-CLOUD-001"
metric_name: "云桌面台数入网数"
domain: "战新"
category: "云业务"
period: "日/月/年"
cdap_flow: "资源明细清单生成"
owners:
  business: "骆如怡"
  technical: "钟雨君"
source_file: "云业务.md"
---

# [M-NEW-CLOUD-001] 云桌面台数入网数

## 指标属性

| 字段 | 值 |
|------|-----|
| 业务板块 | 战新 |
| 业务分类 | 云业务 |
| 统计周期 | 日/月/年 |
| 业务口径责任人 | 骆如怡 |
| 技术口径责任人 | 钟雨君 |
| CDAP生产流程 | 资源明细清单生成 |

## 业务口径

(未填写)

## 技术口径（SQL）

```sql
--查看政企版某分局/营服的入网量：
SELECT sum(resource_packages_number)
FROM  zone_gz.view_ads_yxc_yhs_mon_final
WHERE  par_month_id = 202604 -- 统计月份
AND yyyymmdd = '20260414' -- 统计日期
AND is_trial_order='0' AND resource_status in ('过期','已释放','正常','无效')
AND (origin_channel = '省公司'  OR  origin_channel = '云省分')
AND (cust_name not like '%中国电信%' OR cust_name = '中国电信股份有限公司广东研究院')
AND tag_name = '云桌面' AND city='广州市'
AND from_unixtime(unix_timestamp(to_date(resource_start_date),'yyyyMMdd'),'yyyyMMdd')>='20230801'
AND from_unixtime(unix_timestamp(to_date(resource_start_date),'yyyyMMdd'),'yyyyMMdd')<='23030806'
AND subst_name='天河分公司'  ---划小分局
AND branch_name='天河环五山政商营销服务中心'  ---划小营服
;
```

## 参数化建议

- 将固定月份参数化（如 `par_month_id`、`month_id`、`day_id`）。
- 若涉及日期范围，建议统一为 `${start_day}` / `${end_day}`。

## 依赖说明

- 相关表请通过 `metric_table_map.md` 与 `metric_bridge.md` 映射到 A 层表文档。
