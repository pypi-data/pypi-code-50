import abc


class FileApiBase(abc.ABC):

    @abc.abstractmethod
    def get(self):
        """获取文件"""

    @abc.abstractmethod
    def add(self):
        """添加文件"""

    @abc.abstractmethod
    def destroy(self):
        """销毁文件"""

    @abc.abstractmethod
    def get_bdata_by_uuid(self, uuid):
        """获取元数据"""
