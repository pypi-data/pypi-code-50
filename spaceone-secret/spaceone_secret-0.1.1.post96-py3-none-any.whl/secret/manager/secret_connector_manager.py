# -*- coding: utf-8 -*-

import logging

from spaceone.core.manager import BaseManager
from spaceone.secret.connector.secret_connector import SecretConnector

_LOGGER = logging.getLogger(__name__)


class SecretConnectorManager(BaseManager):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.secret_conn: SecretConnector = self.locator.get_connector('SecretConnector')

    def create_credential(self, credential_id, params):
        def _rollback(credential_id):
            _LOGGER.info(f'[ROLLBACK] Delete credential data in secret store : {credential_id}')
            self.secret_conn.delete_secret(credential_id)

        self.transaction.add_rollback(_rollback, credential_id)
        return self.secret_conn.create_secret(credential_id, params)

    def update_credential(self, params, credential_vo):
        def _rollback(old_data):
            _LOGGER.info(f'[ROLLBACK] Revert data in secret store : {credential_vo.credential_id}')
            pass

        self.transaction.add_rollback(_rollback, credential_vo.tags)

        return self.secret_conn.update_secret(credential_vo.credential_id, params)

    def delete_credential(self, credential_id):
        self.secret_conn.delete_secret(credential_id)

    def get_credential(self, credential_id):
        return self.secret_conn.get_secret(credential_id)
