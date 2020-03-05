'''_3504.py

HypoidGearSetParametricStudyTool
'''


from typing import List

from mastapy.system_model.part_model.gears import _2052
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6113
from mastapy.system_model.analyses_and_results.parametric_study_tools import _3503, _3502, _3445
from mastapy.system_model.analyses_and_results.system_deflections import _2250
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'HypoidGearSetParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearSetParametricStudyTool',)


class HypoidGearSetParametricStudyTool(_3445.AGMAGleasonConicalGearSetParametricStudyTool):
    '''HypoidGearSetParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _HYPOID_GEAR_SET_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearSetParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2052.HypoidGearSet':
        '''HypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2052.HypoidGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6113.HypoidGearSetLoadCase':
        '''HypoidGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6113.HypoidGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def hypoid_gears_parametric_study_tool(self) -> 'List[_3503.HypoidGearParametricStudyTool]':
        '''List[HypoidGearParametricStudyTool]: 'HypoidGearsParametricStudyTool' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearsParametricStudyTool, constructor.new(_3503.HypoidGearParametricStudyTool))
        return value

    @property
    def hypoid_meshes_parametric_study_tool(self) -> 'List[_3502.HypoidGearMeshParametricStudyTool]':
        '''List[HypoidGearMeshParametricStudyTool]: 'HypoidMeshesParametricStudyTool' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidMeshesParametricStudyTool, constructor.new(_3502.HypoidGearMeshParametricStudyTool))
        return value

    @property
    def assembly_system_deflection_results(self) -> 'List[_2250.HypoidGearSetSystemDeflection]':
        '''List[HypoidGearSetSystemDeflection]: 'AssemblySystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblySystemDeflectionResults, constructor.new(_2250.HypoidGearSetSystemDeflection))
        return value
