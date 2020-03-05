'''_1386.py

CustomReportDefinitionItem
'''


from mastapy.utility.report import _1396
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_DEFINITION_ITEM = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomReportDefinitionItem')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomReportDefinitionItem',)


class CustomReportDefinitionItem(_1396.CustomReportNameableItem):
    '''CustomReportDefinitionItem

    This is a mastapy class.
    '''

    TYPE = _CUSTOM_REPORT_DEFINITION_ITEM

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CustomReportDefinitionItem.TYPE'):
        super().__init__(instance_to_wrap)
