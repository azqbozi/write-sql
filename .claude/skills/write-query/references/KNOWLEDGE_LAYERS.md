# write-query 四层知识模型与路径

> 与 [SKILL.md](../SKILL.md) 中工作流程一致：**D 经验路由 → A 表结构 → B 指标口径 → C 案例参考**。
> 口径冲突优先级：B 技术口径 > A 表条件速查 > C 案例（结构借鉴）> D 经验补充 > 自由推理（标"假设"待确认）。

## 四层一图

```
                       用户提需求
                           │
                           ▼
            ┌──────────────────────────────────────┐
            │  D 层 经验/路由 (D_experience/)       │
            │  - business_glossary  术语映射        │
            │  - table_routing       业务→表 路由   │
            │  - anti_patterns       反 pattern     │
            │  - cdap_global_rules   全局硬约束     │
            │  - dictionaries/       状态/动作码值  │
            │  - lessons_learned     已知陷阱日志   │
            └──────────────┬───────────────────────┘
                           │ 路由后
            ┌──────────────┼───────────────┐
            ▼              ▼               ▼
       ┌─────────┐    ┌─────────┐    ┌─────────────┐
       │  A 层   │    │  B 层   │    │   C 层       │
       │tables/  │    │metrics/ │    │demand-cases/│
       │字段/分区│    │指标口径 │    │ 案例编排     │
       └─────────┘    └─────────┘    └─────────────┘
                           │
                           ▼
              SQL（含口径来源标注）
                           │
                           ▼
              反向回填 → D 层各文件
```

## D 层 — 经验 / 路由 / 全局规则（★关键差异化）

| 内容 | 路径 |
|------|------|
| 经验层入口（含回填规则） | [D_experience/INDEX.md](D_experience/INDEX.md) |
| 业务术语 ↔ CDAP 概念映射 | [D_experience/business_glossary.md](D_experience/business_glossary.md) |
| 业务场景 → 候选表 路由 | [D_experience/table_routing.md](D_experience/table_routing.md) |
| 反 pattern 库 | [D_experience/anti_patterns.md](D_experience/anti_patterns.md) |
| 全局硬约束 | [D_experience/cdap_global_rules.md](D_experience/cdap_global_rules.md) |
| 已知陷阱（追加日志） | [D_experience/lessons_learned.md](D_experience/lessons_learned.md) |
| 状态/动作码值字典 | [D_experience/dictionaries/](D_experience/dictionaries/) |

**约定**：
- D 层是 SKILL.md **启动强制加载**的核心层（除 dictionaries 按需加载）
- D 层**不重复 ABC 内容**，只做"翻译表 / 路由表 / 反例 / 硬约束 / 码值字典"
- 每次任务结束按"回填规则"更新对应 D 层文件，长期演进

## A 层 — 数据目录（表结构）

| 内容 | 路径 |
|------|------|
| 单表字段、分区、粒度、本表常用条件速查 | `references/tables/{序号}_{表名}.md` |
| 按业务主题找表 | [TABLE_INDEX.md](TABLE_INDEX.md) |

**约定**：
- `tables/` 下文件名中的**序号**与 `TABLE_INDEX.md` 中「序号」列一致
- `layer: A` 的 YAML frontmatter 便于检索
- **A 层 hive_name 仅供参考**，落 SQL 前必须列生产表名让用户校对（[R-004](D_experience/cdap_global_rules.md)）
- A 层字段表是**参考清单非完备清单**，怀疑字段存在与否要问用户（[AP-002](D_experience/anti_patterns.md)）

## B 层 — 指标层（业务口径 + 技术口径 SQL）

| 内容 | 路径 |
|------|------|
| 指标总索引与列表 | [metrics/INDEX.md](metrics/INDEX.md) |
| 按业务板块/分类的指标详情 | [metrics/](metrics/)（`基本面/`、`专题/`、`战新/`） |
| 指标 ↔ CDAP 生产流程名 | [metric_table_map.md](metric_table_map.md) |
| CDAP 流程名 ↔ 表序号 / 表文档（桥接） | [metric_bridge.md](metric_bridge.md) |

**约定**：标准指标以 **技术口径 (SQL)** 为权威；`metric_bridge` 用于从「CDAP 生产流程」跳到 `tables/` 文档。

## C 层 — 需求案例 / 查询模式（编排）

| 内容 | 路径 |
|------|------|
| 案例索引 | [demand-cases/INDEX.md](demand-cases/INDEX.md) |
| 单篇案例 + 新建模板 | [demand-cases/](demand-cases/) |

**约定**：案例**不定义新指标**；须引用 B 层指标名与 A 层 `table_id`，SQL 为模板化或说明性；与 B 冲突时以 B 为准。

## 快速对照（执行顺序）

```
自然语言需求
    → 第 1 步：D.business_glossary 解析业务概念
    → 第 2 步：D.table_routing + D.anti_patterns 路由选表
    → 第 3 步：A.tables/{xxx}.md + 用户校对生产表名
    → 第 4 步（可选）：B.metric_table_map / metrics → 标准技术口径
    → 第 5 步（可选）：C.demand-cases 类似案例
    → 第 6 步：写 SQL，应用 D.cdap_global_rules + D.dictionaries
    → 输出 SQL + 口径来源
    → 反向回填 D 层
```
