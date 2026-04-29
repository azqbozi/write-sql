---
metric_id: "M-BASIC-MV-004"
metric_name: "合约T+n出账率"
domain: "基本面"
category: "移动"
period: "月"
cdap_flow: "移动日报"
owners:
  business: "邱礼佳"
  technical: "林泳洁"
source_file: "移动.md"
---

# [M-BASIC-MV-004] 合约T+n出账率

## 指标属性

| 字段 | 值 |
|------|-----|
| 业务板块 | 基本面 |
| 业务分类 | 移动 |
| 统计周期 | 月 |
| 业务口径责任人 | 邱礼佳 |
| 技术口径责任人 | 林泳洁 |
| CDAP生产流程 | 移动日报 |

## 业务口径

(未填写)

## 技术口径（SQL）

```sql
SELECT count(distinct a.serv_id) as cnt_xrw --入网用户数【分母】
,count(distinct case when b.is_cz=1 then a.serv_id else null end) as cnt_cz_t12 --出账用户数【分子】
,count(distinct case when b.is_cz=1 then a.serv_id else null end) /count(distinct a.serv_id) --出账率
FROM 
(SELECT serv_id,
case when channel_subtype_2011='电信员工协销' AND subst_name='市分公司本部' then 1 else 0 end as is_tc
FROM 
view_dwm_yz_cm_cdma_hy_final
 WHERE par_month_id=202304   --入网月
           AND is_new_user=1  --锁定当月新入网用户
) a
LEFT JOIN 
(SELECT serv_id,is_cz
FROM 
view_ads_yz_tb_comm_cm_all_final
WHERE prod_id in (3204,3205) --锁定移动产品
AND par_month_id=202404  --统计月(如果是当前月就是最新一天，如果是历史月就是最后一天) 
) b
on a.serv_id=b.serv_id
WHERE a.is_tc=0 --剔除渠道小类为'电信员工协销'且划小局向为'市分公司本部'的号码
;
```

## 参数化建议

- 将固定月份参数化（如 `par_month_id`、`month_id`、`day_id`）。
- 若涉及日期范围，建议统一为 `${start_day}` / `${end_day}`。

## 依赖说明

- 相关表请通过 `metric_table_map.md` 与 `metric_bridge.md` 映射到 A 层表文档。
