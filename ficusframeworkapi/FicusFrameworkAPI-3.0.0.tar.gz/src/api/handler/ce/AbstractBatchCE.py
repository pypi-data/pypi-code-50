from abc import abstractmethod

from api.handler.ICacheAbleHandler import ICacheAbleHandler
from api.handler.ITaskHandler import ITaskHandler
from api.handler.outputer.IBatchOutputer import IBatchOutputer
from api.model.BatchOutputPipe import BatchOutputPipe
from api.model.FdInputPipe import FdInputPipe


class AbstractBatchCE(ITaskHandler, IBatchOutputer, ICacheAbleHandler):

    @abstractmethod
    def do_compute(self, output_stream: BatchOutputPipe, source_fds: FdInputPipe, params: dict):
        pass