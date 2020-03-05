'''_1887.py

AlignConnectedComponentOptions
'''


from typing import Callable

from mastapy._internal import constructor, conversion, enum_with_selected_value_runtime
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.system_model.imported_fes import _1897
from mastapy.math_utility import _1051, _1050
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_ALIGN_CONNECTED_COMPONENT_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.ImportedFEs', 'AlignConnectedComponentOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('AlignConnectedComponentOptions',)


class AlignConnectedComponentOptions(_1.APIBase):
    '''AlignConnectedComponentOptions

    This is a mastapy class.
    '''

    TYPE = _ALIGN_CONNECTED_COMPONENT_OPTIONS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AlignConnectedComponentOptions.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def align_component(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'AlignComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AlignComponent

    @property
    def component_orientation(self) -> 'enum_with_selected_value.EnumWithSelectedValue_ComponentOrientationOption':
        '''enum_with_selected_value.EnumWithSelectedValue_ComponentOrientationOption: 'ComponentOrientation' is the original name of this property.'''

        value = enum_with_selected_value.EnumWithSelectedValue_ComponentOrientationOption.implicit_type()
        return enum_with_selected_value_runtime.create(self.wrapped.ComponentOrientation, value) if self.wrapped.ComponentOrientation else None

    @component_orientation.setter
    def component_orientation(self, value: 'enum_with_selected_value.EnumWithSelectedValue_ComponentOrientationOption.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_ComponentOrientationOption.implicit_type().type_()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value if value else None)
        self.wrapped.ComponentOrientation = value

    @property
    def first_component_alignment_axis(self) -> '_1051.Axis':
        '''Axis: 'FirstComponentAlignmentAxis' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.FirstComponentAlignmentAxis)
        return constructor.new(_1051.Axis)(value) if value else None

    @first_component_alignment_axis.setter
    def first_component_alignment_axis(self, value: '_1051.Axis'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.FirstComponentAlignmentAxis = value

    @property
    def second_component_alignment_axis(self) -> 'enum_with_selected_value.EnumWithSelectedValue_Axis':
        '''enum_with_selected_value.EnumWithSelectedValue_Axis: 'SecondComponentAlignmentAxis' is the original name of this property.'''

        value = enum_with_selected_value.EnumWithSelectedValue_Axis.implicit_type()
        return enum_with_selected_value_runtime.create(self.wrapped.SecondComponentAlignmentAxis, value) if self.wrapped.SecondComponentAlignmentAxis else None

    @second_component_alignment_axis.setter
    def second_component_alignment_axis(self, value: 'enum_with_selected_value.EnumWithSelectedValue_Axis.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_Axis.implicit_type().type_()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value if value else None)
        self.wrapped.SecondComponentAlignmentAxis = value

    @property
    def first_fe_alignment_axis(self) -> '_1050.AlignmentAxis':
        '''AlignmentAxis: 'FirstFEAlignmentAxis' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.FirstFEAlignmentAxis)
        return constructor.new(_1050.AlignmentAxis)(value) if value else None

    @first_fe_alignment_axis.setter
    def first_fe_alignment_axis(self, value: '_1050.AlignmentAxis'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.FirstFEAlignmentAxis = value

    @property
    def second_fe_alignment_axis(self) -> 'enum_with_selected_value.EnumWithSelectedValue_AlignmentAxis':
        '''enum_with_selected_value.EnumWithSelectedValue_AlignmentAxis: 'SecondFEAlignmentAxis' is the original name of this property.'''

        value = enum_with_selected_value.EnumWithSelectedValue_AlignmentAxis.implicit_type()
        return enum_with_selected_value_runtime.create(self.wrapped.SecondFEAlignmentAxis, value) if self.wrapped.SecondFEAlignmentAxis else None

    @second_fe_alignment_axis.setter
    def second_fe_alignment_axis(self, value: 'enum_with_selected_value.EnumWithSelectedValue_AlignmentAxis.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_AlignmentAxis.implicit_type().type_()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value if value else None)
        self.wrapped.SecondFEAlignmentAxis = value

    @property
    def component_direction_normal_to_surface(self) -> '_1051.Axis':
        '''Axis: 'ComponentDirectionNormalToSurface' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.ComponentDirectionNormalToSurface)
        return constructor.new(_1051.Axis)(value) if value else None

    @component_direction_normal_to_surface.setter
    def component_direction_normal_to_surface(self, value: '_1051.Axis'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.ComponentDirectionNormalToSurface = value

    @property
    def perpendicular_component_alignment_axis(self) -> 'enum_with_selected_value.EnumWithSelectedValue_Axis':
        '''enum_with_selected_value.EnumWithSelectedValue_Axis: 'PerpendicularComponentAlignmentAxis' is the original name of this property.'''

        value = enum_with_selected_value.EnumWithSelectedValue_Axis.implicit_type()
        return enum_with_selected_value_runtime.create(self.wrapped.PerpendicularComponentAlignmentAxis, value) if self.wrapped.PerpendicularComponentAlignmentAxis else None

    @perpendicular_component_alignment_axis.setter
    def perpendicular_component_alignment_axis(self, value: 'enum_with_selected_value.EnumWithSelectedValue_Axis.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_Axis.implicit_type().type_()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value if value else None)
        self.wrapped.PerpendicularComponentAlignmentAxis = value

    @property
    def fe_axis_approximately_in_perpendicular_direction(self) -> '_1050.AlignmentAxis':
        '''AlignmentAxis: 'FEAxisApproximatelyInPerpendicularDirection' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.FEAxisApproximatelyInPerpendicularDirection)
        return constructor.new(_1050.AlignmentAxis)(value) if value else None

    @fe_axis_approximately_in_perpendicular_direction.setter
    def fe_axis_approximately_in_perpendicular_direction(self, value: '_1050.AlignmentAxis'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.FEAxisApproximatelyInPerpendicularDirection = value
