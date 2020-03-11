import os
import subprocess


def get_process_id(process_name: str) -> list:
    """
    获得指定进程名的进程id
    :param process_name:进程名
    :return:
    """
    process = subprocess.Popen(["pgrep", "-f", process_name],
                               stdout=subprocess.PIPE,
                               shell=False)
    pid_infos = process.communicate()[0]
    return [pid for pid in pid_infos.decode("utf-8").split("\n") if pid != '']


def kill_process(process_name: str = None, process_port: int = None):
    """
    杀指定进程
    :param process_name:进程名
    :param process_port:端口号
    :return:
    """
    if process_name is not None:
        pids = get_process_id(process_name)
        for process_port in pids:
            os.system("sudo kill -s  9 " + process_port + " > /dev/null 2>&1 &")
    elif process_port is not None:
        info = os.popen(f"lsof -i:{process_port}| tr -s ' '|cut -d ' ' -f 2").readlines()
        if len(info) == 0:
            return
        else:
            os.system("sudo kill -s  9 " + info[1] + " > /dev/null 2>&1 &")
