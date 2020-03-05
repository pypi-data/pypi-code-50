'''_5338.py

RootAssemblyGearWhineAnalysis
'''


from mastapy.system_model.part_model import _1993
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _5300, _5236
from mastapy.system_model.analyses_and_results.system_deflections import _2282
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'RootAssemblyGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblyGearWhineAnalysis',)


class RootAssemblyGearWhineAnalysis(_5236.AssemblyGearWhineAnalysis):
    '''RootAssemblyGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _ROOT_ASSEMBLY_GEAR_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RootAssemblyGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_1993.RootAssembly':
        '''RootAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1993.RootAssembly)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def gear_whine_analysis_inputs(self) -> '_5300.GearWhineAnalysis':
        '''GearWhineAnalysis: 'GearWhineAnalysisInputs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5300.GearWhineAnalysis)(self.wrapped.GearWhineAnalysisInputs) if self.wrapped.GearWhineAnalysisInputs else None

    @property
    def system_deflection_results(self) -> '_2282.RootAssemblySystemDeflection':
        '''RootAssemblySystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2282.RootAssemblySystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
