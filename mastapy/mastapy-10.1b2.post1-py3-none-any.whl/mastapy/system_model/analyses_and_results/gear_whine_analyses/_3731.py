'''_3731.py

BoltedJointGearWhineAnalysis
'''


from mastapy.system_model.part_model import _1860
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _2313
from mastapy.system_model.analyses_and_results.system_deflections import _2155
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _3749
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'BoltedJointGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BoltedJointGearWhineAnalysis',)


class BoltedJointGearWhineAnalysis(_3749.SpecialisedAssemblyGearWhineAnalysis):
    '''BoltedJointGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _BOLTED_JOINT_GEAR_WHINE_ANALYSIS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'BoltedJointGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_1860.BoltedJoint':
        '''BoltedJoint: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1860.BoltedJoint)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_2313.BoltedJointLoadCase':
        '''BoltedJointLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2313.BoltedJointLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def system_deflection_results(self) -> '_2155.BoltedJointSystemDeflection':
        '''BoltedJointSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2155.BoltedJointSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None
