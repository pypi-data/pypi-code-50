# -*- coding: utf-8 -*-
# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.pool import Pool
from .purchaseline import PurchaseLine
from .purchase import Purchase


def register():
    Pool.register(
        Purchase,
        PurchaseLine,
        module='purchase_line_twocolumn', type_='model')
