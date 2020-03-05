'''_6046.py

ClutchHalfLoadCase
'''


from mastapy.system_model.part_model.couplings import _2092
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6064
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ClutchHalfLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchHalfLoadCase',)


class ClutchHalfLoadCase(_6064.CouplingHalfLoadCase):
    '''ClutchHalfLoadCase

    This is a mastapy class.
    '''

    TYPE = _CLUTCH_HALF_LOAD_CASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ClutchHalfLoadCase.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2092.ClutchHalf':
        '''ClutchHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2092.ClutchHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None
