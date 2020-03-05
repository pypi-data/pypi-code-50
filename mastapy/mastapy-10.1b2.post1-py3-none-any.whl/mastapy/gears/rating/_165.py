'''_165.py

GearSetDutyCycleRating
'''


from typing import Callable, List

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs import _706
from mastapy.gears.gear_designs.zerol_bevel import _710
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.worm import _715
from mastapy.gears.gear_designs.straight_bevel_diff import _719
from mastapy.gears.gear_designs.straight_bevel import _723
from mastapy.gears.gear_designs.spiral_bevel import _727
from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _731
from mastapy.gears.gear_designs.klingelnberg_hypoid import _735
from mastapy.gears.gear_designs.klingelnberg_conical import _739
from mastapy.gears.gear_designs.hypoid import _743
from mastapy.gears.gear_designs.face import _751
from mastapy.gears.gear_designs.cylindrical import _778, _787
from mastapy.gears.gear_designs.conical import _881
from mastapy.gears.gear_designs.concept import _903
from mastapy.gears.gear_designs.bevel import _907
from mastapy.gears.gear_designs.agma_gleason_conical import _920
from mastapy.gears.rating import _161, _168, _158
from mastapy._internal.python_net import python_net_import

_GEAR_SET_DUTY_CYCLE_RATING = python_net_import('SMT.MastaAPI.Gears.Rating', 'GearSetDutyCycleRating')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetDutyCycleRating',)


class GearSetDutyCycleRating(_158.AbstractGearSetRating):
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
    def gear_set_design(self) -> '_706.GearSetDesign':
        '''GearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_706.GearSetDesign)(self.wrapped.GearSetDesign) if self.wrapped.GearSetDesign else None

    @property
    def gear_set_design_of_type_zerol_bevel_gear_set_design(self) -> '_710.ZerolBevelGearSetDesign':
        '''ZerolBevelGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _710.ZerolBevelGearSetDesign.TYPE not in self.wrapped.GearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to ZerolBevelGearSetDesign. Expected: {}.'.format(self.wrapped.GearSetDesign.__class__.__qualname__))

        return constructor.new(_710.ZerolBevelGearSetDesign)(self.wrapped.GearSetDesign) if self.wrapped.GearSetDesign else None

    @property
    def gear_set_design_of_type_worm_gear_set_design(self) -> '_715.WormGearSetDesign':
        '''WormGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _715.WormGearSetDesign.TYPE not in self.wrapped.GearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to WormGearSetDesign. Expected: {}.'.format(self.wrapped.GearSetDesign.__class__.__qualname__))

        return constructor.new(_715.WormGearSetDesign)(self.wrapped.GearSetDesign) if self.wrapped.GearSetDesign else None

    @property
    def gear_set_design_of_type_straight_bevel_diff_gear_set_design(self) -> '_719.StraightBevelDiffGearSetDesign':
        '''StraightBevelDiffGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _719.StraightBevelDiffGearSetDesign.TYPE not in self.wrapped.GearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to StraightBevelDiffGearSetDesign. Expected: {}.'.format(self.wrapped.GearSetDesign.__class__.__qualname__))

        return constructor.new(_719.StraightBevelDiffGearSetDesign)(self.wrapped.GearSetDesign) if self.wrapped.GearSetDesign else None

    @property
    def gear_set_design_of_type_straight_bevel_gear_set_design(self) -> '_723.StraightBevelGearSetDesign':
        '''StraightBevelGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _723.StraightBevelGearSetDesign.TYPE not in self.wrapped.GearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to StraightBevelGearSetDesign. Expected: {}.'.format(self.wrapped.GearSetDesign.__class__.__qualname__))

        return constructor.new(_723.StraightBevelGearSetDesign)(self.wrapped.GearSetDesign) if self.wrapped.GearSetDesign else None

    @property
    def gear_set_design_of_type_spiral_bevel_gear_set_design(self) -> '_727.SpiralBevelGearSetDesign':
        '''SpiralBevelGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _727.SpiralBevelGearSetDesign.TYPE not in self.wrapped.GearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to SpiralBevelGearSetDesign. Expected: {}.'.format(self.wrapped.GearSetDesign.__class__.__qualname__))

        return constructor.new(_727.SpiralBevelGearSetDesign)(self.wrapped.GearSetDesign) if self.wrapped.GearSetDesign else None

    @property
    def gear_set_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_design(self) -> '_731.KlingelnbergCycloPalloidSpiralBevelGearSetDesign':
        '''KlingelnbergCycloPalloidSpiralBevelGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _731.KlingelnbergCycloPalloidSpiralBevelGearSetDesign.TYPE not in self.wrapped.GearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to KlingelnbergCycloPalloidSpiralBevelGearSetDesign. Expected: {}.'.format(self.wrapped.GearSetDesign.__class__.__qualname__))

        return constructor.new(_731.KlingelnbergCycloPalloidSpiralBevelGearSetDesign)(self.wrapped.GearSetDesign) if self.wrapped.GearSetDesign else None

    @property
    def gear_set_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set_design(self) -> '_735.KlingelnbergCycloPalloidHypoidGearSetDesign':
        '''KlingelnbergCycloPalloidHypoidGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _735.KlingelnbergCycloPalloidHypoidGearSetDesign.TYPE not in self.wrapped.GearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to KlingelnbergCycloPalloidHypoidGearSetDesign. Expected: {}.'.format(self.wrapped.GearSetDesign.__class__.__qualname__))

        return constructor.new(_735.KlingelnbergCycloPalloidHypoidGearSetDesign)(self.wrapped.GearSetDesign) if self.wrapped.GearSetDesign else None

    @property
    def gear_set_design_of_type_klingelnberg_conical_gear_set_design(self) -> '_739.KlingelnbergConicalGearSetDesign':
        '''KlingelnbergConicalGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _739.KlingelnbergConicalGearSetDesign.TYPE not in self.wrapped.GearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to KlingelnbergConicalGearSetDesign. Expected: {}.'.format(self.wrapped.GearSetDesign.__class__.__qualname__))

        return constructor.new(_739.KlingelnbergConicalGearSetDesign)(self.wrapped.GearSetDesign) if self.wrapped.GearSetDesign else None

    @property
    def gear_set_design_of_type_hypoid_gear_set_design(self) -> '_743.HypoidGearSetDesign':
        '''HypoidGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _743.HypoidGearSetDesign.TYPE not in self.wrapped.GearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to HypoidGearSetDesign. Expected: {}.'.format(self.wrapped.GearSetDesign.__class__.__qualname__))

        return constructor.new(_743.HypoidGearSetDesign)(self.wrapped.GearSetDesign) if self.wrapped.GearSetDesign else None

    @property
    def gear_set_design_of_type_face_gear_set_design(self) -> '_751.FaceGearSetDesign':
        '''FaceGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _751.FaceGearSetDesign.TYPE not in self.wrapped.GearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to FaceGearSetDesign. Expected: {}.'.format(self.wrapped.GearSetDesign.__class__.__qualname__))

        return constructor.new(_751.FaceGearSetDesign)(self.wrapped.GearSetDesign) if self.wrapped.GearSetDesign else None

    @property
    def gear_set_design_of_type_cylindrical_gear_set_design(self) -> '_778.CylindricalGearSetDesign':
        '''CylindricalGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _778.CylindricalGearSetDesign.TYPE not in self.wrapped.GearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to CylindricalGearSetDesign. Expected: {}.'.format(self.wrapped.GearSetDesign.__class__.__qualname__))

        return constructor.new(_778.CylindricalGearSetDesign)(self.wrapped.GearSetDesign) if self.wrapped.GearSetDesign else None

    @property
    def gear_set_design_of_type_cylindrical_planetary_gear_set_design(self) -> '_787.CylindricalPlanetaryGearSetDesign':
        '''CylindricalPlanetaryGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _787.CylindricalPlanetaryGearSetDesign.TYPE not in self.wrapped.GearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to CylindricalPlanetaryGearSetDesign. Expected: {}.'.format(self.wrapped.GearSetDesign.__class__.__qualname__))

        return constructor.new(_787.CylindricalPlanetaryGearSetDesign)(self.wrapped.GearSetDesign) if self.wrapped.GearSetDesign else None

    @property
    def gear_set_design_of_type_conical_gear_set_design(self) -> '_881.ConicalGearSetDesign':
        '''ConicalGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _881.ConicalGearSetDesign.TYPE not in self.wrapped.GearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to ConicalGearSetDesign. Expected: {}.'.format(self.wrapped.GearSetDesign.__class__.__qualname__))

        return constructor.new(_881.ConicalGearSetDesign)(self.wrapped.GearSetDesign) if self.wrapped.GearSetDesign else None

    @property
    def gear_set_design_of_type_concept_gear_set_design(self) -> '_903.ConceptGearSetDesign':
        '''ConceptGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _903.ConceptGearSetDesign.TYPE not in self.wrapped.GearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to ConceptGearSetDesign. Expected: {}.'.format(self.wrapped.GearSetDesign.__class__.__qualname__))

        return constructor.new(_903.ConceptGearSetDesign)(self.wrapped.GearSetDesign) if self.wrapped.GearSetDesign else None

    @property
    def gear_set_design_of_type_bevel_gear_set_design(self) -> '_907.BevelGearSetDesign':
        '''BevelGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _907.BevelGearSetDesign.TYPE not in self.wrapped.GearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to BevelGearSetDesign. Expected: {}.'.format(self.wrapped.GearSetDesign.__class__.__qualname__))

        return constructor.new(_907.BevelGearSetDesign)(self.wrapped.GearSetDesign) if self.wrapped.GearSetDesign else None

    @property
    def gear_set_design_of_type_agma_gleason_conical_gear_set_design(self) -> '_920.AGMAGleasonConicalGearSetDesign':
        '''AGMAGleasonConicalGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _920.AGMAGleasonConicalGearSetDesign.TYPE not in self.wrapped.GearSetDesign.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to AGMAGleasonConicalGearSetDesign. Expected: {}.'.format(self.wrapped.GearSetDesign.__class__.__qualname__))

        return constructor.new(_920.AGMAGleasonConicalGearSetDesign)(self.wrapped.GearSetDesign) if self.wrapped.GearSetDesign else None

    @property
    def gear_ratings(self) -> 'List[_161.GearDutyCycleRating]':
        '''List[GearDutyCycleRating]: 'GearRatings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.GearRatings, constructor.new(_161.GearDutyCycleRating))
        return value

    @property
    def gear_duty_cycle_ratings(self) -> 'List[_161.GearDutyCycleRating]':
        '''List[GearDutyCycleRating]: 'GearDutyCycleRatings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.GearDutyCycleRatings, constructor.new(_161.GearDutyCycleRating))
        return value

    @property
    def gear_mesh_ratings(self) -> 'List[_168.MeshDutyCycleRating]':
        '''List[MeshDutyCycleRating]: 'GearMeshRatings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.GearMeshRatings, constructor.new(_168.MeshDutyCycleRating))
        return value

    @property
    def gear_mesh_duty_cycle_ratings(self) -> 'List[_168.MeshDutyCycleRating]':
        '''List[MeshDutyCycleRating]: 'GearMeshDutyCycleRatings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.GearMeshDutyCycleRatings, constructor.new(_168.MeshDutyCycleRating))
        return value
