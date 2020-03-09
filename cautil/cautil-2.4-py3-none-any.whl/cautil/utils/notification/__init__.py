import importlib
from cautil import CAUtil

from abc import ABC, abstractmethod

class Notification(CAUtil):
    
    def get_service(self):
        config = self.config
        vendor = config[self.service_name]['vendor']
        module = importlib.import_module('cautil.utils.{0}.{1}'.format(self.service_name, vendor))
        auth_class = getattr(module, '{0}'.format(vendor))
        return auth_class(config[self.service_name])


class NotificationUtilInterface(ABC):
        
    @abstractmethod
    def send_notification(self, device_id, message):
        raise NotImplementedError
    
    @abstractmethod
    def send_group_notification(self, device_ids, message):
        raise NotImplementedError