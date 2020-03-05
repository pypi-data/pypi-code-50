'''_1950.py

ConcentricPartGroup
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.math_utility.measured_vectors import _1169
from mastapy.utility.units_and_measurements.measurements import _1312
from mastapy.system_model.part_model.part_groups import _1951, _1949
from mastapy._internal.python_net import python_net_import

_CONCENTRIC_PART_GROUP = python_net_import('SMT.MastaAPI.SystemModel.PartModel.PartGroups', 'ConcentricPartGroup')


__docformat__ = 'restructuredtext en'
__all__ = ('ConcentricPartGroup',)


class ConcentricPartGroup(_1949.ConcentricOrParallelPartGroup):
    '''ConcentricPartGroup

    This is a mastapy class.
    '''

    TYPE = _CONCENTRIC_PART_GROUP

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConcentricPartGroup.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def total_of_cylindrical_gear_face_widths(self) -> 'float':
        '''float: 'TotalOfCylindricalGearFaceWidths' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TotalOfCylindricalGearFaceWidths

    @property
    def radial_position(self) -> '_1169.Vector2D[_1312.LengthShort]':
        '''Vector2D[LengthShort]: 'RadialPosition' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1169.Vector2D)[_1312.LengthShort](self.wrapped.RadialPosition) if self.wrapped.RadialPosition else None

    @property
    def parallel_groups(self) -> 'List[_1951.ConcentricPartGroupParallelToThis]':
        '''List[ConcentricPartGroupParallelToThis]: 'ParallelGroups' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ParallelGroups, constructor.new(_1951.ConcentricPartGroupParallelToThis))
        return value
