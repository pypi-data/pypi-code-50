# -*- coding: utf-8 -*-
# Copyright (c) 2016 - 2020 Sqreen. All rights reserved.
# Please refer to our terms for more information:
#
#     https://www.sqreen.io/terms.html
#
""" Record response
"""

from logging import getLogger

from ..frameworks.wsgi import WSGIResponse
from ..rules import RuleCallback

LOGGER = getLogger(__name__)


class RecordResponse(RuleCallback):
    """ Record a WSGI response.
    """

    INTERRUPTIBLE = False

    def pre(self, instance, args, kwargs, **options):
        """ Store the response.
        """
        current_request = self.storage.get_current_request()
        # Do not set a response if we don't have a request yet.
        if current_request is not None:
            response = WSGIResponse(*args[:2])
            self.storage.store_response_default(response)
