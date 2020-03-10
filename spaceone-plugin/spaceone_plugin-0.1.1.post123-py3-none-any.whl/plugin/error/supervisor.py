# -*- coding: utf-8 -*-
from spaceone.core.error import *


class ERROR_NO_POSSIBLE_SUPERVISOR(ERROR_BASE):
    _message = 'There is no supervisor to run plugin. params: {params}'
