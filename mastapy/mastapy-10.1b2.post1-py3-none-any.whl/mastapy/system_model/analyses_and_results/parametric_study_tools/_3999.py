'''_3999.py

SpringDamperHalfParametricStudyTool
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2028
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _2264
from mastapy.system_model.analyses_and_results.system_deflections import _2263
from mastapy.system_model.analyses_and_results.parametric_study_tools import _3991
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'SpringDamperHalfParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperHalfParametricStudyTool',)


class SpringDamperHalfParametricStudyTool(_3991.CouplingHalfParametricStudyTool):
    '''SpringDamperHalfParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _SPRING_DAMPER_HALF_PARAMETRIC_STUDY_TOOL
    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpringDamperHalfParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2028.SpringDamperHalf':
        '''SpringDamperHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2028.SpringDamperHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_2264.SpringDamperHalfLoadCase':
        '''SpringDamperHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2264.SpringDamperHalfLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def component_system_deflection_results(self) -> 'List[_2263.SpringDamperHalfSystemDeflection]':
        '''List[SpringDamperHalfSystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentSystemDeflectionResults, constructor.new(_2263.SpringDamperHalfSystemDeflection))
        return value
