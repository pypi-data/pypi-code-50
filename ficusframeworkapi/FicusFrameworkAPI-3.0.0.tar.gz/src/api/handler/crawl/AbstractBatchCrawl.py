from abc import abstractmethod

from api.handler.ICacheAbleHandler import ICacheAbleHandler
from api.handler.ITaskHandler import ITaskHandler
from api.handler.outputer.IBatchOutputer import IBatchOutputer
from api.model.BatchOutputPipe import BatchOutputPipe


class AbstractBatchCrawl(ITaskHandler, IBatchOutputer, ICacheAbleHandler):

    @abstractmethod
    def do_crawl(self, output_stream: BatchOutputPipe, params: dict):
        """
        真正执行数据挖掘的逻辑
        :param output_stream: 数据的输出
        :param params: 需要的参数
        :return:
        """
