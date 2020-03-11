from abc import abstractmethod


from api.handler.IAsyncAble import IAsyncAble
from api.handler.ICacheAbleHandler import ICacheAbleHandler
from api.handler.ITaskHandler import ITaskHandler
from api.handler.outputer.IBatchOutputer import IBatchOutputer
from api.model.AsyncServiceRequest import AsyncServiceRequest
from api.model.BatchOutputPipe import BatchOutputPipe
from api.model.FdInputPipe import FdInputPipe


class AbstractAsyncServiceBatchCE(ITaskHandler, IBatchOutputer, ICacheAbleHandler, IAsyncAble):
    """
    调用 异步服务的Batch处理器
    """


    # region 需要实现的抽象方法
    @abstractmethod
    def generate_request(self, input_pipe: FdInputPipe, params: dict) -> AsyncServiceRequest:
        """
        生成异步任务的请求的抽象方法
        :param input_pipe:
        :param params:
        :return:
        """
        pass

    @abstractmethod
    def do_compute(self, response, header: dict, task_status: int, output_stream: BatchOutputPipe,
                   source_fds: FdInputPipe, ficus_param: dict) -> str:
        """
        异步任务的返回
        :param response:
        :param header:
        :param task_status:
        :param output_stream:
        :param source_fds:
        :param ficus_param:
        :return:
        """
        pass
    # endregion
