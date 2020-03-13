# -*- coding: utf-8 -*-

__all__ = ["RegistryConnector"]

from docker_registry_client import DockerRegistryClient

from spaceone.core.connector import BaseConnector
from spaceone.repository.error import *

class RegistryConnector(BaseConnector):
    def __init__(self, transaction, config):
        super().__init__(transaction, config)

    def get_tags(self, image):
        params = {}
        for (k,v) in self.config.items():
            if v == '' or v == None:
                continue
            params.update({k:v})
        try:
            client = DockerRegistryClient(**params)
            r = client.repository(image)
            tags = r.tags()
            # return sorted list
            return tags
        except Exception as e:
            # Hard to determine backend problems
            print(e)
            raise ERROR_REPOSITORY_BACKEND(host=params['host'])
