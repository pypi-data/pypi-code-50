"""
执行器的接口
"""
from abc import abstractmethod

from api.handler.IHandler import IHandler
from api.handler.IKillable import IKillable
from api.handler.ILogAbleHandler import ILogAbleHandler
from api.handler.IProgressAble import IProgressAble


class ITaskHandler(ILogAbleHandler, IHandler, IKillable, IProgressAble):

    @abstractmethod
    def execute(self, params):
        """
        执行任务
        :return:
        """

    @abstractmethod
    def get_execution_message_cache(self):
        """
        获取执行消息的写入器
        :return:
        """

    def write_execution_message(self, execution_message):
        """
        写入执行消息
        :param execution_message:
        :return:
        """
