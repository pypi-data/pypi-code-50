# -*- coding: utf-8 -*-

__all__ = ['PluginManager']

import logging

from abc import abstractmethod

from spaceone.core import config
from spaceone.core import pygrpc
from spaceone.core.error import *
from spaceone.core.manager import BaseManager
from spaceone.repository.model import *
from spaceone.repository.error.custom import *

_LOGGER = logging.getLogger(__name__)

class PluginManager(BaseManager):
    def __init__(self, transaction, **kwargs):
        super().__init__(transaction, **kwargs)

    @abstractmethod
    def register_plugin(self, params):
        pass

    @abstractmethod
    def update_plugin(self, params):
        pass

    @abstractmethod
    def enable_plugin(self, plugin_id, domain_id):
        pass

    @abstractmethod
    def disable_plugin(self, plugin_id, domain_id):
        pass

    @abstractmethod
    def delete_plugin(self, plugin_id, domain_id):
        pass

    @abstractmethod
    def get_plugin(self, plugin_id, domain_id):
        pass

    @abstractmethod
    def list_plugins(self, query, domain_id):
        pass

    @abstractmethod
    def get_plugin_versions(self, plugin_id, domain_id):
        pass

    """"
    Internal Methods
    """
    def check_service_type(self, name):
        """
        service_type has format rule
        format:
            <service>.<purpose>
            custom.<service>.<purpose>
        example:
            identity.domain
            custom.identity.domain
        return:
            True | False
        """
        if name is None:
            return True

        idx = name.split('.')
        if len(idx) == 2:
            # TODO: check service name
            return True
        elif len(idx) == 3 and idx[0] == 'custom':
            # TODO: check service name
            return True
        else:
            # TODO: Raise Format Error
            return False

    def check_project_id(self, project_id):
        # Check project_id is valid or not
        # contact to Identity
        # return True/False
        if project_id is None:
            return True 
        connector = self.locator.get_connector('IdentityConnector')
        return connector.exist_project(project_id)

