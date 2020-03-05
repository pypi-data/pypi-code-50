# -*- coding: utf-8 -*-
# Copyright (c) 2016 - 2020 Sqreen. All rights reserved.
# Please refer to our terms for more information:
#
#     https://www.sqreen.io/terms.html
#

import logging

from ..actions import ACTION_STORE, ActionName
from ..rules import RuleCallback
from ..sdk import events

LOGGER = logging.getLogger(__name__)


class IPActionCB(RuleCallback):

    INTERRUPTIBLE = False

    def pre(self, instance, args, kwargs, **options):
        request = self.storage.get_current_request()
        if request is None:
            return
        client_ip = request.raw_client_ip
        if client_ip is None:
            return
        action = ACTION_STORE.get_for_ip(client_ip)
        if action is None:
            return
        events.track_action(action, {"ip_address": str(client_ip)},
                            storage=self.storage)
        if action.name == ActionName.BLOCK_IP:
            LOGGER.debug(
                "IP %s is blacklisted by action %s",
                client_ip,
                action.iden,
            )
            return {
                "status": "action_block",
                "action_id": action.iden,
                "immediate": True,
            }
        elif action.name == ActionName.REDIRECT_IP:
            LOGGER.debug(
                "IP %s is redirected to %r by action %s",
                client_ip,
                action.target_url,
                action.iden,
            )
            return {
                "status": "action_redirect",
                "action_id": action.iden,
                "target_url": action.target_url,
                "immediate": True,
            }
