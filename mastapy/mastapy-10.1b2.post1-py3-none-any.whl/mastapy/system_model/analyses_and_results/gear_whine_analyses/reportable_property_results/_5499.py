'''_5499.py

ResultsForOrder
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.gear_whine_analyses.reportable_property_results import (
    _5493, _5496, _5497, _5494
)
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_RESULTS_FOR_ORDER = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.ReportablePropertyResults', 'ResultsForOrder')


__docformat__ = 'restructuredtext en'
__all__ = ('ResultsForOrder',)


class ResultsForOrder(_1.APIBase):
    '''ResultsForOrder

    This is a mastapy class.
    '''

    TYPE = _RESULTS_FOR_ORDER

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ResultsForOrder.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def order(self) -> 'str':
        '''str: 'Order' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.Order

    @property
    def component(self) -> '_5493.GearWhineAnalysisResultsBrokenDownByComponentWithinAHarmonic':
        '''GearWhineAnalysisResultsBrokenDownByComponentWithinAHarmonic: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5493.GearWhineAnalysisResultsBrokenDownByComponentWithinAHarmonic)(self.wrapped.Component) if self.wrapped.Component else None

    @property
    def node_results_global_coordinate_system(self) -> 'List[_5496.GearWhineAnalysisResultsBrokenDownByNodeWithinAHarmonic]':
        '''List[GearWhineAnalysisResultsBrokenDownByNodeWithinAHarmonic]: 'NodeResultsGlobalCoordinateSystem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.NodeResultsGlobalCoordinateSystem, constructor.new(_5496.GearWhineAnalysisResultsBrokenDownByNodeWithinAHarmonic))
        return value

    @property
    def node_results_local_coordinate_system(self) -> 'List[_5496.GearWhineAnalysisResultsBrokenDownByNodeWithinAHarmonic]':
        '''List[GearWhineAnalysisResultsBrokenDownByNodeWithinAHarmonic]: 'NodeResultsLocalCoordinateSystem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.NodeResultsLocalCoordinateSystem, constructor.new(_5496.GearWhineAnalysisResultsBrokenDownByNodeWithinAHarmonic))
        return value

    @property
    def fe_surfaces(self) -> 'List[_5497.GearWhineAnalysisResultsBrokenDownBySurfaceWithinAHarmonic]':
        '''List[GearWhineAnalysisResultsBrokenDownBySurfaceWithinAHarmonic]: 'FESurfaces' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FESurfaces, constructor.new(_5497.GearWhineAnalysisResultsBrokenDownBySurfaceWithinAHarmonic))
        return value

    @property
    def groups(self) -> 'List[_5494.GearWhineAnalysisResultsBrokenDownByGroupsWithinAHarmonic]':
        '''List[GearWhineAnalysisResultsBrokenDownByGroupsWithinAHarmonic]: 'Groups' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Groups, constructor.new(_5494.GearWhineAnalysisResultsBrokenDownByGroupsWithinAHarmonic))
        return value
