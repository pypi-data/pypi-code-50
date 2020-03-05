'''_4124.py

UnbalancedMassParametricStudyTool
'''


from typing import List

from mastapy.system_model.part_model import _1948
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _2313
from mastapy.system_model.analyses_and_results.system_deflections import _2312
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4125
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'UnbalancedMassParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('UnbalancedMassParametricStudyTool',)


class UnbalancedMassParametricStudyTool(_4125.VirtualComponentParametricStudyTool):
    '''UnbalancedMassParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _UNBALANCED_MASS_PARAMETRIC_STUDY_TOOL
    __hash__ = None

    def __init__(self, instance_to_wrap: 'UnbalancedMassParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1948.UnbalancedMass':
        '''UnbalancedMass: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1948.UnbalancedMass)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_2313.UnbalancedMassLoadCase':
        '''UnbalancedMassLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2313.UnbalancedMassLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def component_system_deflection_results(self) -> 'List[_2312.UnbalancedMassSystemDeflection]':
        '''List[UnbalancedMassSystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentSystemDeflectionResults, constructor.new(_2312.UnbalancedMassSystemDeflection))
        return value
