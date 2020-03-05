'''_2033.py

BevelDifferentialGearSet
'''


from typing import List

from mastapy.gears.gear_designs.bevel import _907
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.zerol_bevel import _710
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.straight_bevel_diff import _719
from mastapy.gears.gear_designs.straight_bevel import _723
from mastapy.gears.gear_designs.spiral_bevel import _727
from mastapy.system_model.part_model.gears import _2036, _2037
from mastapy.system_model.connections_and_sockets.gears import _1843
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'BevelDifferentialGearSet')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearSet',)


class BevelDifferentialGearSet(_2037.BevelGearSet):
    '''BevelDifferentialGearSet

    This is a mastapy class.
    '''

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearSet.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def conical_gear_set_design(self) -> '_907.BevelGearSetDesign':
        '''BevelGearSetDesign: 'ConicalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_907.BevelGearSetDesign)(self.wrapped.ConicalGearSetDesign) if self.wrapped.ConicalGearSetDesign else None

    @property
    def conical_gear_set_design_of_type_zerol_bevel_gear_set_design(self) -> '_710.ZerolBevelGearSetDesign':
        '''ZerolBevelGearSetDesign: 'ConicalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _710.ZerolBevelGearSetDesign.TYPE not in self.wrapped.ConicalGearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_set_design to ZerolBevelGearSetDesign. Expected: {}.'.format(self.wrapped.ConicalGearSetDesign.__class__.__qualname__))

        return constructor.new(_710.ZerolBevelGearSetDesign)(self.wrapped.ConicalGearSetDesign) if self.wrapped.ConicalGearSetDesign else None

    @property
    def conical_gear_set_design_of_type_straight_bevel_diff_gear_set_design(self) -> '_719.StraightBevelDiffGearSetDesign':
        '''StraightBevelDiffGearSetDesign: 'ConicalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _719.StraightBevelDiffGearSetDesign.TYPE not in self.wrapped.ConicalGearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_set_design to StraightBevelDiffGearSetDesign. Expected: {}.'.format(self.wrapped.ConicalGearSetDesign.__class__.__qualname__))

        return constructor.new(_719.StraightBevelDiffGearSetDesign)(self.wrapped.ConicalGearSetDesign) if self.wrapped.ConicalGearSetDesign else None

    @property
    def conical_gear_set_design_of_type_straight_bevel_gear_set_design(self) -> '_723.StraightBevelGearSetDesign':
        '''StraightBevelGearSetDesign: 'ConicalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _723.StraightBevelGearSetDesign.TYPE not in self.wrapped.ConicalGearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_set_design to StraightBevelGearSetDesign. Expected: {}.'.format(self.wrapped.ConicalGearSetDesign.__class__.__qualname__))

        return constructor.new(_723.StraightBevelGearSetDesign)(self.wrapped.ConicalGearSetDesign) if self.wrapped.ConicalGearSetDesign else None

    @property
    def conical_gear_set_design_of_type_spiral_bevel_gear_set_design(self) -> '_727.SpiralBevelGearSetDesign':
        '''SpiralBevelGearSetDesign: 'ConicalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _727.SpiralBevelGearSetDesign.TYPE not in self.wrapped.ConicalGearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_set_design to SpiralBevelGearSetDesign. Expected: {}.'.format(self.wrapped.ConicalGearSetDesign.__class__.__qualname__))

        return constructor.new(_727.SpiralBevelGearSetDesign)(self.wrapped.ConicalGearSetDesign) if self.wrapped.ConicalGearSetDesign else None

    @property
    def bevel_gear_set_design(self) -> '_907.BevelGearSetDesign':
        '''BevelGearSetDesign: 'BevelGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_907.BevelGearSetDesign)(self.wrapped.BevelGearSetDesign) if self.wrapped.BevelGearSetDesign else None

    @property
    def bevel_gear_set_design_of_type_zerol_bevel_gear_set_design(self) -> '_710.ZerolBevelGearSetDesign':
        '''ZerolBevelGearSetDesign: 'BevelGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _710.ZerolBevelGearSetDesign.TYPE not in self.wrapped.BevelGearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast bevel_gear_set_design to ZerolBevelGearSetDesign. Expected: {}.'.format(self.wrapped.BevelGearSetDesign.__class__.__qualname__))

        return constructor.new(_710.ZerolBevelGearSetDesign)(self.wrapped.BevelGearSetDesign) if self.wrapped.BevelGearSetDesign else None

    @property
    def bevel_gear_set_design_of_type_straight_bevel_diff_gear_set_design(self) -> '_719.StraightBevelDiffGearSetDesign':
        '''StraightBevelDiffGearSetDesign: 'BevelGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _719.StraightBevelDiffGearSetDesign.TYPE not in self.wrapped.BevelGearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast bevel_gear_set_design to StraightBevelDiffGearSetDesign. Expected: {}.'.format(self.wrapped.BevelGearSetDesign.__class__.__qualname__))

        return constructor.new(_719.StraightBevelDiffGearSetDesign)(self.wrapped.BevelGearSetDesign) if self.wrapped.BevelGearSetDesign else None

    @property
    def bevel_gear_set_design_of_type_straight_bevel_gear_set_design(self) -> '_723.StraightBevelGearSetDesign':
        '''StraightBevelGearSetDesign: 'BevelGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _723.StraightBevelGearSetDesign.TYPE not in self.wrapped.BevelGearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast bevel_gear_set_design to StraightBevelGearSetDesign. Expected: {}.'.format(self.wrapped.BevelGearSetDesign.__class__.__qualname__))

        return constructor.new(_723.StraightBevelGearSetDesign)(self.wrapped.BevelGearSetDesign) if self.wrapped.BevelGearSetDesign else None

    @property
    def bevel_gear_set_design_of_type_spiral_bevel_gear_set_design(self) -> '_727.SpiralBevelGearSetDesign':
        '''SpiralBevelGearSetDesign: 'BevelGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _727.SpiralBevelGearSetDesign.TYPE not in self.wrapped.BevelGearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast bevel_gear_set_design to SpiralBevelGearSetDesign. Expected: {}.'.format(self.wrapped.BevelGearSetDesign.__class__.__qualname__))

        return constructor.new(_727.SpiralBevelGearSetDesign)(self.wrapped.BevelGearSetDesign) if self.wrapped.BevelGearSetDesign else None

    @property
    def bevel_gears(self) -> 'List[_2036.BevelGear]':
        '''List[BevelGear]: 'BevelGears' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelGears, constructor.new(_2036.BevelGear))
        return value

    @property
    def bevel_meshes(self) -> 'List[_1843.BevelGearMesh]':
        '''List[BevelGearMesh]: 'BevelMeshes' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelMeshes, constructor.new(_1843.BevelGearMesh))
        return value
