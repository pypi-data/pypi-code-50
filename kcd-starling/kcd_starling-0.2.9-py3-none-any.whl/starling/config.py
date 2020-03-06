class Config(dict):
    def __init__(self, defaults: dict = None) -> None:
        super().__init__(defaults or {})


CONFIG = Config({'run_retry_times': 3, 'task_retry_times': 5})
