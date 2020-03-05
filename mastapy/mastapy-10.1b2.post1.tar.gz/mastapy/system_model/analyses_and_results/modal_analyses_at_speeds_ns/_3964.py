'''_3964.py

ClutchHalfModalAnalysesAtSpeeds
'''


from mastapy.system_model.part_model.couplings import _2092
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6046
from mastapy.system_model.analyses_and_results.modal_analyses_at_speeds_ns import _3980
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF_MODAL_ANALYSES_AT_SPEEDS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtSpeedsNS', 'ClutchHalfModalAnalysesAtSpeeds')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchHalfModalAnalysesAtSpeeds',)


class ClutchHalfModalAnalysesAtSpeeds(_3980.CouplingHalfModalAnalysesAtSpeeds):
    '''ClutchHalfModalAnalysesAtSpeeds

    This is a mastapy class.
    '''

    TYPE = _CLUTCH_HALF_MODAL_ANALYSES_AT_SPEEDS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ClutchHalfModalAnalysesAtSpeeds.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2092.ClutchHalf':
        '''ClutchHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2092.ClutchHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6046.ClutchHalfLoadCase':
        '''ClutchHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6046.ClutchHalfLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
