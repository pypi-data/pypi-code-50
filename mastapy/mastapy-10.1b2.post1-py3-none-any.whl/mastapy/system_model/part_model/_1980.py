'''_1980.py

InternalClearanceTolerance
'''


from mastapy._internal.implicit import enum_with_selected_value
from mastapy.bearings.tolerances import _1514, _1512
from mastapy._internal import conversion, enum_with_selected_value_runtime, constructor
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_INTERNAL_CLEARANCE_TOLERANCE = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'InternalClearanceTolerance')


__docformat__ = 'restructuredtext en'
__all__ = ('InternalClearanceTolerance',)


class InternalClearanceTolerance(_1.APIBase):
    '''InternalClearanceTolerance

    This is a mastapy class.
    '''

    TYPE = _INTERNAL_CLEARANCE_TOLERANCE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'InternalClearanceTolerance.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def definition_option(self) -> 'enum_with_selected_value.EnumWithSelectedValue_BearingToleranceDefinitionOptions':
        '''enum_with_selected_value.EnumWithSelectedValue_BearingToleranceDefinitionOptions: 'DefinitionOption' is the original name of this property.'''

        value = enum_with_selected_value.EnumWithSelectedValue_BearingToleranceDefinitionOptions.implicit_type()
        return enum_with_selected_value_runtime.create(self.wrapped.DefinitionOption, value) if self.wrapped.DefinitionOption else None

    @definition_option.setter
    def definition_option(self, value: 'enum_with_selected_value.EnumWithSelectedValue_BearingToleranceDefinitionOptions.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_BearingToleranceDefinitionOptions.implicit_type().type_()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value if value else None)
        self.wrapped.DefinitionOption = value

    @property
    def clearance_class(self) -> 'enum_with_selected_value.EnumWithSelectedValue_InternalClearanceClass':
        '''enum_with_selected_value.EnumWithSelectedValue_InternalClearanceClass: 'ClearanceClass' is the original name of this property.'''

        value = enum_with_selected_value.EnumWithSelectedValue_InternalClearanceClass.implicit_type()
        return enum_with_selected_value_runtime.create(self.wrapped.ClearanceClass, value) if self.wrapped.ClearanceClass else None

    @clearance_class.setter
    def clearance_class(self, value: 'enum_with_selected_value.EnumWithSelectedValue_InternalClearanceClass.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_InternalClearanceClass.implicit_type().type_()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value if value else None)
        self.wrapped.ClearanceClass = value

    @property
    def minimum(self) -> 'float':
        '''float: 'Minimum' is the original name of this property.'''

        return self.wrapped.Minimum

    @minimum.setter
    def minimum(self, value: 'float'):
        self.wrapped.Minimum = float(value) if value else 0.0

    @property
    def maximum(self) -> 'float':
        '''float: 'Maximum' is the original name of this property.'''

        return self.wrapped.Maximum

    @maximum.setter
    def maximum(self, value: 'float'):
        self.wrapped.Maximum = float(value) if value else 0.0
