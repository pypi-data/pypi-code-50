'''_927.py

GearSetOptimiserCandidate
'''


from typing import Callable

from mastapy._internal import constructor
from mastapy.gears.rating import _334, _341, _342
from mastapy._internal.cast_exception import CastException
from mastapy.gears.rating.zerol_bevel import _361
from mastapy.gears.rating.worm import _382, _383
from mastapy.gears.rating.straight_bevel_diff import _405
from mastapy.gears.rating.straight_bevel import _407
from mastapy.gears.rating.spiral_bevel import _408
from mastapy.gears.rating.klingelnberg_spiral_bevel import _409
from mastapy.gears.rating.klingelnberg_hypoid import _410
from mastapy.gears.rating.klingelnberg_conical import _411
from mastapy.gears.rating.hypoid import _412
from mastapy.gears.rating.face import _413, _414
from mastapy.gears.rating.cylindrical import _415, _416
from mastapy.gears.rating.conical import _417, _418
from mastapy.gears.rating.concept import _419, _420
from mastapy.gears.rating.bevel import _421
from mastapy.gears.rating.agma_gleason_conical import _422
from mastapy.gears.gear_set_pareto_optimiser import _923
from mastapy._internal.python_net import python_net_import

_GEAR_SET_OPTIMISER_CANDIDATE = python_net_import('SMT.MastaAPI.Gears.GearSetParetoOptimiser', 'GearSetOptimiserCandidate')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetOptimiserCandidate',)


class GearSetOptimiserCandidate(_923.DesignSpaceSearchCandidateBase['_334.AbstractGearSetRating', 'GearSetOptimiserCandidate']):
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
    def candidate(self) -> '_334.AbstractGearSetRating':
        '''AbstractGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_334.AbstractGearSetRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_gear_set_duty_cycle_rating(self) -> '_341.GearSetDutyCycleRating':
        '''GearSetDutyCycleRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _341.GearSetDutyCycleRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to GearSetDutyCycleRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_341.GearSetDutyCycleRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_gear_set_rating(self) -> '_342.GearSetRating':
        '''GearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _342.GearSetRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to GearSetRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_342.GearSetRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_zerol_bevel_gear_set_rating(self) -> '_361.ZerolBevelGearSetRating':
        '''ZerolBevelGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _361.ZerolBevelGearSetRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to ZerolBevelGearSetRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_361.ZerolBevelGearSetRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_worm_gear_set_duty_cycle_rating(self) -> '_382.WormGearSetDutyCycleRating':
        '''WormGearSetDutyCycleRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _382.WormGearSetDutyCycleRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to WormGearSetDutyCycleRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_382.WormGearSetDutyCycleRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_worm_gear_set_rating(self) -> '_383.WormGearSetRating':
        '''WormGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _383.WormGearSetRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to WormGearSetRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_383.WormGearSetRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_straight_bevel_diff_gear_set_rating(self) -> '_405.StraightBevelDiffGearSetRating':
        '''StraightBevelDiffGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _405.StraightBevelDiffGearSetRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to StraightBevelDiffGearSetRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_405.StraightBevelDiffGearSetRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_straight_bevel_gear_set_rating(self) -> '_407.StraightBevelGearSetRating':
        '''StraightBevelGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _407.StraightBevelGearSetRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to StraightBevelGearSetRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_407.StraightBevelGearSetRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_spiral_bevel_gear_set_rating(self) -> '_408.SpiralBevelGearSetRating':
        '''SpiralBevelGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _408.SpiralBevelGearSetRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to SpiralBevelGearSetRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_408.SpiralBevelGearSetRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_rating(self) -> '_409.KlingelnbergCycloPalloidSpiralBevelGearSetRating':
        '''KlingelnbergCycloPalloidSpiralBevelGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _409.KlingelnbergCycloPalloidSpiralBevelGearSetRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to KlingelnbergCycloPalloidSpiralBevelGearSetRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_409.KlingelnbergCycloPalloidSpiralBevelGearSetRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set_rating(self) -> '_410.KlingelnbergCycloPalloidHypoidGearSetRating':
        '''KlingelnbergCycloPalloidHypoidGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _410.KlingelnbergCycloPalloidHypoidGearSetRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to KlingelnbergCycloPalloidHypoidGearSetRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_410.KlingelnbergCycloPalloidHypoidGearSetRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_klingelnberg_cyclo_palloid_conical_gear_set_rating(self) -> '_411.KlingelnbergCycloPalloidConicalGearSetRating':
        '''KlingelnbergCycloPalloidConicalGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _411.KlingelnbergCycloPalloidConicalGearSetRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to KlingelnbergCycloPalloidConicalGearSetRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_411.KlingelnbergCycloPalloidConicalGearSetRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_hypoid_gear_set_rating(self) -> '_412.HypoidGearSetRating':
        '''HypoidGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _412.HypoidGearSetRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to HypoidGearSetRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_412.HypoidGearSetRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_face_gear_set_duty_cycle_rating(self) -> '_413.FaceGearSetDutyCycleRating':
        '''FaceGearSetDutyCycleRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _413.FaceGearSetDutyCycleRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to FaceGearSetDutyCycleRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_413.FaceGearSetDutyCycleRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_face_gear_set_rating(self) -> '_414.FaceGearSetRating':
        '''FaceGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _414.FaceGearSetRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to FaceGearSetRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_414.FaceGearSetRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_cylindrical_gear_set_duty_cycle_rating(self) -> '_415.CylindricalGearSetDutyCycleRating':
        '''CylindricalGearSetDutyCycleRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _415.CylindricalGearSetDutyCycleRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to CylindricalGearSetDutyCycleRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_415.CylindricalGearSetDutyCycleRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_cylindrical_gear_set_rating(self) -> '_416.CylindricalGearSetRating':
        '''CylindricalGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _416.CylindricalGearSetRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to CylindricalGearSetRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_416.CylindricalGearSetRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_conical_gear_set_duty_cycle_rating(self) -> '_417.ConicalGearSetDutyCycleRating':
        '''ConicalGearSetDutyCycleRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _417.ConicalGearSetDutyCycleRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to ConicalGearSetDutyCycleRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_417.ConicalGearSetDutyCycleRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_conical_gear_set_rating(self) -> '_418.ConicalGearSetRating':
        '''ConicalGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _418.ConicalGearSetRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to ConicalGearSetRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_418.ConicalGearSetRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_concept_gear_set_duty_cycle_rating(self) -> '_419.ConceptGearSetDutyCycleRating':
        '''ConceptGearSetDutyCycleRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _419.ConceptGearSetDutyCycleRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to ConceptGearSetDutyCycleRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_419.ConceptGearSetDutyCycleRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_concept_gear_set_rating(self) -> '_420.ConceptGearSetRating':
        '''ConceptGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _420.ConceptGearSetRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to ConceptGearSetRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_420.ConceptGearSetRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_bevel_gear_set_rating(self) -> '_421.BevelGearSetRating':
        '''BevelGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _421.BevelGearSetRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to BevelGearSetRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_421.BevelGearSetRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None

    @property
    def candidate_of_type_agma_gleason_conical_gear_set_rating(self) -> '_422.AGMAGleasonConicalGearSetRating':
        '''AGMAGleasonConicalGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _422.AGMAGleasonConicalGearSetRating.TYPE not in self.wrapped.Candidate.__class__.__mro__:
            raise CastException('Failed to cast candidate to AGMAGleasonConicalGearSetRating. Expected: {}.'.format(self.wrapped.Candidate.__class__.__qualname__))

        return constructor.new(_422.AGMAGleasonConicalGearSetRating)(self.wrapped.Candidate) if self.wrapped.Candidate else None
