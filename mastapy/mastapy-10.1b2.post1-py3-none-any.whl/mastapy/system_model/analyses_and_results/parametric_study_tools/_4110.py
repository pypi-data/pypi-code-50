'''_4110.py

FlexiblePinAssemblyParametricStudyTool
'''


from typing import List

from mastapy.system_model.part_model import _1930
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _2286
from mastapy.system_model.analyses_and_results.system_deflections import _2285
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4123
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'FlexiblePinAssemblyParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('FlexiblePinAssemblyParametricStudyTool',)


class FlexiblePinAssemblyParametricStudyTool(_4123.SpecialisedAssemblyParametricStudyTool):
    '''FlexiblePinAssemblyParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_PARAMETRIC_STUDY_TOOL
    __hash__ = None

    def __init__(self, instance_to_wrap: 'FlexiblePinAssemblyParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_1930.FlexiblePinAssembly':
        '''FlexiblePinAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1930.FlexiblePinAssembly)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_2286.FlexiblePinAssemblyLoadCase':
        '''FlexiblePinAssemblyLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2286.FlexiblePinAssemblyLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def assembly_system_deflection_results(self) -> 'List[_2285.FlexiblePinAssemblySystemDeflection]':
        '''List[FlexiblePinAssemblySystemDeflection]: 'AssemblySystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblySystemDeflectionResults, constructor.new(_2285.FlexiblePinAssemblySystemDeflection))
        return value
