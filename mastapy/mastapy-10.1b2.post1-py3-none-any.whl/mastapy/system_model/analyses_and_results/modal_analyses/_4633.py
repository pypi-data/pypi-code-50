'''_4633.py

ModalAnalysisBarModelFEExportOptions
'''


from typing import Callable

from mastapy._internal.implicit import enum_with_selected_value, list_with_selected_item
from mastapy.nodal_analysis.fe_export_utility import _139
from mastapy._internal import conversion, enum_with_selected_value_runtime, constructor
from mastapy.nodal_analysis import _49, _48
from mastapy.utility.units_and_measurements import _1264
from mastapy.system_model.part_model import _1926
from mastapy.nodal_analysis.dev_tools_analyses import _141
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_MODAL_ANALYSIS_BAR_MODEL_FE_EXPORT_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'ModalAnalysisBarModelFEExportOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('ModalAnalysisBarModelFEExportOptions',)


class ModalAnalysisBarModelFEExportOptions(_1.APIBase):
    '''ModalAnalysisBarModelFEExportOptions

    This is a mastapy class.
    '''

    TYPE = _MODAL_ANALYSIS_BAR_MODEL_FE_EXPORT_OPTIONS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ModalAnalysisBarModelFEExportOptions.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def fe_package(self) -> 'enum_with_selected_value.EnumWithSelectedValue_FEExportFormat':
        '''enum_with_selected_value.EnumWithSelectedValue_FEExportFormat: 'FEPackage' is the original name of this property.'''

        value = enum_with_selected_value.EnumWithSelectedValue_FEExportFormat.implicit_type()
        return enum_with_selected_value_runtime.create(self.wrapped.FEPackage, value) if self.wrapped.FEPackage else None

    @fe_package.setter
    def fe_package(self, value: 'enum_with_selected_value.EnumWithSelectedValue_FEExportFormat.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_FEExportFormat.implicit_type().type_()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value if value else None)
        self.wrapped.FEPackage = value

    @property
    def shaft_export_type(self) -> 'enum_with_selected_value.EnumWithSelectedValue_BarModelExportType':
        '''enum_with_selected_value.EnumWithSelectedValue_BarModelExportType: 'ShaftExportType' is the original name of this property.'''

        value = enum_with_selected_value.EnumWithSelectedValue_BarModelExportType.implicit_type()
        return enum_with_selected_value_runtime.create(self.wrapped.ShaftExportType, value) if self.wrapped.ShaftExportType else None

    @shaft_export_type.setter
    def shaft_export_type(self, value: 'enum_with_selected_value.EnumWithSelectedValue_BarModelExportType.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_BarModelExportType.implicit_type().type_()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value if value else None)
        self.wrapped.ShaftExportType = value

    @property
    def analysis_type(self) -> '_48.BarModelAnalysisType':
        '''BarModelAnalysisType: 'AnalysisType' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.AnalysisType)
        return constructor.new(_48.BarModelAnalysisType)(value) if value else None

    @analysis_type.setter
    def analysis_type(self, value: '_48.BarModelAnalysisType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.AnalysisType = value

    @property
    def length_unit(self) -> 'list_with_selected_item.ListWithSelectedItem_Unit':
        '''list_with_selected_item.ListWithSelectedItem_Unit: 'LengthUnit' is the original name of this property.'''

        return constructor.new(list_with_selected_item.ListWithSelectedItem_Unit)(self.wrapped.LengthUnit) if self.wrapped.LengthUnit else None

    @length_unit.setter
    def length_unit(self, value: 'list_with_selected_item.ListWithSelectedItem_Unit.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_Unit.TYPE
        enclosed_type = list_with_selected_item.ListWithSelectedItem_Unit.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value else None)
        self.wrapped.LengthUnit = value

    @property
    def force_unit(self) -> 'list_with_selected_item.ListWithSelectedItem_Unit':
        '''list_with_selected_item.ListWithSelectedItem_Unit: 'ForceUnit' is the original name of this property.'''

        return constructor.new(list_with_selected_item.ListWithSelectedItem_Unit)(self.wrapped.ForceUnit) if self.wrapped.ForceUnit else None

    @force_unit.setter
    def force_unit(self, value: 'list_with_selected_item.ListWithSelectedItem_Unit.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_Unit.TYPE
        enclosed_type = list_with_selected_item.ListWithSelectedItem_Unit.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value else None)
        self.wrapped.ForceUnit = value

    @property
    def fe_component(self) -> 'list_with_selected_item.ListWithSelectedItem_ImportedFEComponent':
        '''list_with_selected_item.ListWithSelectedItem_ImportedFEComponent: 'FEComponent' is the original name of this property.'''

        return constructor.new(list_with_selected_item.ListWithSelectedItem_ImportedFEComponent)(self.wrapped.FEComponent) if self.wrapped.FEComponent else None

    @fe_component.setter
    def fe_component(self, value: 'list_with_selected_item.ListWithSelectedItem_ImportedFEComponent.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_ImportedFEComponent.TYPE
        enclosed_type = list_with_selected_item.ListWithSelectedItem_ImportedFEComponent.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value else None)
        self.wrapped.FEComponent = value

    @property
    def coordinate_system(self) -> 'list_with_selected_item.ListWithSelectedItem_ImportedFEComponent':
        '''list_with_selected_item.ListWithSelectedItem_ImportedFEComponent: 'CoordinateSystem' is the original name of this property.'''

        return constructor.new(list_with_selected_item.ListWithSelectedItem_ImportedFEComponent)(self.wrapped.CoordinateSystem) if self.wrapped.CoordinateSystem else None

    @coordinate_system.setter
    def coordinate_system(self, value: 'list_with_selected_item.ListWithSelectedItem_ImportedFEComponent.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_ImportedFEComponent.TYPE
        enclosed_type = list_with_selected_item.ListWithSelectedItem_ImportedFEComponent.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value else None)
        self.wrapped.CoordinateSystem = value

    @property
    def connect_to_full_fe_model(self) -> 'bool':
        '''bool: 'ConnectToFullFEModel' is the original name of this property.'''

        return self.wrapped.ConnectToFullFEModel

    @connect_to_full_fe_model.setter
    def connect_to_full_fe_model(self, value: 'bool'):
        self.wrapped.ConnectToFullFEModel = bool(value) if value else False

    @property
    def use_fe_file_from_imported_fe(self) -> 'bool':
        '''bool: 'UseFEFileFromImportedFE' is the original name of this property.'''

        return self.wrapped.UseFEFileFromImportedFE

    @use_fe_file_from_imported_fe.setter
    def use_fe_file_from_imported_fe(self, value: 'bool'):
        self.wrapped.UseFEFileFromImportedFE = bool(value) if value else False

    @property
    def fe_file_to_include(self) -> 'str':
        '''str: 'FEFileToInclude' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.FEFileToInclude

    @property
    def select_fe_file_to_include(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'SelectFEFileToInclude' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.SelectFEFileToInclude

    @property
    def error_message(self) -> 'str':
        '''str: 'ErrorMessage' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ErrorMessage

    @property
    def export_bar_model_to_file(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'ExportBarModelToFile' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ExportBarModelToFile

    @property
    def mode_options(self) -> '_141.EigenvalueOptions':
        '''EigenvalueOptions: 'ModeOptions' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_141.EigenvalueOptions)(self.wrapped.ModeOptions) if self.wrapped.ModeOptions else None
