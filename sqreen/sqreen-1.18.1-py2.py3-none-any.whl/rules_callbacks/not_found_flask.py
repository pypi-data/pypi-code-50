# -*- coding: utf-8 -*-
# Copyright (c) 2016 - 2020 Sqreen. All rights reserved.
# Please refer to our terms for more information:
#
#     https://www.sqreen.io/terms.html
#
""" Look for badly behaved clients
"""
from logging import getLogger

from ..rules import RuleCallback

LOGGER = getLogger(__name__)


class NotFoundCBFlask(RuleCallback):
    def post(self, instance, args, kwargs, result=None, **options):
        response = result
        if response.status_code == 404:
            current_request = self.storage.get_current_request()

            # A 404 may prevent record request context to store the request
            # store it without arguments
            if current_request is None:
                LOGGER.warning("No request was recorded abort")
                return

            infos = {
                "path": current_request.path,
                "host": current_request.hostname,
                "verb": current_request.method,
                "ua": current_request.client_user_agent,
            }
            self.record_attack(infos)
