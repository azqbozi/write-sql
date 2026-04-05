# CDAP 企业全融合数字化平台 - 数据控制台导航流程

本文档记录从登录页到「数据控制台」的完整点击路径及 MCP 指令序列。

## 前置条件

- 用户已登录：`http://132.122.113.148:19001/atomicportal/#/login`
- 使用 **user-chrome-devtools** MCP 连接已登录的 Chrome 实例

---

## 完整导航步骤

### 步骤 1：进入主页

| 操作 | 说明 |
|------|------|
| **工具** | `navigate_page` |
| **参数** | `{ "type": "url", "url": "http://132.122.113.148:19001/atomicportal/#/home" }` |
| **目标** | 企业全融合数字化平台主页 |

### 步骤 2：点击「自助分析」模块

| 操作 | 说明 |
|------|------|
| **工具** | `take_snapshot` → `click` |
| **查找** | 在快照中定位 `StaticText "自助分析"` 的父级可点击元素（如 `link` 或包含该文本的 `button`） |
| **点击** | 使用对应元素的 `uid` 执行 `click` |
| **验证** | URL 变为 `#/self-analy-list?appId=...&appName=自助分析` |

### 步骤 3：点击「地市专区」

| 操作 | 说明 |
|------|------|
| **工具** | `take_snapshot` → `click` 或 `evaluate_script` |
| **查找** | 定位文本为「地市专区」的卡片（通常为右侧蓝色卡片） |
| **注意** | 点击后可能**新开 Tab**，需 `list_pages` 找到新页面并 `select_page` |
| **验证** | 新 Tab URL 含 `#/main_console`，页面显示「广州专区(zone_gz)」等项目列表 |

### 步骤 4：点击第二条记录的「查看」按钮

| 操作 | 说明 |
|------|------|
| **目标** | 项目「广州专区-IT及业务支持中心-广州业支」 |
| **工具** | `take_snapshot` → `click` |
| **查找** | 表格第二行的「查看」按钮（uid 通常为 `*_201` 或类似） |
| **验证** | 进入项目控制台，面包屑显示「项目 \| 广州专区-IT及业务支持中心-广州业支」 |

### 步骤 5：点击顶部「仓库管理」标签

| 操作 | 说明 |
|------|------|
| **工具** | `take_snapshot` → `click` |
| **查找** | `link "仓库管理"` |
| **验证** | 左侧出现仓库管理菜单（我的收藏、仓库首页、数据控制台等） |

### 步骤 6：点击左侧「数据控制台」

| 操作 | 说明 |
|------|------|
| **工具** | `take_snapshot` → `click` |
| **查找** | `link "数据控制台"` |
| **验证** | URL 变为 `#/query_advance_gp`，出现 SQL 编辑区、本地库/授权库、执行按钮等 |

### 步骤 7：导入数据（可选）

当需要导入 Excel 文件时，在数据控制台执行：

| 子步骤 | 操作 | 说明 |
|--------|------|------|
| 7a | 点击「导入数据」 | `take_snapshot` 查找按钮「导入数据」→ `click(uid)` |
| 7b | 上传文件 | 在弹窗中 `upload_file`，目标为包含 `input[type=file]` 的父元素，传入本地路径如 `C:\驻点-导入模板.xlsx` |
| 7c | 点击「提交」 | `take_snapshot` 查找弹窗内「提交」按钮 → `click(uid)` 完成导入 |

### 步骤 8：执行 SQL 查询（可选）

当需要查询表数据时，在数据控制台执行：

| 子步骤 | 操作 | 说明 |
|--------|------|------|
| 8a | 输入 SQL | `take_snapshot` 查找 SQL 编辑区（`textbox` 多行）→ `fill(uid, "select * from zone_gz_yz_313")` 或按需替换表名 |
| 8b | 点击「执行」 | `take_snapshot` 查找按钮「执行」→ `click(uid)` 运行查询，结果展示在下方 |

---

## MCP 工具调用顺序（伪代码）

```
1. navigate_page(type="url", url="http://132.122.113.148:19001/atomicportal/#/home")
2. take_snapshot() → 找到「自助分析」→ click(uid)
3. take_snapshot() → 找到「地市专区」卡片 → evaluate_script 或 click
4. list_pages() → select_page(pageId=新开的Tab)
5. take_snapshot() → 找到第二条「查看」→ click(uid)
6. take_snapshot() → 找到「仓库管理」→ click(uid)
7. take_snapshot() → 找到「数据控制台」→ click(uid)
8. [可选] 导入数据：take_snapshot() → 找到「导入数据」→ click(uid)
9. [可选] upload_file(uid=文件选择区域, path="C:\\驻点-导入模板.xlsx")
10. [可选] take_snapshot() → 找到「提交」→ click(uid)
11. [可选] 执行 SQL：take_snapshot() → 找到 SQL 编辑区 → fill(uid, "select * from zone_gz_yz_313")
12. [可选] take_snapshot() → 找到「执行」→ click(uid)
```

---

## 关键 URL

| 阶段 | URL 特征 |
|------|----------|
| 登录页 | `#/login` |
| 主页 | `#/home` |
| 自助分析入口 | `#/self-analy-list?appName=自助分析` |
| 地市专区控制台 | `https://132.121.108.31:24102/.../#/main_console` |
| 数据控制台（最终） | `#/query_advance_gp` |

---

## 注意事项

1. **uid 会变化**：每次 `take_snapshot` 的 uid 可能不同，需按**文本内容**定位元素，而非写死 uid。
2. **地市专区会新开 Tab**：点击后需 `list_pages` 获取新 Tab 的 `pageId`，再 `select_page` 切换。
3. **证书问题**：若访问 `https://132.121.108.31:24102` 首次需手动处理证书（或 Chrome 启动时加 `--ignore-certificate-errors`）。
4. **会话**：需在同一 Chrome 实例下完成上述步骤，否则登录态可能丢失。

---

## 本次自动化测试记录（2026-03-06）

说明：以下 `uid/pageId` 为本次会话采样值，仅用于复盘与排障；下次执行仍应以最新 `take_snapshot` 为准。

### 关键点击点（本次实际命中）

| 步骤 | 目标 | 类型 | 取值 |
|------|------|------|------|
| 2 | 自助分析 | uid | `17_26` |
| 3 | 地市专区 | uid | `19_4` |
| 3 | 新开 Tab（地市专区） | pageId | `11` |
| 4 | 第二条「查看」（广州专区-IT及业务支持中心-广州业支） | uid | `20_50` |
| 5 | 仓库管理 | uid | `21_4` |
| 6 | 数据控制台 | uid | `22_4` |
| 7a | 导入数据 | uid | `24_135` |
| 7b | 文件上传区域（含 input[type=file]） | uid | `29_887` |
| 7c | 提交 | uid | `26_12` |
| 8a | SQL 编辑区（textbox multiline） | uid | `24_130` |
| 8b | 执行 | uid | `24_133` |

### 关键 URL 验证（脚本读取 location.href）

| 阶段 | URL（关键片段） |
|------|------------------|
| 自助分析入口 | `http://132.122.113.148:19001/atomicportal/#/self-analy-list?...appName=自助分析` |
| 地市专区（新 Tab） | `https://132.121.108.31:24102/...#/main_console` |
| 项目控制台 | `...#/project_console` |
| 数据控制台（最终） | `...#/query_advance_gp` |

### 过程快照（本次保存）

- `c:\\06_Project\\my-dev-projects\\auto-data\\tmp\\home.snap.txt`
- `c:\\06_Project\\my-dev-projects\\auto-data\\tmp\\warehouse.snap.txt`
