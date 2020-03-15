# coding:utf-8
"""*--撒哈la--*"""

import logging

"""
方式二 日志流处理流程
模块级别的函数是logging.getLogger([name])（返回一个logger对象，如果没有指定名字将返回root logger）

loggin模块四大组件：
日志器： logger 提供了应用程序可一直调用的接口
处理器： Handler 将logger创建的日志记录发送到合适的目的输出
过滤器: Filter 控制工具来决定输出哪条日志记录，丢弃哪条日志记录
格式器: Formatter 决定日志记录的最终输出格式

"""
import os
import time


class Log:

    def __init__(self, outpath_other=None):

        cur_path = os.path.dirname(os.path.realpath(__file__))  # log_path是存放日志的路径
        outpath_logs = os.path.join(os.path.dirname(cur_path), 'logs')  # 日志文件存放路径
        # 默认outpath_other is None输出到logs,否则输出到logs下指定路径
        log_path = outpath_logs if outpath_other is None else os.path.join(os.path.dirname(cur_path), 'logs',
                                                                           outpath_other)
        if not os.path.exists(log_path): os.mkdir(log_path)  # 如果不存在这个logs文件夹，就自动创建一个
        self.log_name = os.path.join(log_path, time.strftime('%Y_%m_%d') + '.log')  # 拼接log输出路径和log文件名称
        self.logger = logging.getLogger()  # 创建logger，默认返回root logger
        self.logger.setLevel(logging.DEBUG)  # 设置logger日志级别
        self.formatter_ = logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')  # 设置日志输出格式

    def __logs(self, level, msg):
        """
        输出日志
        :param level: 日志级别
        :param msg: 日志信息
        """
        if not self.logger.handlers:  # 如果存在logger.handlers就写入，否则创建，避免输出日志重复
            # 创建FileHandler用于写到log.log
            fh = logging.FileHandler(self.log_name, encoding='utf-8')
            fh.setFormatter(self.formatter_)  # 为handler指定输出格式
            self.logger.addHandler(fh)  # 为logger添加日志处理器

            # 创建StreamHandler输出到控制台
            ch = logging.StreamHandler()
            ch.setFormatter(self.formatter_)
            self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(msg)  # 最终输出的日志级别
        elif level == 'warning':
            self.logger.warning(msg)
        elif level == 'error':
            self.logger.error(msg)
        elif level == 'debug':
            self.logger.debug(msg)

    # 外部直接调用方法
    def info(self, msg):
        self.__logs('info', msg)  # 当level == 'info'时输出info日志

    def warning(self, msg):
        self.__logs('warning', msg)

    def error(self, msg):
        self.__logs('error', msg)

    def debug(self, msg):
        self.__logs('debug', msg)


if __name__ == '__main__':
    log = Log('business_log')  # 实例化日志类,输出到logs下制定路径

    log.info('----提示----')  # 直接调用函数，函数再调用self.__logs('info',msg)，输出日志
    log.warning('----警示----')
    log.error('----错误----')
    log.debug('----调试----')
