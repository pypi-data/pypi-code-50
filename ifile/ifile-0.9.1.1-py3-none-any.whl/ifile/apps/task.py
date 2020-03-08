import uuid
import logging
from enum import Enum
from functools import wraps
from datetime import datetime
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

logger = logging.getLogger(__name__)


class TaskState(Enum):
    QUEUED = "queued"
    RUNNING = "running"
    COMPLETED = "completed"


def gen_uuid():
    return str(uuid.uuid4())


class _TaskContext(object):
    def __init__(self, func):
        self.func = func
        self.id = None
        self.task_name = None
        self.start_time = None
        self.end_time = None
        self.result = None
        self.state = TaskState.QUEUED.value
        self.status_code = 0

        self._refresh()

    def _refresh(self):
        self.task_name = self.func.__name__

    def to_json(self):
        return {
            "task_id": self.id,
            "task_name": self.task_name,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "state": self.state,
            "status_code": self.status_code
        }


class AsyncTask(object):
    def __init__(self, func):
        self.context = _TaskContext(func)
        self.func = func
        self.name = func.__name__
        self.future = None

    def excute(self, *args, **kwargs):
        self.context.start_time = datetime.now()
        self.context.state = TaskState.RUNNING.value

        try:
            self.context.result = self.func(*args, **kwargs)
        except Exception as e:
            logger.exception(str(e))
            self.context.status_code = -1
        else:
            self.context.status_code = 1
        finally:
            self.context.end_time = datetime.now()
            self.context.state = TaskState.COMPLETED.value

    @property
    def result(self):
        return self.context.result

    @property
    def is_done(self):
        return self.future.done()


class AsyncApp(object):
    def __init__(self):
        self._tasks = {}
        self.executor = ThreadPoolExecutor(max_workers=100)

    def apply(self, func, *args, task_id=None, **kwargs):
        _task = AsyncTask(func)
        _task.future = self.executor.submit(_task.excute, *args, **kwargs)

        if task_id is None:
            task_id = gen_uuid()
        _task.context.id = task_id

        self._tasks[task_id] = _task
        return _task

    def get_async_task(self, task_id):
        return self._tasks[task_id]

    def get_async_tasks(self):
        return self._tasks.values()


app = AsyncApp()


def hello(id, name=None):
    import time
    time.sleep(3)
    return id, name


def world():
    return "hello world!"


if __name__ == "__main__":
    task1 = app.apply(hello, 1, name="greene")
    task2 = app.apply(hello, 1, name="greene")
    # import pdb;pdb.set_trace()
    print(task1.result, task1.context.id)
    print(task2.result, task2.context.id)
    # myfunc()
