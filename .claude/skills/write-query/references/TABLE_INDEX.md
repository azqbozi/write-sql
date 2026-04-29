# CDAP 表索引

> 按业务主题分类的保留表索引。用于「第二步：找核心表」时快速定位目标表。

## 核心事实表

| 序号  | 表名         | Hive表名                                 | 业务主题标签      |
| --- | ---------- | -------------------------------------- | ----------- |
| 69  | 全业务资料表     | ads_yz_tb_comm_cm_all_final            | 渠道、产品、销量、主体 |
| 60  | 移动新装清单     | dwd_yz_cm_cdma_ydxz_list               | 移动新装        |
| 62  | 宽带新装清单     | ads_yz_kd_new_list                     | 宽带新装        |
| 44  | 全业务号码订单表   | dwm_yz_rpt_comm_ba_subs_final          | 订单          |
| 21  | 拍照客户清单     | ads_pzkh_list                          | 客户          |
| 58  | 小微客户数清单    | ads_yz_cust_ict_list_mon_final         | 小微客户        |
| 19  | 存量追踪月清单    | ads_clzz_list                          | 存量          |
| 22  | 应收月考核客户级宽表 | zone_gz_yz.ads_ys_lst_km_ys_month_push | 应收、考核       |
| 56  | 合约清单       | dwm_yz_cm_cdma_hy_final                | 合约          |
| 57  | 小微ICT竣工清单  | ads_yz_xwict_all_list                  | 小微、竣工       |
| 59  | 移动划小清单     | ads_yz_cdma_hx_list                    | 移动、划小       |

## 收入表

| 序号 | 表名 | Hive表名 | 业务主题标签 |
|------|------|---------|------------|
| 70 | 基本面月清单 | zone_gz_yz.ads_ys_jbm | fee_fm_new、A0税后确认收入 |
| 89 | 全量科目级收入 | ads_srhx_src_income_list_mon | 科目级收入 |
| 88 | 最终版划小收入 | ads_srhx_serv_list_mon | 划小收入 |
| 5 | 台阶收入清单 | ads_yz_xsb_tjsr_skj_list_db | 台阶收入 |
| 16 | 财务部收入多维表 | ads_yz_cwb_sr_list | 财务收入 |
| 50 | 宽带到达套餐收入清单 | ads_yz_kddd_tcsr_list | 宽带、套餐收入 |
| 51 | 小微ict场景化收入数据 | ads_yz_scb_ict_fee_list | 小微、场景化收入 |
| 39 | 小业务收入多维表 | ads_yz_ict_all_ydxyw_sr_LIST | 小业务收入 |
| 29 | 小微清单2024 | zone_gz_yz.ads_yz_ict_all2024_LIST | 小微、ICT |

## 续约表

| 序号 | 表名 | Hive表名 | 业务主题标签 |
|------|------|---------|------------|
| 81 | 移动续约清单 | ads_yz_ydxy_daily_list | 移动、续约 |
| 82 | 移动续约多维表 | ads_yz_ydxy_group | 移动、续约 |
| 83 | 宽带续约清单 | ads_yz_kd_xy_list | 宽带、续约 |
| 84 | 酒宽续约清单 | ads_yz_jdkd_xy_list | 酒宽、续约 |
| 85 | 双线全量清单 | ads_yz_sx_qlyz_list | 双线、全量 |
| 95 | 双线续约清单 | ads_yz_sx_xy_list | 双线、续约 |

## 积分表

| 序号 | 表名 | Hive表名 | 业务主题标签 |
|------|------|---------|------------|
| 63 | 净增积分清单 | ads_yz_tb_tyks_score_inc_mtd | 净增积分 |
| 68 | 发展存量积分清单 | ads_yz_score_all_list | 存量积分 |
| 18 | 揽装积分清单 | ads_yz_lyf_lz | 揽装积分 |
| 18 | 双线净增积分清单 | ads_yz_tb_tyks_score_inc_zx_mtd | 双线、净增积分 |
| 13 | 财务部积分多维表 | zone_gz_yz.view_lw_ads_yz_finance_jf_list | 财务、积分 |

## 降档表

| 序号 | 表名 | Hive表名 | 业务主题标签 |
|------|------|---------|------------|
| 2 | 降档清单 | ads_yz_jd_list | 降档 |
| 66 | 降档原始清单 | ads_yz_sunshou_acc_list | 降档、原始 |
| 67 | 降档动作订单清单 | ads_yz_sunshou_qudao | 降档、动作 |
| 64 | 129+套餐升降档路径清单 | ads_yz_bd129_sdjd_list | 129+、升降档 |
| 65 | 129+套餐升降档路径多维表 | ads_yz_bd129_sdjd_dwb | 129+、升降档、维表 |

## 维表

| 序号 | 表名 | Hive表名 | 业务主题标签 |
|------|------|---------|------------|
| 74 | 产品维表视图 | dws_product | 产品维度 |
| 75 | 机构维表视图 | dwd_yz_dim_org | 机构维度、网点 |
| 72 | 字典表视图 | dws_attr_value | 字典 |
| 73 | 字典维表视图 | dws_attr_SPEC | 字典维度 |
| 76 | 移动主套餐维表视图 | metadata_ods_day.tb_dim_cdma_disc_type | 移动主套餐 |
| 77 | 销售品维表视图 | dws_offer | 销售品 |
| 78 | 揽装网点维表 | dwd_yz_sales_man_outlers_final | 揽装网点 |

## 补充表

| 序号  | 表名       | Hive表名                                   | 业务主题标签 |
| --- | -------- | ---------------------------------------- | ------ |
| 71  | 优惠资料表    | ads_yz_rpt_comm_cm_msdisc_final          | 优惠     |
| 90  | 欠费日清单    | ads_ys_lst_qf_pushdata_daily_bss         | 欠费     |
| 91  | 滞纳金清单    | dwm_tb_zhinajin_baobiao_list_ys_site_mon | 滞纳金    |
| 45  | 欠不列预警清单  | zone_gz_yz.ads_ys_qblyj_daily            | 欠不列、预警 |
| 54  | 基础业务托收清单 | ads_yz_tb_cl_tuoshou_list                | 托收     |
| 98  | 存量未托收清单  | ads_yz_clts_change_list_mon              | 存量、未托收 |
| 6   | 欠补列日清单   | zone_gz_yz.ads_ys_qbl_real               | 欠补列    |
| 9   | 历史欠不列月清单 | zone_gz_yz.view_ads_ys_lst_qbl_mon       | 历史欠不列  |

## 客户类

| 序号 | 表名 | Hive表名 | 业务主题标签 |
|------|------|---------|------------|
| 93 | 商客新建档客户清单 | ads_yz_xjd_kh_list | 商客、新建档 |
| 48 | 企微粉丝清单报表 | dwd_yz_qywx_daily_list_end | 企微、粉丝 |
| 49 | 满卡报表清单 | ads_yz_mk_list | 满卡 |
| 23 | 家庭地址客户入网价值清单 | zone_gz_yz.ads_yz_yzn_addr_label_setting_list | 家庭地址、价值 |

## 成本/佣金类

| 序号 | 表名 | Hive表名 | 业务主题标签 |
|------|------|---------|------------|
| 14 | 财务部佣金多维表 | ads_yz_yj_list | 佣金 |
| 15 | 财务部终端装维成本 | ads_yz_zwzd_cost_all_list | 终端、装维成本 |
| 61 | 自营终端模式发展成本日清单 | zone_gz_yz.ads_yz_zyzd_all_list | 自营终端、成本 |

## 其他清单

| 序号 | 表名 | Hive表名 | 业务主题标签 |
|------|------|---------|------------|
| 53 | fttr清单 | dwm_fttr_list | fttr |
| 46 | 反诈资料宽表 | dwm_yz_fz_rpt_comm_cm_serv_d_final | 反诈 |
| 47 | 政企移动入网清单报表 | dwd_yz_zhengqi_yd_new_daily_list_end | 政企、入网 |
| 96 | 实名装维清单 | ads_yz_smzw_list | 实名、装维 |
| 97 | 燃气卫士到达清单 | ads_yz_rqws_list | 燃气卫士 |
| 92 | 视联网发展规模清单 | ads_yz_slw_136_list | 视联网 |
| 94 | 转化率 | ads_yz_zhl_list | 转化率 |
| 87 | 拆机登记清单（新） | view_tb_zsh_cjdj_list | 拆机、登记 |
| 86 | 主宽拆机挽留清单 | ads_yz_kd_cjwl_list | 主宽、拆机、挽留 |
| 4 | 宽带拆机渠道分类清单 | ads_yz_kdcj_qdfl_list | 宽带、拆机、渠道 |
| 52 | 营业厅月度订单受理量清单 | ads_yz_yyt_sl_list | 营业厅、受理量 |

---

## 使用说明

1. **找核心表**：先确定业务主题，在对应分类下查找
   - 渠道+产品+销量 → `全业务资料表`（69）
   - 收入分析 → `基本面月清单`（70）或`全量科目级收入`（89）
   - 续约分析 → 续约表分类

2. **补字段**：核心表确定后，再从收入表匹配收入字段，从维表补名称

3. **Hive表名**：已补充完成（2026-04-13）

## 来源
基于 `CDAP清单拆分/` 目录下的 104 个 Excel 清单文件。

