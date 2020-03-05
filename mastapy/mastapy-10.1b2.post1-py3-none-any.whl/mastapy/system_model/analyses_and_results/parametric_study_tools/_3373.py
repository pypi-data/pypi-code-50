'''_3373.py

ClutchHalfParametricStudyTool
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2037
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _5898
from mastapy.system_model.analyses_and_results.system_deflections import _2148
from mastapy.system_model.analyses_and_results.parametric_study_tools import _3389
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'ClutchHalfParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchHalfParametricStudyTool',)


class ClutchHalfParametricStudyTool(_3389.CouplingHalfParametricStudyTool):
    '''ClutchHalfParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _CLUTCH_HALF_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ClutchHalfParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2037.ClutchHalf':
        '''ClutchHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2037.ClutchHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_5898.ClutchHalfLoadCase':
        '''ClutchHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5898.ClutchHalfLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def component_system_deflection_results(self) -> 'List[_2148.ClutchHalfSystemDeflection]':
        '''List[ClutchHalfSystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentSystemDeflectionResults, constructor.new(_2148.ClutchHalfSystemDeflection))
        return value
