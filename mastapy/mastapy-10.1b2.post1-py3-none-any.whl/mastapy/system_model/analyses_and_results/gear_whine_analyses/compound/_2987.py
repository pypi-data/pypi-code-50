'''_2987.py

PulleyCompoundGearWhineAnalysis
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2024
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _3757
from mastapy.system_model.analyses_and_results.gear_whine_analyses.compound import _2984
from mastapy._internal.python_net import python_net_import

_PULLEY_COMPOUND_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.Compound', 'PulleyCompoundGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PulleyCompoundGearWhineAnalysis',)


class PulleyCompoundGearWhineAnalysis(_2984.CouplingHalfCompoundGearWhineAnalysis):
    '''PulleyCompoundGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _PULLEY_COMPOUND_GEAR_WHINE_ANALYSIS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'PulleyCompoundGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2024.Pulley':
        '''Pulley: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2024.Pulley)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def load_case_analyses_ready(self) -> 'List[_3757.PulleyGearWhineAnalysis]':
        '''List[PulleyGearWhineAnalysis]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_3757.PulleyGearWhineAnalysis))
        return value

    @property
    def component_gear_whine_analysis_load_cases(self) -> 'List[_3757.PulleyGearWhineAnalysis]':
        '''List[PulleyGearWhineAnalysis]: 'ComponentGearWhineAnalysisLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentGearWhineAnalysisLoadCases, constructor.new(_3757.PulleyGearWhineAnalysis))
        return value
