-- =============================================================================
-- 宽带入网数查询 - 2026年3月
-- 特别关注129+宽带新装情况
-- =============================================================================

-- -----------------------------------------------------------------------------
-- 1. 主宽入网数（全部宽带）
-- 来源：宽带新装清单 (ads_yz_kd_new_list)
-- 口径：kd_desc='普通宽带'，剔除专线、城域网、快捷宽带主账号
-- -----------------------------------------------------------------------------
WITH main_broadband_new AS (
    SELECT
        par_month_id                                    -- 统计月份
        , COUNT(serv_id) AS main_kd_new_cnt            -- 主宽入网数
        , SUM(rh_tc_value) AS main_kd_new_points       -- 主宽入网积分
    FROM view_ads_yz_kd_new_list
    WHERE par_month_id = 202603                         -- 2026年3月
        AND kd_desc = '普通宽带'
        AND COALESCE(prod_name, '-1') NOT LIKE '%专线%'
        AND COALESCE(prod_name, '-1') NOT LIKE '%城域网%'
        AND COALESCE(kd_prod_offer_name, '-1') NOT LIKE '%0时长%'
    GROUP BY par_month_id
)

-- -----------------------------------------------------------------------------
-- 2. 129+宽带入网数
-- 来源：全业务资料表 (ads_yz_tb_comm_cm_all_final)
-- 口径：融合套餐积分 >= 129 的普通宽带
-- -----------------------------------------------------------------------------
, broadband_129plus AS (
    SELECT
        par_month_id                                    -- 统计月份
        , COUNT(serv_id) AS kd_129_new_cnt             -- 129+宽带入网数
        , SUM(rh_tc_value) AS kd_129_new_points         -- 129+宽带入网积分
    FROM view_ads_yz_tb_comm_cm_all_final
    WHERE par_month_id = 202603                         -- 2026年3月
        AND is_cancel_user = 0                          -- 在网
        AND prod_type = 40                              -- 宽带产品
        AND kd_desc = '普通宽带'
        AND mainstream_net_type = 10                   -- 主宽
        AND is_cz = 1                                   -- 当月出账
        AND COALESCE(kd_prod_offer_id, '-1') NOT LIKE '%500046067%'  -- 剔除快捷宽带
        AND rh_tc_value >= 129                          -- 129+套餐
        AND is_rh_ykj = 1                               -- 融合用户
    GROUP BY par_month_id
)

-- -----------------------------------------------------------------------------
-- 3. 129+宽带新装明细（按维度分组）
-- 用于分析129+宽带的渠道、网格、营服等维度分布
-- -----------------------------------------------------------------------------
, broadband_129plus_detail AS (
    SELECT
        par_month_id                                    -- 统计月份
        , region_type                                   -- 五大网格
        , channel_type_2011                             -- 渠道大类
        , channel_subtype_2011                          -- 渠道中类
        , channel_subtype0_2011                         -- 渠道小类
        , subst_name                                    -- 落地局向
        , branch_name                                   -- 落地营服
        , COUNT(serv_id) AS kd_129_new_cnt             -- 129+宽带入网数
        , SUM(rh_tc_value) AS kd_129_new_points        -- 129+宽带入网积分
    FROM view_ads_yz_tb_comm_cm_all_final
    WHERE par_month_id = 202603
        AND is_cancel_user = 0
        AND prod_type = 40
        AND kd_desc = '普通宽带'
        AND mainstream_net_type = 10
        AND is_cz = 1
        AND COALESCE(kd_prod_offer_id, '-1') NOT LIKE '%500046067%'
        AND rh_tc_value >= 129
        AND is_rh_ykj = 1
    GROUP BY
        par_month_id
        , region_type
        , channel_type_2011
        , channel_subtype_2011
        , channel_subtype0_2011
        , subst_name
        , branch_name
)

-- -----------------------------------------------------------------------------
-- 4. 主宽入网明细（按渠道类型分组）
-- -----------------------------------------------------------------------------
, main_broadband_by_channel AS (
    SELECT
        par_month_id
        , region_type
        , channel_type_2011
        , channel_subtype_2011
        , channel_subtype0_2011
        , subst_name
        , branch_name
        , COUNT(serv_id) AS main_kd_new_cnt
        , SUM(rh_tc_value) AS main_kd_new_points
    FROM view_ads_yz_kd_new_list
    WHERE par_month_id = 202603
        AND kd_desc = '普通宽带'
        AND COALESCE(prod_name, '-1') NOT LIKE '%专线%'
        AND COALESCE(prod_name, '-1') NOT LIKE '%城域网%'
        AND COALESCE(kd_prod_offer_name, '-1') NOT LIKE '%0时长%'
    GROUP BY
        par_month_id
        , region_type
        , channel_type_2011
        , channel_subtype_2011
        , channel_subtype0_2011
        , subst_name
        , branch_name
)

-- =============================================================================
-- 最终输出
-- =============================================================================
SELECT
    '2026年3月宽带入网汇总' AS summary_type
    , m.main_kd_new_cnt     AS 总主宽入网数
    , m.main_kd_new_points  AS 总主宽入网积分
    , b.kd_129_new_cnt      AS 129+宽带入网数
    , b.kd_129_new_points   AS 129+宽带入网积分
    , ROUND(b.kd_129_new_cnt * 100.0 / NULLIF(m.main_kd_new_cnt, 0), 2) AS 129+占比
FROM main_broadband_new m
LEFT JOIN broadband_129plus b ON m.par_month_id = b.par_month_id

UNION ALL

SELECT
    '129+宽带-按五大网格分布'
    , NULL, NULL
    , SUM(kd_129_new_cnt)
    , SUM(kd_129_new_points)
    , NULL
FROM broadband_129plus_detail
GROUP BY region_type

UNION ALL

SELECT
    '主宽-按五大网格分布'
    , SUM(main_kd_new_cnt)
    , SUM(main_kd_new_points)
    , NULL
    , NULL
    , NULL
FROM main_broadband_by_channel
GROUP BY region_type
;
