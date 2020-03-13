# -*- coding: utf-8 -*-
import logging

from spaceone.core.connector import BaseConnector
from spaceone.core import pygrpc
from spaceone.core.utils import parse_endpoint
from spaceone.core.error import *

__all__ = ['SecretConnector']

_LOGGER = logging.getLogger(__name__)

class SecretConnector(BaseConnector):
    def __init__(self, transaction, config, **kwargs):
        super().__init__(transaction, config, **kwargs)

        if 'endpoint' not in self.config:
            raise ERROR_WRONG_CONFIGURATION(key='endpoint')

        if len(self.config['endpoint']) > 1:
            raise ERROR_WRONG_CONFIGURATION(key='too many endpoint')

        for (k, v) in self.config['endpoint'].items():
            e = parse_endpoint(v)
            self.client = pygrpc.client(endpoint=f'{e.get("hostname")}:{e.get("port")}', version=k)
        # metadata may be escalated
        print("###########################################################")
        print("##### self.token %s: " % hasattr(self, 'token'))
        if hasattr(self, 'token'):
            print(self.token)

        self.escalated_meta = self._get_escalated_meta()


    def get_credentials(self, credential_id, domain_id):
        return self.client.Credential.get({'credential_id': credential_id, 'domain_id': domain_id},
                                    metadata=self.escalated_meta)

    def get_credential_group(self, credential_group_id, domain_id):
        return self.client.CredentialGroup.get({'credential_group_id': credential_group_id, 'domain_id': domain_id},
                                    metadata=self.escalated_meta)


    def issue_credentials(self, credential_id, domain_id):
        return self.client.Credential.issue({'credential_id': credential_id, 'domain_id': domain_id},
                                    metadata=self.escalated_meta)

    def _get_escalated_meta(self):
        meta = self.transaction.get_connection_meta()
        _LOGGER.debug(f'[_get_escalated_meta] meta: {meta}')
        result = []
        for (k,v) in meta:
            if k == 'token' and hasattr(self, 'token') and self.token is not None:
                result.append((k,self.token))
            elif k == 'domain_id' and hasattr(self, 'domain_id') and self.domain_id is not None:
                result.append((k,self.domain_id))
            else:
                result.append((k,v))
        _LOGGER.debug(f'[_get_escalated_meta] new_meta: {result}')
        return result

