import time
from abc import abstractmethod
from typing import List, Tuple

from ddcmaker.basic.system.host import Host


class BasicMaker:
    def __init__(self, maker_name: str, sleep_time: int = 1):
        self.maker_name = maker_name
        self.sleep_time = sleep_time
        self.host = Host()

    def logger(self, msg):
        """暂且使用print"""
        print(self.maker_name, msg)

    def run_action(self, action, args: tuple = tuple()):
        """
        执行动作函数
        :param action:动作函数
        :param args:动作函数的参数，除第一个robot参数
        :return:
        """
        action(self, *args)

    @abstractmethod
    def run_action_file(self, action_file_name, step=1, msg=None):
        """
        执行动作组文件
        :param action_file_name:
        :param step:
        :param msg:
        :return:
        """
        pass

    @abstractmethod
    def set_servo(self, servo_infos: List[Tuple], used_time: int):
        """
        执行动作
        :param servo_infos:舵机信息,[(servo_id,angle)]
        :param used_time:耗时，单位为ms
        :return:
        """
        pass

    def host_run(self, cmd: str, msg=None, timeout: int = 30):
        self.logger(msg)
        self.host.run(cmd, timeout=timeout)
        time.sleep(self.sleep_time)
