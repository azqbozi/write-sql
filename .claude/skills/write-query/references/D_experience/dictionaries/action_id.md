---
layer: D
title: "action_id 业务动作ID 字典"
field_name: "action_id"
applicable_tables: ["dwm_yz_rpt_comm_ba_msdisc_final", "dwm_yz_rpt_comm_ba_subs_final"]
---

# action_id 业务动作ID 字典

> **字段含义**：订单/优惠的业务动作类型 ID。
>
> **字段类型**：数字。
>
> **关键作用**：识别订单是新订购、变更、退订还是销售品互换；发展量统计要选对动作集合。

## 已知码值

| 码值 | 含义 | 是否计入"销售品发展量" |
|------|------|----------------------|
| `1292` | 订购 | ✅ 计入 |
| `6200` | 销售品互换 | ✅ 计入 |

## 销售品发展量过滤模板

```sql
WHERE action_id IN (1292, 6200)
```

## 反 pattern

- ❌ `WHERE action_type = '新订购'`（用术语而非码值，参见 [AP-004](../anti_patterns.md#ap-004-状态动作码值用术语而非码值)）
- ❌ 漏掉 `6200`（只取订购漏掉互换，发展量偏低）

## 待补充

- 退订 / 变更 / 暂停 / 复机 / 销户 等动作 ID 随业务遇到补充
- 注意 `action_id` 与 `action_type`/`action_ex_type` 是不同字段（前者是数字 ID，后者是分类描述）
