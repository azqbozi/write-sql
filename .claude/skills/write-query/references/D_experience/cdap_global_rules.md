---
layer: D
title: "CDAP 全局硬约束"
---

# CDAP 全局硬约束

> **用途**：SKILL 第六步「写 SQL」时主动套用。每条规则在生产环境必须遵守，违反必出错或漏数据。
>
> **回填规则**：发现一条新硬规则，立即追加到对应章节末尾。

---

## R-001 全省维表必加 city_id=200

**对象表**：
- `dws_crm_cfguse.dws_offer`（销售品维表）
- `dws_crm_cfguse.dws_product`（产品维表）
- 其他全省级维表（用户在场景中明确）

**写法模板**：
```sql
LEFT JOIN (
    SELECT offer_id, prod_offer_code, offer_name
    FROM dws_crm_cfguse.dws_offer
    WHERE city_id = 200
) f ON a.prod_offer_id = f.offer_id
```

**违反代价**：跨城重号销售品错配，结果行数错、销售品名错。

---

## R-002 动作类统计必排撤单作废

**对象**：发展量 / 订购量 / 受理量 / 竣工量 等所有"动作类"统计。

**写法模板**：
```sql
WHERE COALESCE(subs_stat_reason, '-1') NOT IN ('1200','1300')
```

- `1200` = 撤单
- `1300` = 作废
- COALESCE 兜底防 NULL 漏过滤

**违反代价**：发展量虚高（包含已撤回订单）。

---

## R-003 机构维表 JOIN 用 org_id + levs

**对象表**：`dwd_yz_dim_org` 或视图 `view_yz_dwd_yz_dim_org`

**写法模板**（揽装局向 / 营服两级关联）：
```sql
LEFT JOIN dwd_yz_dim_org lz_subst
       ON a.salestaff_subst_id  = lz_subst.org_id
      AND lz_subst.levs = 3                       -- 分局
LEFT JOIN dwd_yz_dim_org lz_branch
       ON a.salestaff_branch_id = lz_branch.org_id
      AND lz_branch.levs = 4                      -- 营服
```

**关键点**：
- 用 `org_id` 关联，**不是** `subst_id`/`branch_id`
- `levs=3` 分局，`levs=4` 营服
- 别名要用对，避免 [AP-009](anti_patterns.md#ap-009-多次-join-on-别名错位)

**违反代价**：JOIN 不上 / 错配。

---

## R-004 表名前缀以生产现网为准

**已知前缀漂移**：

| 表 md | md 写的 hive_name | 生产现网实际名 |
|------|------------------|---------------|
| 069 全业务资料表 | `ads_yz_tb_comm_cm_all_final` | `dwm_yz_tb_comm_cm_all_final` |
| 041 优惠订单表 | `zone_gz_yz.dwm_yz_rpt_comm_ba_msdisc_final` | `dwm_yz_rpt_comm_ba_msdisc_final`（无 schema 前缀） |

**强制规则**：
- A 层 md 的 `hive_name` 仅供参考
- 落 SQL 前**必须在回答中显式列出"我准备使用 X 库 Y 表"，让用户校对**
- 校对后用户给的生产名是最终权威

**违反代价**：表不存在 / 错误库读写。

---

## R-005 "是否X" 标志默认输出，不进 WHERE

**对象**：业务上的标志位（如 是否竣工、是否在网、是否新入网、是否物理拆机）。

**写法模板**：
```sql
SELECT
    CASE WHEN subs_stat = '301200' THEN 1 ELSE 0 END AS is_jg,
    ...
FROM ...
WHERE ...   -- 不要把 is_jg 的判定条件放到 WHERE 里
```

**例外**：用户明确说"只看竣工的 / 只看新入网的"才放 WHERE。

**违反代价**：把用户想看的明细全部过滤掉。

---

## R-006 状态/动作码值禁止用通用术语

**对象**：所有状态/动作字段（subs_stat / action_id / action_type / subs_stat_reason / state / cust_level / strat_grp_dl 等）。

**强制规则**：
- 不允许写 `IN ('竣工','正常','新订购')` 等中文术语
- 必须用码值，码值查 [dictionaries/](dictionaries/)
- dictionaries 里没收录的，**问用户**，不允许猜

**违反代价**：SQL 跑出 0 行或全部命中。

---

## R-007 客户名取数路径

| 表 | 字段 | 是否脱敏 | 客群覆盖 |
|----|-----|---------|---------|
| 041 优惠订单表 | `cust_name` | 不脱敏 | 全客群（041 直接有此字段） |
| 022 商企入网清单 | `cust_name` | 不脱敏 | 仅商企 |
| 069 全业务资料表 | `cust_name_tm` | 脱敏（长度=2 脱敏最后一位，>3 脱敏最后两位） | 全客群 |

**优先级**：用户没明说脱敏需求 → 优先用主表自带的 `cust_name`，省 JOIN。

---

## R-008 分区裁剪前必看 partition_keys

- 表 md frontmatter 的 `partition_keys` 字段未标注 → 不要加 `par_month_id IN (...)` 等分区裁剪条件
- 强行加可能导致：分区不存在 / 误杀数据 / SQL 报错

**对照查询**：
```yaml
# 表 md frontmatter
partition_keys: ["par_month_id"]   # 这才能加 par_month_id 过滤
```

---

## R-009 明细 vs 汇总分清

**禁止**：
```sql
SELECT acc_nbr, ..., COUNT(1) OVER (PARTITION BY month_id) AS month_cnt   -- 反 pattern
FROM ...
```

**正确**：
- 要明细就纯明细
- 要汇总用 GROUPING SETS / UNION ALL / 单独 query
- 同时要两者，分别输出两段 SQL 或显式 GROUPING SETS

---

## R-010 时间字段语义对齐

| 业务说法 | 字段 | 上下文 |
|---------|-----|--------|
| 受理 | `act_date` | 订单受理 |
| 竣工 | `subs_stat_date` + `subs_stat='301200'` | 订单竣工 |
| 开通 | `open_date` | 服务开通 |
| 拆机 | `hist_create_date` 或 `wl_cancel_subs_stat_date` | 拆机时点 |

**禁止**：把 `open_date` 当 "竣工时间" 使用（资料表 069 没有真竣工时间字段，要从订单类表取 `subs_stat_date`）。
