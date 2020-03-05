'''_569.py

FlankMicroGeometry
'''


from mastapy.gears import _309
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs import _655
from mastapy.gears.gear_designs.zerol_bevel import _415
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.worm import _666, _477, _667
from mastapy.gears.gear_designs.straight_bevel_diff import _485
from mastapy.gears.gear_designs.straight_bevel import _445
from mastapy.gears.gear_designs.spiral_bevel import _498
from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _520
from mastapy.gears.gear_designs.klingelnberg_hypoid import _474
from mastapy.gears.gear_designs.hypoid import _560
from mastapy.gears.gear_designs.face import _495, _668, _669
from mastapy.gears.gear_designs.cylindrical import _577, _670
from mastapy.gears.gear_designs.concept import _583
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
    def gear_design(self) -> '_655.GearDesign':
        '''GearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_655.GearDesign)(self.wrapped.GearDesign) if self.wrapped.GearDesign else None

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
    def gear_design_of_type_worm_design(self) -> '_666.WormDesign':
        '''WormDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearDesign.__class__.__qualname__ != 'WormDesign':
            raise CastException('Failed to cast gear_design to WormDesign. Expected: {}.'.format(self.wrapped.GearDesign.__class__.__qualname__))

        return constructor.new(_666.WormDesign)(self.wrapped.GearDesign) if self.wrapped.GearDesign else None

    @property
    def gear_design_of_type_worm_gear_design(self) -> '_477.WormGearDesign':
        '''WormGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearDesign.__class__.__qualname__ != 'WormGearDesign':
            raise CastException('Failed to cast gear_design to WormGearDesign. Expected: {}.'.format(self.wrapped.GearDesign.__class__.__qualname__))

        return constructor.new(_477.WormGearDesign)(self.wrapped.GearDesign) if self.wrapped.GearDesign else None

    @property
    def gear_design_of_type_worm_wheel_design(self) -> '_667.WormWheelDesign':
        '''WormWheelDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearDesign.__class__.__qualname__ != 'WormWheelDesign':
            raise CastException('Failed to cast gear_design to WormWheelDesign. Expected: {}.'.format(self.wrapped.GearDesign.__class__.__qualname__))

        return constructor.new(_667.WormWheelDesign)(self.wrapped.GearDesign) if self.wrapped.GearDesign else None

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

    @property
    def gear_design_of_type_face_gear_design(self) -> '_495.FaceGearDesign':
        '''FaceGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearDesign.__class__.__qualname__ != 'FaceGearDesign':
            raise CastException('Failed to cast gear_design to FaceGearDesign. Expected: {}.'.format(self.wrapped.GearDesign.__class__.__qualname__))

        return constructor.new(_495.FaceGearDesign)(self.wrapped.GearDesign) if self.wrapped.GearDesign else None

    @property
    def gear_design_of_type_face_gear_pinion_design(self) -> '_668.FaceGearPinionDesign':
        '''FaceGearPinionDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearDesign.__class__.__qualname__ != 'FaceGearPinionDesign':
            raise CastException('Failed to cast gear_design to FaceGearPinionDesign. Expected: {}.'.format(self.wrapped.GearDesign.__class__.__qualname__))

        return constructor.new(_668.FaceGearPinionDesign)(self.wrapped.GearDesign) if self.wrapped.GearDesign else None

    @property
    def gear_design_of_type_face_gear_wheel_design(self) -> '_669.FaceGearWheelDesign':
        '''FaceGearWheelDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearDesign.__class__.__qualname__ != 'FaceGearWheelDesign':
            raise CastException('Failed to cast gear_design to FaceGearWheelDesign. Expected: {}.'.format(self.wrapped.GearDesign.__class__.__qualname__))

        return constructor.new(_669.FaceGearWheelDesign)(self.wrapped.GearDesign) if self.wrapped.GearDesign else None

    @property
    def gear_design_of_type_cylindrical_gear_design(self) -> '_577.CylindricalGearDesign':
        '''CylindricalGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearDesign.__class__.__qualname__ != 'CylindricalGearDesign':
            raise CastException('Failed to cast gear_design to CylindricalGearDesign. Expected: {}.'.format(self.wrapped.GearDesign.__class__.__qualname__))

        return constructor.new(_577.CylindricalGearDesign)(self.wrapped.GearDesign) if self.wrapped.GearDesign else None

    @property
    def gear_design_of_type_cylindrical_planet_gear_design(self) -> '_670.CylindricalPlanetGearDesign':
        '''CylindricalPlanetGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearDesign.__class__.__qualname__ != 'CylindricalPlanetGearDesign':
            raise CastException('Failed to cast gear_design to CylindricalPlanetGearDesign. Expected: {}.'.format(self.wrapped.GearDesign.__class__.__qualname__))

        return constructor.new(_670.CylindricalPlanetGearDesign)(self.wrapped.GearDesign) if self.wrapped.GearDesign else None

    @property
    def gear_design_of_type_concept_gear_design(self) -> '_583.ConceptGearDesign':
        '''ConceptGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearDesign.__class__.__qualname__ != 'ConceptGearDesign':
            raise CastException('Failed to cast gear_design to ConceptGearDesign. Expected: {}.'.format(self.wrapped.GearDesign.__class__.__qualname__))

        return constructor.new(_583.ConceptGearDesign)(self.wrapped.GearDesign) if self.wrapped.GearDesign else None
