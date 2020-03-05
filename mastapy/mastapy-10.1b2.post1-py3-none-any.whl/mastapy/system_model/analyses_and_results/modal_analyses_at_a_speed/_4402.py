'''_4402.py

PulleyModalAnalysisAtASpeed
'''


from mastapy.system_model.part_model.couplings import _2045
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _5991
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _4358
from mastapy._internal.python_net import python_net_import

_PULLEY_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed', 'PulleyModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('PulleyModalAnalysisAtASpeed',)


class PulleyModalAnalysisAtASpeed(_4358.CouplingHalfModalAnalysisAtASpeed):
    '''PulleyModalAnalysisAtASpeed

    This is a mastapy class.
    '''

    TYPE = _PULLEY_MODAL_ANALYSIS_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PulleyModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2045.Pulley':
        '''Pulley: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2045.Pulley)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_5991.PulleyLoadCase':
        '''PulleyLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5991.PulleyLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
