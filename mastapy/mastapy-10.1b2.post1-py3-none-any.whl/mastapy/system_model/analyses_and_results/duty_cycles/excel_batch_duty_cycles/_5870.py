'''_5870.py

ExcelBatchDutyCycleSpectraCreatorDetails
'''


from typing import Callable, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.duty_cycles.excel_batch_duty_cycles import _5874, _5871, _5873
from mastapy.utility import _1253
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_EXCEL_BATCH_DUTY_CYCLE_SPECTRA_CREATOR_DETAILS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DutyCycles.ExcelBatchDutyCycles', 'ExcelBatchDutyCycleSpectraCreatorDetails')


__docformat__ = 'restructuredtext en'
__all__ = ('ExcelBatchDutyCycleSpectraCreatorDetails',)


class ExcelBatchDutyCycleSpectraCreatorDetails(_1.APIBase):
    '''ExcelBatchDutyCycleSpectraCreatorDetails

    This is a mastapy class.
    '''

    TYPE = _EXCEL_BATCH_DUTY_CYCLE_SPECTRA_CREATOR_DETAILS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ExcelBatchDutyCycleSpectraCreatorDetails.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def folder(self) -> 'str':
        '''str: 'Folder' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.Folder

    @property
    def edit_folder_path(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'EditFolderPath' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.EditFolderPath

    @property
    def excel_files_found(self) -> 'int':
        '''int: 'ExcelFilesFound' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ExcelFilesFound

    @property
    def write_masta_files(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'WriteMASTAFiles' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.WriteMASTAFiles

    @property
    def prepare_working_folder(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'PrepareWorkingFolder' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PrepareWorkingFolder

    @property
    def masta_file_details(self) -> '_5874.MASTAFileDetails':
        '''MASTAFileDetails: 'MASTAFileDetails' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5874.MASTAFileDetails)(self.wrapped.MASTAFileDetails) if self.wrapped.MASTAFileDetails else None

    @property
    def excel_file_details(self) -> '_5871.ExcelFileDetails':
        '''ExcelFileDetails: 'ExcelFileDetails' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5871.ExcelFileDetails)(self.wrapped.ExcelFileDetails) if self.wrapped.ExcelFileDetails else None

    @property
    def working_folder(self) -> '_1253.SelectableFolder':
        '''SelectableFolder: 'WorkingFolder' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1253.SelectableFolder)(self.wrapped.WorkingFolder) if self.wrapped.WorkingFolder else None

    @property
    def excel_sheet_design_state_selection(self) -> 'List[_5873.ExcelSheetDesignStateSelector]':
        '''List[ExcelSheetDesignStateSelector]: 'ExcelSheetDesignStateSelection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ExcelSheetDesignStateSelection, constructor.new(_5873.ExcelSheetDesignStateSelector))
        return value
