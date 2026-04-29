---
# C 层：需求案例 / 查询模式（模板）
# 复制本文件，改名为 Q-{短描述}.md，并填写 frontmatter 与正文。

case_id: "Q-YYYYMMDD-001"
title: "（一句话说明取数目的）"
tags: []
metrics_used: []
metric_ids: []
# 与 TABLE_INDEX / tables 中 table_id 对齐；可多表
tables_used: []
# 可替换参数（示例值仅作说明）
params:
  - name: "par_month_id"
    description: "统计月份 yyyymm"
    example: "202603"
---

# {title}

## 业务说明

（2～5 句：谁看、出数粒度、与常规报表差异。）

## 口径依据

- 涉及指标以 [metrics/INDEX.md](../metrics/INDEX.md) 与对应 `metric_id` 的单指标文件 **技术口径 (SQL)** 为权威。  
- 本案例若与指标定义冲突，**以指标定义为准**；本页 SQL 为编排模板。

## 参数

| 参数 | 含义 | 示例 |
|------|------|------|
|  |  |  |

## 参考 SQL

```sql
-- 占位；从指标技术口径摘条件，或写 CTE 组合多指标
```

## 易错点

- 分区：必带 `par_month_id`（或实际分区字段名）。  
- 去重：说明是否按 `serv_id` 计数。  
- 其他：  

## 相关 A 层表文档

- （链接到 `../tables/序号_表名.md`）


