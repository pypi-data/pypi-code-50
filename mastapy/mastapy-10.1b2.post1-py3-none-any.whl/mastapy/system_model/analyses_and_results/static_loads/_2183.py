'''_2183.py

ClutchLoadCase
'''


from mastapy.system_model.part_model.couplings import _2046
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _2188
from mastapy._internal.python_net import python_net_import

_CLUTCH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ClutchLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchLoadCase',)


class ClutchLoadCase(_2188.CouplingLoadCase):
    '''ClutchLoadCase

    This is a mastapy class.
    '''

    TYPE = _CLUTCH_LOAD_CASE
    __hash__ = None

    def __init__(self, instance_to_wrap: 'ClutchLoadCase.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2046.Clutch':
        '''Clutch: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2046.Clutch)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None
