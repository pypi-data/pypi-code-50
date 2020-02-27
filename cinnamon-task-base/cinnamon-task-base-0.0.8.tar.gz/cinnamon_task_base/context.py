from cinnamon_task_base.databases.pipeline import Session as PipelineSession

from .config import Config
from .file import File
from .logger import Logger


class Context(object):
    def __init__(self, dag_id: str) -> None:
        self.logger = Logger()
        self.config = Config()
        self.file = File()
        self.session = PipelineSession()
        self.dag_id = dag_id
