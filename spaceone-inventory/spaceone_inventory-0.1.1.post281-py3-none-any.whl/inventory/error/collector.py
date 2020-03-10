# -*- coding: utf-8 -*-
from spaceone.core.error import *


class ERROR_TOKEN_AUTHENTICATION_FAILURE(ERROR_BASE):
    _message = 'A access token or refresh token is invalid.'


class ERROR_AUTHENTICATION_FAILURE_PLUGIN(ERROR_BASE):
    _message = 'External plugin authentication exception. (plugin_error_message={message})'

