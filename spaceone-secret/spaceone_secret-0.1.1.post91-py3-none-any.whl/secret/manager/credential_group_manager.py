# -*- coding: utf-8 -*-

import logging
from spaceone.core.manager import BaseManager
from spaceone.secret.model.credential_group_model import CredentialGroup, CredentialGroupMap

_LOGGER = logging.getLogger(__name__)


class CredentialGroupManager(BaseManager):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.credential_group_model: CredentialGroup = self.locator.get_model('CredentialGroup')
        self.credential_group_map_model: CredentialGroupMap = self.locator.get_model('CredentialGroupMap')

    def create_credential_group(self, params):
        def _rollback(credential_group_vo):
            # TODO : ADD rollback process for credential_group_map
            _LOGGER.info(
                f'[ROLLBACK] Delete credential group : {credential_group_vo.name} ({credential_group_vo.credential_group_id})')
            credential_group_vo.delete()

        credential_group_vo: CredentialGroup = self.credential_group_model.create(params)
        self.transaction.add_rollback(_rollback, credential_group_vo)

        return credential_group_vo

    def update_credential_group(self, params):
        self.update_credential_group_by_vo(params, self.get_credential_group(params['credential_group_id'],
                                                                             params['domain_id']))

    def update_credential_group_by_vo(self, params, credential_group_vo):
        def _rollback(old_data):
            _LOGGER.info(f'[ROLLBACK] Revert Data : {old_data["name"]} ({old_data["credential_group_id"]})')
            credential_group_vo.update(old_data)

        self.transaction.add_rollback(_rollback, credential_group_vo.to_dict())

        return credential_group_vo.update(params)

    def delete_credential_group(self, credential_group_id, domain_id):
        self.delete_credential_group_by_vo(self.get_credential_group(credential_group_id, domain_id))

    def get_credential_group(self, credential_group_id, domain_id):
        return self.credential_group_model.get(credential_group_id=credential_group_id,
                                               domain_id=domain_id)

    def list_credential_groups(self, query, credential_id):
        if credential_id is not None:
            query = self._add_credential_filter_query(query, credential_id)

        return self.credential_group_model.query(**query)

    def list_credential_group_maps(self, query):
        return self.credential_group_map_model.query(**query)

    def _add_credential_filter_query(self, query, credential_id):
        map_query = {
            'filter': [{
                'k': 'credential_id',
                'v': credential_id,
                'o': 'eq'
            }]
        }
        map_vos, total_count = self.credential_group_map_model.query(map_query)

        _filter = query['filter']
        _filter.append({
            'k': 'credential_group_id',
            'v': list(map(lambda map_vo: map_vo.credential_group.credential_group_id, map_vos)),
            'o': 'in'
        })

        return query

    @staticmethod
    def add_credential(credential_group_vo, credential_vo):
        credential_group_vo.append('credentials', credential_vo)

    @staticmethod
    def remove_credential(credential_group_vo, credential_vo):
        credential_group_vo.remove('credentials', credential_vo)

    @staticmethod
    def delete_credential_group_by_vo(credential_group_vo):
        credential_group_vo.delete()
