import time
import logging
from importlib import import_module
from functools import wraps
from threading import Thread, Event
from datetime import datetime, timedelta

from ifile import setting as conf
from ifile.client import Clients

logger = logging.getLogger(__name__)


class BeatService(object):
    tasks = {}

    def __init__(self, name):
        self.name = name
        self._is_stop = Event()

        self.init_task()

    def start(self):
        def inner(func, schedule_time):
            while not self._is_stop.is_set():
                func()
                time.sleep(schedule_time)

        for name, task in self.tasks.items():
            t = Thread(
                target=inner,
                args=(task["func"], task["time"],),
                name=name)
            t.start()

    def stop(self):
        self._is_stop.set()

    def init_task(self):
        task_modules = conf.BEAT_TASKS
        for module in task_modules:
            import_module(module)

    @classmethod
    def register(cls, func, time):
        if func.__name__ in cls.tasks:
            raise

        cls.tasks[func.__name__] = {
            "func": func,
            "time": time
        }


def beat(second=1):
    def decorate(func):
        BeatService.register(func, second)
        return func
    return decorate


@beat(second=2)
def check_client():
    clients = Clients()
    logger.debug(f"checking clients.")

    for (hostname, ip), c in clients.clients.items():
        now = datetime.now()
        util_time = now - timedelta(seconds=10)
        logger.debug(f"the last_alive_time the of client {hostname} "
                     f"is {c.last_alive_time}, now: {now}, "
                     f"util_time: {util_time}.")

        if (c.last_alive_time is None or c.last_alive_time < util_time) \
           and c.is_register is True:
            clients.unregister(hostname, ip)
