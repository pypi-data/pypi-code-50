import importlib
from cautil import CAUtil

from abc import ABC, abstractmethod

class Authorization(CAUtil):
    
    def get_service(self):
        config = self.config
        vendor = config[self.service_name]['vendor']
        module = importlib.import_module('cautil.utils.{0}.{1}'.format(self.service_name, vendor))
        auth_class = getattr(module, '{0}'.format(vendor))
        return auth_class(config[self.service_name])


class AuthorizationUtilInterface(ABC): 

    @abstractmethod
    def get_configuration(self):
        raise NotImplementedError
    
    @abstractmethod
    def validate_token(self, token):
        raise NotImplementedError

    @abstractmethod
    def login(self, username, password, token):
        raise NotImplementedError

    @abstractmethod
    def create_user(self, username, password, user_details):
        raise NotImplementedError

    @abstractmethod
    def delete_user(self, user_id):
        raise NotImplementedError

    @abstractmethod
    def refresh_access(self, refresh_token):
        raise NotImplementedError