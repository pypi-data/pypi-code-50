'''_565.py

FlankMicroGeometry
'''


from mastapy.gears import _313
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs import _638
from mastapy.gears.gear_designs.zerol_bevel import _406
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.worm import _646, _426, _647
from mastapy.gears.gear_designs.straight_bevel_diff import _451
from mastapy.gears.gear_designs.straight_bevel import _442
from mastapy.gears.gear_designs.spiral_bevel import _521
from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _541
from mastapy.gears.gear_designs.klingelnberg_hypoid import _484
from mastapy.gears.gear_designs.hypoid import _492
from mastapy.gears.gear_designs.face import _574, _648, _649
from mastapy.gears.gear_designs.cylindrical import _522, _650
from mastapy.gears.gear_designs.concept import _579
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_FLANK_MICRO_GEOMETRY = python_net_import('SMT.MastaAPI.Gears.MicroGeometry', 'FlankMicroGeometry')


__docformat__ = 'restructuredtext en'
__all__ = ('FlankMicroGeometry',)


class FlankMicroGeometry(_1.APIBase):
    '''FlankMicroGeometry

    This is a mastapy class.
    '''

    TYPE = _FLANK_MICRO_GEOMETRY
    __hash__ = None

    def __init__(self, instance_to_wrap: 'FlankMicroGeometry.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def micro_geometry_input_type(self) -> '_313.MicroGeometryInputTypes':
        '''MicroGeometryInputTypes: 'MicroGeometryInputType' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.MicroGeometryInputType)
        return constructor.new(_313.MicroGeometryInputTypes)(value) if value else None

    @micro_geometry_input_type.setter
    def micro_geometry_input_type(self, value: '_313.MicroGeometryInputTypes'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.MicroGeometryInputType = value

    @property
    def gear_design(self) -> '_638.GearDesign':
        '''GearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_638.GearDesign)(self.wrapped.GearDesign) if self.wrapped.GearDesign else None

    @property
    def gear_design_of_type_zerol_bevel_gear_design(self) -> '_406.ZerolBevelGearDesign':
        '''ZerolBevelGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearDesign.__class__.__qualname__ != 'ZerolBevelGearDesign':
            raise CastException('Failed to cast gear_design to ZerolBevelGearDesign. Expected: {}.'.format(self.wrapped.GearDesign.__class__.__qualname__))

        return constructor.new(_406.ZerolBevelGearDesign)(self.wrapped.GearDesign) if self.wrapped.GearDesign else None

    @property
    def gear_design_of_type_worm_design(self) -> '_646.WormDesign':
        '''WormDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearDesign.__class__.__qualname__ != 'WormDesign':
            raise CastException('Failed to cast gear_design to WormDesign. Expected: {}.'.format(self.wrapped.GearDesign.__class__.__qualname__))

        return constructor.new(_646.WormDesign)(self.wrapped.GearDesign) if self.wrapped.GearDesign else None

    @property
    def gear_design_of_type_worm_gear_design(self) -> '_426.WormGearDesign':
        '''WormGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearDesign.__class__.__qualname__ != 'WormGearDesign':
            raise CastException('Failed to cast gear_design to WormGearDesign. Expected: {}.'.format(self.wrapped.GearDesign.__class__.__qualname__))

        return constructor.new(_426.WormGearDesign)(self.wrapped.GearDesign) if self.wrapped.GearDesign else None

    @property
    def gear_design_of_type_worm_wheel_design(self) -> '_647.WormWheelDesign':
        '''WormWheelDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearDesign.__class__.__qualname__ != 'WormWheelDesign':
            raise CastException('Failed to cast gear_design to WormWheelDesign. Expected: {}.'.format(self.wrapped.GearDesign.__class__.__qualname__))

        return constructor.new(_647.WormWheelDesign)(self.wrapped.GearDesign) if self.wrapped.GearDesign else None

    @property
    def gear_design_of_type_straight_bevel_diff_gear_design(self) -> '_451.StraightBevelDiffGearDesign':
        '''StraightBevelDiffGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearDesign.__class__.__qualname__ != 'StraightBevelDiffGearDesign':
            raise CastException('Failed to cast gear_design to StraightBevelDiffGearDesign. Expected: {}.'.format(self.wrapped.GearDesign.__class__.__qualname__))

        return constructor.new(_451.StraightBevelDiffGearDesign)(self.wrapped.GearDesign) if self.wrapped.GearDesign else None

    @property
    def gear_design_of_type_straight_bevel_gear_design(self) -> '_442.StraightBevelGearDesign':
        '''StraightBevelGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearDesign.__class__.__qualname__ != 'StraightBevelGearDesign':
            raise CastException('Failed to cast gear_design to StraightBevelGearDesign. Expected: {}.'.format(self.wrapped.GearDesign.__class__.__qualname__))

        return constructor.new(_442.StraightBevelGearDesign)(self.wrapped.GearDesign) if self.wrapped.GearDesign else None

    @property
    def gear_design_of_type_spiral_bevel_gear_design(self) -> '_521.SpiralBevelGearDesign':
        '''SpiralBevelGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearDesign.__class__.__qualname__ != 'SpiralBevelGearDesign':
            raise CastException('Failed to cast gear_design to SpiralBevelGearDesign. Expected: {}.'.format(self.wrapped.GearDesign.__class__.__qualname__))

        return constructor.new(_521.SpiralBevelGearDesign)(self.wrapped.GearDesign) if self.wrapped.GearDesign else None

    @property
    def gear_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_design(self) -> '_541.KlingelnbergCycloPalloidSpiralBevelGearDesign':
        '''KlingelnbergCycloPalloidSpiralBevelGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearDesign.__class__.__qualname__ != 'KlingelnbergCycloPalloidSpiralBevelGearDesign':
            raise CastException('Failed to cast gear_design to KlingelnbergCycloPalloidSpiralBevelGearDesign. Expected: {}.'.format(self.wrapped.GearDesign.__class__.__qualname__))

        return constructor.new(_541.KlingelnbergCycloPalloidSpiralBevelGearDesign)(self.wrapped.GearDesign) if self.wrapped.GearDesign else None

    @property
    def gear_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear_design(self) -> '_484.KlingelnbergCycloPalloidHypoidGearDesign':
        '''KlingelnbergCycloPalloidHypoidGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearDesign.__class__.__qualname__ != 'KlingelnbergCycloPalloidHypoidGearDesign':
            raise CastException('Failed to cast gear_design to KlingelnbergCycloPalloidHypoidGearDesign. Expected: {}.'.format(self.wrapped.GearDesign.__class__.__qualname__))

        return constructor.new(_484.KlingelnbergCycloPalloidHypoidGearDesign)(self.wrapped.GearDesign) if self.wrapped.GearDesign else None

    @property
    def gear_design_of_type_hypoid_gear_design(self) -> '_492.HypoidGearDesign':
        '''HypoidGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearDesign.__class__.__qualname__ != 'HypoidGearDesign':
            raise CastException('Failed to cast gear_design to HypoidGearDesign. Expected: {}.'.format(self.wrapped.GearDesign.__class__.__qualname__))

        return constructor.new(_492.HypoidGearDesign)(self.wrapped.GearDesign) if self.wrapped.GearDesign else None

    @property
    def gear_design_of_type_face_gear_design(self) -> '_574.FaceGearDesign':
        '''FaceGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearDesign.__class__.__qualname__ != 'FaceGearDesign':
            raise CastException('Failed to cast gear_design to FaceGearDesign. Expected: {}.'.format(self.wrapped.GearDesign.__class__.__qualname__))

        return constructor.new(_574.FaceGearDesign)(self.wrapped.GearDesign) if self.wrapped.GearDesign else None

    @property
    def gear_design_of_type_face_gear_pinion_design(self) -> '_648.FaceGearPinionDesign':
        '''FaceGearPinionDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearDesign.__class__.__qualname__ != 'FaceGearPinionDesign':
            raise CastException('Failed to cast gear_design to FaceGearPinionDesign. Expected: {}.'.format(self.wrapped.GearDesign.__class__.__qualname__))

        return constructor.new(_648.FaceGearPinionDesign)(self.wrapped.GearDesign) if self.wrapped.GearDesign else None

    @property
    def gear_design_of_type_face_gear_wheel_design(self) -> '_649.FaceGearWheelDesign':
        '''FaceGearWheelDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearDesign.__class__.__qualname__ != 'FaceGearWheelDesign':
            raise CastException('Failed to cast gear_design to FaceGearWheelDesign. Expected: {}.'.format(self.wrapped.GearDesign.__class__.__qualname__))

        return constructor.new(_649.FaceGearWheelDesign)(self.wrapped.GearDesign) if self.wrapped.GearDesign else None

    @property
    def gear_design_of_type_cylindrical_gear_design(self) -> '_522.CylindricalGearDesign':
        '''CylindricalGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearDesign.__class__.__qualname__ != 'CylindricalGearDesign':
            raise CastException('Failed to cast gear_design to CylindricalGearDesign. Expected: {}.'.format(self.wrapped.GearDesign.__class__.__qualname__))

        return constructor.new(_522.CylindricalGearDesign)(self.wrapped.GearDesign) if self.wrapped.GearDesign else None

    @property
    def gear_design_of_type_cylindrical_planet_gear_design(self) -> '_650.CylindricalPlanetGearDesign':
        '''CylindricalPlanetGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearDesign.__class__.__qualname__ != 'CylindricalPlanetGearDesign':
            raise CastException('Failed to cast gear_design to CylindricalPlanetGearDesign. Expected: {}.'.format(self.wrapped.GearDesign.__class__.__qualname__))

        return constructor.new(_650.CylindricalPlanetGearDesign)(self.wrapped.GearDesign) if self.wrapped.GearDesign else None

    @property
    def gear_design_of_type_concept_gear_design(self) -> '_579.ConceptGearDesign':
        '''ConceptGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearDesign.__class__.__qualname__ != 'ConceptGearDesign':
            raise CastException('Failed to cast gear_design to ConceptGearDesign. Expected: {}.'.format(self.wrapped.GearDesign.__class__.__qualname__))

        return constructor.new(_579.ConceptGearDesign)(self.wrapped.GearDesign) if self.wrapped.GearDesign else None
