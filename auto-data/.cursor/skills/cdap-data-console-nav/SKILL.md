---
name: cdap-data-console-nav
description: Navigates to CDAP data console (数据控制台) via browser automation. Use when the user asks to open the data console, go to 数据控制台, enter CDAP data console, or navigate to the SQL query interface in the CDAP enterprise platform. Requires user-chrome-devtools MCP and an already logged-in Chrome session.
---

# CDAP 数据控制台导航

自动按固定路径从主页点击进入「数据控制台」页面。

## 前置条件

- 用户已登录 CDAP 门户：`http://132.122.113.148:19001/atomicportal/#/login`
- **user-chrome-devtools** MCP 已连接同一 Chrome 实例
- 当前选中的 Tab 为已登录会话

## 导航流程（6 步）

按顺序执行以下步骤，每步后可用 `take_snapshot` 验证页面状态。

### 1. 进入主页

```json
call_mcp_tool: user-chrome-devtools, navigate_page
{ "type": "url", "url": "http://132.122.113.148:19001/atomicportal/#/home" }
```

### 2. 点击「自助分析」

- `take_snapshot` 获取页面快照
- 在 a11y 树中查找包含 `StaticText "自助分析"` 的可点击父元素（link/button）
- `click` 传入该元素的 `uid`
- 验证：URL 含 `#/self-analy-list?appName=自助分析`

### 3. 点击「地市专区」

- `take_snapshot` 查找「地市专区」卡片（通常为右侧蓝色卡片）
- 若 a11y 树中无直接可点元素，可用 `evaluate_script` 按文本或位置定位并点击
- **重要**：点击会 `window.open` 新 Tab
- 调用 `list_pages` 获取新 Tab 的 `pageId`，再 `select_page` 切换到新 Tab
- 验证：新 Tab URL 含 `#/main_console`，页面有「广州专区(zone_gz)」等项目列表

### 4. 点击第二条「查看」

- `take_snapshot` 查找表格第二行（广州专区-IT及业务支持中心-广州业支）的「查看」按钮
- `click` 传入对应 `uid`
- 验证：面包屑显示「项目 | 广州专区-IT及业务支持中心-广州业支」

### 5. 点击「仓库管理」

- `take_snapshot` 查找顶部 `link "仓库管理"`
- `click` 传入 `uid`
- 验证：左侧出现仓库管理菜单

### 6. 点击「数据控制台」

- `take_snapshot` 查找左侧 `link "数据控制台"`
- `click` 传入 `uid`
- 验证：URL 变为 `#/query_advance_gp`，出现 SQL 编辑区、本地库/授权库、执行按钮

### 7. 导入数据（可选）

当用户需要导入 Excel 时，在数据控制台执行：

1. **点击「导入数据」**：`take_snapshot` 查找按钮「导入数据」→ `click(uid)`
2. **上传文件**：在弹窗中 `upload_file`，目标为包含 `input[type=file]` 的父元素（通常为文件选择区域），传入本地路径如 `C:\驻点-导入模板.xlsx`
3. **点击「提交」**：`take_snapshot` 查找弹窗内「提交」按钮 → `click(uid)` 完成导入

### 8. 执行 SQL 查询（可选）

当用户需要查询表数据时，在数据控制台执行：

1. **输入 SQL**：`take_snapshot` 查找 SQL 编辑区（`textbox` 多行输入框，通常为「查询」Tab 下的编辑框）→ `fill(uid, "select * from zone_gz_yz_313")` 或按需替换表名
2. **点击「执行」**：`take_snapshot` 查找按钮「执行」→ `click(uid)` 运行查询，结果展示在下方

## 关键点

| 注意 | 说明 |
|------|------|
| uid 会变化 | 每次 `take_snapshot` 的 uid 不同，必须按**文本内容**定位，不能写死 |
| 地市专区新开 Tab | 必须 `list_pages` → `select_page` 切换到新 Tab 才能继续 |
| 证书 | 首次访问 `https://132.121.108.31:24102` 可能需处理证书 |

## 测试采样（用于复盘/排障）

说明：以下 `uid/pageId` 为 2026-03-06 的一次会话采样值，仅用于你排查“点错/找不到元素/没切换 Tab”等问题；**自动化执行时不要写死这些值**，仍应以最新 `take_snapshot` 为准。

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

本次过程快照（如需对照 a11y 树排查）：

- `c:\\06_Project\\my-dev-projects\\auto-data\\tmp\\home.snap.txt`
- `c:\\06_Project\\my-dev-projects\\auto-data\\tmp\\warehouse.snap.txt`

## 详细文档

完整步骤与 URL 说明见：[docs/CDAP-数据控制台导航流程.md](../../docs/CDAP-数据控制台导航流程.md)
