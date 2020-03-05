'''_2798.py

StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed
'''


from typing import List

from mastapy.system_model.part_model.gears import _2063
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6165
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _2799, _2797, _2714
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed', 'StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed',)


class StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed(_2714.BevelGearSetSteadyStateSynchronousResponseAtASpeed):
    '''StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    '''

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2063.StraightBevelDiffGearSet':
        '''StraightBevelDiffGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2063.StraightBevelDiffGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6165.StraightBevelDiffGearSetLoadCase':
        '''StraightBevelDiffGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6165.StraightBevelDiffGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def straight_bevel_diff_gears_steady_state_synchronous_response_at_a_speed(self) -> 'List[_2799.StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed]':
        '''List[StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed]: 'StraightBevelDiffGearsSteadyStateSynchronousResponseAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearsSteadyStateSynchronousResponseAtASpeed, constructor.new(_2799.StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed))
        return value

    @property
    def straight_bevel_diff_meshes_steady_state_synchronous_response_at_a_speed(self) -> 'List[_2797.StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed]':
        '''List[StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed]: 'StraightBevelDiffMeshesSteadyStateSynchronousResponseAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffMeshesSteadyStateSynchronousResponseAtASpeed, constructor.new(_2797.StraightBevelDiffGearMeshSteadyStateSynchronousResponseAtASpeed))
        return value
