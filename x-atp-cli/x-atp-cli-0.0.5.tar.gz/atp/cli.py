#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
import zipfile
import argparse
from pathlib import Path


def main():
    if len(sys.argv) == 1:
        sys.argv.append('--help')
    parser = argparse.ArgumentParser(description='X ATP CLI Client (X自动化测试平台命令行客户端)')
    parser.add_argument('-v', '--version', help='输出客户端的版本信息', action='store_true')
    parser.add_argument('-d', '--demo', help='在当前目录下创建x_sweetest_example项目', action='store_true')
    args = parser.parse_args()
    if args.version:
        print("当前客户端版本: v0.0.5")
    if args.demo:
        x_sweetest_dir = Path(__file__).resolve().parents[0]
        example_dir = x_sweetest_dir / 'example' / 'x_sweetest_example.zip'
        extract(str(example_dir), Path.cwd())
        print('生成 x_sweetest_example 成功\n快速体验, 请输入如下命令 (进入示例目录并启动运行脚本):\n\ncd x_sweetest_example\npython start.py')


def extract(z_file, path):
    f = zipfile.ZipFile(z_file, 'r')
    for file in f.namelist():
        f.extract(file, path)


if __name__ == '__main__':
    main()
