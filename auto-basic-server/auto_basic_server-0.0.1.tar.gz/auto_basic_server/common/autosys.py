# -*- coding: utf-8 -*-
"""
系统相关自动化方法
"""

import os
import platform
import sys
import psutil
import socket


def is_win_system():
    """是否是windows系统"""
    if not sys.platform.startswith('win'):
        return False
    return True


def get_host_name():
    """获取主机名 Test-PC"""
    return socket.gethostname()


def get_system_type():
    """获取系统类型 Windows Linux"""
    return platform.system()


def is_win64():
    return 'PROGRAMFILES(X86)' in os.environ


def get_os_name():
    """获取系统的具体型号 例：Windows-7-6.1.7601-SP1"""
    return platform.platform()


def get_os_version():
    """获取系统版本号 例:6.1.7601"""
    return platform.version()


def get_phys_memory_size():
    """获取物理内存大小 单位byte"""
    mem = psutil.virtual_memory()
    return mem.total


def get_local_ip():
    """获取本地的ip"""
    try:
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        return ip
    except:
        raise Exception('get_local_ip Failed')
    finally:
        s.close()

Local_Ip = get_local_ip()

if __name__ == '__main__':
    print(os.environ)
    print(get_host_name())
    print(get_system_type())
    print(get_os_name())
    print(get_os_version())
    rst = get_phys_memory_size()
    print(rst/1024/1024/1024)

