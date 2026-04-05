---
name: hive-telecom-query
description: 电信业务 Hive SQL 查询助手。当用户用自然语言描述数据需求（如"统计本月移动新发展用户数"、"按营服渠道分组"、"华东区宽带有效用户收入"等），自动生成符合 Hive SQL 语法的查询。使用前需确保项目目录下存在 `表信息.md` 或 `skills/hive-telecom-query/references/字段速查.md`。
argument-hint: "<业务数据需求描述，包含统计指标、时间范围、产品类型、分组维度、过滤条件>"
---

# /hive-telecom-query - 电信业务 Hive SQL 查询助手

将自然语言数据需求转换为 Hive SQL 查询，基于电信业务表结构知识库。

## 核心能力

- **意图解析**：从自然语言提取指标、产品、时间、维度、过滤条件
- **口径映射**：根据业务术语匹配对应字段和过滤值
- **SQL 生成**：输出符合 Hive SQL 规范的 CTE 查询
- **口径确认**：生成前向用户确认口径，避免理解偏差

---

## 工作流程

### Step 1: 读取知识库

读取项目目录下的字段速查文件：
- `skills/hive-telecom-query/references/字段速查.md`（优先）
- `表信息.md`（备用）

加载以下信息：
- 主表名：`ads_yz_tb_comm_cm_all_final`
- 产品类型过滤字段和常用值
- 用户状态字段和口径定义
- 分组维度字段
- 时间口径映射
- 常用业务指标口径

### Step 2: 意图解析

从用户输入提取以下要素：

| 要素 | 识别方式 | 示例 |
|:---|:---|:---|
| **指标** | 关键词匹配 | "用户数"→COUNT(DISTINCT serv_id)，"收入"→SUM(fee) |
| **产品类型** | 关键词匹配 | "移动"→prod_type='30'，"宽带"→prod_type='40' |
| **时间范围** | 关键词匹配 | "当月"→par_month_id，"近7天"→open_date |
| **分组维度** | 关键词匹配 | "营服"→branch_name，"渠道"→channel_type_2011 |
| **过滤条件** | 关键词匹配 | "华东"→branch_name LIKE '%华东%' |
| **状态类型** | 关键词匹配 | "新入网"→is_new_user=1，"有效"→is_yx=1 |

**常见组合映射：**

| 用户需求 | 指标 | 产品 | 状态条件 |
|:---|:---|:---|:---|
| 移动新发展用户 | COUNT(DISTINCT serv_id) | prod_type='30' | is_new_user=1 |
| 宽带有效用户收入 | SUM(fee) | prod_type='40' | is_yx_kd=1 AND is_cz=1 |
| 华东营服拆机用户 | COUNT(DISTINCT serv_id) | 移动或宽带 | is_wl_cancel_user=1 |
| 融合套餐发展量 | COUNT(DISTINCT rh_tc_id) | 融合 | is_rh_ykj=1 AND is_new_user=1 |
| 携入用户数 | COUNT(DISTINCT serv_id) | 全部 | is_xr=1 |

### Step 3: 口径确认（可选）

对于复杂查询，先向用户确认理解的口径：

```
根据您的需求，我理解如下：

【指标】移动新发展用户数
  └─ 计算：COUNT(DISTINCT serv_id)
  └─ 条件：is_new_user=1 AND prod_type='30'

【时间】本月（par_month_id='202403'）

【维度】营服中心、渠道大类
  └─ 字段：branch_name, channel_type_2011

【过滤】华东营服（branch_name LIKE '%华东%'）

请确认以上口径是否正确？[Y/n]
```

如果用户直接说"直接生成"或"不用确认"，跳过此步骤。

### Step 4: SQL 生成

**输出结构：**

```sql
-- =============================================
-- 口径：<一句话说明>
-- 主表：ads_yz_tb_comm_cm_all_final
-- 生成时间：<YYYY-MM-DD>
-- =============================================

SELECT
    <维度字段1> AS <中文别名>,
    <维度字段2> AS <中文别名>,
    <指标计算> AS <中文别名>
FROM ads_yz_tb_comm_cm_all_final
WHERE 1=1
  AND <时间条件>      -- <时间说明>
  AND <产品条件>      -- <产品说明>
  AND <状态条件>      -- <状态说明>
  AND <其他过滤>      -- <过滤说明>
GROUP BY
    <维度字段1>,
    <维度字段2>
ORDER BY <指标> DESC;
```

**Hive SQL 规范：**

- 使用 `date_format()` 处理日期
- 金额字段保留 2 位小数：`ROUND(fee, 2)`
- `COUNT(DISTINCT ...)` 注意数据倾斜
- 分区字段优先过滤（`par_month_id`）
- 字段别名使用中文
- 复杂逻辑添加注释

### Step 5: 口径说明

生成后，提供口径解释：

```markdown
### 口径说明
| 要素 | 定义 |
|:---|:---|
| 移动新发展用户 | 本月新入网且产品类型为移动（is_new_user=1, prod_type='30'） |
| 本月 | 账期月份 par_month_id='202403' |
| 华东营服 | 营服名称包含"华东" |

### 变体建议
- 按天统计：将 `par_month_id` 替换为 `date_format(open_date,'yyyyMMdd')`
- 添加分局维度：加入 `subst_name AS 分局`
- 只看5G用户：加 `AND is_5g=1`
```

---

### 场景 0：状态字段关联（自动识别）

**输入：** 统计各状态的用户数

**自动识别：**
- 用户提到"状态"的中文名 → 需要关联字典表
- 匹配关联：`state` + `attr_id` → `dws_crm_cfguse.dws_attr_value`

**SQL：**
```sql
SELECT
    a.state                              AS 状态代码,
    b.attr_value_name                    AS 状态名称,
    COUNT(DISTINCT a.serv_id)          AS 用户数
FROM ads_yz_tb_comm_cm_all_final a
LEFT JOIN dws_crm_cfguse.dws_attr_value b
    ON a.attr_id = b.attr_id
    AND a.state = b.attr_value
WHERE b.attr_id = '4000000201'
  AND a.par_month_id = '202403'
GROUP BY a.state, b.attr_value_name
ORDER BY 用户数 DESC;
```

---

## 常见场景示例

### 场景 1：新发展用户统计
**输入：** 统计本月移动新发展用户数，按营服和渠道大类分组

**SQL：**
```sql
SELECT
    branch_name                AS 营服中心,
    channel_type_2011         AS 渠道大类,
    COUNT(DISTINCT serv_id)   AS 移动新发展用户数
FROM ads_yz_tb_comm_cm_all_final
WHERE 1=1
  AND par_month_id = '202403'   -- 本月
  AND prod_type = '30'          -- 移动
  AND is_new_user = 1           -- 新入网
  AND is_cancel_user = 0        -- 未拆机
GROUP BY branch_name, channel_type_2011
ORDER BY 移动新发展用户数 DESC;
```

### 场景 2：收入统计
**输入：** 华东区宽带有效用户本月出账收入

**SQL：**
```sql
SELECT
    branch_name                AS 营服中心,
    ROUND(SUM(fee), 2)        AS 宽带出账收入
FROM ads_yz_tb_comm_cm_all_final
WHERE 1=1
  AND par_month_id = '202403'   -- 本月
  AND prod_type = '40'          -- 宽带
  AND is_yx_kd = 1              -- 宽带有效
  AND is_cz = 1                 -- 当月出账
  AND branch_name LIKE '%华东%'  -- 华东区
GROUP BY branch_name;
```

### 场景 3：携转分析
**输入：** 本月携入用户数，按营服和来源运营商分组

**SQL：**
```sql
SELECT
    branch_name                AS 营服中心,
    yys_type                   AS 携入来源,
    COUNT(DISTINCT serv_id)   AS 携入用户数
FROM ads_yz_tb_comm_cm_all_final
WHERE 1=1
  AND par_month_id = '202403'   -- 本月
  AND is_xr = 1                 -- 携入
GROUP BY branch_name, yys_type
ORDER BY 携入用户数 DESC;
```

### 场景 4：融合业务
**输入：** 本月融合套餐发展量，按融合类型分组

**SQL：**
```sql
SELECT
    rh_type_ykj                AS 融合类型,
    COUNT(DISTINCT rh_tc_id)  AS 融合套餐发展量
FROM ads_yz_tb_comm_cm_all_final
WHERE 1=1
  AND par_month_id = '202403'   -- 本月
  AND is_rh_ykj = 1              -- 融合用户
  AND is_new_user = 1            -- 新入网
GROUP BY rh_type_ykj
ORDER BY 融合套餐发展量 DESC;
```

---

## 故障排除

| 问题 | 可能原因 | 解决方案 |
|:---|:---|:---|
| 结果为空 | 营服名称不匹配 | 检查 `branch_name LIKE '%华东%'` 是否符合实际命名 |
| 数量异常偏大 | 未过滤拆机用户 | 添加 `AND is_cancel_user = 0` |
| 数量异常偏小 | 有效用户口径过严 | 确认 `is_yx=1` 或 `is_yx_kd=1` 是否适用 |
| 日期过滤无效 | 字段用错 | "当月"用 `par_month_id`，"当日"用 `open_date` |
| 收入为0 | 未加出账条件 | 添加 `AND is_cz = 1` |

---

## 依赖文件

技能依赖以下文件（按优先级）：
1. `skills/hive-telecom-query/references/字段速查.md` - 提取的关键字段映射
2. `表信息.md` - 完整的表结构知识库

确保使用前这些文件存在于项目目录。
