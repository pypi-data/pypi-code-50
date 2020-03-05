'''_4748.py

ShaftSteadyStateSynchronousResponse
'''


from typing import List

from mastapy.system_model.part_model.shaft_model import _1952
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _2345
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _4663
from mastapy._internal.python_net import python_net_import

_SHAFT_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'ShaftSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftSteadyStateSynchronousResponse',)


class ShaftSteadyStateSynchronousResponse(_4663.AbstractShaftOrHousingSteadyStateSynchronousResponse):
    '''ShaftSteadyStateSynchronousResponse

    This is a mastapy class.
    '''

    TYPE = _SHAFT_STEADY_STATE_SYNCHRONOUS_RESPONSE
    __hash__ = None

    def __init__(self, instance_to_wrap: 'ShaftSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1952.Shaft':
        '''Shaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1952.Shaft)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_2345.ShaftLoadCase':
        '''ShaftLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2345.ShaftLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def planetaries(self) -> 'List[ShaftSteadyStateSynchronousResponse]':
        '''List[ShaftSteadyStateSynchronousResponse]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(ShaftSteadyStateSynchronousResponse))
        return value
