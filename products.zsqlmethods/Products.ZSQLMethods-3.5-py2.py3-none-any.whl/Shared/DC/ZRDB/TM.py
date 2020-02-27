##############################################################################
#
# Copyright (c) 2002 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE
#
##############################################################################
"""Provide support for linking an external transaction manager with Zope's
"""
import logging
from warnings import warn

import transaction
from transaction.interfaces import IDataManager
from transaction.interfaces import TransactionFailedError
from zope.interface import implementer


LOG = logging.getLogger('Products.ZSQLMethods')


@implementer(IDataManager)
class TM:
    """Mix-in class that provides transaction management support

    A sub class should call self._register() whenever it performs any
    transaction-dependent operations (e.g. sql statements).

    The sub class will need to override _finish, to finalize work,
    _abort, to roll-back work, and perhaps _begin, if any work is
    needed at the start of a transaction.

    A subclass that uses locking during transaction commit must
    define a sortKey() method.
    """

    _registered = None
    transaction_manager = transaction.manager

    def _begin(self):
        pass

    def _register(self):
        if not self._registered:
            try:
                self.transaction_manager.get().join(self)
            except TransactionFailedError:
                LOG.error('Failed to join transaction: ', exc_info=True)
                # No need to raise here, the transaction is already
                # broken as a whole
            except ValueError:
                LOG.error('Failed to join transaction: ', exc_info=True)
                # Raising here, the transaction is in an invalid state
                raise
            else:
                self._begin()
                self._registered = 1
                self._finalize = 0

    def tpc_begin(self, *ignored):
        pass

    commit = tpc_begin

    def _finish(self):
        self.db.commit()

    def _abort(self):
        self.db.rollback()

    def tpc_vote(self, *ignored):
        self._finalize = 1

    def tpc_finish(self, *ignored):

        if self._finalize:
            try:
                self._finish()
            finally:
                self._registered = 0

    __inform_commit__ = tpc_finish

    def abort(self, *ignored):
        try:
            self._abort()
        finally:
            self._registered = 0

    tpc_abort = abort
    __inform_abort__ = abort

    # Most DA's talking to RDBMS systems do not care about commit order, so
    # return a constant. Must be a string according to ITransactionManager.
    _sort_key = '1'

    def sortKey(self, *ignored):
        """ The sortKey method is used by the transaction subsystem to have a
            known commit order for lock acquisition.
        """
        return self._sort_key

    def setSortKey(self, sort_key):
        self._sort_key = str(sort_key)


# BBB version 4
class Surrogate:

    def __init__(self, db):
        warn(u'The Surrogate class is deprecated and will be removed in '
             u'Products.ZSQLMethods version 4.')
        self._p_jar = db
        self.__inform_commit__ = db.tpc_finish
        self.__inform_abort__ = db.tpc_abort
