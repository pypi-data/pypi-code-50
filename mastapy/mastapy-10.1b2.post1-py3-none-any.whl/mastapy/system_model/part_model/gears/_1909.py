'''_1909.py

StraightBevelDiffGearSet
'''


from typing import List

from mastapy.gears.gear_designs.straight_bevel_diff import _376
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _1908, _1885
from mastapy.system_model.connections_and_sockets.gears import _1818
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'StraightBevelDiffGearSet')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearSet',)


class StraightBevelDiffGearSet(_1885.BevelGearSet):
    '''StraightBevelDiffGearSet

    This is a mastapy class.
    '''

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET
    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearSet.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def conical_gear_set_design(self) -> '_376.StraightBevelDiffGearSetDesign':
        '''StraightBevelDiffGearSetDesign: 'ConicalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_376.StraightBevelDiffGearSetDesign)(self.wrapped.ConicalGearSetDesign) if self.wrapped.ConicalGearSetDesign else None

    @property
    def straight_bevel_diff_gear_set_design(self) -> '_376.StraightBevelDiffGearSetDesign':
        '''StraightBevelDiffGearSetDesign: 'StraightBevelDiffGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_376.StraightBevelDiffGearSetDesign)(self.wrapped.StraightBevelDiffGearSetDesign) if self.wrapped.StraightBevelDiffGearSetDesign else None

    @property
    def straight_bevel_diff_gears(self) -> 'List[_1908.StraightBevelDiffGear]':
        '''List[StraightBevelDiffGear]: 'StraightBevelDiffGears' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGears, constructor.new(_1908.StraightBevelDiffGear))
        return value

    @property
    def straight_bevel_diff_meshes(self) -> 'List[_1818.StraightBevelDiffGearMesh]':
        '''List[StraightBevelDiffGearMesh]: 'StraightBevelDiffMeshes' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffMeshes, constructor.new(_1818.StraightBevelDiffGearMesh))
        return value
