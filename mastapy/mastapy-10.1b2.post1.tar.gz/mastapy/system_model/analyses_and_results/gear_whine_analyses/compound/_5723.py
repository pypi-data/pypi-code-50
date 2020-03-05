'''_5723.py

PointLoadCompoundGearWhineAnalysis
'''


from typing import List

from mastapy.system_model.part_model import _1990
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _5332
from mastapy.system_model.analyses_and_results.gear_whine_analyses.compound import _5757
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_COMPOUND_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.Compound', 'PointLoadCompoundGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PointLoadCompoundGearWhineAnalysis',)


class PointLoadCompoundGearWhineAnalysis(_5757.VirtualComponentCompoundGearWhineAnalysis):
    '''PointLoadCompoundGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _POINT_LOAD_COMPOUND_GEAR_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PointLoadCompoundGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1990.PointLoad':
        '''PointLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1990.PointLoad)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def load_case_analyses_ready(self) -> 'List[_5332.PointLoadGearWhineAnalysis]':
        '''List[PointLoadGearWhineAnalysis]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_5332.PointLoadGearWhineAnalysis))
        return value

    @property
    def component_gear_whine_analysis_load_cases(self) -> 'List[_5332.PointLoadGearWhineAnalysis]':
        '''List[PointLoadGearWhineAnalysis]: 'ComponentGearWhineAnalysisLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentGearWhineAnalysisLoadCases, constructor.new(_5332.PointLoadGearWhineAnalysis))
        return value
