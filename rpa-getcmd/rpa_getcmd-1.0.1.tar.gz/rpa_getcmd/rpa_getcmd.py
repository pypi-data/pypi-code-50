"""
@Version: 1.0.0
@Author: qi.you
@File: rpa_getcmd.py
@Time: 2020/3/6 10:42
@Describe: 获取RPA传入的参数并解析，包括程序名和json参数
"""

import json
import sys


def getcmd():
    print('获取RPA传入的参数并解析，包括程序名和json参数')
    try:
        jsonpath = ''
        exename = ''
        load_dict = {}
        if len(sys.argv) > 2:
            exename = sys.argv[1]
            jsonpath = sys.argv[2].replace('\\', '/')
        if jsonpath:
            with open(jsonpath, 'r') as load_f:
                load_dict = json.load(load_f)
        return exename, eval(load_dict)
    except Exception as e:
        return e, e




if __name__=="__main__":
    exename, load_dict=getcmd()
    print(exename, load_dict)