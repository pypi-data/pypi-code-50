# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

from ezcad.config.base import _
from ezcad.widgets.list2table import list2table


def dict_sidx_table(dict_sidx):

    column_names = ['Axis', 'First', 'Last', 'Increment', 'Amount']

    listRow1 = ['iline', dict_sidx['IL_FRST'], dict_sidx['IL_LAST'],
                dict_sidx['IL_NCRT'], dict_sidx['IL_AMNT']]
    listRow2 = ['xline', dict_sidx['XL_FRST'], dict_sidx['XL_LAST'],
                dict_sidx['XL_NCRT'], dict_sidx['XL_AMNT']]
    listData = [listRow1, listRow2]

    table_name = _("Grid physical index")
    table = list2table(listData, column_names, table_name=table_name)
    return table
