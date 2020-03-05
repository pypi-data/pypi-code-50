'''_1787.py

RelativeComponentAlignment
'''


from typing import Generic, TypeVar

from mastapy.math_utility import _1050
from mastapy._internal import constructor, conversion
from mastapy.system_model import _1788
from mastapy import _1
from mastapy.system_model.part_model import _1967
from mastapy._internal.python_net import python_net_import

_RELATIVE_COMPONENT_ALIGNMENT = python_net_import('SMT.MastaAPI.SystemModel', 'RelativeComponentAlignment')


__docformat__ = 'restructuredtext en'
__all__ = ('RelativeComponentAlignment',)


T = TypeVar('T', bound='_1967.Component')


class RelativeComponentAlignment(_1.APIBase, Generic[T]):
    '''RelativeComponentAlignment

    This is a mastapy class.

    Generic Types:
        T
    '''

    TYPE = _RELATIVE_COMPONENT_ALIGNMENT

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RelativeComponentAlignment.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def alignment_axis(self) -> '_1050.AlignmentAxis':
        '''AlignmentAxis: 'AlignmentAxis' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.AlignmentAxis)
        return constructor.new(_1050.AlignmentAxis)(value) if value else None

    @alignment_axis.setter
    def alignment_axis(self, value: '_1050.AlignmentAxis'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.AlignmentAxis = value

    @property
    def axial_offset(self) -> '_1788.RelativeOffsetOption':
        '''RelativeOffsetOption: 'AxialOffset' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.AxialOffset)
        return constructor.new(_1788.RelativeOffsetOption)(value) if value else None

    @axial_offset.setter
    def axial_offset(self, value: '_1788.RelativeOffsetOption'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.AxialOffset = value

    @property
    def specified_offset(self) -> 'float':
        '''float: 'SpecifiedOffset' is the original name of this property.'''

        return self.wrapped.SpecifiedOffset

    @specified_offset.setter
    def specified_offset(self, value: 'float'):
        self.wrapped.SpecifiedOffset = float(value) if value else 0.0

    @property
    def rotation_angle(self) -> 'float':
        '''float: 'RotationAngle' is the original name of this property.'''

        return self.wrapped.RotationAngle

    @rotation_angle.setter
    def rotation_angle(self, value: 'float'):
        self.wrapped.RotationAngle = float(value) if value else 0.0
