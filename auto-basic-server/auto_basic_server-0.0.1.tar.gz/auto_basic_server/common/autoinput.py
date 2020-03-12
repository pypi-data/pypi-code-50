# -*- coding: utf-8 -*-
"""
鼠标操作自动化方法
"""
import os
import time
import traceback
import win32api
import win32con
from ctypes import *

from common.logger import log

CLICK_MOUSE = 0
CLICK_MOUSE_DOUBLE = 1
CLICK_MOUSE_RIGHT = 2
MOVE_MOUSE = 3
CLICK_MOUSE_MIDDLE = 4
WITH_DRIVER = 5

g_driver = None


def click_mouse(x, y, with_driver=False, mode=CLICK_MOUSE, move_wait_time=0.1):
    """点击鼠标"""
    if with_driver:
        return handle_mouse_by_driver(x, y, mode, move_wait_time)
    move_mouse(x, y)
    if move_wait_time:
        time.sleep(move_wait_time)
    if mode == MOVE_MOUSE:
        return
    downMsg, upMsg = win32con.MOUSEEVENTF_LEFTDOWN, win32con.MOUSEEVENTF_LEFTUP
    if mode == CLICK_MOUSE_RIGHT:
        downMsg, upMsg = win32con.MOUSEEVENTF_RIGHTDOWN, win32con.MOUSEEVENTF_RIGHTUP
    elif mode == CLICK_MOUSE_MIDDLE:
        downMsg, upMsg = win32con.MOUSEEVENTF_MIDDLEDOWN, win32con.MOUSEEVENTF_MIDDLEUP

    win32api.mouse_event(downMsg, 0, 0, 0, 0)
    win32api.mouse_event(upMsg, 0, 0, 0, 0)
    if mode == CLICK_MOUSE_DOUBLE:
        win32api.mouse_event(downMsg, 0, 0, 0, 0)
        win32api.mouse_event(upMsg, 0, 0, 0, 0)


def click_mouse_double(x, y, with_driver=False):
    """点击鼠标（左键双击）"""
    if with_driver:
        handle_mouse_by_driver(x, y, CLICK_MOUSE_DOUBLE)
    else:
        click_mouse(x, y, False, CLICK_MOUSE_DOUBLE)


def click_mouse_right(x, y, with_driver=False):
    """点击鼠标（右键）"""
    if with_driver:
        handle_mouse_by_driver(x, y, CLICK_MOUSE_RIGHT)
    else:
        click_mouse(x, y, False, CLICK_MOUSE_RIGHT)


def handle_mouse_by_driver(x, y, mode, move_wait_time=0.1):
    """点击鼠标（右键）"""
    log.info("使用驱动点击坐标:{}-{}".format(x, y))
    try:
        global g_driver
        if g_driver is None:
            driver_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "VMOU_DLL.dll"))
            g_driver = CDLL(driver_path)
            log.info("驱动初始化结果:{}".format(g_driver.Init()))
        if not g_driver:
            return None
        log.info("驱动MoveTo结果:{}".format(g_driver.MoveTo(int(x), int(y))))
        time.sleep(move_wait_time)
        if mode == MOVE_MOUSE:
            return
        if mode == CLICK_MOUSE:
            log.info("驱动LeftClick结果:{}".format(g_driver.LeftClick(1)))
        elif mode == CLICK_MOUSE_RIGHT:
            g_driver.RightClick(1)
        elif mode == CLICK_MOUSE_MIDDLE:
            g_driver.MiddleClick(1)
        elif mode == CLICK_MOUSE_DOUBLE:
            g_driver.LeftDoubleClick(1)
    except:
        log.error("驱动点击鼠标异常了:{}".format(traceback.format_exc()))


def move_mouse(x, y, with_driver=False):
    """移动鼠标"""
    if with_driver:
        handle_mouse_by_driver(x, y, MOVE_MOUSE)
    else:
        w, h = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
        x, y = int(float(x) / w * 65535), int(float(y) / h * 65535)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE | win32con.MOUSEEVENTF_ABSOLUTE, x, y, 0, 0)


def wheel_mouse(dw_data=0):
    """鼠标滑轮滚动"""
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, dw_data, win32con.WHEEL_DELTA)


def get_cursor_pos():
    """获取当前坐标"""
    return win32api.GetCursorPos()
