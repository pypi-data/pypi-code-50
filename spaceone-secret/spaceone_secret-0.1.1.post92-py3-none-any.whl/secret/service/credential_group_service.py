# -*- coding: utf-8 -*-

import logging

from spaceone.core.service import *
from spaceone.secret.error.custom import *
from spaceone.secret.manager.credential_group_manager import CredentialGroupManager
from spaceone.secret.manager.credential_manager import CredentialManager

_LOGGER = logging.getLogger(__name__)


@authentication_handler
@authorization_handler
@event_handler
class CredentialGroupService(BaseService):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.credential_group_mgr: CredentialGroupManager = self.locator.get_manager('CredentialGroupManager')

    @transaction
    @check_required(['name', 'domain_id'])
    def create(self, params):
        """ Create credential group

        Args:
            params (dict): {
                'name': 'str',
                'credentials': 'list',
                'tags': 'dict',
                'domain_id': 'str'
            }

        Returns:
            credential_group_vo
        """

        credential_mgr: CredentialManager = self.locator.get_manager('CredentialManager')

        if 'credentials' in params:
            params['credentials'] = list(map(lambda cred_id: credential_mgr.get_credential(cred_id, params['domain_id']),
                                             params.get('credentials', [])))

        return self.credential_group_mgr.create_credential_group(params)

    @transaction
    @check_required(['credential_group_id', 'domain_id'])
    def update(self, params):
        """ Update credential group

        Args:
            params (dict): {
                'credential_group_id' : 'str',
                'name': 'str',
                'reset_credential': 'bool',
                'tags': 'dict',
                'domain_id': 'str'
            }

        Returns:
            credential_group_vo
        """

        cred_grp_vo = self.credential_group_mgr.get_credential_group(params['credential_group_id'],
                                                                     params['domain_id'])

        return self.credential_group_mgr.update_credential_group_by_vo(params, cred_grp_vo)

    @transaction
    @check_required(['credential_group_id', 'domain_id'])
    def delete(self, params):
        """ Delete credential group

        Args:
            params (dict): {
                'credential_group_id' : 'str',
                'domain_id': 'str'
            }

        Returns:
            None
        """

        cred_group_vo = self.credential_group_mgr.get_credential_group(params['credential_group_id'],
                                                                       params['domain_id'])

        self.credential_group_mgr.delete_credential_group_by_vo(cred_group_vo)

    @transaction
    @check_required(['credential_group_id', 'credential_id', 'domain_id'])
    def add_credential(self, params):
        """ Add credential

        Args:
            params (dict): {
                'credential_group_id' : 'str',
                'credential_id: 'str',
                'domain_id': 'str'
            }

        Returns:
            credential_group_vo
        """
        credential_mgr: CredentialManager = self.locator.get_manager('CredentialManager')
        credential_group_id = params['credential_group_id']
        credential_id = params['credential_id']
        domain_id = params['domain_id']

        cred_grp_vo = self.credential_group_mgr.get_credential_group(credential_group_id, domain_id)
        cred_vo = credential_mgr.get_credential(credential_id, domain_id)

        self._check_not_exist_credential_in_group(cred_grp_vo, cred_vo)
        self.credential_group_mgr.add_credential(cred_grp_vo, cred_vo)

        return cred_grp_vo

    @transaction
    @check_required(['credential_group_id', 'credential_id', 'domain_id'])
    def remove_credential(self, params):
        """ Remove credential

        Args:
            params (dict): {
                'credential_group_id' : 'str',
                'credential_id: 'str',
                'domain_id': 'str'
            }

        Returns:
            credential_group_vo
        """
        credential_mgr: CredentialManager = self.locator.get_manager('CredentialManager')
        credential_group_id = params['credential_group_id']
        credential_id = params['credential_id']
        domain_id = params['domain_id']

        cred_grp_vo = self.credential_group_mgr.get_credential_group(credential_group_id, domain_id)
        credential_vo = credential_mgr.get_credential(credential_id, domain_id)

        self._check_exist_credential_in_group(cred_grp_vo, credential_vo)
        self.credential_group_mgr.remove_credential(cred_grp_vo, credential_vo)

    @transaction
    @check_required(['credential_group_id', 'domain_id'])
    def get(self, params):
        """ Get credential group

        Args:
            params (dict): {
                'credential_group_id': 'str',
                'domain_id': 'str'
            }

        Returns:
            None

        """

        return self.credential_group_mgr.get_credential_group(params['credential_group_id'],
                                                              params['domain_id'])

    @transaction
    @check_required(['domain_id'])
    @append_query_filter(['credential_group_id', 'name', 'domain_id'])
    def list(self, params):
        """ List credential groups

        Args:
            params (dict): {
                'credential_group_id': 'str',
                'name': 'str',
                'credential_id': 'str',
                'query': 'dict',
                'domain_id': 'str'
            }

        Returns:
            results (list)
            total_count (int)
        """

        query = params.get('query', {})
        return self.credential_group_mgr.list_credential_groups(query, params.get('credential_id', None))

    def _check_not_exist_credential_in_group(self, cred_grp_vo, cred_vo):
        cred_grp_map_vos, total_count = self._list_credential_group_map(cred_grp_vo, cred_vo)

        if total_count > 0:
            raise ERROR_ALREADY_EXIST_CREDENTIAL_IN_GROUP(credential_id=cred_vo.credential_id,
                                                          credential_group_id=cred_grp_vo.credential_group_id)

    def _check_exist_credential_in_group(self, cred_grp_vo, cred_vo):
        cred_grp_map_vos, total_count = self._list_credential_group_map(cred_grp_vo, cred_vo)

        if total_count == 0:
            raise ERROR_NOT_EXIST_CREDENTIAL_IN_GROUP(credential_id=cred_vo.credential_id,
                                                      credential_group_id=cred_grp_vo.credential_group_id)

    def _list_credential_group_map(self, cred_grp_vo, cred_vo):
        query = {
            'filter': [
                {'k': 'credential_group_id', 'v': cred_grp_vo.credential_group_id, 'o': 'eq'},
                {'k': 'credential_id', 'v': cred_vo.credential_id, 'o': 'eq'}
            ]
        }

        return self.credential_group_mgr.list_credential_group_maps(query)