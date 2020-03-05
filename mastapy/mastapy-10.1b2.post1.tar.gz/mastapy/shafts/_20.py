'''_20.py

ShaftDamageResults
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.math_utility import _1078
from mastapy.shafts import _37, _38, _36
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_SHAFT_DAMAGE_RESULTS = python_net_import('SMT.MastaAPI.Shafts', 'ShaftDamageResults')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftDamageResults',)


class ShaftDamageResults(_1.APIBase):
    '''ShaftDamageResults

    This is a mastapy class.
    '''

    TYPE = _SHAFT_DAMAGE_RESULTS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ShaftDamageResults.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def worst_static_safety_factor(self) -> 'float':
        '''float: 'WorstStaticSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.WorstStaticSafetyFactor

    @property
    def worst_fatigue_safety_factor(self) -> 'float':
        '''float: 'WorstFatigueSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.WorstFatigueSafetyFactor

    @property
    def worst_fatigue_safety_factor_for_infinite_life(self) -> 'float':
        '''float: 'WorstFatigueSafetyFactorForInfiniteLife' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.WorstFatigueSafetyFactorForInfiniteLife

    @property
    def worst_reliability_for_finite_life(self) -> 'float':
        '''float: 'WorstReliabilityForFiniteLife' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.WorstReliabilityForFiniteLife

    @property
    def worst_reliability_for_infinite_life(self) -> 'float':
        '''float: 'WorstReliabilityForInfiniteLife' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.WorstReliabilityForInfiniteLife

    @property
    def worst_fatigue_damage(self) -> 'float':
        '''float: 'WorstFatigueDamage' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.WorstFatigueDamage

    @property
    def displacement_linear(self) -> 'List[_1078.Vector4D]':
        '''List[Vector4D]: 'DisplacementLinear' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.DisplacementLinear, constructor.new(_1078.Vector4D))
        return value

    @property
    def displacement_angular(self) -> 'List[_1078.Vector4D]':
        '''List[Vector4D]: 'DisplacementAngular' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.DisplacementAngular, constructor.new(_1078.Vector4D))
        return value

    @property
    def displacement_maximum_radial_magnitude(self) -> 'float':
        '''float: 'DisplacementMaximumRadialMagnitude' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.DisplacementMaximumRadialMagnitude

    @property
    def force_linear(self) -> 'List[_1078.Vector4D]':
        '''List[Vector4D]: 'ForceLinear' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ForceLinear, constructor.new(_1078.Vector4D))
        return value

    @property
    def force_angular(self) -> 'List[_1078.Vector4D]':
        '''List[Vector4D]: 'ForceAngular' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ForceAngular, constructor.new(_1078.Vector4D))
        return value

    @property
    def stress_highest_equivalent_fully_reversed(self) -> 'float':
        '''float: 'StressHighestEquivalentFullyReversed' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.StressHighestEquivalentFullyReversed

    @property
    def load_case_name(self) -> 'str':
        '''str: 'LoadCaseName' is the original name of this property.'''

        return self.wrapped.LoadCaseName

    @load_case_name.setter
    def load_case_name(self, value: 'str'):
        self.wrapped.LoadCaseName = str(value) if value else None

    @property
    def shaft_section_end_with_worst_static_safety_factor(self) -> '_37.ShaftSectionEndDamageResults':
        '''ShaftSectionEndDamageResults: 'ShaftSectionEndWithWorstStaticSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_37.ShaftSectionEndDamageResults)(self.wrapped.ShaftSectionEndWithWorstStaticSafetyFactor) if self.wrapped.ShaftSectionEndWithWorstStaticSafetyFactor else None

    @property
    def shaft_section_end_with_worst_fatigue_safety_factor(self) -> '_37.ShaftSectionEndDamageResults':
        '''ShaftSectionEndDamageResults: 'ShaftSectionEndWithWorstFatigueSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_37.ShaftSectionEndDamageResults)(self.wrapped.ShaftSectionEndWithWorstFatigueSafetyFactor) if self.wrapped.ShaftSectionEndWithWorstFatigueSafetyFactor else None

    @property
    def shaft_section_end_with_worst_fatigue_safety_factor_for_infinite_life(self) -> '_37.ShaftSectionEndDamageResults':
        '''ShaftSectionEndDamageResults: 'ShaftSectionEndWithWorstFatigueSafetyFactorForInfiniteLife' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_37.ShaftSectionEndDamageResults)(self.wrapped.ShaftSectionEndWithWorstFatigueSafetyFactorForInfiniteLife) if self.wrapped.ShaftSectionEndWithWorstFatigueSafetyFactorForInfiniteLife else None

    @property
    def shaft_settings(self) -> '_38.ShaftSettings':
        '''ShaftSettings: 'ShaftSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_38.ShaftSettings)(self.wrapped.ShaftSettings) if self.wrapped.ShaftSettings else None

    @property
    def shaft_section_damage_results(self) -> 'List[_36.ShaftSectionDamageResults]':
        '''List[ShaftSectionDamageResults]: 'ShaftSectionDamageResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftSectionDamageResults, constructor.new(_36.ShaftSectionDamageResults))
        return value

    @property
    def shaft_section_end_results_by_offset_with_worst_safety_factor(self) -> 'List[_37.ShaftSectionEndDamageResults]':
        '''List[ShaftSectionEndDamageResults]: 'ShaftSectionEndResultsByOffsetWithWorstSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftSectionEndResultsByOffsetWithWorstSafetyFactor, constructor.new(_37.ShaftSectionEndDamageResults))
        return value
