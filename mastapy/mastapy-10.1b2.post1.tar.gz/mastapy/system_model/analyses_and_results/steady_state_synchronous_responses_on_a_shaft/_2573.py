'''_2573.py

WormGearSetSteadyStateSynchronousResponseOnAShaft
'''


from typing import List

from mastapy.system_model.part_model.gears import _2069
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6189
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _2574, _2572, _2508
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft', 'WormGearSetSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetSteadyStateSynchronousResponseOnAShaft',)


class WormGearSetSteadyStateSynchronousResponseOnAShaft(_2508.GearSetSteadyStateSynchronousResponseOnAShaft):
    '''WormGearSetSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    '''

    TYPE = _WORM_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearSetSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2069.WormGearSet':
        '''WormGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2069.WormGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6189.WormGearSetLoadCase':
        '''WormGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6189.WormGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def worm_gears_steady_state_synchronous_response_on_a_shaft(self) -> 'List[_2574.WormGearSteadyStateSynchronousResponseOnAShaft]':
        '''List[WormGearSteadyStateSynchronousResponseOnAShaft]: 'WormGearsSteadyStateSynchronousResponseOnAShaft' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearsSteadyStateSynchronousResponseOnAShaft, constructor.new(_2574.WormGearSteadyStateSynchronousResponseOnAShaft))
        return value

    @property
    def worm_meshes_steady_state_synchronous_response_on_a_shaft(self) -> 'List[_2572.WormGearMeshSteadyStateSynchronousResponseOnAShaft]':
        '''List[WormGearMeshSteadyStateSynchronousResponseOnAShaft]: 'WormMeshesSteadyStateSynchronousResponseOnAShaft' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormMeshesSteadyStateSynchronousResponseOnAShaft, constructor.new(_2572.WormGearMeshSteadyStateSynchronousResponseOnAShaft))
        return value
