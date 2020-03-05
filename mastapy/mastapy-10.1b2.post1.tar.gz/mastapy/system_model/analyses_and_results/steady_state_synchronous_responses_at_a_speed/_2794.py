'''_2794.py

SpringDamperHalfSteadyStateSynchronousResponseAtASpeed
'''


from mastapy.system_model.part_model.couplings import _2112
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6160
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _2735
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed', 'SpringDamperHalfSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperHalfSteadyStateSynchronousResponseAtASpeed',)


class SpringDamperHalfSteadyStateSynchronousResponseAtASpeed(_2735.CouplingHalfSteadyStateSynchronousResponseAtASpeed):
    '''SpringDamperHalfSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    '''

    TYPE = _SPRING_DAMPER_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpringDamperHalfSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2112.SpringDamperHalf':
        '''SpringDamperHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2112.SpringDamperHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6160.SpringDamperHalfLoadCase':
        '''SpringDamperHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6160.SpringDamperHalfLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
