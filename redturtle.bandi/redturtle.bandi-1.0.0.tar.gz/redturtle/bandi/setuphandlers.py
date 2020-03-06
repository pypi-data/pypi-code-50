# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger('redturtle.bandi')


def import_various(context):
    if context.readDataFile('redturtle.bandi_various.txt') is None:
        return
