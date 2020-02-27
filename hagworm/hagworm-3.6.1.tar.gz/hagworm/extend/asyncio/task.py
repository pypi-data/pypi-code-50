# -*- coding: utf-8 -*-

import asyncio

from crontab import CronTab

from hagworm.extend.interface import TaskInterface
from hagworm.extend.error import RateLimitError

from .base import Utils, FutureWithTask


class _BaseTask(TaskInterface):
    """异步任务基类
    """

    @classmethod
    def create(cls, promptly, _callable, *args, **kwargs):

        if args or kwargs:
            _callable = Utils.func_partial(_callable, *args, **kwargs)

        task = cls(_callable)

        task.start(promptly)

        return task

    def __init__(self, _callable):

        self._running = False
        self._next_timeout = 0

        self._event_loop = None
        self._timeout_handle = None

        self._callable = _callable

    def start(self, promptly=False, *, event_loop=None):

        if event_loop:
            self._event_loop = event_loop
        else:
            self._event_loop = asyncio.get_event_loop()

        self._running = True

        if promptly:
            self._timeout_handle = Utils.call_soon(self._run)
        else:
            self._schedule_next()

    def stop(self):

        self._running = False

        if self._timeout_handle is not None:
            self._timeout_handle.cancel()
            self._timeout_handle = None

    def is_running(self):

        return self._running

    async def _run(self):

        if not self._running:
            return

        try:

            await Utils.awaitable_wrapper(
                self._callable()
            )

        except Exception as err:

            Utils.log.error(err)

        finally:

            self._schedule_next()

    def _schedule_next(self):

        if self._running:
            self._timeout_handle = Utils.call_at(self._update_next(), self._run)

    def _update_next(self):

        self._next_timeout = self._event_loop.time()

        return self._next_timeout


class LoopTask(_BaseTask):
    """循环任务类
    """

    @classmethod
    def create(cls, limit_time, promptly, _callable, *args, **kwargs):

        if args or kwargs:
            _callable = Utils.func_partial(_callable, *args, **kwargs)

        task = cls(_callable, limit_time)

        task.start(promptly)

        return task

    def __init__(self, _callable, limit_time):

        super().__init__(_callable)

        self._limit_time = limit_time

    def _update_next(self):

        now_time = self._event_loop.time()
        next_timeout = self._next_timeout + self._limit_time

        if next_timeout < now_time:
            self._next_timeout = now_time
        else:
            self._next_timeout = next_timeout

        return self._next_timeout


class IntervalTask(_BaseTask):
    """间隔任务类
    """

    @classmethod
    def create(cls, interval, promptly, _callable, *args, **kwargs):

        if args or kwargs:
            _callable = Utils.func_partial(_callable, *args, **kwargs)

        task = cls(_callable, interval)

        task.start(promptly)

        return task

    def __init__(self, _callable, interval):

        super().__init__(_callable)

        self._interval = interval

    def _update_next(self):

        self._next_timeout = self._event_loop.time() + self._interval

        return self._next_timeout


class CronTask(_BaseTask, CronTab):
    """定时任务类
    """

    @classmethod
    def create(cls, crontab, promptly, _callable, *args, **kwargs):

        if args or kwargs:
            _callable = Utils.func_partial(_callable, *args, **kwargs)

        task = cls(_callable, crontab)

        task.start(promptly)

        return task

    def __init__(self, _callable, crontab, default_now=None, default_utc=None):

        _BaseTask.__init__(self, _callable)
        CronTab.__init__(self, crontab)

        self._default_now = default_now
        self._default_utc = default_utc

    def _update_next(self):

        params = {}

        if self._default_now is not None:
            params[r'now'] = self._default_now

        if self._default_utc is not None:
            params[r'default_utc'] = self._default_utc

        self._next_timeout = self._event_loop.time() + self.next(**params)

        return self._next_timeout


class RateLimiter:

    def __init__(self, running_limit, waiting_limit=0):

        self._running_limit = running_limit
        self._waiting_limit = waiting_limit

        self._running_tasks = {}
        self._waiting_tasks = []

    async def __call__(self, func, *args, **kwargs):

        future = self.append(func, *args, **kwargs)

        if future is None:
            raise RateLimitError()

        return await future

    def append(self, func, *args, **kwargs):

        future = None

        if self._check_running_limit():
            future = FutureWithTask(func, *args, **kwargs)
            self._add_running_tasks(future)
        elif self._check_waiting_limit():
            future = FutureWithTask(func, *args, **kwargs)
            self._add_waiting_tasks(future)

        return future

    @property
    def running_limit(self):

        return self._running_limit

    @running_limit.setter
    def running_limit(self, val):

        self._running_limit = val

        self._recover_waiting_tasks()

    def _check_running_limit(self):

        return self._running_limit <= 0 or len(self._running_tasks) < self._running_limit

    @property
    def waiting_limit(self):

        return self._waiting_limit

    @waiting_limit.setter
    def waiting_limit(self, val):

        self._waiting_limit = val

        if len(self._waiting_tasks) > self._waiting_limit:
            self._waiting_tasks = self._waiting_tasks[:self._waiting_limit]

    def _check_waiting_limit(self):

        return self._waiting_limit <= 0 or len(self._waiting_tasks) < self._waiting_limit

    def _add_running_tasks(self, future_callable):

        future_callable.add_done_callback(self._done_callback)
        self._running_tasks[future_callable.name] = future_callable

        future_callable()

    def _add_waiting_tasks(self, future_callable):

        self._waiting_tasks.append(future_callable)

    def _recover_waiting_tasks(self):

        for _ in range(len(self._waiting_tasks)):

            if self._check_running_limit():
                future_callable = self._waiting_tasks.pop(0)
                self._add_running_tasks(future_callable)
            else:
                break

    def _done_callback(self, future_callable):

        if future_callable.name in self._running_tasks:
            self._running_tasks.pop(future_callable.name)

        self._recover_waiting_tasks()
