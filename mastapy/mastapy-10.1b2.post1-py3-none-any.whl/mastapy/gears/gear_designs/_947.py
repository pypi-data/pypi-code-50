'''_947.py

GearMeshDesign
'''


from mastapy._internal import constructor
from mastapy.gears.gear_designs import _612, _946
from mastapy.gears.gear_designs.zerol_bevel import _416
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.worm import _613, _471, _614
from mastapy.gears.gear_designs.straight_bevel_diff import _491
from mastapy.gears.gear_designs.straight_bevel import _431
from mastapy.gears.gear_designs.spiral_bevel import _472
from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _512
from mastapy.gears.gear_designs.klingelnberg_hypoid import _456
from mastapy.gears.gear_designs.hypoid import _478
from mastapy.gears.gear_designs.face import _575, _615, _616
from mastapy.gears.gear_designs.cylindrical import _498, _617
from mastapy.gears.gear_designs.concept import _581
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns', 'GearMeshDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshDesign',)


class GearMeshDesign(_946.GearDesignComponent):
    '''GearMeshDesign

    This is a mastapy class.
    '''

    TYPE = _GEAR_MESH_DESIGN
    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearMeshDesign.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def name(self) -> 'str':
        '''str: 'Name' is the original name of this property.'''

        return self.wrapped.Name

    @name.setter
    def name(self, value: 'str'):
        self.wrapped.Name = str(value) if value else None

    @property
    def speed_ratio_a_to_b(self) -> 'float':
        '''float: 'SpeedRatioAToB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.SpeedRatioAToB

    @property
    def torque_ratio_a_to_b(self) -> 'float':
        '''float: 'TorqueRatioAToB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TorqueRatioAToB

    @property
    def highest_common_factor_of_teeth_numbers(self) -> 'int':
        '''int: 'HighestCommonFactorOfTeethNumbers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.HighestCommonFactorOfTeethNumbers

    @property
    def has_hunting_ratio(self) -> 'bool':
        '''bool: 'HasHuntingRatio' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.HasHuntingRatio

    @property
    def hunting_tooth_factor(self) -> 'float':
        '''float: 'HuntingToothFactor' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.HuntingToothFactor

    @property
    def axial_contact_ratio_rating_for_nvh(self) -> 'float':
        '''float: 'AxialContactRatioRatingForNVH' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AxialContactRatioRatingForNVH

    @property
    def transverse_contact_ratio_rating_for_nvh(self) -> 'float':
        '''float: 'TransverseContactRatioRatingForNVH' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TransverseContactRatioRatingForNVH

    @property
    def transverse_and_axial_contact_ratio_rating_for_nvh(self) -> 'float':
        '''float: 'TransverseAndAxialContactRatioRatingForNVH' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TransverseAndAxialContactRatioRatingForNVH

    @property
    def gear_a(self) -> '_612.GearDesign':
        '''GearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_612.GearDesign)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_zerol_bevel_gear_design(self) -> '_416.ZerolBevelGearDesign':
        '''ZerolBevelGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'ZerolBevelGearDesign':
            raise CastException('Failed to cast gear_a to ZerolBevelGearDesign. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_416.ZerolBevelGearDesign)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_worm_design(self) -> '_613.WormDesign':
        '''WormDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'WormDesign':
            raise CastException('Failed to cast gear_a to WormDesign. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_613.WormDesign)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_worm_gear_design(self) -> '_471.WormGearDesign':
        '''WormGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'WormGearDesign':
            raise CastException('Failed to cast gear_a to WormGearDesign. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_471.WormGearDesign)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_worm_wheel_design(self) -> '_614.WormWheelDesign':
        '''WormWheelDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'WormWheelDesign':
            raise CastException('Failed to cast gear_a to WormWheelDesign. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_614.WormWheelDesign)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_straight_bevel_diff_gear_design(self) -> '_491.StraightBevelDiffGearDesign':
        '''StraightBevelDiffGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'StraightBevelDiffGearDesign':
            raise CastException('Failed to cast gear_a to StraightBevelDiffGearDesign. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_491.StraightBevelDiffGearDesign)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_straight_bevel_gear_design(self) -> '_431.StraightBevelGearDesign':
        '''StraightBevelGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'StraightBevelGearDesign':
            raise CastException('Failed to cast gear_a to StraightBevelGearDesign. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_431.StraightBevelGearDesign)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_spiral_bevel_gear_design(self) -> '_472.SpiralBevelGearDesign':
        '''SpiralBevelGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'SpiralBevelGearDesign':
            raise CastException('Failed to cast gear_a to SpiralBevelGearDesign. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_472.SpiralBevelGearDesign)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_design(self) -> '_512.KlingelnbergCycloPalloidSpiralBevelGearDesign':
        '''KlingelnbergCycloPalloidSpiralBevelGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'KlingelnbergCycloPalloidSpiralBevelGearDesign':
            raise CastException('Failed to cast gear_a to KlingelnbergCycloPalloidSpiralBevelGearDesign. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_512.KlingelnbergCycloPalloidSpiralBevelGearDesign)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_klingelnberg_cyclo_palloid_hypoid_gear_design(self) -> '_456.KlingelnbergCycloPalloidHypoidGearDesign':
        '''KlingelnbergCycloPalloidHypoidGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'KlingelnbergCycloPalloidHypoidGearDesign':
            raise CastException('Failed to cast gear_a to KlingelnbergCycloPalloidHypoidGearDesign. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_456.KlingelnbergCycloPalloidHypoidGearDesign)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_hypoid_gear_design(self) -> '_478.HypoidGearDesign':
        '''HypoidGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'HypoidGearDesign':
            raise CastException('Failed to cast gear_a to HypoidGearDesign. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_478.HypoidGearDesign)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_face_gear_design(self) -> '_575.FaceGearDesign':
        '''FaceGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'FaceGearDesign':
            raise CastException('Failed to cast gear_a to FaceGearDesign. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_575.FaceGearDesign)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_face_gear_pinion_design(self) -> '_615.FaceGearPinionDesign':
        '''FaceGearPinionDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'FaceGearPinionDesign':
            raise CastException('Failed to cast gear_a to FaceGearPinionDesign. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_615.FaceGearPinionDesign)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_face_gear_wheel_design(self) -> '_616.FaceGearWheelDesign':
        '''FaceGearWheelDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'FaceGearWheelDesign':
            raise CastException('Failed to cast gear_a to FaceGearWheelDesign. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_616.FaceGearWheelDesign)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_cylindrical_gear_design(self) -> '_498.CylindricalGearDesign':
        '''CylindricalGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'CylindricalGearDesign':
            raise CastException('Failed to cast gear_a to CylindricalGearDesign. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_498.CylindricalGearDesign)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_cylindrical_planet_gear_design(self) -> '_617.CylindricalPlanetGearDesign':
        '''CylindricalPlanetGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'CylindricalPlanetGearDesign':
            raise CastException('Failed to cast gear_a to CylindricalPlanetGearDesign. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_617.CylindricalPlanetGearDesign)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_a_of_type_concept_gear_design(self) -> '_581.ConceptGearDesign':
        '''ConceptGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearA.__class__.__qualname__ != 'ConceptGearDesign':
            raise CastException('Failed to cast gear_a to ConceptGearDesign. Expected: {}.'.format(self.wrapped.GearA.__class__.__qualname__))

        return constructor.new(_581.ConceptGearDesign)(self.wrapped.GearA) if self.wrapped.GearA else None

    @property
    def gear_b(self) -> '_612.GearDesign':
        '''GearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_612.GearDesign)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_zerol_bevel_gear_design(self) -> '_416.ZerolBevelGearDesign':
        '''ZerolBevelGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'ZerolBevelGearDesign':
            raise CastException('Failed to cast gear_b to ZerolBevelGearDesign. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_416.ZerolBevelGearDesign)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_worm_design(self) -> '_613.WormDesign':
        '''WormDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'WormDesign':
            raise CastException('Failed to cast gear_b to WormDesign. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_613.WormDesign)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_worm_gear_design(self) -> '_471.WormGearDesign':
        '''WormGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'WormGearDesign':
            raise CastException('Failed to cast gear_b to WormGearDesign. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_471.WormGearDesign)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_worm_wheel_design(self) -> '_614.WormWheelDesign':
        '''WormWheelDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'WormWheelDesign':
            raise CastException('Failed to cast gear_b to WormWheelDesign. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_614.WormWheelDesign)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_straight_bevel_diff_gear_design(self) -> '_491.StraightBevelDiffGearDesign':
        '''StraightBevelDiffGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'StraightBevelDiffGearDesign':
            raise CastException('Failed to cast gear_b to StraightBevelDiffGearDesign. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_491.StraightBevelDiffGearDesign)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_straight_bevel_gear_design(self) -> '_431.StraightBevelGearDesign':
        '''StraightBevelGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'StraightBevelGearDesign':
            raise CastException('Failed to cast gear_b to StraightBevelGearDesign. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_431.StraightBevelGearDesign)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_spiral_bevel_gear_design(self) -> '_472.SpiralBevelGearDesign':
        '''SpiralBevelGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'SpiralBevelGearDesign':
            raise CastException('Failed to cast gear_b to SpiralBevelGearDesign. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_472.SpiralBevelGearDesign)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_design(self) -> '_512.KlingelnbergCycloPalloidSpiralBevelGearDesign':
        '''KlingelnbergCycloPalloidSpiralBevelGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'KlingelnbergCycloPalloidSpiralBevelGearDesign':
            raise CastException('Failed to cast gear_b to KlingelnbergCycloPalloidSpiralBevelGearDesign. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_512.KlingelnbergCycloPalloidSpiralBevelGearDesign)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_klingelnberg_cyclo_palloid_hypoid_gear_design(self) -> '_456.KlingelnbergCycloPalloidHypoidGearDesign':
        '''KlingelnbergCycloPalloidHypoidGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'KlingelnbergCycloPalloidHypoidGearDesign':
            raise CastException('Failed to cast gear_b to KlingelnbergCycloPalloidHypoidGearDesign. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_456.KlingelnbergCycloPalloidHypoidGearDesign)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_hypoid_gear_design(self) -> '_478.HypoidGearDesign':
        '''HypoidGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'HypoidGearDesign':
            raise CastException('Failed to cast gear_b to HypoidGearDesign. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_478.HypoidGearDesign)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_face_gear_design(self) -> '_575.FaceGearDesign':
        '''FaceGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'FaceGearDesign':
            raise CastException('Failed to cast gear_b to FaceGearDesign. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_575.FaceGearDesign)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_face_gear_pinion_design(self) -> '_615.FaceGearPinionDesign':
        '''FaceGearPinionDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'FaceGearPinionDesign':
            raise CastException('Failed to cast gear_b to FaceGearPinionDesign. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_615.FaceGearPinionDesign)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_face_gear_wheel_design(self) -> '_616.FaceGearWheelDesign':
        '''FaceGearWheelDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'FaceGearWheelDesign':
            raise CastException('Failed to cast gear_b to FaceGearWheelDesign. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_616.FaceGearWheelDesign)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_cylindrical_gear_design(self) -> '_498.CylindricalGearDesign':
        '''CylindricalGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'CylindricalGearDesign':
            raise CastException('Failed to cast gear_b to CylindricalGearDesign. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_498.CylindricalGearDesign)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_cylindrical_planet_gear_design(self) -> '_617.CylindricalPlanetGearDesign':
        '''CylindricalPlanetGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'CylindricalPlanetGearDesign':
            raise CastException('Failed to cast gear_b to CylindricalPlanetGearDesign. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_617.CylindricalPlanetGearDesign)(self.wrapped.GearB) if self.wrapped.GearB else None

    @property
    def gear_b_of_type_concept_gear_design(self) -> '_581.ConceptGearDesign':
        '''ConceptGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.GearB.__class__.__qualname__ != 'ConceptGearDesign':
            raise CastException('Failed to cast gear_b to ConceptGearDesign. Expected: {}.'.format(self.wrapped.GearB.__class__.__qualname__))

        return constructor.new(_581.ConceptGearDesign)(self.wrapped.GearB) if self.wrapped.GearB else None
