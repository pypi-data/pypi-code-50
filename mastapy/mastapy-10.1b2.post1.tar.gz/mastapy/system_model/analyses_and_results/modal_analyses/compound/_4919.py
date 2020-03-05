'''_4919.py

SpringDamperHalfCompoundModalAnalysis
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2112
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4780
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4860
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'SpringDamperHalfCompoundModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperHalfCompoundModalAnalysis',)


class SpringDamperHalfCompoundModalAnalysis(_4860.CouplingHalfCompoundModalAnalysis):
    '''SpringDamperHalfCompoundModalAnalysis

    This is a mastapy class.
    '''

    TYPE = _SPRING_DAMPER_HALF_COMPOUND_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpringDamperHalfCompoundModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2112.SpringDamperHalf':
        '''SpringDamperHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2112.SpringDamperHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def load_case_analyses_ready(self) -> 'List[_4780.SpringDamperHalfModalAnalysis]':
        '''List[SpringDamperHalfModalAnalysis]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_4780.SpringDamperHalfModalAnalysis))
        return value

    @property
    def component_modal_analysis_load_cases(self) -> 'List[_4780.SpringDamperHalfModalAnalysis]':
        '''List[SpringDamperHalfModalAnalysis]: 'ComponentModalAnalysisLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentModalAnalysisLoadCases, constructor.new(_4780.SpringDamperHalfModalAnalysis))
        return value
