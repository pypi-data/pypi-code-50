import importlib
from cautil import CAUtil

from abc import ABC, abstractmethod

class Storage(CAUtil):
    
    def get_service(self):
        config = self.config
        vendor = config[self.service_name]['vendor']
        module = importlib.import_module('cautil.utils.{0}.{1}'.format(self.service_name, vendor))
        auth_class = getattr(module, '{0}'.format(vendor))
        return auth_class(config[self.service_name])


class StorageUtilInterface(ABC):
        
    @abstractmethod
    def upload_file(self, file_content, location, file_name):
        raise NotImplementedError

    @abstractmethod
    def download_file(self, location, file_name):
        raise NotImplementedError

    @abstractmethod
    def copy_file(self, source, destination, file_name, remove_file_from_source):
        raise NotImplementedError

    @abstractmethod
    def read_file(self, location, file_name):
        raise NotImplementedError

    @abstractmethod
    def delete_file(self, location, file_name):
        raise NotImplementedError