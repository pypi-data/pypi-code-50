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

import os
import logging

import tpDcc as tp
from tpDcc.libs.python import decorators

import artellapipe.register
from artellapipe.utils import exceptions
from artellapipe.libs.alembic.core import alembic

LOGGER = logging.getLogger()


class HoudiniAlembic(alembic.AbstractAlembic):

    def import_alembic(self, alembic_file, mode='import', nodes=None, parent=None, fix_path=False, reference=False):
        """
        Imports Alembic into current DCC scene

        :param str alembic_file: file we want to load
        :param str mode: mode we want to use to import the Alembic File
        :param list(str) nodes: optional list of nodes to import
        :param parent:
        :param fix_path: bool, whether to fix path or not
        :param reference: bool,
        :return:
        """

        if not os.path.exists(alembic_file):
            LOGGER.error('Given Alembic File: {} does not exists!'.format(alembic_file))
            tp.Dcc.confirm_dialog(
                title='Error',
                message='Alembic File does not exists:\n{}'.format(alembic_file)
            )
            return None

        LOGGER.debug(
            'Import Alembic File (%s) with job arguments:\n\t(alembic_file) %s\n\t(nodes) %s', mode,
            alembic_file, nodes)

        res = None
        try:
            if fix_path:
                abc_file = artellapipe.FilesMgr().fix_path(alembic_file)
            else:
                abc_file = alembic_file

            if not parent:
                LOGGER.warning('Impossible to import Alembic File because not Alembic parent given!')
                return False
            parent.parm('fileName').set(abc_file)
            build_hierarch_param = parent.parm('buildHierarchy')
            if build_hierarch_param:
                build_hierarch_param.pressButton()

        except RuntimeError as exc:
            exceptions.capture_sentry_exception(exc)
            return res

        LOGGER.debug('Alembic File %s imported successfully!', os.path.basename(alembic_file))
        return res


@decorators.Singleton
class HoudiniAlembicSingleton(HoudiniAlembic, object):
    def __init__(self):
        HoudiniAlembic.__init__(self)


artellapipe.register.register_class('Alembic', HoudiniAlembicSingleton)
