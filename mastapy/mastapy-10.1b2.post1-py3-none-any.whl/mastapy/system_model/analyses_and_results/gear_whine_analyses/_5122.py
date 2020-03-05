'''_5122.py

ClutchHalfGearWhineAnalysis
'''


from mastapy.system_model.part_model.couplings import _2037
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _5898
from mastapy.system_model.analyses_and_results.system_deflections import _2148
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _5139
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'ClutchHalfGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchHalfGearWhineAnalysis',)


class ClutchHalfGearWhineAnalysis(_5139.CouplingHalfGearWhineAnalysis):
    '''ClutchHalfGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _CLUTCH_HALF_GEAR_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ClutchHalfGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2037.ClutchHalf':
        '''ClutchHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2037.ClutchHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_5898.ClutchHalfLoadCase':
        '''ClutchHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5898.ClutchHalfLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def system_deflection_results(self) -> '_2148.ClutchHalfSystemDeflection':
        '''ClutchHalfSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2148.ClutchHalfSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
