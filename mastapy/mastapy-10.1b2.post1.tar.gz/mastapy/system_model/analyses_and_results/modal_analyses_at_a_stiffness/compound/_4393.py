'''_4393.py

PointLoadCompoundModalAnalysisAtAStiffness
'''


from typing import List

from mastapy.system_model.part_model import _1990
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4272
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4427
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound', 'PointLoadCompoundModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('PointLoadCompoundModalAnalysisAtAStiffness',)


class PointLoadCompoundModalAnalysisAtAStiffness(_4427.VirtualComponentCompoundModalAnalysisAtAStiffness):
    '''PointLoadCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    '''

    TYPE = _POINT_LOAD_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PointLoadCompoundModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1990.PointLoad':
        '''PointLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1990.PointLoad)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def load_case_analyses_ready(self) -> 'List[_4272.PointLoadModalAnalysisAtAStiffness]':
        '''List[PointLoadModalAnalysisAtAStiffness]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_4272.PointLoadModalAnalysisAtAStiffness))
        return value

    @property
    def component_modal_analysis_at_a_stiffness_load_cases(self) -> 'List[_4272.PointLoadModalAnalysisAtAStiffness]':
        '''List[PointLoadModalAnalysisAtAStiffness]: 'ComponentModalAnalysisAtAStiffnessLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentModalAnalysisAtAStiffnessLoadCases, constructor.new(_4272.PointLoadModalAnalysisAtAStiffness))
        return value
