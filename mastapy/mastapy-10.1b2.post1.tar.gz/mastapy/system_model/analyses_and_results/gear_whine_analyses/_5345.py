'''_5345.py

SpiralBevelGearGearWhineAnalysis
'''


from mastapy.system_model.part_model.gears import _2060
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6156
from mastapy.system_model.analyses_and_results.system_deflections import _2291
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _5245
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'SpiralBevelGearGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearGearWhineAnalysis',)


class SpiralBevelGearGearWhineAnalysis(_5245.BevelGearGearWhineAnalysis):
    '''SpiralBevelGearGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _SPIRAL_BEVEL_GEAR_GEAR_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2060.SpiralBevelGear':
        '''SpiralBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2060.SpiralBevelGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_6156.SpiralBevelGearLoadCase':
        '''SpiralBevelGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6156.SpiralBevelGearLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def system_deflection_results(self) -> '_2291.SpiralBevelGearSystemDeflection':
        '''SpiralBevelGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2291.SpiralBevelGearSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
