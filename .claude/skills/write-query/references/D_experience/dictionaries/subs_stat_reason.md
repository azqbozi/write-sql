---
layer: D
title: "subs_stat_reason 订单状态原因 字典"
field_name: "subs_stat_reason"
applicable_tables: ["dwm_yz_rpt_comm_ba_msdisc_final", "dwm_yz_rpt_comm_ba_subs_final", "ads_yz_shangqi_rw_list"]
---

# subs_stat_reason 订单状态原因 字典

> **字段含义**：订单状态变更的原因（解释 `subs_stat` 为何是当前状态）。
>
> **字段类型**：字符串。
>
> **关键作用**：发展量 / 订购量统计**必须排除撤单作废**（参考 [R-002](../cdap_global_rules.md)）。

## 已知码值

| 码值 | 含义 | 处理 |
|------|------|------|
| `1200` | 撤单 | **发展量统计排除** |
| `1300` | 作废 | **发展量统计排除** |

## 强制写法（动作类统计必加）

```sql
WHERE COALESCE(subs_stat_reason, '-1') NOT IN ('1200','1300')
```

`COALESCE` 兜底防 NULL 漏过滤。

## 反 pattern

参见 [AP-006 漏掉撤单作废排除](../anti_patterns.md#ap-006-漏掉撤单作废排除)。

## 待补充

- `1100`、`1400` 等其他原因码值随业务遇到补充
