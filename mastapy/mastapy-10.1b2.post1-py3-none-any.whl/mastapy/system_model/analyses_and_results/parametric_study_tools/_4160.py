'''_4160.py

StraightBevelGearSetParametricStudyTool
'''


from typing import List

from mastapy.system_model.part_model.gears import _2017
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _2373
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4159, _4097, _4138
from mastapy.system_model.analyses_and_results.system_deflections import _2372
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'StraightBevelGearSetParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearSetParametricStudyTool',)


class StraightBevelGearSetParametricStudyTool(_4138.BevelGearSetParametricStudyTool):
    '''StraightBevelGearSetParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_PARAMETRIC_STUDY_TOOL
    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelGearSetParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2017.StraightBevelGearSet':
        '''StraightBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2017.StraightBevelGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_2373.StraightBevelGearSetLoadCase':
        '''StraightBevelGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2373.StraightBevelGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def straight_bevel_gears_parametric_study_tool(self) -> 'List[_4159.StraightBevelGearParametricStudyTool]':
        '''List[StraightBevelGearParametricStudyTool]: 'StraightBevelGearsParametricStudyTool' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearsParametricStudyTool, constructor.new(_4159.StraightBevelGearParametricStudyTool))
        return value

    @property
    def straight_bevel_meshes_parametric_study_tool(self) -> 'List[_4097.StraightBevelGearMeshParametricStudyTool]':
        '''List[StraightBevelGearMeshParametricStudyTool]: 'StraightBevelMeshesParametricStudyTool' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelMeshesParametricStudyTool, constructor.new(_4097.StraightBevelGearMeshParametricStudyTool))
        return value

    @property
    def assembly_system_deflection_results(self) -> 'List[_2372.StraightBevelGearSetSystemDeflection]':
        '''List[StraightBevelGearSetSystemDeflection]: 'AssemblySystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblySystemDeflectionResults, constructor.new(_2372.StraightBevelGearSetSystemDeflection))
        return value
