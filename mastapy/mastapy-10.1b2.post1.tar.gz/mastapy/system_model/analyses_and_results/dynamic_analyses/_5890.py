'''_5890.py

WormGearDynamicAnalysis
'''


from mastapy.system_model.part_model.gears import _2068
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6187
from mastapy.system_model.analyses_and_results.dynamic_analyses import _5826
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'WormGearDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearDynamicAnalysis',)


class WormGearDynamicAnalysis(_5826.GearDynamicAnalysis):
    '''WormGearDynamicAnalysis

    This is a mastapy class.
    '''

    TYPE = _WORM_GEAR_DYNAMIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2068.WormGear':
        '''WormGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2068.WormGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6187.WormGearLoadCase':
        '''WormGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6187.WormGearLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None
