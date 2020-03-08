#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains utilities functions to work with Alembics
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

from tpDcc.libs.python import decorators

import artellapipe.register


class AbstractAlembic(object):

    @decorators.abstractmethod
    def load_alembic_plugin(self):
        """
        Forces the loading of the Alembic plugin if it is not already loaded
        """

        raise NotImplementedError(
            'load_alembic_plugin function for "{}" is not implemented!'.format(self.__class__.__name__))

    @decorators.abstractmethod
    def export_alembic(self, *args, **kwargs):
        """
        Exports Alembic file with given attributes
        """

        raise NotImplementedError(
            'export_alembic function for "{}" is not implemented!'.format(self.__class__.__name__))

    @decorators.abstractmethod
    def import_alembic(self, alembic_file, mode='import', nodes=None, parent=None, fix_path=False,
                       namespace=None, reference=False):
        """
        Imports Alembic into current DCC scene

        :param str alembic_file: file we want to load
        :param str mode: mode we want to use to import the Alembic File
        :param list(str) nodes: optional list of nodes to import
        :param parent:
        :param fix_path: bool, whether to fix path or not
        :param namespace: str
        :param reference: bool, whether to fix path or not
        :return:
        """

        raise NotImplementedError(
            'import_alembic function for "{}" is not implemented!'.format(self.__class__.__name__))


@decorators.Singleton
class AbstractAlembicSingleton(AbstractAlembic, object):
    def __init__(self):
        AbstractAlembic.__init__(self)


artellapipe.register.register_class('Alembic', AbstractAlembicSingleton)
