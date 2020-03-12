#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
窗口操作自动化方法
"""
import ctypes
import re
import struct
import time
import win32api
import win32process
import win32con
import win32gui

from common import autoutil, autoinput

# 窗口基类
from common.autoproc import exec_cmd
from common.logger import log


def parse_click_config(clk_cfg):
    """解析配置文件"""
    if clk_cfg is None:
        return None, None, autoinput.CLICK_MOUSE, False
    if type(clk_cfg) == int:
        return None, None, clk_cfg, False
    if len(clk_cfg) == 2:
        return clk_cfg[0], clk_cfg[1], autoinput.CLICK_MOUSE, False
    if len(clk_cfg) == 3:
        return clk_cfg[0], clk_cfg[1], autoinput.CLICK_MOUSE, clk_cfg[3]
    return clk_cfg


def parse_title_config(title_cfg):
    """解析配置文件title"""
    if type(title_cfg) == str:
        return title_cfg, None, False
    if len(title_cfg) == 2:
        if type(title_cfg[1]) == bool:
            return title_cfg[0], None, title_cfg[1]
        return title_cfg[0], title_cfg[1], False
    return title_cfg


def click_window(h_wnd, clk_cfg=None):
    """点击窗口"""
    top_window(h_wnd)
    rect = get_window_rect(h_wnd)
    if not rect:
        return
    x, y, mode, with_driver = parse_click_config(clk_cfg)
    if x is None:
        x = (rect[0] + rect[2]) / 2
    elif x < 0:
        x += rect[2]
    else:
        x += rect[0]
    if y is None:
        y = (rect[1] + rect[3]) / 2
    elif y < 0:
        y += rect[3]
    else:
        y += rect[1]
    autoinput.click_mouse(x, y, with_driver, mode)


def click_window_for(h_wnd, timeout, cond, clk_cfg=None):
    """点击窗口等待条件满足 """
    if type(timeout) is list:
        timeout = tuple(timeout)

    def __click_window_for__(h_wnd, cond, clk_cfg):
        rst = cond.do()
        if not rst or isinstance(rst, Exception):
            click_window(h_wnd, clk_cfg)
        return rst

    return autoutil.handle_timeout(__click_window_for__, timeout, h_wnd, cond, clk_cfg)


def click_window_for_close(h_wnd, timeout, tgt_hwnd, clk_cfg=None):
    """点击窗口等待某窗口关闭"""
    if type(timeout) is list:
        timeout = tuple(timeout)
    cond = not win32gui.IsWindow(tgt_hwnd)
    return click_window_for(h_wnd, timeout, cond, clk_cfg)


def click_window_for_close_self(h_wnd, timeout, clk_cfg=None):
    """点击窗口等待该窗口关闭"""
    if type(timeout) is list:
        timeout = tuple(timeout)
    return click_window_for_close(h_wnd, timeout, h_wnd, clk_cfg)


def click_window_for_find(h_wnd, timeout, title_cfg, clk_cfg=None):
    """点击窗口等待找到某窗口"""
    if type(timeout) is list:
        timeout = tuple(timeout)
    title, parentTitle, isRaw = parse_title_config(title_cfg)
    cond = find_window(title, parentTitle, isRaw)
    return click_window_for(h_wnd, timeout, cond, clk_cfg)


def click_window_for_find_child(h_wnd, timeout, title_cfg, clk_cfg=None):
    """点击窗口等待找到该窗口的某子窗口"""
    if type(timeout) is list:
        timeout = tuple(timeout)
    if type(title_cfg) == tuple:
        title_cfg = title_cfg[0], h_wnd, title_cfg[1]
    else:
        title_cfg = title_cfg, h_wnd
    return click_window_for_find(h_wnd, timeout, title_cfg, clk_cfg)


def click_window_for_hidden(h_wnd, timeout, tgt_hwnd, clk_cfg=None):
    """点击窗口等待某窗口不可见"""
    if type(timeout) is list:
        timeout = tuple(timeout)
    cond = not win32gui.IsWindowVisible(tgt_hwnd)
    return click_window_for(h_wnd, timeout, cond, clk_cfg)


def click_window_for_hidden_self(h_wnd, timeout, clk_cfg=None):
    """点击窗口等待该窗口不可见"""
    if type(timeout) is list:
        timeout = tuple(timeout)
    return click_window_for_hidden(h_wnd, timeout, h_wnd, clk_cfg)


def find_raw_window(title, parent_title=None):
    """查找第一个窗口（包含不可见、不可用、阻塞）"""
    return find_windows(title, parent_title, True, True)


def find_raw_windows(title, parent_title=None):
    """查找窗口（包含不可见、不可用、阻塞）"""
    return find_windows(title, parent_title, True)


def find_window(title, parent_title=None, is_raw=False):
    """查找第一个窗口"""
    return find_windows(title, parent_title, is_raw, True)


def find_windows(title, parent_title=None, is_raw=False, return_first=False):
    """查找窗口"""
    def __fill_window_attrs__(h_wnd, rst):
        if not return_first:
            rst.add(h_wnd)
        elif __match_window__(h_wnd, title):
            rst.add(h_wnd)

    def __enum_child_windows__(h_wnd, h_wnds):
        h_wnds.add(h_wnd)
        rst = set()
        if not h_wnd:
            autoutil.try_except(win32gui.EnumWindows, __fill_window_attrs__, rst)
        else:
            autoutil.try_except(win32gui.EnumChildWindows, h_wnd, __fill_window_attrs__, rst)
            crst = set()
            for cwnd in rst:
                if cwnd not in h_wnds:
                    crst.update(__enum_child_windows__(cwnd, h_wnds))
            rst.update(crst)
        return rst

    def __find_child_windows__(h_wnd, h_wnds):
        h_wnds.add(h_wnd)
        rst = set()
        hcwnd = autoutil.try_except(win32gui.FindWindowEx, h_wnd, None, None, None)
        while hcwnd and not isinstance(hcwnd, Exception) and hcwnd not in h_wnds:
            __fill_window_attrs__(hcwnd, rst)
            if h_wnd:
                rst.update(__find_child_windows__(hcwnd, h_wnds))
            hcwnd = autoutil.try_except(win32gui.FindWindowEx, h_wnd, hcwnd, None, None)
        return rst

    def __get_child_windows__(h_wnd, h_wnds):
        h_wnds.add(h_wnd)
        rest = set()
        hcwnd = autoutil.try_except(win32gui.GetWindow, h_wnd or win32gui.GetDesktopWindow(), win32con.GW_CHILD)
        while hcwnd and not autoutil.is_except(hcwnd) and hcwnd not in h_wnds:
            __fill_window_attrs__(hcwnd, rest)
            if h_wnd:
                rest.update(__get_child_windows__(hcwnd, h_wnds))
            hcwnd = autoutil.try_except(win32gui.GetWindow, hcwnd, win32con.GW_HWNDNEXT)
        return rest

    def __match_window__(h_wnd, title):
        if not is_raw and is_raw_window(h_wnd):
            return False
        if type(title) == int:
            return win32gui.GetDlgCtrlID(h_wnd) == title
        text = re.split('([\r|\n])+', get_window_text(h_wnd))
        text = text[0].strip()
        if text == title or re.match('^' + title + '$', text, re.S):
            return True
        clazz = get_window_class(h_wnd).strip().decode('utf-8')
        if clazz == title or re.match('^' + title + '$', clazz, re.S):
            return True
        return False

    if not parent_title:
        hpwndList = [None]
    elif type(parent_title) == int:
        hpwndList = [parent_title]
    else:
        hpwndList = find_raw_windows(parent_title)
    rst = set()
    for hpwnd in hpwndList:
        rst.update(__enum_child_windows__(hpwnd, set()))
        if return_first and rst:
            return rst.pop()
        rst.update(__find_child_windows__(hpwnd, set()))
        if return_first and rst:
            return rst.pop()
        rst.update(__get_child_windows__(hpwnd, set()))
        if return_first and rst:
            return rst.pop()
    if return_first:
        return 0
    else:
        lst = []
        for h_wnd in rst:
            if __match_window__(h_wnd, title):
                lst.append(h_wnd)
        return lst


def get_desktop_rect():
    """获取桌面尺寸"""
    return get_window_rect(win32gui.GetDesktopWindow())


def get_parent_window(h_wnd):
    """获取父窗口"""
    h_wnd = autoutil.try_except(win32gui.GetParent, h_wnd)
    if not autoutil.is_except(h_wnd):
        return h_wnd


def get_window_class(h_wnd, buf=ctypes.create_string_buffer(256)):
    """获取窗口类名"""
    if buf is None:
        buf = ctypes.create_string_buffer(256)
    size = ctypes.sizeof(buf)
    ctypes.memset(buf, 0, size)
    ctypes.windll.user32.GetClassNameA(h_wnd, ctypes.addressof(buf), size - 2)
    return buf.value.strip()


def get_window_rect(h_wnd):
    """获得窗口尺寸"""
    rect = autoutil.try_except(win32gui.GetWindowRect, h_wnd)
    if not autoutil.is_except(rect):
        return rect


def get_window_size(h_wnd):
    """获取窗口大小"""
    rect = get_window_rect(h_wnd)
    if not rect:
        return None
    return rect[2] - rect[0], rect[3] - rect[1]


def find_window_with_size(title, size, parent_title=None, is_raw=False):
    """根据size查找窗口"""
    hs = find_windows(title, parent_title, is_raw=is_raw)
    hs = filter(lambda h: get_window_size(h) == size, hs)
    if hs:
        return hs[0]
    else:
        return None


def get_window_text(h_wnd, buf=None):
    """获取窗口文字"""
    if buf is None:
        # get the length of control text
        gtlResult = autoutil.try_except(win32gui.SendMessageTimeout, h_wnd, win32con.WM_GETTEXTLENGTH, 0, 0,
                                        win32con.SMTO_ABORTIFHUNG, 30)

        if not isinstance(gtlResult, tuple):
            log.warn("gtlResult type:{0},value:{1}".format(type(gtlResult), gtlResult))
            return None
        # if the test is null then return empty string
        if gtlResult[0] == 1 and gtlResult[1] == 0:
            buf = ctypes.create_unicode_buffer(1)
            ctypes.memset(buf, 0, ctypes.sizeof(buf))
            return buf.value.strip()

        # calc and allocate the buffer
        len = gtlResult[1] + 1
        buf = ctypes.create_unicode_buffer(len)

    # reset the buffer
    size = ctypes.sizeof(buf)
    ctypes.memset(buf, 0, size)

    # get the text of control (u must make sure the buffer length is enough)
    autoutil.try_except(ctypes.windll.user32.SendMessageTimeoutW, h_wnd, win32con.WM_GETTEXT, size, buf,
                        win32con.SMTO_ABORTIFHUNG, 30)

    # buf -> Unicode
    return buf.value.strip()


def set_window_text(h_wnd, text):
    """设置窗口文字 """
    rst = autoutil.try_except(win32gui.SendMessageTimeout, h_wnd, win32con.WM_SETTEXT, 0, text,
                              win32con.SMTO_ABORTIFHUNG,
                              30)
    return not autoutil.is_except(rst)


def is_raw_window(h_wnd):
    """判断是否为非正常窗口"""
    return not win32gui.IsWindowVisible(h_wnd) or not win32gui.IsWindowEnabled(
        h_wnd) or ctypes.windll.user32.IsHungAppWindow(h_wnd)


def normal_window(h_wnd):
    """还原窗口"""
    try:
        win32gui.ShowWindow(h_wnd, win32con.SW_NORMAL)
    except:
        pass


def max_window(h_wnd):
    """最大化窗口"""
    return win32gui.ShowWindow(h_wnd, win32con.SW_SHOWMAXIMIZED) and top_window(h_wnd)


def min_window(h_wnd):
    """最小化窗口"""
    return win32gui.ShowWindow(h_wnd, win32con.SW_SHOWMINIMIZED)


def show_window(h_wnd):
    """显示默认窗口"""
    return win32gui.ShowWindow(h_wnd, win32con.SW_SHOWDEFAULT) and top_window(h_wnd)


def get_top_parent_window_this_process(h_wnd):
    _, pid = win32process.GetWindowThreadProcessId(h_wnd)
    found_hwnd = h_wnd
    while True:
        h_wnd = get_parent_window(h_wnd)
        _, found_pid = win32process.GetWindowThreadProcessId(h_wnd)
        if found_pid != pid:
            return found_hwnd
        found_hwnd = h_wnd


def top_window(h_wnd):
    hwndParent = get_top_parent_window_this_process(h_wnd)

    # force topmost window
    win32gui.SetWindowPos(hwndParent, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

    # fore window
    autoutil.try_except(win32gui.SetForegroundWindow, hwndParent)


def move_window(h_wnd, x, y):
    left, top, right, bottom = get_window_rect(h_wnd)
    w = right - left
    h = bottom - top
    win32gui.SetWindowPos(h_wnd, win32con.HWND_TOPMOST, x, y, w, h, 0)
    return True


def move_window_by_click(h_wnd, x, y):
    top_window(h_wnd)
    a = 10
    while a:
        left, top, right, bottom = get_window_rect(h_wnd)
        if left == x and right == y:
            break
        pos = left + (right - left) / 2, top + 10
        autoinput.move_mouse(pos[0], pos[1])
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        autoinput.move_mouse(x + (right - left) / 2, y)
        time.sleep(0.1)
        a -= 1
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def alert_message(msg, text='', style=win32con.MB_ICONINFORMATION):
    """显示消息框"""
    if style is None:
        style = win32con.MB_ICONINFORMATION
    return win32gui.MessageBox(None, msg, text, style | win32con.MB_SYSTEMMODAL)


def alert_error(error, text=''):
    """显示错误框"""
    return alert_message(error, text, win32con.MB_ICONERROR)


def alert_choice(choice, text=''):
    """显示选择框"""
    return alert_message(choice, text, win32con.MB_YESNO | win32con.MB_ICONQUESTION) == win32con.IDYES


def gui_ctrl_tree_view_select_item(h_wnd, h_item, i_flag=0):
    TVGN_CARET = 0x0009
    TV_FIRST = 0x1100
    TVM_SELECTITEM = (TV_FIRST + 11)

    if i_flag == 0:
        i_flag = TVGN_CARET
    return win32api.SendMessage(h_wnd, TVM_SELECTITEM, i_flag, h_item)


def gui_ctrl_tree_view_find_item_ex(tree_wnd, target_path):
    TV_FIRST = 0x1100
    TVGN_ROOT = 0x0000

    TVM_EXPAND = (TV_FIRST + 2)

    TVM_GETNEXTITEM = TV_FIRST + 10
    TVM_GETITEMW = TV_FIRST + 62
    CCM_FIRST = 0x2000
    TVM_GETUNICODEFORMAT = CCM_FIRST + 6

    TVM_GETITEMA = (TV_FIRST + 12)
    TVM_GETITEMW = (TV_FIRST + 62)
    TVM_ENSUREVISIBLE = (TV_FIRST + 20)

    TVIF_TEXT = 0x0001
    TVGN_NEXT = 0x0001
    TVE_EXPAND = 0x0002
    TVGN_CHILD = 0x0004
    TVE_COLLAPSE = 0x0001

    class TagTviteMex(ctypes.Structure):
        _fields_ = [
            ("mask", ctypes.c_uint),
            ("hItem", ctypes.c_uint),
            ("state", ctypes.c_uint),
            ("stateMask", ctypes.c_uint),
            ("pszText", ctypes.c_uint),
            ("cchTextMax", ctypes.c_int),
            ("iImage", ctypes.c_int),
            ("iSelectedImage", ctypes.c_int),
            ('cChildren', ctypes.c_int),
            ('lParam', ctypes.c_uint),
            ('iIntegral', ctypes.c_int),
            ('uStateEx', ctypes.c_uint),
            ('hwnd', ctypes.c_uint),
            ('iExpandedImage', ctypes.c_int),
            ('iReserved', ctypes.c_int)
        ]

    GetWindowThreadProcessId = ctypes.windll.user32.GetWindowThreadProcessId
    VirtualAllocEx = ctypes.windll.kernel32.VirtualAllocEx
    ReadProcessMemory = ctypes.windll.kernel32.ReadProcessMemory
    OpenProcess = ctypes.windll.kernel32.OpenProcess

    parent_wnd = win32gui.SendMessage(tree_wnd, TVM_GETNEXTITEM, TVGN_ROOT, 0)
    bUnicode = win32gui.SendMessage(tree_wnd, TVM_GETUNICODEFORMAT, 0, 0)
    pBuffer = None
    if bUnicode:
        pBuffer = ctypes.create_unicode_buffer(4096)
    else:
        pBuffer = ctypes.create_string_buffer(4096)
    tagTVITEMEX_size = ctypes.sizeof(TagTviteMex)

    total_size = 4096 + tagTVITEMEX_size
    pid = ctypes.create_string_buffer(4)
    p_pid = ctypes.addressof(pid)
    GetWindowThreadProcessId(tree_wnd, p_pid)  # process owning the given hwnd
    hProcess = OpenProcess(win32con.PROCESS_ALL_ACCESS, False, struct.unpack("i", pid)[0])
    lpRemoteBuffer = VirtualAllocEx(hProcess, 0, total_size, win32con.MEM_RESERVE | win32con.MEM_COMMIT,
                                    win32con.PAGE_READWRITE)

    def __get_text(h_item_start, lp_buffer):

        tag_tv_item_ex_local = TagTviteMex()
        tag_tv_item_ex_local.mask = TVIF_TEXT
        tag_tv_item_ex_local.hItem = h_item_start
        tag_tv_item_ex_local.cchTextMax = 4096
        tag_tv_item_ex_local.pszText = lp_buffer + tagTVITEMEX_size

        ctypes.windll.kernel32.WriteProcessMemory(hProcess, lpRemoteBuffer, ctypes.addressof(tag_tv_item_ex_local),
                                                  tagTVITEMEX_size, 0)

        if bUnicode:
            b_ret = win32gui.SendMessage(tree_wnd, TVM_GETITEMW, 0, lpRemoteBuffer)
        else:
            b_ret = win32gui.SendMessage(tree_wnd, TVM_GETITEMA, 0, lpRemoteBuffer)

        if not b_ret:
            print('error,SendMessage execute error,GetLastError:%d' % win32api.GetLastError())

        if not ReadProcessMemory(hProcess, lpRemoteBuffer + tagTVITEMEX_size, ctypes.addressof(pBuffer), 4096, p_pid) or \
                not struct.unpack("i", pid)[0] == 4096:
            print('ReadProcessMemory execute error')

        return pBuffer.value.strip()

    def __expend_Item(h_target_tree, l_expend_type, h_item_start):

        win32api.SendMessage(h_target_tree, TVM_EXPAND, l_expend_type, h_item_start)
        if l_expend_type == TVE_EXPAND:
            win32api.SendMessage(h_target_tree, TVM_ENSUREVISIBLE, 0, h_item_start)

        h_item = win32api.SendMessage(h_target_tree, TVM_GETNEXTITEM, TVGN_CHILD, h_item_start)

        while h_item:
            h_child = win32api.SendMessage(h_target_tree, TVM_GETNEXTITEM, TVGN_CHILD, h_item)
            if h_child:
                __expend_Item(h_target_tree, l_expend_type, h_item)
            h_item = win32api.SendMessage(h_target_tree, TVM_GETNEXTITEM, TVGN_NEXT, h_item)

    def __get_first_child(h_wnd, h_item):
        return win32api.SendMessage(h_wnd, TVM_GETNEXTITEM, TVGN_CHILD, h_item)

    def __get_next_sibling(h_wnd, h_item):
        return win32api.SendMessage(h_wnd, TVM_GETNEXTITEM, TVGN_NEXT, h_item)

    split_list = target_path.split('\\')
    i_index = 0

    while parent_wnd and i_index < len(split_list):

        if __get_text(parent_wnd, lpRemoteBuffer) == split_list[i_index]:
            i_index = i_index + 1
            __expend_Item(tree_wnd, TVE_EXPAND, parent_wnd)
            if i_index < len(split_list):
                parent_wnd = __get_first_child(tree_wnd, parent_wnd)
        else:

            parent_wnd = __get_next_sibling(tree_wnd, parent_wnd)
            __expend_Item(tree_wnd, TVE_COLLAPSE, parent_wnd)

    win32api.CloseHandle(hProcess)
    ctypes.windll.kernel32.VirtualFreeEx(hProcess, lpRemoteBuffer, total_size, win32con.MEM_FREE)
    return parent_wnd


def select_file_path_in_tree_view(parent_hwnd, target_path):
    tree_wnd = find_window('SysTreeView32', parent_hwnd)
    if not tree_wnd:
        raise Exception('error,can not find dlg to choose fold')

    parent_wnd = gui_ctrl_tree_view_find_item_ex(tree_wnd, target_path)
    b_ret = gui_ctrl_tree_view_select_item(tree_wnd, parent_wnd)
    try:
        top_window(parent_hwnd)
        b_ret = gui_ctrl_tree_view_select_item(tree_wnd, parent_wnd)
    except:
        pass
    return b_ret


def find_window_tree(h_parent, lpsz_class, lpsz_window):
    # 查找本层窗口
    h_wnd_result = win32gui.FindWindowEx(h_parent, None, lpsz_class, lpsz_window)
    if h_wnd_result:
        return h_wnd_result

    # 查找子窗口
    h_wnd = win32gui.FindWindowEx(h_parent, None, None, None)
    while h_wnd:
        h_wnd_result = find_window_tree(h_wnd, lpsz_class, lpsz_window)
        if h_wnd_result != 0 and h_wnd_result:
            return h_wnd_result
        h_wnd = win32gui.FindWindowEx(h_parent, h_wnd, None, None)

    # 无法找到窗口，返回空
    return None


def window_click_button(str_class, str_caption, str_button_text):
    # 查找对应窗口
    h_wnd_main = win32gui.FindWindow(str_class, str_caption)
    if h_wnd_main is None:
        return False

    # 查找对应控件
    h_wnd_ctrl = find_window_tree(h_wnd_main, None, str_button_text)
    if h_wnd_ctrl is None:
        return False

    # 发送鼠标单击消息，光标位置使用 (0, 0)
    win32gui.SendMessage(h_wnd_ctrl, win32con.WM_LBUTTONDOWN, win32con.VK_LBUTTON, None)
    win32gui.SendMessage(h_wnd_ctrl, win32con.WM_LBUTTONUP, 0, None)
    return True


if __name__ == "__main__":
    exec_cmd(r'C:\360GetMD5Ctrl_setup.exe', is_wait=False)
    h_wnds = find_windows(title='Button', parent_title='#32770')
    for hwnd in h_wnds:
        top_window(hwnd)
        window_text = get_window_text(hwnd)
        print(type(window_text), window_text)
        if window_text == "我接受(&I)":
            print(window_text)
            print(click_window(hwnd))

