---
name: excel-to-table-md
description: 将 CDAP 清单 Excel 转换为 write-query 技能可用的表结构 md 文档。提取表名、Hive表名、视图名、字段分类、字段说明、字典值、口径案例，输出到 references 目录。
argument-hint: "<Excel文件路径>"
---

# excel-to-table-md

将 CDAP 清单 Excel 文件转换为 write-query 技能规范的表结构 md 文档。

## 使用方法

```
/excel-to-table-md <Excel文件路径>
```

## 输出格式

每个表输出为一个 md 文件，包含：

1. **Header** — 表名、Hive 表名、视图名
2. **字段说明** — 按字段分类组织（分类作为小标题），包含字段名、字段含义、标签周期、字典值、说明
3. **口径案例** — 底部单独板块（仅当原 Excel 包含案例指标时）

## 处理流程

1. 调用 `excel-to-markdown` 脚本将 Excel 转为中间 md
2. 解析中间 md，提取表名/Hive表名/视图名、字段分类、字段详情、口径案例
3. 按模板格式重组，输出到技能 references 目录

## 输出路径

`{skill_dir}/references/{序号}_{表名}.md`

## 示例

输入：
```
/excel-to-table-md CDAP清单拆分/069_全业务资料表.xlsx
```

输出：
```
references/069_全业务资料表.md
```
