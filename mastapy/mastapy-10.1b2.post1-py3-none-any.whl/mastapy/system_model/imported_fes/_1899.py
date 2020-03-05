'''_1899.py

CreateConnectedComponentOptions
'''


from typing import Callable

from mastapy._internal.implicit import enum_with_selected_value
from mastapy.system_model import _1775
from mastapy._internal import conversion, enum_with_selected_value_runtime, constructor
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_CREATE_CONNECTED_COMPONENT_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.ImportedFEs', 'CreateConnectedComponentOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('CreateConnectedComponentOptions',)


class CreateConnectedComponentOptions(_1.APIBase):
    '''CreateConnectedComponentOptions

    This is a mastapy class.
    '''

    TYPE = _CREATE_CONNECTED_COMPONENT_OPTIONS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CreateConnectedComponentOptions.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_type(self) -> 'enum_with_selected_value.EnumWithSelectedValue_DesignEntityId':
        '''enum_with_selected_value.EnumWithSelectedValue_DesignEntityId: 'ComponentType' is the original name of this property.'''

        value = enum_with_selected_value.EnumWithSelectedValue_DesignEntityId.implicit_type()
        return enum_with_selected_value_runtime.create(self.wrapped.ComponentType, value) if self.wrapped.ComponentType else None

    @component_type.setter
    def component_type(self, value: 'enum_with_selected_value.EnumWithSelectedValue_DesignEntityId.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_DesignEntityId.implicit_type().type_()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value if value else None)
        self.wrapped.ComponentType = value

    @property
    def create_component(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'CreateComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.CreateComponent
