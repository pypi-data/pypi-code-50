#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Use of this source is governed by the MIT license, see LICENSE file.
#-------------------------------------------------------------------------------


"""
This module contains database layer for *Vial* application.
"""


import flask_sqlalchemy


_DB = None


def db_setup(**kwargs):
    """
    Opens a new database connection if there is none yet for the
    current application context.

    :return: Database storage handler.
    :rtype: flask_sqlalchemy.SQLAlchemy
    """
    global _DB  # pylint: disable=locally-disabled,global-statement
    if not _DB:
        _DB = flask_sqlalchemy.SQLAlchemy(**kwargs)

    return _DB

def db_get():
    """
    Convenience method.
    """
    return _DB


def db_session():
    """
    Convenience method.
    """
    return db_get().session


def db_query(dbmodel):
    """
    Convenience method.
    """
    return db_session().query(dbmodel)
