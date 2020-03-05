'''_5258.py

PowerLoadModalAnalysesAtSpeeds
'''


from mastapy.system_model.part_model import _1944
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _2337
from mastapy.system_model.analyses_and_results.modal_analyses_at_speeds_ns import _5292
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_MODAL_ANALYSES_AT_SPEEDS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtSpeedsNS', 'PowerLoadModalAnalysesAtSpeeds')


__docformat__ = 'restructuredtext en'
__all__ = ('PowerLoadModalAnalysesAtSpeeds',)


class PowerLoadModalAnalysesAtSpeeds(_5292.VirtualComponentModalAnalysesAtSpeeds):
    '''PowerLoadModalAnalysesAtSpeeds

    This is a mastapy class.
    '''

    TYPE = _POWER_LOAD_MODAL_ANALYSES_AT_SPEEDS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'PowerLoadModalAnalysesAtSpeeds.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1944.PowerLoad':
        '''PowerLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1944.PowerLoad)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_2337.PowerLoadLoadCase':
        '''PowerLoadLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2337.PowerLoadLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
