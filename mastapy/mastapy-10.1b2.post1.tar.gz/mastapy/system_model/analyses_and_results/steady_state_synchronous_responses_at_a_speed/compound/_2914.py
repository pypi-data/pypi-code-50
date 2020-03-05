'''_2914.py

SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
'''


from typing import List

from mastapy.system_model.part_model.gears import _2061
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _2912, _2913, _2837
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _2791
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound', 'SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed',)


class SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed(_2837.BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed):
    '''SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    '''

    TYPE = _SPIRAL_BEVEL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2061.SpiralBevelGearSet':
        '''SpiralBevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2061.SpiralBevelGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def assembly_design(self) -> '_2061.SpiralBevelGearSet':
        '''SpiralBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2061.SpiralBevelGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def spiral_bevel_gears_compound_steady_state_synchronous_response_at_a_speed(self) -> 'List[_2912.SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed]':
        '''List[SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed]: 'SpiralBevelGearsCompoundSteadyStateSynchronousResponseAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearsCompoundSteadyStateSynchronousResponseAtASpeed, constructor.new(_2912.SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed))
        return value

    @property
    def spiral_bevel_meshes_compound_steady_state_synchronous_response_at_a_speed(self) -> 'List[_2913.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed]':
        '''List[SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed]: 'SpiralBevelMeshesCompoundSteadyStateSynchronousResponseAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelMeshesCompoundSteadyStateSynchronousResponseAtASpeed, constructor.new(_2913.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed))
        return value

    @property
    def load_case_analyses_ready(self) -> 'List[_2791.SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed]':
        '''List[SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_2791.SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed))
        return value

    @property
    def assembly_steady_state_synchronous_response_at_a_speed_load_cases(self) -> 'List[_2791.SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed]':
        '''List[SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed]: 'AssemblySteadyStateSynchronousResponseAtASpeedLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblySteadyStateSynchronousResponseAtASpeedLoadCases, constructor.new(_2791.SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed))
        return value
