# -*- coding: utf-8 -*-
import sys

sys.path.append(sys.modules['__main__'])

from aishow_model_app.apis.resource_api import ResourceApi


def init_api(app):
    ResourceApi.init_app(app)
