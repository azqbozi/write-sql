#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
batch_convert.py

批量转换 CDAP 清单 Excel 文件为表结构 md 文档。

使用方法：
    python batch_convert.py [Excel目录] [输出目录]
"""

import os
import sys
import glob
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed

# 解决 Windows GBK 编码问题
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

from convert import convert_excel_to_table_md

# 批量任务线程数
MAX_WORKERS = 4


def batch_convert(excel_dir: str, output_dir: str, exclude_patterns: list = None) -> dict:
    """
    批量转换 Excel 文件。

    Args:
        excel_dir: Excel 文件目录
        output_dir: 输出目录
        exclude_patterns: 排除的文件名模式列表（如 "*副本*"）

    Returns:
        {"success": [成功文件列表], "failed": [失败文件列表及错误]}
    """
    exclude_patterns = exclude_patterns or []
    results = {"success": [], "failed": []}

    # 查找所有 xlsx 文件
    excel_files = glob.glob(os.path.join(excel_dir, "*.xlsx"))

    # 过滤排除文件
    for pattern in exclude_patterns:
        excel_files = [f for f in excel_files if not pattern.replace("*", "") in os.path.basename(f)]

    if not excel_files:
        print("未找到 Excel 文件")
        return results

    print(f"找到 {len(excel_files)} 个 Excel 文件待转换\n")

    def convert_one(excel_path):
        try:
            convert_excel_to_table_md(excel_path, output_dir)
            return ("success", excel_path)
        except Exception as e:
            return ("failed", (excel_path, str(e)))
        except:
            return ("failed", (excel_path, "未知编码错误"))

    # 并行转换
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(convert_one, f): f for f in excel_files}

        for future in as_completed(futures):
            status, data = future.result()
            if status == "success":
                results["success"].append(data)
                basename = os.path.basename(data)
                print(f"✓ {basename}")
            else:
                excel_path, error = data
                results["failed"].append((excel_path, error))
                basename = os.path.basename(excel_path)
                print(f"✗ {basename}: {error}")

    return results


def main():
    parser = argparse.ArgumentParser(description="批量转换 Excel 为 Table MD")
    parser.add_argument("excel_dir", nargs="?", default="CDAP清单拆分",
                        help="Excel 文件目录（默认：CDAP清单拆分）")
    parser.add_argument("-o", "--output-dir",
                        default=".claude/skills/excel-to-table-md/references",
                        help="输出目录")
    parser.add_argument("-e", "--exclude", action="append", default=[],
                        help="排除的文件名模式（可多次使用）")
    parser.add_argument("-w", "--workers", type=int, default=MAX_WORKERS,
                        help=f"并行线程数（默认：{MAX_WORKERS}）")

    args = parser.parse_args()

    # 预设排除模式 + 用户指定
    exclude = ["副本", "清单目录"] + args.exclude

    print(f"Excel 目录: {args.excel_dir}")
    print(f"输出目录: {args.output_dir}")
    print(f"排除模式: {exclude}")
    print(f"并行线程: {args.workers}\n")

    results = batch_convert(args.excel_dir, args.output_dir, exclude)

    print(f"\n{'='*50}")
    print(f"转换完成：{len(results['success'])} 成功，{len(results['failed'])} 失败")

    if results["failed"]:
        print("\n失败文件：")
        for path, error in results["failed"]:
            print(f"  - {os.path.basename(path)}: {error}")


if __name__ == "__main__":
    main()
