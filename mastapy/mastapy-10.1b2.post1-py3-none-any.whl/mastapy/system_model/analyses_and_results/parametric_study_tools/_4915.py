'''_4915.py

DutyCycleResultsForAllComponents
'''


from typing import List

from mastapy.system_model.analyses_and_results.parametric_study_tools import _4916, _4917, _4918
from mastapy._internal import constructor, conversion
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_DUTY_CYCLE_RESULTS_FOR_ALL_COMPONENTS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'DutyCycleResultsForAllComponents')


__docformat__ = 'restructuredtext en'
__all__ = ('DutyCycleResultsForAllComponents',)


class DutyCycleResultsForAllComponents(_1.APIBase):
    '''DutyCycleResultsForAllComponents

    This is a mastapy class.
    '''

    TYPE = _DUTY_CYCLE_RESULTS_FOR_ALL_COMPONENTS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'DutyCycleResultsForAllComponents.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def results_for_all_gear_sets(self) -> '_4916.DutyCycleResultsForAllGearSets':
        '''DutyCycleResultsForAllGearSets: 'ResultsForAllGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_4916.DutyCycleResultsForAllGearSets)(self.wrapped.ResultsForAllGearSets) if self.wrapped.ResultsForAllGearSets else None

    @property
    def results_for_all_bearings(self) -> 'List[_4917.DutyCycleResultsForSingleBearing]':
        '''List[DutyCycleResultsForSingleBearing]: 'ResultsForAllBearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ResultsForAllBearings, constructor.new(_4917.DutyCycleResultsForSingleBearing))
        return value

    @property
    def results_for_all_shafts(self) -> 'List[_4918.DutyCycleResultsForSingleShaft]':
        '''List[DutyCycleResultsForSingleShaft]: 'ResultsForAllShafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ResultsForAllShafts, constructor.new(_4918.DutyCycleResultsForSingleShaft))
        return value
