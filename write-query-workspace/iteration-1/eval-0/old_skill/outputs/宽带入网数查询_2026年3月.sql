-- =============================================================================
-- 2026年3月宽带入网数查询
-- 特别关注：129+宽带新装情况
-- 生成时间: 2026-04-22
-- =============================================================================

-- -----------------------------------------------------------------------------
-- Part 1: 2026年3月宽带新装清单（总体宽带入网数）
-- 数据源: ads_yz_kd_new_list (宽带新装清单)
-- -----------------------------------------------------------------------------

WITH kd_new_install AS (
    SELECT
        count(serv_id) AS total_kd_count,          -- 宽带新装总数
        sum(rh_tc_value) AS total_kd_points,      -- 宽带新装总积分
        sum(CASE WHEN rh_type_ykj = '新宽带新移动' AND is_rh_ykj = 1 THEN 1 ELSE 0 END) AS rh_new_kd_new_yd_count  -- 融合新宽新移数
    FROM ads_yz_kd_new_list
    WHERE month_id = 202603
      AND kd_desc = '普通宽带'
      AND COALESCE(prod_name, '-1') NOT LIKE '%专线%'
      AND COALESCE(prod_name, '-1') NOT LIKE '%城域网%'
      AND COALESCE(kd_prod_offer_name, '-1') NOT LIKE '%0时长%'
),

-- -----------------------------------------------------------------------------
-- Part 2: 129+宽带入网数（融合129+）
-- 数据源: ads_yz_tb_comm_cm_all_final (全业务资料表)
-- 筛选条件: 融合套餐积分 >= 129 且为融合用户
-- -----------------------------------------------------------------------------

kd_129_plus AS (
    SELECT
        count(serv_id) AS kd_129_count,            -- 129+宽带入网数
        sum(rh_tc_value) AS kd_129_points          -- 129+宽带入网积分
    FROM ads_yz_tb_comm_cm_all_final
    WHERE par_month_id = 202603
      AND is_cancel_user = 0                       -- 在网
      AND prod_type = 40                           -- 宽带产品
      AND kd_desc = '普通宽带'
      AND mainstream_net_type = 10                -- 主宽
      AND is_cz = 1                                -- 当月出账
      AND COALESCE(kd_prod_offer_id, '-1') NOT LIKE '%500046067%'  -- 剔除快捷宽带
      AND rh_tc_value >= 129                       -- 融合套餐积分 >= 129
      AND is_rh_ykj = 1                            -- 融合用户
),

-- -----------------------------------------------------------------------------
-- Part 3: 129+融合宽带新装（从宽带新装清单直接统计）
-- 数据源: ads_yz_kd_new_list
-- -----------------------------------------------------------------------------

kd_129_new_list AS (
    SELECT
        count(serv_id) AS kd_129_new_count,       -- 129+宽带新装数
        sum(rh_tc_value) AS kd_129_new_points     -- 129+宽带新装积分
    FROM ads_yz_kd_new_list
    WHERE month_id = 202603
      AND kd_desc = '普通宽带'
      AND COALESCE(prod_name, '-1') NOT LIKE '%专线%'
      AND COALESCE(prod_name, '-1') NOT LIKE '%城域网%'
      AND COALESCE(kd_prod_offer_name, '-1') NOT LIKE '%0时长%'
      AND rh_tc_value >= 129                      -- 融合套餐积分 >= 129
      AND is_rh_ykj = 1                            -- 融合用户
)

-- -----------------------------------------------------------------------------
-- 最终结果汇总
-- -----------------------------------------------------------------------------
SELECT
    '2026年3月宽带入网统计' AS stat_period,
    a.total_kd_count AS宽带新装总数,
    a.total_kd_points AS宽带新装总积分,
    a.rh_new_kd_new_yd_count AS融合新宽新移数,
    b.kd_129_count AS "129+宽带入网数(全业务资料表)",
    b.kd_129_points AS "129+宽带入网积分(全业务资料表)",
    c.kd_129_new_count AS "129+宽带新装数(新装清单)",
    c.kd_129_new_points AS "129+宽带新装积分(新装清单)"
FROM kd_new_install a
JOIN kd_129_plus b ON 1=1
JOIN kd_129_new_list c ON 1=1;

-- =============================================================================
-- 详细查询: 按渠道类型统计129+宽带新装
-- =============================================================================

SELECT
    channel_type_2011 AS 渠道大类,
    channel_subtype_2011 AS 渠道中类,
    count(serv_id) AS 129宽带新装数,
    sum(rh_tc_value) AS 129宽带新装积分
FROM ads_yz_kd_new_list
WHERE month_id = 202603
  AND kd_desc = '普通宽带'
  AND COALESCE(prod_name, '-1') NOT LIKE '%专线%'
  AND COALESCE(prod_name, '-1') NOT LIKE '%城域网%'
  AND COALESCE(kd_prod_offer_name, '-1') NOT LIKE '%0时长%'
  AND rh_tc_value >= 129
  AND is_rh_ykj = 1
GROUP BY channel_type_2011, channel_subtype_2011
ORDER BY count(serv_id) DESC;

-- =============================================================================
-- 详细查询: 按分局统计129+宽带新装（Top 20）
-- =============================================================================

SELECT
    subst_id AS 分局ID,
    subst_name AS 分局名称,
    count(serv_id) AS 129宽带新装数,
    sum(rh_tc_value) AS 129宽带新装积分
FROM ads_yz_kd_new_list
WHERE month_id = 202603
  AND kd_desc = '普通宽带'
  AND COALESCE(prod_name, '-1') NOT LIKE '%专线%'
  AND COALESCE(prod_name, '-1') NOT LIKE '%城域网%'
  AND COALESCE(kd_prod_offer_name, '-1') NOT LIKE '%0时长%'
  AND rh_tc_value >= 129
  AND is_rh_ykj = 1
GROUP BY subst_id, subst_name
ORDER BY count(serv_id) DESC
LIMIT 20;

-- =============================================================================
-- 详细查询: 129+套餐升降档路径（新装129+宽带的升降档来源分析）
-- 数据源: ads_yz_bd129_sdjd_list (129+套餐升降档路径清单)
-- =============================================================================

SELECT
    par_month_id AS 月份,
    sd_type AS 升降档类型,
    count(DISTINCT serv_id) AS 用户数
FROM ads_yz_bd129_sdjd_list
WHERE par_month_id = 202603
  AND prod_type = 40  -- 宽带产品
  AND is_new_user = 1  -- 当月新入网
GROUP BY par_month_id, sd_type
ORDER BY count(DISTINCT serv_id) DESC;
