'''_3132.py

KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse
'''


from typing import List

from mastapy.system_model.part_model.gears import _2056
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3130, _3131, _3129
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3007
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound', 'KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse',)


class KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse(_3129.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponse):
    '''KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    '''

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2056.KlingelnbergCycloPalloidHypoidGearSet':
        '''KlingelnbergCycloPalloidHypoidGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2056.KlingelnbergCycloPalloidHypoidGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def assembly_design(self) -> '_2056.KlingelnbergCycloPalloidHypoidGearSet':
        '''KlingelnbergCycloPalloidHypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2056.KlingelnbergCycloPalloidHypoidGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_compound_steady_state_synchronous_response(self) -> 'List[_3130.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponse]':
        '''List[KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponse]: 'KlingelnbergCycloPalloidHypoidGearsCompoundSteadyStateSynchronousResponse' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearsCompoundSteadyStateSynchronousResponse, constructor.new(_3130.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponse))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_compound_steady_state_synchronous_response(self) -> 'List[_3131.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse]':
        '''List[KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse]: 'KlingelnbergCycloPalloidHypoidMeshesCompoundSteadyStateSynchronousResponse' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidMeshesCompoundSteadyStateSynchronousResponse, constructor.new(_3131.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse))
        return value

    @property
    def load_case_analyses_ready(self) -> 'List[_3007.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_3007.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse))
        return value

    @property
    def assembly_steady_state_synchronous_response_load_cases(self) -> 'List[_3007.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse]: 'AssemblySteadyStateSynchronousResponseLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblySteadyStateSynchronousResponseLoadCases, constructor.new(_3007.KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse))
        return value
