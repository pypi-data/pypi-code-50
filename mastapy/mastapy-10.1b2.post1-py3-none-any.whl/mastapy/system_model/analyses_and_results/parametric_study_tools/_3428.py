'''_3428.py

MassDiscParametricStudyTool
'''


from typing import List

from mastapy.system_model.part_model import _1928
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _5976
from mastapy.system_model.analyses_and_results.system_deflections import _2207
from mastapy.system_model.analyses_and_results.parametric_study_tools import _3480
from mastapy._internal.python_net import python_net_import

_MASS_DISC_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'MassDiscParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('MassDiscParametricStudyTool',)


class MassDiscParametricStudyTool(_3480.VirtualComponentParametricStudyTool):
    '''MassDiscParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _MASS_DISC_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'MassDiscParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1928.MassDisc':
        '''MassDisc: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1928.MassDisc)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_5976.MassDiscLoadCase':
        '''MassDiscLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5976.MassDiscLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def planetaries(self) -> 'List[MassDiscParametricStudyTool]':
        '''List[MassDiscParametricStudyTool]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(MassDiscParametricStudyTool))
        return value

    @property
    def component_system_deflection_results(self) -> 'List[_2207.MassDiscSystemDeflection]':
        '''List[MassDiscSystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentSystemDeflectionResults, constructor.new(_2207.MassDiscSystemDeflection))
        return value
