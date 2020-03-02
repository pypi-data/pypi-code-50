from abc import ABC, abstractmethod


class BaseStorageBackend(ABC):

    @abstractmethod
    def persist_status(self):
        """
        This method should store the Status (twit) in the backend database
        """
        pass

    @abstractmethod
    def init_backend(self):
        """
        This method should do whatever is necessary to init the backend: connect, create tables, etc
        """
        pass