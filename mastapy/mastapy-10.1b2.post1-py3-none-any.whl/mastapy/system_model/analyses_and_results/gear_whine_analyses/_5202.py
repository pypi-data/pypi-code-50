'''_5202.py

RollingRingAssemblyGearWhineAnalysis
'''


from mastapy.system_model.part_model.couplings import _2052
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _5993
from mastapy.system_model.analyses_and_results.system_deflections import _2219
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _5210
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'RollingRingAssemblyGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('RollingRingAssemblyGearWhineAnalysis',)


class RollingRingAssemblyGearWhineAnalysis(_5210.SpecialisedAssemblyGearWhineAnalysis):
    '''RollingRingAssemblyGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _ROLLING_RING_ASSEMBLY_GEAR_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RollingRingAssemblyGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2052.RollingRingAssembly':
        '''RollingRingAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2052.RollingRingAssembly)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_5993.RollingRingAssemblyLoadCase':
        '''RollingRingAssemblyLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5993.RollingRingAssemblyLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def system_deflection_results(self) -> '_2219.RollingRingAssemblySystemDeflection':
        '''RollingRingAssemblySystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2219.RollingRingAssemblySystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
