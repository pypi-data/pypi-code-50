# -*- coding: utf-8 -*-

import logging

from spaceone.core.manager import BaseManager
from spaceone.secret.model.credential_model import Credential
from spaceone.secret.model.credential_group_model import CredentialGroupMap

_LOGGER = logging.getLogger(__name__)


class CredentialManager(BaseManager):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.credential_model: Credential = self.locator.get_model('Credential')

    def create_credential(self, params):
        def _rollback(credential_vo):
            _LOGGER.info(f'[ROLLBACK] Delete credential : {credential_vo.name} ({credential_vo.credential_id})')
            credential_vo.delete()

        credential_vo: Credential = self.credential_model.create(params)

        self.transaction.add_rollback(_rollback, credential_vo)

        return credential_vo

    def update_credential(self, params):
        self.update_credential_by_vo(params, self.get_credential(params['credential_id'],
                                                                 params['domain_id']))

    def update_credential_by_vo(self, params, credential_vo):
        def _rollback(old_data):
            _LOGGER.info(f'[ROLLBACK] Revert Data : {old_data["name"]} ({old_data["credential_id"]})')
            credential_vo.update(old_data)

        self.transaction.add_rollback(_rollback, credential_vo.to_dict())

        return credential_vo.update(params)

    def delete_credential(self, credential_id, domain_id):
        self.delete_credential_by_vo(self.get_credential(credential_id, domain_id))

    def get_credential(self, credential_id, domain_id):
        return self.credential_model.get(credential_id=credential_id, domain_id=domain_id)

    def list_credentials(self, query, include_credential_group, credential_group_id):
        if credential_group_id is not None:
            query = self._add_credential_group_filter_query(query, credential_group_id)

        credential_vos, cred_total_count = self.credential_model.query(**query)

        if include_credential_group:
            include_cred_grp_filter = {
                'filter': [{
                    'k': 'credential_id',
                    'v': list(map(lambda cred: cred.credential_id, credential_vos)),
                    'o': 'in'
                }]
            }

            credential_group_map_model: CredentialGroupMap = self.locator.get_model('CredentialGroupMap')
            map_vos, total_count = credential_group_map_model.query(include_cred_grp_filter)

            for cred_vo in credential_vos:
                credential_groups = []
                for map_vo in map_vos:
                    if map_vo.credential == cred_vo:
                        credential_groups.append(map_vo.credential_group)

                setattr(cred_vo, 'credential_groups', credential_groups)

        return credential_vos, cred_total_count

    def _add_credential_group_filter_query(self, query, credential_group_id):
        map_query = {
            'filter': [{
                'k': 'credential_group_id',
                'v': credential_group_id,
                'o': 'eq'
            }]
        }

        credential_group_map_model: CredentialGroupMap = self.locator.get_model('CredentialGroupMap')
        map_vos, total_count = credential_group_map_model.query(**map_query)

        _filter = query['filter']
        _filter.append({
            'k': 'credential_id',
            'v': list(map(lambda map_vo: map_vo.credential.credential_id, map_vos)),
            'o': 'in'
        })

        return query

    @staticmethod
    def delete_credential_by_vo(credential_vo):
        credential_vo.delete()
