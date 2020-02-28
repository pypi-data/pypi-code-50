from abc import abstractmethod
import os.path

from ..util.Optionizable import Optionizable

class DataNotFound(Exception):
    pass

class PermissionDenied(Exception):
    pass

class Storage(Optionizable):
    basePath: str

    def __init__(self, basePath="."):
        self.basePath = basePath

    def getPath(self, path):
        return os.path.normpath(self.basePath + '/' + path)

    @abstractmethod
    def read(self, path):
        pass

    @abstractmethod
    def write(self, path, data):
        pass
