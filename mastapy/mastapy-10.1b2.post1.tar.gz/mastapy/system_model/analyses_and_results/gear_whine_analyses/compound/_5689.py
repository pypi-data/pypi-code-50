'''_5689.py

ExternalCADModelCompoundGearWhineAnalysis
'''


from typing import List

from mastapy.system_model.part_model import _1974
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _5290
from mastapy.system_model.analyses_and_results.gear_whine_analyses.compound import _5666
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_COMPOUND_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.Compound', 'ExternalCADModelCompoundGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ExternalCADModelCompoundGearWhineAnalysis',)


class ExternalCADModelCompoundGearWhineAnalysis(_5666.ComponentCompoundGearWhineAnalysis):
    '''ExternalCADModelCompoundGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _EXTERNAL_CAD_MODEL_COMPOUND_GEAR_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ExternalCADModelCompoundGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1974.ExternalCADModel':
        '''ExternalCADModel: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1974.ExternalCADModel)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def load_case_analyses_ready(self) -> 'List[_5290.ExternalCADModelGearWhineAnalysis]':
        '''List[ExternalCADModelGearWhineAnalysis]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_5290.ExternalCADModelGearWhineAnalysis))
        return value

    @property
    def component_gear_whine_analysis_load_cases(self) -> 'List[_5290.ExternalCADModelGearWhineAnalysis]':
        '''List[ExternalCADModelGearWhineAnalysis]: 'ComponentGearWhineAnalysisLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentGearWhineAnalysisLoadCases, constructor.new(_5290.ExternalCADModelGearWhineAnalysis))
        return value
