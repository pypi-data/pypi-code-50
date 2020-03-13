# -*- coding: utf-8 -*-

import logging

from spaceone.core.service import *
from spaceone.secret.manager.credential_manager import CredentialManager
from spaceone.secret.manager.credential_group_manager import CredentialGroupManager
from spaceone.secret.manager.secret_connector_manager import SecretConnectorManager

_LOGGER = logging.getLogger(__name__)


@authentication_handler
@authorization_handler
@event_handler
class CredentialService(BaseService):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.credential_mgr: CredentialManager = self.locator.get_manager('CredentialManager')

    @transaction
    @check_required(['name', 'data', 'domain_id'])
    def create(self, params):
        """ Create credential

        Args:
            params (dict): {
                'name': 'str',
                'data': 'dict',
                'project_id': 'str',
                'issue_type': 'str',
                'plugin_info': 'dict',
                'tags': 'dict',
                'domain_id': 'str
            }

        Returns:
            credential_vo
        """

        secret_conn_mgr: SecretConnectorManager = self.locator.get_manager('SecretConnectorManager')

        credential_vo = self.credential_mgr.create_credential(params)
        secret_conn_mgr.create_credential(credential_vo.credential_id, params)

        return credential_vo

    @transaction
    @check_required(['credential_id', 'domain_id'])
    def update(self, params):
        """ Update credential

        Args:
            params (dict): {
                'credential_id': 'str',
                'name': 'str',
                'tags': 'dict',
                'domain_id': 'str'
            }

        Returns:
            credential_vo
        """

        credential_vo = self.credential_mgr.get_credential(params['credential_id'], params['domain_id'])

        update_param = {}
        if 'tags' in params:
            update_param['tags'] = params['tags']

        if 'name' in params:
            update_param['name'] = params['name']

        if update_param != {}:
            secret_conn_mgr: SecretConnectorManager = self.locator.get_manager('SecretConnectorManager')
            secret_conn_mgr.update_credential(update_param, credential_vo)
            credential_vo = self.credential_mgr.update_credential_by_vo(update_param, credential_vo)

        return credential_vo

    @transaction
    @check_required(['credential_id', 'domain_id'])
    def delete(self, params):
        """ Delete credential

        Args:
            params (dict): {
                'credential_id': 'str',
                'domain_id': 'str'
            }

        Returns:
            None
        """

        secret_conn_mgr: SecretConnectorManager = self.locator.get_manager('SecretConnectorManager')

        credential_vo = self.credential_mgr.get_credential(params['credential_id'], params['domain_id'])
        secret_conn_mgr.delete_credential(params['credential_id'])

        self.credential_mgr.delete_credential_by_vo(credential_vo)

    @transaction
    @check_required(['credential_id', 'domain_id'])
    def issue(self, params):
        """ Get credential data (or secret token) through backend Secret service

        Args:
            params (dict): {
                'credential_id': 'str',
                'domain_id': 'str'
            }

        Returns:
            (issue_type, secret)
            if issue_type is credential, secret is credentials(dict)
            if issue_type is secret, secret is token string

        """

        credential_vo = self.credential_mgr.get_credential(params['credential_id'], params['domain_id'])

        # Call a method dynamically based on a issue type
        secret = getattr(self, f'_issue_{credential_vo.issue_type}')(params['credential_id'])

        return credential_vo.issue_type, secret

    @transaction
    @check_required(['credential_id', 'domain_id'])
    def get(self, params):
        """ Get credential

        Args:
            params (dict): {
                'credential_id': 'str',
                'domain_id': 'str'
            }

        Returns:
            credential_vo
        """

        return self.credential_mgr.get_credential(params['credential_id'], params['domain_id'])

    @transaction
    @check_required(['domain_id'])
    @append_query_filter(['credential_id', 'name', 'domain_id'])
    def list(self, params):
        """ List credentials

        Args:
            params (dict): {
                'credential_id': 'str',
                'name': 'str',
                'include_credential_group': 'bool',
                'credential_group_id': 'str',
                'query': 'dict',
                'domain_id': 'str'
            }

        Returns:
            results (list)
            total_count (int)
        """

        query = params.get('query', {})
        credential_vos, total_count = self.credential_mgr.list_credentials(query,
                                                                           params.get('include_credential_group', None),
                                                                           params.get('credential_group_id', None)
                                                                           )

        return credential_vos, total_count

    def _issue_credential(self, credential_id):
        secret_conn_mgr: SecretConnectorManager = self.locator.get_manager('SecretConnectorManager')
        return secret_conn_mgr.get_credential(credential_id)

    # TODO: Not Implemented yet
    def _issue_token(self, credential_id):
        return None
