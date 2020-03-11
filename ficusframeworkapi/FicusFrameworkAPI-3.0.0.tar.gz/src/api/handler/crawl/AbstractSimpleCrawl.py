from abc import abstractmethod

from api.handler.ICacheAbleHandler import ICacheAbleHandler
from api.handler.ITaskHandler import ITaskHandler
from api.handler.outputer.ISimpleOutputer import ISimpleOutputer


class AbstractSimpleCrawl(ITaskHandler, ISimpleOutputer, ICacheAbleHandler):
    """
        简单的Crawl,只需要继承这个类,并且实现do_crawl方法即可
    """

    @abstractmethod
    def do_crawl(self, params: dict) -> list:
        """
        真正执行数据挖掘的逻辑
        :param params: 需要存入fd中的数据
        :return:
        """
