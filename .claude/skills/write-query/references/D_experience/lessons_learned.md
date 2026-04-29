---
layer: D
title: "已知陷阱（追加日志）"
---

# 已知陷阱（按时间累积）

> **格式**：每次踩坑追加一段（最新在最上面），五段式：场景 / 错处 / 正确 / 反向更新 / 关联规则。
>
> **回填规则**：每次任务完成必填一段（即便没踩坑也可记"这次差点错的点"）。

---

## 2026-04-28: 销售品发展量陷阱（首批种子）

**场景**：用户要按给定销售品编码看 202509/202510 月发展量，输出号码、客户名、揽装人、竣工时间、划小局向、揽装局向等明细字段。

**错处**：
1. **选错主表**：因 `prod_offer_code/prod_offer_name` 字段名匹配，选了"燃气卫士到达清单"专项表（实际应走 041 优惠订单表）。
2. **A 层 md 名漂移**：069 md 写 `ads_yz_tb_comm_cm_all_final`，生产实际是 `dwm_yz_tb_comm_cm_all_final`；041 md 写 `zone_gz_yz.dwm_yz_rpt_comm_ba_msdisc_final`，生产实际无 schema 前缀。
3. **字段虚构**：直接写了 `prod_offer_code/prod_offer_name/channel_subst_name/channel_branch_name`，没核对所选表是否真有这些字段。
4. **状态码值用术语**：写 `subs_stat IN ('竣工','正常')`，实际生产用 `subs_stat='301200'` + `subs_stat_reason NOT IN ('1200','1300')`。
5. **动作过滤错**：用了 `action_type='新订购'`，实际生产用 `action_id IN (1292,6200)`（订购+销售品互换）。
6. **是否竣工当过滤**：把 is_jg 当 WHERE 条件，实际用户希望保留为标记列。
7. **维表漏 city_id=200**：销售品维表 `dws_offer` 跨城重号，必须按地市过滤。
8. **机构维表 JOIN 字段错位**：用 `salestaff_subst_id` 关联 `subst_id`，应该用 `org_id` + `levs=3/4`。
9. **明细行混汇总**：在明细列里塞 `COUNT(1) OVER (PARTITION BY par_month_id)`。
10. **占位符 SQL 当成完成品**：在 IN 里写 `'销售品编码1','销售品编码2'`。

**正确做法**：041 优惠订单表为主，按 `subs_stat_date` 落 202509/202510，`action_id IN (1292,6200)`，`subs_stat_reason NOT IN ('1200','1300')`；JOIN `dws_offer city_id=200` 取销售品名；JOIN 资料表 `dwm_yz_tb_comm_cm_all_final` 按 serv_id 取划小局向名；JOIN `dwd_yz_dim_org` 两次按 levs=3/4 取揽装局向名；is_jg 作为标记列保留。

**反向更新**：
- `business_glossary.md`：销售品/揽装/竣工/撤单 等 5 行
- `table_routing.md`：销售品类整段（4 行）
- `anti_patterns.md`：AP-001 ~ AP-014 共 14 条
- `cdap_global_rules.md`：R-001 ~ R-010 共 10 条
- `dictionaries/subs_stat.md`：301200=竣工
- `dictionaries/action_id.md`：1292=订购，6200=销售品互换
- `dictionaries/subs_stat_reason.md`：1200=撤单，1300=作废
- `tables/041_优惠订单表.md`：补 `cust_name`、`subs_stat_reason` 字段，标注生产表名
- `tables/069_全业务资料表.md`：frontmatter 标注生产表名漂移

**关联规则**：[AP-001](anti_patterns.md) ~ [AP-014](anti_patterns.md)、[R-001](cdap_global_rules.md) ~ [R-010](cdap_global_rules.md)

---

## 模板（复制下面这块来追加新条目）

```markdown
## YYYY-MM-DD: 简短标题

**场景**：用户的需求是什么

**错处**：
1. 错误 1
2. 错误 2

**正确做法**：怎么做对

**反向更新**：
- `xxx.md`：加了什么
- `yyy.md`：改了什么

**关联规则**：[AP-NNN](anti_patterns.md)、[R-NNN](cdap_global_rules.md)
```
