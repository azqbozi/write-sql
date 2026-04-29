# fttr清单

- **Hive 表名**: `dwm_fttr_list`
- **视图名**: zone_gz.view_分局缩写（th,lw,py....）
- **业务负责人**: 谢钊铭
- **业支负责人**: 陈浩南
- **分区字段**: par_month_id

---

## 字段说明

| 字段 | 字段类型 | 字段含义 |
|------|---------|---------|
| corp_id | decimal(3,0) | 地市ID |
| create_date | string | 设备创建时间 |
| eqpt_sn | string | 设备串码 |
| serv_id | decimal(30,0) | 号码服务标识 |
| acc_nbr | string | 号码 |
| state | string | 号码状态 |
| cust_id | decimal(20,0) | 客户ID |
| subst_id | decimal(22,0) | 分局ID |
| branch_id | decimal(22,0) | 营服ID |
| area_id | decimal(22,0) | 包区ID |
| is_gz_zwg | decimal(1,0) |  |
| is_mon_gz_cwg_cust | decimal(1,0) |  |
| is_sq_zwg | decimal(1,0) |  |
| is_mon_sq_cwg_cust | decimal(1,0) |  |
| is_fttr_gz | decimal(1,0) | 是否公众版（1：是；0：否） |
| is_fttr_sq | decimal(1,0) | 是否商企版（1：是；0：否） |
| is_fttr | decimal(1,0) | 是否办理FTTR（1：是；0：否） |
| open_date | string | 号码入网时间 |
| is_new_user_m | int | 号码是否当月入网 |
| last_order_item_id | decimal(21,0) | 设备订单ID |
| subs_id | decimal(22,0) | 订单ID |
| subs_code | varchar(64) | 订单编码 |
| act_date | timestamp | 订单受理时间（改设备订单受理时间） |
| subs_stat_date | timestamp | 订单竣工时间（改设备订单竣工时间） |
| sales_code | string | 揽装工号 |
| sales_man_name | string | 揽装人（改设备订单揽装人） |
| channel_type_2011 | string | 渠道大类 |
| channel_subtype_2011 | string | 渠道小类 |
| channel_subtype0_2011 | string | 渠道中类 |
| cust_id2 | decimal(22,0) | 客户ID |
| cust_nbr | varchar(30) | 客户编码 |
| cust_name | varchar(1000) | 客户名 |
| subst_name | string | 分局名 |
| subst_order | int | 分局顺序ID |
| branch_order | int | 营服顺序ID |
| branch_name | string | 营服名 |
| area_name | string | 名区名 |
| is_mdz | string | 是否名单制 |
| bg_type | string | bg类型 |
| region_type | varchar(100) | 五大网格 |
| is_new_user | int | 是否新入网 |
| serv_grp_type_desc | string | 服务分群 |
| six_market_desc | string | 六大细分市场 |
| kd_new | int | 宽带是否新入网 |
| kd_desc | string | 宽带类型 |
| kd_open_date | string | 宽带号码入网时间 |
| speed_value | decimal(10,2) | 速率 |
| is_zw | int | 是否总装维 |
| channel_id | string | 渠道ID |
| is_zwrg | int | 是否装维入格 |
| channel_subtype_2011_zw | string | 渠道装维类别 |
| channel_subtype_2011_zwrg | string | 渠道装维入格类别 |
| std_subst_id | decimal(22,0) | 落地分局ID |
| std_subst_name | string | 落地分局名 |
| std_branch_id | decimal(22,0) | 落地营服ID |
| std_branch_name | string | 落地营服名 |
| salestaff_subst_id | decimal(22,0) | 揽装局向id |
| salestaff_branch_id | decimal(22,0) | 揽装营服id |
| salestaff_channel_id | decimal(22,0) | 揽装网点id |
| xx_salestaff_id1 | string | 第一协销人ID |
| xx_salestaff_code1 | string | 第一协销人编码 |
| xx_salestaff_name1 | string | 第一协销名姓名 |
| xx_salestaff_id2 | string | 第二协销人ID |
| xx_salestaff_code2 | string | 第二协销人编码 |
| xx_salestaff_name2 | string | 第二协销名姓名 |
| bu_type | string | bu类型 |
| staff_id | varchar(20) | 受理人 |
| org_id | decimal(22,0) | 受理机构标识 |
| serv_grp_type | varchar(10) | 服务分群id |
| cell_id | decimal(22,0) | 网格单元id |
| cell_code | varchar(20) | 网格单元编码 |
| salestaff_channel_name | string | 销售点名称 |
| salestaff_channel_nbr | string | 销售点编码 |
| salestaff_subst_name | string | 揽装局向 |
| salestaff_branch_name | string | 揽装营服 |
| is_gsm | int | 是否公司名 |
| cell_name | string | 网格单元名 |
| cell_type | string | 网格单元大类id |
| cell_type_name | string | 网格单元大类 |
| kd_type | string | 宽带类型 |
| is_fttr_sq_desc | string | 是否商企版 |
| is_fttr_gz_desc | string | 是否公众版 |
| org_name | varchar(500) | 受理机构 |
| sum_date | string | 统计日期 |
| Par_month_id | string | 月份 |
| kd_offer_name |  | 宽带主套餐 |
| kd_offer_code |  | 宽带主套餐编码 |
| kd_prod_offer_id |  | 宽带主套餐ID |
| cust_code |  | 直销客户编码 |
| grid_code |  | 责任田编码 |
| salestaff_org_name |  | 揽装机构 |
| channel_subtype_flag |  | 日报渠道小类 |
| fttr_offer_name |  | fttr套餐（本地） |
| fttr_offer_code |  | fttr套餐编码（本地） |
| fttr_prod_offer_id |  | fttr套餐ID（本地） |
| salestaff_area_name | string | 揽装包区 |
| salestaff_area_id | decimal(22,0) | 揽装包区ID |
| mobile_phone | varchar(500) | 客户联系方式 |
| mon_gz_cwg_eqpt_sn | varchar(500) | 同客户公众从网关串码 |
| gz_cwg_num | int | 同客户公众从网关串码数量（本地） |
| mon_sq_cwg_eqpt_sn | varchar(500) | 同客户商企从网关串码 |
| sq_cwg_num | int | 同客户商企从网关串码数量（本地） |
| mkt_res_type_id | decimal(22,0) | 设备ID |
| mkt_res_type_name | string | 设备名 |
| prod_offer_id | decimal(21,0) | FTTR销售品ID（省源） |
| prod_offer_name | string | FTTR销售品名（省源） |
| msobjgrp_id | decimal(21,0) | 套餐实例id |
| attr_inner_cd | string | 暂时没用到 |
| xsd_code | string | 销售点（不包含店中商归集到网厅部分） |
| xsd_code_td | string | 销售点编码_厅店（包含店中商归集到网厅部分） |
| xsy_code | string | 销售员 |
| new_channel_type | decimal(1,0) | 新渠道视图
1  主控-营业厅
2  主控-包区厅
3  主控-包区店
4  社会-终端大店
5  社会-中小门店
6  社会-便利点
7  公众直销
8  10000号
-1 其他 |
| is_maincontrol_channel | decimal(1,0) | 是否主控渠道（1是0否）=营业厅+包区厅+包区店 |
| is_yyt_and_bqt | decimal(1,0) | 是否营业厅（含包区厅） |
| is_quickphone_shop | decimal(1,0) | 是否快电店（1是0否）,该标签不能合并到NEW_CHANNEL_TYPE，与其有交集 |
| is_society_channel | decimal(1,0) | 是否社会渠道(终端大店+中小门店+便利点) |
| num_eqpt_sn_cust_gz | decimal(3,0) | 同客户公众从网关串码数量（省源） |
| num_eqpt_sn_cust_sq | decimal(3,0) | 同客户商企从网关串码数量（省源） |
| is_wapon | decimal(1,0) | 是否wapon 认证 |
| num_kdzx_cust | decimal(3,0) | 同客户名下近60天内新装宽带或专线数量 |
| par_month_id | string | 月份 |
| xsp_sales_id | varchar(100) | 销售品订单揽装人标识 |
| xsp_sales_code | string | 销售品订单揽装人工号 |
| xsp_sales_man_name | string | 销售品订单揽装人 |
| xsp_salestaff_large_class | string | 销售品订单揽装人大类 |
| xsp_salestaff_small_class | string | 销售品订单揽装人小类 |
| xsp_salestaff_org_id | string | 销售品订单揽装人管理机构标识 |
| xsp_salestaff_subst_id | bigint | 销售品订单揽装人所属分局标识 |
| xsp_salestaff_branch_id | bigint | 销售品订单揽装人所属营服标识 |
| xsp_salestaff_subst_name | string | 销售品订单揽装人所属分局 |
| xsp_salestaff_branch_name | string | 销售品订单揽装人所属营服 |
| xsp_salestaff_channel_id | string | 销售品订单揽装人进驻网点标识 |
| xsp_salestaff_own_channel_id | string | 销售品订单揽装人归属销售点标识 |
| cwg_xzs | bigint | 主网关下从网关当月新增数 |
| cwg_zws | bigint | 主网关下从网关当月在网数 |
| cwg_serv_list | string | 主网关下从网关在网服务标识列表 |
| xzcwg_serv_list | string | 主网关下从网关当月新增服务标识列表 |
| sqb_zws | bigint | 主网关下从网关商企版在网数 |
| gzb_zws | bigint | 主网关下从网关公众版在网数 |
| sqb_xzs | bigint | 主网关下从网关商企版当月新增数 |
| gzb_xzs | bigint | 主网关下从网关公众版当月新增数 |
| xsp_offer_id | decimal(22,0) | 销售品标识(广州本地维表） |
| xsp_offer_code | string | 销售品编码(广州本地维表） |
| xsp_offer_name | string | 销售品名称(广州本地维表） |
| xsp_channel_type_2011 | string | 销售品订单渠道大类 |
| xsp_channel_subtype_2011 | string | 销售品订单渠道小类 |
