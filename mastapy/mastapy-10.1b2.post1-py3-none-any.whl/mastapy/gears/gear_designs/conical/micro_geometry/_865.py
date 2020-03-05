'''_865.py

ConicalGearFlankMicroGeometry
'''


from mastapy.gears import _309
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.conical.micro_geometry import _1097, _1096, _1095
from mastapy.gears.gear_designs.conical import _1084
from mastapy.gears.gear_designs.zerol_bevel import _415
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.straight_bevel_diff import _485
from mastapy.gears.gear_designs.straight_bevel import _445
from mastapy.gears.gear_designs.spiral_bevel import _498
from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _520
from mastapy.gears.gear_designs.klingelnberg_hypoid import _474
from mastapy.gears.gear_designs.hypoid import _560
from mastapy.gears.micro_geometry import _569
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_FLANK_MICRO_GEOMETRY = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Conical.MicroGeometry', 'ConicalGearFlankMicroGeometry')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearFlankMicroGeometry',)


class ConicalGearFlankMicroGeometry(_569.FlankMicroGeometry):
    '''ConicalGearFlankMicroGeometry

    This is a mastapy class.
    '''

    TYPE = _CONICAL_GEAR_FLANK_MICRO_GEOMETRY
    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConicalGearFlankMicroGeometry.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def micro_geometry_input_type(self) -> '_309.MicroGeometryInputTypes':
        '''MicroGeometryInputTypes: 'MicroGeometryInputType' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.MicroGeometryInputType)
        return constructor.new(_309.MicroGeometryInputTypes)(value) if value else None

    @micro_geometry_input_type.setter
    def micro_geometry_input_type(self, value: '_309.MicroGeometryInputTypes'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.MicroGeometryInputType = value

    @property
    def profile_relief(self) -> '_1097.ConicalGearProfileModification':
        '''ConicalGearProfileModification: 'ProfileRelief' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1097.ConicalGearProfileModification)(self.wrapped.ProfileRelief) if self.wrapped.ProfileRelief else None

    @property
    def lead_relief(self) -> '_1096.ConicalGearLeadModification':
        '''ConicalGearLeadModification: 'LeadRelief' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1096.ConicalGearLeadModification)(self.wrapped.LeadRelief) if self.wrapped.LeadRelief else None

    @property
    def bias(self) -> '_1095.ConicalGearBiasModification':
        '''ConicalGearBiasModification: 'Bias' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1095.ConicalGearBiasModification)(self.wrapped.Bias) if self.wrapped.Bias else None

    @property
    def gear_design(self) -> '_1084.ConicalGearDesign':
        '''ConicalGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1084.ConicalGearDesign)(self.wrapped.GearDesign) if self.wrapped.GearDesign else None

    @property
    def gear_design_of_type_zerol_bevel_gear_design(self) -> '_415.ZerolBevelGearDesign':
        '''ZerolBevelGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearDesign.__class__.__qualname__ != 'ZerolBevelGearDesign':
            raise CastException('Failed to cast gear_design to ZerolBevelGearDesign. Expected: {}.'.format(self.wrapped.GearDesign.__class__.__qualname__))

        return constructor.new(_415.ZerolBevelGearDesign)(self.wrapped.GearDesign) if self.wrapped.GearDesign else None

    @property
    def gear_design_of_type_straight_bevel_diff_gear_design(self) -> '_485.StraightBevelDiffGearDesign':
        '''StraightBevelDiffGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearDesign.__class__.__qualname__ != 'StraightBevelDiffGearDesign':
            raise CastException('Failed to cast gear_design to StraightBevelDiffGearDesign. Expected: {}.'.format(self.wrapped.GearDesign.__class__.__qualname__))

        return constructor.new(_485.StraightBevelDiffGearDesign)(self.wrapped.GearDesign) if self.wrapped.GearDesign else None

    @property
    def gear_design_of_type_straight_bevel_gear_design(self) -> '_445.StraightBevelGearDesign':
        '''StraightBevelGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearDesign.__class__.__qualname__ != 'StraightBevelGearDesign':
            raise CastException('Failed to cast gear_design to StraightBevelGearDesign. Expected: {}.'.format(self.wrapped.GearDesign.__class__.__qualname__))

        return constructor.new(_445.StraightBevelGearDesign)(self.wrapped.GearDesign) if self.wrapped.GearDesign else None

    @property
    def gear_design_of_type_spiral_bevel_gear_design(self) -> '_498.SpiralBevelGearDesign':
        '''SpiralBevelGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearDesign.__class__.__qualname__ != 'SpiralBevelGearDesign':
            raise CastException('Failed to cast gear_design to SpiralBevelGearDesign. Expected: {}.'.format(self.wrapped.GearDesign.__class__.__qualname__))

        return constructor.new(_498.SpiralBevelGearDesign)(self.wrapped.GearDesign) if self.wrapped.GearDesign else None

    @property
    def gear_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_design(self) -> '_520.KlingelnbergCycloPalloidSpiralBevelGearDesign':
        '''KlingelnbergCycloPalloidSpiralBevelGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearDesign.__class__.__qualname__ != 'KlingelnbergCycloPalloidSpiralBevelGearDesign':
            raise CastException('Failed to cast gear_design to KlingelnbergCycloPalloidSpiralBevelGearDesign. Expected: {}.'.format(self.wrapped.GearDesign.__class__.__qualname__))

        return constructor.new(_520.KlingelnbergCycloPalloidSpiralBevelGearDesign)(self.wrapped.GearDesign) if self.wrapped.GearDesign else None

    @property
    def gear_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear_design(self) -> '_474.KlingelnbergCycloPalloidHypoidGearDesign':
        '''KlingelnbergCycloPalloidHypoidGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearDesign.__class__.__qualname__ != 'KlingelnbergCycloPalloidHypoidGearDesign':
            raise CastException('Failed to cast gear_design to KlingelnbergCycloPalloidHypoidGearDesign. Expected: {}.'.format(self.wrapped.GearDesign.__class__.__qualname__))

        return constructor.new(_474.KlingelnbergCycloPalloidHypoidGearDesign)(self.wrapped.GearDesign) if self.wrapped.GearDesign else None

    @property
    def gear_design_of_type_hypoid_gear_design(self) -> '_560.HypoidGearDesign':
        '''HypoidGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearDesign.__class__.__qualname__ != 'HypoidGearDesign':
            raise CastException('Failed to cast gear_design to HypoidGearDesign. Expected: {}.'.format(self.wrapped.GearDesign.__class__.__qualname__))

        return constructor.new(_560.HypoidGearDesign)(self.wrapped.GearDesign) if self.wrapped.GearDesign else None
