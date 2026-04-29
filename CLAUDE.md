# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

本仓库是 CDAP（电信业务数据分析平台）的 SQL 编写技能集，核心功能：

1. **write-query 技能** — 根据自然语言描述编写优化的 Hive SQL 查询
2. **excel-to-table-md 技能** — 将 CDAP 清单 Excel 文件转换为表结构 markdown 文档

## 技能架构

（若本机仅有 `claude/skills/` 而无 `.claude/skills/`，路径等价替换即可。）

```
claude/skills/
├── write-query/
│   ├── SKILL.md
│   └── references/
│       ├── KNOWLEDGE_LAYERS.md   # A/B/C 三层路径总览
│       ├── TABLE_INDEX.md
│       ├── metric_table_map.md  # 指标 → CDAP 流程
│       ├── metric_bridge.md     # CDAP 流程 → tables/ 下现网表 md
│       ├── 指标字典.md
│       ├── 指标字典/
│       ├── tables/             # A 层：各表字段与分区（主路径）
│       ├── demand-cases/       # C 层：需求案例与模板
│       └── metrics/README.md   # B 层入口说明
│
└── excel-to-table-md/
    ├── SKILL.md
    ├── scripts/convert.py
    └── references/
```

## 常用命令

### Excel 转表结构文档
```bash
python claude/skills/excel-to-table-md/scripts/convert.py <Excel文件路径> [-o <输出目录>]
```

### 查看可用表
参考 `claude/skills/write-query/references/TABLE_INDEX.md`，按业务主题（核心事实表、收入表、积分表、维表）查找目标表。

## 工作流程

### 编写 Hive SQL
1. 参照 `TABLE_INDEX.md` 与 `KNOWLEDGE_LAYERS.md` 理解 A/B/C 三层
2. 指标 → `指标字典` + `metric_table_map` / `metric_bridge`；表结构 → `references/tables/{序号}_{表名}.md`（与索引不一致时以表名+Hive 表名为准）
3. 按 `write-query/SKILL.md` 的最佳实践编写 SQL，输出中注明口径来源

### 转换新 Excel
1. 将 Excel 文件放入 `CDAP清单拆分/` 目录
2. 运行转换脚本生成 `references/` 目录的表结构文档
3. 更新 `TABLE_INDEX.md` 添加新表索引

## CDAP Excel 文件说明

`CDAP清单拆分/` 目录包含 104 个 Excel 文件（序号 001-104），命名格式：`{序号}_{表名}.xlsx`

序号 001 为清单目录（不进入索引），序号 069 有已转换的 md 文档。

## 表索引分类

`TABLE_INDEX.md` 按业务主题将 104 张表分为：

| 分类 | 说明 |
|------|------|
| 核心事实表 | 全业务资料表、订单表、新装清单等核心业务表 |
| 收入表 | 基本面月清单、科目级收入、台阶收入等 |
| 续约表 | 移动/宽带/双线续约相关 |
| 积分表 | 净增积分、存量积分、揽装积分 |
| 降档表 | 降档原始清单、129+套餐升降档路径 |
| 维表 | 产品、机构、字典、销售品等维度表 |
| 补充表 | 优惠、欠费、滞纳金等补充数据 |
| 客户类 | 商客、企微粉丝、满卡等客户表 |
| 成本/佣金类 | 佣金、终端装维成本 |
| 其他清单 | 反诈、拆机挽留、实名制等 |

## 表查找规则

优先查找专项表：
- 台阶收入 → `台阶收入清单`(5)
- 科目收入 → `全量科目级收入`(89)
- 号码订单 → `全业务号码订单表`(44)
- 套餐订单 → `宽带到达套餐收入清单`(50)

## 注意事项

- `convert.py` 依赖外部 `excel-to-markdown` 脚本（路径在脚本内硬编码）
- `TABLE_INDEX.md` 中 Hive 表名已补充完成（2026-04-13）
- 口径案例仅当原 Excel 包含案例指标时才会输出
- Excel 文件序号 001 为清单目录，不进入表索引
