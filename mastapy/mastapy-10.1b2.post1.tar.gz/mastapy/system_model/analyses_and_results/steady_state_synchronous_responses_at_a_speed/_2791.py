'''_2791.py

SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed
'''


from typing import List

from mastapy.system_model.part_model.gears import _2061
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6158
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _2792, _2790, _2714
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed', 'SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed',)


class SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed(_2714.BevelGearSetSteadyStateSynchronousResponseAtASpeed):
    '''SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    '''

    TYPE = _SPIRAL_BEVEL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearSetSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2061.SpiralBevelGearSet':
        '''SpiralBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2061.SpiralBevelGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6158.SpiralBevelGearSetLoadCase':
        '''SpiralBevelGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6158.SpiralBevelGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def spiral_bevel_gears_steady_state_synchronous_response_at_a_speed(self) -> 'List[_2792.SpiralBevelGearSteadyStateSynchronousResponseAtASpeed]':
        '''List[SpiralBevelGearSteadyStateSynchronousResponseAtASpeed]: 'SpiralBevelGearsSteadyStateSynchronousResponseAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearsSteadyStateSynchronousResponseAtASpeed, constructor.new(_2792.SpiralBevelGearSteadyStateSynchronousResponseAtASpeed))
        return value

    @property
    def spiral_bevel_meshes_steady_state_synchronous_response_at_a_speed(self) -> 'List[_2790.SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed]':
        '''List[SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed]: 'SpiralBevelMeshesSteadyStateSynchronousResponseAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelMeshesSteadyStateSynchronousResponseAtASpeed, constructor.new(_2790.SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed))
        return value
