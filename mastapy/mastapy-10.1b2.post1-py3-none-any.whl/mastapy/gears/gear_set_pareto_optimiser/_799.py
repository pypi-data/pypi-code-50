'''_799.py

GearSetOptimiserCandidate
'''


from typing import Callable

from mastapy._internal import constructor
from mastapy.gears.rating import _284, _291, _292
from mastapy._internal.cast_exception import CastException
from mastapy.gears.rating.zerol_bevel import _300
from mastapy.gears.rating.worm import _304, _305
from mastapy.gears.rating.straight_bevel_diff import _326
from mastapy.gears.rating.straight_bevel import _330
from mastapy.gears.rating.spiral_bevel import _333
from mastapy.gears.rating.klingelnberg_spiral_bevel import _336
from mastapy.gears.rating.klingelnberg_hypoid import _339
from mastapy.gears.rating.klingelnberg_conical import _342
from mastapy.gears.rating.hypoid import _369
from mastapy.gears.rating.face import _378, _379
from mastapy.gears.rating.cylindrical import _390, _391
from mastapy.gears.rating.conical import _451, _452
from mastapy.gears.rating.concept import _462, _463
from mastapy.gears.rating.bevel import _466
from mastapy.gears.rating.agma_gleason_conical import _477
from mastapy.gears.gear_set_pareto_optimiser import _795
from mastapy._internal.python_net import python_net_import

_GEAR_SET_OPTIMISER_CANDIDATE = python_net_import('SMT.MastaAPI.Gears.GearSetParetoOptimiser', 'GearSetOptimiserCandidate')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetOptimiserCandidate',)


class GearSetOptimiserCandidate(_795.DesignSpaceSearchCandidateBase['_284.AbstractGearSetRating', 'GearSetOptimiserCandidate']):
    '''GearSetOptimiserCandidate

    This is a mastapy class.
    '''

    TYPE = _GEAR_SET_OPTIMISER_CANDIDATE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearSetOptimiserCandidate.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def add_design(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'AddDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AddDesign

    @property
    def candidate(self) -> '_284.AbstractGearSetRating':
        '''AbstractGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_284.AbstractGearSetRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_gear_set_duty_cycle_rating(self) -> '_291.GearSetDutyCycleRating':
        '''GearSetDutyCycleRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _291.GearSetDutyCycleRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to GearSetDutyCycleRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_291.GearSetDutyCycleRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_gear_set_rating(self) -> '_292.GearSetRating':
        '''GearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _292.GearSetRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to GearSetRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_292.GearSetRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_zerol_bevel_gear_set_rating(self) -> '_300.ZerolBevelGearSetRating':
        '''ZerolBevelGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _300.ZerolBevelGearSetRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to ZerolBevelGearSetRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_300.ZerolBevelGearSetRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_worm_gear_set_duty_cycle_rating(self) -> '_304.WormGearSetDutyCycleRating':
        '''WormGearSetDutyCycleRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _304.WormGearSetDutyCycleRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to WormGearSetDutyCycleRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_304.WormGearSetDutyCycleRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_worm_gear_set_rating(self) -> '_305.WormGearSetRating':
        '''WormGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _305.WormGearSetRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to WormGearSetRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_305.WormGearSetRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_straight_bevel_diff_gear_set_rating(self) -> '_326.StraightBevelDiffGearSetRating':
        '''StraightBevelDiffGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _326.StraightBevelDiffGearSetRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to StraightBevelDiffGearSetRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_326.StraightBevelDiffGearSetRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_straight_bevel_gear_set_rating(self) -> '_330.StraightBevelGearSetRating':
        '''StraightBevelGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _330.StraightBevelGearSetRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to StraightBevelGearSetRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_330.StraightBevelGearSetRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_spiral_bevel_gear_set_rating(self) -> '_333.SpiralBevelGearSetRating':
        '''SpiralBevelGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _333.SpiralBevelGearSetRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to SpiralBevelGearSetRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_333.SpiralBevelGearSetRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_rating(self) -> '_336.KlingelnbergCycloPalloidSpiralBevelGearSetRating':
        '''KlingelnbergCycloPalloidSpiralBevelGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _336.KlingelnbergCycloPalloidSpiralBevelGearSetRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to KlingelnbergCycloPalloidSpiralBevelGearSetRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_336.KlingelnbergCycloPalloidSpiralBevelGearSetRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set_rating(self) -> '_339.KlingelnbergCycloPalloidHypoidGearSetRating':
        '''KlingelnbergCycloPalloidHypoidGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _339.KlingelnbergCycloPalloidHypoidGearSetRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to KlingelnbergCycloPalloidHypoidGearSetRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_339.KlingelnbergCycloPalloidHypoidGearSetRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_klingelnberg_cyclo_palloid_conical_gear_set_rating(self) -> '_342.KlingelnbergCycloPalloidConicalGearSetRating':
        '''KlingelnbergCycloPalloidConicalGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _342.KlingelnbergCycloPalloidConicalGearSetRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to KlingelnbergCycloPalloidConicalGearSetRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_342.KlingelnbergCycloPalloidConicalGearSetRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_hypoid_gear_set_rating(self) -> '_369.HypoidGearSetRating':
        '''HypoidGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _369.HypoidGearSetRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to HypoidGearSetRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_369.HypoidGearSetRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_face_gear_set_duty_cycle_rating(self) -> '_378.FaceGearSetDutyCycleRating':
        '''FaceGearSetDutyCycleRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _378.FaceGearSetDutyCycleRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to FaceGearSetDutyCycleRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_378.FaceGearSetDutyCycleRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_face_gear_set_rating(self) -> '_379.FaceGearSetRating':
        '''FaceGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _379.FaceGearSetRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to FaceGearSetRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_379.FaceGearSetRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_cylindrical_gear_set_duty_cycle_rating(self) -> '_390.CylindricalGearSetDutyCycleRating':
        '''CylindricalGearSetDutyCycleRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _390.CylindricalGearSetDutyCycleRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to CylindricalGearSetDutyCycleRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_390.CylindricalGearSetDutyCycleRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_cylindrical_gear_set_rating(self) -> '_391.CylindricalGearSetRating':
        '''CylindricalGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _391.CylindricalGearSetRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to CylindricalGearSetRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_391.CylindricalGearSetRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_conical_gear_set_duty_cycle_rating(self) -> '_451.ConicalGearSetDutyCycleRating':
        '''ConicalGearSetDutyCycleRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _451.ConicalGearSetDutyCycleRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to ConicalGearSetDutyCycleRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_451.ConicalGearSetDutyCycleRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_conical_gear_set_rating(self) -> '_452.ConicalGearSetRating':
        '''ConicalGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _452.ConicalGearSetRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to ConicalGearSetRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_452.ConicalGearSetRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_concept_gear_set_duty_cycle_rating(self) -> '_462.ConceptGearSetDutyCycleRating':
        '''ConceptGearSetDutyCycleRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _462.ConceptGearSetDutyCycleRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to ConceptGearSetDutyCycleRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_462.ConceptGearSetDutyCycleRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_concept_gear_set_rating(self) -> '_463.ConceptGearSetRating':
        '''ConceptGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _463.ConceptGearSetRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to ConceptGearSetRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_463.ConceptGearSetRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_bevel_gear_set_rating(self) -> '_466.BevelGearSetRating':
        '''BevelGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _466.BevelGearSetRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to BevelGearSetRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_466.BevelGearSetRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_agma_gleason_conical_gear_set_rating(self) -> '_477.AGMAGleasonConicalGearSetRating':
        '''AGMAGleasonConicalGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _477.AGMAGleasonConicalGearSetRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to AGMAGleasonConicalGearSetRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_477.AGMAGleasonConicalGearSetRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None
