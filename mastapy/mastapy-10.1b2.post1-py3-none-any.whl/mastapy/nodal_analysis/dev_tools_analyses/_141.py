'''_141.py

EigenvalueOptions
'''


from mastapy._internal.implicit import enum_with_selected_value, overridable
from mastapy.nodal_analysis import _71
from mastapy._internal import conversion, enum_with_selected_value_runtime, constructor
from mastapy.nodal_analysis.dev_tools_analyses import _159
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_EIGENVALUE_OPTIONS = python_net_import('SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses', 'EigenvalueOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('EigenvalueOptions',)


class EigenvalueOptions(_1.APIBase):
    '''EigenvalueOptions

    This is a mastapy class.
    '''

    TYPE = _EIGENVALUE_OPTIONS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'EigenvalueOptions.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def mode_input_method(self) -> 'enum_with_selected_value.EnumWithSelectedValue_ModeInputType':
        '''enum_with_selected_value.EnumWithSelectedValue_ModeInputType: 'ModeInputMethod' is the original name of this property.'''

        value = enum_with_selected_value.EnumWithSelectedValue_ModeInputType.implicit_type()
        return enum_with_selected_value_runtime.create(self.wrapped.ModeInputMethod, value) if self.wrapped.ModeInputMethod else None

    @mode_input_method.setter
    def mode_input_method(self, value: 'enum_with_selected_value.EnumWithSelectedValue_ModeInputType.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_ModeInputType.implicit_type().type_()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value if value else None)
        self.wrapped.ModeInputMethod = value

    @property
    def number_of_modes(self) -> 'int':
        '''int: 'NumberOfModes' is the original name of this property.'''

        return self.wrapped.NumberOfModes

    @number_of_modes.setter
    def number_of_modes(self, value: 'int'):
        self.wrapped.NumberOfModes = int(value) if value else 0

    @property
    def minimum_mode_frequency(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'MinimumModeFrequency' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.MinimumModeFrequency) if self.wrapped.MinimumModeFrequency else None

    @minimum_mode_frequency.setter
    def minimum_mode_frequency(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.TYPE
        enclosed_type = overridable.Overridable_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0.0)
        self.wrapped.MinimumModeFrequency = value

    @property
    def maximum_mode_frequency(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'MaximumModeFrequency' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.MaximumModeFrequency) if self.wrapped.MaximumModeFrequency else None

    @maximum_mode_frequency.setter
    def maximum_mode_frequency(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.TYPE
        enclosed_type = overridable.Overridable_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0.0)
        self.wrapped.MaximumModeFrequency = value

    @property
    def mode_frequency_shift(self) -> 'float':
        '''float: 'ModeFrequencyShift' is the original name of this property.'''

        return self.wrapped.ModeFrequencyShift

    @mode_frequency_shift.setter
    def mode_frequency_shift(self, value: 'float'):
        self.wrapped.ModeFrequencyShift = float(value) if value else 0.0

    @property
    def mass_matrix_type(self) -> '_159.MassMatrixType':
        '''MassMatrixType: 'MassMatrixType' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.MassMatrixType)
        return constructor.new(_159.MassMatrixType)(value) if value else None

    @mass_matrix_type.setter
    def mass_matrix_type(self, value: '_159.MassMatrixType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.MassMatrixType = value
