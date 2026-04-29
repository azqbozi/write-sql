# 降档清单(ads_yz_jd_list)


---

## 字段说明

### 基础字段

| 字段 | 字段含义 | 标签周期 | 字典值 | 说明 |
|------|---------|---------|-------|------|
| new_mix_type_relat_id | varchar(100) |  |  | 套餐标识 |
| serv_id | decimal(22,0) |  |  | 设备标识 |
| acc_nbr | varchar(40) |  |  | 号码 |
| prod_id | decimal(22,0) |  |  | 产品id |
| disc_name | varchar(20) |  |  | 产品名称 |
| is_vice_card | decimal(2,0) |  |  | 是否副卡 |
| new_mix_type_prod | 融合套餐类型产品 |  |  |  |
| mix_first_open_date | 入网时间 |  |  |  |
| cust_id | decimal(22,0) |  |  | 产权客户ID |
| cust_nbr | varchar(30) |  |  | 产权客户编码 |
| cust_name | varchar(1000) |  |  | 产权客户名称 |
| serv_grp_type | varchar(10) |  |  | 服务分群 |
| subst_id | decimal(22,0) |  |  | 县分id |
| branch_id | decimal(22,0) |  |  | 营服id |
| subst_name | 县分名称 |  |  |  |
| branch_name | 营服名称 |  |  |  |
| cell_id | decimal(22,0) |  |  | 网格单元id |
| cell_code | varchar(20) |  |  | 网格单元编码 |
| cell_name | 网格单元名称 |  |  |  |
| grid_id | decimal(22,0) |  |  | 划小责任田ID |
| grid_code | varchar(20) |  |  | 责任田编码 |
| grid_name | 责任田名称 |  |  |  |
| area_id | decimal(22,0) |  |  | 包区id |
| area_name | 包区名称 |  |  |  |
| bg_type | bg类型 |  |  |  |
| bu_type | bu类型 |  |  |  |
| region_type | varchar(100) |  |  | 五大网格 |
| jd_act_type | 降档动作类型 |  |  |  |
| jd_score | decimal(38,2) |  |  | 降档动作积分 |
| jd_zr_rule | 降档责任规则 |  |  |  |
| jd_zr_staff_name | 降档责任人 |  |  |  |
| jd_zr_subst_name | 降档责任分局 |  |  |  |
| jd_zr_branch_name | 降档责任营服 |  |  |  |
| jd_zr_org_name | 降档责任机构 |  |  |  |
| jd_zr_channel_type | 降档责任网点类型 |  |  |  |
| jd_action_id | decimal(22,0) |  |  | 降档动作id |
| jd_subs_stat_date | 降档订单状态时间 |  |  |  |
| jd_subs_code | varchar(64) |  |  | 降档订单编码 |
| jd_disc_type | varchar(200) |  |  | 降档套餐类型 |
| jd_msinfo_open_date | 降档实例入网时间 |  |  |  |
| jd_disc_xl | 降档套餐小类2 |  |  |  |
| jd_msinfo_id | 降档实例id |  |  |  |
| jd_prod_offer_id | decimal(22,0) |  |  | 降档销售品id |
| jd_prod_offer_code | varchar(200) |  |  | 降档销售品编码 |
| jd_offer_name | varchar(500) |  |  | 降档销售品名称 |
| jd_action_id2 | decimal(22,0) |  |  | 降档动作id2， |
| jd_subs_stat_date2 | 降档订单状态时间2 |  |  |  |
| jd_subs_code2 | varchar(64) |  |  | 降档订单编码2 |
| jd_disc_type2 | varchar(200) |  |  | 降档套餐类型2 |
| jd_msinfo_open_date2 | 降档实例入网时间2 |  |  |  |
| jd_disc_xl2 | 降档套餐小类2 |  |  |  |
| jd_msinfo_id2 | 降档实例2 |  |  |  |
| jd_prod_offer_id2 | decimal(22,0) |  |  | 降档销售品id2 |
| jd_prod_offer_code2 | varchar(200) |  |  | 降档销售品编码2 |
| jd_offer_name2 | varchar(500) |  |  | 降档销售品名称2 |
| sd_act_type | 升档动作类型 |  |  |  |
| sd_score | decimal(29,2) |  |  | 升档动作积分 |
| sd_zr_rule | 升档责任规则 |  |  |  |
| sd_zr_staff_name | 升档责任揽装人 |  |  |  |
| sd_zr_subst_name |  |  |  |  |
| sd_zr_branch_name |  |  |  |  |
| sd_zr_org_name |  |  |  |  |
| sd_zr_channel_type |  |  |  |  |
| sd_action_id | decimal(22,0) |  |  |  |
| sd_subs_stat_date |  |  |  |  |
| sd_subs_code | varchar(64) |  |  |  |
| sd_disc_type | varchar(200) |  |  |  |
| sd_msinfo_open_date |  |  |  |  |
| sd_disc_xl |  |  |  |  |
| sd_msinfo_id |  |  |  |  |
| sd_prod_offer_id | decimal(22,0) |  |  |  |
| sd_prod_offer_code | varchar(200) |  |  |  |
| sd_offer_name | varchar(500) |  |  |  |
| value02_yhdq | decimal(28,2) |  |  | 当月优惠到期积分 |
| value02_yhdq_lst6 | decimal(28,2) |  |  | 近6个月优惠到期积分 |
| xy_flag | 续约标签 |  |  |  |
| cjwl_flag | 拆机挽留标签 |  |  |  |
| score | decimal(38,2) |  |  | 降档积分 |
| lrr_flag | 零容忍标签 |  |  |  |
| zqjd_flag | 政企团单标签 |  |  |  |
| khts_flag | 客户投诉标签 |  |  |  |
| jd_scene | 降档场景 |  |  |  |
| data_date | 统计日期 |  |  |  |
| load_date | 加载时间 |  |  |  |
| jd_act_date | 降档动作时间 |  |  |  |
| jd_act_date2 | 降档动作时间2 |  |  |  |
| sd_act_date |  |  |  |  |
| kysl_flag | 跨越受理标签 |  |  |  |
| jd_zr_staff_code | 降档责任揽装工号 |  |  |  |
| sd_zr_staff_code | 升档责任工号 |  |  |  |
| dg_salestaff_id | decimal(22,0) |  |  | 订购揽装人id |
| dg_channel_subtype_2011 | 订购渠道小类 |  |  |  |
| dg_salestaff_subst_name | 订购揽装分局 |  |  |  |
| dg_salestaff_branch_name | 订购揽装营服 |  |  |  |
| dg_staff_subst_name | 订购受理局向 |  |  |  |
| dg_staff_branch_name | 订购受理营服 |  |  |  |
| is_gsm | decimal(20,0) |  |  | 是否公司名 |
| tc_score_band | 套餐分档次 |  |  |  |
| last_tc_score | decimal(29,2) |  |  | 上月套餐分 |
| par_month_id | 月份 |  |  |  |
