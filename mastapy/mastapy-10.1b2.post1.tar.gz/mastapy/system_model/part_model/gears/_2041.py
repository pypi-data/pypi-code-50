'''_2041.py

ConicalGearSet
'''


from typing import List

from mastapy.gears.gear_designs.conical import _881
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.zerol_bevel import _710
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.straight_bevel_diff import _719
from mastapy.gears.gear_designs.straight_bevel import _723
from mastapy.gears.gear_designs.spiral_bevel import _727
from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _731
from mastapy.gears.gear_designs.klingelnberg_hypoid import _735
from mastapy.gears.gear_designs.klingelnberg_conical import _739
from mastapy.gears.gear_designs.hypoid import _743
from mastapy.gears.gear_designs.bevel import _907
from mastapy.gears.gear_designs.agma_gleason_conical import _920
from mastapy.system_model.part_model.gears import _2040, _2049
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ConicalGearSet')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearSet',)


class ConicalGearSet(_2049.GearSet):
    '''ConicalGearSet

    This is a mastapy class.
    '''

    TYPE = _CONICAL_GEAR_SET

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConicalGearSet.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def active_gear_set_design(self) -> '_881.ConicalGearSetDesign':
        '''ConicalGearSetDesign: 'ActiveGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_881.ConicalGearSetDesign)(self.wrapped.ActiveGearSetDesign) if self.wrapped.ActiveGearSetDesign else None

    @property
    def active_gear_set_design_of_type_zerol_bevel_gear_set_design(self) -> '_710.ZerolBevelGearSetDesign':
        '''ZerolBevelGearSetDesign: 'ActiveGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _710.ZerolBevelGearSetDesign.TYPE not in self.wrapped.ActiveGearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_set_design to ZerolBevelGearSetDesign. Expected: {}.'.format(self.wrapped.ActiveGearSetDesign.__class__.__qualname__))

        return constructor.new(_710.ZerolBevelGearSetDesign)(self.wrapped.ActiveGearSetDesign) if self.wrapped.ActiveGearSetDesign else None

    @property
    def active_gear_set_design_of_type_straight_bevel_diff_gear_set_design(self) -> '_719.StraightBevelDiffGearSetDesign':
        '''StraightBevelDiffGearSetDesign: 'ActiveGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _719.StraightBevelDiffGearSetDesign.TYPE not in self.wrapped.ActiveGearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_set_design to StraightBevelDiffGearSetDesign. Expected: {}.'.format(self.wrapped.ActiveGearSetDesign.__class__.__qualname__))

        return constructor.new(_719.StraightBevelDiffGearSetDesign)(self.wrapped.ActiveGearSetDesign) if self.wrapped.ActiveGearSetDesign else None

    @property
    def active_gear_set_design_of_type_straight_bevel_gear_set_design(self) -> '_723.StraightBevelGearSetDesign':
        '''StraightBevelGearSetDesign: 'ActiveGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _723.StraightBevelGearSetDesign.TYPE not in self.wrapped.ActiveGearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_set_design to StraightBevelGearSetDesign. Expected: {}.'.format(self.wrapped.ActiveGearSetDesign.__class__.__qualname__))

        return constructor.new(_723.StraightBevelGearSetDesign)(self.wrapped.ActiveGearSetDesign) if self.wrapped.ActiveGearSetDesign else None

    @property
    def active_gear_set_design_of_type_spiral_bevel_gear_set_design(self) -> '_727.SpiralBevelGearSetDesign':
        '''SpiralBevelGearSetDesign: 'ActiveGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _727.SpiralBevelGearSetDesign.TYPE not in self.wrapped.ActiveGearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_set_design to SpiralBevelGearSetDesign. Expected: {}.'.format(self.wrapped.ActiveGearSetDesign.__class__.__qualname__))

        return constructor.new(_727.SpiralBevelGearSetDesign)(self.wrapped.ActiveGearSetDesign) if self.wrapped.ActiveGearSetDesign else None

    @property
    def active_gear_set_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_design(self) -> '_731.KlingelnbergCycloPalloidSpiralBevelGearSetDesign':
        '''KlingelnbergCycloPalloidSpiralBevelGearSetDesign: 'ActiveGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _731.KlingelnbergCycloPalloidSpiralBevelGearSetDesign.TYPE not in self.wrapped.ActiveGearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_set_design to KlingelnbergCycloPalloidSpiralBevelGearSetDesign. Expected: {}.'.format(self.wrapped.ActiveGearSetDesign.__class__.__qualname__))

        return constructor.new(_731.KlingelnbergCycloPalloidSpiralBevelGearSetDesign)(self.wrapped.ActiveGearSetDesign) if self.wrapped.ActiveGearSetDesign else None

    @property
    def active_gear_set_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set_design(self) -> '_735.KlingelnbergCycloPalloidHypoidGearSetDesign':
        '''KlingelnbergCycloPalloidHypoidGearSetDesign: 'ActiveGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _735.KlingelnbergCycloPalloidHypoidGearSetDesign.TYPE not in self.wrapped.ActiveGearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_set_design to KlingelnbergCycloPalloidHypoidGearSetDesign. Expected: {}.'.format(self.wrapped.ActiveGearSetDesign.__class__.__qualname__))

        return constructor.new(_735.KlingelnbergCycloPalloidHypoidGearSetDesign)(self.wrapped.ActiveGearSetDesign) if self.wrapped.ActiveGearSetDesign else None

    @property
    def active_gear_set_design_of_type_klingelnberg_conical_gear_set_design(self) -> '_739.KlingelnbergConicalGearSetDesign':
        '''KlingelnbergConicalGearSetDesign: 'ActiveGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _739.KlingelnbergConicalGearSetDesign.TYPE not in self.wrapped.ActiveGearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_set_design to KlingelnbergConicalGearSetDesign. Expected: {}.'.format(self.wrapped.ActiveGearSetDesign.__class__.__qualname__))

        return constructor.new(_739.KlingelnbergConicalGearSetDesign)(self.wrapped.ActiveGearSetDesign) if self.wrapped.ActiveGearSetDesign else None

    @property
    def active_gear_set_design_of_type_hypoid_gear_set_design(self) -> '_743.HypoidGearSetDesign':
        '''HypoidGearSetDesign: 'ActiveGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _743.HypoidGearSetDesign.TYPE not in self.wrapped.ActiveGearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_set_design to HypoidGearSetDesign. Expected: {}.'.format(self.wrapped.ActiveGearSetDesign.__class__.__qualname__))

        return constructor.new(_743.HypoidGearSetDesign)(self.wrapped.ActiveGearSetDesign) if self.wrapped.ActiveGearSetDesign else None

    @property
    def active_gear_set_design_of_type_bevel_gear_set_design(self) -> '_907.BevelGearSetDesign':
        '''BevelGearSetDesign: 'ActiveGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _907.BevelGearSetDesign.TYPE not in self.wrapped.ActiveGearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_set_design to BevelGearSetDesign. Expected: {}.'.format(self.wrapped.ActiveGearSetDesign.__class__.__qualname__))

        return constructor.new(_907.BevelGearSetDesign)(self.wrapped.ActiveGearSetDesign) if self.wrapped.ActiveGearSetDesign else None

    @property
    def active_gear_set_design_of_type_agma_gleason_conical_gear_set_design(self) -> '_920.AGMAGleasonConicalGearSetDesign':
        '''AGMAGleasonConicalGearSetDesign: 'ActiveGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _920.AGMAGleasonConicalGearSetDesign.TYPE not in self.wrapped.ActiveGearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_set_design to AGMAGleasonConicalGearSetDesign. Expected: {}.'.format(self.wrapped.ActiveGearSetDesign.__class__.__qualname__))

        return constructor.new(_920.AGMAGleasonConicalGearSetDesign)(self.wrapped.ActiveGearSetDesign) if self.wrapped.ActiveGearSetDesign else None

    @property
    def conical_gear_set_design(self) -> '_881.ConicalGearSetDesign':
        '''ConicalGearSetDesign: 'ConicalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_881.ConicalGearSetDesign)(self.wrapped.ConicalGearSetDesign) if self.wrapped.ConicalGearSetDesign else None

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
    def conical_gear_set_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_design(self) -> '_731.KlingelnbergCycloPalloidSpiralBevelGearSetDesign':
        '''KlingelnbergCycloPalloidSpiralBevelGearSetDesign: 'ConicalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _731.KlingelnbergCycloPalloidSpiralBevelGearSetDesign.TYPE not in self.wrapped.ConicalGearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_set_design to KlingelnbergCycloPalloidSpiralBevelGearSetDesign. Expected: {}.'.format(self.wrapped.ConicalGearSetDesign.__class__.__qualname__))

        return constructor.new(_731.KlingelnbergCycloPalloidSpiralBevelGearSetDesign)(self.wrapped.ConicalGearSetDesign) if self.wrapped.ConicalGearSetDesign else None

    @property
    def conical_gear_set_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set_design(self) -> '_735.KlingelnbergCycloPalloidHypoidGearSetDesign':
        '''KlingelnbergCycloPalloidHypoidGearSetDesign: 'ConicalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _735.KlingelnbergCycloPalloidHypoidGearSetDesign.TYPE not in self.wrapped.ConicalGearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_set_design to KlingelnbergCycloPalloidHypoidGearSetDesign. Expected: {}.'.format(self.wrapped.ConicalGearSetDesign.__class__.__qualname__))

        return constructor.new(_735.KlingelnbergCycloPalloidHypoidGearSetDesign)(self.wrapped.ConicalGearSetDesign) if self.wrapped.ConicalGearSetDesign else None

    @property
    def conical_gear_set_design_of_type_klingelnberg_conical_gear_set_design(self) -> '_739.KlingelnbergConicalGearSetDesign':
        '''KlingelnbergConicalGearSetDesign: 'ConicalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _739.KlingelnbergConicalGearSetDesign.TYPE not in self.wrapped.ConicalGearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_set_design to KlingelnbergConicalGearSetDesign. Expected: {}.'.format(self.wrapped.ConicalGearSetDesign.__class__.__qualname__))

        return constructor.new(_739.KlingelnbergConicalGearSetDesign)(self.wrapped.ConicalGearSetDesign) if self.wrapped.ConicalGearSetDesign else None

    @property
    def conical_gear_set_design_of_type_hypoid_gear_set_design(self) -> '_743.HypoidGearSetDesign':
        '''HypoidGearSetDesign: 'ConicalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _743.HypoidGearSetDesign.TYPE not in self.wrapped.ConicalGearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_set_design to HypoidGearSetDesign. Expected: {}.'.format(self.wrapped.ConicalGearSetDesign.__class__.__qualname__))

        return constructor.new(_743.HypoidGearSetDesign)(self.wrapped.ConicalGearSetDesign) if self.wrapped.ConicalGearSetDesign else None

    @property
    def conical_gear_set_design_of_type_bevel_gear_set_design(self) -> '_907.BevelGearSetDesign':
        '''BevelGearSetDesign: 'ConicalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _907.BevelGearSetDesign.TYPE not in self.wrapped.ConicalGearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_set_design to BevelGearSetDesign. Expected: {}.'.format(self.wrapped.ConicalGearSetDesign.__class__.__qualname__))

        return constructor.new(_907.BevelGearSetDesign)(self.wrapped.ConicalGearSetDesign) if self.wrapped.ConicalGearSetDesign else None

    @property
    def conical_gear_set_design_of_type_agma_gleason_conical_gear_set_design(self) -> '_920.AGMAGleasonConicalGearSetDesign':
        '''AGMAGleasonConicalGearSetDesign: 'ConicalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _920.AGMAGleasonConicalGearSetDesign.TYPE not in self.wrapped.ConicalGearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_set_design to AGMAGleasonConicalGearSetDesign. Expected: {}.'.format(self.wrapped.ConicalGearSetDesign.__class__.__qualname__))

        return constructor.new(_920.AGMAGleasonConicalGearSetDesign)(self.wrapped.ConicalGearSetDesign) if self.wrapped.ConicalGearSetDesign else None

    @property
    def conical_gears(self) -> 'List[_2040.ConicalGear]':
        '''List[ConicalGear]: 'ConicalGears' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConicalGears, constructor.new(_2040.ConicalGear))
        return value
