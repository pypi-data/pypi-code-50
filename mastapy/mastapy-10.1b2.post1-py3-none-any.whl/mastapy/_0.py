'''_0.py

ICanOutputReportsExtensions
'''


from typing import List

from mastapy import _6491
from mastapy._internal import constructor
from mastapy._internal.python_net import python_net_import

_I_CAN_OUTPUT_REPORTS_EXTENSIONS = python_net_import('SMT.MastaAPI', 'ICanOutputReportsExtensions')


__docformat__ = 'restructuredtext en'
__all__ = ('ICanOutputReportsExtensions',)


class ICanOutputReportsExtensions:
    '''ICanOutputReportsExtensions

    This is a mastapy class.
    '''

    TYPE = _I_CAN_OUTPUT_REPORTS_EXTENSIONS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ICanOutputReportsExtensions.TYPE'):
        self.wrapped = instance_to_wrap

    @staticmethod
    def output_default_report_to(can_output: '_6491.ICanOutputReports', file_path: 'str'):
        ''' 'OutputDefaultReportTo' is the original name of this method.

        Args:
            can_output (mastapy.ICanOutputReports)
            file_path (str)
        '''

        file_path = str(file_path)
        ICanOutputReportsExtensions.TYPE.OutputDefaultReportTo(can_output.wrapped if can_output else None, file_path if file_path else None)

    @staticmethod
    def get_default_report_with_encoded_images(can_output: '_6491.ICanOutputReports') -> 'str':
        ''' 'GetDefaultReportWithEncodedImages' is the original name of this method.

        Args:
            can_output (mastapy.ICanOutputReports)

        Returns:
            str
        '''

        method_result = ICanOutputReportsExtensions.TYPE.GetDefaultReportWithEncodedImages(can_output.wrapped if can_output else None)
        return method_result

    @staticmethod
    def output_active_report_to(can_output: '_6491.ICanOutputReports', file_path: 'str'):
        ''' 'OutputActiveReportTo' is the original name of this method.

        Args:
            can_output (mastapy.ICanOutputReports)
            file_path (str)
        '''

        file_path = str(file_path)
        ICanOutputReportsExtensions.TYPE.OutputActiveReportTo(can_output.wrapped if can_output else None, file_path if file_path else None)

    @staticmethod
    def output_active_report_as_text_to(can_output: '_6491.ICanOutputReports', file_path: 'str'):
        ''' 'OutputActiveReportAsTextTo' is the original name of this method.

        Args:
            can_output (mastapy.ICanOutputReports)
            file_path (str)
        '''

        file_path = str(file_path)
        ICanOutputReportsExtensions.TYPE.OutputActiveReportAsTextTo(can_output.wrapped if can_output else None, file_path if file_path else None)

    @staticmethod
    def get_active_report_with_encoded_images(can_output: '_6491.ICanOutputReports') -> 'str':
        ''' 'GetActiveReportWithEncodedImages' is the original name of this method.

        Args:
            can_output (mastapy.ICanOutputReports)

        Returns:
            str
        '''

        method_result = ICanOutputReportsExtensions.TYPE.GetActiveReportWithEncodedImages(can_output.wrapped if can_output else None)
        return method_result

    @staticmethod
    def output_named_report_to(can_output: '_6491.ICanOutputReports', report_name: 'str', file_path: 'str'):
        ''' 'OutputNamedReportTo' is the original name of this method.

        Args:
            can_output (mastapy.ICanOutputReports)
            report_name (str)
            file_path (str)
        '''

        report_name = str(report_name)
        file_path = str(file_path)
        ICanOutputReportsExtensions.TYPE.OutputNamedReportTo(can_output.wrapped if can_output else None, report_name if report_name else None, file_path if file_path else None)

    @staticmethod
    def report_names(can_output: '_6491.ICanOutputReports') -> 'List[str]':
        ''' 'ReportNames' is the original name of this method.

        Args:
            can_output (mastapy.ICanOutputReports)

        Returns:
            List[str]
        '''

        method_result = ICanOutputReportsExtensions.TYPE.ReportNames(can_output.wrapped if can_output else None)
        return method_result

    @staticmethod
    def output_named_report_as_text_to(can_output: '_6491.ICanOutputReports', report_name: 'str', file_path: 'str'):
        ''' 'OutputNamedReportAsTextTo' is the original name of this method.

        Args:
            can_output (mastapy.ICanOutputReports)
            report_name (str)
            file_path (str)
        '''

        report_name = str(report_name)
        file_path = str(file_path)
        ICanOutputReportsExtensions.TYPE.OutputNamedReportAsTextTo(can_output.wrapped if can_output else None, report_name if report_name else None, file_path if file_path else None)

    @staticmethod
    def get_named_report_with_encoded_images(can_output: '_6491.ICanOutputReports', report_name: 'str') -> 'str':
        ''' 'GetNamedReportWithEncodedImages' is the original name of this method.

        Args:
            can_output (mastapy.ICanOutputReports)
            report_name (str)

        Returns:
            str
        '''

        report_name = str(report_name)
        method_result = ICanOutputReportsExtensions.TYPE.GetNamedReportWithEncodedImages(can_output.wrapped if can_output else None, report_name if report_name else None)
        return method_result
