import logging
import time
import socket

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
    def __init__(self):
        self.start_time = time.time()
        logging.basicConfig(
            format='%(levelname)s:%(message)s', level=logging.DEBUG)

    def warning(self, msg, *args, **kwargs):
        logging.warning(self.add_time(msg), *args, **kwargs)

    def warn(self, msg, *args, **kwargs):
        logging.warning(self.add_time(msg), *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        logging.info(self.add_time(msg), *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        logging.debug(self.add_time(msg), *args, **kwargs)

    def log(self, msg, *args, **kwargs):
        logging.log(self.add_time(msg), *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        logging.error(self.add_time(msg), *args, **kwargs)

    def add_time(self, msg):
        time_spent = round((time.time() - self.start_time), 3)
        msg_with_time = "[{}] {}".format(time_spent, msg)
        return msg_with_time
