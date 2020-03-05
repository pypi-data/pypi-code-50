'''_3816.py

OilSealGearWhineAnalysis
'''


from mastapy.system_model.part_model import _1939
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _2333
from mastapy.system_model.analyses_and_results.system_deflections import _2236
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _3806
from mastapy._internal.python_net import python_net_import

_OIL_SEAL_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'OilSealGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('OilSealGearWhineAnalysis',)


class OilSealGearWhineAnalysis(_3806.ConnectorGearWhineAnalysis):
    '''OilSealGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _OIL_SEAL_GEAR_WHINE_ANALYSIS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'OilSealGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1939.OilSeal':
        '''OilSeal: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1939.OilSeal)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_2333.OilSealLoadCase':
        '''OilSealLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2333.OilSealLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def system_deflection_results(self) -> '_2236.OilSealSystemDeflection':
        '''OilSealSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2236.OilSealSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
