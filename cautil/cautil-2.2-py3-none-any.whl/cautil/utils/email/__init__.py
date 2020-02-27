import importlib
from cautil import CAUtil
from abc import ABC, abstractmethod

class Email(CAUtil):

    def get_service(self):
        config = self.config
        vendor = config[self.service_name]['vendor']
        module = importlib.import_module('cautil.utils.{0}.{1}'.format(self.service_name, vendor))
        auth_class = getattr(module, '{0}'.format(vendor))
        return auth_class(config[self.service_name])

class EmailUtilInterface(ABC):
    
    @abstractmethod
    def send_email(self, to_email, subject, message):
        raise NotImplementedError
        
    @abstractmethod
    def get_email_configuration(self):
        raise NotImplementedError
    
    @abstractmethod
    def set_email_configuration(self, config):
        raise NotImplementedError
    
    @abstractmethod
    def validate_configuration(self, config):
        raise NotImplementedError

    