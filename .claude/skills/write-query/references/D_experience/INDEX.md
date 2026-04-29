---
layer: D
title: "D 层 经验/路由 索引"
---

# D 层 — 经验 / 路由 / 全局规则

> SKILL.md **启动时强制加载本目录的核心索引文件**。本层是这次知识体系最关键的"业务决策层"——把"什么业务去什么表、不要去什么表、有什么硬约束、码值长什么样"等隐性经验结构化沉淀。

## 文件清单与定位

| 文件 | 作用 | 加载时机 | 回填触发条件 |
|------|------|---------|------------|
| [business_glossary.md](business_glossary.md) | 业务术语 ↔ CDAP 概念映射 | **启动加载** | 用户用了我们没收录的术语 |
| [table_routing.md](table_routing.md) | 业务场景 → 候选表（含优先级 + 反例） | **启动加载** | 选错表/选对表都要补 |
| [anti_patterns.md](anti_patterns.md) | 选表与写法的反 pattern 库 | **启动加载** | 踩坑后必填 |
| [cdap_global_rules.md](cdap_global_rules.md) | 全省 / 全 CDAP 通用硬约束 | **启动加载** | 发现一条新硬规则 |
| [lessons_learned.md](lessons_learned.md) | 已知陷阱（按时间累积的追加日志） | **启动加载** | 每次踩坑结尾追加一条 |
| [dictionaries/](dictionaries/) | 状态/动作字典（按字段分文件，按需加载） | 写 WHERE 遇码值时 | 新发现一个码值即追加 |

## 本层与 ABC 三层的关系

```
A 表结构 ←—— 字段、分区是什么
B 口径   ←—— 标准指标怎么算
C 案例   ←—— 例题怎么编排
D 经验   ←—— 业务来了从哪出发？哪些坑？哪些硬约束？哪些码值？  ← SKILL 第一步用
```

**D 不重复 ABC 内容**，只做：
- 业务术语→CDAP 概念的"翻译表"（不写表字段）
- 业务场景→候选表的"路由表"（不写表字段，只指目录）
- 反例和硬约束（不写口径，只写"不要做什么"）

## 反向回填规则（强制）

每完成一次任务，按下面表格判断是否要回填：

| 这次发生了什么 | 必须回填 |
|--------------|---------|
| 用户口语术语不在 glossary | `business_glossary.md` 加 1 行 |
| Agent 第一次选错表，被用户纠正 | `table_routing.md` 加正反两行 + `anti_patterns.md` 加 1 条 |
| 字典/状态值用错 | `dictionaries/{字段}.md` 加 1 行 |
| 表 md 与生产现网名不一致 | `lessons_learned.md` + 修对应 A 层表 md |
| 发现新的全局硬约束 | `cdap_global_rules.md` 加 1 行 |

不回填的代价：下次会再踩一次同样的坑。
