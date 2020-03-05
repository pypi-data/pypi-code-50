'''_3374.py

ClutchParametricStudyTool
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2036
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _5899
from mastapy.system_model.analyses_and_results.system_deflections import _2149
from mastapy.system_model.analyses_and_results.parametric_study_tools import _3390
from mastapy._internal.python_net import python_net_import

_CLUTCH_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'ClutchParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchParametricStudyTool',)


class ClutchParametricStudyTool(_3390.CouplingParametricStudyTool):
    '''ClutchParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _CLUTCH_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ClutchParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2036.Clutch':
        '''Clutch: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2036.Clutch)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_5899.ClutchLoadCase':
        '''ClutchLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5899.ClutchLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def assembly_system_deflection_results(self) -> 'List[_2149.ClutchSystemDeflection]':
        '''List[ClutchSystemDeflection]: 'AssemblySystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblySystemDeflectionResults, constructor.new(_2149.ClutchSystemDeflection))
        return value
