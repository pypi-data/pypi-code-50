 # -*- coding: utf-8 -*-

__all__ = ["IdentityConnector"]

from spaceone.core.connector import BaseConnector
from spaceone.core import pygrpc
from spaceone.core.utils import parse_endpoint
from spaceone.core.error import *
from spaceone.repository.error import *

class IdentityConnector(BaseConnector):
    def __init__(self, transaction, config):
        super().__init__(transaction, config)
        if 'endpoint' not in self.config:
            raise ERROR_WRONG_CONFIGURATION(key='endpoint')

        if len(self.config['endpoint']) > 1:
            raise ERROR_WRONG_CONFIGURATION(key='too many endpoint')

        for (k,v) in self.config['endpoint'].items():
            # parse endpoint
            e = parse_endpoint(v)
            self.protocol = e['scheme']
            if self.protocol == 'grpc':
                # create grpc client
                self.client = pygrpc.client(endpoint="%s:%s" % (e['hostname'], e['port']), version=k)
            elif self.protocol == 'http':
                # TODO:
                pass


    def exist_project(self, project_id):
        """ Check project is exist or not

        Args: project_id

        Returns: True or False
        """
        if self.protocol == 'grpc':
            # Try to connect via grpc client
            r = self.client.Project.get({'project_id':project_id})
            if r.project_id == project_id:
                return True
            return False
        elif self.protocol == 'http':
            raise ERROR_UNSUPPORT(message=self.protocol)
