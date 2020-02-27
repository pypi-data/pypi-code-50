"""Ocean module."""
#  Copyright 2018 Ocean Protocol Foundation
#  SPDX-License-Identifier: Apache-2.0

import logging

from ocean_utils.agreements.service_types import ServiceTypes

logger = logging.getLogger(__name__)


class OceanTemplates:
    """Ocean templates class."""

    def __init__(self, keeper, config):
        self._keeper = keeper
        self._config = config
        self.access_template_id = self._keeper.get_agreement_template_id(ServiceTypes.ASSET_ACCESS)

    def propose(self, template_id, account):
        """
        Propose a new template.

        :param template_id: hex str bytes32 ID of the template
        :param account: account proposing the template, Account
        :return: bool
        """
        try:
            proposed = self._keeper.template_manager.propose_template(template_id, account)
            return proposed
        except ValueError as err:
            template_values = self._keeper.template_manager.get_template(template_id)
            if not template_values:
                logger.warning(f'Propose template failed: {err}')
                return False

            if template_values.state != 1:
                logger.warning(
                    f'Propose template failed, current state is set to {template_values.state}')
                return False

            return True

    def approve(self, template_id, account):
        """
        Approve a template already proposed. The account needs to be owner of the templateManager
        contract to be able of approve the template.

        :param template_id: hex str bytes32 ID of the template
        :param account: account approving the template, Account
        :return: bool
        """
        try:
            approved = self._keeper.template_manager.approve_template(template_id, account)
            return approved
        except ValueError as err:
            template_values = self._keeper.template_manager.get_template(template_id)
            if not template_values:
                logger.warning(f'Approve template failed: {err}')
                return False

            if template_values.state == 1:
                logger.warning(f'Approve template failed, this template is '
                               f'currently in "proposed" state.')
                return False

            if template_values.state == 3:
                logger.warning(f'Approve template failed, this template appears to be '
                               f'revoked.')
                return False

            if template_values.state == 2:
                return True

            return False

    def revoke(self, template_id, account):
        """
        Revoke a template already approved. The account needs to be owner of the templateManager
        contract to be able of revoke the template.

        :param template_id: hex str bytes32 ID of the template
        :param account: account revoking the template, Account
        :return: bool
        """
        try:
            revoked = self._keeper.template_manager.revoke_template(template_id, account)
            return revoked
        except ValueError as err:
            template_values = self._keeper.template_manager.get_template(template_id)
            if not template_values:
                logger.warning(f'Cannot revoke template since it does not exist: {err}')
                return False

            logger.warning(f'Only template admin or owner can revoke a template: {err}')
            return False
