---
layer: D
title: "业务术语 → CDAP 概念 映射"
---

# 业务术语 ↔ CDAP 概念 映射表

> **用途**：SKILL 第一步「业务概念解析」必读。把用户口语化术语翻译成 CDAP 标准概念、对应主候选表、关键字段与硬约束。
>
> **回填规则**：用户说了我们没收录的术语，立刻在下表加一行；同义词在「用户说」列用 `/` 分隔。

---

## 核心业务概念

| 用户说 | CDAP 概念 | 主候选表（详见 table_routing.md） | 关键字段 | 注意事项 |
|-------|---------|------------------------------|---------|---------|
| 销售品 / offer | offer（销售品） | 041 优惠订单表（动作）；014 优惠资料表（存量） | `prod_offer_id` ↔ `dws_offer.offer_id` | `dws_offer` 维表 **必加 `city_id=200`**；销售品编码字段是 `prod_offer_code`，名称是 `offer_name` |
| 揽装 / 揽装人 / 销售员 | 销售员 + 销售员所属机构 | 主表自带（041/040/022 等） | `sales_code`（揽装工号）、`sales_man_name`（揽装人姓名）；`salestaff_subst_id`（揽装分局）、`salestaff_branch_id`（揽装营服） | 机构维表 `dwd_yz_dim_org` 用 `org_id` 关联，**`levs=3`=分局、`levs=4`=营服** |
| 划小局向 / 划小分局 | 号码归属机构（落到划小） | 069 全业务资料表 / 040 / 041 等主表 | `subst_id`、`subst_name`、`branch_id`、`branch_name` | 资料表 `dwm_yz_tb_comm_cm_all_final` 按 `serv_id` 关联取名称 |
| 落地局向 | 标准落地机构（不同于划小） | 主表 | `std_subst_id`、`std_subst_name`、`std_branch_id`、`std_branch_name` | 与划小不同，谨慎区分用户语义 |
| 竣工 | 订单状态=竣工 | 任意带 `subs_stat` 的订单表 | `subs_stat='301200'` | **默认作为 `is_jg` 标记列输出，不进 WHERE**；过滤竣工与否要看用户意图 |
| 撤单 / 作废 | 订单状态原因 | 任意带 `subs_stat_reason` 的订单表 | `subs_stat_reason IN ('1200','1300')` | **发展量统计必加 `COALESCE(subs_stat_reason,'-1') NOT IN ('1200','1300')` 排除** |
| 发展量（销售品） | 订购 + 销售品互换 | 041 优惠订单表 | `action_id IN (1292, 6200)` | 1292=订购，6200=销售品互换；要排除撤单作废 |
| 入网量 / 到达量（全业务口径） | 全业务新增/到达/在网/拆机规模 | **069 全业务资料表** `dwm_yz_tb_comm_cm_all_final` | `is_new_user`、`open_date`、`prod_type`、`kd_desc`、`is_cz`、`is_cancel_user`、`is_wl_cancel_user`、`rh_type_ykj`、`is_rh_ykj`、`rh_tc_value`、`prod_type2` | 当用户未限定专项清单，且口径是"全业务/全产品规模"，优先走 069；明细强依赖专项字段时再切专项表 |
| 新装 | 新入网 | 060 移动新装清单 / 062 宽带新装 / 069 `is_new_user=1` | `is_new_user`、`subs_id`、`open_date` | 新装专项表 vs 资料表标志位选择，看用户要不要全字段 |
| 续约 | 合约续约 | 081 移动续约 / 083 宽带续约 / 085/095 双线 | 看具体表 | 不同业务用不同续约表 |
| 拆机 | 物理拆机 | 069 `is_wl_cancel_user=1` 或 086 主宽拆机挽留清单 | `wl_cancel_subs_stat_date`、`hist_create_date` | 物理拆机 ≠ 逻辑销户 |
| 客户名 | 客户名称 | 041 / 022 直接 `cust_name`（不脱敏）；069 `cust_name_tm`（脱敏） | - | 业务范围决定取哪个；公众客群可能仅 069 有 |
| 在网 / 在用 | 在网状态 | 069 `is_cancel_user=0` / `is_online_user=1` | - | 不同口径定义不同，必须看 metrics 字典 |
| 出账 | 当月出账 | 069 `is_cz=1`（当月） / `is_cz_last=1`（上月） | - | 月维度判断 |
| 融合 | 融合套餐 | 069 `rh_type_ykj` / `is_rh_ykj=1` | `rh_tc_id`、`rh_tc_value` | 严口径见 metrics |
| 价值积分 | 当月价值积分 | 069 `jz_points` | - | 已分摊 |

---

## 时间字段语义

| 用户说 | 字段 | 适用表 | 说明 |
|-------|-----|--------|-----|
| 受理时间 | `act_date` | 040/041/022 等订单表 | 订单受理时点 |
| 竣工时间 | `subs_stat_date`（配合 `subs_stat='301200'`） | 040/041/022 等订单表 | 订单状态变为竣工的日期 |
| 开通时间 / 入网时间 | `open_date` | 069 资料表 + 部分订单表 | 服务开通时点 |
| 拆机时间 | `hist_create_date` 或 `wl_cancel_subs_stat_date` | 069 / 拆机清单 | - |
| 携入/携出时间 | `xr_date` / `xc_date` | 069 | - |

---

## 客群范围

| 用户说 | 候选主表 |
|-------|---------|
| 公众 | 069 全业务资料表（`serv_grp_type='02'`） |
| 商企 / 政企 | 022 商企入网清单、047 政企移动入网清单 |
| 小微 | 058 小微客户数清单、057 小微 ICT 竣工清单 |
| 全部 | 069 全业务资料表 |

---

## 全量资料表常见案例指标条件（069）

> **适用前提**：用户说"入网量/到达量/在网量/拆机量"且未限定专项产品清单时，优先在 `dwm_yz_tb_comm_cm_all_final` 取数。

| 案例指标 | 条件语句 |
|---------|---------|
| 当月新入网移动号码 | `is_new_user=1 and date_format(open_date,'yyyyMM')='当月' and prod_type=30` |
| 当日新入网主流宽带 | `is_new_user=1 and date_format(open_date,'yyyyMMdd')='当日' and kd_desc='普通宽带'` |
| 当月新发展 129 融合 | `rh_type_ykj='新宽带新移动' and prod_type=40 and COALESCE(prod_type2,-1) not in (50,60,70,80) and is_rh_ykj=1 and rh_tc_value>=129` |
| 当月到达移动号码数 | `prod_type=30 and is_cz=1` |
| 当月在网移动号码数 | `prod_type=30 and is_cancel_user=0` |
| 当月物理拆机宽带数 | `is_wl_cancel_user=1 and prod_type=40` |
