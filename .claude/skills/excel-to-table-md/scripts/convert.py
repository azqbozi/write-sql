#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
excel_to_table_md.py

将 CDAP 清单 Excel 转换为 write-query 技能规范的表结构 md 文档。

处理流程：
1. 调用 excel-to-markdown 脚本将 Excel 转为中间 md
2. 解析中间 md，提取：表名、Hive表名、视图名、字段分类、字段详情、口径案例
3. 按模板格式重组，输出到技能 references 目录
"""

import argparse
import os
import re
import subprocess
import sys
import tempfile
import logging

# 路径配置
SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# excel-to-markdown 技能的绝对路径（可能与本技能不在同一父目录下）
EXCEL_TO_MD_SCRIPT = "/Users/bozi/.claude/skills/excel-to-markdown/scripts/excel_to_markdown_general.py"
REFERENCES_DIR = os.path.join(SKILL_DIR, "references")


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
    stream=sys.stdout
)
logger = logging.getLogger("excel_to_table_md")


def run_excel_to_markdown(excel_path: str) -> str:
    """调用 excel-to-markdown 脚本将 Excel 转为中间 md"""
    with tempfile.NamedTemporaryFile(suffix=".md", delete=False, mode="w", encoding="utf-8") as f:
        temp_path = f.name

    try:
        result = subprocess.run(
            [sys.executable, EXCEL_TO_MD_SCRIPT, excel_path, "-o", temp_path],
            capture_output=True,
            text=True,
            encoding="utf-8"
        )
        if result.returncode != 0:
            logger.error(f"excel-to-markdown 失败: {result.stderr}")
            raise RuntimeError(f"excel-to-markdown 失败: {result.stderr}")

        with open(temp_path, encoding="utf-8") as f:
            content = f.read()
        return content
    finally:
        if os.path.exists(temp_path):
            os.unlink(temp_path)


def parse_intermediate_md(content: str) -> dict:
    """
    解析中间 md，提取关键信息。

    返回结构：
    {
        "table_name": str,          # 中文表名
        "hive_table": str,          # Hive 表名
        "view_name": str,           # 视图名
        "sections": [                # 字段分类 sections
            {
                "category": str,    # 分类名称（如"新入网"，空字符串表示"基础字段"）
                "fields": [         # 该分类下的字段列表
                    {
                        "field": str,
                        "meaning": str,
                        "cycle": str,
                        "dict_value": str,
                        "note": str
                    }
                ]
            }
        ],
        "case_metrics": [           # 口径案例
            {"name": str, "sql": str}
        ]
    }
    """
    lines = content.split("\n")

    result = {
        "table_name": "",
        "hive_table": "",
        "view_name": "",
        "sections": [],
        "case_metrics": []
    }

    # 提取表名（中文名）：从第一行的 ## {sheet_name} 中提取
    for line in lines:
        line = line.strip()
        m = re.match(r"^##\s+(.+)$", line)
        if m:
            result["table_name"] = m.group(1).strip()
            break

    # 提取 Hive表名、视图名、英文表名（从表格行中提取）
    # 格式如：| Hive表名： | xxx | 或 | 视图名： | xxx | 或 | 表名： | xxx |
    for line in lines:
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.split("|")[1:-1]]
        if len(cells) < 2:
            continue

        # 精确匹配：避免 "Hive" in "表名：" 导致误匹配
        if re.fullmatch(r"Hive表名[：:]?", cells[0]):
            result["hive_table"] = cells[1] if len(cells) > 1 else ""
        elif re.fullmatch(r"视图名[：:]?", cells[0]):
            result["view_name"] = cells[1] if len(cells) > 1 else ""
        elif re.fullmatch(r"表名[：:]?", cells[0]):
            # "表名："行通常是英文 Hive 表名（如 ads_yz_tb_comm_cm_all_final）
            if not result["hive_table"] and len(cells) > 1 and cells[1]:
                result["hive_table"] = cells[1]

    # 找到字段表头行（包含"字段"和"字段含义"的行）
    header_line_idx = -1
    for i, line in enumerate(lines):
        if re.search(r"字段分类", line) and re.search(r"字段含义", line):
            header_line_idx = i
            break

    if header_line_idx == -1:
        logger.warning("未找到字段表头，跳过字段解析")
        return result

    # 解析字段分类
    current_category = ""
    current_fields = []

    # 从表头下一行开始解析
    for i in range(header_line_idx + 1, len(lines)):
        line = lines[i].strip()

        # 跳过空行和分隔线
        if not line or line.startswith("| ---"):
            continue

        # 跳过非数据行
        if not line.startswith("|"):
            continue

        # 遇到案例指标标题，停止字段解析
        if re.search(r"案例指标|语句", line) and "|" not in line.split("|")[1]:
            # 可能是案例指标区域的标题行
            if re.search(r"案例指标|口径|指标名称", line):
                break

        cells = [c.strip() for c in line.split("|")[1:-1]]

        # 正常应该是5-6列：字段分类、字段、字段含义、标签周期、字典值、说明
        if len(cells) < 2:
            continue

        # 字段分类列有内容，表示遇到了新的分类
        category_cell = cells[0] if len(cells) > 0 else ""
        if category_cell and category_cell not in ("", "字段分类"):
            # 保存上一个分类
            if current_fields or current_category:
                result["sections"].append({
                    "category": current_category or "基础字段",
                    "fields": current_fields
                })
            current_category = category_cell
            current_fields = []

            # 如果只有分类行没有字段行，继续
            if len(cells) < 2 or not cells[1]:
                continue

        # 字段名在第2列（索引1）
        field_name = cells[1] if len(cells) > 1 else ""
        if not field_name or field_name in ("字段", ""):
            continue

        # 提取字段信息
        field_info = {
            "field": field_name,
            "meaning": cells[2] if len(cells) > 2 else "",
            "cycle": cells[3] if len(cells) > 3 else "",
            "dict_value": cells[4] if len(cells) > 4 else "",
            "note": cells[5] if len(cells) > 5 else ""
        }
        current_fields.append(field_info)

    # 保存最后一个分类
    if current_fields or current_category:
        result["sections"].append({
            "category": current_category or "基础字段",
            "fields": current_fields
        })

    # 解析口径案例（从案例指标标题之后）
    case_started = False
    for i in range(header_line_idx + 1, len(lines)):
        line = lines[i].strip()

        if re.search(r"案例指标", line):
            case_started = True
            continue
        if not case_started:
            continue
        if not line.startswith("|"):
            continue
        if "---" in line:
            continue

        cells = [c.strip() for c in line.split("|")[1:-1]]
        if len(cells) < 2:
            continue

        # 找有 SQL 口径的行（包含 = 或 and 或 or 的行）
        name = cells[0] if cells[0] else ""
        sql_cell_idx = -1
        for j, c in enumerate(cells[1:], 1):
            if c and any(k in c for k in ["=", "and", "or", "date_format", "COALESCE", "prod_type", "is_"]):
                sql_cell_idx = j
                break

        if sql_cell_idx == -1 and not name:
            continue

        # 如果名称列是空的但SQL列有内容，说明这是延续行
        if not name and sql_cell_idx >= 0:
            # 这种情况通常是SQL被换行拆分了，尝试合并
            if result["case_metrics"] and cells[sql_cell_idx] if sql_cell_idx < len(cells) else "":
                last_metric = result["case_metrics"][-1]
                sql_text = cells[sql_cell_idx] if sql_cell_idx < len(cells) else ""
                last_metric["sql"] = last_metric["sql"].rstrip() + " " + sql_text
                continue

        sql = cells[sql_cell_idx] if sql_cell_idx >= 0 and sql_cell_idx < len(cells) else ""

        if name or sql:
            result["case_metrics"].append({
                "name": name,
                "sql": sql
            })

    return result


def build_output_md(data: dict) -> str:
    """将解析后的数据构建为最终 md 格式"""
    lines = []

    # Header
    lines.append(f"# {data['table_name']}\n")

    if data["hive_table"]:
        lines.append(f"- **Hive 表名**：`{data['hive_table']}`")
    if data["view_name"]:
        lines.append(f"- **视图名**：`{data['view_name']}`")

    lines.append("\n---\n")

    # 字段说明
    lines.append("## 字段说明\n")

    for section in data["sections"]:
        category = section["category"] if section["category"] else "基础字段"
        lines.append(f"### {category}\n")

        if not section["fields"]:
            lines.append("*（无字段）*\n")
            continue

        lines.append("| 字段 | 字段含义 | 标签周期 | 字典值 | 说明 |")
        lines.append("|------|---------|---------|-------|------|")

        for f in section["fields"]:
            field = f.get("field", "")
            meaning = f.get("meaning", "")
            cycle = f.get("cycle", "")
            dict_value = f.get("dict_value", "")
            note = f.get("note", "")

            # 转义 md 特殊字符
            def esc(s):
                return str(s).replace("|", "\\|").replace("\n", "<br>")

            lines.append(f"| {esc(field)} | {esc(meaning)} | {esc(cycle)} | {esc(dict_value)} | {esc(note)} |")

        lines.append("")

    # 口径案例
    if data["case_metrics"]:
        lines.append("---\n")
        lines.append("## 口径案例\n")
        lines.append("| 指标名称 | 计算口径 |")
        lines.append("|---------|---------|")

        for metric in data["case_metrics"]:
            name = metric.get("name", "")
            sql = metric.get("sql", "").replace("|", "\\|")
            lines.append(f"| {name} | `{sql}` |")

        lines.append("")

    return "\n".join(lines)


def get_table_name_from_path(excel_path: str) -> str:
    """从 Excel 文件路径提取表名作为输出文件名"""
    basename = os.path.splitext(os.path.basename(excel_path))[0]
    return basename


def convert_excel_to_table_md(excel_path: str, output_dir: str = None) -> str:
    """主转换函数"""
    if not os.path.exists(excel_path):
        raise FileNotFoundError(f"Excel 文件不存在: {excel_path}")

    logger.info(f"开始转换: {excel_path}")

    # Step 1: 转为中间 md
    logger.info("Step 1: 调用 excel-to-markdown...")
    intermediate_md = run_excel_to_markdown(excel_path)

    # Step 2: 解析中间 md
    logger.info("Step 2: 解析中间 md...")
    data = parse_intermediate_md(intermediate_md)
    logger.info(f"  - 表名: {data['table_name']}")
    logger.info(f"  - Hive表名: {data['hive_table']}")
    logger.info(f"  - 视图名: {data['view_name']}")
    logger.info(f"  - 字段分类数: {len(data['sections'])}")
    logger.info(f"  - 口径案例数: {len(data['case_metrics'])}")

    # Step 3: 构建输出 md
    logger.info("Step 3: 构建最终 md...")
    output_md = build_output_md(data)

    # Step 4: 写入输出文件
    output_dir = output_dir or REFERENCES_DIR
    os.makedirs(output_dir, exist_ok=True)

    table_name_for_file = get_table_name_from_path(excel_path)
    output_path = os.path.join(output_dir, f"{table_name_for_file}.md")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(output_md)

    logger.info(f"完成，输出文件: {output_path}")
    return output_path


def main():
    parser = argparse.ArgumentParser(description="Excel to Table MD")
    parser.add_argument("excel_path", help="Excel 文件路径")
    parser.add_argument("-o", "--output-dir", help="输出目录（默认：references 目录）")
    parser.add_argument("-v", "--verbose", action="store_true", help="详细输出")
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    output_path = convert_excel_to_table_md(
        args.excel_path,
        output_dir=args.output_dir
    )
    print(f"\n输出文件: {output_path}")


if __name__ == "__main__":
    main()
