---
metric_id: "M-BASIC-MV-003"
metric_name: "合约129+占比"
domain: "基本面"
category: "移动"
period: "日/月/年"
cdap_flow: "移动日报"
owners:
  business: "李小院"
  technical: "林泳洁"
source_file: "移动.md"
---

# [M-BASIC-MV-003] 合约129+占比

## 指标属性

| 字段 | 值 |
|------|-----|
| 业务板块 | 基本面 |
| 业务分类 | 移动 |
| 统计周期 | 日/月/年 |
| 业务口径责任人 | 李小院 |
| 技术口径责任人 | 林泳洁 |
| CDAP生产流程 | 移动日报 |

## 业务口径

(未填写)

## 技术口径（SQL）

```sql
SELECT count(distinct serv_id) 
FROM view_dwm_yz_cm_cdma_hy_final 
WHERE par_month_id = 202603 --月份
AND data_type = '合约'  --筛选合约
AND sum_date = '20260301'  --日期
AND is_jd='否'  --是否降档
AND is_new_user=1  --是否新用户
AND jz_points >= 129  --是否价值129
;
```

## 参数化建议

- 将固定月份参数化（如 `par_month_id`、`month_id`、`day_id`）。
- 若涉及日期范围，建议统一为 `${start_day}` / `${end_day}`。

## 依赖说明

- 相关表请通过 `metric_table_map.md` 与 `metric_bridge.md` 映射到 A 层表文档。
