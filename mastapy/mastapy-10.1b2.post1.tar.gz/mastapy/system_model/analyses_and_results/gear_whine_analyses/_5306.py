'''_5306.py

HypoidGearGearWhineAnalysis
'''


from mastapy.system_model.part_model.gears import _2051
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6111
from mastapy.system_model.analyses_and_results.system_deflections import _2251
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _5233
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'HypoidGearGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearGearWhineAnalysis',)


class HypoidGearGearWhineAnalysis(_5233.AGMAGleasonConicalGearGearWhineAnalysis):
    '''HypoidGearGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _HYPOID_GEAR_GEAR_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2051.HypoidGear':
        '''HypoidGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2051.HypoidGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6111.HypoidGearLoadCase':
        '''HypoidGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6111.HypoidGearLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def system_deflection_results(self) -> '_2251.HypoidGearSystemDeflection':
        '''HypoidGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2251.HypoidGearSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
