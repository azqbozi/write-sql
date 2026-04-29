---
layer: D
title: "码值字典 索引"
---

# 码值字典 索引

> **用途**：写 WHERE 过滤遇到状态/动作类字段时，按需查询对应字典；未收录的码值要问用户，不允许猜（参考 [R-006](../cdap_global_rules.md)、[AP-004](../anti_patterns.md)）。
>
> **加载时机**：按需加载（不进 SKILL 启动加载列表）。
>
> **回填规则**：每次确认一个新码值，立即追加到对应字典文件。

## 已收录字典

| 字段 | 文件 | 适用表 | 关键码值 |
|------|------|--------|---------|
| `subs_stat` 订单状态 | [subs_stat.md](subs_stat.md) | 040/041/022 等订单表 | 301200=竣工 |
| `subs_stat_reason` 订单状态原因 | [subs_stat_reason.md](subs_stat_reason.md) | 040/041/022 等订单表 | 1200=撤单, 1300=作废 |
| `action_id` 业务标识 / 动作ID | [action_id.md](action_id.md) | 040/041 等订单表 | 1292=订购, 6200=销售品互换 |

## 待补充字典

随业务积累。建议优先补：
- `state` 服务状态（069 字段，attr_value 表 attr_id='4000000201'）
- `cust_level` 客户级别
- `strat_grp_dl` 客户分类（attr_value 表 attr_id='4000000043'）
- `user_type` 用户类型（attr_value 表 attr_id='94'）
- `payment_type` 付费类型（attr_value 表 attr_id='4000000200'）
- `wl_cancel_type` 物理拆机业务子类型（attr_value 表 attr_id='400002918'）

> 上述字典在 CDAP 字典维表 `dws_attr_value` / `dws_attr_SPEC` 中有完整对照，按需查表后回填到本目录。
