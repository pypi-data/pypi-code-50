# -*- coding: utf-8 -*-
"""
注册表相关自动化方法
"""
import binascii
import ctypes
import os
import re
import struct
import sys
import win32api
import win32con
import winnt
import wmi

from common.autosys import is_win64

REG_SZ = win32con.REG_SZ
REG_DWORD = win32con.REG_DWORD
REG_MULTI_SZ = win32con.REG_MULTI_SZ
REG_EXPAND_SZ = win32con.REG_EXPAND_SZ


def get_sam_desired(attr, re_direct=False):
    sam_desired = attr
    if not re_direct:
        if struct.calcsize("P") == 8:  # python  64 位
            sam_desired = attr | win32con.KEY_WOW64_32KEY
        else:  # python  32 位
            sam_desired = attr | win32con.KEY_WOW64_64KEY
    return sam_desired

def _get_cur_file_dir():
    # 获取脚本路径
    path = sys.path[0]
    # 判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)

def has_key(key_full_name, re_direct=True):
    """返回注册表键是否存在

    :param key_full_name:   键全名
    :param re_direct:       是否开启重定向
    :return: 存在返回True，否则返回False
    """
    hreg = None
    root_key_name, sub_key_name, _re_direct = __trans_root_and_sub(key_full_name, re_direct)
    try:
        hreg = win32api.RegOpenKeyEx(root_key_name, sub_key_name, 0, get_sam_desired(win32con.KEY_READ, _re_direct))
    except Exception:
        return False
    finally:
        if hreg:
            win32api.RegCloseKey(hreg)
    return True

def __get_reg_sub_keys_list__(key_full_name, sub_keys, re_direct=False):
    """递归的方法寻找注册表路径下所有子健"""
    root_key_name, sub_key_name, __re_direct = __trans_root_and_sub(key_full_name, re_direct)
    hreg = None
    try:
        hreg = win32api.RegOpenKeyEx(root_key_name, sub_key_name, 0, get_sam_desired(win32con.KEY_READ, __re_direct))
        sub_key_tuple = win32api.RegEnumKeyEx(hreg)
    except:
        return False
    finally:
        if hreg:
            win32api.RegCloseKey(hreg)
    for sub_key in sub_key_tuple:
        sub_key_path = key_full_name + '\\' + sub_key[0]
        sub_keys.insert(0, sub_key_path)
        __get_reg_sub_keys_list__(sub_key_path, sub_keys)

def del_key(key_full_name, re_direct=True):
    """删除注册表中的某键(此操作会删除键级键的所有子键)

    :param key_full_name:   键全名
    :param re_direct:       是否开启重定向
    :return: 存在返回True，否则返回False
    """
    if has_key(key_full_name, re_direct):
        sub_keys_list = []
        __get_reg_sub_keys_list__(key_full_name, sub_keys_list)
        sub_keys_list.append(key_full_name)
        for sub_key in sub_keys_list:
            root_key_name, sub_key_name, _re_direct = __trans_root_and_sub(sub_key, re_direct)
            try:
                if is_win64():
                    win32api.RegDeleteKeyEx(root_key_name, sub_key_name, get_sam_desired(win32con.KEY_WRITE, _re_direct), 0)
                else:
                    win32api.RegDeleteKey(root_key_name, sub_key_name)
            except Exception:
                return False
        return True
    return True

def add_key(key_full_name, re_direct=True):
    """ 向注册表中添加键

    :param key_full_name: 键全名
    :param re_direct:     是否开启重定向
    :return:              存在返回True，否则返回False
    """
    b_exist = has_key(key_full_name, re_direct)
    if not b_exist:
        hreg = None
        root_key_name, sub_key_name, __re_direct = __trans_root_and_sub(key_full_name, re_direct)
        try:
            hreg, flag = win32api.RegCreateKeyEx(root_key_name, sub_key_name,
                                                 get_sam_desired(win32con.KEY_WRITE, __re_direct),
                                                 None, winnt.REG_OPTION_NON_VOLATILE, None, None)
        except:
            return False
        finally:
            if hreg:
                win32api.RegCloseKey(hreg)
    return True

def get_reg_value(key_name, sub_key_name, value_name, _type=win32con.KEY_READ):
    hreg = None
    try:
        hreg = win32api.RegOpenKeyEx(key_name, sub_key_name, 0, _type)
        return win32api.RegQueryValueEx(hreg, value_name)[0]
    except:
        return None
    finally:
        if hreg:
            win32api.RegCloseKey(hreg)

def get_key_value(key_full_name, value_name=None, re_direct=True):
    """获取注册表键的值

    :param key_full_name: 键全名
    :param value_name:    值名（可选，为None时返回键的默认值）
    :param re_direct:     是否开启重定向
    :return: 存在返回值，否则返回None
    """
    if has_key(key_full_name, re_direct):
        hreg = None
        root_key_name, sub_key_name, _re_direct = __trans_root_and_sub(key_full_name, re_direct)
        try:
            hreg = win32api.RegOpenKeyEx(root_key_name, sub_key_name, 0, get_sam_desired(win32con.KEY_READ, _re_direct))
            value_data, reg_type = win32api.RegQueryValueEx(hreg, value_name)
            if reg_type == win32con.REG_DWORD and value_data < 0:
                value_data = ctypes.c_uint(value_data).value
                if not value_data:
                    return None
                return value_data
            if reg_type == REG_MULTI_SZ:
                return get_multi_key_value(key_full_name, value_name)
            elif reg_type == win32con.REG_QWORD:
                ret = 0
                k = 0
                for i in value_data:
                    ret += ord(i) * (16 ** k)
                    k += 2
                # 10进制
                return ret
            elif reg_type == win32con.REG_BINARY:
                return binascii.b2a_hex(value_data)
            return str(value_data)
        except Exception:
            return None
        finally:
            if hreg:
                win32api.RegCloseKey(hreg)
    return None

def get_multi_key_value(key_full_name, value_name, re_direct=False):
    """获取多字符串值

    :param key_full_name:   键全名
    :param value_name:      值名（可选，为None时返回键的默认值）
    :param re_direct:       是否开启重定向
    :return:                存在返回值，否则返回None
    """
    c = wmi.WMI(namespace='DEFAULT').StdRegProv
    root_key_name, sub_key_name, _re_direct = __trans_root_and_sub(key_full_name, re_direct)
    r1, value = c.GetMultiStringValue(root_key_name, sub_key_name, value_name)
    return value

def has_key_value(key_full_name, value_name, re_direct=False):
    """判断是否有注册表值

    :param key_full_name: 键全名
    :param value_name: 值名（可选，为None时返回键的默认值）
    :param re_direct: 是否开启重定向
    :return: 存在返回True，否则返回False
    """
    if get_key_value(key_full_name, value_name, re_direct) is None:
        return False
    else:
        return True

def set_reg_value(key_name, sub_key_name, value_name, value_type, value,
        _type=win32con.WRITE_OWNER | win32con.KEY_ALL_ACCESS):
    hreg = None
    try:
        hreg = win32api.RegCreateKeyEx(key_name, sub_key_name, _type)[0]
        win32api.RegSetValueEx(hreg, value_name, 0, value_type, value)
        return True
    except:
        return False
    finally:
        if hreg:
            win32api.RegCloseKey(hreg)

def set_key_value(key_full_name, value_name, value_type, value, re_direct=True):
    """设置注册表键的值

    :param key_full_name:   键全名
    :param value_name:      值名
    :param value_type:      值类型
    :param value:           值
    :param re_direct:       是否开启重定向
    :return: 添加成功返回True，否则返回False
    """
    hreg = None
    add_key(key_full_name, re_direct)
    root_key_name, sub_key_name, _re_direct = __trans_root_and_sub(key_full_name, re_direct)
    try:
        hreg = win32api.RegOpenKeyEx(root_key_name, sub_key_name, 0, get_sam_desired(win32con.KEY_WRITE, _re_direct))
        if value_type == win32con.REG_DWORD:
            value = int(value)
        win32api.RegSetValueEx(hreg, value_name, 0, value_type, value)
    except Exception:
        return False
    finally:
        if hreg:
            win32api.RegCloseKey(hreg)
    return True

def del_key_value(key_full_name, value_name, re_direct=True):
    """删除注册表键的值

    :param key_full_name:   键全名
    :param value_name:      值名
    :param re_direct:       是否开启重定向
    :return:    删除成功返回True，否则返回False
    """
    if has_key(key_full_name, re_direct):
        hreg = None
        root_key_name, sub_key_name, _re_direct = __trans_root_and_sub(key_full_name, re_direct)
        try:
            hreg = win32api.RegOpenKeyEx(root_key_name, sub_key_name, 0, get_sam_desired(win32con.KEY_WRITE, _re_direct))
            win32api.RegDeleteValue(hreg, value_name)
        except:
            return False
        finally:
            if hreg:
                win32api.RegCloseKey(hreg)
    return True

def backup_key(key_full_name, backup_file_name):
    """备份注册表键下所有内容

    :param key_full_name:   键全名
    :param backup_file_name: 备份文件名
    :return:
    """
    cmd = r'REG SAVE %s "%s" /y 1> NUL 2> NUL' % (key_full_name, backup_file_name)
    if os.system(cmd) != 0:
        raise Exception('备份注册表键失败！%s' % key_full_name)

def restore_key(key_full_name, backup_file_name):
    """恢复注册表键下所有内容

    :param key_full_name:    键全名
    :param backup_file_name: 恢复文件名
    :return:
    """
    add_key(key_full_name)
    cmd = r'REG RESTORE %s "%s" 1> NUL 2> NUL' % (key_full_name, backup_file_name)
    if os.system(cmd) != 0:
        raise Exception('恢复注册表键失败！%s' % key_full_name)

def import_reg_file(reg_file):
    """导入注册表文件

    :param reg_file: 注册表文件路径
    :return:
    """
    cmd = r'REG IMPORT "%s" 1> NUL 2> NUL ' % reg_file
    os.system(cmd)
    if os.system(cmd) != 0:
        raise Exception('导入注册文件失败:"%s"' % reg_file)

def export_key(key_full_name, export_file_name):
    """导出注册表文件

    :param key_full_name:   键全名
    :param export_file_name: 注册表文件路径
    :return:
    """
    if os.path.exists(export_file_name):
        return False
    cmd = r'REG export "%s" "%s" 1> NUL' % (key_full_name, export_file_name)
    if os.system(cmd) != 0:
        return False
    return True

def trans_key_name(key_name):
    """注册表跟路径名称转换"""
    key_name = key_name.upper()
    if key_name in ['HKLM', 'HKEY_LOCAL_MACHINE']:
        key_name = win32con.HKEY_LOCAL_MACHINE
    elif key_name in ['HKCR', 'HKEY_CLASSES_ROOT']:
        key_name = win32con.HKEY_CLASSES_ROOT
    elif key_name in ['HKCU', 'HKEY_CURRENT_USER']:
        key_name = win32con.HKEY_CURRENT_USER
    elif key_name in ['HKU', 'HKEY_USERS']:
        key_name = win32con.HKEY_USERS
    elif key_name in ['HKCC', 'HKEY_CURRENT_CONFIG']:
        key_name = win32con.HKEY_CURRENT_CONFIG
    return key_name

def __trans_root_and_sub(key_full_name, b_redirect):
    name_list = key_full_name.split('\\', 1)
    root_key_name = trans_key_name(name_list[0])
    sub_key_name = None
    _b_redirect = b_redirect
    if len(name_list) == 2:
        sub_key_name = name_list[1]
        pos = sub_key_name.upper().find('WOW6432NODE\\')
        
        if struct.calcsize("P") == 8:  # 64位python判断逻辑与32位python刚好相反
            if pos != -1:
                _b_redirect = False
        else:
            if pos != -1 and not name_list[0] in ['HKCU', 'HKEY_CURRENT_USER']:
                sub_key_name = '%s%s' % (sub_key_name[0:pos], sub_key_name[pos + len('WOW6432NODE\\'):])
                _b_redirect = True
    
    return root_key_name, sub_key_name, _b_redirect

def _open_key(key_name, sub_key_name=None, _re_direct=False, key=win32con.KEY_ALL_ACCESS):
    try:
        return win32api.RegOpenKeyEx(key_name, sub_key_name, 0, get_sam_desired(key, _re_direct))
    except:
        return -1

def _get_all_value(key):
    res = {}
    index = 0
    while True:
        try:
            name, value, value_type = win32api.RegEnumValue(key, index)
            res[name] = (value, value_type)
            index += 1
        except:
            break
    return res

def get_reg_tree_info(key_full_name, open_key=win32con.KEY_ALL_ACCESS, re_direct=False):
    """得到注册表键及其所有子键的值信息(当键不存在时返回空dict)

    :param key_full_name:   键全名
    :param open_key:        打开权限
    :param re_direct:       是否重定向
    :return: 此操作返回一个dict，以注册表键全名为dict的键，以注册表键的值为了dict的值
    """
    if open_key is None:
        open_key = win32con.KEY_ALL_ACCESS
    stack = [key_full_name]
    res = {}
    while len(stack) != 0:
        key_full_name = stack.pop()
        root_key_name, sub_key_name, __re_direct = __trans_root_and_sub(key_full_name, re_direct)
        key = _open_key(root_key_name, sub_key_name, __re_direct, open_key)
        if key == -1:
            continue
        if not key:
            break
        # 枚举value
        value_map = _get_all_value(key)
        res[key_full_name] = value_map
        # 枚举子项
        try:
            key_name_list = list(win32api.RegEnumKeyEx(key))
            for key_name in key_name_list:
                stack.append(os.path.join(key_full_name, key_name[0]))
        except:
            win32api.RegCloseKey(key)
            continue
    
    return res

def enum_reg_values(key_full_name, re_direct=True):
    """枚举注册表键下的所有值(当键不存在时返回空list)

    :param key_full_name:   键全名
    :param re_direct:       是否重定向
    :return: 值列表
    """
    hreg = None
    root_key_name, sub_key_name, _re_direct = __trans_root_and_sub(key_full_name, re_direct)
    try:
        hreg = win32api.RegOpenKeyEx(root_key_name, sub_key_name, 0, get_sam_desired(win32con.KEY_READ, _re_direct))
        value_num = win32api.RegQueryInfoKey(hreg)[1]
        ret = []
        for i in range(value_num):
            ret.append(win32api.RegEnumValue(hreg, i)[0])
        return ret
    except Exception:
        import traceback
        print(traceback.format_exc())
        return []
    finally:
        if hreg:
            win32api.RegCloseKey(hreg)

def re_match_reg_key(key_full_name, re_direct=False):
    """支持路径中带通配符.*寻找匹配的注册表键

    :param key_full_name: 通配符.*的键
    :param re_direct:     是否重定向
    :return: 真实注册表键
    """
    if '.*' not in key_full_name:
        return key_full_name
    key_items = key_full_name.split('\\')
    ret = []
    for item in key_items:
        if '.*' not in item:
            ret.append(item)
        else:
            __key_full_name = '\\'.join(ret)
            tree_info = get_reg_tree_info(__key_full_name, win32con.KEY_READ, re_direct=re_direct)
            if not tree_info:
                return None
            findret = False
            for i in tree_info.keys():
                next_path = i.replace(__key_full_name + '\\', '').split('\\')[0]
                if re.match(item, next_path):
                    ret.append(next_path)
                    findret = True
                    break
            if not findret:
                return None
    return '\\'.join(ret)

def delete_reg_key(key_name, sub_key_name):
    try:
        return win32api.RegDeleteKey(key_name, sub_key_name)
    except:
        pass
    
def delete_reg_value(key_name, sub_key_name, value_name):
    if not get_reg_value(key_name, sub_key_name, value_name):
        return
    hreg = win32api.RegOpenKey(key_name, sub_key_name, 0, win32con.KEY_ALL_ACCESS)
    value = win32api.RegDeleteValue(hreg, value_name)
    if hreg:
        win32api.RegCloseKey(hreg)
    return value


if __name__ == '__main__':
    print((re_match_reg_key(r'HKEY_USERS\360SandBox\Device\HarddiskVolume.*\test')))
