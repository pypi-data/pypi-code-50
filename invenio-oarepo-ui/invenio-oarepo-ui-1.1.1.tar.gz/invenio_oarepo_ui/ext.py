# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CESNET.
#
# invenio-oarepo-ui is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""OARepo UI module for invenio"""

from __future__ import absolute_import, print_function

from flask import g, request
from flask_babelex import Babel

from . import config


class OARepoUI(object):
    """invenio-oarepo-ui extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.init_config(app)
        app.extensions['invenio-oarepo-ui'] = self

        def get_locale():
            current_lang = request.cookies.get('language')
            if current_lang:
                return current_lang
            user = getattr(g, 'user', None)
            if user is not None:
                return user.locale
            return request.accept_languages.best_match(['cs', 'en'])

        self.babelex = Babel(app)
        self.babelex.localeselector(get_locale)

    def init_config(self, app):
        """Initialize configuration."""
        for k in dir(config):
            if k.startswith('INVENIO_OAREPO_UI_'):
                app.config.setdefault(k, getattr(config, k))
