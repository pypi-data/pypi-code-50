# -*- coding: utf-8 -*-
"""
获取系统的环境变量,获取相应路径
"""
import os
import traceback
import win32api
from win32comext.shell import shell, shellcon
from common.logger import log


def __get_special_path(ptype):
    idList = shell.SHGetSpecialFolderLocation(0, ptype)
    return shell.SHGetPathFromIDList(idList)

def __get_path__(path, file_name=None):
    try:
        if file_name:
            file_name = os.path.basename(file_name)
            return os.path.join(path, file_name)
        if isinstance(path, bytes):
            path = path.decode()
        return path
    except:
        log.error(traceback.format_exc())
        return ""

def get_cookies_path(file_name=None):
    return __get_path__(__get_special_path(shellcon.CSIDL_COOKIES), file_name)

def get_local_app(file_name=None):
    return __get_path__(__get_special_path(shellcon.CSIDL_LOCAL_APPDATA), file_name)

def get_temp_path(file_name=None):
    if file_name:
        return os.path.join(win32api.GetLongPathName(os.environ['TMP']), file_name)
    else:
        return win32api.GetLongPathName(os.environ['TMP'])

def get_windows_temp_path(file_name=None):
    if file_name:
        return os.path.join(win32api.GetLongPathName(os.environ['SYSTEMROOT']), 'Temp', file_name)
    else:
        return os.path.join(win32api.GetLongPathName(os.environ['SYSTEMROOT']), 'Temp')

def get_public_path(file_name=None):
    public_path = os.path.join(os.environ['HOMEDRIVE'], r'Users\Public')
    if file_name:
        return os.path.join(public_path, file_name)
    else:
        return public_path

def get_common_app(file_name=None):
    return __get_path__(__get_special_path(shellcon.CSIDL_COMMON_APPDATA), file_name)

def get_desktop_path(file_name=None):
    return __get_path__(__get_special_path(shellcon.CSIDL_DESKTOP), file_name)

def get_start_menu_path(file_name=None):
    return __get_path__(__get_special_path(shellcon.CSIDL_STARTMENU), file_name)

def get_common_start_menu_path(file_name=None):
    return __get_path__(__get_special_path(shellcon.CSIDL_COMMON_STARTMENU), file_name)

def get_favorite_path(file_name=None):
    return __get_path__(__get_special_path(shellcon.CSIDL_FAVORITES), file_name)

def get_personal_path(file_name=None):
    return __get_path__(__get_special_path(shellcon.CSIDL_PERSONAL), file_name)

def get_desktop_directory_path(file_name=None):
    return __get_path__(__get_special_path(shellcon.CSIDL_DESKTOPDIRECTORY), file_name)

def get_common_desktop_directory_path(file_name=None):
    return __get_path__(__get_special_path(shellcon.CSIDL_COMMON_DESKTOPDIRECTORY), file_name)

def get_fonts_path(file_name=None):
    return __get_path__(__get_special_path(shellcon.CSIDL_FONTS), file_name)

def get_pro_grams_path(file_name=None):
    return __get_path__(__get_special_path(shellcon.CSIDL_PROGRAMS), file_name)

def get_internet_cache_path(file_name=None):
    return __get_path__(__get_special_path(shellcon.CSIDL_INTERNET_CACHE), file_name)

def get_app_data(file_name=None):
    return __get_path__(__get_special_path(shellcon.CSIDL_APPDATA), file_name)

def get_quick_launch_path():
    return os.path.join(get_app_data(), 'Microsoft\\Internet Explorer\\Quick Launch')

