# -*- coding: utf-8 -*-

import consul
import logging
import time

from spaceone.core import config
from spaceone.core.auth.jwt.jwt_util import JWTUtil

from spaceone.repository.connector.repository_connector import RepositoryConnector
from spaceone.repository.manager.repository_manager import RepositoryManager
from spaceone.repository.model.repository_model import Repository

_LOGGER = logging.getLogger(__name__)

INTERVAL = 10
def _validate_token(token):
    if isinstance(token, dict):
        protocol = token['protocol']
        if protocol == 'consul':
            consul_instance = Consul(token['config'])
            value = False
            count = 0
            while value is False:
                value = consul_instance.patch_token(token['uri'])
                _LOGGER.warn(f'[_validate_token] token: {value}')
                if value:
                    break
                time.sleep(INTERVAL)

            token = value

    _LOGGER.debug(f'[_validate_token] token: {token}')
    return token


class RemoteRepositoryManager(RepositoryManager):

    def register_repository(self, params):
        """
        Args:
            params:
                - name
                - repository_type: remote
                - endpoint
                - version
                - credential_id

        Connect to Remote Repository via credential_id
        Get repository_id of remote.
        use remote's repository_id as my repository_id
        """
        domain_id = self._get_domain_id_from_token(self.transaction.get_meta('token'))
        credentials = self._issue_credentials(params.get('credential_id', None), domain_id)

        conn = {
            'endpoint': params.get('endpoint', None),
            'version': params.get('version', None),
            'credential': {'token': credentials['token']}
        }
        
        connector = self.locator.get_connector('RepositoryConnector', conn=conn)
        repo_info = connector.get_local_repository()
        # Overwrite repository_id to Remote one
        params['repository_id'] = repo_info.repository_id

        # TODO: connect remote repository, then check
        return self.repo_model.create(params)

    ###############################
    # Credential/CredentialGroup
    ###############################
    def _issue_credentials(self, credential_id, domain_id):
        """ Return secret data

        This call must be root domain.
        DO NOT check ROOT_TOKEN 

        """
        root_token = config.get_global('ROOT_TOKEN')
        root_token_info = config.get_global('ROOT_TOKEN_INFO')

        root_domain_id = domain_id
        if root_token is not "":
            root_domain_id = self._get_domain_id_from_token(root_token)
            _LOGGER.debug(f'[_issue_credentials] root_domain_id: {root_domain_id} vs domain_id: {domain_id}')
        elif root_token_info:
            # Patch from Consul
            _LOGGER.debug(f'[_issue_credentials] Patch root_token from Consul')
            root_token = _validate_token(root_token_info)
            root_domain_id = self._get_domain_id_from_token(root_token)
        else:
            _LOGGER.warn(f'[_issue_credentials] root_token is not configured, may be your are root')
            root_token = self.transaction.get_meta('token')


        connector = self.locator.get_connector('SecretConnector', token=root_token, domain_id=root_domain_id)
        cred = connector.issue_credentials(credential_id, domain_id)
        return cred.secret

    def _get_domain_id_from_token(self, token):
        decoded_token = JWTUtil.unverified_decode(token)
        return decoded_token['did']

class Consul:
    def __init__(self, config):
        """
        Args:
          - config: connection parameter

        Example:
            config = {
                    'host': 'consul.example.com',
                    'port': 8500
                }
        """
        self.config = self._validate_config(config)

    def _validate_config(self, config):
        """
        Parameter for Consul
        - host, port=8500, token=None, scheme=http, consistency=default, dc=None, verify=True, cert=None
        """
        options = ['host', 'port', 'token', 'scheme', 'consistency', 'dc', 'verify', 'cert']
        result = {}
        for item in options:
            value = config.get(item, None)
            if value:
              result[item] = value
        return result

    def patch_token(self, key):
        """
        Args:
            key: Query key (ex. /debug/supervisor/TOKEN)

        """
        try:
            conn = consul.Consul(**self.config)
            index, data = conn.kv.get(key)
            return data['Value'].decode('ascii')

        except Exception as e:
            return False
