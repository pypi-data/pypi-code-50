# -*- coding: utf-8 -*-
"""
进程自动化方法
"""
import subprocess
from time import sleep
import psutil

from common.autosys import Local_Ip
from common.common_logic import dispose_result


def get_process_names_by_psutil():
    """通过psutil获取进程名"""
    pnames = []
    pidlist = psutil.pids()
    for pid in pidlist:
        if psutil.pid_exists(pid):
            p = psutil.Process(pid)
            pnames.append(p.name().lower())
    return pnames


def exec_cmd(cmd, cwd=None, is_wait=True, timeout=15):
    rst = subprocess.Popen(cmd, cwd=cwd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                           shell=True)
    if is_wait:
        result = rst.communicate(timeout=timeout)
        result = dispose_result(result)
        return result
    else:
        return True


def exist_process_by_name(p_name):
    """判断指定name的进程是否存在"""
    return exist_process_by_names([p_name])


def exist_process_by_names(pname_list):
    """判断指定进程名的列表中进程是否都存在"""

    pnames = get_process_names_by_psutil()
    for pname in pname_list:
        if not pname.lower() in pnames:
            return False
    return True


def get_process_info_by_pname(p_name, process_type):
    pid_list = psutil.pids()
    for pid in pid_list:
        if not psutil.pid_exists(pid):
            continue
        p = psutil.Process(pid)
        if p.name() == p_name:
            if "id" == process_type:
                result = pid
            elif "cmdline" == process_type:
                result = p.cmdline()
            elif "username" == process_type:
                result = p.username()
            elif "status" == process_type:
                result = p.status()
            else:
                raise Exception("IP:{local_ip}process_type参数错误，没有属性：{0}".format(process_type, local_ip=Local_Ip))
            return result
    raise Exception("IP:{local_ip}没有找到进程名：{0}的进程".format(p_name, local_ip=Local_Ip))


def get_process_info_by_pid(pid, process_type):
    p = psutil.Process(pid)
    if "name" == process_type:
        result = p.name()
    elif "cmdline" == process_type:
        result = p.cmdline()
    elif "username" == process_type:
        result = p.username()
    elif "status" == process_type:
        result = p.status()
    else:
        result = None
    if result:
        return result
    raise Exception("IP:{local_ip}没有找到pid：{0}的进程".format(pid, local_ip=Local_Ip))


def get_process_info_by_cmdline(cmd_line, process_type):
    pid_list = psutil.pids()
    for pid in pid_list:
        if not psutil.pid_exists(pid):
            continue
        p = psutil.Process(pid)
        if p.cmdline() == cmd_line:
            if "id" == process_type:
                result = pid
            elif "name" == process_type:
                result = p.name()
            elif "username" == process_type:
                result = p.username()
            elif "status" == process_type:
                result = p.status()
            else:
                raise Exception("IP:{local_ip}process_type参数错误，没有属性：{0}".format(process_type, local_ip=Local_Ip))
            return result
    raise Exception("IP:{local_ip}没有找到进程指令行：{0}的进程".format(cmd_line, local_ip=Local_Ip))


def get_process_info_list_by_pname(p_name, process_type):
    result = list()
    pid_list = psutil.pids()
    for pid in pid_list:
        if not psutil.pid_exists(pid):
            continue
        p = psutil.Process(pid)
        if p.name() == p_name:
            if "id" == process_type:
                result.append(pid)
            elif "cmdline" == process_type:
                result.append(p.cmdline())
            elif "username" == process_type:
                result.append(p.username())
            elif "status" == process_type:
                result.append(p.status())
            else:
                raise Exception("IP:{local_ip}process_type参数错误，没有属性：{0}".format(process_type, local_ip=Local_Ip))
    if result:
        return result
    else:
        raise Exception("IP:{local_ip}没有找到进程名：{0}的进程".format(p_name, local_ip=Local_Ip))


def get_process_info_list_by_username(user_name, process_type):
    result = list()
    pid_list = psutil.pids()
    for pid in pid_list:
        if not psutil.pid_exists(pid):
            continue
        p = psutil.Process(pid)
        if p.username() == user_name:
            if "id" == process_type:
                result.append(pid)
            elif "cmdline" == process_type:
                result.append(p.cmdline())
            elif "name" == process_type:
                result.append(p.name())
            # elif "status" == process_type:
            #     result.append(p.status())
            else:
                raise Exception("IP:{local_ip}process_type参数错误，没有属性：{0}".format(process_type, local_ip=Local_Ip))
    if result:
        return result
    else:
        raise Exception("IP:{local_ip}没有找到用户名：{0}的进程".format(user_name, local_ip=Local_Ip))


def kill_process_by_name(p_name):
    """杀掉指定name的进程"""
    kill_process_by_names([p_name])


def kill_process_by_names(pname_list, user=None):
    """杀掉指定name的进程列表"""
    pid_list = psutil.pids()
    for pid in pid_list:
        if not psutil.pid_exists(pid):
            continue
        p = psutil.Process(pid)
        if user and not user == p.username():
            continue
        if p.name() in pname_list:
            p.kill()
    sleep(0.6)
    if not exist_process_by_names(pname_list):
        return True
    raise Exception("IP:{local_ip}根据进程名列表:{0}杀死进程失败".format(pname_list, local_ip=Local_Ip))


def kill_process_by_id(pid):
   return kill_process_by_ids([pid])


def kill_process_by_ids(pid_list: list):
    for pid in pid_list:
        if not psutil.pid_exists(pid):
            continue
        p = psutil.Process(pid)
        p.kill()
        sleep(0.6)
        if psutil.pid_exists(pid):
            raise Exception("IP:{local_ip}根据pid:{0}杀死进程失败".format(pid, local_ip=Local_Ip))
    return True


def kill_process_by_cmd_line(cmd_line):
    pid_list = psutil.pids()
    for pid in pid_list:
        if not psutil.pid_exists(pid):
            continue
        p = psutil.Process(pid)
        if p.cmdline() == cmd_line:
            p.kill()
            sleep(0.6)
            if psutil.pid_exists(pid):
                raise Exception("IP:{local_ip}根据指令行:{0}杀死进程失败".format(cmd_line, local_ip=Local_Ip))
    return True


def show_process_cpu_percent_by_id(pid):
    """
    根据pid查看进程的CPU占用率
    :param pid:     进程pid
    :return:        进程占用率
    """
    cpu_num = psutil.cpu_count()
    pro = psutil.Process(pid)
    cpu = pro.cpu_percent(interval=1)
    cpu_percent = cpu / cpu_num
    return cpu_percent


if __name__ == '__main__':
    print(kill_process_by_cmd_line(["python", "flask_server.py"]))
    # kill_process_by_cmd_line(['D:\\软件\\TeamViewer.exe'])
    # pidlist = psutil.pids()
    # for pid in pidlist:
    #     p = psutil.Process(pid)
    #     print("pid:", pid, "name:", p.name(), "username：", p.username(), "cmdline:", p.cmdline())
    # print(kill_process_by_names("chrome.exe"))

    # print(get_process_names_by_psutil())
    # # print(get_process_status_by_name('360skylarsvc.exe'))
    #
    # print(get_process_id_by_name('chrome.exe'))

    # cmd = 'mspaint'
    # print(create_process(cmd, True))
