'''_341.py

GearSetDutyCycleRating
'''


from typing import Callable, List

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs import _365
from mastapy.gears.gear_designs.zerol_bevel import _366
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.worm import _367
from mastapy.gears.gear_designs.straight_bevel_diff import _368
from mastapy.gears.gear_designs.straight_bevel import _369
from mastapy.gears.gear_designs.spiral_bevel import _370
from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _371
from mastapy.gears.gear_designs.klingelnberg_hypoid import _372
from mastapy.gears.gear_designs.klingelnberg_conical import _373
from mastapy.gears.gear_designs.hypoid import _374
from mastapy.gears.gear_designs.face import _375
from mastapy.gears.gear_designs.cylindrical import _376, _377
from mastapy.gears.gear_designs.conical import _378
from mastapy.gears.gear_designs.concept import _379
from mastapy.gears.gear_designs.bevel import _380
from mastapy.gears.gear_designs.agma_gleason_conical import _381
from mastapy.gears.rating import _337, _344, _334
from mastapy._internal.python_net import python_net_import

_GEAR_SET_DUTY_CYCLE_RATING = python_net_import('SMT.MastaAPI.Gears.Rating', 'GearSetDutyCycleRating')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetDutyCycleRating',)


class GearSetDutyCycleRating(_334.AbstractGearSetRating):
    '''GearSetDutyCycleRating

    This is a mastapy class.
    '''

    TYPE = _GEAR_SET_DUTY_CYCLE_RATING
    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearSetDutyCycleRating.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def name(self) -> 'str':
        '''str: 'Name' is the original name of this property.'''

        return self.wrapped.Name

    @name.setter
    def name(self, value: 'str'):
        self.wrapped.Name = str(value) if value else None

    @property
    def total_duty_cycle_gear_set_reliability(self) -> 'float':
        '''float: 'TotalDutyCycleGearSetReliability' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.TotalDutyCycleGearSetReliability

    @property
    def duty_cycle_name(self) -> 'str':
        '''str: 'DutyCycleName' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.DutyCycleName

    @property
    def set_face_widths_for_specified_safety_factors(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'SetFaceWidthsForSpecifiedSafetyFactors' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.SetFaceWidthsForSpecifiedSafetyFactors

    @property
    def gear_set_design(self) -> '_365.GearSetDesign':
        '''GearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_365.GearSetDesign)(self.wrapped.GearSetDesign) if self.wrapped.GearSetDesign else None

    @property
    def gear_set_design_of_type_zerol_bevel_gear_set_design(self) -> '_366.ZerolBevelGearSetDesign':
        '''ZerolBevelGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _366.ZerolBevelGearSetDesign.TYPE not in self.wrapped.GearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to ZerolBevelGearSetDesign. Expected: {}.'.format(self.wrapped.GearSetDesign.__class__.__qualname__))

        return constructor.new(_366.ZerolBevelGearSetDesign)(self.wrapped.GearSetDesign) if self.wrapped.GearSetDesign else None

    @property
    def gear_set_design_of_type_worm_gear_set_design(self) -> '_367.WormGearSetDesign':
        '''WormGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _367.WormGearSetDesign.TYPE not in self.wrapped.GearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to WormGearSetDesign. Expected: {}.'.format(self.wrapped.GearSetDesign.__class__.__qualname__))

        return constructor.new(_367.WormGearSetDesign)(self.wrapped.GearSetDesign) if self.wrapped.GearSetDesign else None

    @property
    def gear_set_design_of_type_straight_bevel_diff_gear_set_design(self) -> '_368.StraightBevelDiffGearSetDesign':
        '''StraightBevelDiffGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _368.StraightBevelDiffGearSetDesign.TYPE not in self.wrapped.GearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to StraightBevelDiffGearSetDesign. Expected: {}.'.format(self.wrapped.GearSetDesign.__class__.__qualname__))

        return constructor.new(_368.StraightBevelDiffGearSetDesign)(self.wrapped.GearSetDesign) if self.wrapped.GearSetDesign else None

    @property
    def gear_set_design_of_type_straight_bevel_gear_set_design(self) -> '_369.StraightBevelGearSetDesign':
        '''StraightBevelGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _369.StraightBevelGearSetDesign.TYPE not in self.wrapped.GearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to StraightBevelGearSetDesign. Expected: {}.'.format(self.wrapped.GearSetDesign.__class__.__qualname__))

        return constructor.new(_369.StraightBevelGearSetDesign)(self.wrapped.GearSetDesign) if self.wrapped.GearSetDesign else None

    @property
    def gear_set_design_of_type_spiral_bevel_gear_set_design(self) -> '_370.SpiralBevelGearSetDesign':
        '''SpiralBevelGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _370.SpiralBevelGearSetDesign.TYPE not in self.wrapped.GearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to SpiralBevelGearSetDesign. Expected: {}.'.format(self.wrapped.GearSetDesign.__class__.__qualname__))

        return constructor.new(_370.SpiralBevelGearSetDesign)(self.wrapped.GearSetDesign) if self.wrapped.GearSetDesign else None

    @property
    def gear_set_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_design(self) -> '_371.KlingelnbergCycloPalloidSpiralBevelGearSetDesign':
        '''KlingelnbergCycloPalloidSpiralBevelGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _371.KlingelnbergCycloPalloidSpiralBevelGearSetDesign.TYPE not in self.wrapped.GearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to KlingelnbergCycloPalloidSpiralBevelGearSetDesign. Expected: {}.'.format(self.wrapped.GearSetDesign.__class__.__qualname__))

        return constructor.new(_371.KlingelnbergCycloPalloidSpiralBevelGearSetDesign)(self.wrapped.GearSetDesign) if self.wrapped.GearSetDesign else None

    @property
    def gear_set_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set_design(self) -> '_372.KlingelnbergCycloPalloidHypoidGearSetDesign':
        '''KlingelnbergCycloPalloidHypoidGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _372.KlingelnbergCycloPalloidHypoidGearSetDesign.TYPE not in self.wrapped.GearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to KlingelnbergCycloPalloidHypoidGearSetDesign. Expected: {}.'.format(self.wrapped.GearSetDesign.__class__.__qualname__))

        return constructor.new(_372.KlingelnbergCycloPalloidHypoidGearSetDesign)(self.wrapped.GearSetDesign) if self.wrapped.GearSetDesign else None

    @property
    def gear_set_design_of_type_klingelnberg_conical_gear_set_design(self) -> '_373.KlingelnbergConicalGearSetDesign':
        '''KlingelnbergConicalGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _373.KlingelnbergConicalGearSetDesign.TYPE not in self.wrapped.GearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to KlingelnbergConicalGearSetDesign. Expected: {}.'.format(self.wrapped.GearSetDesign.__class__.__qualname__))

        return constructor.new(_373.KlingelnbergConicalGearSetDesign)(self.wrapped.GearSetDesign) if self.wrapped.GearSetDesign else None

    @property
    def gear_set_design_of_type_hypoid_gear_set_design(self) -> '_374.HypoidGearSetDesign':
        '''HypoidGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _374.HypoidGearSetDesign.TYPE not in self.wrapped.GearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to HypoidGearSetDesign. Expected: {}.'.format(self.wrapped.GearSetDesign.__class__.__qualname__))

        return constructor.new(_374.HypoidGearSetDesign)(self.wrapped.GearSetDesign) if self.wrapped.GearSetDesign else None

    @property
    def gear_set_design_of_type_face_gear_set_design(self) -> '_375.FaceGearSetDesign':
        '''FaceGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _375.FaceGearSetDesign.TYPE not in self.wrapped.GearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to FaceGearSetDesign. Expected: {}.'.format(self.wrapped.GearSetDesign.__class__.__qualname__))

        return constructor.new(_375.FaceGearSetDesign)(self.wrapped.GearSetDesign) if self.wrapped.GearSetDesign else None

    @property
    def gear_set_design_of_type_cylindrical_gear_set_design(self) -> '_376.CylindricalGearSetDesign':
        '''CylindricalGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _376.CylindricalGearSetDesign.TYPE not in self.wrapped.GearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to CylindricalGearSetDesign. Expected: {}.'.format(self.wrapped.GearSetDesign.__class__.__qualname__))

        return constructor.new(_376.CylindricalGearSetDesign)(self.wrapped.GearSetDesign) if self.wrapped.GearSetDesign else None

    @property
    def gear_set_design_of_type_cylindrical_planetary_gear_set_design(self) -> '_377.CylindricalPlanetaryGearSetDesign':
        '''CylindricalPlanetaryGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _377.CylindricalPlanetaryGearSetDesign.TYPE not in self.wrapped.GearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to CylindricalPlanetaryGearSetDesign. Expected: {}.'.format(self.wrapped.GearSetDesign.__class__.__qualname__))

        return constructor.new(_377.CylindricalPlanetaryGearSetDesign)(self.wrapped.GearSetDesign) if self.wrapped.GearSetDesign else None

    @property
    def gear_set_design_of_type_conical_gear_set_design(self) -> '_378.ConicalGearSetDesign':
        '''ConicalGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _378.ConicalGearSetDesign.TYPE not in self.wrapped.GearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to ConicalGearSetDesign. Expected: {}.'.format(self.wrapped.GearSetDesign.__class__.__qualname__))

        return constructor.new(_378.ConicalGearSetDesign)(self.wrapped.GearSetDesign) if self.wrapped.GearSetDesign else None

    @property
    def gear_set_design_of_type_concept_gear_set_design(self) -> '_379.ConceptGearSetDesign':
        '''ConceptGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _379.ConceptGearSetDesign.TYPE not in self.wrapped.GearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to ConceptGearSetDesign. Expected: {}.'.format(self.wrapped.GearSetDesign.__class__.__qualname__))

        return constructor.new(_379.ConceptGearSetDesign)(self.wrapped.GearSetDesign) if self.wrapped.GearSetDesign else None

    @property
    def gear_set_design_of_type_bevel_gear_set_design(self) -> '_380.BevelGearSetDesign':
        '''BevelGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _380.BevelGearSetDesign.TYPE not in self.wrapped.GearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to BevelGearSetDesign. Expected: {}.'.format(self.wrapped.GearSetDesign.__class__.__qualname__))

        return constructor.new(_380.BevelGearSetDesign)(self.wrapped.GearSetDesign) if self.wrapped.GearSetDesign else None

    @property
    def gear_set_design_of_type_agma_gleason_conical_gear_set_design(self) -> '_381.AGMAGleasonConicalGearSetDesign':
        '''AGMAGleasonConicalGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _381.AGMAGleasonConicalGearSetDesign.TYPE not in self.wrapped.GearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to AGMAGleasonConicalGearSetDesign. Expected: {}.'.format(self.wrapped.GearSetDesign.__class__.__qualname__))

        return constructor.new(_381.AGMAGleasonConicalGearSetDesign)(self.wrapped.GearSetDesign) if self.wrapped.GearSetDesign else None

    @property
    def gear_ratings(self) -> 'List[_337.GearDutyCycleRating]':
        '''List[GearDutyCycleRating]: 'GearRatings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.GearRatings, constructor.new(_337.GearDutyCycleRating))
        return value

    @property
    def gear_duty_cycle_ratings(self) -> 'List[_337.GearDutyCycleRating]':
        '''List[GearDutyCycleRating]: 'GearDutyCycleRatings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.GearDutyCycleRatings, constructor.new(_337.GearDutyCycleRating))
        return value

    @property
    def gear_mesh_ratings(self) -> 'List[_344.MeshDutyCycleRating]':
        '''List[MeshDutyCycleRating]: 'GearMeshRatings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.GearMeshRatings, constructor.new(_344.MeshDutyCycleRating))
        return value

    @property
    def gear_mesh_duty_cycle_ratings(self) -> 'List[_344.MeshDutyCycleRating]':
        '''List[MeshDutyCycleRating]: 'GearMeshDutyCycleRatings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.GearMeshDutyCycleRatings, constructor.new(_344.MeshDutyCycleRating))
        return value
