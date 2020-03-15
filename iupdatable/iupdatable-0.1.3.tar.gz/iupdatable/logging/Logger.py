import threading
from .LogLevel import LogLevel
import logging as sys_logging
import logging.handlers
import datetime
import sys
from colorlog import ColoredFormatter
import inspect


class Logger(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Logger, "_instance"):
            with Logger._instance_lock:
                if not hasattr(Logger, "_instance"):
                    Logger._instance = object.__new__(cls)
                    cls._is_init = False
        return Logger._instance

    @classmethod
    def get_instance(cls):
        """
        获取日志实例
        :return:
        """
        return Logger()

    @classmethod
    def config(cls,
               log_level=LogLevel.DEBUG,
               log_file_full_path="all.log",
               date_format="%Y-%m-%d %H:%M:%S",
               is_with_datetime=True,
               is_with_level=True,
               is_output_file=True,
               is_output_console=True,
               is_colored=True
               ):
        """
        配置日志
        :param log_level:           日志输出等级，参考：LogLevel的值
        :param log_file_full_path:  日志输出的文件名的完整路径，默认：all.log
        :param date_format:         每天日志前日期时间的格式，默认: %Y-%m-%d %H:%M:%S
        :param is_with_datetime:    是否在每条日志前添加日期时间
        :param is_with_level:       是否在每天日志前添加日志等级
        :param is_output_file:      是否将日志输出到文件
        :param is_output_console:   是否将日志输出到控制台
        :param is_colored:          是否将控制台的输出设为彩色
        :return:
        """
        print("log file: " + log_file_full_path)
        cls._logger = cls._get_config_logger("my_logger", is_with_src_info=False, log_level=log_level,
                                             log_file_full_path=log_file_full_path, date_format=date_format,
                                             is_with_datetime=is_with_datetime, is_with_level=is_with_level,
                                             is_output_file=is_output_file, is_output_console=is_output_console,
                                             is_colored=is_colored)
        # 输出调试信息，如：文件路径，代码行定位
        cls._debug_logger = cls._get_config_logger("my_debug_logger", is_with_src_info=True, log_level=log_level,
                                                   log_file_full_path=log_file_full_path, date_format=date_format,
                                                   is_with_datetime=is_with_datetime, is_with_level=is_with_level,
                                                   is_output_file=is_output_file, is_output_console=is_output_console,
                                                   is_colored=is_colored)
        cls._is_init = True

    @classmethod
    def _get_config_logger(cls,
                           logger_name,
                           log_level=LogLevel.DEBUG,
                           log_file_full_path="all.log",
                           date_format="%Y-%m-%d %H:%M:%S",
                           is_with_datetime=True,
                           is_with_level=True,
                           is_with_src_info=False,
                           is_output_file=True,
                           is_output_console=True,
                           is_colored=True
                           ):
        """
        获取一个配置后的logger
        :param logger_name:         日志对象的名称，用户指定
        :param log_level:           日志输出等级，参考：LogLevel的值
        :param log_file_full_path:  日志输出的文件名的完整路径，默认：all.log
        :param date_format:         每天日志前日期时间的格式，默认: %Y-%m-%d %H:%M:%S
        :param is_with_datetime:    是否在每条日志前添加日期时间
        :param is_with_level:       是否在每天日志前添加日志等级
        :param is_with_src_info:    是否包含源码定位信息，如:所在文件及代码行
        :param is_output_file:      是否将日志输出到文件
        :param is_output_console:   是否将日志输出到控制台
        :param is_colored:          是否将控制台的输出设为彩色
        :return: 返回一个配置完成的logger
        """
        if log_file_full_path == "all.log" or len(log_file_full_path.strip()) == 0:
            log_file_full_path = "all.log"

        logger = sys_logging.getLogger(logger_name)
        logger.handlers.clear()  # 清空handlers，防止是二次调用config

        # 设置日志输出格式
        formatter_prefix = ""
        if is_with_level:
            formatter_prefix += "[%(levelname)-8s]\t"  # -8s表示总计占8个字符，负号表示左对齐
        if is_with_datetime:
            formatter_prefix += "%(asctime)s\t>>\t"
        if is_with_src_info:
            formatter_prefix += "%(myfullpath)s, Function: %(myfuncName)s, Line: %(mylineno)s:\n\t\t\t\t\t\t\t\t\t"
        formatter_str = formatter_prefix + "%(message)s"
        cls._Level = log_level
        logger.setLevel(log_level)
        logger_formatter = sys_logging.Formatter(fmt=formatter_str, datefmt=date_format)

        # 设置日志输出到文件
        if is_output_file:
            # 输出到文件的 handler
            logger_file_handler = sys_logging.handlers.TimedRotatingFileHandler(
                log_file_full_path,
                when='midnight', interval=1, backupCount=7,
                atTime=datetime.time(0, 0, 0, 0))
            logger_file_handler.suffix = "%Y-%m-%d.log"
            logger_file_handler.setFormatter(logger_formatter)
            logger.addHandler(logger_file_handler)

        # 设置日志色彩相关
        # 色彩只和控制台相关，故本段代码要放在文件handler之后，控制台handler之前
        if is_colored:
            formatter_str = "%(log_color)s" + formatter_str + "%(reset)s"
            logger_formatter = ColoredFormatter(fmt=formatter_str, datefmt=date_format)

        # 设置日志输出到控制台
        if is_output_console:
            logger_console_handler = sys_logging.StreamHandler(stream=sys.stdout)  # 输出到控制台的 handler
            logger_console_handler.setFormatter(logger_formatter)
            logger.addHandler(logger_console_handler)
        return logger

    @classmethod
    def debug(cls, message, is_with_debug_info=False):
        if not cls._is_init:
            cls.config()
        if is_with_debug_info:
            # 获取调用者的信息（该部分代码不能再次封装成函数）
            full_path = sys._getframe(1).f_code.co_filename
            func_name = sys._getframe(1).f_code.co_name
            line_no = sys._getframe(1).f_lineno
            cls._extra_args = {'myfullpath': full_path, 'myfuncName': func_name, 'mylineno': line_no}
            cls._debug_logger.debug(message, extra=cls._extra_args)
        else:
            cls._logger.debug(message)

    @classmethod
    def info(cls, message, is_with_debug_info=False):
        if not cls._is_init:
            cls.config()
        if is_with_debug_info:
            # 获取调用者的信息（该部分代码不能再次封装成函数）
            full_path = sys._getframe(1).f_code.co_filename
            func_name = sys._getframe(1).f_code.co_name
            line_no = sys._getframe(1).f_lineno
            cls._extra_args = {'myfullpath': full_path, 'myfuncName': func_name, 'mylineno': line_no}
            cls._debug_logger.info(message, extra=cls._extra_args)
        else:
            cls._logger.info(message)

    @classmethod
    def warning(cls, message, is_with_debug_info=False):
        if not cls._is_init:
            cls.config()
        if is_with_debug_info:
            # 获取调用者的信息（该部分代码不能再次封装成函数）
            full_path = sys._getframe(1).f_code.co_filename
            func_name = sys._getframe(1).f_code.co_name
            line_no = sys._getframe(1).f_lineno
            cls._extra_args = {'myfullpath': full_path, 'myfuncName': func_name, 'mylineno': line_no}
            cls._debug_logger.warning(message, extra=cls._extra_args)
        else:
            cls._logger.warning(message)

    @classmethod
    def error(cls, message, is_with_debug_info=False):
        if not cls._is_init:
            cls.config()
        if is_with_debug_info:
            # 获取调用者的信息（该部分代码不能再次封装成函数）
            full_path = sys._getframe(1).f_code.co_filename
            func_name = sys._getframe(1).f_code.co_name
            line_no = sys._getframe(1).f_lineno
            cls._extra_args = {'myfullpath': full_path, 'myfuncName': func_name, 'mylineno': line_no}
            cls._debug_logger.error(message, extra=cls._extra_args)
        else:
            cls._logger.error(message)

    @classmethod
    def critical(cls, message, is_with_debug_info=False):
        if not cls._is_init:
            cls.config()
        if is_with_debug_info:
            # 获取调用者的信息（该部分代码不能再次封装成函数）
            full_path = sys._getframe(1).f_code.co_filename
            func_name = sys._getframe(1).f_code.co_name
            line_no = sys._getframe(1).f_lineno
            cls._extra_args = {'myfullpath': full_path, 'myfuncName': func_name, 'mylineno': line_no}
            cls._debug_logger.critical(message, extra=cls._extra_args)
        else:
            cls._logger.critical(message)

    @classmethod
    def fatal(cls, message, is_with_debug_info=False):
        if not cls._is_init:
            cls.config()
        if is_with_debug_info:
            # 获取调用者的信息（该部分代码不能再次封装成函数）
            full_path = sys._getframe(1).f_code.co_filename
            func_name = sys._getframe(1).f_code.co_name
            line_no = sys._getframe(1).f_lineno
            cls._extra_args = {'myfullpath': full_path, 'myfuncName': func_name, 'mylineno': line_no}
            cls._debug_logger.critical(message, extra=cls._extra_args)
        else:
            cls._logger.critical(message)
