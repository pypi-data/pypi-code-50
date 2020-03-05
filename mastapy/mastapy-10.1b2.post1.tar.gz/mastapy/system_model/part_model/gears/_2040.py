'''_2040.py

ConicalGear
'''


from mastapy.system_model.part_model.gears import _2048, _2047
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.conical import _879
from mastapy.gears.gear_designs.zerol_bevel import _708
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.straight_bevel_diff import _717
from mastapy.gears.gear_designs.straight_bevel import _721
from mastapy.gears.gear_designs.spiral_bevel import _725
from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _729
from mastapy.gears.gear_designs.klingelnberg_hypoid import _733
from mastapy.gears.gear_designs.klingelnberg_conical import _737
from mastapy.gears.gear_designs.hypoid import _741
from mastapy.gears.gear_designs.bevel import _905
from mastapy.gears.gear_designs.agma_gleason_conical import _918
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ConicalGear')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGear',)


class ConicalGear(_2047.Gear):
    '''ConicalGear

    This is a mastapy class.
    '''

    TYPE = _CONICAL_GEAR

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConicalGear.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def orientation(self) -> '_2048.GearOrientations':
        '''GearOrientations: 'Orientation' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.Orientation)
        return constructor.new(_2048.GearOrientations)(value) if value else None

    @orientation.setter
    def orientation(self, value: '_2048.GearOrientations'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.Orientation = value

    @property
    def length(self) -> 'float':
        '''float: 'Length' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.Length

    @property
    def active_gear_design(self) -> '_879.ConicalGearDesign':
        '''ConicalGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_879.ConicalGearDesign)(self.wrapped.ActiveGearDesign) if self.wrapped.ActiveGearDesign else None

    @property
    def active_gear_design_of_type_zerol_bevel_gear_design(self) -> '_708.ZerolBevelGearDesign':
        '''ZerolBevelGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _708.ZerolBevelGearDesign.TYPE not in self.wrapped.ActiveGearDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to ZerolBevelGearDesign. Expected: {}.'.format(self.wrapped.ActiveGearDesign.__class__.__qualname__))

        return constructor.new(_708.ZerolBevelGearDesign)(self.wrapped.ActiveGearDesign) if self.wrapped.ActiveGearDesign else None

    @property
    def active_gear_design_of_type_straight_bevel_diff_gear_design(self) -> '_717.StraightBevelDiffGearDesign':
        '''StraightBevelDiffGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _717.StraightBevelDiffGearDesign.TYPE not in self.wrapped.ActiveGearDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to StraightBevelDiffGearDesign. Expected: {}.'.format(self.wrapped.ActiveGearDesign.__class__.__qualname__))

        return constructor.new(_717.StraightBevelDiffGearDesign)(self.wrapped.ActiveGearDesign) if self.wrapped.ActiveGearDesign else None

    @property
    def active_gear_design_of_type_straight_bevel_gear_design(self) -> '_721.StraightBevelGearDesign':
        '''StraightBevelGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _721.StraightBevelGearDesign.TYPE not in self.wrapped.ActiveGearDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to StraightBevelGearDesign. Expected: {}.'.format(self.wrapped.ActiveGearDesign.__class__.__qualname__))

        return constructor.new(_721.StraightBevelGearDesign)(self.wrapped.ActiveGearDesign) if self.wrapped.ActiveGearDesign else None

    @property
    def active_gear_design_of_type_spiral_bevel_gear_design(self) -> '_725.SpiralBevelGearDesign':
        '''SpiralBevelGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _725.SpiralBevelGearDesign.TYPE not in self.wrapped.ActiveGearDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to SpiralBevelGearDesign. Expected: {}.'.format(self.wrapped.ActiveGearDesign.__class__.__qualname__))

        return constructor.new(_725.SpiralBevelGearDesign)(self.wrapped.ActiveGearDesign) if self.wrapped.ActiveGearDesign else None

    @property
    def active_gear_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_design(self) -> '_729.KlingelnbergCycloPalloidSpiralBevelGearDesign':
        '''KlingelnbergCycloPalloidSpiralBevelGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _729.KlingelnbergCycloPalloidSpiralBevelGearDesign.TYPE not in self.wrapped.ActiveGearDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to KlingelnbergCycloPalloidSpiralBevelGearDesign. Expected: {}.'.format(self.wrapped.ActiveGearDesign.__class__.__qualname__))

        return constructor.new(_729.KlingelnbergCycloPalloidSpiralBevelGearDesign)(self.wrapped.ActiveGearDesign) if self.wrapped.ActiveGearDesign else None

    @property
    def active_gear_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear_design(self) -> '_733.KlingelnbergCycloPalloidHypoidGearDesign':
        '''KlingelnbergCycloPalloidHypoidGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _733.KlingelnbergCycloPalloidHypoidGearDesign.TYPE not in self.wrapped.ActiveGearDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to KlingelnbergCycloPalloidHypoidGearDesign. Expected: {}.'.format(self.wrapped.ActiveGearDesign.__class__.__qualname__))

        return constructor.new(_733.KlingelnbergCycloPalloidHypoidGearDesign)(self.wrapped.ActiveGearDesign) if self.wrapped.ActiveGearDesign else None

    @property
    def active_gear_design_of_type_klingelnberg_conical_gear_design(self) -> '_737.KlingelnbergConicalGearDesign':
        '''KlingelnbergConicalGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _737.KlingelnbergConicalGearDesign.TYPE not in self.wrapped.ActiveGearDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to KlingelnbergConicalGearDesign. Expected: {}.'.format(self.wrapped.ActiveGearDesign.__class__.__qualname__))

        return constructor.new(_737.KlingelnbergConicalGearDesign)(self.wrapped.ActiveGearDesign) if self.wrapped.ActiveGearDesign else None

    @property
    def active_gear_design_of_type_hypoid_gear_design(self) -> '_741.HypoidGearDesign':
        '''HypoidGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _741.HypoidGearDesign.TYPE not in self.wrapped.ActiveGearDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to HypoidGearDesign. Expected: {}.'.format(self.wrapped.ActiveGearDesign.__class__.__qualname__))

        return constructor.new(_741.HypoidGearDesign)(self.wrapped.ActiveGearDesign) if self.wrapped.ActiveGearDesign else None

    @property
    def active_gear_design_of_type_bevel_gear_design(self) -> '_905.BevelGearDesign':
        '''BevelGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _905.BevelGearDesign.TYPE not in self.wrapped.ActiveGearDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to BevelGearDesign. Expected: {}.'.format(self.wrapped.ActiveGearDesign.__class__.__qualname__))

        return constructor.new(_905.BevelGearDesign)(self.wrapped.ActiveGearDesign) if self.wrapped.ActiveGearDesign else None

    @property
    def active_gear_design_of_type_agma_gleason_conical_gear_design(self) -> '_918.AGMAGleasonConicalGearDesign':
        '''AGMAGleasonConicalGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _918.AGMAGleasonConicalGearDesign.TYPE not in self.wrapped.ActiveGearDesign.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to AGMAGleasonConicalGearDesign. Expected: {}.'.format(self.wrapped.ActiveGearDesign.__class__.__qualname__))

        return constructor.new(_918.AGMAGleasonConicalGearDesign)(self.wrapped.ActiveGearDesign) if self.wrapped.ActiveGearDesign else None

    @property
    def conical_gear_design(self) -> '_879.ConicalGearDesign':
        '''ConicalGearDesign: 'ConicalGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_879.ConicalGearDesign)(self.wrapped.ConicalGearDesign) if self.wrapped.ConicalGearDesign else None

    @property
    def conical_gear_design_of_type_zerol_bevel_gear_design(self) -> '_708.ZerolBevelGearDesign':
        '''ZerolBevelGearDesign: 'ConicalGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _708.ZerolBevelGearDesign.TYPE not in self.wrapped.ConicalGearDesign.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_design to ZerolBevelGearDesign. Expected: {}.'.format(self.wrapped.ConicalGearDesign.__class__.__qualname__))

        return constructor.new(_708.ZerolBevelGearDesign)(self.wrapped.ConicalGearDesign) if self.wrapped.ConicalGearDesign else None

    @property
    def conical_gear_design_of_type_straight_bevel_diff_gear_design(self) -> '_717.StraightBevelDiffGearDesign':
        '''StraightBevelDiffGearDesign: 'ConicalGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _717.StraightBevelDiffGearDesign.TYPE not in self.wrapped.ConicalGearDesign.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_design to StraightBevelDiffGearDesign. Expected: {}.'.format(self.wrapped.ConicalGearDesign.__class__.__qualname__))

        return constructor.new(_717.StraightBevelDiffGearDesign)(self.wrapped.ConicalGearDesign) if self.wrapped.ConicalGearDesign else None

    @property
    def conical_gear_design_of_type_straight_bevel_gear_design(self) -> '_721.StraightBevelGearDesign':
        '''StraightBevelGearDesign: 'ConicalGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _721.StraightBevelGearDesign.TYPE not in self.wrapped.ConicalGearDesign.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_design to StraightBevelGearDesign. Expected: {}.'.format(self.wrapped.ConicalGearDesign.__class__.__qualname__))

        return constructor.new(_721.StraightBevelGearDesign)(self.wrapped.ConicalGearDesign) if self.wrapped.ConicalGearDesign else None

    @property
    def conical_gear_design_of_type_spiral_bevel_gear_design(self) -> '_725.SpiralBevelGearDesign':
        '''SpiralBevelGearDesign: 'ConicalGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _725.SpiralBevelGearDesign.TYPE not in self.wrapped.ConicalGearDesign.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_design to SpiralBevelGearDesign. Expected: {}.'.format(self.wrapped.ConicalGearDesign.__class__.__qualname__))

        return constructor.new(_725.SpiralBevelGearDesign)(self.wrapped.ConicalGearDesign) if self.wrapped.ConicalGearDesign else None

    @property
    def conical_gear_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_design(self) -> '_729.KlingelnbergCycloPalloidSpiralBevelGearDesign':
        '''KlingelnbergCycloPalloidSpiralBevelGearDesign: 'ConicalGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _729.KlingelnbergCycloPalloidSpiralBevelGearDesign.TYPE not in self.wrapped.ConicalGearDesign.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_design to KlingelnbergCycloPalloidSpiralBevelGearDesign. Expected: {}.'.format(self.wrapped.ConicalGearDesign.__class__.__qualname__))

        return constructor.new(_729.KlingelnbergCycloPalloidSpiralBevelGearDesign)(self.wrapped.ConicalGearDesign) if self.wrapped.ConicalGearDesign else None

    @property
    def conical_gear_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear_design(self) -> '_733.KlingelnbergCycloPalloidHypoidGearDesign':
        '''KlingelnbergCycloPalloidHypoidGearDesign: 'ConicalGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _733.KlingelnbergCycloPalloidHypoidGearDesign.TYPE not in self.wrapped.ConicalGearDesign.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_design to KlingelnbergCycloPalloidHypoidGearDesign. Expected: {}.'.format(self.wrapped.ConicalGearDesign.__class__.__qualname__))

        return constructor.new(_733.KlingelnbergCycloPalloidHypoidGearDesign)(self.wrapped.ConicalGearDesign) if self.wrapped.ConicalGearDesign else None

    @property
    def conical_gear_design_of_type_klingelnberg_conical_gear_design(self) -> '_737.KlingelnbergConicalGearDesign':
        '''KlingelnbergConicalGearDesign: 'ConicalGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _737.KlingelnbergConicalGearDesign.TYPE not in self.wrapped.ConicalGearDesign.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_design to KlingelnbergConicalGearDesign. Expected: {}.'.format(self.wrapped.ConicalGearDesign.__class__.__qualname__))

        return constructor.new(_737.KlingelnbergConicalGearDesign)(self.wrapped.ConicalGearDesign) if self.wrapped.ConicalGearDesign else None

    @property
    def conical_gear_design_of_type_hypoid_gear_design(self) -> '_741.HypoidGearDesign':
        '''HypoidGearDesign: 'ConicalGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _741.HypoidGearDesign.TYPE not in self.wrapped.ConicalGearDesign.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_design to HypoidGearDesign. Expected: {}.'.format(self.wrapped.ConicalGearDesign.__class__.__qualname__))

        return constructor.new(_741.HypoidGearDesign)(self.wrapped.ConicalGearDesign) if self.wrapped.ConicalGearDesign else None

    @property
    def conical_gear_design_of_type_bevel_gear_design(self) -> '_905.BevelGearDesign':
        '''BevelGearDesign: 'ConicalGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _905.BevelGearDesign.TYPE not in self.wrapped.ConicalGearDesign.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_design to BevelGearDesign. Expected: {}.'.format(self.wrapped.ConicalGearDesign.__class__.__qualname__))

        return constructor.new(_905.BevelGearDesign)(self.wrapped.ConicalGearDesign) if self.wrapped.ConicalGearDesign else None

    @property
    def conical_gear_design_of_type_agma_gleason_conical_gear_design(self) -> '_918.AGMAGleasonConicalGearDesign':
        '''AGMAGleasonConicalGearDesign: 'ConicalGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _918.AGMAGleasonConicalGearDesign.TYPE not in self.wrapped.ConicalGearDesign.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_design to AGMAGleasonConicalGearDesign. Expected: {}.'.format(self.wrapped.ConicalGearDesign.__class__.__qualname__))

        return constructor.new(_918.AGMAGleasonConicalGearDesign)(self.wrapped.ConicalGearDesign) if self.wrapped.ConicalGearDesign else None
