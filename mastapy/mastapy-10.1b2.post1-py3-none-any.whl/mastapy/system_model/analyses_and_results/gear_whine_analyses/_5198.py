'''_5198.py

PlanetCarrierGearWhineAnalysis
'''


from mastapy.system_model.part_model import _1934
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _5986
from mastapy.system_model.analyses_and_results.system_deflections import _2215
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _5192
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'PlanetCarrierGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetCarrierGearWhineAnalysis',)


class PlanetCarrierGearWhineAnalysis(_5192.MountableComponentGearWhineAnalysis):
    '''PlanetCarrierGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _PLANET_CARRIER_GEAR_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PlanetCarrierGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1934.PlanetCarrier':
        '''PlanetCarrier: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1934.PlanetCarrier)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_5986.PlanetCarrierLoadCase':
        '''PlanetCarrierLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5986.PlanetCarrierLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def system_deflection_results(self) -> '_2215.PlanetCarrierSystemDeflection':
        '''PlanetCarrierSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2215.PlanetCarrierSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
