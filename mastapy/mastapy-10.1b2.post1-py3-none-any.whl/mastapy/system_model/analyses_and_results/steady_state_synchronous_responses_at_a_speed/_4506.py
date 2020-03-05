'''_4506.py

RootAssemblySteadyStateSynchronousResponseAtASpeed
'''


from mastapy.system_model.part_model import _1945
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _4517, _4428
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed', 'RootAssemblySteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblySteadyStateSynchronousResponseAtASpeed',)


class RootAssemblySteadyStateSynchronousResponseAtASpeed(_4428.AssemblySteadyStateSynchronousResponseAtASpeed):
    '''RootAssemblySteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    '''

    TYPE = _ROOT_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    __hash__ = None

    def __init__(self, instance_to_wrap: 'RootAssemblySteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_1945.RootAssembly':
        '''RootAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1945.RootAssembly)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def steady_state_synchronous_response_at_a_speed_inputs(self) -> '_4517.SteadyStateSynchronousResponseAtASpeed':
        '''SteadyStateSynchronousResponseAtASpeed: 'SteadyStateSynchronousResponseAtASpeedInputs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_4517.SteadyStateSynchronousResponseAtASpeed)(self.wrapped.SteadyStateSynchronousResponseAtASpeedInputs) if self.wrapped.SteadyStateSynchronousResponseAtASpeedInputs else None
