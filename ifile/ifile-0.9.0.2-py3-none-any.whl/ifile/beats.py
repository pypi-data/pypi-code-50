import time
from importlib import import_module
from functools import wraps
from threading import Thread, Event

from ifile import setting as conf


class Service(object):
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
        Service.register(func, second)
        return func
    return decorate
