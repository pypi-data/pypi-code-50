from abc import abstractmethod

from api.handler.ICacheAble import ICacheAble

CACHE_PREFIX = "sobeyficus.cache."
PROCESS_CACHE_PREFIX = "sobeyficus.process.cache."


class ICacheAbleHandler(ICacheAble):
    """
    缓存操作的接口
    """

    @abstractmethod
    def get_code_thread_local(self):
        """
        需要实现的方法,返回一个 thread_local对象
        :return:
        """

    @abstractmethod
    def get_process_thread_local(self):
        """
        需要实现的方法,返回一个 thread_local对象
        :return:
        """

    # region 同执行器的缓存
    def set_cache_value(self, key, value):
        """
        放入缓存
        :param key:
        :param value:
        :return:
        """


    def set_cache_value_if_absent(self, key, value):
        """
        放入缓存
        :param key:
        :param value:
        :return:
        """

    def get_cache_value(self, key):
        """
        获取缓存
        :param key:
        :return:
        """

    def delete_cache_value(self, key):
        """
        删除缓存
        :param key:
        :return:
        """
    # endregion

    # region 同执行计划的缓存
    def set_cache_value_from_process(self, key, value):
        """
        放入缓存
        :param key:
        :param value:
        :return:
        """

    def set_cache_value_if_absent_from_process(self, key, value):
        """
        放入缓存
        :param key:
        :param value:
        :return:
        """

    def get_cache_value_from_process(self, key):
        """
        获取缓存
        :param key:
        :return:
        """

    def delete_cache_value_from_process(self, key):
        """
        删除缓存
        :param key:
        :return:
        """
    # endregion