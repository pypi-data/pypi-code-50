import threading

thread_storage = threading.local()


class RequestStorage:
    def __init__(self):
        self.request = None
        self.user = None
        self.user_group = None
        self.response: dict = {}
        self.execution_time: int = -1
        self.status_code = 200  # todo implement it
        self.data = {}


thread_storage.current_request = {}

current_request = thread_storage.current_request
