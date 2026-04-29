---
layer: D
title: "subs_stat 订单状态 字典"
field_name: "subs_stat"
applicable_tables: ["dwm_yz_rpt_comm_ba_msdisc_final", "dwm_yz_rpt_comm_ba_subs_final", "ads_yz_shangqi_rw_list"]
---

# subs_stat 订单状态 字典

> **字段含义**：订单当前状态。
>
> **字段类型**：字符串/数字（按表存储）。

## 已知码值

| 码值 | 含义 | 备注 |
|------|------|------|
| `301200` | 竣工 | 销售品订单的"成功完成"终态；常作为 `is_jg = CASE WHEN subs_stat='301200' THEN 1 ELSE 0 END` 的判定 |

## 使用模板

```sql
-- 标记是否竣工（推荐：标记列，不进 WHERE）
SELECT CASE WHEN subs_stat = '301200' THEN 1 ELSE 0 END AS is_jg, ...
```

```sql
-- 仅当用户明确"只看竣工"时才进 WHERE
WHERE subs_stat = '301200'
```

## 待补充

其他状态码（受理中/挂起/取消/失败/作废 等）随业务遇到补充。

## 参考

- 通常配合 [`subs_stat_reason`](subs_stat_reason.md) 一起使用：`subs_stat_reason` 给出"为什么是这个状态"
- 未收录码值 → 查 `dws_attr_value` 字典维表，或问用户
