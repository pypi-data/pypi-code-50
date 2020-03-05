'''_5551.py

FaceGearCompoundGearWhineAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _1990
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _5161
from mastapy.system_model.analyses_and_results.gear_whine_analyses.compound import _5555
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_COMPOUND_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.Compound', 'FaceGearCompoundGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearCompoundGearWhineAnalysis',)


class FaceGearCompoundGearWhineAnalysis(_5555.GearCompoundGearWhineAnalysis):
    '''FaceGearCompoundGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _FACE_GEAR_COMPOUND_GEAR_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearCompoundGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1990.FaceGear':
        '''FaceGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1990.FaceGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def load_case_analyses_ready(self) -> 'List[_5161.FaceGearGearWhineAnalysis]':
        '''List[FaceGearGearWhineAnalysis]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_5161.FaceGearGearWhineAnalysis))
        return value

    @property
    def component_gear_whine_analysis_load_cases(self) -> 'List[_5161.FaceGearGearWhineAnalysis]':
        '''List[FaceGearGearWhineAnalysis]: 'ComponentGearWhineAnalysisLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentGearWhineAnalysisLoadCases, constructor.new(_5161.FaceGearGearWhineAnalysis))
        return value
