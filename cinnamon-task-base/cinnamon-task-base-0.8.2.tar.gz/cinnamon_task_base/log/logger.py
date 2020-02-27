import datetime
import inspect
import logging
import sys
import time
import socket

from .log_setting import LogSetting


host_name = socket.gethostname()
job_id = 'JOB_ID'
task_name = 'TASK_NAME'


def set_job_id(id: str):
    global job_id
    job_id = id


def set_host_name(name: str):
    global host_name
    host_name = name


def set_task_name(name: str):
    global task_name
    task_name = name


class PodderTaskLogger(logging.Logger):
    def _log(self, level, msg, args, exc_info=None, extra=None, stack_info=False):
        message = f'[{task_name}][{host_name}][{job_id}] - {msg}'
        super(PodderTaskLogger, self)._log(level, message, args, exc_info, extra)


logging.setLoggerClass(PodderTaskLogger)

logging.getLogger().__class__ = PodderTaskLogger


class Logger(object):
    TRACE_LOG_LEVEL = 5

    def __init__(self):
        self.start_time = time.time()
        self.task_start_time = time.time()
        self.setting = LogSetting().load()
        self.logger = logging.getLogger('podder.task')
        self.logger.propagate = False
        log_format = self.setting["task_log_format"]
        log_level = self.setting["task_log_level"]
        self.logger.setLevel(log_level)
        self._add_default_handler(log_format, log_level)
        logging.addLevelName(self.TRACE_LOG_LEVEL, "TRACE")

    def init_tasktime(self):
        self.task_start_time = time.time()

    def fatal(self, msg, *args, **kwargs):
        # fatal -> critical(python logger)
        self._format(logging.CRITICAL, msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self._format(logging.ERROR, msg, *args, **kwargs)

    def warn(self, msg, *args, **kwargs):
        # warn -> warning(python logger)
        self._format(logging.WARNING, msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self._format(logging.INFO, msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        self._format(logging.DEBUG, msg, *args, **kwargs)

    def trace(self, msg, *args, **kwargs):
        self._format(self.TRACE_LOG_LEVEL, msg, *args, **kwargs)

    def customize_log(self, lvl, msg, *args, **kwargs):
        self._format(lvl, msg, *args, **kwargs)

    # private
    def _create_extra(self):
        ex = {'progresstime': str(round((time.time() - self.start_time), 3)),
              'tasktime': str(round((time.time() - self.task_start_time), 3)),
              'taskname': str(self.setting["task_name"])}
        caller_info = sys._getframe(2)  # caller of 2 level depth
        module_info = inspect.getmodule(caller_info)
        script_info = inspect.getsourcelines(caller_info)[1]
        ex['scriptinfo'] = "%s:%s" % (module_info, script_info)
        # original time code, because logging "datefmt" is not support microsecond
        now = datetime.datetime.now()
        ex['time'] = now.strftime("%Y-%m-%d %H:%M:%S.") + "%06d" % now.microsecond
        return ex

    def _add_default_handler(self, log_format, log_level):
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(log_level)
        handler.setFormatter(logging.Formatter(fmt=log_format, datefmt='%Y-%m-%d %H:%M:%S'))
        self.logger.addHandler(handler)

    def _convert_newline_character(self, msg):
        old_character =  '\n'
        new_character = '\\n'
        return msg.replace(old_character, new_character)

    def _format(self, lvl, msg, *args, **kwargs):
        self.logger.log(lvl, self._convert_newline_character(msg),  extra=self._create_extra(), *args, **kwargs)


def class_logger(cls):
    global _is_logged
    if _is_logged is False:
        logging.basicConfig()
        _is_logged = Logger()

    cls.logger = _is_logged
    return cls


_is_logged = False
