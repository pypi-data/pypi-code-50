# -*- coding: utf-8 -*-
"""
自动化常用操作
"""
import os
import time
import traceback

from PIL import ImageGrab


def try_except(func, *params, **param_map):
    """在try中执行"""
    try:
        return func(*params, **param_map)
    except Exception as e:
        traceback.print_exc()
        return e


def handle_timeout(func, timeout, *params, **param_map):
    """在超时范围内执行

    :param func: 函数名
    :param timeout: timeout为数值或元组（超时时长,间隔时间）
    :param params: 参数
    :param param_map: 参数map
    :return:
    """
    interval = 0.6
    if type(timeout) == tuple:
        timeout, interval = timeout
    rst = None
    while timeout > 0:
        time_start = time.perf_counter()
        try:
            rst = func(*params, **param_map)
        except:
            pass
        if rst and not isinstance(rst, Exception):
            break
        time.sleep(interval)
        timeout -= time.perf_counter() - time_start
    return rst


def is_except(e, e_type=Exception):
    """判断是否为异常"""
    return isinstance(e, e_type)


def return_root_path():
    """返回工程的根目录"""
    return os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

# 获取屏幕截图
def grab_screen(path=None):
    return grab(None, path)


# 获取指定区域的截图
def grab(rect, path=None):
    img = ImageGrab.grab(rect)
    if path:
        img.save(path, 'PNG')
    return img

