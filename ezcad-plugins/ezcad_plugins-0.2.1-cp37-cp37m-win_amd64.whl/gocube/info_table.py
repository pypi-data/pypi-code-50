# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

from math import sqrt
from ezcad.config.base import _
from ezcad.widgets.list2table import list2table


def dict_vidx_table(dict_vidx):

    column_names = ['Axis', 'First', 'Last', 'Increment', 'Amount']

    listRow1 = ['iline', dict_vidx['IL_FRST'], dict_vidx['IL_LAST'],
                dict_vidx['IL_NCRT'], dict_vidx['IL_AMNT']]
    listRow2 = ['xline', dict_vidx['XL_FRST'], dict_vidx['XL_LAST'],
                dict_vidx['XL_NCRT'], dict_vidx['XL_AMNT']]
    listRow3 = ['depth', dict_vidx['DP_FRST'], dict_vidx['DP_LAST'],
                dict_vidx['DP_NCRT'], dict_vidx['DP_AMNT']]
    listData = [listRow1, listRow2, listRow3]

    table_name = _("Cube physical index")
    table = list2table(listData, column_names, table_name=table_name)
    return table


def dict_vxyz_table(dict_vxyz):

    column_names = ['Axis', 'X', 'Y', 'Z', 'Length']

    lenOR = 0.0
    lenIL = sqrt((dict_vxyz['AXIS_ILX'] - dict_vxyz['AXIS_ORX'])**2 +
                 (dict_vxyz['AXIS_ILY'] - dict_vxyz['AXIS_ORY'])**2)
    lenXL = sqrt((dict_vxyz['AXIS_XLX'] - dict_vxyz['AXIS_ORX'])**2 +
                 (dict_vxyz['AXIS_XLY'] - dict_vxyz['AXIS_ORY'])**2)
    lenDP = dict_vxyz['AXIS_DPZ'] - dict_vxyz['AXIS_ORZ']

    x = dict_vxyz['AXIS_ILX'] + dict_vxyz['AXIS_XLX'] - dict_vxyz['AXIS_ORX']
    y = dict_vxyz['AXIS_ILY'] + dict_vxyz['AXIS_XLY'] - dict_vxyz['AXIS_ORY']
    z = dict_vxyz['AXIS_ORZ']
    lenDiagonal = sqrt((x - dict_vxyz['AXIS_ORX'])**2 +
                       (y - dict_vxyz['AXIS_ORY'])**2)

    listRow1 = ['origin', dict_vxyz['AXIS_ORX'], dict_vxyz['AXIS_ORY'],
                dict_vxyz['AXIS_ORZ'], lenOR]
    listRow2 = ['iline', dict_vxyz['AXIS_ILX'], dict_vxyz['AXIS_ILY'],
                dict_vxyz['AXIS_ILZ'], lenIL]
    listRow3 = ['xline', dict_vxyz['AXIS_XLX'], dict_vxyz['AXIS_XLY'],
                dict_vxyz['AXIS_XLZ'], lenXL]
    listRow4 = ['diagonal', x, y, z, lenDiagonal]
    listRow5 = ['depth', dict_vxyz['AXIS_DPX'], dict_vxyz['AXIS_DPY'],
                dict_vxyz['AXIS_DPZ'], lenDP]
    listData = [listRow1, listRow2, listRow3, listRow4, listRow5]

    table_name = _("Cube corner coordinate")
    table = list2table(listData, column_names, table_name=table_name)
    return table


def dict_sgmt_table(dict_sgmt):
    column_names = ['Corner', 'ILNO', 'XLNO', 'X', 'Y']

    listRow1 = ['Point A', dict_sgmt['P1_ILNO'], dict_sgmt['P1_XLNO'],
                dict_sgmt['P1_CRSX'], dict_sgmt['P1_CRSY']]
    listRow2 = ['Point B', dict_sgmt['P2_ILNO'], dict_sgmt['P2_XLNO'],
                dict_sgmt['P2_CRSX'], dict_sgmt['P2_CRSY']]
    listRow3 = ['Point C', dict_sgmt['P3_ILNO'], dict_sgmt['P3_XLNO'],
                dict_sgmt['P3_CRSX'], dict_sgmt['P3_CRSY']]
    listData = [listRow1, listRow2, listRow3]

    table_name = _("Survey geometry")
    table = list2table(listData, column_names, table_name=table_name)
    return table


def dict_parm_table(dict_parm):
    column_names = ['Name', 'Axis', 'Step', 'Unit', 'DeltaX', 'DeltaY']

    listRow1 = ['PANEL', 'iline', dict_parm['PANEL_INC'],
                dict_parm['PANEL_UNIT'], dict_parm['PNDX'], dict_parm['PNDY']]
    listRow2 = ['TRACE', 'xline', dict_parm['TRACE_INC'],
                dict_parm['TRACE_UNIT'], dict_parm['TRDX'], dict_parm['TRDY']]
    listRow3 = ['SAMPLE', 'depth', dict_parm['SAMPLE_INC'],
                dict_parm['SAMPLE_UNIT'], 0, 0]
    listData = [listRow1, listRow2, listRow3]

    table_name = _("VTB binary cube parameters")
    table = list2table(listData, column_names, table_name=table_name)
    return table
